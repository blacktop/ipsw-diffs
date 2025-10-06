## com.apple.mlhost.TelemetryWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker`

```diff

-2.0.12.0.0
-  __TEXT.__text: 0x146cc
-  __TEXT.__auth_stubs: 0xda0
-  __TEXT.__const: 0x3a8
-  __TEXT.__cstring: 0xa49
-  __TEXT.__swift5_typeref: 0x25c
-  __TEXT.__swift5_reflstr: 0x11f
-  __TEXT.__swift5_assocty: 0x48
+3.0.10.0.0
+  __TEXT.__text: 0x5cac
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__const: 0x242
+  __TEXT.__cstring: 0x535
+  __TEXT.__swift5_typeref: 0xcb
+  __TEXT.__swift5_reflstr: 0x46
+  __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_fieldmd: 0xb4
-  __TEXT.__swift5_capture: 0x830
-  __TEXT.__objc_methname: 0x22c
-  __TEXT.__swift5_proto: 0x28
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x2e0
-  __TEXT.__eh_frame: 0x290
-  __DATA_CONST.__auth_got: 0x6d0
-  __DATA_CONST.__got: 0x190
+  __TEXT.__constg_swiftt: 0x44
+  __TEXT.__swift5_fieldmd: 0x50
+  __TEXT.__objc_methname: 0x1bd
+  __TEXT.__swift5_capture: 0x40
+  __TEXT.__swift5_proto: 0x1c
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0x1a4
+  __TEXT.__eh_frame: 0x220
+  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1878
+  __DATA_CONST.__const: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x30
-  __DATA.__objc_selrefs: 0x80
-  __DATA.__data: 0x2b8
-  __DATA.__bss: 0x520
-  __DATA.__common: 0x48
+  __DATA_CONST.__objc_classrefs: 0x20
+  __DATA.__objc_selrefs: 0x58
+  __DATA.__data: 0xf8
+  __DATA.__bss: 0x390
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7557353A-2D66-3224-81FA-A46585612A01
-  Functions: 364
-  Symbols:   95
-  CStrings:  76
+  UUID: C8092121-4C61-39E4-8F5B-F2FD329F6FF8
+  Functions: 107
+  Symbols:   79
+  CStrings:  44
 
Symbols:
+ _objc_retain_x19
+ _objc_retain_x20
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_CLASS_$_NSTextCheckingResult
- __os_signpost_emit_with_name_impl
- __swiftEmptyDictionarySingleton
- _bzero
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x27
- _swift_arrayInitWithCopy
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_beginAccess
- _swift_deallocClassInstance
- _swift_errorRelease
- _swift_getTypeByMangledNameInContextInMetadataState2
- _swift_release_n
- _swift_setDeallocating
- _swift_willThrow
CStrings:
+ "%s Output: %s"
+ "CUSTOM EVENT: %s"
+ "Device Telemetry Output: %s"
+ "Processing custom telemetry"
+ "Push Telemetry Output: %s"
- "    contextId=%{public, signpost.telemetry:string1, name=contextId,public}s\n    taskCount=%{public, signpost.telemetry:number1, name=taskCount,public}ld\n    tasksRun=%{public, signpost.telemetry:number2, name=tasksRun,public}ld\n    enableTelemetry=YES"
- "(?=(N[^N]*N))"
- "(D[^C]*C)"
- "(D[^C]*[CF])"
- "(F[^F]*F)"
- "(RC)"
- "(RD)"
- "(RF)"
- "24-hour Output: %s"
- "7-day Output: %s"
- "Adjusting startTimestamp using UserDefaults timestamp: %f"
- "Already Processed Current Data"
- "DailyTaskTelemetry"
- "Deferral during 24-hour loop"
- "Deferral during 7-day loop"
- "Division by zero"
- "Division results in an overflow"
- "Events For Matching: %s | %ld, Regex: %s"
- "LedgerRead"
- "Match: %s | Indices: %ld, %ld"
- "Processing device telemetry for bucket: %s"
- "Push Telemetry for %s: %s"
- "Swift/IntegerTypes.swift"
- "TotalDuration"
- "UnsafeMutablePointer.initialize with negative count"
- "WeeklyTaskTelemetry"
- "[Error] Interval already ended"
- "contextId=%{public, signpost.telemetry:string1, name=contextId,public}s\nenableTelemetry=YES"
- "contextId=%{public, signpost.telemetry:string1, name=contextId,public}s\nstatus=%{public, signpost.telemetry:string2, name=status,public}s\nenableTelemetry=YES"
- "contextId=%{public, signpost.telemetry:string1, name=contextId,public}s\ntotalEvents=%{public, signpost.telemetry:number1, name=sleepTime,public}ld\nenableTelemetry=YES"
- "enableTelemetry=YES"
- "initWithPattern:options:error:"
- "matchesInString:options:range:"
- "numberOfRanges"
- "rangeAtIndex:"
- "substringWithRange:"

```
