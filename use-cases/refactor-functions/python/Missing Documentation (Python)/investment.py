def calculate(principal, rate, time, additional=0, frequency=12):
    """
    Calculate compound growth with optional recurring contributions.

    Args:
        principal (float): The starting amount invested or borrowed.
        rate (float): Annual interest rate as a percentage, e.g. 5 for 5%.
        time (int or float): Total duration in years.
        additional (float, optional): Contribution added once per year at the end of each full year.
        frequency (int, optional): Number of compounding periods per year. Defaults to 12.

    Returns:
        dict: A summary containing:
            - final_amount: Total value after compounding and contributions
            - interest_earned: Growth earned from compounding
            - total_contributions: Principal plus recurring contributions

    Assumptions:
        - Interest compounds at a constant rate throughout the full period.
        - Additional contributions are added once per full year, not every period.
        - Contributions are not added after the final year, since the loop adds them
          only between full years.
        - `time * frequency` should represent a whole number of periods for the loop.

    Limitations:
        - The `interest_earned` calculation assumes one contribution per completed year.
          It does not account for fractional years or mid-year contributions.
    """
    result = principal
    rate_per_period = rate / 100 / frequency
    total_periods = time * frequency

    # Apply compound interest period by period.
    for period in range(1, total_periods + 1):
        interest = result * rate_per_period
        result += interest

        # Add the yearly contribution after each full year except the final one.
        if period % frequency == 0 and period < total_periods:
            result += additional

    # Contributions are assumed to occur once per completed year.
    total_contributions = principal + (additional * (time - 1))

    return {
        "final_amount": round(result, 2),
        "interest_earned": round(result - total_contributions, 2),
        "total_contributions": total_contributions
    }