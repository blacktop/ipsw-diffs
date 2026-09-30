## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

```diff

-2311.0.0.0.3
-  __TEXT.__text: 0x33518
+2313.40.1.0.1
+  __TEXT.__text: 0x33348
   __TEXT.__auth_stubs: 0xa20
-  __TEXT.__cstring: 0x678a
+  __TEXT.__cstring: 0x6643
   __TEXT.__const: 0x338
-  __TEXT.__oslogstring: 0x13c3
-  __TEXT.__unwind_info: 0x628
+  __TEXT.__oslogstring: 0x12b6
+  __TEXT.__unwind_info: 0x620
   __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x720
+  __DATA_CONST.__const: 0x6e0
   __DATA_CONST.__cfstring: 0xc80
   __DATA.__data: 0x98
   __DATA.__bss: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 550
+  Functions: 545
   Symbols:   187
-  CStrings:  788
+  CStrings:  777
 
CStrings:
+ "%!s(MISSING):%!d(MISSING): rdlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): unlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): wrlock == 0 failed %!d(MISSING)\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-read failed %!d(MISSING)\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-write failed %!d(MISSING)\n"
- "DONE: Suspending hint extents activity until next interval"
- "DONE: Suspending hint extents activity until next interval\n"
- "Failed to initialize dispatch queue for hint extents activity"
- "Failed to initialize dispatch queue for hint extents activity\n"
- "START: Initiating hint extents activity"
- "START: Initiating hint extents activity\n"
- "com.apple.filesystems.apfs_iosd.hint_extents"
- "com.apple.filesystems.apfs_iosd_hint_extents"
- "failed to set hint extents activity state to DONE"
- "failed to set hint extents activity state to DONE\n"
- "no volume supports iteration, unregistering activity"
- "no volume supports iteration, unregistering activity\n"

```
