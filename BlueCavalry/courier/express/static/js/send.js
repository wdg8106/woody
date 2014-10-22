/*
描述：我要发件页面js
作者：梁银乔
时间：2014-10-13
*/
$(function() {
    $(".value_area").hide();
    var _flag = false;
    $("#toggle").click(function() {
        if (!_flag) {
            $(".value_area").slideToggle();
            $(this).attr("src", "/static/images/remove.png");

        } else {
            $(".value_area").slideToggle();
            $(this).attr("src", "/static/images/add.png");
        }
        _flag = !_flag;
    });
    $("#minus_s").click(function() {
        handle_time(false, "start");
    });
    $("#plus_s").click(function() {
        handle_time(true, "start");
    });
    $("#minus_e").click(function() {
        handle_time(false, "end");
    });
    $("#plus_e").click(function() {
        handle_time(true, "end");
    });
    $("form").submit(function() {
       validate_form(this);
    });
});
//时间处理函数
function handle_time(isAdd, selector) {
        var time = parseInt($("#" + selector).val());
        if (!isAdd) {
            if ((time - 1))
                time--;
        } else {
            if ((time + 1) < 24)
                time++;
        }
        $("#" + selector).val(time + ":00");

    }
function validate_form(thisform) {
    with(thisform) {
 
    }
}
