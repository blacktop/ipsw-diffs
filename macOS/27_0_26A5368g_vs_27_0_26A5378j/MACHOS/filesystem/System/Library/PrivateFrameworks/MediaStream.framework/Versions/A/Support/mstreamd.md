## mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Versions/A/Support/mstreamd`

```diff

-  __TEXT.__text: 0xba3c
+  __TEXT.__text: 0xbd54
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0x1f20
+  __TEXT.__objc_stubs: 0x1f40
   __TEXT.__objc_methlist: 0xab4
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__objc_methname: 0x3218
+  __TEXT.__objc_methname: 0x32dd
   __TEXT.__oslogstring: 0xc49
   __TEXT.__objc_classname: 0x13a
   __TEXT.__objc_methtype: 0xfc9
   __TEXT.__cstring: 0x4b3
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__unwind_info: 0x250
   __DATA_CONST.__const: 0x440
   __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x20

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0x578
+  __DATA_CONST.__got: 0x598
   __DATA.__objc_const: 0xb90
-  __DATA.__objc_selrefs: 0xbe0
+  __DATA.__objc_selrefs: 0xbe8
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/MediaStream.framework/Versions/A/MediaStream
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 185
-  Symbols:   244
-  CStrings:  676
+  Functions: 186
+  Symbols:   248
+  CStrings:  677
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _kMSASClientVersionKey
+ _kMSASDestinationAssetCountKey
+ _kMSASModelRefreshContentOfAlbumWithGUIDWithCompletionFn
+ _kMSASSourceAssetCountKey
Functions:
~ sub_1000080fc : 11524 -> 12176
+ sub_10000c4b0
CStrings:
+ "cancelMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:"
+ "completeMigrationToCPLForAlbumWithGUID:personID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:"
+ "failMigrationToCPLForAlbumWithGUID:migrationError:personID:clientVersion:completionBlock:"
+ "initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:"
+ "refreshContentOfAlbumWithGUID:resetSync:personID:info:completionBlock:"
+ "unarchiveMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:"
- "cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:"
- "completeMigrationToCPLForAlbumWithGUID:personID:completionBlock:"
- "failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:"
- "initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:completionBlock:"
- "unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:"

```
