## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-4026.100.72.0.0
-  __TEXT.__text: 0x3b4984
+4026.110.81.1.0
+  __TEXT.__text: 0x3b4abc
   __TEXT.__objc_methlist: 0xe714
   __TEXT.__const: 0x25d4c
   __TEXT.__dlopen_cstrs: 0x2d1
-  __TEXT.__gcc_except_tab: 0x144ec
-  __TEXT.__cstring: 0x74db0
-  __TEXT.__oslogstring: 0x1d65c
+  __TEXT.__gcc_except_tab: 0x14518
+  __TEXT.__cstring: 0x74dd1
+  __TEXT.__oslogstring: 0x1d678
   __TEXT.__ustring: 0x210
   __TEXT.__unwind_info: 0x72e8
   __TEXT.__eh_frame: 0x50

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9dc8
+  __DATA_CONST.__const: 0x9de8
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arraydata: 0x1418
   __DATA_CONST.__got: 0xb38
   __AUTH_CONST.__const: 0x19420
-  __AUTH_CONST.__cfstring: 0x28700
+  __AUTH_CONST.__cfstring: 0x28760
   __AUTH_CONST.__objc_const: 0x159f0
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x22c8

   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0xff0
-  __AUTH.__objc_data: 0x3070
+  __AUTH.__objc_data: 0x19f0
   __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0xf2c
   __DATA.__data: 0x1708
   __DATA.__bss: 0xe40
   __DATA.__common: 0xb20
-  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA_DIRTY.__objc_data: 0x2c60
   __DATA_DIRTY.__data: 0x80
-  __DATA_DIRTY.__bss: 0x10d0
+  __DATA_DIRTY.__bss: 0x10e0
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libz.1.dylib
   Functions: 8472
   Symbols:   17476
-  CStrings:  7527
+  CStrings:  7530
 
Functions:
~ __ZNK23ML3MatchAlbumImportItem15getIntegerValueEj : 632 -> 660
~ __ZNK28ML3ProtoSyncArtistImportItem8hasValueEj : 1124 -> 1156
~ __ZNK28ML3ProtoSyncArtistImportItem15getIntegerValueEj : 584 -> 600
~ __ZN16ML3ImportSession9_addAlbumENSt3__110shared_ptrI13ML3ImportItemEEP26ML3AlbumGroupingIdentifierxS3_ : 20004 -> 20084
~ __ZN16ML3ImportSession15_addAlbumArtistENSt3__110shared_ptrI13ML3ImportItemEEP6NSDataS3_ : 10252 -> 10408
CStrings:
+ "Disliked"
+ "Liked"
+ "Setting albumArtistLikedState=%{public}@ (oldValue=%{public}@)"
+ "Setting albumLikedState=%{public}@ (oldValue=%{public}@)"
+ "Unrecognized(%ld)"
- "Setting albumArtistLikedState=%d (oldValue=%d)"
- "Setting albumLikedState=%lld (oldValue=%lld)"
```
