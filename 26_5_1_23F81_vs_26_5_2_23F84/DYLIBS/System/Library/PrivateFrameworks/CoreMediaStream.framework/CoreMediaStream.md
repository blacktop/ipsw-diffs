## CoreMediaStream

> `/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream`

```diff

-  __TEXT.__text: 0xc7d00
+  __TEXT.__text: 0xc7d58
   __TEXT.__auth_stubs: 0xf40
   __TEXT.__objc_methlist: 0x74e8
   __TEXT.__const: 0x1eb
-  __TEXT.__cstring: 0xa004
+  __TEXT.__cstring: 0xa006
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__gcc_except_tab: 0x2f54
-  __TEXT.__oslogstring: 0xe918
+  __TEXT.__oslogstring: 0xe91a
   __TEXT.__unwind_info: 0x2e08
   __TEXT.__objc_classname: 0x813
-  __TEXT.__objc_methname: 0x12ac4
+  __TEXT.__objc_methname: 0x12af7
   __TEXT.__objc_methtype: 0x438d
-  __TEXT.__objc_stubs: 0xc940
+  __TEXT.__objc_stubs: 0xc980
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x22f8
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ee0
+  __DATA_CONST.__objc_selrefs: 0x3ef0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1c0
   __AUTH_CONST.__auth_got: 0x7b0
   __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x80e0
+  __AUTH_CONST.__cfstring: 0x8100
   __AUTH_CONST.__objc_const: 0x8768
   __AUTH_CONST.__objc_intobj: 0x30
   __DATA.__objc_ivar: 0x654

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 3280
-  Symbols:   10395
-  CStrings:  6294
+  Symbols:   10397
+  CStrings:  6298
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[MSAlbumSharingDaemon updateOwnerReputationScoreForAlbum:withAddress:]
+ _objc_msgSend$containsString:
+ _objc_msgSend$handleWithPhoneNumber:
+ _objc_msgSend$updateOwnerReputationScoreForAlbum:withAddress:
- -[MSAlbumSharingDaemon updateOwnerReputationScoreForAlbum:]
- _objc_msgSend$updateOwnerReputationScoreForAlbum:
Functions:
~ -[MSAlbumSharingDaemon updateOwnerReputationScoreForAlbum:] -> -[MSAlbumSharingDaemon updateOwnerReputationScoreForAlbum:withAddress:] : 472 -> 492
~ -[MSAlbumSharingDaemon addAlbum:] : 268 -> 304
~ -[MSASServerSideModel dbQueueSetAlbum:info:] : 1264 -> 1296
CStrings:
+ "%{public}@: Unexpected nil album owner address"
+ "containsString:"
+ "handleWithPhoneNumber:"
+ "updateOwnerReputationScoreForAlbum:withAddress:"
- "%{public}@: Unexpected nil album owner email"
- "updateOwnerReputationScoreForAlbum:"

```
