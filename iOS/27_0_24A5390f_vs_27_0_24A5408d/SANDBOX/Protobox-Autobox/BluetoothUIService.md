## BluetoothUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.TextInput"))
 		(require-not (global-name "com.apple.accessibility.mediaaccessibilityd"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))

 			(global-name "com.apple.feedbackd.remote-feedback")
 		))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
+		(require-not (global-name "com.apple.DragUI.druid.destination"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.coremedia.asset.xpc"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.CARenderServer"))
-				(require-not (global-name "com.apple.DragUI.druid.destination"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
 				(require-not (global-name "PurplePPTServer"))

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.CARenderServer"))
-				(require-not (global-name "com.apple.DragUI.druid.destination"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
 				(require-not (global-name "PurplePPTServer"))
```
