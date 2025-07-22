## audioclocksyncd

> `/usr/libexec/audioclocksyncd`

```diff

-1400.58.0.0.0
-  __TEXT.__text: 0x30988
-  __TEXT.__auth_stubs: 0x930
+1400.60.0.0.0
+  __TEXT.__text: 0x30c34
+  __TEXT.__auth_stubs: 0x940
   __TEXT.__objc_stubs: 0x4ca0
   __TEXT.__objc_methlist: 0x3028
   __TEXT.__const: 0x170
-  __TEXT.__oslogstring: 0x3660
+  __TEXT.__oslogstring: 0x3716
   __TEXT.__cstring: 0x273a
-  __TEXT.__gcc_except_tab: 0x11ac
+  __TEXT.__gcc_except_tab: 0x11c4
   __TEXT.__objc_methname: 0x81d0
   __TEXT.__objc_classname: 0x45c
   __TEXT.__objc_methtype: 0x14fc
-  __TEXT.__unwind_info: 0xc90
-  __DATA_CONST.__auth_got: 0x4b0
+  __TEXT.__unwind_info: 0xca0
+  __DATA_CONST.__auth_got: 0x4b8
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0xc78
   __DATA_CONST.__cfstring: 0x23c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FDAF3A24-E64E-33FF-AC9A-5BE0948D8036
-  Functions: 1271
-  Symbols:   202
-  CStrings:  2400
+  UUID: 975A8D42-3F14-303C-AC1E-9816B190D958
+  Functions: 1274
+  Symbols:   203
+  CStrings:  2403
 
Symbols:
+ _pthread_cond_timedwait
CStrings:
+ "1400.60"
+ "Error waiting for sync session to start: 0x%x"
+ "Failed to read current time for CLOCK_REALTIME\n"
+ "Monitor thread: error waiting for sync session to exit: %i, sync thread state: %hhu\n"
+ "Monitor thread: requesting external sync session to stop\n"
- "1400.58"
- "Unexpected error waiting for sync session to start: %i"

```
