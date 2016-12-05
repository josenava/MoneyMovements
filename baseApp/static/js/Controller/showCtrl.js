/**
 * Created by josenava on 09/11/14.
 */
app.controller('ShowCtrl', ['$scope', '$http', 'movementsFactory', 'categoriesFactory',
    function($scope, $http, movementsFactory, categoriesFactory) {
    $scope.movements = [];
    $scope.startDate = moment(new Date()).startOf('month').format('YYYY-MM-DD');
    $scope.endDate = moment(new Date()).format('YYYY-MM-DD');
    $scope.datesErrorMsg = "";

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
