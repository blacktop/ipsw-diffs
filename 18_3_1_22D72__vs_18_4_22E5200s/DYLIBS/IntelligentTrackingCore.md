## IntelligentTrackingCore

> `/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore`

```diff

-261.0.0.0.0
-  __TEXT.__text: 0x120998
-  __TEXT.__auth_stubs: 0x21e0
-  __TEXT.__objc_methlist: 0x90
-  __TEXT.__const: 0xb424
-  __TEXT.__cstring: 0x5dc7
-  __TEXT.__constg_swiftt: 0x8c34
-  __TEXT.__swift5_typeref: 0x2f1e
-  __TEXT.__swift5_reflstr: 0x36c1
-  __TEXT.__swift5_fieldmd: 0x4fa0
+273.0.0.0.0
+  __TEXT.__text: 0x11dc40
+  __TEXT.__auth_stubs: 0x2150
+  __TEXT.__objc_methlist: 0x194
+  __TEXT.__const: 0xc334
+  __TEXT.__cstring: 0x5c87
+  __TEXT.__constg_swiftt: 0x9084
+  __TEXT.__swift5_typeref: 0x313c
+  __TEXT.__swift5_reflstr: 0x3921
+  __TEXT.__swift5_fieldmd: 0x52c0
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_assocty: 0x4c8
+  __TEXT.__swift5_assocty: 0x510
   __TEXT.__swift5_capture: 0xec
-  __TEXT.__swift5_proto: 0x9b8
-  __TEXT.__swift5_types: 0x4b0
+  __TEXT.__swift5_proto: 0xa64
+  __TEXT.__swift5_types: 0x4e8
+  __TEXT.__swift_as_entry: 0x100
+  __TEXT.__swift_as_ret: 0xb8
   __TEXT.__oslogstring: 0x268
   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x43d8
-  __TEXT.__eh_frame: 0x51c0
+  __TEXT.__unwind_info: 0x4288
+  __TEXT.__eh_frame: 0x54a8
   __TEXT.__objc_classname: 0x35
   __TEXT.__objc_methname: 0x745
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0x1958
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__const: 0x19e0
+  __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x278
+  __DATA_CONST.__objc_selrefs: 0x318
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x10f0
-  __AUTH_CONST.__auth_ptr: 0xa38
-  __AUTH_CONST.__const: 0x6ff0
-  __AUTH_CONST.__objc_const: 0x95c0
-  __AUTH.__objc_data: 0x1f40
-  __AUTH.__data: 0xd630
-  __DATA.__data: 0x2f80
-  __DATA.__common: 0xd78
-  __DATA.__bss: 0x13080
+  __AUTH_CONST.__auth_got: 0x10a8
+  __AUTH_CONST.__auth_ptr: 0xa28
+  __AUTH_CONST.__const: 0x7968
+  __AUTH_CONST.__objc_const: 0x9770
+  __AUTH.__objc_data: 0x1fe0
+  __AUTH.__data: 0xdf40
+  __DATA.__data: 0x31a8
+  __DATA.__common: 0xda0
+  __DATA.__bss: 0x14600
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8243
-  Symbols:   376
-  CStrings:  948
+  Functions: 8289
+  Symbols:   380
+  CStrings:  947
 
Symbols:
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initStructMetadataWithLayoutString
- _objc_retain_x28
- _objc_retain_x9
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
+ "Confidence should be between 0.0 and 1.0"
+ "IntelligentTrackingCore.DKIdentityKalmanFilter"
+ "IntelligentTrackingCore/IdentityFilter.swift"
+ "_TtC23IntelligentTrackingCore16DKIdentityFilter"
+ "_TtC23IntelligentTrackingCore22DKIdentityKalmanFilter"
+ "_TtCC23IntelligentTrackingCore16DKIdentityFilter13Configuration"
+ "_TtCC23IntelligentTrackingCore22DKIdentityKalmanFilter11Measurement"
+ "dynamicBodyProbabilities"
+ "dynamicFaceProbabilities"
+ "enrolledFaceProbabilities"
+ "filters"
+ "identityFilterConfig"
+ "identityFilterNew"
+ "identityProbabilities"
+ "identityState"
+ "isIdentityFilterEnabled"
+ "kfConfig"
+ "maxValue"
+ "minValue"
+ "predictionTimeout"
+ "trackingLock"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.copyMemory with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
