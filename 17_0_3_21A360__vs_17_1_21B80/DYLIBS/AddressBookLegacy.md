## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12691.1.0.0.0
-  __TEXT.__text: 0x6d94c
+12695.0.0.0.0
+  __TEXT.__text: 0x6ddfc
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x2c70
+  __TEXT.__objc_methlist: 0x2c78
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x230ca
-  __TEXT.__oslogstring: 0x184c
+  __TEXT.__cstring: 0x23109
+  __TEXT.__oslogstring: 0x1a74
   __TEXT.__gcc_except_tab: 0x560
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x1764
+  __TEXT.__unwind_info: 0x1774
   __TEXT.__objc_classname: 0x4bc
-  __TEXT.__objc_methname: 0x8c53
+  __TEXT.__objc_methname: 0x8c7d
   __TEXT.__objc_methtype: 0x13e0
   __TEXT.__objc_stubs: 0x77a0
   __DATA_CONST.__got: 0x1e8

   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x36d8
-  __DATA_CONST.__objc_selrefs: 0x2308
+  __DATA_CONST.__objc_selrefs: 0x2310
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0xcd80
+  __AUTH_CONST.__cfstring: 0xcda0
   __AUTH_CONST.__const: 0xdd0
   __AUTH_CONST.__objc_const: 0x1338
   __AUTH_CONST.__objc_doubleobj: 0x60

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2B18BFAB-A403-3DA4-91CD-19ED1D412702
-  Functions: 2307
-  Symbols:   6609
-  CStrings:  5710
+  UUID: 90493ABA-E2DB-3E8D-B34D-0061FCF4FE2F
+  Functions: 2308
+  Symbols:   6611
+  CStrings:  5720
 
Symbols:
+ +[ABSQLPredicate predicateForContactsWithWallpaperMetadata]
+ ___ABAddressBookPersonBufferRowHandler_block_invoke.510
- ___ABAddressBookPersonBufferRowHandler_block_invoke_3
CStrings:
+ "ABBufferQueryCursor (%p) AppendImageData, reading %d from recordID %d into buffer (%p), [%lu]"
+ "ABBufferQueryCursor (%p) AppendPropertyBlobData, SQLITE_MISUSE opening blob %s from recordID %d"
+ "ABBufferQueryCursor (%p) AppendPropertyBlobData, reading %s from recordID %d into buffer (%p), [%lu + %lu = %lu]"
+ "ABBufferQueryCursor (%p) created buffer (%p)"
+ "ABBufferQueryCursor (%p) dealloc, releasing buffer (%p) [%lu]"
+ "ABBufferQueryCursor (%p) fetchNextBatchWithReply, releasing buffer (%p) [%lu]"
+ "ABBufferQueryCursor (%p), re-created buffer (%p) [previous %lu]"
+ "SELECT rowid FROM ABPerson WHERE WallpaperMetadata is NOT NULL"
+ "predicateForContactsWithWallpaperMetadata"

```
