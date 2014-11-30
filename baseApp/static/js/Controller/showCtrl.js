/**
 * Created by josenava on 09/11/14.
 */
app.controller('ShowCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.movements = [];

    $http.get('/api/movements/5/').success(function(data, status) {
        // TODO improve json parsing
        var movements = [];

        $.each(data.movements, function(idx, mov) {
            var parsedMov = JSON.parse(mov);
            parsedMov['categories'] = JSON.parse(parsedMov['categories']);
            movements.push(parsedMov);
        });
        $scope.movements = movements;
    });
}]);