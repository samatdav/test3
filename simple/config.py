# config.py

from authomatic.providers import oauth2, oauth1

CONFIG = {
    
    'tw': { # Your internal provider name
        
        # Provider class
        'class_': oauth1.Twitter,
        
        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': '########################',
        'consumer_secret': '########################',
    },
    
    'fb': {
           
        'class_': oauth2.Facebook,
        
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '1579999525609087',
        'consumer_secret': 'b23b89a6d965d2ca0892dbf8f03a7eed',
        
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    }
}