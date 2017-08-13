# numbers
# $ git config --global user.name "Bob"
# $ git config --global user.email "bob@example.com"
# you'll need to remove authorization info from Keychain. This is something I've also struggled with until I
# found that I also had certificate in my Keychain.
# Open up Keychain access, click on All Items and search for git. You will get some items like this:

#Delete them. Now try to push the repo and git will ask you to write password for the user and you will be good #to go.
