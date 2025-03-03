## ActivitySharingServices

> `/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices`

```diff

-823.10.0.0.0
-  __TEXT.__text: 0x12e9ec
-  __TEXT.__auth_stubs: 0x1e90
-  __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0x4d38
-  __TEXT.__cstring: 0x473e
-  __TEXT.__swift5_typeref: 0x30a0
-  __TEXT.__swift5_fieldmd: 0x2b24
-  __TEXT.__constg_swiftt: 0x279c
-  __TEXT.__oslogstring: 0x59c3
+824.7.0.0.0
+  __TEXT.__text: 0x13d484
+  __TEXT.__auth_stubs: 0x1e50
+  __TEXT.__objc_methlist: 0x954
+  __TEXT.__const: 0x6278
+  __TEXT.__cstring: 0x43fe
+  __TEXT.__swift5_typeref: 0x33e2
+  __TEXT.__swift5_fieldmd: 0x2b90
+  __TEXT.__constg_swiftt: 0x281c
+  __TEXT.__oslogstring: 0x5c43
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x3f14
+  __TEXT.__swift5_reflstr: 0x4024
   __TEXT.__swift5_assocty: 0x210
   __TEXT.__swift5_protos: 0x130
   __TEXT.__swift5_proto: 0x318
   __TEXT.__swift5_types: 0x234
-  __TEXT.__swift5_capture: 0x1a04
+  __TEXT.__swift_as_entry: 0x694
+  __TEXT.__swift_as_ret: 0xaec
+  __TEXT.__swift5_capture: 0x1b00
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6400
-  __TEXT.__eh_frame: 0x13560
-  __TEXT.__objc_classname: 0x1b9
-  __TEXT.__objc_methname: 0x3b32
-  __TEXT.__objc_methtype: 0x12e6
+  __TEXT.__unwind_info: 0x6a40
+  __TEXT.__eh_frame: 0x15158
+  __TEXT.__objc_classname: 0x1d9
+  __TEXT.__objc_methname: 0x3b92
+  __TEXT.__objc_methtype: 0x1308
   __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x9b8
-  __DATA_CONST.__objc_classlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc20
-  __DATA_CONST.__objc_protorefs: 0x80
-  __AUTH_CONST.__auth_got: 0xf48
-  __AUTH_CONST.__auth_ptr: 0xe00
-  __AUTH_CONST.__const: 0x7928
-  __AUTH_CONST.__objc_const: 0x5b40
-  __AUTH.__objc_data: 0x318
-  __AUTH.__data: 0x6f8
-  __DATA.__data: 0x2948
+  __DATA_CONST.__objc_selrefs: 0xe40
+  __DATA_CONST.__objc_protorefs: 0x88
+  __AUTH_CONST.__auth_got: 0xf28
+  __AUTH_CONST.__auth_ptr: 0x11a8
+  __AUTH_CONST.__const: 0x89b0
+  __AUTH_CONST.__objc_const: 0x5510
+  __AUTH.__objc_data: 0x3e0
+  __AUTH.__data: 0x768
+  __DATA.__data: 0x2c28
   __DATA.__bss: 0x2d00
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x670
-  __DATA_DIRTY.__data: 0x12c0
+  __DATA_DIRTY.__data: 0x12d8
   __DATA_DIRTY.__common: 0x48
   __DATA_DIRTY.__bss: 0xa80
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4776
-  Symbols:   461
+  Functions: 4845
+  Symbols:   674
   CStrings:  1359
 
Symbols:
+ _objc_retain_x13
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_getExistentialTypeMetadata
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x9
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
CStrings:
+ "ActivitySharingServices.DatabaseCoordinator"
+ "Adding addresses to legacy relationship"
+ "Adding received addresses to legacy relationship"
+ "Failed to add remote event type for relationship: %@"
+ "Fetching change while accepting invitation from friend with identifier: %s"
+ "HDDatabaseProtectedDataObserver"
+ "Loaded anchor map for: %s"
+ "Not pushing activity data updates to CloudKit, protected data unavailable"
+ "Preparing anchor store for protected data change: %s"
+ "Protected data available but already loaded anchor for: %s"
+ "Protected data available for: %s"
+ "Protected data is unavailable on prepare: %s"
+ "Waiting for protected data for anchor store: %s"
+ "_TtC23ActivitySharingServices19DatabaseCoordinator"
+ "addProtectedDataObserver:"
+ "database:protectedDataDidBecomeAvailable:"
+ "databaseCoordinator"
+ "insertRemoteEventType:onContactWithUUID:cloudType:completion:"
+ "protectedDataObservers"
+ "v28@0:8@\"<HDHealthDatabase>\"16B24"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
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
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"
- "setSecureCloudRemoteRelationship:"

```
