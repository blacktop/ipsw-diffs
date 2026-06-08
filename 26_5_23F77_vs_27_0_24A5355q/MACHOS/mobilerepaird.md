## mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

-921.120.4.0.0
-  __TEXT.__text: 0xe6f4
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x1a40
-  __TEXT.__objc_methlist: 0xbcc
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x216e
-  __TEXT.__objc_methname: 0x1edb
-  __TEXT.__objc_classname: 0x29c
-  __TEXT.__objc_methtype: 0x33e
-  __TEXT.__gcc_except_tab: 0x46c
-  __TEXT.__oslogstring: 0x857
-  __TEXT.__unwind_info: 0x360
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x378
-  __DATA_CONST.__cfstring: 0x22e0
-  __DATA_CONST.__objc_classlist: 0xb8
+1291.0.0.502.1
+  __TEXT.__text: 0xe3c4
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_stubs: 0x1be0
+  __TEXT.__objc_methlist: 0xcfc
+  __TEXT.__const: 0xb8
+  __TEXT.__gcc_except_tab: 0x438
+  __TEXT.__objc_methname: 0x211d
+  __TEXT.__cstring: 0x2303
+  __TEXT.__oslogstring: 0xb2c
+  __TEXT.__objc_classname: 0x2e1
+  __TEXT.__objc_methtype: 0x3da
+  __TEXT.__unwind_info: 0x338
+  __DATA_CONST.__const: 0x428
+  __DATA_CONST.__cfstring: 0x22c0
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x18a0
-  __DATA.__objc_selrefs: 0x850
-  __DATA.__objc_ivar: 0xb0
-  __DATA.__objc_data: 0x730
+  __DATA_CONST.__auth_got: 0x348
+  __DATA_CONST.__got: 0x318
+  __DATA.__objc_const: 0x1b08
+  __DATA.__objc_selrefs: 0x8d0
+  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_data: 0x820
   __DATA.__data: 0x190
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x150
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
+  - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libFDR.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 42D1FABF-2CFF-304B-8872-B2D6EBD28F46
-  Functions: 267
-  Symbols:   189
-  CStrings:  1059
+  UUID: 5ABDE5C4-DD8A-369B-9716-CDA172F193FB
+  Functions: 295
+  Symbols:   200
+  CStrings:  1102
 
Symbols:
+ _OBJC_CLASS_$_CRComponentAuth
+ _OBJC_METACLASS_$_CRComponentAuth
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_respondsToSelector
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _tb_daemon_notification_handle
+ _tb_daemon_notification_register
+ _tb_daemon_notification_unregister
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "!"
+ "@20@0:8i16"
+ "@28@0:8@16i24"
+ "BatteryPacks"
+ "CRDisplayTCONStatus"
+ "DISPLAYTCON_FOLLOWUP_INFO"
+ "DISPLAYTCON_FOLLOWUP_INFO_IPAD"
+ "DISPLAYTCON_FOLLOWUP_TITLE"
+ "DISPLAYTCON_POPUP_INFO"
+ "DISPLAYTCON_POPUP_INFO_IPAD"
+ "Exclave notification handler already registered"
+ "Exclave notification handler not registered, nothing to unregister"
+ "FINISH_BATTERY_REPAIR_DESC_IPAD"
+ "Failed to handle pending EIC strobe notification: %@, error: %d"
+ "Failed to register for EIC strobe notification: %@. Ensure daemon is part of conclave: com.apple.mobilerepaird.conclave"
+ "Handling pending EIC strobe notification synchronously: %@"
+ "InDiagnosticsMode"
+ "MRDisplayTCONComponentHandler"
+ "MRExclaveNotificationHandler"
+ "Processing EIC strobe notification - posting DisplayTCON hardware failure status"
+ "Received EIC strobe daemon notification - marking DisplayTCON as failed"
+ "Registering for EIC strobe daemon notification: %@"
+ "Successfully registered for EIC strobe notification: %@"
+ "Successfully unregistered exclave notification listener"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_notificationQueue"
+ "TB,N,V_isRegistered"
+ "T^{tb_daemon_listener_s=},N,V_notificationListener"
+ "Ti,N,V_componentType"
+ "Unregistering exclave daemon notification listener"
+ "[%s] no finish repair title or message, followup skipped"
+ "[%s] popup skipped"
+ "^{tb_daemon_listener_s=}"
+ "^{tb_daemon_listener_s=}16@0:8"
+ "_checkForComponentFailureInDefaults:"
+ "_componentType"
+ "_isRegistered"
+ "_notificationListener"
+ "_notificationQueue"
+ "com.apple.medina.hw.failure"
+ "com.apple.medina.hw.success"
+ "com.apple.mobilerepair.DisplayTCONRepair"
+ "com.apple.mobilerepaird.eicstrobe"
+ "com.apple.mobilerepaird.exclave.eicstrobe"
+ "componentType"
+ "copySealingManifestDataInstanceForComponentType:"
+ "getInternalName:"
+ "handleExclaveNotification"
+ "handlePendingNotificationSynchronously:"
+ "initWithComponentName:componentType:"
+ "initWithComponentType:"
+ "isBatteryInServiceState:reply:"
+ "isComponentFailed"
+ "isRegistered"
+ "notificationListener"
+ "notificationQueue"
+ "overriddenComponentStatus:"
+ "packIndex %d is out of bounds (count %lu)"
+ "packIndex %d requested but no BatteryPacks found"
+ "registerChangeForComponentType:fdrError:"
+ "registerForNotifications"
+ "setComponentType:"
+ "setIsRegistered:"
+ "setNotificationListener:"
+ "setNotificationQueue:"
+ "settings-navigation://com.apple.Settings.General/About/MAIN_PARTS_AND_SERVICE"
+ "settings-navigation://com.apple.Settings.General/About/MAIN_PARTS_AND_SERVICE/%@"
+ "settings-navigation://com.apple.Settings.General/About/MAIN_PARTS_AND_SERVICE/Battery"
+ "settings-navigation://com.apple.Settings.General/About/MAIN_PARTS_AND_SERVICE/Camera"
+ "settings-navigation://com.apple.Settings.General/About/MAIN_PARTS_AND_SERVICE/TouchController"
+ "unregisterNotifications"
+ "v24@0:8^{tb_daemon_listener_s=}16"
+ "v32@0:8@\"NSNumber\"16@?<v@?B@\"NSError\">24"
- "3kmXfug8VcxLI5yEmsqQKw"
- "BackGlass"
- "Camera"
- "CoverGlass"
- "Enclosure"
- "FaceID"
- "ForceBackGlassStatus"
- "ForceBatteryStatus"
- "ForceCameraStatus"
- "ForceCoverGlassStatus"
- "ForceDisplayStatus"
- "ForceEnclosureStatus"
- "ForceFaceIDStatus"
- "ForceTouchIDStatus"
- "ForceVolumeButtonStatus"
- "T@\"NSString\",&,N,VcomponentForceKey"
- "TouchID"
- "VolumeButton"
- "componentForceKey"
- "copySealingManifestDataInstanceForComponent:"
- "isBatteryInServiceState:"
- "prefs:root=General&path=About/MAIN_PARTS_AND_SERVICE"
- "prefs:root=General&path=About/MAIN_PARTS_AND_SERVICE/%@"
- "prefs:root=General&path=About/MAIN_PARTS_AND_SERVICE/Battery"
- "prefs:root=General&path=About/MAIN_PARTS_AND_SERVICE/Camera"
- "prefs:root=General&path=About/MAIN_PARTS_AND_SERVICE/TouchController"
- "registerChangeForComponent:fdrError:"
- "setComponentForceKey:"

```
