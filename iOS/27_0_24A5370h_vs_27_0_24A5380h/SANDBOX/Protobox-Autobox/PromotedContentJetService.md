## PromotedContentJetService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.xpc.amsaccountsd"))
+		(require-not (global-name "com.apple.webinspector"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
-		(require-not (global-name "com.apple.amsprivateidentifiers"))
+		(require-not (global-name "com.apple.dt.automationmode.reader"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
+		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.ap.promotedcontent.supportinterface"))
 		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))
-		(require-not (global-name "com.apple.webinspector"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.dt.automationmode.reader"))
 		(require-not (global-name "com.apple.servicesanalytics.xpc"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.amsprivateidentifiers"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (xpc-service-name "com.apple.JetTracingSupport.JetTracingService"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
```
