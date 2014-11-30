/**
 * Created by josenava on 16/11/14.
 */
app.controller("CategoriesCtrl", ['$scope', 'categoriesFactory', function($scope, categoriesFactory) {

    $scope.formErrorMsg = "";
    $scope.availableCategories = [];

    categoriesFactory.getCategories().success(function (data) {
        $scope.availableCategories = JSON.parse(data.categories);
    });


    $scope.addCategory = function() {
        var category_form_data = {name: $scope.category.fields.name, related_words: $scope.category.fields.related_words};
        categoriesFactory.createCategory(category_form_data).success(function(){
            $scope.availableCategories.push({ fields: category_form_data});
            $scope.category.fields = {};
            $scope.formErrorMsg = "";
        })
        .error(function(data){
            $scope.formErrorMsg = data.created;
        });
    };


    $scope.deleteCategory = function(name) {
        categoriesFactory.deleteCategory(name).success(function(data){
            $scope.availableCategories = _.reject($scope.availableCategories, function(obj) { return name == obj.fields.name});
        });
    };
}]);
