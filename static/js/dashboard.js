function Dashboard(){
    Dashboard.init();
}

Dashboard.init = function(){
    Dashboard.initSidebarNav();
}

Dashboard.initSidebarNav = function(){
    $('.nav.nav-sidebar li').click(function(){
        if ($(this).children('.subnav').size() > 0){
            $('.nav.subnav').removeClass('open');
            $(this).children('.subnav').addClass('open');
        }
    })

    $('.active-app').click();


}

$(document).ready(function(){
    Dashboard();    
})
