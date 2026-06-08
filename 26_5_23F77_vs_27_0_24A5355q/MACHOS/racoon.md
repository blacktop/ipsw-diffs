## racoon

> `/usr/sbin/racoon`

```diff

-1125.0.0.0.0
-  __TEXT.__text: 0x66298
+1129.0.0.0.0
+  __TEXT.__text: 0x62ab0
   __TEXT.__auth_stubs: 0x1060
   __TEXT.__const: 0x70ea
-  __TEXT.__oslogstring: 0xc44d
+  __TEXT.__oslogstring: 0xc479
   __TEXT.__cstring: 0x56dc
-  __TEXT.__unwind_info: 0xe90
+  __TEXT.__unwind_info: 0xe98
+  __DATA_CONST.__const: 0x23d0
+  __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__auth_got: 0x830
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x23d0
-  __DATA_CONST.__cfstring: 0x1e0
   __DATA.__data: 0x538
   __DATA.__bss: 0x3300
   __DATA.__common: 0x14f0

   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libipsec.A.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: D9C12FDF-19CE-34AC-9945-3B93B928863D
-  Functions: 2171
+  UUID: 354F45BA-E2A5-34CC-A946-D353E17AACB5
+  Functions: 2160
   Symbols:   302
-  CStrings:  2225
+  CStrings:  2226
 
CStrings:
+ "SecItemCopyMatching() failed, error %d %s.\n"

```
