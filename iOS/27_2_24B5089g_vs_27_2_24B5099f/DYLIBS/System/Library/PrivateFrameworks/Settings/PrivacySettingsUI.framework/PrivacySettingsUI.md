## PrivacySettingsUI

> `/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI`

```diff

-2027.1.7.0.0
-  __TEXT.__text: 0x67948
-  __TEXT.__objc_methlist: 0x442c
+2027.1.9.0.0
+  __TEXT.__text: 0x683e8
+  __TEXT.__objc_methlist: 0x4444
   __TEXT.__const: 0x524
-  __TEXT.__gcc_except_tab: 0x130c
-  __TEXT.__cstring: 0x8694
-  __TEXT.__oslogstring: 0x2e70
+  __TEXT.__gcc_except_tab: 0x135c
+  __TEXT.__cstring: 0x87c4
+  __TEXT.__oslogstring: 0x2fb0
   __TEXT.__dlopen_cstrs: 0xe98
   __TEXT.__swift5_typeref: 0x544
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift_as_cont: 0x34
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x1f58
+  __TEXT.__unwind_info: 0x1f88
   __TEXT.__eh_frame: 0x648
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1b48
+  __DATA_CONST.__const: 0x1bc0
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3460
+  __DATA_CONST.__objc_selrefs: 0x3480
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x188
-  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__got: 0xab8
   __AUTH_CONST.__const: 0xad8
   __AUTH_CONST.__cfstring: 0x7360
   __AUTH_CONST.__objc_const: 0x6850
-  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xaf8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2178
-  Symbols:   3778
-  CStrings:  1452
+  Functions: 2189
+  Symbols:   3789
+  CStrings:  1463
 
Symbols:
+ -[PUITrackingReportManager clearTrackingHistoryForBundleIDs:completion:]
+ -[PUITrackingReportManager clearTrackingHistoryWithCompletion:]
+ GCC_except_table37
+ ___63-[PUITrackingReportManager clearTrackingHistoryWithCompletion:]_block_invoke
+ ___72-[PUITrackingReportManager clearTrackingHistoryForBundleIDs:completion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48w_e34_v24?0"NSDictionary"8"NSError"16lw48l8s32l8r40l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0ls32l8w48l8s40l8
+ _kSymptomAnalyticsServiceDomainTrackingClearHistoryBundleIDs
+ _kSymptomAnalyticsServiceDomainTrackingClearHistoryEndDate
+ _kSymptomAnalyticsServiceDomainTrackingClearHistoryKey
+ _kSymptomAnalyticsServiceDomainTrackingClearHistoryStartDate
- ___58-[PUIReportController setRecordActivityEnabled:specifier:]_block_invoke_3
CStrings:
+ "%s: cleared tracking history, outcome: %@"
+ "%s: clearing tracking history for %lu apps"
+ "%s: could not clear the recorded tracking history"
+ "%s: failed to clear tracking history: %@"
+ "%s: failed to enumerate the apps holding tracking records: %@"
+ "%s: failed to send the clear history request"
+ "%s: no tracking records to clear"
+ "-[PUIReportController setRecordActivityEnabled:specifier:]_block_invoke_2"
+ "-[PUITrackingReportManager clearTrackingHistoryForBundleIDs:completion:]"
+ "-[PUITrackingReportManager clearTrackingHistoryForBundleIDs:completion:]_block_invoke"
+ "-[PUITrackingReportManager clearTrackingHistoryWithCompletion:]_block_invoke"
```
