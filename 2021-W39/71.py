class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")
        final_directories = []
        for d in directories:
            if d in ("", "."):
                continue
            elif d == "..":
                final_directories = final_directories[:-1]
            else:
                final_directories.append(d)
        return "/" + "/".join(final_directories)
