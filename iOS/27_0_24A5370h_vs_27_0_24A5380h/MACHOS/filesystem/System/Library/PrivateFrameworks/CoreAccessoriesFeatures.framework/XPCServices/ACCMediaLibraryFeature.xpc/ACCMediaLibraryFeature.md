## ACCMediaLibraryFeature

> `/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCMediaLibraryFeature.xpc/ACCMediaLibraryFeature`

```diff

-  __TEXT.__text: 0x2a410
+  __TEXT.__text: 0x2a520
   __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_stubs: 0x4100
   __TEXT.__objc_methlist: 0x2160
   __TEXT.__cstring: 0x16bc
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x564
+  __TEXT.__gcc_except_tab: 0x560
   __TEXT.__objc_methname: 0x5291
-  __TEXT.__oslogstring: 0x59c6
+  __TEXT.__oslogstring: 0x5a1b
   __TEXT.__objc_classname: 0x33c
   __TEXT.__objc_methtype: 0xe7d
   __TEXT.__ustring: 0xa

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__got: 0x260
   __DATA.__objc_const: 0x3e10
   __DATA.__objc_selrefs: 0x1348
   __DATA.__objc_ivar: 0x278

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 859
-  Symbols:   6337
-  CStrings:  1681
+  Symbols:   6338
+  CStrings:  1682
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ ___51-[ACCMediaLibraryShimInfo _sendRadioLibraryUpdates]_block_invoke : 236 -> 244
~ -[ACCMediaLibraryShimInfo dealloc] : 668 -> 656
~ -[ACCMediaLibraryShimInfo stopSendingMediaLibraryUpdates] : 372 -> 456
~ -[ACCMediaLibraryShimInfo confirmMediaLibraryUpdateLastRevision:updateCount:] : 244 -> 256
~ -[ACCMediaLibraryShim _updateSubscribedToAppleMusicStatus:] : 356 -> 336
~ ___74-[ACCMediaLibraryProvider confirmUpdate:library:lastRevision:updateCount:]_block_invoke : 1148 -> 1140
~ ___77-[ACCMediaLibraryProvider confirmPlaylistContentUpdate:library:lastRevision:]_block_invoke : 860 -> 856
~ -[ACCMediaLibraryAccessory confirmUpdates:revision:count:] : 616 -> 612
~ ___58-[ACCMediaLibraryAccessory confirmUpdates:revision:count:]_block_invoke : 1792 -> 2036
~ -[ACCMediaLibraryAccessory confirmPlaylistContentUpdates:revision:] : 436 -> 432
~ -[ACCMediaLibraryFeature confirmUpdate:library:lastRevision:updateCount:] : 184 -> 160
CStrings:
+ "confirmUpdates: %@, library %@, revision %@, drained %lu update(s), waitlist now %lu"

```
