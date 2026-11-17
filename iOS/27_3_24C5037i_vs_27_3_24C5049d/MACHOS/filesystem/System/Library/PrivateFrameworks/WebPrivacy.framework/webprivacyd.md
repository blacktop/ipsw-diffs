## webprivacyd

> `/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_selrefs`

```diff

-62.0.0.0.0
-  __TEXT.__text: 0x14384
+63.0.0.0.0
+  __TEXT.__text: 0x1441c
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_stubs: 0xa20
   __TEXT.__const: 0x250
-  __TEXT.__gcc_except_tab: 0x192c
-  __TEXT.__cstring: 0x6e2
+  __TEXT.__gcc_except_tab: 0x1930
+  __TEXT.__cstring: 0x6fe
   __TEXT.__oslogstring: 0xf53
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__objc_methname: 0x684
   __TEXT.__unwind_info: 0xc90
   __DATA_CONST.__const: 0xb80
-  __DATA_CONST.__cfstring: 0x720
+  __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x538

   - /usr/lib/libobjc.A.dylib
   Functions: 524
   Symbols:   979
-  CStrings:  259
+  CStrings:  260
 
Functions:
~ __ZN10WebPrivacy3XPCL6decodeEPU24objcproto13OS_xpc_object8NSObjectRN7Backend10RemoteListEm : 232 -> 280
~ __ZN7Backend6Server15handleGetStatusEPU24objcproto13OS_xpc_object8NSObject : 796 -> 808
~ __ZN7Backend6ServerC2Ev : 604 -> 640
~ __ZN7Backend6Server25initializeDatabaseManagerERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_10RemoteListE : 828 -> 864
~ ____ZN7Backend6Server10initializeEv_block_invoke : 1876 -> 1892
~ __ZN7Backend6Server18unlinkAllDatabasesEONSt3__18functionIFvvEEE : 568 -> 572
CStrings:
+ "DEFAULT_TRACKER_BLOCK_RULES"
```
