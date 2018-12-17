(function () {
  'use strict';

  angular
    .module('site.layout.controllers')
    .controller('LayoutController', LayoutController);

  LayoutController.$inject = ['$scope', 'Layout'];

  function LayoutController($scope, Layout) {
    var vm = this;

    vm.next_page = null;
    vm.previous_page = null;
    vm.tasks = null;
    vm.count = null;
    vm.pagination = pagination

    function renderPage(data) {
      vm.taskId = data.id;
      vm.taskList = data.results;
      vm.next_page = data.next;
      vm.previous_page = data.previous;
      vm.tasks = data.results;
      vm.count = data.count;
      return
    }

    function pagination(url) {
      Layout.getPaginationResponse(url).then(function (d) {
        renderPage(d.data);
        return
      })
    }

    Layout.GetAllTask().then(function (d) {
      renderPage(d.data);
      return
    })
  }
})();