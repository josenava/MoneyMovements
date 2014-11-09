/**
 * Created by josenava on 05/11/14.
 */
var app = angular.module('movementApp', []);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);