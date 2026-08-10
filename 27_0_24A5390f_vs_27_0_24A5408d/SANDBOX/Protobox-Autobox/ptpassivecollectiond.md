## ptpassivecollectiond

> Group: ⬆️ Updated

```diff

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_GETFL
 		F_GETPATH
 		F_GETPROTECTIONCLASS
```
