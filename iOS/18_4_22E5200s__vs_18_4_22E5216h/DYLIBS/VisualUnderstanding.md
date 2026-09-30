## VisualUnderstanding

> `/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding`

```diff

-66.1.0.0.0
-  __TEXT.__text: 0xd6660
-  __TEXT.__auth_stubs: 0x18c0
+67.0.0.0.0
+  __TEXT.__text: 0xd74fc
+  __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_methlist: 0x47c
-  __TEXT.__const: 0x2b0c
-  __TEXT.__cstring: 0x293c
-  __TEXT.__swift5_typeref: 0x170c
-  __TEXT.__oslogstring: 0x2049
-  __TEXT.__swift5_capture: 0x86c
-  __TEXT.__swift5_reflstr: 0x1461
+  __TEXT.__const: 0x2b9c
+  __TEXT.__cstring: 0x298c
+  __TEXT.__swift5_typeref: 0x16d4
+  __TEXT.__oslogstring: 0x2099
+  __TEXT.__swift5_capture: 0x890
+  __TEXT.__swift5_reflstr: 0x14c1
   __TEXT.__swift5_assocty: 0x268
-  __TEXT.__constg_swiftt: 0x2054
-  __TEXT.__swift5_fieldmd: 0x15ac
+  __TEXT.__constg_swiftt: 0x2090
+  __TEXT.__swift5_fieldmd: 0x15f8
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x180
-  __TEXT.__swift5_types: 0x160
+  __TEXT.__swift5_proto: 0x184
+  __TEXT.__swift5_types: 0x164
   __TEXT.__swift5_protos: 0xc
   __TEXT.__unwind_info: 0x22a8
-  __TEXT.__eh_frame: 0x5690
+  __TEXT.__eh_frame: 0x5568
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0x1232
   __TEXT.__objc_methtype: 0x134
-  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__got: 0x470
   __DATA_CONST.__const: 0x390
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x738
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xc60
-  __AUTH_CONST.__auth_ptr: 0x4a0
-  __AUTH_CONST.__const: 0x3ca0
-  __AUTH_CONST.__objc_const: 0x2670
-  __AUTH.__objc_data: 0xc0
-  __AUTH.__data: 0x9c0
-  __DATA.__data: 0x838
-  __DATA.__bss: 0x2a00
-  __DATA_DIRTY.__objc_data: 0x9a0
-  __DATA_DIRTY.__data: 0x2d80
-  __DATA_DIRTY.__common: 0x140
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
   __DATA_DIRTY.__bss: 0x380
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2825
+  Functions: 2829
   Symbols:   422
-  CStrings:  757
+  CStrings:  763
 
Symbols:
+ _BNNSComputeSimilarities
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
- _cblas_sgemm$NEWLAPACK
- _objc_retain_x12
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ "Failed to fetch parameters for type %hhu"
+ "Fetching vector store asset to identifier mapping"
+ "Missing parameters for type %hhu"
+ "No parameters for type %hhu"
+ "Re-computing centroids..."
+ "Updating partitions..."
+ "_TtC19VisualUnderstanding21VUVectorSearchScanner"
+ "cacheSize"
+ "embeddingPrecision"
+ "embeddingSize"
+ "mapping.partition == %lld AND noindex:(type) == %d AND noindex:(isPrimary) == YES"
+ "noindex:(embedding) != nil"
+ "numClusteringProbes"
+ "quantizerAveragePartitionSize"
+ "scannerCacheSize"
+ "type == %d AND isPrimary == YES"
+ "vectorSearchStore.lock"
- "Embeddings cannot be converted to data!"
- "Looking for neighbors of %ld embeddings"
- "Searching embeddings %ld..%ld"
- "Vector store is missing embedding!"
- "_TtC19VisualUnderstanding19VUVectorSearchStore"
- "mapping.partition == %lld AND noindex:(type) == %d AND noindex:(embedding) != nil AND noindex:(isPrimary) == YES"
- "numProbes"
- "secondaryIdentifiers"
- "type == %d AND embedding != nil AND isPrimary == YES"
- "vectorSearch"
- "vectorSearchBatch"

```
