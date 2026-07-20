## textcontextd

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
+(deny iokit-open-user-client)
+
 (deny iokit-open-service)
 
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")

 	)
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.TextInput.accessibility"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
+		(require-not (global-name "com.apple.passd.library"))
 		(require-not (global-name "com.apple.generativesearch.server.search"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.NPKCompanionAgent.library"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.Archetype.personalContext"))
 		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
-		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
-		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command CTLIOCGINFO)

 		io_iterator_next
 		io_registry_create_iterator
 		io_registry_entry_from_path
+		io_registry_entry_get_name
 		io_service_close
 		io_connect_get_service
 		io_registry_entry_create_iterator
```
