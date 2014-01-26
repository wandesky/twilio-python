from nose.tools import assert_equal

from twilio.rest import find_credentials

def test_creds_not_found():
    """ I shouldn't find credentials if they are not there """
    assert_equal(find_credentials({'foo': 'bar'}), (None, None))

def test_find_creds():
    """ I should find the credentials if they are there """
    env = {
        'TWILIO_ACCOUNT_SID': 'AC123',
        'foo': 'bar',
        'TWILIO_AUTH_TOKEN': '456',
    }
    assert_equal(find_credentials(env), ('AC123', '456'))

