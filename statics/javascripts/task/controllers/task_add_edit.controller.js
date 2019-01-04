(function () {
  'use strict';

  angular
    .module('site.task.controllers')
    .controller('TaskAddEditController', TaskAddEditController);

  TaskAddEditController.$inject = ['$scope', '$routeParams', 'Task', 'Authentication'];

  function TaskAddEditController($scope, $routeParams, Task, Authentication) {
    var vm = this;
    vm.tags = null;
    vm.categories = null;
    vm.searchUser = searchUser;
    vm.userList = null;
    vm.user = null;
    vm.addEditTask = addEditTask;
    vm.message = null;
    vm.error = null;
    vm.taskCreateRespose = null

    // function renderPage(data) {
    //   vm.tags = data.results;
    //   vm.categories: data.results;
    // }

    function addEditTask(){
      Task.postNewTask(vm.task).then(d) {
        if (d.status === 201) {
          vm.message = 'Successful';
        } else {
          vm.message = 'data';
        }
      }
    }

    Task.getAllTags().then(function (d) {
      vm.tags = d.data.results;
    });

    Task.getAllCategories().then(function (d) {
      vm.categories = d.data.results
    });

    function searchUser() {
      if (vm.user) {
        Authentication.searchUser(vm.user).then(function (d) {
          vm.userList = d.data.results;
        })
      }

    }

  }
})();