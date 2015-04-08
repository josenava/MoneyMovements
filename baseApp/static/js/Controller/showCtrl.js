/**
 * Created by josenava on 09/11/14.
 */
app.controller('ShowCtrl', ['$scope', '$http', 'movementsFactory', 'categoriesFactory',
    function($scope, $http, movementsFactory, categoriesFactory) {
    $scope.movements = [];
    $scope.startDate = moment(new Date()).startOf('month').format('YYYY-MM-DD');
    $scope.endDate = moment(new Date()).format('YYYY-MM-DD');
    $scope.datesErrorMsg = "";
    $scope.chartConfig = {
        options: {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Monthly Average Rainfall'
            },
            subtitle: {
                text: 'Source: WorldClimate.com'
            }

        },
        xAxis: {
            categories: [
                'Jan'
            ]
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Rainfall (mm)'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'Tokyo',
            data: [49.9]

        }, {
            name: 'New York',
            data: [83.6]

        }, {
            name: 'London',
            data: [48.9]

        }, {
            name: 'Berlin',
            data: [42.4]

        }]

    };



    $scope.checkDates = function () {
        // todo add security layer to check if they are actually dates
        var startDate = moment($scope.startDate).format('YYYY-MM-DD');
        var endDate = moment($scope.endDate).format('YYYY-MM-DD');
        if (startDate <= endDate) {
            movementsFactory.getMovements(5, startDate, endDate)
                .success(function(data) {
                    var movements = [];
                    $scope.datesErrorMsg = "";
                    $.each(data.movements, function(idx, mov) {
                        var parsedMov = JSON.parse(mov);
                        parsedMov['categories'] = JSON.parse(parsedMov['categories']);
                        movements.push(parsedMov);
                    });
                    $scope.movements = movements;
                });
            categoriesFactory.getCategories()
                .success(function(data) {
                    $scope.availableCategories = JSON.parse(data.categories);
                    console.log($scope.availableCategories);
                });
            categoriesFactory.getCategoriesTotalAmount(startDate, endDate)
                .success(function(data) {
                   $scope.categoryExpenses = JSON.parse(data.categories);
                });

        }
        else {
            $scope.datesErrorMsg = "End date must be bigger than start date"
        }
    };


    $scope.checkDates();
    $scope.getCategoryMovements = function() {
        console.log($scope.selectedCategory.pk);
        movementsFactory.getMovements(5, $scope.startDate, $scope.endDate, $scope.selectedCategory.pk)
            .success(function(data){
                var categoryMovements = [];
                    $scope.datesErrorMsg = "";
                    $.each(data.movements, function(idx, mov) {
                        var parsedMov = JSON.parse(mov);
                        categoryMovements.push(parsedMov);
                    });
                    $scope.categoryMovements = categoryMovements;
            });
    };

}]);