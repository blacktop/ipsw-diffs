## clocksyncd

> `/usr/libexec/clocksyncd`

```diff

-  __TEXT.__text: 0x3af9c
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0x59c0
-  __TEXT.__objc_methlist: 0x36b4
+  __TEXT.__text: 0x3b254
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_stubs: 0x59e0
+  __TEXT.__objc_methlist: 0x36c4
   __TEXT.__const: 0x129
   __TEXT.__cstring: 0x27e0
-  __TEXT.__oslogstring: 0x57e9
-  __TEXT.__gcc_except_tab: 0x1ac0
-  __TEXT.__objc_methname: 0x917d
+  __TEXT.__oslogstring: 0x5923
+  __TEXT.__gcc_except_tab: 0x1ae8
+  __TEXT.__objc_methname: 0x91c9
   __TEXT.__objc_classname: 0x508
   __TEXT.__objc_methtype: 0x197a
-  __TEXT.__unwind_info: 0xe80
+  __TEXT.__unwind_info: 0xe88
   __DATA_CONST.__const: 0x948
   __DATA_CONST.__cfstring: 0x1ee0
   __DATA_CONST.__objc_classlist: 0x168

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x6b8
-  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x110
-  __DATA.__objc_const: 0x6a28
-  __DATA.__objc_selrefs: 0x1d90
-  __DATA.__objc_ivar: 0x514
+  __DATA.__objc_const: 0x6a68
+  __DATA.__objc_selrefs: 0x1d98
+  __DATA.__objc_ivar: 0x51c
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x141

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1531
-  Symbols:   282
-  CStrings:  2715
+  Functions: 1529
+  Symbols:   281
+  CStrings:  2722
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
- _mach_get_times
CStrings:
+ "1501.4"
+ "Dropping stale trigger timing for triggerId %u: GTB %llu < threshold %llu\n"
+ "GTB/MCT offset changed (%llu -> %llu) — clearing trigger timing buffer before read\n"
+ "GTB/MCT offset changed mid-fetch (%llu -> %llu) — buffer entries are mixed; resetting\n"
+ "Nominal sync period: (%llu/%llu), nominal syncs per poll: %llu, %@\n"
+ "Reset MSG trigger timings, cachedGtbMctOffset: %llu, postResetGtbThreshold: %llu\n"
+ "Reset trigger timings: re-register failed for triggerId %u: 0x%x\n"
+ "Reset trigger timings: unregister failed for triggerId %u: 0x%x\n"
+ "Trigger timestamp overflow: whole=%llu, offset=%llu\n"
+ "_cachedGtbMctOffset"
+ "_postResetGtbThreshold"
+ "_resetTriggerTimingBuffersLocked"
- "1501.1"
- "Failed to calculate MAT offset because MCT < MAT. MCT: %llu, MAT: %llu\n"
- "Failed to calculate MAT offset from MCT. Error: %i\n"
- "MAT/MCT offset greater than INT64_MAX. MCT: %llu, MAT: %llu\n"
- "Nominal sync period: (%llu/%llu), nominal syncs per poll: %llu, %@, matOffset: %lli\n"

```
