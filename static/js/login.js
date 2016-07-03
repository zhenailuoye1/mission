$(function () {
    //登录账号
    $('#btn-login').click(function () {
        var name = $('input[name="user_name"]').val();
        var pw = $('input[name="password"]').val();
        if (!name) {
            alert('用户名不能为空!');
            return false;
        }
        if (!pw) {
            alert('密码不能为空!')
            return false;
        }
        $.ajax({
            url: '/login',
            type: 'POST',
            data: {
                user_name: name,
                password: pw,
            },
            success: function (data, Status) {
                if (data == 'ok') {
                    alert('登录成功！跳转到首页中...')
                    window.location.href = "/";
                }
                else {
                    alert("用户名或密码错误");
                }
            }
        })
    })
    //注册账号
    $('#btn-register').click(function () {
        var em = $('input[name="re_email"]').val();
        var un = $('input[name="re_user_name"]').val();
        var pw = $('input[name="re_password"]').val();
        var cf = $('input[name="re_confirm"]').val();
        if (name.length < 6) {
            alert('用户名至少6位');
            return false;
        } else if (pw.length < 6) {
            alert('密码至少6位')
            return false;
        } else if (pw != cf) {
            alert('两次密码不一致')
        }

        $.ajax({
            url: '/login',
            type: 'POST',
            data: {
                user_name: un,
                password: pw,
            },
            success: function (data, Status) {
                if (data == 'ok') {
                    alert('注册成功！')
                    window.location.href = "/login";
                } else if (data == 'email exist') {
                    alert('邮箱已注册');
                }
                else if (data == 'user_name exist') {
                    alert('用户名已注册');
                }
            }
        })
    })
})