/**
 * Created by wrose on 5/6/17.
 */
var waypoint = new Waypoint({
    element: document.getElementsByClassName('card'),
    handler: function () {
        notify('Basic waypoint triggered')
        console.log('Worked ?')
    }
})