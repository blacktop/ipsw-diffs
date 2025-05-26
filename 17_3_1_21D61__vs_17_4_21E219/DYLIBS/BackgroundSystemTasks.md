## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`

```diff

-1439.80.3.0.0
-  __TEXT.__text: 0x6070
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x824
-  __TEXT.__const: 0x78
+1470.100.56.0.0
+  __TEXT.__text: 0x694c
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_methlist: 0x8ac
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x581
+  __TEXT.__oslogstring: 0xa96
   __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__cstring: 0x550
-  __TEXT.__oslogstring: 0x911
-  __TEXT.__unwind_info: 0x194
-  __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0x1bf6
-  __TEXT.__objc_methtype: 0x287
-  __TEXT.__objc_stubs: 0x1240
+  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__objc_classname: 0x11a
+  __TEXT.__objc_methname: 0x1cec
+  __TEXT.__objc_methtype: 0x2d8
+  __TEXT.__objc_stubs: 0x12e0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x218
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf50
-  __DATA_CONST.__objc_selrefs: 0x570
-  __AUTH_CONST.__objc_const: 0x318
+  __DATA_CONST.__objc_const: 0xf98
+  __DATA_CONST.__objc_selrefs: 0x5a8
+  __DATA_CONST.__objc_classrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x40
+  __AUTH_CONST.__objc_const: 0x3f0
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x7e0
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x2b8
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x60
-  __DATA.__objc_superrefs: 0x40
+  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x10c
   __DATA.__data: 0x60
-  __DATA_DIRTY.__objc_data: 0x230
+  __DATA.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 222
-  Symbols:   856
-  CStrings:  475
+  Functions: 234
+  Symbols:   909
+  CStrings:  499
 
Symbols:
+ +[BGSystemTask logger]
+ +[BGSystemTaskCheckpoints logger]
+ +[BGSystemTaskCheckpoints reportCustomCheckpoint:forTask:error:]
+ +[BGSystemTaskCheckpoints reportFeatureCheckpoint:forFeature:error:]
+ +[BGSystemTaskCheckpoints reportTaskCheckpoint:forTask:value:error:]
+ +[BGSystemTaskWorkload logger]
+ +[BGSystemTaskWorkload reportSystemWorkload:ofCategory:error:]
+ -[BGSystemTask clearLocked]
+ -[BGSystemTask reportTaskWorkloadProgress:completed:category:subCategory:error:]
+ GCC_except_table6
+ _BGSystemTaskCustomCheckpointMax
+ _BGSystemTaskCustomCheckpointMin
+ _OBJC_CLASS_$_BGSystemTaskCheckpoints
+ _OBJC_CLASS_$_BGSystemTaskWorkload
+ _OBJC_METACLASS_$_BGSystemTaskCheckpoints
+ _OBJC_METACLASS_$_BGSystemTaskWorkload
+ __OBJC_$_CLASS_METHODS_BGSystemTask
+ __OBJC_$_CLASS_METHODS_BGSystemTaskCheckpoints
+ __OBJC_$_CLASS_METHODS_BGSystemTaskWorkload
+ __OBJC_CLASS_RO_$_BGSystemTaskCheckpoints
+ __OBJC_CLASS_RO_$_BGSystemTaskWorkload
+ __OBJC_METACLASS_RO_$_BGSystemTaskCheckpoints
+ __OBJC_METACLASS_RO_$_BGSystemTaskWorkload
+ ___22+[BGSystemTask logger]_block_invoke
+ ___30+[BGSystemTaskWorkload logger]_block_invoke
+ ___33+[BGSystemTaskCheckpoints logger]_block_invoke
+ _logger.log
+ _logger.onceToken
+ _objc_msgSend$clearLocked
+ _objc_msgSend$logger
+ _objc_msgSend$reportCustomCheckpoint:forTask:error:
+ _objc_msgSend$reportFeatureCheckpoint:forFeature:error:
+ _objc_msgSend$reportSystemWorkload:ofCategory:error:
+ _objc_retain_x3
+ _objc_retain_x5
- GCC_except_table3
CStrings:
+ "B40@0:8Q16@24^@32"
+ "B40@0:8Q16Q24^@32"
+ "B48@0:8Q16@24@32^@40"
+ "B56@0:8Q16Q24Q32@40^@48"
+ "BGSTCheckpoint"
+ "BGSystemTaskCheckpoints"
+ "BGSystemTaskWorkload"
+ "Completed %lu [Target:%lu] for workload %lu, subcategory %@"
+ "Error:%@ custom checkpoint %lu for task %@"
+ "Error:%@ feature checkpoint %lu for feature %lu"
+ "Error:%@ reporting system workload %lu for category %lu"
+ "Received checkpoint %lu for %@ with value %@"
+ "Received custom checkpoint %lu for task %@"
+ "Received feature checkpoint %lu for feature %lu"
+ "Received system workload %lu for category %lu"
+ "clearLocked"
+ "logger"
+ "reportCustomCheckpoint:forTask:error:"
+ "reportFeatureCheckpoint:forFeature:error:"
+ "reportSystemWorkload:ofCategory:error:"
+ "reportTaskCheckpoint:forTask:value:error:"
+ "reportTaskWorkloadProgress:completed:category:subCategory:error:"

```
