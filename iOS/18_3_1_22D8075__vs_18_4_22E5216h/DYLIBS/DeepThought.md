## DeepThought

> `/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought`

```diff

-4.3.3.0.0
-  __TEXT.__text: 0x2a9a8
-  __TEXT.__auth_stubs: 0x1270
-  __TEXT.__const: 0x245a
-  __TEXT.__swift5_typeref: 0x984
-  __TEXT.__swift5_fieldmd: 0x948
+4.6.0.0.0
+  __TEXT.__text: 0x28480
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__const: 0x265a
+  __TEXT.__swift5_typeref: 0x958
+  __TEXT.__swift5_fieldmd: 0x93c
   __TEXT.__constg_swiftt: 0xd50
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x6a9

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x1ec
   __TEXT.__swift5_types: 0x100
-  __TEXT.__cstring: 0x1504
+  __TEXT.__cstring: 0x1294
   __TEXT.__oslogstring: 0x75e
+  __TEXT.__swift_as_entry: 0x74
+  __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xbf8
-  __TEXT.__eh_frame: 0xfb8
-  __TEXT.__objc_methname: 0x54b
+  __TEXT.__unwind_info: 0xad8
+  __TEXT.__eh_frame: 0xec0
+  __TEXT.__objc_methname: 0x4ed
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e0
-  __AUTH_CONST.__auth_got: 0x940
-  __AUTH_CONST.__auth_ptr: 0x388
-  __AUTH_CONST.__const: 0x13c8
+  __DATA_CONST.__objc_selrefs: 0x1b8
+  __AUTH_CONST.__auth_got: 0x900
+  __AUTH_CONST.__auth_ptr: 0x370
+  __AUTH_CONST.__const: 0x1370
   __AUTH_CONST.__cfstring: 0x1a20
   __AUTH_CONST.__objc_const: 0xbf8
   __AUTH.__objc_data: 0x320
-  __AUTH.__data: 0xce0
-  __DATA.__data: 0xc40
-  __DATA.__bss: 0x3c00
+  __AUTH.__data: 0xbe8
+  __DATA.__data: 0xc28
+  __DATA.__bss: 0x3b80
   __DATA.__common: 0x50
+  __DATA_DIRTY.__data: 0x110
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
-  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1020
-  Symbols:   208
-  CStrings:  405
+  Functions: 976
+  Symbols:   214
+  CStrings:  387
 
Symbols:
+ _OBJC_CLASS_$_NSString
+ _objc_retain_x27
+ _objc_retain_x28
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
- _OBJC_CLASS_$_TRIBackgroundMLTaskIdentifiers
- ___stack_chk_fail
- ___stack_chk_guard
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x9
- _objc_retain_x24
- _objc_retain_x26
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
+ "Trial experimentId - DEPRECATED, NIL"
+ "Trial treatmentId - DEPRECATED, NIL"
+ "trialDeploymentId DEPRECATED, NIL"
+ "trialExperimentId - DEPRECATED, NIL"
+ "trialTreatmentId - DEPRECATED, NIL"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "bmltTaskId"
- "deploymentId"
- "factorPackId"
- "initWithBMLTTaskId:deploymentId:treatmentId:"
- "invalid Collection: less than 'count' elements in collection"
- "treatmentId"

```
