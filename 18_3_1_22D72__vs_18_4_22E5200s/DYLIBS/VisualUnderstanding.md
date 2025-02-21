## VisualUnderstanding

> `/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding`

```diff

-63.0.0.0.0
-  __TEXT.__text: 0xda840
-  __TEXT.__auth_stubs: 0x18a0
-  __TEXT.__objc_methlist: 0x304
-  __TEXT.__const: 0x254c
-  __TEXT.__cstring: 0x2d7c
-  __TEXT.__swift5_typeref: 0x1644
-  __TEXT.__oslogstring: 0x1df9
+66.1.0.0.0
+  __TEXT.__text: 0xd6660
+  __TEXT.__auth_stubs: 0x18c0
+  __TEXT.__objc_methlist: 0x47c
+  __TEXT.__const: 0x2b0c
+  __TEXT.__cstring: 0x293c
+  __TEXT.__swift5_typeref: 0x170c
+  __TEXT.__oslogstring: 0x2049
   __TEXT.__swift5_capture: 0x86c
-  __TEXT.__swift5_reflstr: 0x1281
-  __TEXT.__swift5_assocty: 0x238
-  __TEXT.__constg_swiftt: 0x1edc
-  __TEXT.__swift5_fieldmd: 0x13ac
+  __TEXT.__swift5_reflstr: 0x1461
+  __TEXT.__swift5_assocty: 0x268
+  __TEXT.__constg_swiftt: 0x2054
+  __TEXT.__swift5_fieldmd: 0x15ac
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x15c
-  __TEXT.__swift5_types: 0x14c
+  __TEXT.__swift5_proto: 0x180
+  __TEXT.__swift5_types: 0x160
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x2350
-  __TEXT.__eh_frame: 0x4f10
+  __TEXT.__unwind_info: 0x22a8
+  __TEXT.__eh_frame: 0x5690
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0x1232
   __TEXT.__objc_methtype: 0x134
-  __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x380
+  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__const: 0x390
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x698
+  __DATA_CONST.__objc_selrefs: 0x738
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xc50
-  __AUTH_CONST.__auth_ptr: 0x4d8
-  __AUTH_CONST.__const: 0x38f0
-  __AUTH_CONST.__objc_const: 0x2850
-  __AUTH.__objc_data: 0x250
-  __AUTH.__data: 0x1100
-  __DATA.__data: 0xad8
-  __DATA.__bss: 0x2700
-  __DATA.__common: 0x70
-  __DATA_DIRTY.__objc_data: 0x810
-  __DATA_DIRTY.__data: 0x2188
-  __DATA_DIRTY.__common: 0xd8
-  __DATA_DIRTY.__bss: 0x200
+  __AUTH_CONST.__auth_got: 0xc60
+  __AUTH_CONST.__auth_ptr: 0x4a0
+  __AUTH_CONST.__const: 0x3ca0
+  __AUTH_CONST.__objc_const: 0x2670
+  __AUTH.__objc_data: 0xc0
+  __AUTH.__data: 0x9c0
+  __DATA.__data: 0x838
+  __DATA.__bss: 0x2a00
+  __DATA_DIRTY.__objc_data: 0x9a0
+  __DATA_DIRTY.__data: 0x2d80
+  __DATA_DIRTY.__common: 0x140
+  __DATA_DIRTY.__bss: 0x380
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2853
-  Symbols:   402
-  CStrings:  771
+  Functions: 2825
+  Symbols:   422
+  CStrings:  757
 
Symbols:
+ _objc_release_x10
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_isUniquelyReferenced_nonNull
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_unknownObjectRelease_n
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ "Could not add enrollment observation, as gallery failed to add observation and generate an identifier for observation with revision: %s, and confidence: %s"
+ "No observations found in the store for this bucket: %ld"
+ "Pruning gallery using cluster based method"
+ "Pruning gallery using legacy path"
+ "Something went wrong in the sorting"
+ "Unable to add observation. Observation must be of type person (originated from VNFaceObservation) or animal (originated from VNAnimalObservation)."
+ "Unable to compute enrollment for direction bucket %ld, as there are no enrollment observations with angles for this bucket"
+ "Unable to find identifier in the enrollment angle for the only observation for this bucket. "
+ "clusteringThreshold"
+ "densities"
+ "minObservationsPerEntity"
+ "observationIdentifierEnrollmentSortingDataMap"
+ "partners"
+ "pruningType"
+ "similarities"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unable to add observation. Observation must be of type person (originated from VNFaceObservation) or animal  (originated from VNAnimalObservation)."
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.copyMemory with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"
- "numberKeyObservations"

```
