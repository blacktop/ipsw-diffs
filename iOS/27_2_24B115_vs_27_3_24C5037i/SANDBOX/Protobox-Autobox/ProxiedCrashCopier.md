## ProxiedCrashCopier

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.nsurlsessiond.NSURLSessionProxyService"))
 		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.OTATaskingAgent"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.FileCoordination"))

 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
 		SYS_fileport_makeport
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (deny system-mac-syscall
 	(require-all
 		(mac-syscall-number 1)

 )
 
 (deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action NECP_CLIENT_ACTION_ADD)
+)
 
 (allow process-exec-update-label)
```
