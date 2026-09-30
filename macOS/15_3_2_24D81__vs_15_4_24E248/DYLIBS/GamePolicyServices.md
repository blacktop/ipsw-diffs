## GamePolicyServices

> `/System/Library/PrivateFrameworks/GamePolicyServices.framework/Versions/A/GamePolicyServices`

```diff

-2.2.1.0.0
-  __TEXT.__text: 0x2020
+2.4.2.0.0
+  __TEXT.__text: 0x2124
   __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x1dc
+  __TEXT.__objc_methlist: 0x33c
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__cstring: 0x211
   __TEXT.__oslogstring: 0x1e2
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__unwind_info: 0x130
   __TEXT.__objc_classname: 0x9f
   __TEXT.__objc_methname: 0x83f
   __TEXT.__objc_methtype: 0x225

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_selrefs: 0x2a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0xf0
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x850
+  __AUTH_CONST.__objc_const: 0x5d0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x1e0

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 457E87A8-9F70-3780-88B6-8151BEE258B4
-  Functions: 61
-  Symbols:   247
+  UUID: F24B3F3D-ED77-3968-B35F-C8B6F8B4F0CC
+  Functions: 76
+  Symbols:   262
   CStrings:  199
 
Symbols:
+ +[GPSGameFilter _onqueue_processLaunchTask:mobileAssetInfo:].cold.1
+ +[GPSGameFilter _onqueue_processLaunchTask:mobileAssetInfo:].cold.2
+ +[GPSGameFilter _onqueue_processLaunchTask:mobileAssetInfo:].cold.3
+ +[GPSGameFilter _onqueue_processLaunchTask:mobileAssetInfo:].cold.4
+ +[GPSGameFilter _onqueue_processLaunchTask:mobileAssetInfo:].cold.5
+ +[GPSGameFilter launchTaskQueue].cold.1
+ +[GPSGameFilter queue].cold.1
+ -[GPSMobileAssetRetriever _onqueue_retrieveMobileAsset].cold.2
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __51-[GPSMobileAssetRetriever _onqueue_setupConnection]_block_invoke.5.cold.1
+ __51-[GPSMobileAssetRetriever _onqueue_setupConnection]_block_invoke.cold.1
+ __55-[GPSMobileAssetRetriever _onqueue_retrieveMobileAsset]_block_invoke_2.cold.1
+ getGPSLogger.cold.1
+ gps_isInternalBuild.cold.1

```
