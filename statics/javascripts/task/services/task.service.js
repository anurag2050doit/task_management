/**
 * Dashboard
 * @namespace site.task.services
 */

(function () {
  'use strict';

  angular
    .module('site.task.services')
    .factory('Task', Task);


  Task.$inject = ['$http'];


  function Task($http) {
    /**
     * @name Task
     * @desc The Factory to be returned
     */
    var Task = {
      getTaskDetail: getTaskDetail,
      updateTaskStatus: updateTaskStatus,
      getAllTags: getAllTags,
      getAllCategories: getAllCategories,
      postNewTask: postNewTask
    };

    return Task;

   //
   //
   //
   //

    /**
     * @name PostNewTask
     * @desc Make Post request to create new Task
     * @param data
     * @returns {*|*|PromiseLike<T | never>|Promise<T | never>}
     * @memberOf site.task.services
     *
     */
   function postNewTask(data) {
     return $http({
       url: '/api/v1/task/',
       method: 'POST',
       headers: {
         'Content-Type': 'application/json'
       }
     }).then(taskCreatedSuccessFn, taskCreatedSuccessFn);

     function taskCreatedSuccessFn(data, status, headers, config) {
       return data;
     }
   }

    /**
     * @name GetTaskDetail
     * @desc Return Task Detail of specific ID
     * @returns {Promise}
     * @memberOf site.task.services
     */

    function getTaskDetail(taskId) {
      return $http({
        url: '/api/v1/task/' + taskId + '/',
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(getTaskSuccessFn, getTaskSuccessFn);

      function getTaskSuccessFn(data, status, headers, config) {
        return data;
      }
    }

    /**
     *
     * @param status
     * @param taskId
     * @returns {*|*|PromiseLike<T | never>|Promise<T | never>}
     * @memberOf site.task.services
     */

    function updateTaskStatus(status, taskId) {
      return $http({
        url: '/api/v1/task/' + taskId + '/',
        method: 'PATCH',
        data: {
          "task_status": status
        },
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(getTaskSuccessFn, getTaskSuccessFn);

      function getTaskSuccessFn(data, status, headers, config) {
        return data;
      }
    }

    /**
     * @desc Return list of All tasks
     * @returns {*|*|PromiseLike<T | never>|Promise<T | never>}
     * @memberOf site.task.services
     */

    function getAllTags() {
      return $http({
        url: '/api/v1/tag/',
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(getTagSuccessFn, getTagSuccessFn);

      function getTagSuccessFn(data, status, header, config) {
        return data;
      }
    }

    /**
     * @desc Return list of all categories
     * @returns {*|*|PromiseLike<T | never>|Promise<T | never>}
     * @memberOf site.task.services
     */

    function getAllCategories() {
      return $http({
        url: '/api/v1/category/',
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(getTagSuccessFn, getTagSuccessFn);

      function getTagSuccessFn(data, status, header, config) {
        return data;
      }
    }
  }
})();