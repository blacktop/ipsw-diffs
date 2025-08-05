## CoreRepairUI

> `/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`

```diff

-921.0.98.0.0
-  __TEXT.__text: 0x1b684
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x1354
+921.0.119.0.0
+  __TEXT.__text: 0x1b72c
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x136c
   __TEXT.__const: 0x2b6
-  __TEXT.__cstring: 0x2e49
-  __TEXT.__oslogstring: 0xc4e
-  __TEXT.__gcc_except_tab: 0x434
+  __TEXT.__cstring: 0x2f29
+  __TEXT.__oslogstring: 0xc5d
+  __TEXT.__gcc_except_tab: 0x404
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_fieldmd: 0x2c

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x4e0
+  __TEXT.__unwind_info: 0x4d8
   __TEXT.__objc_classname: 0x685
-  __TEXT.__objc_methname: 0x3317
-  __TEXT.__objc_methtype: 0x399
-  __TEXT.__objc_stubs: 0x2c00
-  __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x4b8
+  __TEXT.__objc_methname: 0x33c0
+  __TEXT.__objc_methtype: 0x3a1
+  __TEXT.__objc_stubs: 0x2cc0
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__const: 0x488
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd98
+  __DATA_CONST.__objc_selrefs: 0xdc8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x520
-  __AUTH_CONST.__const: 0x1f8
-  __AUTH_CONST.__cfstring: 0x37e0
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__const: 0x218
+  __AUTH_CONST.__cfstring: 0x38e0
   __AUTH_CONST.__objc_const: 0x2f38
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9066B83A-CA4B-3A04-80BA-1D9A7EC14466
-  Functions: 481
-  Symbols:   2059
-  CStrings:  1669
+  UUID: C11008C2-1B74-3CB1-B768-66BDA15CA619
+  Functions: 486
+  Symbols:   2076
+  CStrings:  1692
 
Symbols:
+ -[CRUIAnalytics sendAsyncAnalyticsForEvent:moduleName:]
+ -[CoreRepairUIUtils _preflight:]
+ -[SystemHealthUI constructSpecifiersWithPrivacySpecifier:rchlHistory:caaHistory:srvp:]
+ GCC_except_table30
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSThread
+ ___32-[CoreRepairUIUtils _preflight:]_block_invoke
+ ___36-[CoreRepairUIUtils getRepairTicket]_block_invoke.121
+ ___44-[CoreRepairUIUtils isBatteryInServiceState]_block_invoke.153
+ ___44-[CoreRepairUIUtils isBatteryInServiceState]_block_invoke.153.cold.1
+ ___52-[MRUINotificationHelper updateFollowupsToNewLocale]_block_invoke.cold.1
+ ___52-[MRUINotificationHelper updateFollowupsToNewLocale]_block_invoke.cold.2
+ ___55-[CRUIAnalytics sendAsyncAnalyticsForEvent:moduleName:]_block_invoke
+ ___55-[CRUIAnalytics sendAsyncAnalyticsForEvent:moduleName:]_block_invoke_2
+ ___56-[SystemHealthUI getCurrentDetailsWithPrivacySpecifier:]_block_invoke.257
+ ___56-[SystemHealthUI updateSpecifiersWithCompletionHandler:]_block_invoke.290
+ ___block_descriptor_32_e37_v28?0B8"NSDictionary"12"NSError"20l
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.129
+ ___block_literal_global.152
+ _objc_msgSend$_preflight:
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$constructSpecifiersWithPrivacySpecifier:rchlHistory:caaHistory:srvp:
+ _objc_msgSend$groupStandardUserDefaults
+ _objc_msgSend$groupUserDefaultsWithSuiteName:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$sendAsyncAnalyticsForEvent:moduleName:
+ _objc_retain_x26
- -[CoreRepairUIUtils performMiniPreflightWith:]
- GCC_except_table11
- GCC_except_table17
- GCC_except_table31
- ___36-[CoreRepairUIUtils getRepairTicket]_block_invoke.106
- ___44-[CoreRepairUIUtils isBatteryInServiceState]_block_invoke.133
- ___44-[CoreRepairUIUtils isBatteryInServiceState]_block_invoke.133.cold.1
- ___51-[CoreRepairUIUtils performBackGroundMiniPreflight]_block_invoke_2
- ___52-[MRUINotificationHelper updateFollowupsToNewLocale]_block_invoke_2
- ___52-[MRUINotificationHelper updateFollowupsToNewLocale]_block_invoke_2.cold.1
- ___52-[MRUINotificationHelper updateFollowupsToNewLocale]_block_invoke_2.cold.2
- ___56-[SystemHealthUI updateSpecifiersWithCompletionHandler:]_block_invoke.288
- ___57-[CoreRepairUIUtils performInteractiveMiniPreflightWith:]_block_invoke_2
- ___block_descriptor_40_e8_32r_e37_v28?0B8"NSDictionary"12"NSError"20lr32l8
- ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
- ___block_literal_global.132
- _objc_msgSend$pendingFollowUpItemsWithCompletion:
- _objc_msgSend$performInteractiveMiniPreflightWith:
CStrings:
+ "-[CRUIAnalytics sendAsyncAnalyticsForEvent:moduleName:]_block_invoke_2"
+ "/System/Library/PrivateFrameworks/CoreRepairUI.framework/"
+ "@40@0:8@16#24@32"
+ "@44@0:8B16@20@28@36"
+ "ApplicationIcon"
+ "BackGroundPreflight"
+ "BootIntent"
+ "InteractivePreflight"
+ "PartsAndServiceHistory"
+ "PreflightDone"
+ "PreflightError"
+ "_preflight:"
+ "bundleWithPath:"
+ "constructSpecifiersWithPrivacySpecifier:rchlHistory:caaHistory:srvp:"
+ "groupStandardUserDefaults"
+ "groupUserDefaultsWithSuiteName:"
+ "icns"
+ "iconpath is:%@"
+ "isMainThread"
+ "pathForResource:ofType:"
+ "sendAsyncAnalyticsForEvent:moduleName:"
- "\n%@\n"
- "@40@0:8@16@24@32"
- "B24@0:8@?16"
- "pendingFollowUpItemsWithCompletion:"
- "performMiniPreflightWith:"
- "v24@?0@\"NSArray\"8@\"NSError\"16"

```
