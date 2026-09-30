## streaming_zip_conduit

> Group: ⬆️ Updated

```diff

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_PREALLOCATE
```
