## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-162.11.0.0.0
-  __TEXT.__cstring: 0x690a
+162.16.1.0.0
+  __TEXT.__cstring: 0x6a09
   __TEXT.__os_log: 0x568f
   __TEXT.__const: 0xe4
-  __TEXT_EXEC.__text: 0x49ed8
+  __TEXT_EXEC.__text: 0x4a19c
   __TEXT_EXEC.__auth_stubs: 0xe30
   __DATA.__data: 0x460
   __DATA.__common: 0x8e8
   __DATA.__bss: 0x9
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x110
-  __DATA_CONST.__const: 0xd2d0
+  __DATA_CONST.__const: 0xd2d8
   __DATA_CONST.__kalloc_type: 0x1240
   __DATA_CONST.__kalloc_var: 0x1090
   __DATA_CONST.__assert: 0x28
   __DATA_CONST.__auth_got: 0x718
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2168
-  Symbols:   3680
+  Functions: 2170
+  Symbols:   3682
   CStrings:  981
 
Symbols:
+ __ZN19IOGPUSurfaceMTLList18retainSurfaceForIDEjP4task
+ __ZN5IOGPU15flushUnmapQueueEv
+ __ZN5IOGPU16thread_stall_endE29eIOGPUSubmissionStallLocation
+ __ZN5IOGPU18thread_stall_beginE29eIOGPUSubmissionStallLocation
+ __ZZN14IOGPUScheduler20registerCommandQueueEPK17IOGPUCommandQueueE21kalloc_type_view_2301
+ __ZZN14IOGPUScheduler20registerCommandQueueEPK17IOGPUCommandQueueE21kalloc_type_view_2309
+ __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1150
+ __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1188
+ __ZZN17IOGPUEventMachine19setStampBaseAddressEPVjE20kalloc_type_view_114
+ __ZZN17IOGPUEventMachine4freeEvE19kalloc_type_view_93
+ __ZZN5IOGPU4freeEvE21kalloc_type_view_1009
+ __ZZN5IOGPU5startEP9IOServiceE20kalloc_type_view_359
- _ZN5IOGPU15systemPagingOffEv
- __ZN19IOGPUSurfaceMTLList18retainSurfaceForIDEj
- __ZZN14IOGPUScheduler20registerCommandQueueEPK17IOGPUCommandQueueE21kalloc_type_view_2294
- __ZZN14IOGPUScheduler20registerCommandQueueEPK17IOGPUCommandQueueE21kalloc_type_view_2302
- __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1146
- __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1184
- __ZZN17IOGPUEventMachine19setStampBaseAddressEPVjE20kalloc_type_view_112
- __ZZN17IOGPUEventMachine4freeEvE19kalloc_type_view_91
- __ZZN5IOGPU4freeEvE20kalloc_type_view_992
- __ZZN5IOGPU5startEP9IOServiceE20kalloc_type_view_342
CStrings:
+ "\"IOGPU::systemPagingOff() timeout. %d threads still stuck. addCommandToTail_slow %u, waitForAllSubmitted %u, workQueuesDisabled %u, waitingOnResources %u, waitForStamp %u, wireMemory %u\\n\" @%s:%d"
+ "1211111212221212121111111212211121222221111112112211122211111121112112122222222222222222222222222122212"
+ "IOGPU::systemPagingOff() timeout. %d threads still stuck. addCommandToTail_slow %u, waitForAllSubmitted %u, workQueuesDisabled %u, waitingOnResources %u, waitForStamp %u, wireMemory %u\n"
- "\"IOGPU::systemPagingOff() timeout. %d threads still stuck.\\n\" @%s:%d"
- "121111121222121212111111121211121222221111112112211122211111121112112122222222222222222222222222122212"
- "IOGPU::systemPagingOff() timeout. %d threads still stuck.\n"
```
