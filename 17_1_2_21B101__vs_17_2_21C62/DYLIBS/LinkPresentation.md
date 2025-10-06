## LinkPresentation

> `/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation`

```diff

-240.1.0.0.0
-  __TEXT.__text: 0xce19c
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0xdf0c
-  __TEXT.__cstring: 0x806f
-  __TEXT.__gcc_except_tab: 0x1d340
+240.3.6.0.0
+  __TEXT.__text: 0xcf738
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_methlist: 0xdfc4
+  __TEXT.__cstring: 0x80b5
+  __TEXT.__gcc_except_tab: 0x1d370
   __TEXT.__const: 0x778
   __TEXT.__ustring: 0x484
-  __TEXT.__oslogstring: 0x29ed
+  __TEXT.__oslogstring: 0x2ce1
   __TEXT.__dlopen_cstrs: 0x96f
-  __TEXT.__unwind_info: 0x6cc4
+  __TEXT.__unwind_info: 0x6d30
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x2217
-  __TEXT.__objc_methname: 0x1cc32
-  __TEXT.__objc_methtype: 0x3e86
-  __TEXT.__objc_stubs: 0x16400
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x20f0
+  __TEXT.__objc_classname: 0x2221
+  __TEXT.__objc_methname: 0x1d0f6
+  __TEXT.__objc_methtype: 0x3eae
+  __TEXT.__objc_stubs: 0x16640
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__const: 0x2140
   __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x1d8
+  __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x24268
-  __DATA_CONST.__objc_selrefs: 0x64b0
-  __DATA_CONST.__objc_arraydata: 0x1490
-  __AUTH_CONST.__const: 0xce0
-  __AUTH_CONST.__objc_const: 0x6d68
-  __AUTH_CONST.__cfstring: 0xce80
+  __DATA_CONST.__objc_const: 0x24798
+  __DATA_CONST.__objc_selrefs: 0x6550
+  __DATA_CONST.__objc_arraydata: 0x14b8
+  __AUTH_CONST.__const: 0xd40
+  __AUTH_CONST.__objc_const: 0x6db0
+  __AUTH_CONST.__cfstring: 0xcf40
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH_CONST.__objc_arrayobj: 0x420
+  __AUTH_CONST.__objc_arrayobj: 0x438
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__auth_got: 0x7d8
   __AUTH.__objc_data: 0x2a58
   __DATA.__objc_protorefs: 0x70
   __DATA.__objc_classrefs: 0xc40
-  __DATA.__objc_superrefs: 0x650
-  __DATA.__objc_ivar: 0x1608
-  __DATA.__data: 0x1840
-  __DATA.__bss: 0x5d0
+  __DATA.__objc_superrefs: 0x648
+  __DATA.__objc_ivar: 0x160c
+  __DATA.__data: 0x18a0
+  __DATA.__bss: 0x600
   __DATA_DIRTY.__objc_data: 0x2828
   __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2EE806B2-4932-34D1-9F83-CDEBBA49132A
-  Functions: 5279
-  Symbols:   20659
-  CStrings:  9419
+  UUID: F0BCFF2B-C036-31B0-8E60-7D8441B12A8D
+  Functions: 5309
+  Symbols:   20778
+  CStrings:  9473
 
Symbols:
+ +[LPApplicationIdentification isFreeform]
+ +[LPInlineMediaPlaybackInformation _inlineiTunesMediaPlaybackInformationWithType:storeIdentifier:storefrontIdentifier:offers:previewURL:lyricExcerpt:]
+ +[LPInlineMediaPlaybackInformation albumPlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:]
+ +[LPInlineMediaPlaybackInformation audioBookPlaybackInformationWithStoreIdentifier:storefrontIdentifier:previewURL:persistentIdentifier:]
+ +[LPInlineMediaPlaybackInformation audioFilePlaybackInformationWithAudio:]
+ +[LPInlineMediaPlaybackInformation playlistPlaybackInformationWithStoreIdentifier:storefrontIdentifier:]
+ +[LPInlineMediaPlaybackInformation podcastEpisodePlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:]
+ +[LPInlineMediaPlaybackInformation podcastPlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:]
+ +[LPInlineMediaPlaybackInformation radioPlaybackInformationWithStoreIdentifier:storefrontIdentifier:]
+ +[LPInlineMediaPlaybackInformation songPlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:previewURL:lyricExcerpt:]
+ -[LPAudio _canEncodeWithoutComputation]
+ -[LPImage _cachedAtomicData]
+ -[LPImage _canEncodeWithoutComputation]
+ -[LPImage _waitForAsynchronouslyLoadedImageIfNeeded].cold.1
+ -[LPImage _waitForAsynchronouslyLoadedImageIfNeeded].cold.2
+ -[LPImage set_cachedAtomicData:]
+ -[LPLinkMetadata dataRepresentationForLocalLowFidelityUseOnly]
+ -[LPLinkMetadata dataRepresentationWithEncodingType:options:]
+ -[LPLinkMetadataPresentationTransformer _shouldUseMicroblogQuotedTextForStyle:]
+ -[LPLinkView _allowsAsynchronousImageDecoding]
+ -[LPLinkView _setAllowsAsynchronousImageDecoding:]
+ -[LPLinkView allowsAsynchronousImageDecodingForComponentView:]
+ -[LPPlayButtonView installiTunesButton].cold.1
+ -[LPTextViewStyle maximumLineCountScalingBehavior]
+ -[LPTextViewStyle setMaximumLineCountScalingBehavior:]
+ -[LPVideo _canEncodeWithoutComputation]
+ -[LPVisualMedia _cachedData]
+ -[LPVisualMedia _canEncodeWithoutComputation]
+ -[LPiTunesPlayButtonControl createPlaybackQueue].cold.1
+ -[NSCoder(LPExtras) _lp_coderOptions]
+ -[NSCoder(LPExtras) _lp_setCoderOptions:]
+ -[NSURL(LPInternal) _lp_fileSize]
+ -[NSURL(LPInternal) _lp_fileSize].cold.1
+ GCC_except_table1006
+ GCC_except_table1009
+ GCC_except_table1019
+ GCC_except_table1032
+ GCC_except_table1035
+ GCC_except_table1045
+ GCC_except_table1052
+ GCC_except_table1070
+ GCC_except_table1090
+ GCC_except_table110
+ GCC_except_table1106
+ GCC_except_table1108
+ GCC_except_table1110
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table179
+ GCC_except_table187
+ GCC_except_table191
+ GCC_except_table202
+ GCC_except_table207
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table216
+ GCC_except_table232
+ GCC_except_table242
+ GCC_except_table247
+ GCC_except_table258
+ GCC_except_table269
+ GCC_except_table270
+ GCC_except_table278
+ GCC_except_table285
+ GCC_except_table289
+ GCC_except_table291
+ GCC_except_table311
+ GCC_except_table342
+ GCC_except_table365
+ GCC_except_table386
+ GCC_except_table407
+ GCC_except_table445
+ GCC_except_table466
+ GCC_except_table468
+ GCC_except_table499
+ GCC_except_table520
+ GCC_except_table545
+ GCC_except_table572
+ GCC_except_table595
+ GCC_except_table618
+ GCC_except_table639
+ GCC_except_table658
+ GCC_except_table683
+ GCC_except_table704
+ GCC_except_table706
+ GCC_except_table727
+ GCC_except_table729
+ GCC_except_table748
+ GCC_except_table750
+ GCC_except_table76
+ GCC_except_table770
+ GCC_except_table772
+ GCC_except_table80
+ GCC_except_table815
+ GCC_except_table817
+ GCC_except_table840
+ GCC_except_table855
+ GCC_except_table857
+ GCC_except_table879
+ GCC_except_table891
+ GCC_except_table90
+ GCC_except_table909
+ GCC_except_table924
+ GCC_except_table947
+ GCC_except_table950
+ GCC_except_table960
+ GCC_except_table969
+ GCC_except_table972
+ GCC_except_table982
+ GCC_except_table996
+ GCC_except_table999
+ _LPLogChannelFilesystem
+ _LPLogChannelFilesystem.log
+ _LPLogChannelFilesystem.onceToken
+ _LPLogChannelImage
+ _LPLogChannelImage.log
+ _LPLogChannelImage.onceToken
+ _MRSystemAppPlaybackQueueSetFeatureName
+ _OBJC_IVAR_$_LPImage.__cachedAtomicData
+ _OBJC_IVAR_$_LPLinkView._allowsAsynchronousImageDecoding
+ _OBJC_IVAR_$_LPTextViewStyle._maximumLineCountScalingBehavior
+ __OBJC_$_CLASS_METHODS_LPInlineMediaPlaybackInformation
+ __OBJC_$_PROP_LIST_LPCodable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LPCodable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LPCodable
+ __OBJC_$_PROTOCOL_REFS_LPCodable
+ __OBJC_LABEL_PROTOCOL_$_LPCodable
+ __OBJC_PROTOCOL_$_LPCodable
+ ___41-[LPImageView _createImageViewWithImage:]_block_invoke
+ ___41-[LPImageView _createImageViewWithImage:]_block_invoke_2
+ ___54-[LPImage _initWithPlatformImageGenerator:properties:]_block_invoke.48
+ ___LPLogChannelFilesystem_block_invoke
+ ___LPLogChannelImage_block_invoke
+ ___block_descriptor_48_ea8_32s40w_e17_v16?0"UIImage"8ls32l8w40l8
+ ___block_descriptor_49_ea8_32s40r_e24_v16?0?<v?"UIImage">8lr40l8s32l8
+ ___block_descriptor_56_ea8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
+ ___block_descriptor_57_ea8_32s40r_e24_v16?0?<v?"UIImage">8lr40l8s32l8
+ ___block_literal_global.109
+ ___block_literal_global.1174
+ ___block_literal_global.1183
+ ___block_literal_global.1190
+ ___block_literal_global.1877
+ ___block_literal_global.22
+ ___block_literal_global.25
+ ___block_literal_global.268
+ ___block_literal_global.287
+ ___block_literal_global.303
+ ___block_literal_global.306
+ ___block_literal_global.76
+ ___block_literal_global.79
+ ___dynamicTypeLeadingScalingFactorLargeToXXXL_block_invoke
+ _cardHeadingIconSize.normalSize.1191
+ _dynamicTypeLeadingScalingFactorLargeToXXXL.onceToken
+ _dynamicTypeLeadingScalingFactorLargeToXXXL.scalingFactor
+ _fallbackIconSize.normalSize.1177
+ _kCTFontContentSizeCategoryXXXL
+ _objc_getProperty
+ _objc_msgSend$_cachedAtomicData
+ _objc_msgSend$_cachedData
+ _objc_msgSend$_canEncodeWithoutComputation
+ _objc_msgSend$_inlineiTunesMediaPlaybackInformationWithType:storeIdentifier:storefrontIdentifier:offers:previewURL:lyricExcerpt:
+ _objc_msgSend$_lp_coderOptions
+ _objc_msgSend$_lp_fileSize
+ _objc_msgSend$_lp_setCoderOptions:
+ _objc_msgSend$_setAllowsAsynchronousImageDecoding:
+ _objc_msgSend$_shouldUseMicroblogQuotedTextForStyle:
+ _objc_msgSend$albumPlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:
+ _objc_msgSend$allowsAsynchronousImageDecodingForComponentView:
+ _objc_msgSend$audioBookPlaybackInformationWithStoreIdentifier:storefrontIdentifier:previewURL:persistentIdentifier:
+ _objc_msgSend$audioFilePlaybackInformationWithAudio:
+ _objc_msgSend$dataRepresentationWithEncodingType:options:
+ _objc_msgSend$filteredImageFromImage:filterInfo:size:contentsScale:waitForCPUSynchronization:logKey:completion:
+ _objc_msgSend$isFreeform
+ _objc_msgSend$playlistPlaybackInformationWithStoreIdentifier:storefrontIdentifier:
+ _objc_msgSend$podcastEpisodePlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:
+ _objc_msgSend$podcastPlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:
+ _objc_msgSend$prepareThumbnailOfSize:completionHandler:
+ _objc_msgSend$radioPlaybackInformationWithStoreIdentifier:storefrontIdentifier:
+ _objc_msgSend$setMaximumLineCountScalingBehavior:
+ _objc_msgSend$set_cachedAtomicData:
+ _objc_msgSend$songPlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:previewURL:lyricExcerpt:
+ _objc_setProperty_atomic
+ _sizeFitsWithinSize
+ _subscribeToAppleMusicStatus
+ _transcriptBoldTextFont.contentSizeCategory.163
+ _transcriptBoldTextFont.font.164
- -[LPARAsset _encodedSize]
- -[LPImage _preparePlatformImageWithCompletionHandler:]
- -[LPInlineMediaPlaybackInformation initWithType:]
- -[LPInlineMediaPlaybackInformation setAudio:]
- -[LPInlineMediaPlaybackInformation setLyricExcerpt:]
- -[LPInlineMediaPlaybackInformation setOffers:]
- -[LPInlineMediaPlaybackInformation setPersistentIdentifier:]
- -[LPInlineMediaPlaybackInformation setPreviewURL:]
- -[LPInlineMediaPlaybackInformation setStoreIdentifier:]
- -[LPInlineMediaPlaybackInformation setStorefrontIdentifier:]
- -[LPLinkMetadata dataRepresentationWithEncodingType:]
- -[LPTextViewStyle setShouldScaleMaximumLinesWithDynamicType:]
- -[LPTextViewStyle shouldScaleMaximumLinesWithDynamicType]
- -[LPVideo _encodedSize]
- GCC_except_table1005
- GCC_except_table1007
- GCC_except_table1015
- GCC_except_table1031
- GCC_except_table1033
- GCC_except_table1044
- GCC_except_table1048
- GCC_except_table1066
- GCC_except_table1086
- GCC_except_table1105
- GCC_except_table1107
- GCC_except_table1109
- GCC_except_table111
- GCC_except_table113
- GCC_except_table115
- GCC_except_table166
- GCC_except_table175
- GCC_except_table182
- GCC_except_table188
- GCC_except_table190
- GCC_except_table192
- GCC_except_table203
- GCC_except_table209
- GCC_except_table211
- GCC_except_table213
- GCC_except_table226
- GCC_except_table229
- GCC_except_table241
- GCC_except_table257
- GCC_except_table259
- GCC_except_table263
- GCC_except_table267
- GCC_except_table284
- GCC_except_table286
- GCC_except_table290
- GCC_except_table338
- GCC_except_table361
- GCC_except_table382
- GCC_except_table403
- GCC_except_table418
- GCC_except_table441
- GCC_except_table462
- GCC_except_table467
- GCC_except_table493
- GCC_except_table516
- GCC_except_table541
- GCC_except_table568
- GCC_except_table591
- GCC_except_table614
- GCC_except_table635
- GCC_except_table654
- GCC_except_table679
- GCC_except_table700
- GCC_except_table705
- GCC_except_table723
- GCC_except_table728
- GCC_except_table744
- GCC_except_table749
- GCC_except_table766
- GCC_except_table771
- GCC_except_table811
- GCC_except_table816
- GCC_except_table836
- GCC_except_table851
- GCC_except_table856
- GCC_except_table875
- GCC_except_table887
- GCC_except_table905
- GCC_except_table920
- GCC_except_table945
- GCC_except_table948
- GCC_except_table956
- GCC_except_table968
- GCC_except_table970
- GCC_except_table978
- GCC_except_table995
- GCC_except_table997
- _OBJC_IVAR_$_LPImage._data
- _OBJC_IVAR_$_LPTextViewStyle._shouldScaleMaximumLinesWithDynamicType
- ___54-[LPImage _initWithPlatformImageGenerator:properties:]_block_invoke_4
- ___54-[LPImage _preparePlatformImageWithCompletionHandler:]_block_invoke
- ___block_descriptor_41_ea8_32s_e24_v16?0?<v?"UIImage">8ls32l8
- ___block_descriptor_49_ea8_32s_e24_v16?0?<v?"UIImage">8ls32l8
- ___block_literal_global.108
- ___block_literal_global.1181
- ___block_literal_global.1186
- ___block_literal_global.1859
- ___block_literal_global.296
- ___block_literal_global.299
- ___block_literal_global.75
- ___block_literal_global.78
- ___block_literal_global.95
- _cardHeadingIconSize.normalSize.1189
- _fallbackIconSize.normalSize.1174
- _objc_msgSend$curatorID
- _objc_msgSend$dataRepresentationWithEncodingType:
- _objc_msgSend$filteredImageFromImage:filterInfo:size:contentsScale:completion:
- _objc_msgSend$setPersistentIdentifier:
- _objc_msgSend$setShouldScaleMaximumLinesWithDynamicType:
- _objc_msgSend$setStorefrontIdentifier:
- _transcriptBoldTextFont.contentSizeCategory.166
- _transcriptBoldTextFont.font.167
CStrings:
+ "\bF"
+ "#\x16"
+ "@32@0:8Q16Q24"
+ "@64@0:8Q16@24@32@40@48@56"
+ "Failed to read size of file: %@"
+ "Filesystem"
+ "Image"
+ "LPAnimatedImageTranscoder<%d>: failed, output file is too big (size=%llu)"
+ "LPAnimatedImageTranscoder<%d>: finished transcoding (size=%llu)"
+ "LPCodable"
+ "LPImage<%p, %p>: created async LPImages for book cover"
+ "LPImage<%p>: created async LPImage for %@"
+ "LPImage<%p>: created async image for %@"
+ "LPImage<%p>: finished loading async image"
+ "LPImage<%p>: finished loading async image (success: %d)"
+ "LPImage<%p>: started loading async image"
+ "LPImage<%p>: taking too long in _waitForAsynchronouslyLoadedImageIfNeeded"
+ "LPImage<%p>: timed out in _waitForAsynchronouslyLoadedImageIfNeeded"
+ "MusicKit"
+ "T@\"LPLyricExcerptMetadata\",R,&,N,V_lyricExcerpt"
+ "T@\"NSArray\",R,C,N,V_offers"
+ "T@\"NSData\",&,V__cachedAtomicData"
+ "T@\"NSString\",R,C,N,V_persistentIdentifier"
+ "T@\"NSString\",R,C,N,V_storeIdentifier"
+ "T@\"NSString\",R,C,N,V_storefrontIdentifier"
+ "TB,N,S_setAllowsAsynchronousImageDecoding:,V_allowsAsynchronousImageDecoding"
+ "TQ,N,S_lp_setCoderOptions:"
+ "Tq,N,V_maximumLineCountScalingBehavior"
+ "Trying to install an iTunes button with no store identifier or persistent identifier %@; falling back to preview button"
+ "Trying to install an iTunes button with no store identifier or persistent identifier or preview url %@; this violates the invariant"
+ "__cachedAtomicData"
+ "_allowsAsynchronousImageDecoding"
+ "_cachedAtomicData"
+ "_cachedData"
+ "_canEncodeWithoutComputation"
+ "_inlineiTunesMediaPlaybackInformationWithType:storeIdentifier:storefrontIdentifier:offers:previewURL:lyricExcerpt:"
+ "_lp_coderOptions"
+ "_lp_fileSize"
+ "_lp_setCoderOptions:"
+ "_maximumLineCountScalingBehavior"
+ "_setAllowsAsynchronousImageDecoding:"
+ "_shouldUseMicroblogQuotedTextForStyle:"
+ "albumPlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:"
+ "allowsAsynchronousImageDecodingForComponentView:"
+ "audioBookPlaybackInformationWithStoreIdentifier:storefrontIdentifier:previewURL:persistentIdentifier:"
+ "audioFilePlaybackInformationWithAudio:"
+ "dataRepresentationForLocalLowFidelityUseOnly"
+ "dataRepresentationWithEncodingType:options:"
+ "filteredImageFromImage:filterInfo:size:contentsScale:waitForCPUSynchronization:logKey:completion:"
+ "isFreeform"
+ "maximumLineCountScalingBehavior"
+ "playlistPlaybackInformationWithStoreIdentifier:storefrontIdentifier:"
+ "podcastEpisodePlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:"
+ "podcastPlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:"
+ "prepareThumbnailOfSize:completionHandler:"
+ "radioPlaybackInformationWithStoreIdentifier:storefrontIdentifier:"
+ "setMaximumLineCountScalingBehavior:"
+ "set_cachedAtomicData:"
+ "songPlaybackInformationWithStoreIdentifier:storefrontIdentifier:offers:previewURL:lyricExcerpt:"
+ "store identifier for playback information %@ is nil"
- "\tE"
- "3\x16"
- "LPAnimatedImageTranscoder<%d>: failed, output file is too big (size=%zd)"
- "LPAnimatedImageTranscoder<%d>: finished transcoding (size=%zd)"
- "T@\"LPLyricExcerptMetadata\",&,N,V_lyricExcerpt"
- "T@\"NSString\",C,N,V_persistentIdentifier"
- "T@\"NSString\",C,N,V_storefrontIdentifier"
- "T@\"NSURL\",R,&,N,V_fileURL"
- "TB,N,V_shouldScaleMaximumLinesWithDynamicType"
- "_preparePlatformImageWithCompletionHandler:"
- "_shouldScaleMaximumLinesWithDynamicType"
- "dataRepresentationWithEncodingType:"
- "filteredImageFromImage:filterInfo:size:contentsScale:completion:"
- "setPersistentIdentifier:"
- "setShouldScaleMaximumLinesWithDynamicType:"
- "setStorefrontIdentifier:"
- "shouldScaleMaximumLinesWithDynamicType"

```
