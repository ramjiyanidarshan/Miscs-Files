#!/bin/bash

# Define a function to convert a string to keypad numbers
string_to_keypad_number() {
  local input_string="$1"
  local result=""
  
  # Define keypad mappings
  declare -A keypad_mapping
  keypad_mapping=( 
    [1]="~\`!@#$%^&*()-_+={}[]|\\:;\"'<,.>?/" [2]="ABC" [3]="DEF" [4]="GHI" 
    [5]="JKL" [6]="MNO" [7]="PQRS" [8]="TUV" 
    [9]="WXYZ" [0]=" " 
  )
  
  # Loop through each character in the input string
  for (( i=0; i<${#input_string}; i++ )); do
    char="${input_string:i:1}"
    char_upper=$(echo "$char" | tr '[:lower:]' '[:upper:]') # Convert to uppercase
    
    # Find the corresponding number for the character
    found=false
    for key in "${!keypad_mapping[@]}"; do
      if [[ "${keypad_mapping[$key]}" == *"$char_upper"* ]]; then
        result+="$key"
        found=true
        break
      fi
    done
    
    # Append non-mapped characters as-is
    if [[ "$found" == false ]]; then
      result+="$char"
    fi
  done
  
  echo "$result"
}

# Main script to process input
if [[ -z "$1" ]]; then
  echo "Usage: $0 <string>"
  exit 1
fi

input_string="$1"
output=$(string_to_keypad_number "$input_string")
echo "The keypad number for '$input_string' is: $output"
