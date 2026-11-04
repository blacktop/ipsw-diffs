## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-162.16.1.0.0
-  __TEXT.__cstring: 0x62b2
-  __TEXT.__os_log: 0x52f6
+163.1.4.0.0
+  __TEXT.__cstring: 0x644e
+  __TEXT.__os_log: 0x52e4
   __TEXT.__const: 0x8c
-  __TEXT_EXEC.__text: 0x42700
+  __TEXT_EXEC.__text: 0x43648
   __TEXT_EXEC.__auth_stubs: 0xdc0
-  __DATA.__data: 0x460
-  __DATA.__common: 0x898
+  __DATA.__data: 0x4b0
+  __DATA.__common: 0x8a0
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0x6fd8
+  __DATA_CONST.__const: 0x7018
   __DATA_CONST.__kalloc_type: 0x11c0
   __DATA_CONST.__kalloc_var: 0x1090
   __DATA_CONST.__assert: 0x28
   __DATA_CONST.__auth_got: 0x6e0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2004
+  Functions: 2016
   Symbols:   0
-  CStrings:  921
+  CStrings:  929
 
CStrings:
+ "\"Evicted member not found in main set\" @%s:%d"
+ "%s <%s> (%p) : required > max : descriptorBytes = <%llu> preparedBytes : <%llu> maxWired = <%llu> maxWiredInternal = <%llu> currentWired = <%llu>\n"
+ "%s: failed to grow pending set to %u, reclaim may have to allocate\n"
+ "%s: nothing to reclaim, bytes == 0, type %u\n"
+ "%s: pending set full at %u members, stopping eviction early\n"
+ "%s: promoting NoResources->NoMemory on workQueue %p: outstanding=%u throttled=%u prepareSeed=%u/%u\n"
+ "121111112121122222222221111222111222221111121112222111122212222122222221"
+ "1212222221211122111112222221111122222222"
+ "Disable residency-set reclaim mitigations: demand full-teardown instead of partial evict(bytes), and skip the collector's per-group grace"
+ "IOReturn IOGPUScheduler::freeToWireSysMemoryStrictLRU(uint64_t, eIOGPUWiredMemoryType, IOGPUMemory *)"
+ "disable_partial_evict"
+ "virtual bool IOGPUGroupMemory::evict(uint64_t)"
+ "void IOGPUScheduler::scheduleWorkqueue(IOGPUWorkQueue *)"
- "%s <%s> (%p) : required > max : requiredBytes = <%llu> preparedBytes : <%llu> maxWired = <%llu> maxWiredInternal = <%llu> currentWired = <%llu>\n"
- "%s <%s>: preparedBytes != requiredBytes : preparedBytes = <%llu> requiredBytes = <%llu> maxWired = <%llu> preWiring = <%llu> currentWired = <%llu> wiring delta = <%llu>\n\n"
- "%s <%s>: requiredBytes = <%llu> maxWired = <%llu> preparedBytes : <%llu> remainingBytes : <%lld> remainingPages = <%lld>\n\n"
- "12111111212112222222222111122211122222111112111222222111122212222122222221"
- "12122222212111221111122222211111222222"
```
