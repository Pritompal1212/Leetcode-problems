def checkAttendanceRecord(s):
    # Condition 1: Check if 'A' appears fewer than 2 times
    if s.count('A') >= 2:
        return False

    # Condition 2: Check if 'LLL' (3 consecutive 'L') appears in the string
    if 'LLL' in s:
        return False

    # If both conditions are satisfied
    return True

# Example inputs
s1 = "PPALLP"  # Valid record
s2 = "PPALLL"  # Invalid record (3 consecutive 'L')
s3 = "PPAAP"   # Invalid record (2 'A's)

print(checkAttendanceRecord(s1))  # Output: True
print(checkAttendanceRecord(s2))  # Output: False
print(checkAttendanceRecord(s3))  # Output: False
