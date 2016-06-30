alert('请输入用户名和密码')

$(function () {
    $('#btn-login').click(function () {
        $.ajax({
            url: '/login',
            type: 'POST',
            data: {
                user_name: $('input[name="user_name"]').val(),
                password: $('input[name="password"]').val(),
            },
            success: function (data) {
                alert(data);
            }
        })
    })
})