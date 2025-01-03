def checkInclusion(s1, s2):
    # Lengths of the strings
    len_s1, len_s2 = len(s1), len(s2)

    # If s1 is longer than s2, it's impossible for s2 to contain a permutation of s1
    if len_s1 > len_s2:
        return False

    # Frequency count of characters in s1
    s1_count = [0] * 26
    window_count = [0] * 26

    # Fill the initial counts for s1 and the first window of s2
    for i in range(len_s1):
        s1_count[ord(s1[i]) - ord('a')] += 1
        window_count[ord(s2[i]) - ord('a')] += 1

    # Check all windows in s2
    for i in range(len_s2 - len_s1):
        if s1_count == window_count:  # Check if the current window matches s1's count
            return True

        # Slide the window: remove the left character and add the right character
        window_count[ord(s2[i]) - ord('a')] -= 1
        window_count[ord(s2[i + len_s1]) - ord('a')] += 1

    # Check the last window
    return s1_count == window_count

# Example usage:
s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))  # Output: True
