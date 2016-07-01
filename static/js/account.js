$(function () {
    $('#btn-login').click(function () {
        var em = $('input[name="email"]').val();
        var un = $('input[name="user_name"]').val();
        var pw = $('input[name="password"]').val();
        var cf = $('input[name="confirm"]').val();
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