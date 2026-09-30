## FMCore

> `/System/Library/PrivateFrameworks/FMCore.framework/Versions/A/FMCore`

```diff

-214.22.7.13.3
-  __TEXT.__text: 0x15c1c
+214.24.7.11.9
+  __TEXT.__text: 0x15bdc
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x1890
+  __TEXT.__objc_methlist: 0x1af4
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x370
   __TEXT.__cstring: 0xe12
   __TEXT.__oslogstring: 0x1273
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x738
+  __TEXT.__unwind_info: 0x768
   __TEXT.__objc_classname: 0x2d3
   __TEXT.__objc_methname: 0x4251
   __TEXT.__objc_methtype: 0xaa7

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1230
+  __DATA_CONST.__objc_selrefs: 0x1310
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x8d0
   __AUTH_CONST.__cfstring: 0x1120
-  __AUTH_CONST.__objc_const: 0x34b8
+  __AUTH_CONST.__objc_const: 0x3058
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x960
   __DATA.__objc_ivar: 0x194

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A5FEEB81-FE0B-3665-9E66-ABB3AA3DA399
-  Functions: 689
-  Symbols:   1918
+  UUID: 21F14CB2-CE66-3FB3-B55F-EFAD52108F54
+  Functions: 709
+  Symbols:   1938
   CStrings:  1379
 
Symbols:
+ +[FMAlertManager sharedInstance].cold.1
+ +[FMNetworkMonitor sharedInstance].cold.1
+ +[FMOwnerAccount sharedInstance].cold.1
+ +[FMSystemInfo sharedInstance].cold.1
+ +[FMXPCNotificationsUtil sharedInstance].cold.1
+ +[FMXPCTransactionManager sharedInstance].cold.1
+ -[FMServerInteractionController _simulatedLatency].cold.1
+ -[FMSystemInfo_osx productName].cold.1
+ -[NSString(FMCoreAdditions) legacyAllowedCharacterSet].cold.1
+ LogCategory_APS.cold.1
+ LogCategory_FMRunLoopMonitor.cold.1
+ LogCategory_FMSynchronizer.cold.1
+ LogCategory_FMXPCActivity.cold.1
+ LogCategory_FMXPCBridge.cold.1
+ LogCategory_Networking.cold.1
+ LogCategory_NetworkingVerbose.cold.1
+ LogCategory_ServerError.cold.1
+ LogCategory_SharedFileContainer.cold.1
+ LogCategory_Unspecified.cold.1
+ nanosecondTimestamp.cold.1

```
