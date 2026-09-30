## nanosystemsettingsd

> `/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd`

```diff

-366.0.0.0.0
-  __TEXT.__text: 0x1dd60
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_stubs: 0x3cc0
-  __TEXT.__objc_methlist: 0x1be4
+369.0.0.0.0
+  __TEXT.__text: 0x20430
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_stubs: 0x3da0
+  __TEXT.__objc_methlist: 0x1c44
   __TEXT.__const: 0xe2
-  __TEXT.__oslogstring: 0x2535
-  __TEXT.__objc_classname: 0x26e
+  __TEXT.__oslogstring: 0x25e1
+  __TEXT.__objc_classname: 0x284
   __TEXT.__objc_methtype: 0x141f
-  __TEXT.__cstring: 0x17fc
-  __TEXT.__objc_methname: 0x64af
-  __TEXT.__gcc_except_tab: 0xf8
+  __TEXT.__cstring: 0x1841
+  __TEXT.__objc_methname: 0x6577
+  __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__swift5_typeref: 0x15
-  __TEXT.__unwind_info: 0x4f8
-  __DATA_CONST.__auth_got: 0x4a8
-  __DATA_CONST.__got: 0x5f0
+  __TEXT.__unwind_info: 0x708
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x600
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x870
-  __DATA_CONST.__cfstring: 0x1380
+  __DATA_CONST.__cfstring: 0x13a0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x3ad8
-  __DATA.__objc_selrefs: 0x17a8
+  __DATA.__objc_const: 0x3ae0
+  __DATA.__objc_selrefs: 0x17e0
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x5c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FF47B9B0-76A1-35E6-B1EE-D9D0184B4F02
-  Functions: 540
-  Symbols:   366
-  CStrings:  1689
+  UUID: B96E3BE6-6554-3149-8816-85A9F216165F
+  Functions: 551
+  Symbols:   370
+  CStrings:  1703
 
Symbols:
+ _NSSAirplaneModeReqMsgReadFrom
+ _NSSDisableAirplaneModeMsgReadFrom
+ _OBJC_CLASS_$_NSSAirplaneModeReqMsg
+ _OBJC_CLASS_$_NSSDisableAirplaneModeMsg
+ __os_feature_enabled_impl
+ _objc_release_x2
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
CStrings:
+ "-[NSSCompanionServer handleAirplaneModeMsg:]"
+ "E7995851-332F-481C-B7DE-7E80973B07BF"
+ "Launching; \"NanoSystemSettingsDaemon-369\" \"2141\""
+ "NanoPhone"
+ "Not in a valid configuration to send APM message to paired device."
+ "RadiosPreferencesAirplaneModeDidChangeNotification"
+ "Received Airplane Mode state request"
+ "Received Disable Airplane Mode request"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_airplaneModeQueue"
+ "airplaneModeChanged"
+ "handleAirplandModeStateReqMsg:"
+ "handleDisableAirplaneModeReqMsg:"
+ "hasModifyAirplaneModeEntitlement"
+ "isRemoteAirplaneModeManagementEnabled"
+ "kAirplaneModeQueueOneIdentifier"
+ "nearbyDevicesChanged:"
+ "remoteAirplaneModeManagement"
+ "service: (%@), devices: (%@)"
- "-[NSSServer handleAirplaneModeMsg:]"
- "E7995851-D32D-4A4F-B12C-3DD8D0252581"
- "Launching; \"NanoSystemSettingsDaemon-366\" \"6709\""
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_airplaneModeQueue"
- "setAirplaneModeQueue:"

```
