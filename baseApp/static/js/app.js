/**
 * Created by josenava on 05/11/14.
 */
var app = angular.module('movementApp', ['ui.router']);

app.config(function($httpProvider, $stateProvider, $urlRouterProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('addMovements', {
            url: '/addMovements',
            controller: 'UploadMovementsCtrl',
            templateUrl: '/static/templates_angularViews/uploadMovements.html'
        })
        .state('movements', {
            url: '/movements',
            controller: 'ShowCtrl',
            templateUrl: '/static/templates_angularViews/movements.html'
        });
//    $routeProvider.
//        when('/addMovements', {
//            controller: 'UploadMovementsCtrl',
//            templateUrl: '/static/templates_angularViews/uploadMovements.html'
//        })
//        .when('/movements', {
//            controller: 'ShowCtrl',
//            templateUrl: '/static/templates_angularViews/movements.html'
//        })
//        .otherwise({
//            redirectTo: '/'
//        });
//    $locationProvider.html5Mode(true);
});