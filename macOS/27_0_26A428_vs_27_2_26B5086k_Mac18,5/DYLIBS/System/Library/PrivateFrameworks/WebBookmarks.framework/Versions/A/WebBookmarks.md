## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/Versions/A/WebBookmarks`

```diff

-625.1.29.11.27
-  __TEXT.__text: 0xf4d08
-  __TEXT.__objc_methlist: 0x8b80
+625.2.4.1.0
+  __TEXT.__text: 0xf51f8
+  __TEXT.__objc_methlist: 0x8bb8
   __TEXT.__const: 0x2058
-  __TEXT.__gcc_except_tab: 0xc388
-  __TEXT.__cstring: 0xfb30
+  __TEXT.__gcc_except_tab: 0xc3f8
+  __TEXT.__cstring: 0xfbe0
   __TEXT.__oslogstring: 0xb9ec
   __TEXT.__dlopen_cstrs: 0x50
   __TEXT.__constg_swiftt: 0xadc

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_assocty: 0xa0
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x6ad8
+  __TEXT.__unwind_info: 0x6af8
   __TEXT.__eh_frame: 0x3d18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50d0
+  __DATA_CONST.__objc_selrefs: 0x50e0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__got: 0x9f0
   __AUTH_CONST.__const: 0x5668
-  __AUTH_CONST.__cfstring: 0x63e0
+  __AUTH_CONST.__cfstring: 0x6420
   __AUTH_CONST.__objc_const: 0xa610
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5001
-  Symbols:   8567
-  CStrings:  2173
+  Functions: 5006
+  Symbols:   8571
+  CStrings:  2175
 
Symbols:
+ -[WBTabCollection localTabGroupWithUUID:]
+ -[WBTabGroupManager localTabGroupWithUUID:]
+ -[WBWindowState initWithUUID:localTabGroup:sceneID:]
+ -[WebBookmarkTabCollection _localTabGroupWithUUID:]
+ GCC_except_table324
+ GCC_except_table332
+ GCC_except_table361
+ ___41-[WBTabCollection localTabGroupWithUUID:]_block_invoke
+ _objc_msgSend$_localTabGroupWithUUID:
- GCC_except_table128
- GCC_except_table329
- GCC_except_table330
- GCC_except_table344
- GCC_except_table364
CStrings:
+ "Failed to check whether tab group %d is claimed by an open window"
+ "SELECT 1 FROM windows WHERE date_closed IS NULL AND (local_tab_group_id = %d OR private_tab_group_id = %d)"
```
