## SNCFeaturesPlugin

> `/System/Library/ExtensionKit/Extensions/SNCFeaturesPlugin.appex/SNCFeaturesPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`

```diff

-44.0.0.0.0
-  __TEXT.__text: 0x53a0
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0x5c8
+46.0.0.0.0
+  __TEXT.__text: 0x13f4
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_stubs: 0x20
+  __TEXT.__const: 0x1d2
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xb8
-  __TEXT.__swift5_typeref: 0x175
-  __TEXT.__swift5_fieldmd: 0xbc
-  __TEXT.__swift5_reflstr: 0xf9
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__cstring: 0x152
+  __TEXT.__constg_swiftt: 0x64
+  __TEXT.__swift5_typeref: 0x6e
+  __TEXT.__swift5_fieldmd: 0x20
+  __TEXT.__swift5_reflstr: 0xe
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__cstring: 0x4f
   __TEXT.__objc_methtype: 0x14
-  __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift_as_entry: 0x24
-  __TEXT.__swift_as_ret: 0x18
-  __TEXT.__swift_as_cont: 0x18
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_cont: 0x14
   __TEXT.__objc_classname: 0x31
-  __TEXT.__oslogstring: 0x195
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__objc_methname: 0x20
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__eh_frame: 0x2e8
-  __DATA_CONST.__const: 0x395
+  __TEXT.__objc_methname: 0x15
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__eh_frame: 0x190
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__auth_ptr: 0x1f8
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0xb8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x1c0
+  __DATA.__objc_selrefs: 0x8
+  __DATA.__data: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 129
-  Symbols:   107
-  CStrings:  21
+  Functions: 42
+  Symbols:   71
+  CStrings:  5
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
- _OBJC_CLASS_$_NSNumber
- ___chkstk_darwin
- __os_log_impl
- __swiftEmptyArrayStorage
- __swiftEmptyDictionarySingleton
- __swiftImmortalRefCount
- _bzero
- _malloc_size
- _memcpy
- _memmove
- _objc_release_x20
- _os_log_type_enabled
- _swift_allocError
- _swift_arrayDestroy
- _swift_beginAccess
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain
- _swift_bridgeObjectRetain_n
- _swift_cvw_assignWithCopy
- _swift_cvw_assignWithTake
- _swift_cvw_destroy
- _swift_cvw_initWithCopy
- _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_deallocObject
- _swift_dynamicCast
- _swift_getDynamicType
- _swift_getObjectType
- _swift_initStackObject
- _swift_isUniquelyReferenced_nonNull_native
- _swift_release_x19
- _swift_release_x21
- _swift_release_x22
- _swift_release_x23
- _swift_retain_x23
- _swift_setDeallocating
- _swift_slowAlloc
- _swift_slowDealloc
- _swift_unknownObjectRetain
- _swift_willThrow
CStrings:
- ",\n    trainingFunction: "
- "Failed to convert all model_diff entries to Float32 (%ld/%ld)"
- "Hyper Parameters: %s"
- "Morpheus program attachment not found: %s"
- "Morpheus training returned unexpected result type: %s"
- "MorpheusDecoding"
- "MorpheusExecution"
- "PreparePFLResult"
- "SNCFeaturesHyperParams(\n    morpheusTrainingProgramFileName: "
- "Training metrics: %s"
- "Weight vector count: %ld, first 5: %s"
- "floatValue"
- "metrics (index 0) not a dict in training result list"
- "model_diff (index 1) not an array in training result list"
- "morpheus_training_program_file_name"
- "training_function"
```
