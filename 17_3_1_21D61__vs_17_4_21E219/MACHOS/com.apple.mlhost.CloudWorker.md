## com.apple.mlhost.CloudWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker`

```diff

-1.2.9.0.0
-  __TEXT.__text: 0x19f54
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__const: 0x626
-  __TEXT.__swift5_typeref: 0x337
-  __TEXT.__swift5_fieldmd: 0x240
-  __TEXT.__constg_swiftt: 0x140
-  __TEXT.__cstring: 0x8fc
-  __TEXT.__objc_methname: 0x262
-  __TEXT.__swift5_reflstr: 0x254
+2.0.12.0.0
+  __TEXT.__text: 0x1b78c
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__const: 0x6f6
+  __TEXT.__swift5_typeref: 0x357
+  __TEXT.__swift5_fieldmd: 0x288
+  __TEXT.__constg_swiftt: 0x158
+  __TEXT.__cstring: 0xbec
+  __TEXT.__objc_methname: 0x275
+  __TEXT.__swift5_reflstr: 0x264
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x1c

   __TEXT.__objc_methtype: 0xad
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_capture: 0xbc0
-  __TEXT.__unwind_info: 0x508
-  __TEXT.__eh_frame: 0x9c8
-  __DATA_CONST.__auth_got: 0x528
-  __DATA_CONST.__got: 0x148
+  __TEXT.__swift5_capture: 0xb80
+  __TEXT.__unwind_info: 0x554
+  __TEXT.__eh_frame: 0xa00
+  __DATA_CONST.__auth_got: 0x570
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2310
+  __DATA_CONST.__const: 0x2170
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x58
   __DATA.__objc_const: 0x2f0
   __DATA.__objc_selrefs: 0x80
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x58
-  __DATA.__data: 0x3c0
+  __DATA.__data: 0x4f8
+  __DATA.__common: 0x48
   __DATA.__bss: 0xb80
-  __DATA.__common: 0x18
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ECD8096F-46E9-3D2E-BF96-A45A1877AA4C
-  Functions: 555
-  Symbols:   119
-  CStrings:  113
+  UUID: AECBE94C-6B47-39E4-BDDC-B63F048E12B6
+  Functions: 575
+  Symbols:   117
+  CStrings:  132
 
Symbols:
+ _objc_retain_x26
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
- _objc_retain_x10
- _objc_retain_x22
- _objc_retain_x27
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "Can't construct Array with count < 0"
+ "Division by zero"
+ "Division results in an overflow"
+ "Failed to parse TaskDefinition from config file, skipping task."
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Invalid task definition, skipping task: %@"
+ "Querying TaskParameters for fetched tasks: %s"
+ "Querying TaskPayload for fetched tasks: %s"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"
- "Failed to parse LHTaskDefinition from config file, moving on to the next task."
- "Querying TaskParameters for registered tasks: %s"
- "Querying TaskPayload for registered tasks: %s"
- "Task %s has failed to register."
- "Task cannot be registered before being created on CK with task name: %s."
- "com.apple.MLHost.CloudWorkerTelemetry"

```
