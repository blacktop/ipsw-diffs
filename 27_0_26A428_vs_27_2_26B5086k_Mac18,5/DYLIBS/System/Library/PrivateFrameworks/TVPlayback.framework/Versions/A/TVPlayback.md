## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/Versions/A/TVPlayback`

```diff

-635.0.7.0.0
-  __TEXT.__text: 0x146624
-  __TEXT.__objc_methlist: 0x58d0
+635.10.11.0.0
+  __TEXT.__text: 0x1485e8
+  __TEXT.__objc_methlist: 0x5a38
   __TEXT.__const: 0x22e90
-  __TEXT.__cstring: 0x6768
-  __TEXT.__oslogstring: 0x572b
-  __TEXT.__gcc_except_tab: 0x1d58
-  __TEXT.__unwind_info: 0x1bf8
+  __TEXT.__cstring: 0x67fe
+  __TEXT.__oslogstring: 0x5996
+  __TEXT.__gcc_except_tab: 0x1d84
+  __TEXT.__unwind_info: 0x1c90
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1b40
-  __DATA_CONST.__objc_classlist: 0x1d0
-  __DATA_CONST.__objc_catlist: 0x80
+  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b80
+  __DATA_CONST.__objc_selrefs: 0x3c68
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x738
-  __AUTH_CONST.__const: 0xba70
-  __AUTH_CONST.__cfstring: 0x6600
-  __AUTH_CONST.__objc_const: 0x89d0
+  __DATA_CONST.__got: 0x770
+  __AUTH_CONST.__const: 0xbac0
+  __AUTH_CONST.__cfstring: 0x6700
+  __AUTH_CONST.__objc_const: 0x8ba8
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x388
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x6cc
+  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH.__objc_data: 0x7d0
+  __DATA.__objc_ivar: 0x6d8
   __DATA.__data: 0x1040
   __DATA.__common: 0x9f0
   __DATA_DIRTY.__objc_data: 0xaa0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2330
-  Symbols:   5384
-  CStrings:  1288
+  Functions: 2371
+  Symbols:   5472
+  CStrings:  1308
 
Symbols:
+ +[AVMediaSelectionGroup(TVPSignLanguageAdditions) tvp_signLanguageOptionMatchingLanguage:inOptions:]
+ +[TVPPlayer _updateVideoSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:]
+ -[AVMediaSelectionGroup(TVPSignLanguageAdditions) tvp_signLanguageDownloadOption]
+ -[AVQueuePlayer(TVPAdditions) setTvp_cachedVideoSelectionCriteria:]
+ -[AVQueuePlayer(TVPAdditions) tvp_cachedVideoSelectionCriteria]
+ -[TVPPlayer _nextChapterInDirection:]
+ -[TVPPlayer _populatePlayerItemArtwork:withMetadataFromMediaItem:]
+ -[TVPPlayer _updateVideoSelectionCriteria]
+ -[TVPPlayer cachedSelectedVideoOption]
+ -[TVPPlayer canSkipToNextChapterInDirection:]
+ -[TVPPlayer selectedVideoOption]
+ -[TVPPlayer setCachedSelectedVideoOption:]
+ -[TVPPlayer setSelectedVideoOption:]
+ -[TVPPlayer videoOptions]
+ -[TVPVideoOption .cxx_destruct]
+ -[TVPVideoOption avMediaSelectionOption]
+ -[TVPVideoOption description]
+ -[TVPVideoOption extendedLanguageCode]
+ -[TVPVideoOption hasMediaCharacteristic:]
+ -[TVPVideoOption hasSignLanguage]
+ -[TVPVideoOption hash]
+ -[TVPVideoOption initWithOption:isDefault:]
+ -[TVPVideoOption isDefault]
+ -[TVPVideoOption isEqual:]
+ -[TVPVideoOption localizedDisplayString]
+ -[TVPVideoOption mediaCharacteristics]
+ -[TVPVideoOption setAvMediaSelectionOption:]
+ -[TVPVideoOption setIsDefault:]
+ GCC_except_table147
+ GCC_except_table253
+ GCC_except_table259
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table315
+ GCC_except_table347
+ GCC_except_table361
+ GCC_except_table388
+ GCC_except_table392
+ GCC_except_table402
+ GCC_except_table410
+ GCC_except_table434
+ GCC_except_table442
+ GCC_except_table451
+ GCC_except_table452
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table458
+ GCC_except_table464
+ GCC_except_table468
+ GCC_except_table473
+ GCC_except_table477
+ GCC_except_table482
+ GCC_except_table490
+ GCC_except_table492
+ GCC_except_table494
+ GCC_except_table521
+ GCC_except_table525
+ GCC_except_table528
+ GCC_except_table543
+ GCC_except_table545
+ GCC_except_table548
+ GCC_except_table553
+ GCC_except_table557
+ GCC_except_table571
+ GCC_except_table574
+ GCC_except_table586
+ GCC_except_table588
+ GCC_except_table591
+ GCC_except_table595
+ OBJC_IVAR_$_TVPPlayer._cachedSelectedVideoOption
+ OBJC_IVAR_$_TVPVideoOption._avMediaSelectionOption
+ OBJC_IVAR_$_TVPVideoOption._isDefault
+ TVPSignLanguageDefaultLanguageCode
+ TVPSignLanguageDefaultLanguageCode.onceToken
+ TVPSignLanguageDefaultLanguageCode.sDefaultLanguageCode
+ _AVMediaCharacteristicSignLanguageInterpretationForAccessibility
+ _AVMediaCharacteristicVisual
+ _AVMetadataCommonIdentifierArtwork
+ _CFPreferencesAppSynchronize
+ _CFPreferencesCopyAppValue
+ _CFPreferencesSetAppValue
+ _NSLocaleCountryCode
+ _OBJC_CLASS_$_AVMediaSelectionGroup
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_TVPVideoOption
+ _OBJC_METACLASS_$_TVPVideoOption
+ _TVPSignLanguageCopyPreference
+ _TVPSignLanguageDefaultLanguageCode
+ _TVPSignLanguagePreferredLanguage
+ _TVPSignLanguageSetPreferredLanguage
+ _TVPSignLanguageSetSettingEnabled
+ _TVPSignLanguageSettingEnabled
+ __66-[TVPPlayer _populatePlayerItemArtwork:withMetadataFromMediaItem:]_block_invoke
+ __OBJC_$_CATEGORY_AVMediaSelectionGroup_$_TVPSignLanguageAdditions
+ __OBJC_$_CATEGORY_CLASS_METHODS_AVMediaSelectionGroup_$_TVPSignLanguageAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_AVMediaSelectionGroup_$_TVPSignLanguageAdditions
+ __OBJC_$_INSTANCE_METHODS_TVPVideoOption
+ __OBJC_$_INSTANCE_VARIABLES_TVPVideoOption
+ __OBJC_$_PROP_LIST_AVMediaSelectionGroup_$_TVPSignLanguageAdditions
+ __OBJC_$_PROP_LIST_TVPVideoOption
+ __OBJC_CLASS_RO_$_TVPVideoOption
+ __OBJC_METACLASS_RO_$_TVPVideoOption
+ ___66-[TVPPlayer _populatePlayerItemArtwork:withMetadataFromMediaItem:]_block_invoke
+ ___TVPSignLanguageDefaultLanguageCode_block_invoke
+ ___block_descriptor_40_e8_32w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
+ _objc_msgSend$_nextChapterInDirection:
+ _objc_msgSend$_populatePlayerItemArtwork:withMetadataFromMediaItem:
+ _objc_msgSend$_updateVideoSelectionCriteria
+ _objc_msgSend$_updateVideoSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:
+ _objc_msgSend$assetCache
+ _objc_msgSend$cachedSelectedVideoOption
+ _objc_msgSend$dataTaskWithURL:completionHandler:
+ _objc_msgSend$defaultOption
+ _objc_msgSend$extendedLanguageCode
+ _objc_msgSend$initWithOption:isDefault:
+ _objc_msgSend$isDefault
+ _objc_msgSend$mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:
+ _objc_msgSend$mediaSelectionOptionsFromArray:withMediaCharacteristics:
+ _objc_msgSend$mediaSelectionOptionsInMediaSelectionGroup:
+ _objc_msgSend$resume
+ _objc_msgSend$selectedVideoOption
+ _objc_msgSend$setCachedSelectedVideoOption:
+ _objc_msgSend$setTvp_cachedVideoSelectionCriteria:
+ _objc_msgSend$sharedSession
+ _objc_msgSend$supplementalMetadata
+ _objc_msgSend$tvp_cachedVideoSelectionCriteria
+ _objc_msgSend$tvp_signLanguageOptionMatchingLanguage:inOptions:
+ _objc_msgSend$uppercaseString
- GCC_except_table145
- GCC_except_table248
- GCC_except_table254
- GCC_except_table258
- GCC_except_table261
- GCC_except_table309
- GCC_except_table341
- GCC_except_table353
- GCC_except_table380
- GCC_except_table384
- GCC_except_table399
- GCC_except_table423
- GCC_except_table430
- GCC_except_table431
- GCC_except_table435
- GCC_except_table436
- GCC_except_table440
- GCC_except_table443
- GCC_except_table444
- GCC_except_table453
- GCC_except_table462
- GCC_except_table466
- GCC_except_table471
- GCC_except_table479
- GCC_except_table481
- GCC_except_table483
- GCC_except_table510
- GCC_except_table512
- GCC_except_table514
- GCC_except_table517
- GCC_except_table532
- GCC_except_table537
- GCC_except_table542
- GCC_except_table546
- GCC_except_table552
- GCC_except_table560
- GCC_except_table575
- GCC_except_table577
- GCC_except_table580
- GCC_except_table584
CStrings:
+ "%@ isDefault: %@"
+ "Failed to load artwork for player item metadata: %{public}@"
+ "GB"
+ "Performing automatic re-selection of video for player item %@ in player %@"
+ "PreferredSignLanguage"
+ "Selected video option: %@"
+ "Selecting video media option: %@"
+ "Setting cached video option from active player item %@ to %@."
+ "Setting prefs for video language code to %@"
+ "Setting visual media selection criteria on %@ (is interstitial player: %@) to %@"
+ "SignLanguageEnabled"
+ "Unable to load visual media selection group due to error %@"
+ "Updating player item supplamental metadata with artwork"
+ "Video selection option is nil, not selecting"
+ "Will perform automatic re-selection of video for player item %@ in player %@"
+ "ase"
+ "bfi"
+ "selectedVideoOption"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "videoOptions"
```
