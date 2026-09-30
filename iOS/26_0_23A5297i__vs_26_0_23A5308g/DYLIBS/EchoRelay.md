## EchoRelay

> `/System/Library/PrivateFrameworks/EchoRelay.framework/EchoRelay`

```diff

-59.0.1.0.0
-  __TEXT.__text: 0x1284c
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__const: 0xbc4
+61.0.0.0.0
+  __TEXT.__text: 0x13424
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__const: 0xbd4
   __TEXT.__swift5_typeref: 0x310
   __TEXT.__constg_swiftt: 0x398
   __TEXT.__swift5_reflstr: 0x325
   __TEXT.__swift5_fieldmd: 0x3c8
   __TEXT.__swift5_types: 0x38
-  __TEXT.__cstring: 0x603
+  __TEXT.__cstring: 0x843
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__oslogstring: 0x2fc
+  __TEXT.__oslogstring: 0x4a0
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_capture: 0x88
-  __TEXT.__unwind_info: 0x730
+  __TEXT.__unwind_info: 0x6f0
   __TEXT.__eh_frame: 0x7d0
-  __TEXT.__objc_methname: 0x14c
-  __DATA_CONST.__got: 0x1a0
+  __TEXT.__objc_methname: 0x16e
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x638
+  __DATA_CONST.__objc_selrefs: 0xa0
+  __AUTH_CONST.__auth_got: 0x668
   __AUTH_CONST.__const: 0x398
   __AUTH_CONST.__objc_const: 0x120
   __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x638
-  __DATA.__data: 0x418
+  __AUTH.__data: 0x548
+  __DATA.__data: 0x408
   __DATA.__bss: 0xf00
+  __DATA_DIRTY.__data: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary_AppleInternal.framework/IntelligencePlatformLibrary_AppleInternal

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 11B0D9F5-21CC-3E11-81D0-BC70F272BADC
-  Functions: 655
-  Symbols:   126
-  CStrings:  94
+  UUID: F4B724FD-64CC-383C-A1E2-B09F41108A67
+  Functions: 661
+  Symbols:   130
+  CStrings:  115
 
Symbols:
+ _OBJC_CLASS_$_BMSQLDatabase
+ _OBJC_CLASS_$_NSUUID
+ _objc_retain_x22
+ _objc_retain_x24
CStrings:
+ "'bootUUID' data was not 16 bytes long. It was %ld bytes."
+ "An error occurred during the Biome SQL query: %@"
+ "BMILibrary.GenerativeExperiences.Proactive.UseModelShortcuts"
+ "Failed to retrieve the last boot UUID via SQL. Using fallback."
+ "Last boot UUID retrieved synchronously via SQL: %s"
+ "MLSE.ShareSheet.Feedback"
+ "MLSE.ShareSheet.Inference.PeopleSuggestions"
+ "MLSE.ShareSheet.Metrics.SystemResourceUsage"
+ "No boot session event found."
+ "Results.row was nil or not an NSDictionary."
+ "Row contents: %@"
+ "SELECT bootUUID FROM \"Device.BootSession\" ORDER BY eventTimestamp DESC LIMIT 1"
+ "The key 'bootUUID' was not found in the row using KVC."
+ "UUIDString"
+ "com.apple.pet3.event.GenerativeExperiencesUseModelShortcutsEvent"
+ "com.apple.pet3.event.MLSEShareSheetFeedbackEvent"
+ "com.apple.pet3.event.MLSEShareSheetInferencePeopleSuggestionsEvent"
+ "com.apple.pet3.event.MLSEShareSheetMetricsSystemResourceUsageEvent"
+ "error"
+ "initWithUUIDBytes:"
+ "next"
+ "row"
- "deviceUUID"

```
