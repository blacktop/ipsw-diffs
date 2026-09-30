## clocksyncd

> `/usr/libexec/clocksyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1501.4.0.0.0
-  __TEXT.__text: 0x3b254
+1501.5.0.0.0
+  __TEXT.__text: 0x3b028
   __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_stubs: 0x59e0
-  __TEXT.__objc_methlist: 0x36c4
+  __TEXT.__objc_methlist: 0x36b4
   __TEXT.__const: 0x129
   __TEXT.__cstring: 0x27e0
-  __TEXT.__oslogstring: 0x5923
-  __TEXT.__gcc_except_tab: 0x1ae8
-  __TEXT.__objc_methname: 0x91c9
+  __TEXT.__oslogstring: 0x5853
+  __TEXT.__gcc_except_tab: 0x1aa8
+  __TEXT.__objc_methname: 0x9192
   __TEXT.__objc_classname: 0x508
   __TEXT.__objc_methtype: 0x197a
-  __TEXT.__unwind_info: 0xe88
+  __TEXT.__unwind_info: 0xe78
   __DATA_CONST.__const: 0x948
   __DATA_CONST.__cfstring: 0x1ee0
   __DATA_CONST.__objc_classlist: 0x168

   __DATA_CONST.__auth_got: 0x6b0
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x110
-  __DATA.__objc_const: 0x6a68
+  __DATA.__objc_const: 0x6a28
   __DATA.__objc_selrefs: 0x1d98
-  __DATA.__objc_ivar: 0x51c
+  __DATA.__objc_ivar: 0x514
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x141

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1529
+  Functions: 1528
   Symbols:   281
-  CStrings:  2458
+  CStrings:  2453
 
CStrings:
+ "%@: Dropping future trigger timing at index %ld: %llu > current MCT %llu\n"
+ "1501.5"
+ "Dropping stale trigger timing for triggerId %u: converted time %llu is in the future (now %llu) — likely a pre-hibernation entry\n"
+ "GTB/MCT offset changed mid-fetch (%llu -> %llu)\n"
+ "removeObjectAtIndex:"
- "1501.4"
- "Dropping stale trigger timing for triggerId %u: GTB %llu < threshold %llu\n"
- "GTB/MCT offset changed (%llu -> %llu) — clearing trigger timing buffer before read\n"
- "GTB/MCT offset changed mid-fetch (%llu -> %llu) — buffer entries are mixed; resetting\n"
- "Reset MSG trigger timings, cachedGtbMctOffset: %llu, postResetGtbThreshold: %llu\n"
- "Reset trigger timings: re-register failed for triggerId %u: 0x%x\n"
- "Reset trigger timings: unregister failed for triggerId %u: 0x%x\n"
- "_cachedGtbMctOffset"
- "_postResetGtbThreshold"
- "_resetTriggerTimingBuffersLocked"
```
