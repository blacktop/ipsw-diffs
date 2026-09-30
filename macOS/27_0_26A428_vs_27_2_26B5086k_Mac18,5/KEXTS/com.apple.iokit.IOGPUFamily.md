## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-162.11.0.0.0
-  __TEXT.__cstring: 0x690a
-  __TEXT.__os_log: 0x568f
+162.13.0.0.0
+  __TEXT.__cstring: 0x6941
+  __TEXT.__os_log: 0x56f3
   __TEXT.__const: 0xe4
-  __TEXT_EXEC.__text: 0x482e8
+  __TEXT_EXEC.__text: 0x482fc
   __TEXT_EXEC.__auth_stubs: 0xe30
   __DATA.__data: 0x460
   __DATA.__common: 0x8e8

   __DATA_CONST.__auth_got: 0x718
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2168
-  Symbols:   3680
-  CStrings:  981
+  Functions: 2169
+  Symbols:   3682
+  CStrings:  983
 
Symbols:
+ __ZN14IOGPUScheduler32decrementOutstandingCommandCountEv
+ __ZZN14IOGPUScheduler17scheduleWorkqueueEP14IOGPUWorkQueueE11_os_log_fmt
+ __ZZN14IOGPUScheduler20registerCommandQueueEPK17IOGPUCommandQueueE21kalloc_type_view_2269
+ __ZZN14IOGPUScheduler20registerCommandQueueEPK17IOGPUCommandQueueE21kalloc_type_view_2277
+ __ZZN14IOGPUScheduler4freeEvE20kalloc_type_view_310
+ __ZZN14IOGPUScheduler4initEP5IOGPUE20kalloc_type_view_142
- __ZZN14IOGPUScheduler20registerCommandQueueEPK17IOGPUCommandQueueE21kalloc_type_view_2294
- __ZZN14IOGPUScheduler20registerCommandQueueEPK17IOGPUCommandQueueE21kalloc_type_view_2302
- __ZZN14IOGPUScheduler4freeEvE20kalloc_type_view_312
- __ZZN14IOGPUScheduler4initEP5IOGPUE20kalloc_type_view_144
CStrings:
+ "%s: promoting NoResources->NoMemory on workQueue %p: outstanding=%u throttled=%u prepareSeed=%u/%u\n"
+ "1211111121211222222222211211222111222221111121112222111122212222122222221"
+ "void IOGPUScheduler::scheduleWorkqueue(IOGPUWorkQueue *)"
- "121111112121122222222221121122211122222111112111222222111122212222122222221"
```
