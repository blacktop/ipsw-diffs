## profiled

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
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleCredentialManager")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-sem-create)
-(allow ipc-posix-sem-create
+(deny ipc-posix-sem*)
+(allow ipc-posix-sem*
 	(ipc-posix-name "profiled.firstboot_check")
 )
 
-(deny ipc-posix-sem-open)
-(allow ipc-posix-sem-open
+(deny ipc-posix-sem-create)
+(allow ipc-posix-sem-create
 	(require-any
 		(ipc-posix-name "profiled.firstboot_check")
 		(ipc-posix-name "purplebuddy.sentinel")
 	)
 )
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.cfprefs.daemonv1")

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
 		(require-not (global-name "com.apple.gamed"))

 		(require-not (require-any
 			(global-name "com.apple.assessmentagent.activeRestrictionUUIDFetching")
 			(global-name "com.apple.biometrickitd.oyster")
-			(global-name "com.apple.managedconfiguration.mdmuserdservice")
 			(global-name "com.apple.studentd")
 		))
 		(require-not (global-name "com.apple.webinspector"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (xpc-service-name "com.apple.FontServices.UserFontServices"))
+		(require-not (global-name "com.apple.managedconfiguration.mdmuserdservice"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.manageddeviced"))

 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.nehelper"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (global-name "com.apple.installcoordinationd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.carkit.service"))

 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.diagd"))
-		(require-not (xpc-service-name "com.apple.FontServices.GSFontServices"))
+		(require-not (xpc-service-name "com.apple.FontServices.UserFontServices"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))
 		(require-not (global-name "com.apple.chronoservices"))

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.online-auth-agent.xpc"))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (xpc-service-name "com.apple.FontServices.GSFontServices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.itunesstored.xpc"))
 		(require-not (global-name "com.apple.remindd"))

 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.security.XPCAcmeService"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fchmodat
 		SYS_fstatat
```
