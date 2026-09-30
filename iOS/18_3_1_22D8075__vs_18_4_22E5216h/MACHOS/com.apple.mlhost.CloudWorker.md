## com.apple.mlhost.CloudWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker`

```diff

-3.5.6.0.0
-  __TEXT.__text: 0x3097c
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__const: 0xb06
-  __TEXT.__cstring: 0x6ac
-  __TEXT.__swift5_typeref: 0x4fb
-  __TEXT.__swift5_fieldmd: 0x2cc
-  __TEXT.__constg_swiftt: 0x1d8
-  __TEXT.__oslogstring: 0x9fa
-  __TEXT.__objc_methname: 0x2a2
-  __TEXT.__swift5_reflstr: 0x2a4
-  __TEXT.__swift5_assocty: 0x78
+3.5.31.0.0
+  __TEXT.__text: 0x3e198
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__const: 0xb62
+  __TEXT.__cstring: 0x32c
+  __TEXT.__swift5_typeref: 0x53b
+  __TEXT.__swift5_fieldmd: 0x318
+  __TEXT.__constg_swiftt: 0x1f4
+  __TEXT.__oslogstring: 0xe8a
+  __TEXT.__objc_methname: 0x2b6
+  __TEXT.__swift5_reflstr: 0x2bd
+  __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0xa0
-  __TEXT.__swift5_types: 0x28
+  __TEXT.__swift5_proto: 0xb8
+  __TEXT.__swift5_types: 0x2c
   __TEXT.__objc_classname: 0x17
   __TEXT.__objc_methtype: 0xad
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_capture: 0xfe0
-  __TEXT.__unwind_info: 0x660
-  __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__auth_got: 0x730
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__auth_ptr: 0x2e0
-  __DATA_CONST.__const: 0x2be8
+  __TEXT.__swift5_capture: 0x1640
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__eh_frame: 0xc00
+  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__auth_ptr: 0x308
+  __DATA_CONST.__const: 0x3c40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x2f0
-  __DATA.__objc_selrefs: 0x90
-  __DATA.__data: 0x610
-  __DATA.__common: 0x48
-  __DATA.__bss: 0x1280
+  __DATA.__objc_const: 0x100
+  __DATA.__objc_selrefs: 0x138
+  __DATA.__data: 0x648
+  __DATA.__bss: 0x1580
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 668
-  Symbols:   136
-  CStrings:  161
+  Functions: 776
+  Symbols:   144
+  CStrings:  162
 
Symbols:
+ _objc_retain_x28
+ _sqrt
+ _swift_allocError
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_bridgeObjectRelease_n
- _swift_initStructMetadata
CStrings:
+ "Computed removalTaskNames: %s"
+ "Failed to parse TaskDefinition from config file, skipping task %s."
+ "Failed to parse TaskParameters from config file, skipping task %s."
+ "Failed to remove task %s: %@"
+ "Parsed TaskParameters successfully for task %s: %s"
+ "Parsing config file for taskName: %s"
+ "Processing TaskParametersRecords (count: %ld): %s"
+ "Processing TaskPayloadRecords (count: %ld): %s"
+ "Processing taskRecords (count: %ld): %s"
+ "Querying TaskParameters for tasks."
+ "Querying registered tasks for existing payloads..."
+ "Retrieved registered dynamic tasks: %s"
+ "Skipping payloads for registeredTask %s it was not added in this run."
+ "Skipping registration of task %s as it does not satisfy the targeting rules."
+ "Skipping task. It is being removed: %s"
+ "Skipping task. It was not registered locally: %s"
+ "Skipping task. No TaskParametersRecord found for: %s"
+ "Skipping task. No TaskPayloadRecord found for: %s"
+ "Skipping taskParametersRecord because extensionId is not recognized."
+ "Skipping taskPayloadRecord because associated with an unavailable extensionId."
+ "Task %s is being removed."
+ "Task %s is marked as canceled, skipping."
+ "Task %s is removed: %{bool}d."
+ "Task cancelled before processing TaskPayloads."
+ "Task cancelled before querying for TaskPayloads."
+ "Task cancelled while processing TaskPayloads."
+ "predicateWithValue:"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Parsing  config file for taskName: %s"
- "Processing TaskParametersRecords: %s"
- "Processing TaskPayloadRecords: %s"
- "Querying TaskParameters for added tasks: %s"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Task %s not registered on the system. Skipping task."
- "Task cancelled before while processing TaskPayloads."
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
