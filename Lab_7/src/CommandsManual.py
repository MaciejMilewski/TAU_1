class CommandsManual:
    driver = ""
    manual = {}

    def __init__(self, driver):
        driver_lower = driver.lower()

        if driver_lower != "windows" and driver_lower != "linux":
            raise Exception("No driver for" + driver_lower + " system.")

        self.driver = driver_lower

        if self.driver == "windows":
            self.manual = {
                "dir": {
                    "": "displays a list of a directory's files and subdirectories",
                    "/p": "displays one screen of the listing at a time. To see the next screen, press any key",
                    "/q": "displays file ownership information"
                },
                "fc": {
                    "": "performs either an ascii or a binary file comparison and will"
                        " list all of the differences that it finds",
                    "/a": 'compare ascii of files',
                    "/b": 'binary comparison of two images'
                },
                "where": {
                    "": "Displays the location of files that match the given search pattern",
                    "/t": "Displays the file size and the last modified date and time of each matched file",
                    "/f": "Displays the results of the where command in quotation marks"
                },
                "netstat": {
                    "": "Displays active TCP connections, ports on which the computer is listening, Ethernet statistics,"
                        " the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols),"
                        " and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols)."
                        " Used without parameters, this command displays active TCP connections.",
                    "/a": "Displays all active TCP connections and the TCP and UDP ports"
                          " on which the computer is listening.",
                    "/n": "Displays active TCP connections, however, addresses and port numbers are"
                          " expressed numerically and no attempt is made to determine names."
                },
                "cd": {
                    "": "Displays the name of the current directory or"
                        " changes the current directory to given path, cd <path>",
                    "/d": 'Changes the current drive as well as the current directory for a drive.',
                    "..": "Leave current directory."
                }
            }

        elif self.driver == "linux":
            self.manual = {
                "ls": {
                    "": "lists directory contents of files and directories",
                    "-s": "list file size",
                    "-l": "show permissions"
                },
                "cp": {
                    "": "copy files and directories, cp [options] source dest",
                    "-R": "recursive copy",
                    "-l": "creates link to file/files instead of copying"
                },
                "tail": {
                    "": "display the last ten lines of a text file, tail [OPTION]... [FILE]...",
                    "-n": "diplay x last lines, if number is not given then 10 last lines",
                    "-c": "diplay x last bytes, if number is not given then 10 last bytes"
                },
                'diff': {
                    "": "compares files line by line, diff [OPTION]... FILES",
                    "-q": "report only when files differ",
                    "-s": "report when two files are the same"
                },
                "mkdir": {
                    "": "make directories, mkdir [OPTION]... DIRECTORY...",
                    "-p": "no error if existing, make parent directories as needed",
                    "-v": "print a message for each created directory"
                }
            }

    def show_command_manual(self, command, parameter):
        command = command.lower()
        parameter = parameter.lower()

        if command not in self.manual:
            return None

        if parameter.upper() in self.manual[command]:
            return str(command + " " + parameter.upper() + ": " + self.manual[command][parameter.upper()])
        elif parameter not in self.manual[command]:
            return str("Brak instrukcji dla parametru " + parameter + " dla komendy " + command)

        return str(command + " " + parameter + ": " + self.manual[command][parameter])
