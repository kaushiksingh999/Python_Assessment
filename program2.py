def decode_the_ring(s: str, p: str) -> bool:
    m_ptr = 0  # Pointer for the message `s`
    p_ptr = 0  # Pointer for the pattern `p`
    star_idx = -1  # The position of the last '*' in the pattern
    match = 0  # The position in the message `s` to resume after a star

    while m_ptr < len(s):
        # If characters match or pattern has '?', advance both pointers
        if p_ptr < len(p) and (p[p_ptr] == s[m_ptr] or p[p_ptr] == '?'):
            m_ptr += 1
            p_ptr += 1
        # If pattern has '*', mark the position and try to match the rest
        elif p_ptr < len(p) and p[p_ptr] == '*':
            star_idx = p_ptr
            match = m_ptr
            p_ptr += 1  # Move pattern pointer to the next character after '*'
        # If no match, backtrack to the last '*' and try matching more characters
        elif star_idx != -1:
            p_ptr = star_idx + 1
            match += 1
            m_ptr = match
        # If no match and no star to backtrack to, return false
        else:
            return False

    # Ensure that the remaining characters in the pattern are all '*'
    while p_ptr < len(p) and p[p_ptr] == '*':
        p_ptr += 1

    # If we've processed the entire pattern, it's a match
    return p_ptr == len(p)