# we start dir fuzzing just basic not the recursive and extenstion stuff 
# basic dir 

import subprocess
from wordlist import print_separator

def directory_fuzzing(target_input, word_list):
    '''
    Basic dir fuzzing like, 19.10.10.10/fuzz
    '''
    print_separator(" 🚀 Starting Directory Fuzzing... ")
    file_size_filter = input("📏 Enter file size to filter out (or press Enter to skip): ")
    error_code_filter = input("🚫 Enter error code to filter out (or press Enter to skip): ")
    response_codes = input("✅ Enter response codes to match (e.g., 200, 303) (or press Enter to skip): ")

    #bare basic
    fuzz_commands = [
        "ffuf",
        "-w", word_list,
        "-u",f"http://{target_input}/FUZZ"
    ]

    #special features more to be added 
    if file_size_filter:
        fuzz_commands.extend(["-fs", file_size_filter])
    if error_code_filter:
        fuzz_commands.extend(["-mc", f"!{error_code_filter}"])
    if file_size_filter:
        fuzz_commands.extend(["-fs", file_size_filter])
    if response_codes:
        fuzz_commands.extend(["-mc", response_codes])

    print(f"\n🔍 Running fuzzing on: {target_input}")
    print(f"📂 Using wordlist: {word_list}")
    print(f"🛠️ Command: {' '.join(fuzz_commands)}\n")

    #execute the command 
    dir_fuzz_process = subprocess.run(fuzz_commands, capture_output=True, text=True)

    print("🔵 Fuzzing Output:\n", dir_fuzz_process.stdout)

    if dir_fuzz_process.returncode == 0:
        print("✅ Fuzzing Completed Successfully!")
    else:
        print("❌ Fuzzing Failed! Check errors below.")
        print("🔴 Error:", dir_fuzz_process.stderr)

