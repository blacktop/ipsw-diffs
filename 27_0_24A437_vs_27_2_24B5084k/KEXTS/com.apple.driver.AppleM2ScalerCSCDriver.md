## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-200.62.4.0.0
-  __TEXT.__const: 0xc3090
-  __TEXT.__cstring: 0x2515b
-  __TEXT_EXEC.__text: 0x13bab8
+200.66.0.0.0
+  __TEXT.__const: 0xc3140
+  __TEXT.__cstring: 0x2534c
+  __TEXT_EXEC.__text: 0x13c150
   __TEXT_EXEC.__auth_stubs: 0xbd0
   __DATA.__data: 0x22388
   __DATA.__common: 0x2738
   __DATA_CONST.__mod_init_func: 0x698
   __DATA_CONST.__mod_term_func: 0x670
-  __DATA_CONST.__const: 0x2abf0
+  __DATA_CONST.__const: 0x2ac90
   __DATA_CONST.__kalloc_type: 0x4e80
   __DATA_CONST.__kalloc_var: 0x13b0
   __DATA_CONST.__auth_got: 0x5e8
-  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x88
-  Functions: 10262
+  Functions: 10275
   Symbols:   0
-  CStrings:  3704
+  CStrings:  3714
 
CStrings:
+ "\"[%s] \" \"Failed to load MsrCPU firmware %s: MSR%u scaler %u path=%s embedded=%u imem0=0x%08x apImg0=0x%08x bootProgress=%s(0x%08x) bootEntries=%u running=0x%08x ibootFw=%d ctrrLock=%u ctrrWrDis=%u\\n\" @%s:%d"
+ "%.4s"
+ "121111121222121211111111111221221121121212212222"
+ "12111121221111111222"
+ "121111212211111112222"
+ "12111121221111111222222"
+ "1211112122111111122222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "AP"
+ "Histogram bin count (%ld) exceeds maximum (%d)"
+ "arenaReturnPage"
+ "command %u in use but has no packet sequence (valid=%u)\n"
+ "command %u sequence list spans two requests (%p != %p)\n"
+ "deferring arena release during flush, queue length %u\n"
+ "for PG"
+ "for reset (postInit)"
+ "for reset (resetScaler)"
+ "iBoot"
+ "reclaimed %u PIODMA command(s), released %u MSR power ref(s), refCount now %u\n"
+ "reclaiming PIODMA command idx=%u tag=%u transformId=%d powerRefOutstanding=%d release=%d\n"
- "\"[%s] \" \"Failed to load MsrCPU firmware for PG\\n\" @%s:%d"
- "\"[%s] \" \"Failed to load MsrCPU firmware for reset\\n\" @%s:%d"
- "12111112122212121111111111122122112112112212222"
- "121111211111111222"
- "1211112111111112222"
- "121111211111111222222"
- "12111121111111122222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "Histogram bin count (%d) exceeds maximum (%d)"
- "command %d not valid!"
```
