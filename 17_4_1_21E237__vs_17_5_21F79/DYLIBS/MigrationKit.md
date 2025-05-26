## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-17.4.19.0.0
-  __TEXT.__text: 0x30900
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x353c
+17.120.4.0.0
+  __TEXT.__text: 0x313c8
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0x358c
   __TEXT.__const: 0x44c
-  __TEXT.__cstring: 0x3045
+  __TEXT.__cstring: 0x3073
   __TEXT.__oslogstring: 0x232f
-  __TEXT.__gcc_except_tab: 0xc24
-  __TEXT.__unwind_info: 0xcec
+  __TEXT.__gcc_except_tab: 0xc84
+  __TEXT.__unwind_info: 0xd1c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x813
-  __TEXT.__objc_methname: 0x70be
-  __TEXT.__objc_methtype: 0xf9e
-  __TEXT.__objc_stubs: 0x6f80
+  __TEXT.__objc_methname: 0x7156
+  __TEXT.__objc_methtype: 0xfd4
+  __TEXT.__objc_stubs: 0x7060
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x330

   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x6b98
-  __DATA_CONST.__objc_selrefs: 0x1e50
-  __DATA_CONST.__objc_classrefs: 0x510
+  __DATA_CONST.__objc_selrefs: 0x1e90
+  __DATA_CONST.__objc_classrefs: 0x518
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x480
   __AUTH_CONST.__objc_intobj: 0xc18
-  __AUTH_CONST.__cfstring: 0x4600
+  __AUTH_CONST.__cfstring: 0x4620
   __AUTH_CONST.__objc_const: 0x1f68
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__auth_got: 0x630
   __AUTH.__objc_data: 0x1f90
   __DATA.__objc_ivar: 0x594
   __DATA.__data: 0x540

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1352
-  Symbols:   5252
-  CStrings:  2677
+  Functions: 1364
+  Symbols:   5285
+  CStrings:  2690
 
Symbols:
+ -[MKApplicationMigrator importAndWait]
+ -[MKMigrator importAndWait]
+ -[MKPhotoLibraryAlbumMigrator importAndWait]
+ -[MKPhotoLibraryAlbumMigrator initWithReuseDatabase:]
+ -[MKPhotoLibraryAssetDatabase create:]
+ -[MKPhotoLibraryAssetDatabase initWithType:reuse:]
+ -[MKPhotoLibraryAssetDatabase initWithType:reuse:].cold.1
+ -[MKPhotoLibraryAssetDatabase initWithType:reuse:].cold.2
+ -[MKPhotoLibraryAssetDatabase open:reuse:]
+ -[MKPhotoLibraryAssetDatabase open:reuse:].cold.1
+ -[MKPhotoLibraryAssetDatabase removeCollection:]
+ -[MKPhotoLibraryAssetDatabase removeCollection:].cold.1
+ -[MKPhotoLibraryAssetDatabase removeCollection:].cold.2
+ -[MKPhotoLibraryMigrator importAndWait]
+ -[MKPhotoLibraryMigrator importAssetAndWait:retryNeeded:]
+ -[MKPhotoLibraryMigrator importAssetAndWait:retryNeeded:].cold.1
+ -[MKPhotoLibraryMigrator initWithType:reuseDatabase:]
+ ___57-[MKPhotoLibraryMigrator importAssetAndWait:retryNeeded:]_block_invoke
+ ___block_descriptor_88_e8_32s40s48r56r64r72r80r_e36_v32?0B8B12"NSString"16"NSError"24ls32l8r48l8r56l8r64l8r72l8r80l8s40l8
+ _objc_msgSend$create:
+ _objc_msgSend$importAndWait
+ _objc_msgSend$importAssetAndWait:retryNeeded:
+ _objc_msgSend$initWithReuseDatabase:
+ _objc_msgSend$initWithType:reuse:
+ _objc_msgSend$initWithType:reuseDatabase:
+ _objc_msgSend$open:reuse:
+ _objc_msgSend$removeCollection:
+ _objc_opt_self
- -[MKApplicationMigrator install]
- -[MKPhotoLibraryAlbumMigrator import]
- -[MKPhotoLibraryAssetDatabase create]
- -[MKPhotoLibraryAssetDatabase initWithType:].cold.1
- -[MKPhotoLibraryAssetDatabase initWithType:].cold.2
- -[MKPhotoLibraryAssetDatabase open:]
- -[MKPhotoLibraryAssetDatabase open:].cold.1
- ___110-[MKPhotoLibraryMigrator import:identifier:offset:length:total:filename:collection:originalFilename:complete:]_block_invoke
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- _objc_msgSend$addToAssetQueue:
CStrings:
+ "@20@0:8B16"
+ "@28@0:8Q16B24"
+ "B32@0:8@16^B24"
+ "DELETE FROM identifiers WHERE collection = ?;"
+ "create:"
+ "importAndWait"
+ "importAssetAndWait:retryNeeded:"
+ "initWithReuseDatabase:"
+ "initWithType:reuse:"
+ "initWithType:reuseDatabase:"
+ "open:reuse:"
+ "removeCollection:"
+ "v28@0:8@16B24"

```
