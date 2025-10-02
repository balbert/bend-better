#    In Python, there are multiple ways to extract the filename and path components
#    from a given file path, primarily using the os.path module or the pathlib module.
#
#    Using os.path:
#
#    The os.path module provides functions for path manipulation.
#
#    Get the filename (with extension).
#
#        import os
#
#        file_path = "/home/user/documents/my_file.txt"
#        filename = os.path.basename(file_path)
#        print(filename)
#        # Output: my_file.txt
#
#    Get the directory path.
#
#        import os
#
#        file_path = "/home/user/documents/my_file.txt"
#        directory_path = os.path.dirname(file_path)
#        print(directory_path)
#        # Output: /home/user/documents
#
#    Split the path into directory and filename:
#
#        import os
#
#        file_path = "/home/user/documents/my_file.txt"
#        directory, filename = os.path.split(file_path)
#        print(f"Directory: {directory}, Filename: {filename}")
#        # Output: Directory: /home/user/documents, Filename: my_file.txt
#
#    Get the filename without the extension.
#
#        import os
#
#        file_path = "/home/user/documents/my_file.txt"
#        filename_with_ext = os.path.basename(file_path)
#        filename_without_ext, extension = os.path.splitext(filename_with_ext)
#        print(filename_without_ext)
#        # Output: my_file
#
#
#    Using pathlib (Python 3.4+):
#
#    The pathlib module offers an object-oriented approach to path manipulation.
#
#    Get the filename (with extension).
#
#        from pathlib import Path
#
#        file_path = Path("/home/user/documents/my_file.txt")
#        filename = file_path.name
#        print(filename)
#        # Output: my_file.txt
#
#    Get the directory path.
#
#        from pathlib import Path
#
#        file_path = Path("/home/user/documents/my_file.txt")
#        directory_path = file_path.parent
#        print(directory_path)
#        # Output: /home/user/documents
#
#    Get the filename without the extension.
#
#        from pathlib import Path
#
#        file_path = Path("/home/user/documents/my_file.txt")
#        filename_without_ext = file_path.stem
#        print(filename_without_ext)
#        # Output: my_file
#
#    Get the file extension.
#
#        from pathlib import Path
#
#        file_path = Path("/home/user/documents/my_file.txt")
#        extension = file_path.suffix
#        print(extension)
#        # Output: .txt
#
#    Getting the path of the current script:
#
#    The __file__ special attribute can be used to get the path of the current Python script.
#
#        import os
#        from pathlib import Path
#
#        # Using os.path
#        current_script_path_os = os.path.abspath(__file__)
#        print(f"Current script path (os.path): {current_script_path_os}")
#
#        # Using pathlib
#        current_script_path_pathlib = Path(__file__).resolve()
#        print(f"Current script path (pathlib): {current_script_path_pathlib}")
