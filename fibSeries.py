def series(self, n):
       
        fibonacci_series = [0, 1]  # Initialize the series with first two terms.

        # Generate the series up to the nth term.
        for _ in range(n - 1):
            next_term = (fibonacci_series[-1] + fibonacci_series[-2]) % (10**9 + 7)
            fibonacci_series.append(next_term)

        return fibonacci_series