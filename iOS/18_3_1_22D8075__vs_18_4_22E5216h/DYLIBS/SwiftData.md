## SwiftData

> `/System/Library/Frameworks/SwiftData.framework/SwiftData`

```diff

-92.2.0.0.0
-  __TEXT.__text: 0x114fec
-  __TEXT.__auth_stubs: 0x27e0
+97.0.0.0.0
+  __TEXT.__text: 0x106bf4
+  __TEXT.__auth_stubs: 0x2770
   __TEXT.__objc_methlist: 0x114
-  __TEXT.__cstring: 0x6f1a
-  __TEXT.__const: 0x6c28
-  __TEXT.__constg_swiftt: 0x4d24
-  __TEXT.__swift5_typeref: 0x2f1a
+  __TEXT.__cstring: 0x6e0a
+  __TEXT.__const: 0x7278
+  __TEXT.__constg_swiftt: 0x4d34
+  __TEXT.__swift5_typeref: 0x2ecc
   __TEXT.__swift5_reflstr: 0x1e35
   __TEXT.__swift5_fieldmd: 0x2370
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_capture: 0x7f8
+  __TEXT.__swift5_capture: 0x8b8
   __TEXT.__swift5_assocty: 0x5c8
   __TEXT.__swift5_proto: 0x4d0
   __TEXT.__swift5_types: 0x234
-  __TEXT.__oslogstring: 0xab3
+  __TEXT.__oslogstring: 0xc53
   __TEXT.__swift5_protos: 0x94
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__unwind_info: 0x3b40
-  __TEXT.__eh_frame: 0x6df0
+  __TEXT.__unwind_info: 0x3810
+  __TEXT.__eh_frame: 0x6e98
   __TEXT.__objc_methname: 0x1338
-  __DATA_CONST.__got: 0xb90
+  __DATA_CONST.__got: 0xba8
   __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x780
-  __AUTH_CONST.__auth_got: 0x13f0
-  __AUTH_CONST.__auth_ptr: 0xe50
-  __AUTH_CONST.__const: 0x4710
+  __AUTH_CONST.__auth_got: 0x13b8
+  __AUTH_CONST.__auth_ptr: 0xe40
+  __AUTH_CONST.__const: 0x48f0
   __AUTH_CONST.__objc_const: 0x3868
-  __AUTH.__objc_data: 0x208
-  __AUTH.__data: 0xf18
-  __DATA.__data: 0x1220
-  __DATA.__bss: 0x6660
-  __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x288
-  __DATA_DIRTY.__data: 0x4108
-  __DATA_DIRTY.__bss: 0x2e10
-  __DATA_DIRTY.__common: 0x170
+  __AUTH.__objc_data: 0x1b8
+  __AUTH.__data: 0xb90
+  __DATA.__data: 0x1448
+  __DATA.__bss: 0x65e0
+  __DATA.__common: 0x110
+  __DATA_DIRTY.__objc_data: 0x2d8
+  __DATA_DIRTY.__data: 0x44e0
+  __DATA_DIRTY.__bss: 0x2e90
+  __DATA_DIRTY.__common: 0x178
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5170
-  Symbols:   382
-  CStrings:  956
+  Functions: 4894
+  Symbols:   394
+  CStrings:  950
 
Symbols:
+ _objc_retain_x1
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
- _objc_release_x11
- _objc_retain_x10
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
- _swift_unknownObjectWeakCopyAssign
- _swift_unknownObjectWeakCopyInit
- _swift_unknownObjectWeakTakeAssign
- _swift_unknownObjectWeakTakeInit
- _swift_weakCopyAssign
- _swift_weakCopyInit
- _swift_weakTakeAssign
- _swift_weakTakeInit
CStrings:
+ " but insert was called on "
+ " but it's trying to insert in to "
+ " but we're trying to generate a '"
+ " is already bound to "
+ " points to a property of a id which cannot be used for sorting or queries. Please file a bug report with your desired use case and a test / example of your FetchDescriptor."
+ " points to a property of a persistentModelID which cannot be used for sorting or queries. Please file a bug report with your desired use case and a test / example of your FetchDescriptor."
+ " stores at this time. Please file a bug report for other stores."
+ "%s"
+ "'. This is very likely a bug in the implementation of the DataStore "
+ ". It is possible that this path traverses a type that does not work with append(), please file a bug report with a test."
+ "A ModelSnapshot must be initialized with a known-keys dictionary"
+ "A model should only be updated after being inserted into a Model Context"
+ "A snapshot should exist before creating a new snapshot for undo"
+ "Attempting to use Undo without a model context"
+ "Attempting to use a Model with an unexpected backing data type "
+ "Attempting to use modelContext that does not know this entity - "
+ "Failed to cast existing model for "
+ "Illegal attempt to insert a model from a different context. "
+ "Illegal attempt to insert a model in to a different model context. Model "
+ "Illegal attempt to update a model with a snapshot of a different type. Was given a snapshot for "
+ "ModelConfiguration"
+ "SchemaGeneration"
+ "SchemaValidation"
+ "SwiftData isn't prepared for custom metadata implementations yet. Please file a bug report."
+ "Unabel to cast keyPath "
+ "Unable to fulfill future for %s"
+ "Unable to fulfill future for %s - given error: %@"
+ "Unable to fulfill futures for %s - given error: %@"
+ "cannot fulfill model without a store identifier:%s"
+ "com.apple.swiftdata"
+ "data store (%s) did not return a snapshot for: %s"
+ "data store not found for:%s in: %s"
+ "failed to fulfill a snapshot for: %s with error: %@"
- "\n For fetch descriptor: "
- "  modeled as a relationship: "
- " modeled as a relationship: "
- " points to a property of a persistentModelID which cannot be used for sorting or queries. Please file a radar with your desired use case and a test / example of your FetchDescriptor."
- " stores at this time. Please file a radar for other stores."
- ". It is possible that this path traverses a type that does not work with append(), please file a radar with a test."
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Expected a relationship keypath "
- "Failed to materialize a model for "
- "Insufficient space allocated to copy string contents"
- "No registered model after update? "
- "Schema Generation"
- "Schema Validation"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "SwiftData isn't prepared for custom metadata implementations yet. Please file a radar."
- "Unable to determine the primitive for "
- "Unable to find the relationship for "
- "Unable to get primitive toMany for "
- "Unable to get primitive toOne for "
- "Unable to set primitive toMany for "
- "Unexpectedly found an array with a codable element type"
- "Unexpectedly found an array with a codable element type "
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "com.apple.SwiftData"
- "invalid Collection: less than 'count' elements in collection"

```
