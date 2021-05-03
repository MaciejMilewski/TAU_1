import pytest
from src.CommandsManual import CommandsManual


class TestWindowsCommandsManual:
    def test_before_start(self):
        hasattr(CommandsManual, 'driver')
        hasattr(CommandsManual, 'manual')

    def test_after_start(self):
        commands_manual = CommandsManual("windows")
        assert commands_manual.driver == "windows"
        assert commands_manual.manual != {}

    def test_driver_windows(self):
        commands_manual = CommandsManual("windows")
        assert commands_manual.driver == "windows"

    def test_driver_linux(self):
        commands_manual = CommandsManual("linux")
        assert commands_manual.driver == "linux"

    def test_incorrect_driver(self):
        with pytest.raises(Exception):
            CommandsManual("DhkbsdbKHD")

    def test_incorrect_data_type_for_driver(self):
        with pytest.raises(Exception):
            CommandsManual(["DhkbsdbKHD", "DhkbsdbKHD"])

    def test_no_driver(self):
        with pytest.raises(Exception):
            CommandsManual("")
