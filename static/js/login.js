alert('请输入用户名和密码')

$(function () {
    $('#btn-login').click(function () {
        var name = $('input[name="user_name"]').val();
        var pw = $('input[name="password"]').val();
        $.ajax({
            url: '/login',
            type: 'POST',
            data: {
                user_name: name,
                password: pw,
            },
            success: function (data,Status) {
                if (data == 'ok') {
                    window.location.href = "/";
                }
                else {
                alert("用户名或密码错误");
                }
            }
        })
    })
})