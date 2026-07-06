## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-  __TEXT.__text: 0x16cfc
-  __TEXT.__objc_methlist: 0x9f0
-  __TEXT.__const: 0x260
+  __TEXT.__text: 0x174f0
+  __TEXT.__objc_methlist: 0x9fc
+  __TEXT.__const: 0x268
   __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__cstring: 0x43cf
-  __TEXT.__oslogstring: 0x2bc8
+  __TEXT.__cstring: 0x4534
+  __TEXT.__oslogstring: 0x2bf4
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x5a8
+  __TEXT.__unwind_info: 0x5c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1768
+  __DATA_CONST.__const: 0x17b8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa20
+  __DATA_CONST.__objc_selrefs: 0xa58
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x1d8
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x5a40
-  __AUTH_CONST.__objc_const: 0x1a68
+  __DATA_CONST.__got: 0x1f0
+  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__cfstring: 0x5b80
+  __AUTH_CONST.__objc_const: 0x1a98
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x5c8
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1f0
-  __DATA.__data: 0x218
+  __AUTH_CONST.__auth_got: 0x5f0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x1f4
+  __DATA.__data: 0x220
   __DATA.__common: 0x18
-  __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 571
-  Symbols:   2122
-  CStrings:  1698
+  Functions: 588
+  Symbols:   2191
+  CStrings:  1723
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ -[HTPrefs shouldMonitorCPURoleForAppExtensions]
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _HTAnalyticsShouldReportBundleID.sDeviceIdentifier
+ _HTAnalyticsShouldReportBundleID.sDeviceIdentifierOnce
+ _HTCPURoleMonitoringDenylist.denylist
+ _HTCPURoleMonitoringDenylist.onceToken
+ _HTReportSignpostStateForBundleID
+ _HTSamplingQueue.once
+ _HTSamplingQueue.q
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_HTPrefs._shouldMonitorCPURoleForAppExtensions
+ ___HTAnalyticsShouldReportBundleID_block_invoke
+ ___HTCPURoleMonitoringDenylist_block_invoke
+ ___HTReportSignpostStateForBundleID_block_invoke
+ ___HTReportSignpostStateForBundleID_block_invoke_2
+ ___HTSamplingQueue_block_invoke
+ ___block_descriptor_41_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___tailspinBoostingSignpost_block_invoke
+ ___tailspinProcessingSignpost_block_invoke
+ __block_invoke.sLastReportedState
+ _disableProcess
+ _gettimeofday
+ _kHTCoreAnalyticsHangSignpostsEnabled
+ _kHTDoneProcessingTailspinNotification
+ _kHTExtendedAttributeIsBoosted
+ _kHTExtendedAttributeTailspinPath
+ _kHTPrefsShouldMonitorCPURoleForAppExtensions
+ _kHTServiceMessageNameBoostTask
+ _localtime_r
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$deviceIdentifierForVendor
+ _objc_msgSend$enableLoggingForPoster
+ _objc_msgSend$enableLoggingForWidgetRenderer
+ _objc_msgSend$extensionPointRecord
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$initWithBundleIdentifier:error:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$shouldMonitorCPURoleForAppExtensions
+ _shouldMonitorCPURoleForProcessBundleID
+ _tailspinBoostingSignpost
+ _tailspinBoostingSignpost.onceToken
+ _tailspinBoostingSignpost.signpostLog
+ _tailspinProcessingSignpost
+ _tailspinProcessingSignpost.onceToken
+ _tailspinProcessingSignpost.signpostLog
- ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
- ___signpostHangInterval_block_invoke
- ___signpostHangInterval_block_invoke_2
- _signpostHangInterval.onceToken
CStrings:
+ "PosterBoard"
+ "Should sample bundleID:%@ for telemetry: %@"
+ "ShouldMonitorCPURoleForAppExtensions"
+ "WidgetRenderer-Default"
+ "Yes"
+ "boost-task"
+ "com.apple.chrono.WidgetRenderer-Default"
+ "com.apple.hangreporter.doneProcessingTailspin"
+ "com.apple.hangtracer.sampling-helper"
+ "com.apple.posterkit.provider"
+ "enabled"
+ "hangreporter_tailspin_boosting"
+ "hangreporter_tailspin_processing"
+ "hangtracer.isBoosted"
+ "hangtracer.tailspin_path"

```
