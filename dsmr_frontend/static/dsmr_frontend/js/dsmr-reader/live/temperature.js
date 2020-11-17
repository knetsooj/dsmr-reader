$(document).ready(function () {

    var echarts_temperature_graph = echarts.init(document.getElementById('echarts-temperature-graph'));
    echarts_temperature_graph.showLoading('default', echarts_loading_options);

    /* Init graph. */
    $.get(echarts_temperature_graph_url, function (xhr_data) {
        echarts_temperature_graph.hideLoading();

        var option = {
            color: [
                temperature_color
            ],
            tooltip: {
                formatter: "{c} {a}",
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow',
                    label: {
                        show: true
                    }
                }
            },
            calculable: true,
            grid: {
                top: '12%',
                left: '1%',
                right: '2%',
                containLabel: true
            },
            xAxis: [
                {
                    type: 'category',
                    boundaryGap: false,
                    data: xhr_data.read_at
                }
            ],
            yAxis: [
                {
                    type: 'value'
                }
            ],
            dataZoom: [
                {
                    show: true,
                    start: 0,
                    end: 100
                },
                {
                    type: 'inside',
                    start: 0,
                    end: 100
                }
            ],
            series: [
                {
                    name: '°C',
                    type: 'line',
                    areaStyle: {},
                    data: xhr_data.degrees_celcius,
                    smooth: true
                }
            ]
        };
        echarts_temperature_graph.setOption(option);
    });


    /* Responsiveness. */
    $(window).resize(function () {
        echarts_temperature_graph.resize();
    });
});
