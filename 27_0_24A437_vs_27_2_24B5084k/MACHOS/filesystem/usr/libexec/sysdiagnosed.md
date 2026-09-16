## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1598.0.6.0.0
-  __TEXT.__text: 0x5ff8c
+1598.40.4.0.0
+  __TEXT.__text: 0x60134
   __TEXT.__auth_stubs: 0x1700
-  __TEXT.__objc_stubs: 0x9400
-  __TEXT.__objc_methlist: 0x3f6c
-  __TEXT.__const: 0x1cc
-  __TEXT.__cstring: 0x10cc9
+  __TEXT.__objc_stubs: 0x9420
+  __TEXT.__objc_methlist: 0x3f74
+  __TEXT.__const: 0x1d4
+  __TEXT.__cstring: 0x10d32
   __TEXT.__objc_classname: 0x38b
   __TEXT.__objc_methtype: 0x183c
   __TEXT.__gcc_except_tab: 0xda8
-  __TEXT.__objc_methname: 0xa78d
+  __TEXT.__objc_methname: 0xa7b4
   __TEXT.__oslogstring: 0x8111
   __TEXT.__ustring: 0x4e8
-  __TEXT.__unwind_info: 0x1628
+  __TEXT.__unwind_info: 0x1630
   __DATA_CONST.__const: 0x13c0
-  __DATA_CONST.__cfstring: 0x11720
+  __DATA_CONST.__cfstring: 0x117c0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0x470
   __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_const: 0x53b8
-  __DATA.__objc_selrefs: 0x2a00
+  __DATA.__objc_selrefs: 0x2a08
   __DATA.__objc_ivar: 0x478
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x3a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1775
+  Functions: 1776
   Symbols:   505
-  CStrings:  4866
+  CStrings:  4872
 
Functions:
~ sub_100011fd4 : 1048 -> 1076
+ sub_1000165b4
CStrings:
+ "/private/var/db/com.apple.countryd/countryCodeCache.plist"
+ "/private/var/mobile/Library/SecureElementService/Ledger"
+ "Country"
+ "_copySecureElementServiceLogsContainer"
+ "defaultContactlessApp.log"
+ "endpoint.log"
+ "logs/Country"
- "/private/var/mobile/Library/SecureElementService/Ledger/endpoint.log"
```
