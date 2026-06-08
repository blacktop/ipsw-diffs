## seputil

> `/usr/libexec/seputil`

```diff

-880.120.2.0.0
-  __TEXT.__text: 0x15a38
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__cstring: 0x6364
-  __TEXT.__const: 0xc34
+926.0.0.0.0
+  __TEXT.__text: 0x16370
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__cstring: 0x65af
+  __TEXT.__const: 0xd14
   __TEXT.__oslogstring: 0x6f
   __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__unwind_info: 0x4d8
-  __DATA_CONST.__auth_got: 0x548
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__unwind_info: 0x4f0
+  __DATA_CONST.__const: 0x1e0
+  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__auth_got: 0x550
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x180
-  __DATA_CONST.__cfstring: 0x100
   __DATA.__data: 0xc80
   __DATA.__common: 0xc
   __DATA.__bss: 0x8f5

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 08551A43-CEB7-315A-B2C3-4C334387A89F
-  Functions: 498
-  Symbols:   200
-  CStrings:  745
+  UUID: D38BCCE7-60EC-37F8-99E7-9704666AC8D5
+  Functions: 502
+  Symbols:   203
+  CStrings:  763
 
Symbols:
+ __NSConcreteStackBlock
+ _kIOMainPortDefault
+ _sscanf
CStrings:
+ "%2x"
+ "%s: Couldn't find property \"%s\"\n"
+ "%s: Incorrect %s entry value type\n"
+ "%s: Incorrect value size for %s property\n"
+ "%s: failed to show lynx epochs\n"
+ "%s: lynx get epochs returned 0x%x"
+ "%s: prop %s val 0x%x\n"
+ "Epoch %lu: 0x%x\n"
+ "WARNING: Chip ID 0x%x not specified as having TZ0 alignment requirements or not\n"
+ "WARNING: Unable to read chip_id, assuming SEP has TZ0 alignment requirement\n"
+ "WARNING: iBoot allocated an extremely high amount of ar0 memory!\n"
+ "WARNING: iBoot allocated an odd number of bytes for ar0 memory!\n"
+ "WARNING: iBoot did not allocate enough space for scheme2!\n"
+ "a:b:c:d:f:g:hkmno:pq:r:s:t:uv:wx:CDFQI:L:NO:PR:T:W:"
+ "chip-id"
+ "i24@?0^{?=Q{?=*Q}}8^B16"
+ "show-epochs"
+ "ucert-offset"
+ "ucert-size"
+ "ucont-offset"
+ "ucont-size"
- "\t\t--sleep                  Sleep the SEP NOW!\n"
- "%s: Sleep failed\n"
- "a:b:c:d:f:g:hkmno:pq:r:s:t:uv:wx:CDFQI:L:NO:PR:ST:W:"
- "sleep"

```
