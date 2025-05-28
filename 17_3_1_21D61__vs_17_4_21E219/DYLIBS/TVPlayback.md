## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-529.20.11.0.0
-  __TEXT.__text: 0x616e4
+529.40.22.0.0
+  __TEXT.__text: 0x61824
   __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x51ec
+  __TEXT.__objc_methlist: 0x5204
   __TEXT.__const: 0x1e4
-  __TEXT.__cstring: 0x640c
+  __TEXT.__cstring: 0x642f
   __TEXT.__oslogstring: 0x5b81
   __TEXT.__gcc_except_tab: 0x158c
-  __TEXT.__unwind_info: 0x1598
+  __TEXT.__unwind_info: 0x159c
   __TEXT.__objc_classname: 0x7c7
-  __TEXT.__objc_methname: 0x127f4
-  __TEXT.__objc_methtype: 0x22bd
+  __TEXT.__objc_methname: 0x12916
+  __TEXT.__objc_methtype: 0x2329
   __TEXT.__objc_stubs: 0xb040
   __DATA_CONST.__got: 0x490
   __DATA_CONST.__const: 0x2390

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8f88
-  __DATA_CONST.__objc_selrefs: 0x3a18
+  __DATA_CONST.__objc_const: 0x9028
+  __DATA_CONST.__objc_selrefs: 0x3a28
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x66e0
+  __AUTH_CONST.__cfstring: 0x6700
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_const: 0x19b0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x408
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x428
-  __DATA.__objc_superrefs: 0x160
-  __DATA.__objc_ivar: 0x794
+  __DATA.__objc_ivar: 0x79c
   __DATA.__data: 0x9d0
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xa00
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA_DIRTY.__bss: 0x1f8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2163
-  Symbols:   7984
-  CStrings:  4539
+  Functions: 2166
+  Symbols:   7992
+  CStrings:  4551
 
Symbols:
+ -[TVPClipMediaItem clipTimeRange]
+ -[TVPMediaItemPromoInfo initWithTitleImageURL:originalTitleImageWidth:originalTitleImageHeight:title:genre:ratingDisplayName:ratingSystem:movieRuntime:canonicalId:isAddedToUpNext:addToUpNextLabelString:addedToUpNextLabelString:]
+ -[TVPMediaItemPromoInfo movieRuntime]
+ -[TVPPlayer updateAudioSelectionCriteria]
+ -[TVPTimeRange isEqual:]
+ _OBJC_IVAR_$_TVPClipMediaItem._clipTimeRange
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._movieRuntime
+ ___37-[TVPMediaItemLoader _avAssetOptions]_block_invoke.249
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.192
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.194
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.196
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.213
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.220
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.220.cold.1
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.223
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.229
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.234
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.193
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.195
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.195.cold.1
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.195.cold.2
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.224
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.230
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.235
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.225
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.231
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.226
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.232
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.456
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.458
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.459
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.467
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.460
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.468
+ ___block_literal_global.222
+ ___block_literal_global.228
+ ___block_literal_global.246
+ _objc_msgSend$initWithTitleImageURL:originalTitleImageWidth:originalTitleImageHeight:title:genre:ratingDisplayName:ratingSystem:movieRuntime:canonicalId:isAddedToUpNext:addToUpNextLabelString:addedToUpNextLabelString:
+ _objc_msgSend$updateAudioSelectionCriteria
- -[TVPMediaItemPromoInfo initWithTitleImageURL:originalTitleImageWidth:originalTitleImageHeight:title:genre:ratingDisplayName:ratingSystem:canonicalId:isAddedToUpNext:addToUpNextLabelString:addedToUpNextLabelString:]
- -[TVPPlayer _updateAudioSelectionCriteria]
- ___37-[TVPMediaItemLoader _avAssetOptions]_block_invoke.248
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.191
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.193
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.195
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.212
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.218
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.219.cold.1
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.222
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.228
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.232
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.192
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.194
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.194.cold.1
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.194.cold.2
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.223
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.229
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.234
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.224
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.230
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.225
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.231
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.452
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.454
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.455
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.463
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.456
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.464
- ___block_literal_global.221
- ___block_literal_global.227
- ___block_literal_global.245
- _objc_msgSend$_updateAudioSelectionCriteria
- _objc_msgSend$initWithTitleImageURL:originalTitleImageWidth:originalTitleImageHeight:title:genre:ratingDisplayName:ratingSystem:canonicalId:isAddedToUpNext:addToUpNextLabelString:addedToUpNextLabelString:
CStrings:
+ "\x11*!"
+ "@108@0:8@16d24d32@40@48@56@64@72@80B88@92@100"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_movieRuntime"
+ "T@\"TVPTimeRange\",R,N,V_clipTimeRange"
+ "_clipTimeRange"
+ "_movieRuntime"
+ "clipTimeRange"
+ "com.apple.hls.%@.%lu.promo.runtime"
+ "contentKeySession:didProvideContentKeyRequests:forInitializationData:"
+ "contentKeySession:externalProtectionStatusDidChangeForContentKey:"
+ "initWithTitleImageURL:originalTitleImageWidth:originalTitleImageHeight:title:genre:ratingDisplayName:ratingSystem:movieRuntime:canonicalId:isAddedToUpNext:addToUpNextLabelString:addedToUpNextLabelString:"
+ "movieRuntime"
+ "updateAudioSelectionCriteria"
+ "v32@0:8@\"AVContentKeySession\"16@\"AVContentKey\"24"
+ "v40@0:8@\"AVContentKeySession\"16@\"NSArray\"24@\"NSData\"32"
- "\x11)!"
- "@100@0:8@16d24d32@40@48@56@64@72B80@84@92"
- "_updateAudioSelectionCriteria"
- "initWithTitleImageURL:originalTitleImageWidth:originalTitleImageHeight:title:genre:ratingDisplayName:ratingSystem:canonicalId:isAddedToUpNext:addToUpNextLabelString:addedToUpNextLabelString:"

```
