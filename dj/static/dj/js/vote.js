function vote(yt_id) {
    $.ajax({url: '/dj/vote/' + yt_id + '/', type: 'post'})
        .done(function (data) {
            // Update vote count
            $("#nbvotes" + yt_id).text(data.nb_votes)

            // Update vote icon
            var icon = $("#icon" + yt_id);
            if (data.is_upvote)
                icon.toggleClass("vote_button unvote_button");
            else
                icon.toggleClass("unvote_button vote_button");
        });
}
