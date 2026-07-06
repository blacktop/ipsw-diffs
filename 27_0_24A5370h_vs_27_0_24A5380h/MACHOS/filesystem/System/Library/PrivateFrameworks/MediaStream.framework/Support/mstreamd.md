## mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd`

```diff

-  __TEXT.__text: 0xbdec
+  __TEXT.__text: 0xc0d0
   __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_stubs: 0x2220
+  __TEXT.__objc_stubs: 0x2240
   __TEXT.__objc_methlist: 0xb04
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__objc_methname: 0x348d
+  __TEXT.__objc_methname: 0x3552
   __TEXT.__oslogstring: 0xe67
   __TEXT.__cstring: 0x596
   __TEXT.__objc_classname: 0x13a

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__got: 0x5c0
   __DATA.__objc_const: 0xb90
-  __DATA.__objc_selrefs: 0xca0
+  __DATA.__objc_selrefs: 0xca8
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x3c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 186
-  Symbols:   280
-  CStrings:  723
+  Functions: 187
+  Symbols:   284
+  CStrings:  724
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
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
~ sub_100008954 : 11176 -> 11780
+ sub_10000ca28
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
