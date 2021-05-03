from src.CommandsManual import CommandsManual


class TestLinuxCommandsManual:
    linux_commands_manual = CommandsManual("linux")

    def test_not_existing_command(self):
        result = self.linux_commands_manual.show_command_manual("aXgHHi", "")
        assert result is None

    def test_bad_parameter_correct_command(self):
        result = self.linux_commands_manual.show_command_manual("ls", "krkrk")
        expected_result = "Brak instrukcji dla parametru krkrk dla komendy ls"
        assert result == expected_result

    def test_existing_parameter_bad_command(self):
        result = self.linux_commands_manual.show_command_manual("aXgHHi", "/a")
        assert result is None

    def test_upper_letters_parameter(self):
        result = self.linux_commands_manual.show_command_manual("ls", "-S")
        expected_result = "ls -s: list file size"
        assert result == expected_result

    def test_ls_no_parameter(self):
        result = self.linux_commands_manual.show_command_manual("ls", "")
        expected_result = "ls : lists directory contents of files and directories"
        assert result == expected_result

    def test_ls_parameter_s(self):
        result = self.linux_commands_manual.show_command_manual("ls", "-s")
        expected_result = "ls -s: list file size"
        assert result == expected_result

    def test_ls_parameter_l(self):
        result = self.linux_commands_manual.show_command_manual("ls", "-l")
        expected_result = "ls -l: show permissions"
        assert result == expected_result

    def test_cp_no_parameter(self):
        result = self.linux_commands_manual.show_command_manual("cp", "")
        expected_result = "cp : copy files and directories, cp [options] source dest"
        assert result == expected_result

    def test_cp_parameter_R(self):
        result = self.linux_commands_manual.show_command_manual("cp", "-R")
        expected_result = "cp -R: recursive copy"
        assert result == expected_result

    def test_cp_parameter_l(self):
        result = self.linux_commands_manual.show_command_manual("cp", "-l")
        expected_result = "cp -l: creates link to file/files instead of copying"
        assert result == expected_result

    def test_tail_no_parameter(self):
        result = self.linux_commands_manual.show_command_manual("tail", "")
        expected_result = "tail : display the last ten lines of a text file, tail [OPTION]... [FILE]..."
        assert result == expected_result

    def test_tail_parameter_n(self):
        result = self.linux_commands_manual.show_command_manual("tail", "-n")
        expected_result = "tail -n: diplay x last lines, if number is not given then 10 last lines"
        assert result == expected_result

    def test_tail_parameter_c(self):
        result = self.linux_commands_manual.show_command_manual("tail", "-c")
        expected_result = "tail -c: diplay x last bytes, if number is not given then 10 last bytes"
        assert result == expected_result

    def test_diff_no_parameter(self):
        result = self.linux_commands_manual.show_command_manual("diff", "")
        expected_result = "diff : compares files line by line, diff [OPTION]... FILES"
        assert result == expected_result

    def test_diff_parameter_q(self):
        result = self.linux_commands_manual.show_command_manual("diff", "-q")
        expected_result = "diff -q: report only when files differ"
        assert result == expected_result

    def test_diff_parameter_s(self):
        result = self.linux_commands_manual.show_command_manual("diff", "-s")
        expected_result = "diff -s: report when two files are the same"
        assert result == expected_result

    def test_mkdir_no_parameter(self):
        result = self.linux_commands_manual.show_command_manual("mkdir", "")
        expected_result = "mkdir : make directories, mkdir [OPTION]... DIRECTORY..."
        assert result == expected_result

    def test_mkdir_parameter_p(self):
        result = self.linux_commands_manual.show_command_manual("mkdir", "-p")
        expected_result = "mkdir -p: no error if existing, make parent directories as needed"
        assert result == expected_result

    def test_mkdir_parameter_v(self):
        result = self.linux_commands_manual.show_command_manual("mkdir", "-v")
        expected_result = "mkdir -v: print a message for each created directory"
        assert result == expected_result

    def test_mkdir_incorrect_parameter(self):
        result = self.linux_commands_manual.show_command_manual("mkdir", "DvIVD")
        expected_result = "Brak instrukcji dla parametru dvivd dla komendy mkdir"
        assert result == expected_result
