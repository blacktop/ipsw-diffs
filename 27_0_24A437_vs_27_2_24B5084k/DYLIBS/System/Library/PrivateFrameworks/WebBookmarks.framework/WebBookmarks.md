## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-625.1.29.10.29
-  __TEXT.__text: 0xe9ce8
-  __TEXT.__objc_methlist: 0x8b80
+625.2.4.1.0
+  __TEXT.__text: 0xea188
+  __TEXT.__objc_methlist: 0x8bb0
   __TEXT.__const: 0x2048
-  __TEXT.__gcc_except_tab: 0xc370
-  __TEXT.__cstring: 0x10160
+  __TEXT.__gcc_except_tab: 0xc3e0
+  __TEXT.__cstring: 0x10210
   __TEXT.__oslogstring: 0xb38c
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0xadc

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_assocty: 0xa0
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x69c0
+  __TEXT.__unwind_info: 0x69f0
   __TEXT.__eh_frame: 0x3d68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5130
+  __DATA_CONST.__objc_selrefs: 0x5140
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x370
   __DATA_CONST.__got: 0xa20
   __AUTH_CONST.__const: 0x2be8
-  __AUTH_CONST.__cfstring: 0x6500
+  __AUTH_CONST.__cfstring: 0x6540
   __AUTH_CONST.__objc_const: 0xa828
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x3c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4938
-  Symbols:   8590
-  CStrings:  2188
+  Functions: 4943
+  Symbols:   8598
+  CStrings:  2190
 
Symbols:
+ -[WBTabCollection localTabGroupWithUUID:]
+ -[WBTabGroupManager localTabGroupWithUUID:]
+ -[WBWindowState initWithUUID:localTabGroup:sceneID:]
+ -[WebBookmarkTabCollection _localTabGroupWithUUID:]
+ GCC_except_table136
+ GCC_except_table276
+ ___41-[WBTabCollection localTabGroupWithUUID:]_block_invoke
+ _objc_msgSend$_localTabGroupWithUUID:
CStrings:
+ "Failed to check whether tab group %d is claimed by an open window"
+ "SELECT 1 FROM windows WHERE date_closed IS NULL AND (local_tab_group_id = %d OR private_tab_group_id = %d)"
```
