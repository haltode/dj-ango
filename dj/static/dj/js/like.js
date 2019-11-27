function like(yt_id) {
    $.ajax({url: '/like/' + yt_id + '/', type: 'post'})
        .done(function (data) {
            // Update like icon
            var icon = $("#likeicon" + yt_id);
            if (data.is_liked)
                icon.toggleClass("like_button unlike_button");
            else
                icon.toggleClass("unlike_button like_button");
        });
}
