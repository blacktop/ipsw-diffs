## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Sharing`

```diff

-2088.10.21.0.0
-  __TEXT.__text: 0x302824
+2090.10.1.2.2
+  __TEXT.__text: 0x302c5c
   __TEXT.__auth_stubs: 0x4b50
-  __TEXT.__objc_methlist: 0x1434c
+  __TEXT.__objc_methlist: 0x1437c
   __TEXT.__const: 0x1c3d4
-  __TEXT.__cstring: 0x3b5f6
-  __TEXT.__gcc_except_tab: 0x3490
+  __TEXT.__cstring: 0x3b5e6
+  __TEXT.__gcc_except_tab: 0x34bc
   __TEXT.__oslogstring: 0x97ae
   __TEXT.__dlopen_cstrs: 0x640
   __TEXT.__ustring: 0xf0

   __TEXT.__swift5_mpenum: 0xa8
   __TEXT.__unwind_info: 0xcbe0
   __TEXT.__eh_frame: 0xbab8
-  __TEXT.__objc_classname: 0x1ec8
-  __TEXT.__objc_methname: 0x2cf02
-  __TEXT.__objc_methtype: 0x5e52
-  __TEXT.__objc_stubs: 0x188e0
+  __TEXT.__objc_classname: 0x1ecb
+  __TEXT.__objc_methname: 0x2cfb6
+  __TEXT.__objc_methtype: 0x5e72
+  __TEXT.__objc_stubs: 0x18920
   __DATA_CONST.__got: 0x11f0
-  __DATA_CONST.__const: 0x7600
+  __DATA_CONST.__const: 0x75e0
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x96d0
+  __DATA_CONST.__objc_selrefs: 0x96e8
   __DATA_CONST.__objc_protorefs: 0x1e8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x538
-  __DATA_CONST.__objc_arraydata: 0x478
+  __DATA_CONST.__objc_arraydata: 0x448
   __AUTH_CONST.__auth_got: 0x25c0
-  __AUTH_CONST.__const: 0x13058
+  __AUTH_CONST.__const: 0x13038
   __AUTH_CONST.__cfstring: 0x13900
-  __AUTH_CONST.__objc_const: 0x37410
+  __AUTH_CONST.__objc_const: 0x374e0
   __AUTH_CONST.__objc_intobj: 0x660
-  __AUTH_CONST.__objc_dictobj: 0x640
+  __AUTH_CONST.__objc_dictobj: 0x5c8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0x2a60
   __AUTH.__data: 0x2568
-  __DATA.__objc_ivar: 0x2564
-  __DATA.__data: 0xb928
+  __DATA.__objc_ivar: 0x257c
+  __DATA.__data: 0xb968
   __DATA.__bss: 0x33ab0
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x4258

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
-  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C3F02A8D-0BB6-3DC8-A4D9-69B0C61750A3
-  Functions: 20817
-  Symbols:   37976
-  CStrings:  19980
+  UUID: BC5D5D08-260C-3079-8A53-3E997E8B9FAD
+  Functions: 20824
+  Symbols:   37996
+  CStrings:  19989
 
Symbols:
+ -[SFCompanionXPCManager clearConnection]
+ -[SFDeviceOperationCNJSetup homePodHasCaptiveNetwork]
+ -[SFDeviceOperationCNJSetup setHomePodHasCaptiveNetwork:]
+ -[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:].cold.2
+ -[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:].cold.3
+ -[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:].cold.4
+ -[SFDeviceOperationHandlerCNJSetup reset]
+ GCC_except_table28
+ _OBJC_IVAR_$_SFDeviceOperationCNJSetup._captiveIPAssignError
+ _OBJC_IVAR_$_SFDeviceOperationCNJSetup._homePodHasCaptiveNetwork
+ _OBJC_IVAR_$_SFDeviceOperationHandlerCNJSetup._captiveAuthenticated
+ _OBJC_IVAR_$_SFDeviceOperationHandlerCNJSetup._didAssignIP
+ _OBJC_IVAR_$_SFDeviceOperationHandlerCNJSetup._ipAssignTimeout
+ _OBJC_IVAR_$_SFDeviceOperationHandlerCNJSetup._pathMonitor
+ ___40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.602
+ ___40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.609
+ ___41-[SFDeviceOperationHandlerCNJSetup reset]_block_invoke
+ ___41-[SFDeviceOperationHandlerCNJSetup reset]_block_invoke.cold.1
+ ___68-[SFDeviceAssetManager onqueue_updateMetaDataWithCompletionHandler:]_block_invoke.632
+ ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.637
+ ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.637.cold.1
+ ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke_2.638
+ ___99-[SFDeviceOperationHandlerCNJSetup _handleCaptiveJoinRequestWithResponseHandler:reachabilityError:]_block_invoke_3
+ ___99-[SFDeviceOperationHandlerCNJSetup _handleCaptiveJoinRequestWithResponseHandler:reachabilityError:]_block_invoke_4
+ ___99-[SFDeviceOperationHandlerCNJSetup _handleCaptiveJoinRequestWithResponseHandler:reachabilityError:]_block_invoke_4.cold.1
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"SKEvent"8ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"SKEvent"8lw40l8s32l8
+ ___block_literal_global.1328
+ ___block_literal_global.1332
+ ___block_literal_global.1336
+ ___block_literal_global.1341
+ ___block_literal_global.1345
+ ___block_literal_global.1349
+ ___block_literal_global.1354
+ ___block_literal_global.1358
+ ___block_literal_global.1363
+ ___block_literal_global.1370
+ ___block_literal_global.1377
+ ___block_literal_global.1389
+ ___block_literal_global.1394
+ ___block_literal_global.1398
+ ___block_literal_global.1402
+ ___block_literal_global.1407
+ ___block_literal_global.1412
+ ___block_literal_global.300
+ ___block_literal_global.305
+ ___block_literal_global.715
+ ___block_literal_global.719
+ ___block_literal_global.930
+ ___block_literal_global.934
+ ___block_literal_global.938
+ ___block_literal_global.943
+ __connectionLock
+ _objc_msgSend$clearConnection
+ _objc_msgSend$reset
- GCC_except_table44
- ___40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.605
- ___40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.612
- ___68-[SFDeviceAssetManager onqueue_updateMetaDataWithCompletionHandler:]_block_invoke.635
- ___69-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke
- ___69-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke.cold.1
- ___69-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke.cold.2
- ___69-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke.cold.3
- ___69-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke.cold.4
- ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.640
- ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.640.cold.1
- ___71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke_2.641
- ___block_descriptor_32_e17_v16?0"SKEvent"8l
- ___block_descriptor_40_e8_32w_e17_v16?0"SKEvent"8lw32l8
- ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8ls32l8s40l8w48l8
- ___block_literal_global.1331
- ___block_literal_global.1335
- ___block_literal_global.1339
- ___block_literal_global.1344
- ___block_literal_global.1348
- ___block_literal_global.1352
- ___block_literal_global.1357
- ___block_literal_global.1361
- ___block_literal_global.1366
- ___block_literal_global.1376
- ___block_literal_global.1380
- ___block_literal_global.1392
- ___block_literal_global.1397
- ___block_literal_global.1401
- ___block_literal_global.1405
- ___block_literal_global.1410
- ___block_literal_global.1421
- ___block_literal_global.278
- ___block_literal_global.303
- ___block_literal_global.308
- ___block_literal_global.718
- ___block_literal_global.722
- ___block_literal_global.933
- ___block_literal_global.937
- ___block_literal_global.941
- ___block_literal_global.946
CStrings:
+ "-[SFDeviceOperationHandlerCNJSetup _handleCaptiveJoinRequestWithResponseHandler:reachabilityError:]_block_invoke_4"
+ "-[SFDeviceOperationHandlerCNJSetup reset]_block_invoke"
+ "@\"NSObject<OS_nw_path_monitor>\""
+ "CNJ: IPAssign or Incomplete Captive setup detected, resetting."
+ "Captive IP skip"
+ "Starting Reachability"
+ "TB,N,V_homePodHasCaptiveNetwork"
+ "_captiveAuthenticated"
+ "_captiveIPAssignError"
+ "_didAssignIP"
+ "_homePodHasCaptiveNetwork"
+ "_ipAssignTimeout"
+ "_pathMonitor"
+ "clearConnection"
+ "homePodHasCaptiveNetwork"
+ "setHomePodHasCaptiveNetwork:"
- "-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke"
- "CaptiveMismatchOnly"
- "Reachability check detected mismatch. Skipping captive join"
- "Reachability check timed out. Skipping captive join"
- "Reachability returned error: %@"
- "Reachability succeeded. Skipping captive join"
- "T@\"NSXPCConnection\",&,V_connection"

```
