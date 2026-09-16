## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-635.0.7.0.0
-  __TEXT.__text: 0x67320
-  __TEXT.__objc_methlist: 0x5fb0
+635.10.11.0.0
+  __TEXT.__text: 0x68cbc
+  __TEXT.__objc_methlist: 0x6118
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x6b1f
-  __TEXT.__oslogstring: 0x7016
+  __TEXT.__cstring: 0x6ba3
+  __TEXT.__oslogstring: 0x7253
   __TEXT.__gcc_except_tab: 0x1fd8
-  __TEXT.__unwind_info: 0x1b58
+  __TEXT.__unwind_info: 0x1bd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x24e0
-  __DATA_CONST.__objc_classlist: 0x1f8
-  __DATA_CONST.__objc_catlist: 0x80
+  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e08
+  __DATA_CONST.__objc_selrefs: 0x3eb8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x170
+  __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x8d8
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x6c80
-  __AUTH_CONST.__objc_const: 0x9aa8
+  __DATA_CONST.__got: 0x8f8
+  __AUTH_CONST.__const: 0x6a0
+  __AUTH_CONST.__cfstring: 0x6da0
+  __AUTH_CONST.__objc_const: 0x9c80
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x430
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x7cc
+  __AUTH_CONST.__auth_got: 0x448
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x7d8
   __DATA.__data: 0xae0
   __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__bss: 0x230

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2276
-  Symbols:   5677
-  CStrings:  1449
+  Functions: 2313
+  Symbols:   5750
+  CStrings:  1468
 
