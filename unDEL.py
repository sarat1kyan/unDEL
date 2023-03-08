import os
import shutil
import subprocess
import magic
import paramiko

from typing import List


class RecoveredFile:
    def __init__(self, path: str, content: bytes):
        self.path = path
        self.content = content


class FileRecovery:
    def __init__(self, preview: bool = False, types: List[str] = None, recursive: bool = False):
        self.preview = preview
        self.types = types
        self.recursive = recursive
        self.recovered_files = []

    def recover_file(self, file_path: str) -> List[RecoveredFile]:
       
        if os.path.exists(file_path):
            # Check if file is of specified type(s)
            if self.types:
                file_type = magic.from_file(file_path, mime=True)
                if not any(file_type.startswith(file_type) for file_type in self.types):
                    return self.recovered_files

            # Recover file from local file system
            recovered_file_path = os.path.basename(file_path)
            with open(file_path, 'rb') as f:
                file_data = f.read()

        elif file_path.startswith("http") or file_path.startswith("https"):
            # Recover file from remote server
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname, port, username, password)
            sftp = ssh.open_sftp()
            remote_file_path = os.path.basename(file_path)
            sftp.get(file_path, remote_file_path)
            sftp.close()
            ssh.close()

            recovered_file_path = remote_file_path
            with open(recovered_file_path, 'rb') as f:
                file_data = f.read()

        elif os.path.exists(disk_image_path):
            # Recover file from disk image
            if disk_image_path.endswith('.iso'):
                # Mount disk image as loop device
                mount_dir = '/mnt/{}'.format(os.path.basename(disk_image_path))
                os.makedirs(mount_dir, exist_ok=True)
                subprocess.run(['sudo', 'mount', '-o', 'loop', disk_image_path, mount_dir])

                # Recover file from mounted file system
                recovered_file_path = os.path.join(mount_dir, os.path.basename(file_path))
                with open(recovered_file_path, 'rb') as f:
                    file_data = f.read()

                # Unmount loop device
                subprocess.run(['sudo', 'umount', mount_dir])
                os.rmdir(mount_dir)

            else:
                # Create disk image mount point
                mount_dir = '/mnt/{}'.format(os.path.basename(disk_image_path))
                os.makedirs(mount_dir, exist_ok=True)

                # Mount disk image to mount point
                subprocess.run(['sudo', 'mount', disk_image_path, mount_dir])

                # Recover file from mounted file system
                recovered_file_path = os.path.join(mount_dir, os.path.basename(file_path))
                with open(recovered_file_path, 'rb') as f:
                    file_data = f.read()

                # Unmount disk image
                subprocess.run(['sudo', 'umount', mount_dir])
                os.rmdir(mount_dir)

        else:
            return self.recovered_files

        # Save recovered file
        if not os.path.exists(recovered_file_path):
            with open(recovered_file_path, 'wb') as f:
                f.write(file_data)

            # Preview contents of recovered file
            if self.preview:
                print(f"Recovered contents of {recovered_file_path}:")
                print(file_data)

            self.recovered_files.append(RecoveredFile(recovered_file_path, file_data))

        return self.recovered_files

    def recover_directory(self, directory_path: str) -> List[RecoveredFile]:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)

                if self.recursive and os.path.isdir(file_path):
                    self.recover_directory(file_path)
                else:
                    self.recover_file(file_path)

        return self.recovered_files
