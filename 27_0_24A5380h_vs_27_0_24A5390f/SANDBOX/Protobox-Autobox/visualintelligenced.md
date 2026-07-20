## visualintelligenced

> Group: ⬆️ Updated

```diff

 	(process-attribute is-autoboxed)
 )
 
-(deny iokit-issue-extension
+(deny iokit-get-properties
 	(with no-report)
 	(process-attribute is-autoboxed)
 )
 
-(deny iokit-open-user-client
+(deny iokit-open*
 	(process-attribute is-autoboxed)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(process-attribute is-autoboxed)
 		(require-any

 	)
 )
 
+(deny iokit-open-service
+	(with no-report)
+	(process-attribute is-autoboxed)
+)
+
 (deny iokit-set-properties
 	(with no-report)
 	(process-attribute is-autoboxed)

 	(process-attribute is-autoboxed)
 )
 
-(deny ipc-posix-shm-read-data
+(deny ipc-posix-shm*
 	(process-attribute is-autoboxed)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(process-attribute is-autoboxed)
 		(require-any

 	)
 )
 
-(deny job-creation
+(deny isp-command-send
+	(with no-report)
+	(process-attribute is-autoboxed)
+)
+
+(deny mach-host-special-port-set
 	(with no-report)
 	(process-attribute is-autoboxed)
 )
 
 (deny mach-issue-extension
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
-
-(deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.linkd.registry"))

 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.networkscored"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.DeviceConfigurationAgent.consumer.async"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))

 	)
 )
 
+(deny process-codesigning
+	(with no-report)
+	(process-attribute is-autoboxed)
+)
+
 (deny process-exec*
 	(with no-report)
 	(process-attribute is-autoboxed)
```
