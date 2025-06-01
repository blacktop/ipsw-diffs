## usermanagerd

> `/usr/libexec/usermanagerd`

```diff

-384.60.3.0.0
-  __TEXT.__text: 0xa8764
-  __TEXT.__auth_stubs: 0x1890
+384.100.10.0.0
+  __TEXT.__text: 0xa8aac
+  __TEXT.__auth_stubs: 0x1870
   __TEXT.__objc_stubs: 0x2160
   __TEXT.__objc_methlist: 0x1068
-  __TEXT.__const: 0xfb4
+  __TEXT.__const: 0xfc4
   __TEXT.__gcc_except_tab: 0xc0c
-  __TEXT.__cstring: 0x5cd3
+  __TEXT.__cstring: 0x5d28
   __TEXT.__objc_classname: 0x398
-  __TEXT.__objc_methname: 0x335b
+  __TEXT.__objc_methname: 0x336f
   __TEXT.__objc_methtype: 0x127a
-  __TEXT.__oslogstring: 0x100aa
-  __TEXT.__unwind_info: 0x130c
-  __DATA_CONST.__auth_got: 0xc58
+  __TEXT.__oslogstring: 0x10224
+  __TEXT.__unwind_info: 0x12f8
+  __DATA_CONST.__auth_got: 0xc48
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x50
   __DATA_CONST.__const: 0x3098

   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x5600
   __DATA.__objc_selrefs: 0xbb0
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x1a0
-  __DATA.__objc_superrefs: 0x90
   __DATA.__objc_ivar: 0x1d8
   __DATA.__objc_data: 0xa00
   __DATA.__data: 0x10d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 43D694F0-5D71-3BF9-A644-00C3A8E94033
-  Functions: 1673
-  Symbols:   462
-  CStrings:  3249
+  UUID: 01BBBCD2-99B8-32D7-B4E3-1BBCFE169AD2
+  Functions: 1658
+  Symbols:   460
+  CStrings:  3262
 
Symbols:
+ _calloc
+ _malloc
- _cccurve25519_make_key_pair
- _ccder_encode_body
- _ccder_encode_tl
- _cced25519_make_key_pair
CStrings:
+ "/exclave"
+ "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
+ "Skipping the registration of the exclaves writable storage\n"
+ "T@\"NSString\",?,R,C"
+ "failed to change ownership on %s (%s)\n"
+ "failed to create path %s (%s)\n"
+ "failed to get exclaves status: %d\n"
+ "failed to get the homeDirPath\n"
+ "failed to register the exclaves writable storage path %s (%s)\n"
+ "failed to register the exclaves writable storage: %d\n"
+ "failed to stat path %s (%s)\n"
+ "invalid exclaves status: %d\n"
+ "kern.exclaves_status"
+ "successfully registered the exclaves writable storage at %s\n"
- "AssertMacros: %s, %s file: %s, line: %d, value: %ld\n"

```
