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
-  __TEXT.__swift5_capture: 0x86c
-  __TEXT.__swift5_reflstr: 0x1281
-  __TEXT.__swift5_assocty: 0x238
-  __TEXT.__constg_swiftt: 0x1edc
-  __TEXT.__swift5_fieldmd: 0x13ac
+67.0.0.0.0
+  __TEXT.__text: 0xd74fc
+  __TEXT.__auth_stubs: 0x1860
+  __TEXT.__objc_methlist: 0x47c
+  __TEXT.__const: 0x2b9c
+  __TEXT.__cstring: 0x298c
+  __TEXT.__swift5_typeref: 0x16d4
+  __TEXT.__oslogstring: 0x2099
+  __TEXT.__swift5_capture: 0x890
+  __TEXT.__swift5_reflstr: 0x14c1
+  __TEXT.__swift5_assocty: 0x268
+  __TEXT.__constg_swiftt: 0x2090
+  __TEXT.__swift5_fieldmd: 0x15f8
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x15c
-  __TEXT.__swift5_types: 0x14c
+  __TEXT.__swift5_proto: 0x184
+  __TEXT.__swift5_types: 0x164
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x2350
-  __TEXT.__eh_frame: 0x4f10
+  __TEXT.__unwind_info: 0x22a8
+  __TEXT.__eh_frame: 0x5568
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0x1232
   __TEXT.__objc_methtype: 0x134
-  __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x380
+  __DATA_CONST.__got: 0x470
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
+  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH_CONST.__auth_ptr: 0x4c8
+  __AUTH_CONST.__const: 0x3d90
+  __AUTH_CONST.__objc_const: 0x26d0
+  __AUTH.__objc_data: 0x110
+  __AUTH.__data: 0xb10
+  __DATA.__data: 0x878
+  __DATA.__bss: 0x2b00
+  __DATA.__common: 0x28
+  __DATA_DIRTY.__objc_data: 0x950
+  __DATA_DIRTY.__data: 0x2bf0
+  __DATA_DIRTY.__common: 0x108
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
+  Functions: 2829
+  Symbols:   422
+  CStrings:  763
 
Symbols:
+ _BNNSComputeSimilarities
+ _objc_release_x10
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_isUniquelyReferenced_nonNull
+ _swift_unknownObjectRelease_n
- _cblas_sgemm$NEWLAPACK
- _objc_retain_x12
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ "Could not add enrollment observation, as gallery failed to add observation and generate an identifier for observation with revision: %s, and confidence: %s"
+ "Failed to fetch parameters for type %hhu"
+ "Fetching vector store asset to identifier mapping"
+ "Missing parameters for type %hhu"
+ "No observations found in the store for this bucket: %ld"
+ "No parameters for type %hhu"
+ "Pruning gallery using cluster based method"
+ "Pruning gallery using legacy path"
+ "Re-computing centroids..."
+ "Something went wrong in the sorting"
+ "Unable to add observation. Observation must be of type person (originated from VNFaceObservation) or animal (originated from VNAnimalObservation)."
+ "Unable to compute enrollment for direction bucket %ld, as there are no enrollment observations with angles for this bucket"
+ "Unable to find identifier in the enrollment angle for the only observation for this bucket. "
+ "Updating partitions..."
+ "_TtC19VisualUnderstanding21VUVectorSearchScanner"
+ "cacheSize"
+ "clusteringThreshold"
+ "densities"
+ "embeddingPrecision"
+ "embeddingSize"
+ "mapping.partition == %lld AND noindex:(type) == %d AND noindex:(isPrimary) == YES"
+ "minObservationsPerEntity"
+ "noindex:(embedding) != nil"
+ "numClusteringProbes"
+ "observationIdentifierEnrollmentSortingDataMap"
+ "partners"
+ "pruningType"
+ "quantizerAveragePartitionSize"
+ "scannerCacheSize"
+ "similarities"
+ "type == %d AND isPrimary == YES"
+ "vectorSearchStore.lock"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Embeddings cannot be converted to data!"
- "Insufficient space allocated to copy string contents"
- "Looking for neighbors of %ld embeddings"
- "Must take zero or more splits"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Range requires lowerBound <= upperBound"
- "Searching embeddings %ld..%ld"
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
- "Vector store is missing embedding!"
- "_TtC19VisualUnderstanding19VUVectorSearchStore"
- "invalid Collection: less than 'count' elements in collection"
- "mapping.partition == %lld AND noindex:(type) == %d AND noindex:(embedding) != nil AND noindex:(isPrimary) == YES"
- "numProbes"
- "numberKeyObservations"
- "secondaryIdentifiers"
- "type == %d AND embedding != nil AND isPrimary == YES"
- "vectorSearch"
- "vectorSearchBatch"

```
