## SiriCoreMetricsWorker

> `/System/Library/ExtensionKit/Extensions/SiriCoreMetricsWorker.appex/SiriCoreMetricsWorker`

```diff

-3.0.7.0.0
-  __TEXT.__text: 0x3f10
-  __TEXT.__auth_stubs: 0x550
+3.0.9.0.0
+  __TEXT.__text: 0x41b4
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__const: 0x1e6
-  __TEXT.__cstring: 0x175
+  __TEXT.__cstring: 0x3f5
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_typeref: 0x103

   __TEXT.__objc_methname: 0x2d
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__unwind_info: 0x190
   __TEXT.__eh_frame: 0x1b0
-  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x308
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__objc_classrefs: 0x8
   __DATA.__data: 0x1d8
   __DATA.__bss: 0x390
   __DATA.__common: 0x18

   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
+  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreML.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib
+  - /usr/lib/swift/libswiftHomeKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVision.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 89
-  Symbols:   70
-  CStrings:  14
+  Functions: 90
+  Symbols:   77
+  CStrings:  28
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftHomeKit
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftVision
- _objc_release_x21
CStrings:
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```
