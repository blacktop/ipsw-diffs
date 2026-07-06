## fseventsd

> `/usr/libexec/fseventsd`

```diff

-  __TEXT.__text: 0x16ce0
+  __TEXT.__text: 0x16edc
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__cstring: 0xee0
+  __TEXT.__cstring: 0xf1d
   __TEXT.__const: 0x168
   __TEXT.__oslogstring: 0x326a
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__unwind_info: 0x368
   __DATA_CONST.__const: 0x318
   __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__auth_got: 0x6e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 392
+  Functions: 393
   Symbols:   247
-  CStrings:  508
+  CStrings:  511
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
Symbols:
+ _basename_r
- _basename
CStrings:
+ "bname != NULL && bname_size > 0"
+ "com.apple.fseventsd.%s.%d.%s"
+ "nameForPID"
+ "system.unknown"
- "com.apple.fseventsd.%s.%d"

```
