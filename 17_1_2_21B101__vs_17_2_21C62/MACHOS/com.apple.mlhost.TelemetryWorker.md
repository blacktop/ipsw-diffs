## com.apple.mlhost.TelemetryWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker`

```diff

-1.1.6.0.0
-  __TEXT.__text: 0x13464
-  __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__const: 0x2c2
-  __TEXT.__swift5_typeref: 0x294
-  __TEXT.__cstring: 0x305
-  __TEXT.__objc_methname: 0x1fc
-  __TEXT.__swift5_reflstr: 0x56
-  __TEXT.__swift5_assocty: 0x30
-  __TEXT.__constg_swiftt: 0x44
+1.2.9.0.0
+  __TEXT.__text: 0xc090
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__const: 0x34e
+  __TEXT.__swift5_typeref: 0x1a6
+  __TEXT.__cstring: 0x405
+  __TEXT.__objc_methname: 0x26b
+  __TEXT.__swift5_reflstr: 0x11f
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_fieldmd: 0x50
-  __TEXT.__swift5_capture: 0x490
-  __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x26c
-  __TEXT.__eh_frame: 0x278
-  __DATA_CONST.__auth_got: 0x5d8
-  __DATA_CONST.__got: 0x148
+  __TEXT.__swift5_fieldmd: 0xb4
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__unwind_info: 0x204
+  __TEXT.__eh_frame: 0x1e8
+  __DATA_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe80
+  __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x78
-  __DATA.__objc_classrefs: 0x28
-  __DATA.__data: 0x230
-  __DATA.__bss: 0x490
+  __DATA.__objc_selrefs: 0xa0
+  __DATA.__objc_classrefs: 0x38
+  __DATA.__data: 0x2d0
+  __DATA.__bss: 0x610
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 254
-  Symbols:   91
-  CStrings:  38
+  Functions: 157
+  Symbols:   93
+  CStrings:  53
 
Symbols:
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSTextCheckingResult
+ _objc_retain_x20
+ _objc_retain_x28
+ _swift_bridgeObjectRelease_n
+ _swift_errorRelease
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_willThrow
- _objc_release
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x22
- _swift_allocBox
- _swift_release_n
CStrings:
+ "(?=(N[^N]*N))"
+ "(D[^C]*C)"
+ "(D[^C]*[CF])"
+ "(F[^F]*F)"
+ "(RC)"
+ "(RD)"
+ "(RF)"
+ "24-hour Output: %s"
+ "7-day Output: %s"
+ "Events For Matching: %s | %ld, Regex: %s"
+ "Match: %s | Indices: %ld, %ld"
+ "No events in ledger."
+ "Processing 24-hour analytics aggregation"
+ "Processing 7-day analytics aggregation"
+ "Processing device telemetry for bucket: %s"
+ "TelemetryWorker: startTimestamp: %f -- endTimestamp: %f"
+ "initWithPattern:options:error:"
+ "matchesInString:options:range:"
+ "numberOfRanges"
+ "rangeAtIndex:"
+ "substringWithRange:"
+ "telemetry.lastTimestamp"
- "%s"
- "Found %ld events."
- "No bucket key."
- "Processing bucket timestamp: %f"
- "Querying ledgerClient from: %s to: %s"
- "Task: %s | Daily Execution Latency: %f seconds"
- "telemetry.lastProcessedTimestamp"

```
