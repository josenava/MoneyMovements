/**
 * Created by josenava on 05/11/14.
 */
var app = angular.module('movementApp', ['ngRoute']);

app.config(['$httpProvider', '$routeProvider', '$locationProvider', function($httpProvider, $routeProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $routeProvider.
        when('/addMovements', {
            controller: 'UploadMovementsCtrl',
            templateUrl: '/static/templates_angularViews/uploadMovements.html'
        })
        .when('/movements', {
            controller: 'ShowCtrl',
            templateUrl: '/static/templates_angularViews/movements.html'
        })
        .otherwise({
            redirectTo: '/'
        });
    $locationProvider.html5Mode(true);
}]);