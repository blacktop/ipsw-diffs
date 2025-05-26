## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-529.10.8.0.0
-  __TEXT.__text: 0x5fbf0
+529.20.11.0.0
+  __TEXT.__text: 0x616e4
   __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x5014
-  __TEXT.__const: 0x1d4
-  __TEXT.__cstring: 0x61cd
-  __TEXT.__oslogstring: 0x5980
-  __TEXT.__gcc_except_tab: 0x1570
-  __TEXT.__unwind_info: 0x1560
-  __TEXT.__objc_classname: 0x7ab
-  __TEXT.__objc_methname: 0x1208a
-  __TEXT.__objc_methtype: 0x2266
-  __TEXT.__objc_stubs: 0xad80
-  __DATA_CONST.__got: 0x470
+  __TEXT.__objc_methlist: 0x51ec
+  __TEXT.__const: 0x1e4
+  __TEXT.__cstring: 0x640c
+  __TEXT.__oslogstring: 0x5b81
+  __TEXT.__gcc_except_tab: 0x158c
+  __TEXT.__unwind_info: 0x1598
+  __TEXT.__objc_classname: 0x7c7
+  __TEXT.__objc_methname: 0x127f4
+  __TEXT.__objc_methtype: 0x22bd
+  __TEXT.__objc_stubs: 0xb040
+  __DATA_CONST.__got: 0x490
   __DATA_CONST.__const: 0x2390
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8bc0
-  __DATA_CONST.__objc_selrefs: 0x38e0
+  __DATA_CONST.__objc_const: 0x8f88
+  __DATA_CONST.__objc_selrefs: 0x3a18
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x64e0
+  __AUTH_CONST.__cfstring: 0x66e0
   __AUTH_CONST.__objc_intobj: 0x480
-  __AUTH_CONST.__objc_const: 0x1968
+  __AUTH_CONST.__objc_const: 0x19b0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x408
-  __AUTH.__objc_data: 0x8c0
+  __AUTH.__objc_data: 0x910
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x418
-  __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x74c
+  __DATA.__objc_classrefs: 0x428
+  __DATA.__objc_superrefs: 0x160
+  __DATA.__objc_ivar: 0x794
   __DATA.__data: 0x9d0
   __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0xa00

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2122
-  Symbols:   7850
-  CStrings:  4434
+  Functions: 2163
+  Symbols:   7984
+  CStrings:  4539
 
