# Destiny2API
A handwritten API class for Destiny2.
All calls are currenty GET based, post actions are not included, feel free to fork and contribute. Please make sure that if you are working on authenticated endpoints that you clearly document your methodology and attempt to include some compatibility with Python Social Auth.
All functions are to follow the API key name from bungie docs located:
https://bungie-net.github.io/
Please sluggify the function names like so:
`User.GetBungieNetUserById` would fall under the `user.py` class with the function name: `def get_bungie_net_user_by_id()`
Please specify in the doc string for the function whether it is GET or POST and assert the calls and returns. (note: this work still needs to be done)

utils.py contains:
  int32 conversion for manifest lookups
  request call for api
  api key lookups (change for your path)

user.py contains:
  user based API calls

groupsv2 contains:
  group based API calls

destiny2 contains:
  destiny2 game content API calls
