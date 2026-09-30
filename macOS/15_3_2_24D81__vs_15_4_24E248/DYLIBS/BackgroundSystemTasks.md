## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks`

```diff

-1786.80.10.0.0
-  __TEXT.__text: 0x11d8c
+1856.101.1.0.0
+  __TEXT.__text: 0x120e8
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0xe44
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x8a9
-  __TEXT.__oslogstring: 0x1b81
-  __TEXT.__gcc_except_tab: 0x4f8
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__objc_classname: 0x205
-  __TEXT.__objc_methname: 0x3340
-  __TEXT.__objc_methtype: 0x4a4
-  __TEXT.__objc_stubs: 0x1fe0
+  __TEXT.__objc_methlist: 0xfdc
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x8da
+  __TEXT.__oslogstring: 0x1bf3
+  __TEXT.__gcc_except_tab: 0x548
+  __TEXT.__unwind_info: 0x450
+  __TEXT.__objc_classname: 0x206
+  __TEXT.__objc_methname: 0x33c8
+  __TEXT.__objc_methtype: 0x48f
+  __TEXT.__objc_stubs: 0x2060
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f8
+  __DATA_CONST.__objc_selrefs: 0xa90
   __DATA_CONST.__objc_superrefs: 0x58
   __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x530
-  __AUTH_CONST.__cfstring: 0xb80
-  __AUTH_CONST.__objc_const: 0x2578
+  __AUTH_CONST.__cfstring: 0xba0
+  __AUTH_CONST.__objc_const: 0x22f0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/Versions/A/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C02DD052-8E74-3281-8C20-DD6E570DF47A
-  Functions: 472
-  Symbols:   1164
-  CStrings:  949
+  UUID: 170B5B94-0265-323D-AEF8-B0E2A6CAC8F7
+  Functions: 480
+  Symbols:   1184
+  CStrings:  956
 
Symbols:
+ +[BGSystemTask logger].cold.1
+ +[BGSystemTaskCheckpoints logger].cold.1
+ +[BGSystemTaskRequest taskRequestWithDescriptor:withIdentifier:].cold.12
+ +[BGSystemTaskScheduler sharedScheduler].cold.1
+ +[BGSystemTaskWorkload logger].cold.1
+ -[BGSystemTask queue_reportBufferedTaskWorkloadProgress]
+ -[BGSystemTaskRequest applicationRelationship]
+ -[BGSystemTaskRequest setApplicationRelationship:]
+ GCC_except_table100
+ GCC_except_table153
+ GCC_except_table159
+ GCC_except_table160
+ GCC_except_table36
+ GCC_except_table7
+ GCC_except_table77
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table88
+ GCC_except_table93
+ GCC_except_table96
+ OBJC_IVAR_$_BGSystemTaskRequest._applicationRelationship
+ __54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.110
+ __58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.128
+ __58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.124
+ __63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.109
+ __63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.109.cold.1
+ __68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.129
+ __77-[BGSystemTask sendTaskWorkloadProgressToPPS:completed:category:subCategory:]_block_invoke.cold.1
+ ___80-[BGSystemTask reportTaskWorkloadProgress:completed:category:subCategory:error:]_block_invoke
+ ___block_descriptor_88_e8_32s40s48r56r_e5_v8?0l
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _objc_msgSend$applicationRelationship
+ _objc_msgSend$handleClientFailedtoExpireTaskWithIdentifier:completionHandler:
+ _objc_msgSend$queue_reportBufferedTaskWorkloadProgress
+ _objc_msgSend$setApplicationRelationship:
+ _objc_msgSend$useStatisticalModelForTriggersRestart
- +[BGSystemTaskCheckpoints reportTaskCheckpoint:forTask:value:error:]
- -[BGSystemTask reportBufferedTaskWorkloadProgress]
- GCC_except_table151
- GCC_except_table152
- GCC_except_table8
- GCC_except_table80
- GCC_except_table83
- GCC_except_table87
- GCC_except_table92
- GCC_except_table95
- GCC_except_table99
- __54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.109
- __58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.127
- __58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.123
- __68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.128
- __77-[BGSystemTask sendTaskWorkloadProgressToPPS:completed:category:subCategory:]_block_invoke_2.cold.1
- ___77-[BGSystemTask sendTaskWorkloadProgressToPPS:completed:category:subCategory:]_block_invoke_2
- ___block_descriptor_80_e8_32s40s48r_e5_v8?0l
- _objc_msgSend$reportBufferedTaskWorkloadProgress
CStrings:
+ "%{public}@: relatedApplications cannot be empty when applicationRelationship is set to true"
+ "ApplicationRelationship"
+ "RunWhenAppLaunchUnlikely"
+ "Tq,N,V_applicationRelationship"
+ "_applicationRelationship"
+ "applicationRelationship"
+ "handleClientFailedtoExpireTaskWithIdentifier failed for %{public}@"
+ "handleClientFailedtoExpireTaskWithIdentifier:completionHandler:"
+ "queue_reportBufferedTaskWorkloadProgress"
+ "setApplicationRelationship:"
- "B48@0:8Q16@24@32^@40"
- "Received checkpoint %lu for %@ with value %@"
- "reportBufferedTaskWorkloadProgress"
- "reportTaskCheckpoint:forTask:value:error:"

```
