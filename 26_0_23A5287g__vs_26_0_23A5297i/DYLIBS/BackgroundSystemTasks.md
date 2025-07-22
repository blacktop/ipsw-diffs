## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`

```diff

-2109.0.69.0.1
-  __TEXT.__text: 0x13194
+2109.0.84.0.0
+  __TEXT.__text: 0x13388
   __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_methlist: 0x1264
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0xa35
-  __TEXT.__oslogstring: 0x1f64
-  __TEXT.__gcc_except_tab: 0x6d4
-  __TEXT.__unwind_info: 0x4f8
+  __TEXT.__oslogstring: 0x1fc5
+  __TEXT.__gcc_except_tab: 0x758
+  __TEXT.__unwind_info: 0x508
   __TEXT.__objc_classname: 0x266
   __TEXT.__objc_methname: 0x3d4c
   __TEXT.__objc_methtype: 0x52d
   __TEXT.__objc_stubs: 0x25a0
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x670
+  __DATA_CONST.__const: 0x698
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B36F2B64-DC44-38C4-955E-11381476EE90
-  Functions: 513
-  Symbols:   1861
-  CStrings:  1114
+  UUID: 0FB33C78-46BA-3D92-8E83-85EFA0CEA765
+  Functions: 516
+  Symbols:   1871
+  CStrings:  1115
 
Symbols:
+ -[BGSystemTaskScheduler handleDeniedTaskLaunch:].cold.3
+ GCC_except_table12
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table25
+ GCC_except_table30
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table76
+ ___27-[BGSystemTask clearLocked]_block_invoke
+ ___48-[BGSystemTaskScheduler handleDeniedTaskLaunch:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- GCC_except_table11
- GCC_except_table18
- GCC_except_table20
- GCC_except_table24
- GCC_except_table38
- GCC_except_table40
- GCC_except_table54
- GCC_except_table56
- GCC_except_table59
- GCC_except_table63
- GCC_except_table66
- GCC_except_table69
- GCC_except_table71
- GCC_except_table75
Functions:
~ -[BGSystemTask clearLocked] : 144 -> 212
~ +[BGSystemTaskWorkload reportSystemWorkload:ofCategory:error:] : 372 -> 380
~ -[BGSystemTaskScheduler handleDeniedTaskLaunch:] : 300 -> 708
+ ___48-[BGSystemTaskScheduler handleDeniedTaskLaunch:]_block_invoke
~ _OUTLINED_FUNCTION_1 : 20 -> 24
~ _OUTLINED_FUNCTION_2 : 28 -> 20
~ _OUTLINED_FUNCTION_3 : 12 -> 28
~ _OUTLINED_FUNCTION_8 : 32 -> 12
~ _OUTLINED_FUNCTION_9 : 12 -> 16
~ _OUTLINED_FUNCTION_11 : 12 -> 32
+ ___27-[BGSystemTask clearLocked]_block_invoke
~ ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.cold.7 : 160 -> 164
~ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke_2.cold.1 : 128 -> 120
~ -[BGSystemTaskScheduler handleDeniedTaskLaunch:].cold.1 : 164 -> 72
~ -[BGSystemTaskScheduler handleDeniedTaskLaunch:].cold.2 : 164 -> 72
+ -[BGSystemTaskScheduler handleDeniedTaskLaunch:].cold.3
~ -[BGSystemTaskScheduler systemTask:producedResults:error:].cold.1 : 88 -> 80
~ ___58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.cold.1 : 184 -> 192
~ -[BGSystemTaskScheduler systemTask:consumedResults:error:].cold.1 : 88 -> 80
~ ___58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.cold.1 : 192 -> 196
~ ___68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.cold.1 : 172 -> 176
CStrings:
+ "Task request for %{public}@ was already cleared before handleDeniedTaskLaunch could copy it (%@)"

```
