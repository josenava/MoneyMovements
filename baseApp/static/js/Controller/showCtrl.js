/**
 * Created by josenava on 09/11/14.
 */
app.controller('ShowCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.movements = [];

    $http.get('/api/movements/5/').success(function(data, status) {
        $scope.movements = JSON.parse(data.movements);
    });
}]);