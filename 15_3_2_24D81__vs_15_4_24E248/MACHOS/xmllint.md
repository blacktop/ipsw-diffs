## xmllint

> `/usr/bin/xmllint`

```diff

-38.2.0.0.0
-  __TEXT.__text: 0x6ecc
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__cstring: 0x21fd
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x610
+38.9.0.0.0
+  __TEXT.__text: 0x6c68
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__cstring: 0x21e3
+  __TEXT.__unwind_info: 0x100
+  __DATA_CONST.__auth_got: 0x5d8
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__data: 0x310
   __DATA.__bss: 0xc6d0
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 8760FA2D-8064-3945-8347-C84E8DA81049
-  Functions: 57
-  Symbols:   203
-  CStrings:  403
+  UUID: 01AA8F5E-CFB1-3866-B831-81849B786D13
+  Functions: 52
+  Symbols:   196
+  CStrings:  401
 
Symbols:
- _xmlMemFree
- _xmlMemMalloc
- _xmlMemRealloc
- _xmlMemSetup
- _xmlMemSize
- _xmlMemUsed
- _xmlMemoryStrdup
CStrings:
+ "\t--maxmem nbbytes : limits memory allocation to nbbytes bytes [DEPRECATED]\n"
- "\t--maxmem nbbytes : limits memory allocation to nbbytes bytes\n"
- "-o"
- "Ran out of memory needs > %d bytes\n"

```
