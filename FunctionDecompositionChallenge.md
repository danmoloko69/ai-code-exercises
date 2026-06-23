## Exercise: Function Decomposition Challenge

# Report Generation Function with Multiple Data Transformations

**Identify the distinct responsibilities in the function**

- The `generate_sales_report` has many responsibility crammed into one function namely: 

    - validating inputs

    - parsing and applying data-range filtering

    - applying extra filters

    - handling the "no data left" case

    - calculating summary metrics

    - building grouped aggregates

    - building forecast data

    - building chart data

    - formatting output for the requested export type

**Create a decomposition plan**

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

**Extract helper functions with clear names and purposes.**

- `validate_report_request()`. Checks that inputs are valid before any processing starts.

- `filter_by_date_range()`. Keeps only sales records that fall within the requested start and end dates.

- `apply_filters()`. Applies extra field-based filters like category, region, or product.

- `build_summary()`. Calculates total sales, average sale, max sale, and min sale.

- `build_grouping()`. Groups sales by a field such as category or region and computes group totals and percentages.

- `build_detailed_transactions()`. Creates the detailed transaction list and adds calculated fields like pre-tax, profit, and margin.

- `build_forecast()`. Builds monthly sales totals, growth rates, and projected future sales.

- `build_charts()`. Prepares chart-ready data for sales over time and grouped breakdowns.

- `generate_output()`. Sends the finished report to JSON, HTML, Excel, or PDF output.

**Document refactoring approach and the benefits gained.** 

- So the first thing was to remove all request validation out of the main function that checks: sales_data, report_type, output_forrmat, data_range into the `validate_report_request()`. This make the main function easier to read.

- Then date_range filtering was separated and moved into the `filter_by_date_range()` function being a specific transformation on data it belongs to helper not main reporting flow.

- Extra filter was move to `apply_fiilters()` function this keeps all filtering behavior in one place and avoids repeating the filter pattern in the main function.

- The warning messsage and empty_result return logic moved into `hhandles_empty_result()` function as the "no data left after filtering" is a control_flow path does not belong to the main function.

- The summary calculation was moved into `build_summary()` function this makes the calculation reusable and easier to test independently.

- The grouping logic was then moved into `building grouping()` function. Removing it from the main function increase readability.

- The loop that build transaction details was moved into `build_detailed_transaction()` function its formatting is specific to one report type do it should not be mixed into general reports. 

- The forecast generation was also moved into the  `build_forecast()` function as it its own algorithm it should not be in the main function and keeps the forecasting ruule in  on place.

- Chart data generation is also moved into `build_charts()` function this keeps visualization logic separate from the reporting logic.

- The output-format is moved into the `generate__output()` which is the final delivery step should not be part of the reporting calculation itself. 

- Then finally the `generate_sales_report()` the main function now mostly calls helper function instead of containing all the logic inlines.

