## MediaStream

> `/System/Library/PrivateFrameworks/MediaStream.framework/MediaStream`

```diff

-  __TEXT.__text: 0x15710
-  __TEXT.__objc_methlist: 0x19c4
+  __TEXT.__text: 0x15be4
+  __TEXT.__objc_methlist: 0x19cc
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x110
   __TEXT.__oslogstring: 0x1881
   __TEXT.__cstring: 0x11f7
   __TEXT.__ustring: 0x74
-  __TEXT.__unwind_info: 0x788
+  __TEXT.__unwind_info: 0x7a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0xf90
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__got: 0x5b0
+  __DATA_CONST.__got: 0x5d0
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x22b0
+  __AUTH_CONST.__objc_const: 0x22a8
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x164
   __DATA.__data: 0x300
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 612
-  Symbols:   2272
+  Functions: 614
+  Symbols:   2280
   CStrings:  394
 
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
+ GCC_except_table446
+ GCC_except_table452
+ GCC_except_table457
+ GCC_except_table462
+ GCC_except_table522
+ GCC_except_table571
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
- GCC_except_table440
- GCC_except_table450
- GCC_except_table455
- GCC_except_table460
- GCC_except_table520
- GCC_except_table569
- ___100-[MSASConnection initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:completionBlock:]_block_invoke
- ___80-[MSASConnection cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___82-[MSASConnection completeMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___83-[MSASConnection unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___93-[MSASConnection failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]_block_invoke

```
