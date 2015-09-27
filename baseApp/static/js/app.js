/**
 * Created by josenava on 05/11/14.
 */
var app = angular.module('movementApp', ['ui.router', 'highcharts-ng']);

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
        })
        .state('categories', {
            url: '/categories',
            controller: 'CategoriesCtrl',
            templateUrl: '/static/templates_angularViews/categories.html'
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

app.directive('tagElement', function() {
    return {
        restrict: 'E',
        scope: {
            name: '@',
            onDelete: '&'
        },
        template: '<li class="tag-element">{{ name }} <span class="glyphicon glyphicon-remove" ng-click="onDelete(name)"></span></li>',
        replace: true
    };
});

app.factory('categoriesFactory', ['$http', function($http) {

    var urlBase = '/api/categories';
    var categoriesFactory = {};

    categoriesFactory.getCategories = function() {
        return $http.get(urlBase);
    };

    categoriesFactory.deleteCategory = function(name) {
        return $http.delete(urlBase + '/' + name);
    };

    categoriesFactory.createCategory = function(category_data) {
        return $http({
            method: 'post',
            url: urlBase + '/',
            data: category_data,
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        });
    };

    categoriesFactory.getCategoriesTotalAmount = function(startDate, endDate) {
        return $http.get(urlBase,
            {
                params:
                    {
                        total_amount: true,
                        start_date: startDate,
                        end_date: endDate
                    }
            }
        );
    };

    return categoriesFactory;
}]);

app.factory('movementsFactory', ['$http', function($http) {

    var urlBase = '/api/movements';
    var movementsFactory = {};

    movementsFactory.getMovements = function(number, startDate, endDate, categoryId) {
        return $http.get(urlBase + '/' + number + '/',
            {
                params:
                    {
                        start_date: startDate,
                        end_date: endDate,
                        categoryId: categoryId
                    }
            }
        );
    };

    return movementsFactory;
}]);
