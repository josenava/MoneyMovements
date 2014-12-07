/**
 * Created by josenava on 09/11/14.
 */
app.controller('ShowCtrl', ['$scope', '$http', 'movementsFactory', function($scope, $http, movementsFactory) {
    $scope.movements = [];
    $scope.startDate = moment(new Date()).startOf('month').format('YYYY-MM-DD');
    $scope.endDate = moment(new Date()).format('YYYY-MM-DD');
    $scope.datesErrorMsg = "";

    $scope.checkDates = function () {
        // todo add security layer to check if they are actually dates
        var startDate = moment($scope.startDate).format('YYYY-MM-DD');
        var endDate = moment($scope.endDate).format('YYYY-MM-DD');
        if (startDate <= endDate) {
            movementsFactory.getMovements(10, startDate, endDate)
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
        }
        else {
            $scope.datesErrorMsg = "End date must be bigger than start date"
        }
    };


    $scope.checkDates();

}]);