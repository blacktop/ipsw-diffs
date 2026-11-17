## appmanagedfeaturesd

> Group: ⬆️ Updated

```diff

 (allow socket-ioctl
 	(ioctl-command
 		CTLIOCGINFO
+		SIOCGCONNINFO
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE

 			SYS_recvmsg
 			SYS_sendmsg
 			SYS_recvfrom
+			SYS_getsockname
 			SYS_crossarch_trap
 			SYS_dup
 			SYS_getegid
```
