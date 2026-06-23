## Exercise: Function Decomposition Challenge

# Report Generation Function with Multiple Data Transformations

* Identify the distinct responsibilities in the function

- The `generate_sales_report` has many responsibility cramed into one function namely: 

    - validating inputs

    - parsing and applying data-range filtering

    - applying extra filters

    - handling the "no data left" case

    - calculating summary metrics

    - building grouped aggregates

    - building forecast data

    - building chart data

    - formatting output for the requested export type

* Create a decomposiition plan

- This will include a split off the responsibilities into their own functions namely:

    - validate_report_request()

    - filter_by_date_range()

    - apply_filters()

    - build_summary()

    - build_grouping()

    - build_detailed_transactions()

    - build_forecast()

    - build_charts()

    - build_report_data()

    - generate_output()

For the main function it will co-ordinate those helpers in order.

* Extract helper functions with clear names and purposes

- `validate_report_request()`. Checks that inputs are valid before any processing starts.

- `filter_by_date_range()`. Keeps only sales records that fall within the requested start and end dates.

- `apply_filters()`. Applies extra field-based filters like category, region, or product.

- `build_summary()`. Calculates total sales, average sale, max sale, and min sale.

- `build_grouping()`. Groups sales by a field such as category or region and computes group totals and percentages.

- `build_detailed_transactions()`. Creates the detailed transaction list and adds calculated fields like pre-tax, profit, and margin.

- `build_forecast()`. Builds monthly sales totals, growth rates, and projected future sales.

- `build_charts()`. Prepares chart-ready data for sales over time and grouped breakdowns.

- `generate_output()`. Sends the finished report to JSON, HTML, Excel, or PDF output.

* Doocument refactoring approach and the benefits gained. 