## MetricsExtension

> `/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension`

```diff

-1.5.1.0.0
-  __TEXT.__text: 0x3f88
-  __TEXT.__auth_stubs: 0x5d0
+2.6.0.0.0
+  __TEXT.__text: 0x441c
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__cstring: 0x3a2
   __TEXT.__swift5_typeref: 0x14f
-  __TEXT.__cstring: 0xd2
   __TEXT.__const: 0x386
   __TEXT.__swift5_reflstr: 0x75
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1cc
+  __TEXT.__unwind_info: 0x1e0
   __TEXT.__eh_frame: 0x250
-  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__const: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x7c0

   - /System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework
   - /System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime
   - /System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework
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
-  UUID: F270B74C-90D4-3A5B-9602-E7EB07FC26D8
-  Functions: 124
-  Symbols:   71
-  CStrings:  8
+  UUID: 5E816426-ACDD-3B2B-BCD9-743EE44B779A
+  Functions: 128
+  Symbols:   81
+  CStrings:  23
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftHomeKit
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftVision
+ _objc_release_x21
+ _objc_retain
+ _objc_retain_x22
- _objc_release_x24
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
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```
