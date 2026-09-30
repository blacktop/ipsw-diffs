## racoon

> `/usr/sbin/racoon`

```diff

-  __TEXT.__text: 0x62eec
+  __TEXT.__text: 0x62f28
   __TEXT.__auth_stubs: 0x1060
   __TEXT.__const: 0x70ea
   __TEXT.__oslogstring: 0xc479
-  __TEXT.__cstring: 0x56dc
-  __TEXT.__unwind_info: 0xe98
+  __TEXT.__cstring: 0x56fa
+  __TEXT.__unwind_info: 0xe90
   __DATA_CONST.__const: 0x23d0
   __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__auth_got: 0x830
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__data: 0x538
-  __DATA.__bss: 0x3300
+  __DATA.__bss: 0x3308
   __DATA.__common: 0x14f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libipsec.A.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 2160
+  Functions: 2161
   Symbols:   302
-  CStrings:  2226
+  CStrings:  2227
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
CStrings:
+ "bad length in yy_scan_bytes()"

```
