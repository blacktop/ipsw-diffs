## MediaStream

> `/System/Library/PrivateFrameworks/MediaStream.framework/Versions/A/MediaStream`

```diff

-  __TEXT.__text: 0x16184
-  __TEXT.__objc_methlist: 0x194c
+  __TEXT.__text: 0x166fc
+  __TEXT.__objc_methlist: 0x1954
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x110
   __TEXT.__oslogstring: 0x172c
   __TEXT.__cstring: 0x118d
   __TEXT.__ustring: 0x74
-  __TEXT.__unwind_info: 0x7c0
+  __TEXT.__unwind_info: 0x7d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0xf40
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__got: 0x5a8
   __AUTH_CONST.__const: 0xa90
   __AUTH_CONST.__cfstring: 0xf20
-  __AUTH_CONST.__objc_const: 0x21f0
+  __AUTH_CONST.__objc_const: 0x21e8
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x150
   __DATA.__data: 0x300

   - /System/Library/PrivateFrameworks/CoreMediaStream.framework/Versions/A/CoreMediaStream
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 626
-  Symbols:   1620
+  Functions: 628
+  Symbols:   1626
   CStrings:  377
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[MSASConnection cancelMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]
+ -[MSASConnection completeMigrationToCPLForAlbumWithGUID:personID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]
+ -[MSASConnection failMigrationToCPLForAlbumWithGUID:migrationError:personID:clientVersion:completionBlock:]
+ -[MSASConnection initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]
+ -[MSASConnection refreshContentOfAlbumWithGUID:resetSync:personID:completionBlock:]
+ -[MSASConnection unarchiveMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]
+ GCC_except_table450
+ GCC_except_table456
+ GCC_except_table462
+ GCC_except_table467
+ GCC_except_table472
+ GCC_except_table536
+ GCC_except_table585
+ ___107-[MSASConnection failMigrationToCPLForAlbumWithGUID:migrationError:personID:clientVersion:completionBlock:]_block_invoke
+ ___131-[MSASConnection initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke
+ ___135-[MSASConnection completeMigrationToCPLForAlbumWithGUID:personID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]_block_invoke
+ ___83-[MSASConnection refreshContentOfAlbumWithGUID:resetSync:personID:completionBlock:]_block_invoke
+ ___94-[MSASConnection cancelMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]_block_invoke
+ ___97-[MSASConnection unarchiveMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]_block_invoke
+ _kMSASClientVersionKey
+ _kMSASDestinationAssetCountKey
+ _kMSASModelRefreshContentOfAlbumWithGUIDWithCompletionFn
+ _kMSASSourceAssetCountKey
- -[MSASConnection cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
- -[MSASConnection completeMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
- -[MSASConnection failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]
- -[MSASConnection initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:completionBlock:]
- -[MSASConnection unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
- GCC_except_table448
- GCC_except_table452
- GCC_except_table460
- GCC_except_table465
- GCC_except_table470
- GCC_except_table534
- GCC_except_table583
- ___100-[MSASConnection initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:completionBlock:]_block_invoke
- ___80-[MSASConnection cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___82-[MSASConnection completeMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___83-[MSASConnection unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___93-[MSASConnection failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]_block_invoke

```
