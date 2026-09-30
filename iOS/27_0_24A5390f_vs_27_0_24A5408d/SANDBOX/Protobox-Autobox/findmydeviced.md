## findmydeviced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.nanoprefsync"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.ndoagent"))
+		(require-not (require-any
+			(global-name "com.apple.icloud.FindMyDevice.FindMyDeviceTheftAndLossXPCService")
+			(global-name "com.apple.icloud.findmydevice.alert")
+			(global-name "com.apple.icloud.findmydevice.command")
+			(global-name "com.apple.icloud.findmydevice.network")
+		))
 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.CompanionLink"))

 		(require-not (global-name "com.apple.icloud.searchpartyd.pairingmanager"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (require-any
-			(global-name "com.apple.icloud.FindMyDevice.FindMyDeviceTheftAndLossXPCService")
-			(global-name "com.apple.icloud.findmydevice.command")
-			(global-name "com.apple.icloud.findmydevice.network")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FMDSharedConfigurationXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceBTDiscoveryXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceEraseXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceIdentityXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfigurationXPCService")
 		))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.iohideventsystem"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (require-any
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FMDSharedConfigurationXPCService")
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceBTDiscoveryXPCService")
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceEraseXPCService")
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceIdentityXPCService")
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfigurationXPCService")
-		))
 		(require-not (xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService"))
 		(require-not (xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceUserNotificationsXPCService"))
 		(require-not (xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceTheftAndLossXPCService"))
```
