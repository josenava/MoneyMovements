/**
 * Created by josenava on 05/11/14.
 */
app.controller('MovementCtrl', ['$scope', '$http', function($scope, $http) {
    console.log("hey I am using angular, it's amazing, isn't it?");
    $scope.movement = {};
    console.log($scope.movement.date, $scope.movement.description, $scope.movement.amount);
    $scope.addMovement = function() {
        console.log($scope.movement.date, $scope.movement.description, $scope.movement.amount);
        $http({
            method: 'post',
            url: 'api/add/',
            data: {
                movDate: $scope.movement.date,
                movDescription: $scope.movement.description,
                movAmount: $scope.movement.amount
            },
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        }).success(function(data, status, headers, config) {
            $scope.movement = {}
        });
    }
}]);