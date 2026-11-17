## powerlogHelperd

> Group: ⬆️ Updated

```diff

 		SYS_fgetxattr
 		SYS_setxattr
 		SYS_fsetxattr
+		SYS_fremovexattr
 		SYS_listxattr
 		SYS_flistxattr
 		SYS_fsctl

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_SETFL
```
