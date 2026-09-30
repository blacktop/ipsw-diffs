## ProxiedCrashCopier

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.rtcreportingd"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
-		(require-not (global-name "com.apple.nsurlsessiond.NSURLSessionProxyService"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.nsurlsessiond.NSURLSessionProxyService"))
+		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.analyticsd"))

 		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_registry_entry_get_name
+		io_service_close
 		io_service_open_extended
+		io_connect_method
 		io_service_get_matching_service
 		io_server_version
 		io_service_get_matching_service_bin
```