Symbols:
+ +[AVAsset(TVPAdditions) tvp_shouldIgnoreLoadFailureForKey:error:logObject:]
+ -[TVPAudioOption mediaCharacteristics]
+ -[TVPMediaItemLoader _promoInfoFromMetadata:keyIdentifierMap:forSkipKey:skipCounter:]
+ -[TVPMediaItemPromoInfo .cxx_destruct]
+ -[TVPMediaItemPromoInfo _calculateImageSize]
+ -[TVPMediaItemPromoInfo _loadImage]
+ -[TVPMediaItemPromoInfo addToUpNextLabelString]
+ -[TVPMediaItemPromoInfo addedToUpNextLabelString]
+ -[TVPMediaItemPromoInfo canonicalId]
+ -[TVPMediaItemPromoInfo expectedImageSize]
+ -[TVPMediaItemPromoInfo genre]
+ -[TVPMediaItemPromoInfo getTitleImageUsingCompletionHandler:]
+ -[TVPMediaItemPromoInfo imageCompletionHandler]
+ -[TVPMediaItemPromoInfo imageProxy]
+ -[TVPMediaItemPromoInfo initWithTitleImageURL:originalTitleImageWidth:originalTitleImageHeight:title:genre:ratingDisplayName:ratingSystem:canonicalId:isAddedToUpNext:addToUpNextLabelString:addedToUpNextLabelString:]
+ -[TVPMediaItemPromoInfo isAddedToUpNext]
+ -[TVPMediaItemPromoInfo maxImageHeight]
+ -[TVPMediaItemPromoInfo originalTitleImageHeight]
+ -[TVPMediaItemPromoInfo originalTitleImageWidth]
+ -[TVPMediaItemPromoInfo promoViewWidth]
+ -[TVPMediaItemPromoInfo ratingDisplayName]
+ -[TVPMediaItemPromoInfo ratingSystem]
+ -[TVPMediaItemPromoInfo setExpectedImageSize:]
+ -[TVPMediaItemPromoInfo setImageCompletionHandler:]
+ -[TVPMediaItemPromoInfo setImageProxy:]
+ -[TVPMediaItemPromoInfo setIsAddedToUpNext:]
+ -[TVPMediaItemPromoInfo setMaxImageHeight:]
+ -[TVPMediaItemPromoInfo setOriginalTitleImageHeight:]
+ -[TVPMediaItemPromoInfo setOriginalTitleImageWidth:]
+ -[TVPMediaItemPromoInfo setPromoViewWidth:]
+ -[TVPMediaItemPromoInfo setTitleImage:]
+ -[TVPMediaItemPromoInfo titleImageURLString]
+ -[TVPMediaItemPromoInfo titleImage]
+ -[TVPMediaItemPromoInfo title]
+ -[TVPMediaItemSkipInfo promoInfo]
+ -[TVPMediaItemSkipInfo setPromoInfo:]
+ -[TVPPlayer cachedElapsedCMTime]
+ -[TVPPlayer setCachedElapsedCMTime:]
+ -[TVPPlayer setReportingValueWithNumber:forKey:]
+ -[TVPPlayer setReportingValueWithString:forKey:]
+ GCC_except_table107
+ GCC_except_table113
+ GCC_except_table208
+ GCC_except_table212
+ GCC_except_table218
+ GCC_except_table286
+ GCC_except_table296
+ GCC_except_table319
+ GCC_except_table323
+ GCC_except_table332
+ GCC_except_table338
+ GCC_except_table357
+ GCC_except_table376
+ GCC_except_table377
+ GCC_except_table386
+ GCC_except_table390
+ GCC_except_table394
+ GCC_except_table399
+ GCC_except_table404
+ GCC_except_table406
+ GCC_except_table408
+ GCC_except_table433
+ GCC_except_table438
+ GCC_except_table444
+ GCC_except_table448
+ GCC_except_table452
+ GCC_except_table457
+ GCC_except_table461
+ GCC_except_table467
+ GCC_except_table478
+ GCC_except_table490
+ GCC_except_table495
+ GCC_except_table499
+ _AVErrorFailedDependenciesKey
+ _AVKitMetadataIdentifierApproximateEndDate
+ _AVKitMetadataIdentifierApproximateStartDate
+ _AVKitMetadataIdentifierLeagueName
+ _AVKitMetadataIdentifierProgramScheduledTime
+ _OBJC_CLASS_$_TVPMediaItemPromoInfo
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._addToUpNextLabelString
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._addedToUpNextLabelString
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._canonicalId
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._expectedImageSize
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._genre
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._imageCompletionHandler
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._imageProxy
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._isAddedToUpNext
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._maxImageHeight
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._originalTitleImageHeight
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._originalTitleImageWidth
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._promoViewWidth
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._ratingDisplayName
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._ratingSystem
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._title
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._titleImage
+ _OBJC_IVAR_$_TVPMediaItemPromoInfo._titleImageURLString
+ _OBJC_IVAR_$_TVPMediaItemSkipInfo._promoInfo
+ _OBJC_IVAR_$_TVPPlayer._cachedElapsedCMTime
+ _OBJC_METACLASS_$_TVPMediaItemPromoInfo
+ _TVPMediaItemMetadataLocalizedScheduledTimeString
+ __OBJC_$_INSTANCE_METHODS_TVPMediaItemPromoInfo
+ __OBJC_$_INSTANCE_VARIABLES_TVPMediaItemPromoInfo
+ __OBJC_$_PROP_LIST_TVPMediaItemPromoInfo
+ __OBJC_CLASS_RO_$_TVPMediaItemPromoInfo
+ __OBJC_METACLASS_RO_$_TVPMediaItemPromoInfo
+ ___35-[TVPMediaItemPromoInfo _loadImage]_block_invoke
+ ___35-[TVPMediaItemPromoInfo _loadImage]_block_invoke_2
+ ___37-[TVPMediaItemLoader _avAssetOptions]_block_invoke.248
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.720
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.723
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.736
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.738.cold.1
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.745
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.750
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.755
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.759
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.763
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.766
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.767
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.768
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.770
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.791
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.801
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.806
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.811
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.814
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.819
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.821
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.823
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.831
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.833
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.835
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.840
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.842
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.853
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.854
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.856
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.865
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.866
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.876
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.879
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.880
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.884
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.887
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.888
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.897
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.912
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.921
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.931
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.935
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.851
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.906
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.852
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.907
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_12.908
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_13.909
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_14.910
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_15.911
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.714
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.724
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.741
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.746
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.772
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.808
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.813
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.815
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.820
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.822
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.824
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.832
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.834
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.841
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.843
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.855
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.867
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.877
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.881
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.885
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.889
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.898
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.913
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.936
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.716
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.725
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.748
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.774
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.809
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.816
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.827
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.844
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.868
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.882
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.886
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.890
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.899
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.914
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.939
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.718
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.743
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.781
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.805
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.817
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.828
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.845
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.871
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.883
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.891
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.900
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.915
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.940
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.784
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.818
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.829
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.846
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.872
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.892
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.901
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.916
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.941
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.785
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.830
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.847
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.893
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.902
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.917
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.786
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.848
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.894
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.903
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.920
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.920.cold.1
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.920.cold.2
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.920.cold.3
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.920.cold.4
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.920.cold.5
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.788
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.849
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.895
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.904
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.789
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.850
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.896
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.905
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.160
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.163
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.167
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.174
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.183
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.190
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.161
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.177
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.184
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.193
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_3.179
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_3.185
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_4.186
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_5.189
+ ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_5.189.cold.1
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.452
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.454
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.455
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.463
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.456
+ ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.464
+ ___block_literal_global.188
+ ___block_literal_global.192
+ ___block_literal_global.245
+ ___block_literal_global.826
+ ___block_literal_global.919
+ _kFigStdAssetProperty_LocalizedMediaSelectionOptionDisplayNames
+ _objc_msgSend$_calculateImageSize
+ _objc_msgSend$_loadImage
+ _objc_msgSend$_promoInfoFromMetadata:keyIdentifierMap:forSkipKey:skipCounter:
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$cachedElapsedCMTime
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$imageCompletionHandler
+ _objc_msgSend$initWithTitleImageURL:originalTitleImageWidth:originalTitleImageHeight:title:genre:ratingDisplayName:ratingSystem:canonicalId:isAddedToUpNext:addToUpNextLabelString:addedToUpNextLabelString:
+ _objc_msgSend$maxImageHeight
+ _objc_msgSend$mediaCharacteristics
+ _objc_msgSend$originalTitleImageHeight
+ _objc_msgSend$originalTitleImageWidth
+ _objc_msgSend$promoViewWidth
+ _objc_msgSend$setCachedElapsedCMTime:
+ _objc_msgSend$setExpectedImageSize:
+ _objc_msgSend$setImageCompletionHandler:
+ _objc_msgSend$setImageProxy:
+ _objc_msgSend$setPromoInfo:
+ _objc_msgSend$setReportingValueWithNumber:forKey:
+ _objc_msgSend$setReportingValueWithString:forKey:
+ _objc_msgSend$setTitleImage:
+ _objc_msgSend$titleImage
+ _objc_msgSend$titleImageURLString
+ _objc_msgSend$tvp_shouldIgnoreLoadFailureForKey:error:logObject:
- -[TVPPlayer setCachedElapsedTime:]
- GCC_except_table106
- GCC_except_table112
- GCC_except_table202
- GCC_except_table209
- GCC_except_table215
- GCC_except_table283
- GCC_except_table293
- GCC_except_table316
- GCC_except_table320
- GCC_except_table329
- GCC_except_table335
- GCC_except_table354
- GCC_except_table361
- GCC_except_table362
- GCC_except_table380
- GCC_except_table387
- GCC_except_table391
- GCC_except_table396
- GCC_except_table401
- GCC_except_table403
- GCC_except_table405
- GCC_except_table430
- GCC_except_table432
- GCC_except_table441
- GCC_except_table445
- GCC_except_table449
- GCC_except_table454
- GCC_except_table458
- GCC_except_table464
- GCC_except_table472
- GCC_except_table487
- GCC_except_table489
- GCC_except_table496
- _AVURLAssetInheritURIQueryComponentFromReferencingURIKey
- _AVURLAssetOptimizeAccessForLinearMoviePlaybackKey
- _OBJC_IVAR_$_TVPPlayer._cachedElapsedTime
- _TVPMediaItemTraitOptimizeForLinearPlayback
- ___37-[TVPMediaItemLoader _avAssetOptions]_block_invoke.247
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.704
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.715
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.729
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.731
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.731.cold.1
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.739
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.743
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.747
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.748
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.752
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.756
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.757
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.761
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.785
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.795
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.800
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.805
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.808
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.813
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.815
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.817
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.825
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.827
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.829
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.830
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.834
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.847
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.848
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.850
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.859
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.860
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.867
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.870
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.872
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.874
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.881
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.882
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.891
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.906
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.915
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.925
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.929
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.845
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.900
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.846
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.901
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_12.902
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_13.903
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_14.904
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_15.905
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.706
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.716
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.735
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.740
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.766
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.796
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.807
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.809
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.814
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.816
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.818
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.826
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.828
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.831
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.835
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.849
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.861
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.871
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.875
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.879
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.883
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.892
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.907
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.930
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.708
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.717
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.736
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.768
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.797
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.810
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.821
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.832
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.862
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.876
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.880
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.884
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.893
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.908
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.933
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.710
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.737
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.775
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.799
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.811
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.822
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.833
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.865
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.877
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.885
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.894
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.909
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.934
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.778
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.812
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.823
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.840
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.866
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.886
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.895
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.910
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.935
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.779
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.824
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.841
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.887
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.896
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.911
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.780
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.842
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.888
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.897
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.914
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.914.cold.1
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.914.cold.2
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.914.cold.3
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.914.cold.4
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.914.cold.5
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.782
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.843
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.889
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.898
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.783
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.844
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.890
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.899
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.159
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.162
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.166
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.173
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.181
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke.189
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.160
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.176
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.183
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_2.192
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_3.178
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_3.184
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_4.185
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_5.188
- ___51-[TVPMediaItemLoader _registerStateMachineHandlers]_block_invoke_5.188.cold.1
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.415
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.417
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.418
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.426
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.419
- ___58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.427
- ___block_literal_global.187
- ___block_literal_global.191
- ___block_literal_global.244
- ___block_literal_global.820
- ___block_literal_global.913
- _objc_msgSend$cachedElapsedTime
- _objc_msgSend$setCachedElapsedTime:
- _objc_msgSend$setWillNeverSeekBackwardsHint:
CStrings:
+ "\x11)!"
+ "@\"TVPMediaItemPromoInfo\""
+ "@100@0:8@16d24d32@40@48@56@64@72B80@84@92"
+ "@48@0:8@16@24@32Q40"
+ "AVAssetKeysForWhichToIgnoreFailures"
+ "C"
+ "ExactEndTimeOverrideInMS"
+ "ExactStartTimeOverrideInMS"
+ "Ignoring failure of key %@ due to non-fatal failure to load localized media selection names: %@"
+ "Ignoring failure of key %@ due to user defaults"
+ "Not setting approximate end date because none was provided"
+ "Not setting approximate start date because none was provided"
+ "Overriding exact end time with date %@"
+ "Overriding exact start time with date %@"
+ "Setting approximate end date %@ with seekable end date %@"
+ "Setting approximate start date %@ with seekable start date %@"
+ "Setting reporting value %@ for key %@; player %@"
+ "T@\"NSString\",R,N,V_addToUpNextLabelString"
+ "T@\"NSString\",R,N,V_addedToUpNextLabelString"
+ "T@\"NSString\",R,N,V_canonicalId"
+ "T@\"NSString\",R,N,V_genre"
+ "T@\"NSString\",R,N,V_ratingDisplayName"
+ "T@\"NSString\",R,N,V_ratingSystem"
+ "T@\"NSString\",R,N,V_title"
+ "T@\"NSString\",R,N,V_titleImageURLString"
+ "T@\"TVImageProxy\",&,N,V_imageProxy"
+ "T@\"TVPMediaItemPromoInfo\",&,N,V_promoInfo"
+ "T@\"UIImage\",&,N,V_titleImage"
+ "T@?,C,N,V_imageCompletionHandler"
+ "TB,N,V_isAddedToUpNext"
+ "TVPMediaItemMetadataLocalizedScheduledTimeString"
+ "TVPMediaItemPromoInfo"
+ "Td,N,V_maxImageHeight"
+ "Td,N,V_originalTitleImageHeight"
+ "Td,N,V_originalTitleImageWidth"
+ "Td,N,V_promoViewWidth"
+ "T{?=qiIq},N,V_cachedElapsedCMTime"
+ "T{CGSize=dd},N,V_expectedImageSize"
+ "_addToUpNextLabelString"
+ "_addedToUpNextLabelString"
+ "_cachedElapsedCMTime"
+ "_calculateImageSize"
+ "_canonicalId"
+ "_expectedImageSize"
+ "_genre"
+ "_imageCompletionHandler"
+ "_imageProxy"
+ "_isAddedToUpNext"
+ "_loadImage"
+ "_maxImageHeight"
+ "_originalTitleImageHeight"
+ "_originalTitleImageWidth"
+ "_promoInfo"
+ "_promoInfoFromMetadata:keyIdentifierMap:forSkipKey:skipCounter:"
+ "_promoViewWidth"
+ "_ratingDisplayName"
+ "_ratingSystem"
+ "_titleImage"
+ "_titleImageURLString"
+ "addToUpNextLabelString"
+ "addedToUpNextLabelString"
+ "arrayForKey:"
+ "cachedElapsedCMTime"
+ "canonicalId"
+ "com.apple.hls.%@.%lu.promo.canonical-id"
+ "com.apple.hls.%@.%lu.promo.enabled"
+ "com.apple.hls.%@.%lu.promo.genre"
+ "com.apple.hls.%@.%lu.promo.image"
+ "com.apple.hls.%@.%lu.promo.image-height"
+ "com.apple.hls.%@.%lu.promo.image-width"
+ "com.apple.hls.%@.%lu.promo.rating-display-name"
+ "com.apple.hls.%@.%lu.promo.rating-system"
+ "com.apple.hls.%@.%lu.promo.title"
+ "com.apple.hls.%@.%lu.promo.up-next.add-label"
+ "com.apple.hls.%@.%lu.promo.up-next.added-label"
+ "com.apple.hls.%@.%lu.promo.up-next.is-added"
+ "dateWithTimeIntervalSince1970:"
+ "doubleForKey:"
+ "expectedImageSize"
+ "genre"
+ "getTitleImageUsingCompletionHandler:"
+ "imageCompletionHandler"
+ "imageProxy"
+ "initWithTitleImageURL:originalTitleImageWidth:originalTitleImageHeight:title:genre:ratingDisplayName:ratingSystem:canonicalId:isAddedToUpNext:addToUpNextLabelString:addedToUpNextLabelString:"
+ "isAddedToUpNext"
+ "maxImageHeight"
+ "mediaCharacteristics"
+ "originalTitleImageHeight"
+ "originalTitleImageWidth"
+ "png"
+ "promoInfo"
+ "promoViewWidth"
+ "ratingDisplayName"
+ "ratingSystem"
+ "setCachedElapsedCMTime:"
+ "setExpectedImageSize:"
+ "setImageCompletionHandler:"
+ "setImageProxy:"
+ "setIsAddedToUpNext:"
+ "setMaxImageHeight:"
+ "setOriginalTitleImageHeight:"
+ "setOriginalTitleImageWidth:"
+ "setPromoInfo:"
+ "setPromoViewWidth:"
+ "setReportingValueWithNumber:forKey:"
+ "setReportingValueWithString:forKey:"
+ "setTitleImage:"
+ "titleImage"
+ "titleImageURLString"
+ "tvp_shouldIgnoreLoadFailureForKey:error:logObject:"
- "TVPMediaItemTraitOptimizeForLinearPlayback"
- "T{?=qiIq},N,V_cachedElapsedTime"
- "_cachedElapsedTime"
- "setCachedElapsedTime:"
- "setWillNeverSeekBackwardsHint:"

```
