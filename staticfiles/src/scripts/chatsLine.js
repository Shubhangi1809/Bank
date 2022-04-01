function generateDateLineChart(target, data, parameter) {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    const chartData = [];

    data.forEach(record => {
        const d = {}
        d.date = Date.parse(record.fields.CreatedAt);
        d[parameter]  = record.fields[parameter];
        chartData.push(d)
    })

    // Create chart instance
    var chart = am4core.create(target, am4charts.XYChart);

    // Add data
    chart.data = chartData;
    // Create axes
    var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
    dateAxis.baseInterval = {
        "timeUnit": "second",
        "count": 1
    }
    dateAxis.renderer.minGridDistance = 50;

    var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());


    // Create series
    var series = chart.series.push(new am4charts.LineSeries());
    series.dataFields.valueY = parameter;
    series.dataFields.dateX = "date";
    series.strokeWidth = 2;
    series.minBulletDistance = 10;
    series.tooltipText = "{valueY}";
    series.tooltip.pointerOrientation = "vertical";
    series.tooltip.background.cornerRadius = 20;
    series.tooltip.background.fillOpacity = 0.5;
    series.tooltip.label.padding(12,12,12,12)

    // Add scrollbar
    chart.scrollbarX = new am4charts.XYChartScrollbar();
    chart.scrollbarX.series.push(series);

    // Add cursor
    chart.cursor = new am4charts.XYCursor();
    chart.cursor.xAxis = dateAxis;
    chart.cursor.snapToSeries = series;
}