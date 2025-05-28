## SiriCoreMetrics

> `/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics`

```diff

-3.0.7.0.0
-  __TEXT.__text: 0x1f9ec
-  __TEXT.__auth_stubs: 0xf80
+3.0.9.0.0
+  __TEXT.__text: 0x20138
+  __TEXT.__auth_stubs: 0xfa0
   __TEXT.__const: 0x1220
   __TEXT.__swift5_typeref: 0x702
-  __TEXT.__cstring: 0xe51
+  __TEXT.__cstring: 0x11d1
   __TEXT.__constg_swiftt: 0x678
   __TEXT.__swift5_reflstr: 0x587
   __TEXT.__swift5_fieldmd: 0x58c

   __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_types: 0x74
   __TEXT.__swift5_assocty: 0x128
-  __TEXT.__unwind_info: 0x1184
-  __TEXT.__eh_frame: 0x990
+  __TEXT.__unwind_info: 0x11dc
+  __TEXT.__eh_frame: 0x9c0
   __TEXT.__objc_methname: 0x49e
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x720
   __DATA_CONST.__objc_selrefs: 0x1f8
+  __DATA_CONST.__objc_classrefs: 0xa8
   __AUTH_CONST.__const: 0xda0
   __AUTH_CONST.__auth_ptr: 0x50
   __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_got: 0x7d8
   __AUTH.__data: 0xa00
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_classrefs: 0xa8
-  __DATA.__data: 0x5e0
+  __DATA.__data: 0x5f0
   __DATA.__bss: 0x2000
-  __DATA.__common: 0x58
+  __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
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
   Functions: 690
-  Symbols:   372
-  CStrings:  160
+  Symbols:   387
+  CStrings:  179
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_SiriCoreMetrics
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_SiriCoreMetrics
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_SiriCoreMetrics
+ __swift_FORCE_LOAD_$_swiftHomeKit
+ __swift_FORCE_LOAD_$_swiftHomeKit_$_SiriCoreMetrics
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swiftMapKit_$_SiriCoreMetrics
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_SiriCoreMetrics
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_SiriCoreMetrics
+ __swift_FORCE_LOAD_$_swiftVision
+ __swift_FORCE_LOAD_$_swiftVision_$_SiriCoreMetrics
+ _objc_retain_x26
+ _swift_initStaticObject
- _objc_release
- _objc_retain_x19
- _objc_retain_x23
CStrings:
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```
