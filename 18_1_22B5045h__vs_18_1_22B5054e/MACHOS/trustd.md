## trustd

> `/usr/libexec/trustd`

```diff

-61439.40.45.0.1
-  __TEXT.__text: 0x5c02c
-  __TEXT.__auth_stubs: 0x2310
-  __TEXT.__objc_stubs: 0x2ae0
-  __TEXT.__objc_methlist: 0x918
+61439.40.54.0.0
+  __TEXT.__text: 0x5c4b4
+  __TEXT.__auth_stubs: 0x2320
+  __TEXT.__objc_stubs: 0x2b00
+  __TEXT.__objc_methlist: 0x920
   __TEXT.__const: 0x3c9a
-  __TEXT.__gcc_except_tab: 0xccc
-  __TEXT.__cstring: 0x64dd
-  __TEXT.__oslogstring: 0x56f9
+  __TEXT.__gcc_except_tab: 0xcec
+  __TEXT.__cstring: 0x65a4
+  __TEXT.__oslogstring: 0x5765
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methname: 0x2a66
+  __TEXT.__objc_methname: 0x2a89
   __TEXT.__objc_methtype: 0xab8
-  __TEXT.__unwind_info: 0x1020
-  __DATA_CONST.__auth_got: 0x1198
+  __TEXT.__unwind_info: 0x1030
+  __DATA_CONST.__auth_got: 0x11a0
   __DATA_CONST.__got: 0x708
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x48f0
-  __DATA_CONST.__cfstring: 0x5b20
+  __DATA_CONST.__const: 0x48f8
+  __DATA_CONST.__cfstring: 0x5b60
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x16e0
-  __DATA.__objc_selrefs: 0xb78
+  __DATA.__objc_selrefs: 0xb80
   __DATA.__objc_ivar: 0xa4
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x398

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1212
-  Symbols:   800
-  CStrings:  2087
+  Functions: 1215
+  Symbols:   801
+  CStrings:  2096
 
Symbols:
+ _clock_gettime
CStrings:
+ "writing asset path \"%!@(MISSING)\" (was \"%!@(MISSING)\")"
+ "retryReadSavedTrustStoreAssetPath result: %!@(MISSING)"
+ "%!s(MISSING) uptime: %!l(MISSING)lu, system: %!l(MISSING)lus"
+ "NO"
+ "Will not exit due to earlier error."
+ "Will exit when clean to use updated asset path."
+ "Will exit when clean to use downloaded asset."
+ "timed out attempting to read saved asset path"
+ "Will exit when clean to use newer asset version."
+ "retryReadSavedTrustStoreAssetPath:"
+ "Will exit trustd when all transactions are complete."
- "Will exit when clean to use updated asset"
- "Will exit when clean to use updated assets"

```
