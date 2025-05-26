## com.apple.mlhost.CloudWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker`

```diff

-3.0.10.0.0
-  __TEXT.__text: 0x1e994
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__const: 0x836
-  __TEXT.__cstring: 0xdcc
-  __TEXT.__swift5_typeref: 0x3b1
-  __TEXT.__swift5_fieldmd: 0x2b0
-  __TEXT.__constg_swiftt: 0x174
-  __TEXT.__objc_methname: 0x275
-  __TEXT.__swift5_reflstr: 0x284
+3.1.14.0.0
+  __TEXT.__text: 0x2de64
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__const: 0xae6
+  __TEXT.__cstring: 0x10ac
+  __TEXT.__swift5_typeref: 0x4cd
+  __TEXT.__swift5_fieldmd: 0x2cc
+  __TEXT.__constg_swiftt: 0x1d8
+  __TEXT.__objc_methname: 0x2a2
+  __TEXT.__swift5_reflstr: 0x2a4
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x7c
-  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_proto: 0xa0
+  __TEXT.__swift5_types: 0x28
   __TEXT.__objc_classname: 0x17
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_capture: 0xc30
-  __TEXT.__unwind_info: 0x10a4
+  __TEXT.__swift5_capture: 0xfe0
+  __TEXT.__unwind_info: 0x1130
   __TEXT.__eh_frame: 0xa98
-  __DATA_CONST.__auth_got: 0x610
-  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__auth_got: 0x730
+  __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2468
+  __DATA_CONST.__const: 0x2ed0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x60
   __DATA.__objc_const: 0x2f0
-  __DATA.__objc_selrefs: 0x80
-  __DATA.__data: 0x590
+  __DATA.__objc_selrefs: 0x90
+  __DATA.__data: 0x660
   __DATA.__common: 0x48
-  __DATA.__bss: 0xe00
+  __DATA.__bss: 0x1280
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 637
-  Symbols:   121
-  CStrings:  142
+  Functions: 772
+  Symbols:   129
+  CStrings:  161
 
Symbols:
+ _CKErrorDomain
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCompression
+ _objc_retain_x21
+ _objc_retain_x22
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_getForeignTypeMetadata
- _objc_retain_x25
CStrings:
+ "Assets already available. Skipping payload download for task: %s"
+ "CKError: %@"
+ "Computed addedTaskNames: %s"
+ "Computed payloadsTaskNames: %s"
+ "Decompression completed: %s"
+ "Decompression failed: %@"
+ "Failed at asset to: %s : %@"
+ "Failed at creating extractStream: %s"
+ "Failed at decoding archive: %s"
+ "Failed at decompressing archive: %s"
+ "Failed at processing archive, copying raw archive into taskFolder."
+ "Failed at reading archive: %s"
+ "Found CloudKit rate-limit, deferring execution."
+ "Processing TaskParametersRecords: %s"
+ "Processing TaskPayloadRecords: %s"
+ "Querying TaskParameters for added tasks: %s"
+ "Querying TaskPayloads for new tasks: %s"
+ "Skipping registeredTask %s due to lack of taskFolder."
+ "Task %s not registered on the system. Skipping task."
+ "Task cancelled before while processing TaskPayloads."
+ "TaskPayload extracted at: %s"
+ "Unable to create destination directory: %s"
+ "copyItemAtURL:toURL:error:"
+ "fileExistsAtPath:"
- "Querying TaskParameters for fetched tasks: %s"
- "Querying TaskPayload for fetched tasks: %s"
- "Task %s not registred on the system. Skipping task."
- "Task cancelled during parsing of TaskParameters."
- "Task cancelled during parsing of TaskPayloads."

```
