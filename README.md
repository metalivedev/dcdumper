dcdumper
========

Adding tools to the dotcloud CLI which make it easier to do backups.

The first addition is `sshconf` which is super-useful for working directly with `ssh`, `scp` and `rsync`

```
$ dcdumper.py sshconf -A myapp --file myapp.conf
==> Wrote 1 entries to myapp.conf. You can now sync your data with:
==> "rsync -azv -e 'ssh -F myapp.conf' myapp.myservice.0:code/ code"
```

