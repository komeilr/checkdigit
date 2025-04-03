def check_digit(trans:int) -> int:
    """
    CBSA 14-digit transaction number checkdigit calculation
    
    (a) link together the account security and sequential number into one 13-digit number;   
    (b) starting with the high-order digit (the most left hand), multiply each digit in an odd-numbered position by 1, and
    multiply each digit in an even-numbered position by 2;
    (c) for each result of the multiplication above, if the result is greater than or equal to 10, add the two digits together to
    give a single digit result (e.g., a digit of 9 multiplied by 2 gives a result of 18. 18 is greater than 10, so add the digits 1 and
    8 together to give a result of 9);
    (d) sum all of the results calculated above;
    (e) divide the sum by 10, giving a quotient and a remainder;
    (f) the remainder becomes the check digit and the 14th digit of the transaction number.
    """
    
    assert len(str(trans))==13, "trans argument must be of length 13"

    odds = [int(n) for idx, n in enumerate(str(trans)) if idx%2 == 0]
    evens = [int(n) for idx, n in enumerate(str(trans)) if idx%2 == 1]
    odd_sum = sum(odds)
    even_sum = 0
    for n in evens:
        result = n * 2
        if result > 10:
            result = sum([int(i) for i in str(result)])
        even_sum += result

    return f"{trans}{(odd_sum + even_sum) % 10}"
