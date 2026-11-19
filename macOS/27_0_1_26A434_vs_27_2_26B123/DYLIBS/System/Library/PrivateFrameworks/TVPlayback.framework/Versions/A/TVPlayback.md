## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/Versions/A/TVPlayback`

```diff

-635.0.7.0.0
-  __TEXT.__text: 0x1482c8
-  __TEXT.__objc_methlist: 0x58d0
+635.10.15.0.0
+  __TEXT.__text: 0x14aaac
+  __TEXT.__objc_methlist: 0x5ae0
   __TEXT.__const: 0x22e90
-  __TEXT.__cstring: 0x6768
-  __TEXT.__oslogstring: 0x572b
-  __TEXT.__gcc_except_tab: 0x1d58
-  __TEXT.__unwind_info: 0x16c0
+  __TEXT.__cstring: 0x686d
+  __TEXT.__oslogstring: 0x5a04
+  __TEXT.__gcc_except_tab: 0x1d84
+  __TEXT.__unwind_info: 0x1740
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1b40
-  __DATA_CONST.__objc_classlist: 0x1d0
-  __DATA_CONST.__objc_catlist: 0x80
+  __DATA_CONST.__const: 0x1b50
+  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b80
+  __DATA_CONST.__objc_selrefs: 0x3cc8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x738
-  __AUTH_CONST.__const: 0xba70
-  __AUTH_CONST.__cfstring: 0x6600
-  __AUTH_CONST.__objc_const: 0x89d0
+  __DATA_CONST.__got: 0x770
+  __AUTH_CONST.__const: 0xbaf0
+  __AUTH_CONST.__cfstring: 0x6720
+  __AUTH_CONST.__objc_const: 0x8c68
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x6cc
+  __AUTH.__objc_data: 0x7d0
+  __DATA.__objc_ivar: 0x6e8
   __DATA.__data: 0x1040
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x110
   __DATA.__common: 0x9f0
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__bss: 0x1f8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2330
-  Symbols:   5384
-  CStrings:  1288
+  Functions: 2385
+  Symbols:   5506
+  CStrings:  1311
 
Symbols:
+ +[AVMediaSelectionGroup(TVPSignLanguageAdditions) tvp_signLanguageOptionMatchingLanguage:inOptions:]
+ +[TVPPlayer _downloadedOptionsInGroup:ofAsset:]
+ +[TVPPlayer _updateVideoSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:preferredSignLanguage:]
+ +[TVPPlayer savedPreferredSignLanguage]
+ -[AVMediaSelectionGroup(TVPSignLanguageAdditions) tvp_signLanguageDownloadOption]
+ -[AVQueuePlayer(TVPAdditions) setTvp_cachedVideoSelectionCriteria:]
+ -[AVQueuePlayer(TVPAdditions) tvp_cachedVideoSelectionCriteria]
+ -[TVPPlayer _downloadedSignLanguageOptions]
+ -[TVPPlayer _effectiveSignLanguage]
+ -[TVPPlayer _nextChapterInDirection:]
+ -[TVPPlayer _populatePlayerItemArtwork:withMetadataFromMediaItem:]
+ -[TVPPlayer _signLanguageForSelectionCriteria]
+ -[TVPPlayer _updateVideoSelectionCriteria]
+ -[TVPPlayer allowsSignLanguageSelection]
+ -[TVPPlayer cachedSelectedVideoOption]
+ -[TVPPlayer canSkipToNextChapterInDirection:]
+ -[TVPPlayer preferredSignLanguage]
+ -[TVPPlayer selectedVideoOption]
+ -[TVPPlayer setAllowsSignLanguageSelection:]
+ -[TVPPlayer setArtworkImageData:onPlayerItem:]
+ -[TVPPlayer setCachedSelectedVideoOption:]
+ -[TVPPlayer setPreferredSignLanguage:]
+ -[TVPPlayer setSelectedVideoOption:]
+ -[TVPPlayer setSignLanguageChosenByViewer:]
+ -[TVPPlayer signLanguageChosenByViewer]
+ -[TVPPlayer videoOptions]
+ -[TVPVideoOption .cxx_destruct]
+ -[TVPVideoOption avMediaSelectionOption]
+ -[TVPVideoOption description]
+ -[TVPVideoOption extendedLanguageCode]
+ -[TVPVideoOption hasMediaCharacteristic:]
+ -[TVPVideoOption hasSignLanguage]
+ -[TVPVideoOption hash]
+ -[TVPVideoOption initWithOption:isDefault:isDownloaded:]
+ -[TVPVideoOption isDefault]
+ -[TVPVideoOption isDownloaded]
+ -[TVPVideoOption isEqual:]
+ -[TVPVideoOption localizedDisplayString]
+ -[TVPVideoOption mediaCharacteristics]
+ -[TVPVideoOption setAvMediaSelectionOption:]
+ -[TVPVideoOption setIsDefault:]
+ -[TVPVideoOption setIsDownloaded:]
+ GCC_except_table147
+ GCC_except_table255
+ GCC_except_table265
+ GCC_except_table268
+ GCC_except_table317
+ GCC_except_table349
+ GCC_except_table367
+ GCC_except_table394
+ GCC_except_table398
+ GCC_except_table408
+ GCC_except_table419
+ GCC_except_table450
+ GCC_except_table451
+ GCC_except_table455
+ GCC_except_table456
+ GCC_except_table460
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table464
+ GCC_except_table467
+ GCC_except_table473
+ GCC_except_table477
+ GCC_except_table482
+ GCC_except_table486
+ GCC_except_table491
+ GCC_except_table497
+ GCC_except_table499
+ GCC_except_table501
+ GCC_except_table528
+ GCC_except_table530
+ GCC_except_table535
+ GCC_except_table541
+ GCC_except_table550
+ GCC_except_table555
+ GCC_except_table564
+ GCC_except_table570
+ GCC_except_table578
+ GCC_except_table581
+ GCC_except_table593
+ GCC_except_table595
+ GCC_except_table598
+ GCC_except_table602
+ OBJC_IVAR_$_TVPPlayer._allowsSignLanguageSelection
+ OBJC_IVAR_$_TVPPlayer._cachedSelectedVideoOption
+ OBJC_IVAR_$_TVPPlayer._preferredSignLanguage
+ OBJC_IVAR_$_TVPPlayer._signLanguageChosenByViewer
+ OBJC_IVAR_$_TVPVideoOption._avMediaSelectionOption
+ OBJC_IVAR_$_TVPVideoOption._isDefault
+ OBJC_IVAR_$_TVPVideoOption._isDownloaded
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
+ _TVPMediaItemMetadataArtworkImageData
+ _TVPSignLanguageCopyPreference
+ _TVPSignLanguageDefaultLanguageCode
+ _TVPSignLanguageDownloadLanguage
+ _TVPSignLanguagePreferredLanguage
+ _TVPSignLanguageSetPreferredLanguage
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
+ ___block_descriptor_56_e8_32s40s48w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0l
+ _notify_post
+ _objc_msgSend$_downloadedOptionsInGroup:ofAsset:
+ _objc_msgSend$_downloadedSignLanguageOptions
+ _objc_msgSend$_effectiveSignLanguage
+ _objc_msgSend$_nextChapterInDirection:
+ _objc_msgSend$_populatePlayerItemArtwork:withMetadataFromMediaItem:
+ _objc_msgSend$_signLanguageForSelectionCriteria
+ _objc_msgSend$_updateVideoSelectionCriteria
+ _objc_msgSend$_updateVideoSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:preferredSignLanguage:
+ _objc_msgSend$allowsSignLanguageSelection
+ _objc_msgSend$assetCache
+ _objc_msgSend$cachedSelectedVideoOption
+ _objc_msgSend$dataTaskWithURL:completionHandler:
+ _objc_msgSend$defaultOption
+ _objc_msgSend$extendedLanguageCode
+ _objc_msgSend$hasSignLanguage
+ _objc_msgSend$initWithOption:isDefault:isDownloaded:
+ _objc_msgSend$isDefault
+ _objc_msgSend$mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:
+ _objc_msgSend$mediaSelectionOptionsFromArray:withMediaCharacteristics:
+ _objc_msgSend$mediaSelectionOptionsInMediaSelectionGroup:
+ _objc_msgSend$preferredSignLanguage
+ _objc_msgSend$resume
+ _objc_msgSend$savedPreferredSignLanguage
+ _objc_msgSend$selectedVideoOption
+ _objc_msgSend$setArtworkImageData:onPlayerItem:
+ _objc_msgSend$setCachedSelectedVideoOption:
+ _objc_msgSend$setPreferredSignLanguage:
+ _objc_msgSend$setSignLanguageChosenByViewer:
+ _objc_msgSend$setTvp_cachedVideoSelectionCriteria:
+ _objc_msgSend$sharedSession
+ _objc_msgSend$signLanguageChosenByViewer
+ _objc_msgSend$supplementalMetadata
+ _objc_msgSend$tvp_cachedVideoSelectionCriteria
+ _objc_msgSend$tvp_signLanguageOptionMatchingLanguage:inOptions:
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$videoOptions
- GCC_except_table145
- GCC_except_table248
- GCC_except_table254
- GCC_except_table258
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
- GCC_except_table441
- GCC_except_table444
- GCC_except_table446
- GCC_except_table447
- GCC_except_table453
- GCC_except_table457
- GCC_except_table462
- GCC_except_table471
- GCC_except_table479
- GCC_except_table481
- GCC_except_table483
- GCC_except_table510
- GCC_except_table512
- GCC_except_table514
- GCC_except_table517
- GCC_except_table523
- GCC_except_table534
- GCC_except_table537
- GCC_except_table542
- GCC_except_table546
- GCC_except_table563
- GCC_except_table575
- GCC_except_table577
- GCC_except_table580
- GCC_except_table584
CStrings:
+ "%@ isDefault: %@ isDownloaded: %@"
+ "Dropping artwork downloaded from URL, image data was set during the download and takes precedence"
+ "Failed to load artwork for player item metadata: %{public}@"
+ "GB"
+ "Not the same show; clearing the preferred sign language"
+ "Performing automatic re-selection of video for player item %@ in player %@"
+ "PreferredSignLanguage"
+ "PreferredSignLanguageDownload"
+ "Selected video option: %@"
+ "Selecting video media option: %@"
+ "Setting cached video option from active player item %@ to %@."
+ "Setting visual media selection criteria on %@ (is interstitial player: %@) to %@"
+ "TVPMediaItemMetadataArtworkImageData"
+ "Unable to load visual media selection group due to error %@"
+ "Updating player item supplamental metadata with artwork"
+ "Video selection option is nil, not selecting"
+ "Will perform automatic re-selection of video for player item %@ in player %@"
+ "ase"
+ "bfi"
+ "com.apple.AppleTV.signLanguageSettingDidChange"
+ "selectedVideoOption"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "videoOptions"
```
