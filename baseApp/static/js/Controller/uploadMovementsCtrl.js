/**
 * Created by josenava on 05/11/14.
 */
app.controller('UploadMovementsCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.movement = {};
    $scope.addMovement = function() {
        $http({
            method: 'post',
            url: 'api/add/',
            data: {
                movDate: $scope.movement.date,
                movDescription: $scope.movement.description,
                movAmount: $scope.movement.amount
            },
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        }).success(function(data, status) {
            $scope.movement = {}
        });
    };

    $scope.uploadCSV = function(files) {
        var fd = new FormData();
        fd.append("file", files[0]);
        $http.post('/api/import/', fd, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        }).success(function(data, status) {
            $scope.movement.CSVUploadMessage = "CSV uploaded";
        });
    };
}]);