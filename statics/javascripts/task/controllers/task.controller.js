(function () {
  'use strict';

  angular
    .module('site.task.controllers')
    .controller('TaskController', TaskController);

    TaskController.$inject = ['$scope', '$routeParams', 'Task'];

  function TaskController($scope, $routeParams, Task) {
    var vm = this;
    var taskId = $routeParams.taskId;
    vm.updateTaskStatus = updateTaskStatus;

    function renderResponse(data) {
      vm.id = data.id;
      vm.title = data.title;
      vm.description = data.description;
      vm.priority = data.priority_name;
      vm.task_status = data.task_status;
      vm.creator_name = data.creator_name;
      vm.assignee_name = data.assignee_name;
      vm.categories = data.category;
      vm.tags = data.tag;
      vm.created_at = data.created_at;
      vm.modified_at = data.modified_at;
    }

    Task.getTaskDetail(taskId).then(function (d) {
      renderResponse(d.data);
    });

    function updateTaskStatus(status) {
      Task.updateTaskStatus(status, taskId).then(function (d) {
        renderResponse(d.data);
      })
    }
  }
})();