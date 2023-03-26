from web_test import app


def test_google():
    app.google.open()

    app.google \
        .search('yashaka selene python') \
        .should_have_results_amount_at_least(12)