Symbols:
+ +[AVMediaSelectionGroup(TVPSignLanguageAdditions) tvp_signLanguageOptionMatchingLanguage:inOptions:]
+ +[TVPPlayer _updateVideoSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:]
+ -[AVMediaSelectionGroup(TVPSignLanguageAdditions) tvp_signLanguageDownloadOption]
+ -[AVQueuePlayer(TVPAdditions) setTvp_cachedVideoSelectionCriteria:]
+ -[AVQueuePlayer(TVPAdditions) tvp_cachedVideoSelectionCriteria]
+ -[TVPPlayer _nextChapterInDirection:]
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
+ GCC_except_table136
+ GCC_except_table239
+ GCC_except_table245
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table301
+ GCC_except_table331
+ GCC_except_table343
+ GCC_except_table365
+ GCC_except_table369
+ GCC_except_table378
+ GCC_except_table389
+ GCC_except_table415
+ GCC_except_table418
+ GCC_except_table421
+ GCC_except_table422
+ GCC_except_table424
+ GCC_except_table427
+ GCC_except_table433
+ GCC_except_table440
+ GCC_except_table444
+ GCC_except_table449
+ GCC_except_table454
+ GCC_except_table456
+ GCC_except_table458
+ GCC_except_table483
+ GCC_except_table485
+ GCC_except_table487
+ GCC_except_table490
+ GCC_except_table496
+ GCC_except_table503
+ GCC_except_table505
+ GCC_except_table507
+ GCC_except_table512
+ GCC_except_table516
+ GCC_except_table530
+ GCC_except_table533
+ GCC_except_table545
+ GCC_except_table547
+ GCC_except_table550
+ GCC_except_table554
+ _AVMediaCharacteristicSignLanguageInterpretationForAccessibility
+ _AVMediaCharacteristicVisual
+ _CFPreferencesAppSynchronize
+ _CFPreferencesCopyAppValue
+ _CFPreferencesSetAppValue
+ _NSLocaleCountryCode
+ _OBJC_CLASS_$_TVPVideoOption
+ _OBJC_IVAR_$_TVPPlayer._cachedSelectedVideoOption
+ _OBJC_IVAR_$_TVPVideoOption._avMediaSelectionOption
+ _OBJC_IVAR_$_TVPVideoOption._isDefault
+ _OBJC_METACLASS_$_TVPVideoOption
+ _TVPSignLanguageCopyPreference
+ _TVPSignLanguageDefaultLanguageCode
+ _TVPSignLanguageDefaultLanguageCode.onceToken
+ _TVPSignLanguageDefaultLanguageCode.sDefaultLanguageCode
+ _TVPSignLanguagePreferredLanguage
+ _TVPSignLanguageSetPreferredLanguage
+ _TVPSignLanguageSetSettingEnabled
+ _TVPSignLanguageSettingEnabled
+ __OBJC_$_CATEGORY_AVMediaSelectionGroup_$_TVPSignLanguageAdditions
+ __OBJC_$_CATEGORY_CLASS_METHODS_AVMediaSelectionGroup_$_TVPSignLanguageAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_AVMediaSelectionGroup_$_TVPSignLanguageAdditions
+ __OBJC_$_INSTANCE_METHODS_TVPVideoOption
+ __OBJC_$_INSTANCE_VARIABLES_TVPVideoOption
+ __OBJC_$_PROP_LIST_AVMediaSelectionGroup_$_TVPSignLanguageAdditions
+ __OBJC_$_PROP_LIST_TVPVideoOption
+ __OBJC_CLASS_RO_$_TVPVideoOption
+ __OBJC_METACLASS_RO_$_TVPVideoOption
+ ___TVPSignLanguageDefaultLanguageCode_block_invoke
+ _objc_msgSend$_nextChapterInDirection:
+ _objc_msgSend$_updateVideoSelectionCriteria
+ _objc_msgSend$_updateVideoSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:
+ _objc_msgSend$assetCache
+ _objc_msgSend$cachedSelectedVideoOption
+ _objc_msgSend$defaultOption
+ _objc_msgSend$extendedLanguageCode
+ _objc_msgSend$initWithOption:isDefault:
+ _objc_msgSend$isDefault
+ _objc_msgSend$mediaSelectionOptionsInMediaSelectionGroup:
+ _objc_msgSend$selectedVideoOption
+ _objc_msgSend$setCachedSelectedVideoOption:
+ _objc_msgSend$setTvp_cachedVideoSelectionCriteria:
+ _objc_msgSend$tvp_cachedVideoSelectionCriteria
+ _objc_msgSend$tvp_signLanguageDownloadOption
+ _objc_msgSend$tvp_signLanguageOptionMatchingLanguage:inOptions:
+ _objc_msgSend$uppercaseString
- GCC_except_table134
- GCC_except_table234
- GCC_except_table240
- GCC_except_table244
- GCC_except_table247
- GCC_except_table295
- GCC_except_table325
- GCC_except_table335
- GCC_except_table357
- GCC_except_table361
- GCC_except_table370
- GCC_except_table381
- GCC_except_table400
- GCC_except_table407
- GCC_except_table410
- GCC_except_table411
- GCC_except_table413
- GCC_except_table414
- GCC_except_table417
- GCC_except_table420
- GCC_except_table432
- GCC_except_table441
- GCC_except_table446
- GCC_except_table448
- GCC_except_table450
- GCC_except_table475
- GCC_except_table477
- GCC_except_table479
- GCC_except_table482
- GCC_except_table488
- GCC_except_table495
- GCC_except_table497
- GCC_except_table499
- GCC_except_table504
- GCC_except_table508
- GCC_except_table514
- GCC_except_table525
- GCC_except_table537
- GCC_except_table539
- GCC_except_table542
- GCC_except_table546
CStrings:
+ "%@ isDefault: %@"
+ "GB"
+ "Performing automatic re-selection of video for player item %@ in player %@"
+ "PreferredSignLanguage"
+ "Replacing default media selection with sign-language selection for %@"
+ "Selected video option: %@"
+ "Selecting video media option: %@"
+ "Setting cached video option from active player item %@ to %@."
+ "Setting prefs for video language code to %@"
+ "Setting visual media selection criteria on %@ (is interstitial player: %@) to %@"
+ "SignLanguageEnabled"
+ "Unable to load visual media selection group due to error %@"
+ "Video selection option is nil, not selecting"
+ "Will perform automatic re-selection of video for player item %@ in player %@"
+ "ase"
+ "bfi"
+ "com.apple.videos-preferences"
+ "selectedVideoOption"
+ "videoOptions"
```
