## assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0x1ae94
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_stubs: 0x5380
+916.40.110.0.0
+  __TEXT.__text: 0x1b004
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_stubs: 0x53c0
   __TEXT.__objc_methlist: 0xfe4
   __TEXT.__dlopen_cstrs: 0x11b
   __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x780
+  __TEXT.__gcc_except_tab: 0x7b0
   __TEXT.__objc_classname: 0x74e
-  __TEXT.__objc_methname: 0x5fc3
+  __TEXT.__objc_methname: 0x5fe8
   __TEXT.__objc_methtype: 0xa06
-  __TEXT.__oslogstring: 0x46bb
+  __TEXT.__oslogstring: 0x473d
   __TEXT.__cstring: 0x1a89
   __TEXT.__unwind_info: 0x708
   __DATA_CONST.__const: 0xfd8

   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__auth_got: 0x5f0
+  __DATA_CONST.__auth_got: 0x5f8
   __DATA_CONST.__got: 0x790
   __DATA.__objc_const: 0x3120
-  __DATA.__objc_selrefs: 0x16c0
+  __DATA.__objc_selrefs: 0x16d0
   __DATA.__objc_ivar: 0xa8
   __DATA.__objc_data: 0xeb0
   __DATA.__data: 0x360

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 402
-  Symbols:   442
-  CStrings:  1398
+  Symbols:   443
+  CStrings:  1402
 
Symbols:
+ _PLPlatformVisualIntelligenceSyncSupported
Functions:
~ sub_100008aac : 1448 -> 1808
~ sub_10000b130 -> sub_10000b298 : 732 -> 740
CStrings:
+ "File Provider cache cleanup: removed empty directory %@"
+ "File Provider cache cleanup: removed empty domain root directory %@"
+ "Ignoring requested moment rebuild because moments not supported on platform"
+ "descriptionWithPath:"
+ "standardizedURL"
- "Ignoring requested moment rebuild because of outstanding transactions"
```
