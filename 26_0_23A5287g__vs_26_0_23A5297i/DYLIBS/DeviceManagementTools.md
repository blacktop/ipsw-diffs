## DeviceManagementTools

> `/System/Library/PrivateFrameworks/DeviceManagementTools.framework/DeviceManagementTools`

```diff

-76.0.0.0.0
-  __TEXT.__text: 0x1757c
+77.0.0.0.0
+  __TEXT.__text: 0x1767c
   __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0x20ac
+  __TEXT.__objc_methlist: 0x20ec
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x2001
+  __TEXT.__cstring: 0x2025
   __TEXT.__ustring: 0x55e
   __TEXT.__oslogstring: 0x1b25
   __TEXT.__gcc_except_tab: 0x380
-  __TEXT.__unwind_info: 0x740
-  __TEXT.__objc_classname: 0x964
-  __TEXT.__objc_methname: 0x525f
-  __TEXT.__objc_methtype: 0xe60
-  __TEXT.__objc_stubs: 0x36e0
-  __DATA_CONST.__got: 0x208
+  __TEXT.__unwind_info: 0x750
+  __TEXT.__objc_classname: 0x966
+  __TEXT.__objc_methname: 0x5333
+  __TEXT.__objc_methtype: 0xe83
+  __TEXT.__objc_stubs: 0x3740
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0x8c8
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10c8
+  __DATA_CONST.__objc_selrefs: 0x10f0
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x2480
-  __AUTH_CONST.__objc_const: 0x5160
+  __AUTH_CONST.__cfstring: 0x24a0
+  __AUTH_CONST.__objc_const: 0x5200
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0x27c
+  __DATA.__objc_ivar: 0x280
   __DATA.__data: 0xa80
   __DATA.__bss: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F75A1B7-B8CE-377F-BB8B-941569B0E318
-  Functions: 740
-  Symbols:   2996
-  CStrings:  1808
+  UUID: 0C11B783-5ADD-382F-807F-FC400B42E235
+  Functions: 744
+  Symbols:   3009
+  CStrings:  1818
 
Symbols:
+ +[DMTPairingConstants deviceContextDidUpdateNotification]
+ +[DMTPairingConstants productTypeKey]
+ -[DMTBuddyDaemonProximityAutomatedDeviceEnrollmentController remoteHostLocaleIdentifier]
+ -[DMTSharingBackedRemoteSetupBroadcaster broadcastPrimitives]
+ -[DMTSharingBackedRemoteSetupBroadcaster remoteHostLocaleIdentifier]
+ -[DMTSharingBroadcastPrimitives remoteHostLocaleIdentifier]
+ -[DMTSharingBroadcastPrimitives setRemoteHostLocaleIdentifier:]
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_IVAR_$_DMTSharingBackedRemoteSetupBroadcaster._broadcastPrimitives
+ _OBJC_IVAR_$_DMTSharingBroadcastPrimitives._remoteHostLocaleIdentifier
+ ___101-[DMTCatalystSharingBackedDeviceSession sendRequestID:unencryptedRequestData:withTimeout:completion:]_block_invoke.27
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.31
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.31.cold.1
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.32
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.32.cold.1
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.32.cold.2
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$deviceContextDidUpdateNotification
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$productTypeKey
+ _objc_msgSend$remoteHostLocaleIdentifier
+ _objc_msgSend$setContext:
+ _objc_msgSend$setRemoteHostLocaleIdentifier:
- -[DMTSharingBroadcastPrimitives remoteLocaleIdentifier]
- -[DMTSharingBroadcastPrimitives setRemoteLocaleIdentifier:]
- -[DMTSharingDevice updateDeviceContext:]
- _OBJC_IVAR_$_DMTSharingBroadcastPrimitives._remoteLocaleIdentifier
- ___101-[DMTCatalystSharingBackedDeviceSession sendRequestID:unencryptedRequestData:withTimeout:completion:]_block_invoke.26
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.34.cold.1
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.35
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.35.cold.1
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.35.cold.2
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.37
- _objc_msgSend$remoteLocaleIdentifier
- _objc_msgSend$setDeviceContext:
- _objc_msgSend$setRemoteLocaleIdentifier:
- _objc_msgSend$updateDeviceContext:
CStrings:
+ "@\"<CATSharingBroadcastPrimitives>\""
+ "T@\"<CATSharingBroadcastPrimitives>\",R,N,V_broadcastPrimitives"
+ "T@\"NSString\",&,N,V_remoteHostLocaleIdentifier"
+ "_broadcastPrimitives"
+ "_deviceContextDidUpdateNotification"
+ "_remoteHostLocaleIdentifier"
+ "broadcastPrimitives"
+ "defaultCenter"
+ "deviceContextDidUpdateNotification"
+ "postNotificationName:object:userInfo:"
+ "productTypeKey"
+ "remoteHostLocaleIdentifier"
+ "setContext:"
+ "setRemoteHostLocaleIdentifier:"
- "T@\"NSString\",&,N,V_remoteLocaleIdentifier"
- "_remoteLocaleIdentifier"
- "remoteLocaleIdentifier"
- "setRemoteLocaleIdentifier:"
- "updateDeviceContext:"

```
