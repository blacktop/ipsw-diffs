## com.apple.IdentityLookup.MessageFilter

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.pluginkit.pkd"))
-		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
+		(require-not (global-name "com.apple.pluginkit.pkd"))
+		(require-not (global-name "com.lre.SubClassFilter.SubClassFilterMsgExtension"))
 		(require-not (global-name "com.apple.nehelper"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.SharedWebCredentials"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
-		(require-not (global-name "com.lre.SubClassFilter.SubClassFilterMsgExtension"))
+		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.SharedWebCredentials"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
```
