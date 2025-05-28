## HealthRecordsDaemon

> `/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x2cffe0
-  __TEXT.__auth_stubs: 0x2d30
+4146.4.18.0.0
+  __TEXT.__text: 0x2d6678
+  __TEXT.__auth_stubs: 0x2d50
   __TEXT.__objc_methlist: 0x3d4
-  __TEXT.__const: 0x15758
-  __TEXT.__cstring: 0xe75f
+  __TEXT.__const: 0x15748
+  __TEXT.__cstring: 0xe80f
   __TEXT.__constg_swiftt: 0x69b8
   __TEXT.__swift5_typeref: 0x4611
   __TEXT.__swift5_builtin: 0x208

   __TEXT.__swift5_capture: 0x22f0
   __TEXT.__swift5_protos: 0x5c
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0xac20
-  __TEXT.__eh_frame: 0x8ec0
+  __TEXT.__unwind_info: 0xb378
+  __TEXT.__eh_frame: 0x8ee8
   __TEXT.__objc_classname: 0x187
-  __TEXT.__objc_methname: 0x3017
+  __TEXT.__objc_methname: 0x3009
   __TEXT.__objc_methtype: 0x7a0
-  __DATA_CONST.__got: 0xbf8
+  __DATA_CONST.__got: 0xbf0
   __DATA_CONST.__const: 0x1458
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5498
-  __DATA_CONST.__objc_selrefs: 0xf50
+  __DATA_CONST.__objc_selrefs: 0xf48
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0x428
   __AUTH_CONST.__const: 0xdbb0
-  __AUTH_CONST.__auth_ptr: 0x4b8
+  __AUTH_CONST.__auth_ptr: 0x4a0
   __AUTH_CONST.__objc_const: 0x2c0
-  __AUTH_CONST.__auth_got: 0x1698
-  __AUTH.__data: 0x9148
+  __AUTH_CONST.__auth_got: 0x16a8
+  __AUTH.__data: 0x8fb8
   __AUTH.__objc_data: 0x12f8
-  __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x428
-  __DATA.__data: 0x7c90
-  __DATA.__bss: 0x211e0
+  __DATA.__data: 0x9968
+  __DATA.__bss: 0x20e60
   __DATA.__common: 0x50
   __DATA_DIRTY.__const: 0x80
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__data: 0x1b68
-  __DATA_DIRTY.__bss: 0x800
+  __DATA_DIRTY.__data: 0x21c8
+  __DATA_DIRTY.__bss: 0xb80
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17172
-  Symbols:   2807
-  CStrings:  2353
+  Functions: 17293
+  Symbols:   2811
+  CStrings:  2362
 
Symbols:
+ _block_copy_helper.25
+ _block_copy_helper.31
+ _block_descriptor.27
+ _block_descriptor.33
+ _block_destroy_helper.26
+ _block_destroy_helper.32
+ _objectdestroy.26Tm
- _block_copy_helper.16
- _block_copy_helper.28
- _block_copy_helper.34
- _block_descriptor.18
- _block_descriptor.30
- _block_descriptor.36
- _block_destroy_helper.17
- _block_destroy_helper.29
- _block_destroy_helper.35
- _objectdestroy.27Tm
CStrings:
+ ".ActivitySummary"
+ ".HKReminderWeekdayOptions"
+ "Can't construct Array with count < 0"
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Negative value is not representable"
+ "Not enough bits to represent the passed value"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"
- "com.apple.health.oslo.data.ActivitySummarySeries.ActivitySummary"
- "com.apple.health.oslo.data.CategorySeries.Event"
- "com.apple.health.oslo.data.CategorySeries.Range"
- "com.apple.health.oslo.data.CycleTracking.Cycle"
- "com.apple.health.oslo.data.CycleTracking.Event"
- "com.apple.health.oslo.data.CycleTracking.Range"
- "com.apple.health.oslo.data.CycleTracking.SexualActivity"
- "com.apple.health.oslo.data.HKMedicationScheduleIntervalData.HKReminderWeekdayOptions"
- "com.apple.health.oslo.data.HistogramSeries.Value"
- "com.apple.health.oslo.data.PatientMeta.CHRMeta"
- "com.apple.health.oslo.data.PatientMeta.HeartRateMeds"
- "com.apple.health.oslo.data.PatientMeta.HumanName"
- "com.apple.health.oslo.data.SleepSeries.Value"
- "com.apple.health.oslo.data.SleepSummary.Schedule"
- "com.apple.health.oslo.data.TimeSeries.Value"
- "setAllowsExpensiveNetworkAccess:"

```
