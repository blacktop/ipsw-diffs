## com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker`

```diff

-1.2.9.0.0
-  __TEXT.__text: 0x8714
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__const: 0x522
+2.0.12.0.0
+  __TEXT.__text: 0xa9f4
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__const: 0x548
+  __TEXT.__cstring: 0x804
   __TEXT.__swift5_typeref: 0x1d9
   __TEXT.__objc_methname: 0x3f
-  __TEXT.__cstring: 0x234
   __TEXT.__swift5_reflstr: 0xbb
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_fieldmd: 0xf8
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2a0
-  __TEXT.__eh_frame: 0x458
-  __DATA_CONST.__auth_got: 0x4e0
-  __DATA_CONST.__got: 0x110
+  __TEXT.__unwind_info: 0x2cc
+  __TEXT.__eh_frame: 0x468
+  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x10
   __DATA.__objc_selrefs: 0x20
-  __DATA.__objc_classrefs: 0x10
-  __DATA.__data: 0x338
+  __DATA.__data: 0x348
   __DATA.__bss: 0xa50
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 22726243-CF83-3569-8AF4-1C1BE23B101A
-  Functions: 179
-  Symbols:   76
-  CStrings:  26
+  UUID: A47A0F4F-76EF-320A-B937-3BB0A5A79FEC
+  Functions: 195
+  Symbols:   82
+  CStrings:  49
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x24
+ _objc_retain_x26
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_stdlib_random
- _objc_retain_x10
- _objc_retain_x23
CStrings:
+ "    correlationID=%{public, signpost.telemetry:string1, name=correlationID,public}s\n    numberOfStates=%{public, signpost.telemetry:number1, name=numberOfStates,public}ld\n    enableTelemetry=YES"
+ "CustomTelemetryEvent"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "SleepLoop"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Task interrupted while sleeping."
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "WorkLoop"
+ "[Error] Interval already ended"
+ "correlationID=%{public, signpost.telemetry:string1, name=correlationID,public}s\nsleepTime=%{public, signpost.telemetry:number1, name=sleepTime,public}f\nmaxDuration=%{public, signpost.telemetry:number2, name=maxDuration,public}f\nenableTelemetry=YES"
+ "correlationID=%{public, signpost.telemetry:string1, name=correlationID,public}s\nworkTime=%{public, signpost.telemetry:number1, name=workTime,public}f\nenableTelemetry=YES"
+ "enableTelemetry=YES"
+ "invalid Collection: less than 'count' elements in collection"
- "Task interruped while sleeping."

```
