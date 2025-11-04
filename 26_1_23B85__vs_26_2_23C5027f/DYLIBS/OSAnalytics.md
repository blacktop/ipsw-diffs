## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

```diff

-927.40.4.0.0
-  __TEXT.__text: 0x47194
-  __TEXT.__auth_stubs: 0x1980
-  __TEXT.__objc_methlist: 0x1bf0
-  __TEXT.__const: 0x710
-  __TEXT.__oslogstring: 0x3b0c
-  __TEXT.__cstring: 0x9206
-  __TEXT.__gcc_except_tab: 0x12ac
+927.60.5.0.0
+  __TEXT.__text: 0x4a874
+  __TEXT.__auth_stubs: 0x1b50
+  __TEXT.__objc_methlist: 0x1c78
+  __TEXT.__const: 0x748
+  __TEXT.__oslogstring: 0x3d2c
+  __TEXT.__cstring: 0x936e
+  __TEXT.__gcc_except_tab: 0x125c
   __TEXT.__dlopen_cstrs: 0x21f
+  __TEXT.__swift5_typeref: 0xea
+  __TEXT.__swift5_capture: 0x80
   __TEXT.__constg_swiftt: 0x130
-  __TEXT.__swift5_typeref: 0x7e
   __TEXT.__swift5_fieldmd: 0x64
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_reflstr: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xcb8
-  __TEXT.__eh_frame: 0x170
+  __TEXT.__unwind_info: 0xde0
+  __TEXT.__eh_frame: 0x348
   __TEXT.__objc_classname: 0x318
-  __TEXT.__objc_methname: 0x5123
+  __TEXT.__objc_methname: 0x5256
   __TEXT.__objc_methtype: 0xc05
-  __TEXT.__objc_stubs: 0x4940
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x12c8
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__objc_stubs: 0x4a20
+  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__const: 0x1310
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1638
+  __DATA_CONST.__objc_selrefs: 0x1698
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x970
-  __AUTH_CONST.__auth_got: 0xcd0
-  __AUTH_CONST.__const: 0x4a1
-  __AUTH_CONST.__cfstring: 0xa0a0
-  __AUTH_CONST.__objc_const: 0x38b8
+  __DATA_CONST.__objc_arraydata: 0x990
+  __AUTH_CONST.__auth_got: 0xdb8
+  __AUTH_CONST.__const: 0x660
+  __AUTH_CONST.__cfstring: 0xa1e0
+  __AUTH_CONST.__objc_const: 0x3900
   __AUTH_CONST.__objc_intobj: 0x4c8
-  __AUTH_CONST.__objc_dictobj: 0x550
+  __AUTH_CONST.__objc_dictobj: 0x5a0
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x340
-  __AUTH.__data: 0x168
+  __AUTH.__objc_data: 0x3b0
+  __AUTH.__data: 0x190
   __DATA.__objc_ivar: 0x2cc
-  __DATA.__data: 0x1d8
+  __DATA.__data: 0x218
   __DATA.__bss: 0x178
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x2b8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7459F48E-2A3B-37A8-BA2B-DEE2D63BB2B9
-  Functions: 1150
-  Symbols:   3963
-  CStrings:  4326
+  UUID: 22F9789F-E942-3A93-B220-0CCC9D395BD6
+  Functions: 1234
+  Symbols:   4054
+  CStrings:  4378
 
Symbols:
+ +[OSATasking applyTasking:taskId:fromBlob:].cold.4
+ +[OSATasking installCATasking:withId:untasked:]
+ +[OSATasking installCATasking:withId:untasked:].cold.1
+ +[OSATasking installCATasking:withId:untasked:].cold.2
+ +[OSATasking installCATasking:withId:untasked:].cold.3
+ +[OSATasking installCATasking:withId:untasked:].cold.4
+ +[OSATasking installCATasking:withId:untasked:].cold.5
+ +[OSATasking installCATasking:withId:untasked:].cold.6
+ +[OSATasking proxyTasking:taskId:usingConfig:fromBlob:].cold.1
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_FileUtils
+ _OBJC_METACLASS_$_FileUtils
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_FileUtils
+ __DATA_FileUtils
+ __INSTANCE_METHODS_FileUtils
+ __METACLASS_DATA_FileUtils
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382.cold.1
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382.cold.2
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382.cold.3
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382.cold.4
+ ___43+[OSATasking applyTasking:taskId:fromBlob:]_block_invoke.104
+ ___61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.466
+ ___block_literal_global.39
+ ___block_literal_global.59
+ ___rtc_internal_block_invoke.62
+ ___rtc_internal_block_invoke.62.cold.1
+ ___rtc_internal_block_invoke.62.cold.2
+ ___rtc_internal_block_invoke.62.cold.3
+ ___rtc_internal_block_invoke.64
+ ___rtc_internal_block_invoke.65.cold.1
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ __set_user_dir_suffix
+ _block_copy_helper
+ _block_copy_helper.22
+ _block_copy_helper.28
+ _block_copy_helper.7
+ _block_descriptor
+ _block_descriptor.24
+ _block_descriptor.30
+ _block_descriptor.9
+ _block_destroy_helper
+ _block_destroy_helper.23
+ _block_destroy_helper.29
+ _block_destroy_helper.8
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$floatValue
+ _objc_msgSend$installCATasking:withId:untasked:
+ _objc_msgSend$moveItemAtURL:toURL:error:
+ _objc_msgSend$setXattrWithName:value:at:
+ _objc_msgSend$temporaryFileWithPrefix:fd:
+ _objc_msgSend$writeToURL:atomically:
+ _objc_msgSend$writeToURL:options:error:
+ _strcpy
+ _swift_deallocObject
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_isEscapingClosureAtFileLocation
+ _symbolic SPy_____GSg s4Int8V
+ _symbolic SSSg
+ _symbolic Say_____G s5UInt8V
+ _symbolic So8NSStringCIeyBa_
+ _symbolic Spy_____GSg s4Int8V
+ _symbolic SvSgS2iIgyyd_
+ _symbolic _____ 10Foundation3URLV
+ _symbolic _____ s5Int32V
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s4Int8V
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370.cold.1
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370.cold.2
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370.cold.3
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370.cold.4
- ___43+[OSATasking applyTasking:taskId:fromBlob:]_block_invoke.101
- ___61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.454
- ___block_literal_global.40
- ___block_literal_global.60
- ___rtc_internal_block_invoke.63
- ___rtc_internal_block_invoke.63.cold.1
- ___rtc_internal_block_invoke.63.cold.2
- ___rtc_internal_block_invoke.63.cold.3
- ___rtc_internal_block_invoke.66
- ___rtc_internal_block_invoke.66.cold.1
- ___swift_destroy_boxed_opaque_existential_1Tm
- _objc_msgSend$writeToFile:options:error:
CStrings:
+ "%@-seed"
+ "%f"
+ "' on file with descriptor '"
+ "@\"NSString\"8@?0"
+ "@32@0:8@16^i24"
+ "@32@0:8@?16@?24"
+ "B40@0:8@16@24@32"
+ "Carrier"
+ "CarrierSeed"
+ "Error reading %s: expected to read %ld bytes but read %ld bytes"
+ "Failed to generate temporary file: error %d (%s)"
+ "Failed to read %s: error %d (%s)"
+ "Failed to set xattr '%s' at path '%s': error %d (%s)"
+ "FileUtils"
+ "Seed"
+ "URLByAppendingPathComponent:"
+ "bad_blob_%@_%@"
+ "failed to clean up ca1 tasking: %@"
+ "failed to generate temporary file"
+ "failed to open tasking payload file: %s"
+ "failed to remove previous ca1 tasking: %@"
+ "failed to save ca1 tasking: %@"
+ "failed to save proxy tasking: [%d] %s"
+ "failed to send tasking availability notification to analyticsd"
+ "failed to write CA tasking blob to temporary path"
+ "failed to write CA tasking blob to temporary path: %@"
+ "floatValue"
+ "getXattrBoolValWithName:at:"
+ "getXattrWithName:at:"
+ "getXattrWithName:onFile:"
+ "hasXattrWithName:at:"
+ "installCATasking:withId:untasked:"
+ "moveItemAtURL:toURL:error:"
+ "nothing to do for ca1 tasking update"
+ "q24@?0^v8q16"
+ "readXattrWithReader:errorContext:"
+ "seed"
+ "sendAsMessage"
+ "setXattrWithName:value:at:"
+ "successfully applied ca1 tasking update: %@"
+ "tasked-cfg_%@"
+ "temporaryFileWithPrefix:fd:"
+ "writeToURL:atomically:"
+ "writeToURL:options:error:"
- "/tmp/bad_%@_%@.blob"
- "GM"
- "payload"
- "saving proxy tasking as %@"
- "writeToFile:options:error:"

```
