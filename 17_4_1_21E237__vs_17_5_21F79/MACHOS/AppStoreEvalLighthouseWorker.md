## AppStoreEvalLighthouseWorker

> `/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker`

```diff

-1.2.29.0.0
-  __TEXT.__text: 0xe0d0
-  __TEXT.__auth_stubs: 0x9d0
+1.2.34.0.0
+  __TEXT.__text: 0x12530
+  __TEXT.__auth_stubs: 0xa10
   __TEXT.__const: 0x2e2
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x1fd
+  __TEXT.__swift5_typeref: 0x2c1
   __TEXT.__constg_swiftt: 0x74
-  __TEXT.__swift5_reflstr: 0x29
-  __TEXT.__swift5_fieldmd: 0x54
+  __TEXT.__swift5_reflstr: 0x31
+  __TEXT.__swift5_fieldmd: 0x6c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__cstring: 0x9a4
-  __TEXT.__objc_methname: 0x203
-  __TEXT.__swift5_capture: 0xe0
+  __TEXT.__cstring: 0x924
+  __TEXT.__swift5_capture: 0x510
+  __TEXT.__objc_methname: 0x233
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__eh_frame: 0x298
-  __DATA_CONST.__auth_got: 0x4e8
+  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__eh_frame: 0x390
+  __DATA_CONST.__auth_got: 0x508
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x530
+  __DATA_CONST.__const: 0xfb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x30
-  __DATA.__objc_selrefs: 0x80
-  __DATA.__data: 0x1c0
+  __DATA_CONST.__objc_classrefs: 0x38
+  __DATA.__objc_selrefs: 0x98
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x550
   __DATA.__common: 0x18
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppStoreEvalLighthouseUtils.framework/AppStoreEvalLighthouseUtils

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BE60DC59-C217-37C8-893E-2D26EC00D28F
-  Functions: 171
-  Symbols:   105
-  CStrings:  68
+  UUID: A835C89D-74F6-3277-AA3C-753D5553D917
+  Functions: 279
+  Symbols:   106
+  CStrings:  76
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_release_n
- _objc_release_x28
- _objc_retain_x9
- _swift_initStackObject
CStrings:
+ "%s has already run and runOnce is true. Exiting early."
+ "Execution state saved for taskName %s."
+ "Failed to instantiate userDefaults with suiteName %s. Exiting early."
+ "Unable to parse config. Exiting early."
+ "boolForKey:"
+ "com.apple.AppleMediaDiscoveryLighthousePlugin"
+ "context.taskName %s"
+ "initWithSuiteName:"
+ "setValue:forKey:"
- "  {\"DataProcessingAndModelTraining\": [{\"DataProcessing\": [{\"FunctionName\": \"InsertRawArray\", \"InputArray\": [0], \"OutputArray\": \"temp_name_list_0\"}, {\"FunctionName\": \"ReplicateArray\", \"InputArray\": \"temp_name_list_0\", \"NumberOfCopies\": 1, \"OutputArray\": \"metric\"}], \"DataPostProcessing\": [], \"FinalMetricsToCollect\": [\"metric\"], \"ModelName\": \"my_experiment_name\"}], \"LoggingStrategies\": [], \"AttachmentKeys\": [], \"AttachmentInstructions\": []}"

```
