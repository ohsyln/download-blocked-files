 # download-blocked-files

For frustrated users who just want to download their shit at work, but are unfortunately cockblocked by overly stringent firewall rules or network policies.


A [third-party server](https://www.heroku.com) fetches the file you want to download on your behalf, and encrypts it with some shitty password (1234) so that the encrypted file evades detection from signature-based detectors. Finally, it returns you the encrypted file.

### If you want to self-host

Follow the guide [here](https://devcenter.heroku.com/articles/getting-started-with-python), then replace the `hello/views.py` with the copy provided in this repo.

## License

MIT
