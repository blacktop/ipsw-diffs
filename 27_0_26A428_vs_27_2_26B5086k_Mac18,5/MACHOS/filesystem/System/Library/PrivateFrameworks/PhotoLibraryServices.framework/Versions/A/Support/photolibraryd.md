## photolibraryd

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/Support/photolibraryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x21e70
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_stubs: 0x5e60
+916.41.100.0.0
+  __TEXT.__text: 0x21ff8
+  __TEXT.__auth_stubs: 0xa60
+  __TEXT.__objc_stubs: 0x5ea0
   __TEXT.__objc_methlist: 0x124c
   __TEXT.__dlopen_cstrs: 0xc5
   __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0xa54
+  __TEXT.__gcc_except_tab: 0xa84
   __TEXT.__objc_classname: 0x7c4
-  __TEXT.__objc_methname: 0x6b12
+  __TEXT.__objc_methname: 0x6b37
   __TEXT.__objc_methtype: 0xc18
-  __TEXT.__oslogstring: 0x45df
+  __TEXT.__oslogstring: 0x4661
   __TEXT.__cstring: 0x22b5
   __TEXT.metaschema: 0xc000
   __TEXT.__unwind_info: 0x850

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x538
+  __DATA_CONST.__auth_got: 0x540
   __DATA_CONST.__got: 0x818
   __DATA.__objc_const: 0x34c0
-  __DATA.__objc_selrefs: 0x19a0
+  __DATA.__objc_selrefs: 0x19b0
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0xf50
   __DATA.__data: 0x420

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 490
-  Symbols:   437
-  CStrings:  1586
+  Symbols:   438
+  CStrings:  1590
 
Symbols:
+ _PLPlatformVisualIntelligenceSyncSupported
Functions:
~ sub_100007a98 : 1504 -> 1888
~ sub_10000a45c -> sub_10000a5dc : 800 -> 808
CStrings:
+ "File Provider cache cleanup: removed empty directory %@"
+ "File Provider cache cleanup: removed empty domain root directory %@"
+ "Ignoring requested moment rebuild because moments not supported on platform"
+ "descriptionWithPath:"
+ "standardizedURL"
- "Ignoring requested moment rebuild because of outstanding transactions"
```
