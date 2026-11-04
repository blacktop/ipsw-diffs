## intelligencecontextd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.TextInput.rdt"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.agentboardd.input"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
 		(require-not (global-name "com.apple.coremedia.admin"))

 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.uservault"))
 		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.perceptiond.peripheralSensing"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.intelligenceflow.context"))

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.corerecents.recentsd"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.logd"))

 		SYS_kdebug_trace_string
 		SYS_kdebug_trace64
 		SYS_kdebug_trace
+		SYS_seteuid
 		SYS_sigreturn
 		SYS_stat
 		SYS_fstat

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
