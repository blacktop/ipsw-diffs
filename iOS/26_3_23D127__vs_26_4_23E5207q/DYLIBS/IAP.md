## IAP

> `/System/Library/PrivateFrameworks/IAP.framework/IAP`

```diff

-2173.80.2.0.0
-  __TEXT.__text: 0x10750
+2176.100.2.0.0
+  __TEXT.__text: 0x10828
   __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x184d
-  __TEXT.__cstring: 0x6452
+  __TEXT.__cstring: 0x64d0
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x3b8
+  __TEXT.__unwind_info: 0x3c8
   __TEXT.__objc_classname: 0x85
   __TEXT.__objc_methname: 0x14d9
   __TEXT.__objc_methtype: 0x1bb

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9B56C27-FF43-3020-9C03-D6D76E386652
-  Functions: 320
-  Symbols:   1450
+  UUID: 1A8C05B4-C50E-319A-A5BE-01BE47B17231
+  Functions: 322
+  Symbols:   1454
   CStrings:  1299
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _objc_release_x27
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x27
Functions:
~ __ZL24_GetIAP2DaemonConnectionv.cold.1 : 20 -> 4
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_0
~ -[IAPNavigationAccessory initWithDict:] : 480 -> 492
~ -[IAPNavigationAccessoryComponent initWithDict:] : 536 -> 580
~ -[IAPNavigationAccessoryComponent isEqual:] : 340 -> 336
~ -[IAPNavigation initWithDelegate:] : 504 -> 524
~ ___iap2dServerLaunched : 152 -> 156
~ ___iap2dServerDied : 152 -> 156
~ -[IAPNavigation dealloc] : 168 -> 172
~ -[IAPNavigation updateNavigationGuidanceInfo:forAccessory:withComponent:] : 308 -> 288
~ ___73-[IAPNavigation updateNavigationGuidanceInfo:forAccessory:withComponent:]_block_invoke : 572 -> 580
~ -[IAPNavigation updateNavigationManeuverInfo:forAccessory:withComponent:] : 308 -> 288
~ ___73-[IAPNavigation updateNavigationManeuverInfo:forAccessory:withComponent:]_block_invoke : 572 -> 580
~ ___41-[IAPNavigation _iap2d_server_did_launch]_block_invoke : 204 -> 208
~ ___41-[IAPNavigation _getConnectedAccessories]_block_invoke : 512 -> 524
~ -[IAPNavigation _updateInternalStateWithArrayOfAccessories:] : 3660 -> 3740
~ -[IAPNavigation _convert_xpc_array_to_NSArray:] : 208 -> 216
~ ___47-[IAPNavigation _convert_xpc_array_to_NSArray:]_block_invoke : 416 -> 428
~ ___47-[IAPNavigation _convert_xpc_array_to_NSArray:]_block_invoke_2 : 680 -> 712
~ __ZL21__iap2dServerLaunchedP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary.cold.1 : 20 -> 4
CStrings:
+ "/Library/Caches/com.apple.xbs/DE23EDA2-E688-488B-A1E6-B625658C365D/TemporaryDirectory.To2EnX/Sources/IAPFramework/IAP/IPC_Client/IAPApp.mm"
+ "/Library/Caches/com.apple.xbs/DE23EDA2-E688-488B-A1E6-B625658C365D/TemporaryDirectory.To2EnX/Sources/IAPFramework/common/SharedFunctions.m"
- "/Library/Caches/com.apple.xbs/Sources/IAPFramework/IAP/IPC_Client/IAPApp.mm"
- "/Library/Caches/com.apple.xbs/Sources/IAPFramework/common/SharedFunctions.m"

```
