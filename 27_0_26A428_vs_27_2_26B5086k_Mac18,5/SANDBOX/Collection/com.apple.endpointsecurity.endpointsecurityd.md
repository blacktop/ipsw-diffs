## com.apple.endpointsecurity.endpointsecurityd

> Group: ⬆️ Updated

```diff

 		afpfsSleepWakeFSCTL)
 )
 
+(allow system-info
+	(info-type "vfs.disk-space")
+)
+
 (allow system-socket
 	(socket-domain AF_ROUTE)
 )
```
