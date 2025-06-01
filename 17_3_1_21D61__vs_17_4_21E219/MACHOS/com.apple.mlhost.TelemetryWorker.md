## com.apple.mlhost.TelemetryWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker`

```diff

-1.2.9.0.0
-  __TEXT.__text: 0xc090
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__const: 0x34e
-  __TEXT.__swift5_typeref: 0x1a6
-  __TEXT.__cstring: 0x405
-  __TEXT.__objc_methname: 0x26b
+2.0.12.0.0
+  __TEXT.__text: 0x146cc
+  __TEXT.__auth_stubs: 0xda0
+  __TEXT.__const: 0x3a8
+  __TEXT.__cstring: 0xa49
+  __TEXT.__swift5_typeref: 0x25c
   __TEXT.__swift5_reflstr: 0x11f
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_entry: 0x8
+  __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_fieldmd: 0xb4
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_capture: 0x830
+  __TEXT.__objc_methname: 0x22c
+  __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x204
-  __TEXT.__eh_frame: 0x1e8
-  __DATA_CONST.__auth_got: 0x5a0
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__eh_frame: 0x290
+  __DATA_CONST.__auth_got: 0x6d0
+  __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3f0
+  __DATA_CONST.__const: 0x1878
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xa0
-  __DATA.__objc_classrefs: 0x38
-  __DATA.__data: 0x2d0
-  __DATA.__bss: 0x610
-  __DATA.__common: 0x18
+  __DATA_CONST.__objc_classrefs: 0x30
+  __DATA.__objc_selrefs: 0x80
+  __DATA.__data: 0x2b8
+  __DATA.__bss: 0x520
+  __DATA.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F686CE62-D2DD-3F0C-9F50-8B53828060EC
-  Functions: 157
-  Symbols:   93
-  CStrings:  53
+  UUID: 28A3E6F7-70D7-394E-832D-1013E3161EFD
+  Functions: 364
+  Symbols:   95
+  CStrings:  76
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x27
+ _swift_deallocClassInstance
+ _swift_release_n
+ _swift_setDeallocating
- _OBJC_CLASS_$_NSNumber
- _objc_retain_x10
- _objc_retain_x20
- _objc_retain_x23
- _objc_retain_x28
CStrings:
+ "    contextId=%{public, signpost.telemetry:string1, name=contextId,public}s\n    taskCount=%{public, signpost.telemetry:number1, name=taskCount,public}ld\n    tasksRun=%{public, signpost.telemetry:number2, name=tasksRun,public}ld\n    enableTelemetry=YES"
+ "Already Processed Current Data"
+ "DailyTaskTelemetry"
+ "Deferral during 24-hour loop"
+ "Deferral during 7-day loop"
+ "Division by zero"
+ "Division results in an overflow"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "LedgerRead"
+ "Push Telemetry for %s: %s"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "TotalDuration"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "WeeklyTaskTelemetry"
+ "[Error] Interval already ended"
+ "contextId=%{public, signpost.telemetry:string1, name=contextId,public}s\nenableTelemetry=YES"
+ "contextId=%{public, signpost.telemetry:string1, name=contextId,public}s\nstatus=%{public, signpost.telemetry:string2, name=status,public}s\nenableTelemetry=YES"
+ "contextId=%{public, signpost.telemetry:string1, name=contextId,public}s\ntotalEvents=%{public, signpost.telemetry:number1, name=sleepTime,public}ld\nenableTelemetry=YES"
+ "enableTelemetry=YES"
+ "invalid Collection: less than 'count' elements in collection"
- "crossExecutionDelay"
- "dailyExecutionLatency"
- "executionCompletionTime"
- "executionDeferralTime"
- "executionFailureTime"
- "initWithDouble:"
- "initWithInteger:"
- "initWithLongLong:"
- "latestEventTimestamp"
- "stringValue"

```
