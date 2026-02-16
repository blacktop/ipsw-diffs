## VectorSearch

> `/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch`

```diff

-45.1.0.0.0
-  __TEXT.__text: 0x76b78
-  __TEXT.__auth_stubs: 0x1bd0
-  __TEXT.__objc_methlist: 0x9e4
-  __TEXT.__const: 0x2d00
-  __TEXT.__cstring: 0x45ed
-  __TEXT.__constg_swiftt: 0x100c
-  __TEXT.__swift5_typeref: 0x10c8
+48.2.0.0.0
+  __TEXT.__text: 0x7ccb4
+  __TEXT.__auth_stubs: 0x1bf0
+  __TEXT.__objc_methlist: 0xa0c
+  __TEXT.__const: 0x3240
+  __TEXT.__constg_swiftt: 0x10fc
+  __TEXT.__swift5_typeref: 0x11d6
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0xbf5
-  __TEXT.__swift5_fieldmd: 0xd1c
-  __TEXT.__swift5_types: 0xec
-  __TEXT.__swift5_capture: 0x85c
-  __TEXT.__oslogstring: 0x1034
-  __TEXT.__swift5_proto: 0x184
+  __TEXT.__swift5_reflstr: 0xc25
+  __TEXT.__swift5_fieldmd: 0xde8
+  __TEXT.__swift5_types: 0x104
+  __TEXT.__cstring: 0x3ffe
+  __TEXT.__swift5_capture: 0x874
+  __TEXT.__oslogstring: 0x10f4
+  __TEXT.__swift5_proto: 0x1e4
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_mpenum: 0x3c
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x16a8
-  __TEXT.__eh_frame: 0x41a0
-  __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methname: 0x1c5d
-  __TEXT.__objc_methtype: 0x53d
-  __TEXT.__objc_stubs: 0xa60
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x88
+  __TEXT.__unwind_info: 0x1780
+  __TEXT.__eh_frame: 0x42a0
+  __TEXT.__objc_classname: 0x44b
+  __TEXT.__objc_methname: 0x20f6
+  __TEXT.__objc_methtype: 0x6c7
+  __TEXT.__objc_stubs: 0xf20
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d8
+  __DATA_CONST.__objc_selrefs: 0x500
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0xdf0
-  __AUTH_CONST.__const: 0x2548
+  __AUTH_CONST.__auth_got: 0xe00
+  __AUTH_CONST.__const: 0x28d0
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x1a88
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x278
+  __AUTH.__objc_data: 0x228
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x68
-  __DATA.__data: 0x530
-  __DATA.__bss: 0x1500
-  __DATA_DIRTY.__objc_data: 0x9c0
-  __DATA_DIRTY.__data: 0x14c0
-  __DATA_DIRTY.__bss: 0x1500
+  __DATA.__data: 0x470
+  __DATA.__bss: 0x1d90
+  __DATA_DIRTY.__objc_data: 0xa18
+  __DATA_DIRTY.__data: 0x1698
+  __DATA_DIRTY.__bss: 0x1880
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 24349264-495A-3BE7-B37E-43CA78DBF78F
-  Functions: 1766
-  Symbols:   254
-  CStrings:  700
+  UUID: 5D4A4E41-B7D5-3844-AA05-636DBE3DE1D7
+  Functions: 1859
+  Symbols:   249
+  CStrings:  701
 
Symbols:
+ _swift_willThrowTypedImpl
- __swift_FORCE_LOAD_$_swiftQuartzCore
- _ceilf
- _memset_pattern16
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
CStrings:
+ "    CREATE INDEX "
+ "    SELECT attribute_indices\n    FROM "
+ "    SELECT name FROM sqlite_master\n    WHERE type='index'\n    AND name='"
+ " (\n        key, \n        distance_metric, \n        filterable_attributes, \n        dimension,  \n        average_partition_size,\n        batch_size,\n        batch_factor,\n        tradeoff_parameter_between_clustering_and_balance,\n        enable_fts,\n        data_type,\n        max_index_construction_batches,\n        pretokenization_enabled,\n        prefix_indices,\n        attribute_indices,\n        client_version\n    )\n    VALUES (\n        0,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?\n    )"
+ "' as it is not in the list of filterable attributes."
+ "Cannot create index on attribute '"
+ "Unable to read attribute indices, falling back to empty config. Error: %@"
+ "VectorDatabaseConfig:migrate no-op for .addAttributeIndices migration"
+ "addAttributeIndices"
+ "attribute_indices"
+ "attribute_indices were not correct for read config."
+ "boolValue"
+ "getDeltaCount called"
+ "initWithBool:"
+ "isOneTimeReadWritePrewarmNeededAndReturnError:"
+ "isOneTimeReadWritePrewarmNeededWithError:"
+ "searchByBatch:stringIdentifiers:attributeFilters:selectAttributes:limit:fullScan:includePayload:numberOfProbes:batchSize:numConcurrentReaders:error:"
- " VALUES (\n        0,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?,\n        ?\n    )"

```
