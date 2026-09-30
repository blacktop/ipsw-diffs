## threadradiod

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.srp-mdns-proxy.proxy"))
+		(require-not (global-name "com.apple.securityd.general"))
 		(require-not (global-name "com.apple.WirelessCoexManager"))
-		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
+		(require-not (global-name "com.apple.SafetyKit"))
+		(require-not (global-name "com.apple.audioanalyticsd"))
+		(require-not (global-name "com.apple.bluetooth.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
-		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
-		(require-not (global-name "com.apple.bluetooth.xpc"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.SafetyKit"))
-		(require-not (global-name "com.apple.securityd.general"))
-		(require-not (global-name "com.apple.awdd"))
-		(require-not (global-name "com.apple.homed.xpc"))
-		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.corefollowup.agent"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
-		(require-not (global-name "com.apple.srp-mdns-proxy.proxy"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.audioanalyticsd"))
-		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.awdd"))
+		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
+		(require-not (global-name "com.apple.homed.xpc"))
+		(require-not (global-name "com.apple.corefollowup.agent"))
+		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (system-attribute developer-mode))

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_iterator_next
+		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_service_close
 		io_service_get_state
```
