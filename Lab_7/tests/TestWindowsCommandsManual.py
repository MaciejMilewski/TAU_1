from src.CommandsManual import CommandsManual


class TestWindowsCommandsManual:
    windows_commands_manual = CommandsManual("windows")

    def test_not_existing_command(self):
        result = self.windows_commands_manual.show_command_manual("aXgHHi", "")
        assert result is None

    def test_bad_parameter_correct_command(self):
        result = self.windows_commands_manual.show_command_manual("where", "/t")
        expected_result = "where /t: Displays the file size and the last modified date and time of each matched file"
        assert result == expected_result

    def test_existing_parameter_bad_command(self):
        result = self.windows_commands_manual.show_command_manual("aXgHHi", "/a")
        assert result is None

    def test_netstat_upper_case_letters(self):
        result = self.windows_commands_manual.show_command_manual("NETSTAT", "")
        expected_result = "netstat : Displays active TCP connections, ports on which the computer is listening, Ethernet statistics," \
                          " the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols)," \
                          " and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols)." \
                          " Used without parameters, this command displays active TCP connections."
        assert result == expected_result

    def test_upper_letters_parameter(self):
        result = self.windows_commands_manual.show_command_manual("fc", "/A")
        expected_result = "fc /a: compare ascii of files"
        assert result == expected_result

    def test_fc_no_parameter(self):
        result = self.windows_commands_manual.show_command_manual("fc", "")
        expected_result = "fc : performs either an ascii or a binary file comparison and will list all of the differences that it finds"
        assert result == expected_result

    def test_fc_lower_letters(self):
        result = self.windows_commands_manual.show_command_manual("fc", "")
        expected_result = "fc : performs either an ascii or a binary file comparison and will list all of the differences that it finds"
        assert result == expected_result

    def test_fc_parameter_a(self):
        result = self.windows_commands_manual.show_command_manual("fc", "/a")
        expected_result = "fc /a: compare ascii of files"
        assert result == expected_result

    def test_fc_parameter_b(self):
        result = self.windows_commands_manual.show_command_manual("fc", "/b")
        expected_result = "fc /b: binary comparison of two images"
        assert result == expected_result

    def test_where_no_parameter(self):
        result = self.windows_commands_manual.show_command_manual("where", "")
        expected_result = "where : Displays the location of files that match the given search pattern"
        assert result == expected_result

    def test_where_parameter_t(self):
        result = self.windows_commands_manual.show_command_manual("where", "/t")
        expected_result = "where /t: Displays the file size and the last modified date and time of each matched file"
        assert result == expected_result

    def test_where_parameter_f(self):
        result = self.windows_commands_manual.show_command_manual("where", "/f")
        expected_result = "where /f: Displays the results of the where command in quotation marks"
        assert result == expected_result

    def test_netstat_no_parameter(self):
        result = self.windows_commands_manual.show_command_manual("netstat", "")
        expected_result = "netstat : Displays active TCP connections, ports on which the computer is listening, Ethernet statistics, the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols), and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols). Used without parameters, this command displays active TCP connections."
        assert result == expected_result

    def test_netstat_parameter_a(self):
        result = self.windows_commands_manual.show_command_manual("netstat", "/a")
        expected_result = "netstat /a: Displays all active TCP connections and the TCP and UDP ports on which the computer is listening."
        assert result == expected_result

    def test_netstat_parameter_n(self):
        result = self.windows_commands_manual.show_command_manual("netstat", "/n")
        expected_result = "netstat /n: Displays active TCP connections, however, addresses and port numbers are expressed numerically and no attempt is made to determine names."
        assert result == expected_result

    def test_cd_no_parameter(self):
        result = self.windows_commands_manual.show_command_manual("cd", "")
        expected_result = "cd : Displays the name of the current directory or changes the current directory to given path, cd <path>"
        assert result == expected_result

    def test_cd_parameter_d(self):
        result = self.windows_commands_manual.show_command_manual("cd", "/d")
        expected_result = "cd /d: Changes the current drive as well as the current directory for a drive."
        assert result == expected_result

    def test_cd_parameter_dot_dot(self):
        result = self.windows_commands_manual.show_command_manual("cd", "..")
        expected_result = "cd ..: Leave current directory."
        assert result == expected_result

    def test_cd_incorrect_parameter(self):
        result = self.windows_commands_manual.show_command_manual("cd", "TRtutu")
        expected_result = "Brak instrukcji dla parametru trtutu dla komendy cd"
        assert result == expected_result
