(function () {
  'use strict';

  angular
    .module('site.layout.controllers')
    .controller('LayoutController', LayoutController);

  LayoutController.$inject = ['$scope', 'Layout'];

  function LayoutController($scope, Layout) {
    var vm = this;

    vm.taskList = null;
    vm.next_page = null;
    vm.previous_page = null;
    vm.tasks = null;
    vm.count = null;

    Layout.GetAllTask().then(function (d) {
      vm.next_page = d.data.next;
      vm.previous_page = d.data.previous;
      vm.tasks = d.data.results;
      vm.count = d.data.count;
      return;
    })
  }
})();