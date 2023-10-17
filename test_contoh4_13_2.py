from contoh4_13 import *
import pytest
import builtins
import io
import sys

# We need to simulate user input for the tests
def mock_input(prompt):
    return "3"

def test_dpt_pilihan_pengguna_valid(monkeypatch):
    # We use monkeypatch to replace the input function with our mock_input
    monkeypatch.setattr(builtins, 'input', mock_input)

    noPilihan = dpt_pilihan_pengguna()
    
    assert noPilihan == 3

def test_dpt_pilihan_pengguna_invalid_then_valid(monkeypatch):
    # Simulate two inputs: 0 (invalid) and then 4 (valid)
    input_values = ["0", "4"]

    def mock_input(prompt):
        return input_values.pop(0)

    monkeypatch.setattr(builtins, 'input', mock_input)

    noPilihan = dpt_pilihan_pengguna()
    
    assert noPilihan == 4

# We need to simulate user input for the tests
def mock_input2(prompt):
    return "5"

def test_dpt_dua_nombor(monkeypatch):
    # We use monkeypatch to replace the input function with our mock_input
    monkeypatch.setattr(builtins, 'input', mock_input2)
    
    # Now we can call the function and check if it returns the expected values
    nombor1, nombor2 = dpt_dua_nombor()
    
    assert nombor1 == 5
    assert nombor2 == 5

def test_menu(capsys):
    # Capture the standard output
    with io.StringIO() as captured_output:
        sys.stdout = captured_output

        # Call the menu function
        menu()

        # Get the captured output
        captured = captured_output.getvalue()

    # Check if the menu was printed as expected
    expected_output = """Kalkulator bermenu
1. Tambah
2. Tolak
3. Darab
4. Bahagi
5. Tamat
"""

    assert captured == expected_output

    # Restore the standard output
    sys.stdout = sys.__stdout__

def test_kira_cetak_tambah(capsys):
    with io.StringIO() as captured_output:
        sys.stdout = captured_output

        kira_cetak(1, 5, 3)  # Tambah

        captured = captured_output.getvalue()

    expected_output = "Output: 5 + 3 = 8\n\n"
    assert captured == expected_output

    sys.stdout = sys.__stdout__

def test_kira_cetak_tolak(capsys):
    with io.StringIO() as captured_output:
        sys.stdout = captured_output

        kira_cetak(2, 10, 4)  # Tolak

        captured = captured_output.getvalue()

    expected_output = "Output: 10 - 4 = 6\n\n"
    assert captured == expected_output

    sys.stdout = sys.__stdout__

# Add similar tests for Darab (3) and Bahagi (4) cases

def test_kira_cetak_darab(capsys):
    with io.StringIO() as captured_output:
        sys.stdout = captured_output

        kira_cetak(3, 7, 2)  # Darab

        captured = captured_output.getvalue()

    expected_output = "Output: 7 * 2 = 14\n\n"
    assert captured == expected_output

    sys.stdout = sys.__stdout__

def test_kira_cetak_bahagi(capsys):
    with io.StringIO() as captured_output:
        sys.stdout = captured_output

        kira_cetak(4, 16, 4)  # Bahagi

        captured = captured_output.getvalue()

    expected_output = "Output: 16 / 4 = 4.0\n\n"
    assert captured == expected_output

    sys.stdout = sys.__stdout__
