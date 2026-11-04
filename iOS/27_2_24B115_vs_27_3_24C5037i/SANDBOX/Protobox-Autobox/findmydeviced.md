## findmydeviced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.CompanionLink"))
 		(require-not (global-name "com.apple.SBUserNotification"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.icloud.searchpartyd.beaconmanager.simplebeacon"))
 		(require-not (global-name "com.apple.geod"))

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.ak.anisette.xpc"))
 		(require-not (global-name "com.apple.server.bluetooth.general.xpc"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))

 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.carousel.connectionstatusservice"))
+		(require-not (global-name "com.apple.bioconvenienced"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.icloud.searchpartyd.pairingmanager"))
 		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (require-any
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FMDSharedConfigurationXPCService")
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceBTDiscoveryXPCService")
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceEraseXPCService")
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceIdentityXPCService")
-			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfigurationXPCService")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.findmy.FindMySecureEnvironmentXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceUserNotificationsXPCService")
+		))
+		(require-not (require-any
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FMDSharedConfigurationXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceBTDiscoveryXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceEraseXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceIdentityXPCService")
+			(xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfigurationXPCService")
+		))
 		(require-not (xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService"))
-		(require-not (xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceUserNotificationsXPCService"))
 		(require-not (xpc-service-name "com.apple.icloud.FindMyDevice.FindMyDeviceTheftAndLossXPCService"))
 		(require-any
 			(require-all

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_setattrlist
 		SYS_fgetattrlist
 		SYS_fsetattrlist
 		SYS_getxattr

 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
 		SYS_fileport_makeport
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np

 
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
