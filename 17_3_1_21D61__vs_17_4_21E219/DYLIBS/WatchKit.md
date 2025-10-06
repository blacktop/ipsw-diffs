## WatchKit

> `/System/Library/Frameworks/WatchKit.framework/WatchKit`

```diff

 892.25.0.0.0
-  __TEXT.__text: 0x36da4
+  __TEXT.__text: 0x36da8
   __TEXT.__auth_stubs: 0x8d0
   __TEXT.__objc_methlist: 0x3b10
   __TEXT.__const: 0xa8

   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__unwind_info: 0xe24
   __TEXT.__objc_classname: 0x761
-  __TEXT.__objc_methname: 0x7f78
+  __TEXT.__objc_methname: 0x7f8e
   __TEXT.__objc_methtype: 0xe92
   __TEXT.__objc_stubs: 0x4b20
   __DATA_CONST.__got: 0xf8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x60f0
   __DATA_CONST.__objc_selrefs: 0x1f30
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x310
+  __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__cfstring: 0x4c20
   __AUTH_CONST.__objc_const: 0x1900
   __AUTH_CONST.__const: 0x3a0

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x478
   __AUTH.__objc_data: 0x14a0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x310
-  __DATA.__objc_superrefs: 0x130
   __DATA.__objc_ivar: 0x2e8
   __DATA.__data: 0x498
   __DATA.__bss: 0x350

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA891FDF-A3C4-3C04-9AAC-D823DC9E963B
+  UUID: 5B7038D0-77DE-35AB-83CE-4B86C576899C
   Functions: 1665
   Symbols:   5644
-  CStrings:  3202
+  CStrings:  3203
 
Symbols:
+ ___111-[SPRemoteInterface applicationHandleWatchTaskKeys:reasonForSnapshot:visibleVCID:barTaskUUID:clientIdentifier:]_block_invoke.277
+ ___115-[SPRemoteInterface createViewController:className:properties:contextID:info:gestureDescriptions:clientIdentifier:]_block_invoke.245
+ ___115-[SPRemoteInterface createViewController:className:properties:contextID:info:gestureDescriptions:clientIdentifier:]_block_invoke.255.cold.1
+ ___115-[SPRemoteInterface createViewController:className:properties:contextID:info:gestureDescriptions:clientIdentifier:]_block_invoke.256
+ ___115-[SPRemoteInterface createViewController:className:properties:contextID:info:gestureDescriptions:clientIdentifier:]_block_invoke_2.246
+ ___129-[SPRemoteInterface _handleAction:forNotification:remoteNotificationContext:localNotification:unNotification:handler:controller:]_block_invoke.284
+ ___129-[SPRemoteInterface _handleAction:forNotification:remoteNotificationContext:localNotification:unNotification:handler:controller:]_block_invoke.288
+ ___129-[SPRemoteInterface _handleAction:forNotification:remoteNotificationContext:localNotification:unNotification:handler:controller:]_block_invoke_2.285
+ ___52-[SPDeviceConnection createXPCConnectionIfNecessary]_block_invoke.80
+ ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke.238
+ ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke.242
+ ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke_2.239
+ ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke_3.240
+ ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke_4.241
+ ___SPGetCompanionExtensionPIDForCompanionAppWithIdentifier_block_invoke.116
+ ___SPGetSockPuppetAppRunningStatusForCompanionAppWithIdentifier_block_invoke.114
+ ___SPLaunchSockPuppetAppForCompanionAppWithIdentifier_block_invoke.100
+ ___SPTerminateSockPuppetAppForCompanionAppWithIdentifier_block_invoke.112.cold.1
+ ___SPTerminateSockPuppetAppForCompanionAppWithIdentifier_block_invoke.113
+ ___SPXcodeWillInstallSockPuppetAppWithCompanionAppIdentifier_block_invoke.118
+ ___block_literal_global.142
+ ___block_literal_global.159
+ ___block_literal_global.162
+ ___block_literal_global.204
+ ___block_literal_global.251
+ ___block_literal_global.290
+ ___block_literal_global.551
+ ___block_literal_global.88
+ ___block_literal_global.90
+ ___block_literal_global.96
+ ___block_literal_global.99
+ ___getXcodeSupportRemoteObjectProxy_block_invoke.99
- ___111-[SPRemoteInterface applicationHandleWatchTaskKeys:reasonForSnapshot:visibleVCID:barTaskUUID:clientIdentifier:]_block_invoke.276
- ___115-[SPRemoteInterface createViewController:className:properties:contextID:info:gestureDescriptions:clientIdentifier:]_block_invoke.244
- ___115-[SPRemoteInterface createViewController:className:properties:contextID:info:gestureDescriptions:clientIdentifier:]_block_invoke.254
- ___115-[SPRemoteInterface createViewController:className:properties:contextID:info:gestureDescriptions:clientIdentifier:]_block_invoke.254.cold.1
- ___115-[SPRemoteInterface createViewController:className:properties:contextID:info:gestureDescriptions:clientIdentifier:]_block_invoke_2.245
- ___129-[SPRemoteInterface _handleAction:forNotification:remoteNotificationContext:localNotification:unNotification:handler:controller:]_block_invoke.283
- ___129-[SPRemoteInterface _handleAction:forNotification:remoteNotificationContext:localNotification:unNotification:handler:controller:]_block_invoke.287
- ___129-[SPRemoteInterface _handleAction:forNotification:remoteNotificationContext:localNotification:unNotification:handler:controller:]_block_invoke_2.284
- ___52-[SPDeviceConnection createXPCConnectionIfNecessary]_block_invoke.79
- ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke.236
- ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke.241
- ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke_2.238
- ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke_3.239
- ___58-[SPRemoteInterface handlePlistDictionary:fromIdentifier:]_block_invoke_4.240
- ___SPGetCompanionExtensionPIDForCompanionAppWithIdentifier_block_invoke.115
- ___SPGetSockPuppetAppRunningStatusForCompanionAppWithIdentifier_block_invoke.113
- ___SPLaunchSockPuppetAppForCompanionAppWithIdentifier_block_invoke.99
- ___SPTerminateSockPuppetAppForCompanionAppWithIdentifier_block_invoke.111
- ___SPTerminateSockPuppetAppForCompanionAppWithIdentifier_block_invoke.111.cold.1
- ___SPXcodeWillInstallSockPuppetAppWithCompanionAppIdentifier_block_invoke.117
- ___block_literal_global.141
- ___block_literal_global.158
- ___block_literal_global.161
- ___block_literal_global.203
- ___block_literal_global.250
- ___block_literal_global.289
- ___block_literal_global.550
- ___block_literal_global.87
- ___block_literal_global.89
- ___block_literal_global.95
- ___block_literal_global.98
- ___getXcodeSupportRemoteObjectProxy_block_invoke.98
CStrings:
+ "T@\"NSString\",?,R,C"

```
