## security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

```diff

-61901.60.29.0.0
-  __TEXT.__text: 0x37d8
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x500
+61901.60.37.0.0
+  __TEXT.__text: 0x3c98
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0xd0
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x18c
+  __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__objc_classname: 0x3d
-  __TEXT.__objc_methname: 0x3f8
+  __TEXT.__objc_methname: 0x411
   __TEXT.__objc_methtype: 0x17e
-  __TEXT.__cstring: 0xd62
+  __TEXT.__cstring: 0xea7
   __TEXT.__oslogstring: 0xa8
-  __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x3f8
+  __TEXT.__unwind_info: 0x100
+  __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x310
-  __DATA_CONST.__cfstring: 0xa60
+  __DATA_CONST.__cfstring: 0xc80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x190
-  __DATA.__objc_selrefs: 0x188
+  __DATA.__objc_selrefs: 0x190
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60
   __DATA.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0049FAAB-AFAE-30B7-A825-03E127399D4A
-  Functions: 32
-  Symbols:   172
-  CStrings:  274
+  UUID: 78FEA35F-1396-386B-BA4F-6B2E66333AAB
+  Functions: 34
+  Symbols:   175
+  CStrings:  309
 
Symbols:
+ ___error
+ _objc_retain_x1
+ _stat
CStrings:
+ "\n Keychain Database File Size Information \n"
+ "\n%@:\n"
+ "\nTotal Size (all files): %@ (%lld bytes)\n"
+ "  Block Size: %d bytes\n"
+ "  Blocks Allocated: %lld\n"
+ "  File Size: %@ (%lld bytes)\n"
+ "  Path: %@\n"
+ "  Status: File not found or inaccessible (errno: %d)\n"
+ "%.2f GB"
+ "%.2f KB"
+ "%.2f MB"
+ "%lld bytes"
+ "-shm"
+ "-wal"
+ "Main Database"
+ "Shared Memory File"
+ "WAL File"
+ "stringByAppendingString:"

```
