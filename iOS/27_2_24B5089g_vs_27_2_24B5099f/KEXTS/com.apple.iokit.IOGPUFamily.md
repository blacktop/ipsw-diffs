## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-162.14.0.0.0
-  __TEXT.__cstring: 0x61ea
-  __TEXT.__os_log: 0x535a
+162.16.1.0.0
+  __TEXT.__cstring: 0x62b2
+  __TEXT.__os_log: 0x52f6
   __TEXT.__const: 0x8c
-  __TEXT_EXEC.__text: 0x42500
+  __TEXT_EXEC.__text: 0x42700
   __TEXT_EXEC.__auth_stubs: 0xdc0
   __DATA.__data: 0x460
   __DATA.__common: 0x898

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 2004
   Symbols:   0
-  CStrings:  923
+  CStrings:  921
 
CStrings:
+ "\"IOGPU::systemPagingOff() timeout. %d threads still stuck. addCommandToTail_slow %u, waitForAllSubmitted %u, workQueuesDisabled %u, waitingOnResources %u, waitForStamp %u, wireMemory %u\\n\" @%s:%d"
+ "12111111212112222222222111122211122222111112111222222111122212222122222221"
+ "1211111212221212121111111212211121222221111112112211122111112122222222222222222222222222122212"
+ "IOGPU::systemPagingOff() timeout. %d threads still stuck. addCommandToTail_slow %u, waitForAllSubmitted %u, workQueuesDisabled %u, waitingOnResources %u, waitForStamp %u, wireMemory %u\n"
- "\"IOGPU::systemPagingOff() timeout. %d threads still stuck.\\n\" @%s:%d"
- "%s: promoting NoResources->NoMemory on workQueue %p: outstanding=%u throttled=%u prepareSeed=%u/%u\n"
- "121111112121122222222221111222111222221111121112222111122212222122222221"
- "121111121222121212111111121211121222221111112112211122111112122222222222222222222222222122212"
- "IOGPU::systemPagingOff() timeout. %d threads still stuck.\n"
- "void IOGPUScheduler::scheduleWorkqueue(IOGPUWorkQueue *)"
```
