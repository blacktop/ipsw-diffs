## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-916.51.202.0.0
-  __TEXT.__text: 0x2d88a0
-  __TEXT.__objc_methlist: 0x271fc
+916.57.151.0.0
+  __TEXT.__text: 0x2de614
+  __TEXT.__objc_methlist: 0x275dc
   __TEXT.__const: 0x1868
   __TEXT.__dlopen_cstrs: 0x280
   __TEXT.__constg_swiftt: 0x660

   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift5_types: 0x40
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__cstring: 0x33c05
+  __TEXT.__cstring: 0x3489e
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__oslogstring: 0x250b6
+  __TEXT.__oslogstring: 0x2590d
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x9804
+  __TEXT.__gcc_except_tab: 0x9a38
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xbb58
+  __TEXT.__unwind_info: 0xbc98
   __TEXT.__eh_frame: 0x4d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9140
-  __DATA_CONST.__objc_classlist: 0xf60
+  __DATA_CONST.__const: 0x9240
+  __DATA_CONST.__objc_classlist: 0xf80
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14aa0
+  __DATA_CONST.__objc_selrefs: 0x14cb8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xc78
-  __DATA_CONST.__objc_arraydata: 0x940
-  __DATA_CONST.__got: 0x2ac0
+  __DATA_CONST.__objc_superrefs: 0xc98
+  __DATA_CONST.__objc_arraydata: 0x970
+  __DATA_CONST.__got: 0x2b18
   __AUTH_CONST.__const: 0x4770
-  __AUTH_CONST.__cfstring: 0x2db40
-  __AUTH_CONST.__objc_const: 0x42d70
-  __AUTH_CONST.__objc_intobj: 0x2508
-  __AUTH_CONST.__objc_arrayobj: 0x7b0
+  __AUTH_CONST.__cfstring: 0x2e3a0
+  __AUTH_CONST.__objc_const: 0x43448
+  __AUTH_CONST.__objc_intobj: 0x2550
+  __AUTH_CONST.__objc_arrayobj: 0x7c8
   __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x1948
-  __AUTH.__objc_data: 0x78e8
+  __AUTH.__objc_data: 0x7a28
   __AUTH.__data: 0x3c0
-  __DATA.__objc_ivar: 0x3670
+  __DATA.__objc_ivar: 0x36c8
   __DATA.__data: 0x2c28
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x55

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15116
-  Symbols:   26211
-  CStrings:  9004
+  Functions: 15209
+  Symbols:   26371
+  CStrings:  9120
 
Symbols:
+ +[PHAmbientPosterBundle _compressBundleAtURL:error:]
+ +[PHAmbientPosterBundle _decompressBundleArchiveAtURL:error:]
+ +[PHAmbientPosterBundle bundleWithURL:error:]
+ +[PHAmbientPosterConfiguration ambientPosterConfigurationFromURL:error:]
+ +[PHAmbientPosterConfiguration ambientPosterConfigurationWithContentsOfURL:error:]
+ +[PHAmbientPosterConfiguration applyConfigurationAtURL:toPhotoLibrary:error:]
+ +[PHAmbientPosterConfiguration supportsSecureCoding]
+ +[PHAmbientPosterSelection posterSelectionFromData:error:]
+ +[PHAmbientPosterSelection supportsSecureCoding]
+ +[PHAsset fetchAllPebblePlaceholderAssetsExcludingAssetsWithIdentifiers:options:]
+ +[PHAsset fetchPebblePlaceholderAssetsWithIdentifiers:options:]
+ +[PHAssetResource(Private) _isMediaAssetResource:]
+ +[PHAssetResource(Private) _masterThumbnailAssetResourceForAsset:]
+ +[PHAssetResource(Private) assetResourcesForOsMigrationForAsset:]
+ +[PHImportAmbientPosterSource _isValidBundle:error:]
+ -[PHAmbientPosterBundle .cxx_destruct]
+ -[PHAmbientPosterBundle configuration]
+ -[PHAmbientPosterBundle description]
+ -[PHAmbientPosterBundle ingestResourcesIntoPhotoLibrary:error:]
+ -[PHAmbientPosterBundle initWithBundleURL:]
+ -[PHAmbientPosterBundle initWithConfiguration:]
+ -[PHAmbientPosterBundle resourceURLs]
+ -[PHAmbientPosterBundle url]
+ -[PHAmbientPosterBundle writeToDestinationFolderURL:photoLibrary:compress:assetBundleHandler:error:]
+ -[PHAmbientPosterConfiguration .cxx_destruct]
+ -[PHAmbientPosterConfiguration coldStartAssetLocalIdentifiers]
+ -[PHAmbientPosterConfiguration description]
+ -[PHAmbientPosterConfiguration encodeWithCoder:]
+ -[PHAmbientPosterConfiguration initWithCoder:]
+ -[PHAmbientPosterConfiguration initWithPosterSelection:posterType:coldStartAssetLocalIdentifiers:]
+ -[PHAmbientPosterConfiguration initWithPosterSelection:posterType:coldStartAssetLocalIdentifiers:version:]
+ -[PHAmbientPosterConfiguration posterSelection]
+ -[PHAmbientPosterConfiguration posterType]
+ -[PHAmbientPosterConfiguration saveForPhotoLibrary:coldStartAssetHandler:error:]
+ -[PHAmbientPosterConfiguration saveForPhotoLibrary:compress:coldStartAssetHandler:error:]
+ -[PHAmbientPosterConfiguration setColdStartAssetLocalIdentifiers:]
+ -[PHAmbientPosterConfiguration version]
+ -[PHAmbientPosterConfiguration writeToDestinationFolderURL:error:]
+ -[PHAmbientPosterSelection .cxx_destruct]
+ -[PHAmbientPosterSelection assetCloudIdentifiers]
+ -[PHAmbientPosterSelection assetCollectionCloudIdentifiers]
+ -[PHAmbientPosterSelection description]
+ -[PHAmbientPosterSelection encodeToData:]
+ -[PHAmbientPosterSelection encodeWithCoder:]
+ -[PHAmbientPosterSelection frequency]
+ -[PHAmbientPosterSelection hash]
+ -[PHAmbientPosterSelection initWithAssetCloudIdentifiers:frequency:]
+ -[PHAmbientPosterSelection initWithCoder:]
+ -[PHAmbientPosterSelection initWithMemoryType:memoryTitle:memorySubtitle:]
+ -[PHAmbientPosterSelection initWithSharedAlbumCloudIdentifiers:]
+ -[PHAmbientPosterSelection initWithSmartAlbumSubtypes:assetCollectionCloudIdentifiers:sharedAlbumCloudIdentifiers:peopleCloudIdentifiers:socialGroupCloudIdentifiers:frequency:]
+ -[PHAmbientPosterSelection initWithSmartAlbums:memoryType:frequency:mode:memoryTitle:memorySubtitle:smartAlbumSubtypes:assetCollectionCloudIdentifiers:peopleCloudIdentifiers:socialGroupCloudIdentifiers:assetCloudIdentifiers:sharedAlbumCloudIdentifiers:]
+ -[PHAmbientPosterSelection initWithSmartAlbums:peopleCloudIdentifiers:frequency:]
+ -[PHAmbientPosterSelection init]
+ -[PHAmbientPosterSelection isEqual:]
+ -[PHAmbientPosterSelection memorySubtitle]
+ -[PHAmbientPosterSelection memoryTitle]
+ -[PHAmbientPosterSelection memoryType]
+ -[PHAmbientPosterSelection mode]
+ -[PHAmbientPosterSelection peopleCloudIdentifiers]
+ -[PHAmbientPosterSelection setMode:]
+ -[PHAmbientPosterSelection sharedAlbumCloudIdentifiers]
+ -[PHAmbientPosterSelection smartAlbumSubtypes]
+ -[PHAmbientPosterSelection smartAlbums]
+ -[PHAmbientPosterSelection socialGroupCloudIdentifiers]
+ -[PHFetchOptions includePebblePlaceholderAssets]
+ -[PHFetchOptions setIncludePebblePlaceholderAssets:]
+ -[PHImportAmbientPosterSource .cxx_destruct]
+ -[PHImportAmbientPosterSource assetsByProcessingItem:]
+ -[PHImportAmbientPosterSource beginProcessingWithCompletion:]
+ -[PHImportAmbientPosterSource initWithBundle:]
+ -[PHImportAmbientPosterSource name]
+ -[PHImportAmbientPosterSource productKind]
+ -[PHPersonChangeRequest verifyBySelectingInPicker]
+ -[PHPhotoLibrary(OsMigration) _assetBytesForOsMigration]
+ -[PHPhotoLibrary(OsMigration) _thumbnailOnlyAssetBytesForOsMigrationWithGroupedResults:]
+ -[PHPhotoLibrary(OsMigration) estimatedLibrarySizeForOsMigration]
+ -[PHSocialGroupChangeRequest verifyBySelectingInPicker]
+ GCC_except_table10005
+ GCC_except_table10007
+ GCC_except_table10098
+ GCC_except_table10189
+ GCC_except_table10311
+ GCC_except_table10321
+ GCC_except_table10443
+ GCC_except_table10444
+ GCC_except_table10445
+ GCC_except_table10446
+ GCC_except_table10447
+ GCC_except_table10448
+ GCC_except_table10449
+ GCC_except_table10450
+ GCC_except_table10451
+ GCC_except_table10452
+ GCC_except_table10453
+ GCC_except_table10454
+ GCC_except_table10455
+ GCC_except_table10456
+ GCC_except_table10457
+ GCC_except_table10458
+ GCC_except_table10459
+ GCC_except_table10460
+ GCC_except_table10461
+ GCC_except_table10462
+ GCC_except_table10463
+ GCC_except_table10464
+ GCC_except_table10465
+ GCC_except_table10466
+ GCC_except_table10467
+ GCC_except_table10468
+ GCC_except_table10469
+ GCC_except_table10470
+ GCC_except_table10471
+ GCC_except_table10472
+ GCC_except_table10473
+ GCC_except_table10474
+ GCC_except_table10475
+ GCC_except_table10476
+ GCC_except_table10477
+ GCC_except_table10478
+ GCC_except_table10479
+ GCC_except_table10480
+ GCC_except_table10481
+ GCC_except_table10482
+ GCC_except_table10483
+ GCC_except_table10484
+ GCC_except_table10485
+ GCC_except_table10486
+ GCC_except_table10487
+ GCC_except_table10598
+ GCC_except_table10607
+ GCC_except_table10608
+ GCC_except_table10609
+ GCC_except_table10610
+ GCC_except_table10611
+ GCC_except_table10612
+ GCC_except_table10613
+ GCC_except_table10624
+ GCC_except_table10642
+ GCC_except_table10675
+ GCC_except_table10676
+ GCC_except_table10677
+ GCC_except_table10678
+ GCC_except_table10679
+ GCC_except_table10689
+ GCC_except_table10707
+ GCC_except_table10710
+ GCC_except_table10711
+ GCC_except_table10712
+ GCC_except_table10714
+ GCC_except_table10715
+ GCC_except_table10716
+ GCC_except_table10753
+ GCC_except_table10754
+ GCC_except_table10758
+ GCC_except_table10778
+ GCC_except_table10783
+ GCC_except_table10865
+ GCC_except_table10958
+ GCC_except_table11126
+ GCC_except_table11145
+ GCC_except_table11148
+ GCC_except_table11149
+ GCC_except_table11175
+ GCC_except_table11177
+ GCC_except_table11267
+ GCC_except_table11295
+ GCC_except_table11432
+ GCC_except_table11436
+ GCC_except_table11836
+ GCC_except_table11993
+ GCC_except_table11996
+ GCC_except_table12002
+ GCC_except_table12010
+ GCC_except_table12014
+ GCC_except_table12016
+ GCC_except_table12020
+ GCC_except_table12026
+ GCC_except_table12132
+ GCC_except_table12152
+ GCC_except_table12154
+ GCC_except_table12156
+ GCC_except_table12158
+ GCC_except_table12193
+ GCC_except_table12242
+ GCC_except_table12249
+ GCC_except_table12251
+ GCC_except_table12253
+ GCC_except_table12259
+ GCC_except_table12296
+ GCC_except_table12427
+ GCC_except_table12453
+ GCC_except_table12465
+ GCC_except_table12507
+ GCC_except_table12509
+ GCC_except_table12522
+ GCC_except_table12627
+ GCC_except_table12631
+ GCC_except_table12672
+ GCC_except_table12676
+ GCC_except_table12685
+ GCC_except_table12693
+ GCC_except_table12731
+ GCC_except_table12738
+ GCC_except_table12770
+ GCC_except_table12775
+ GCC_except_table12825
+ GCC_except_table12917
+ GCC_except_table12920
+ GCC_except_table12928
+ GCC_except_table12968
+ GCC_except_table12987
+ GCC_except_table12998
+ GCC_except_table13060
+ GCC_except_table13063
+ GCC_except_table13071
+ GCC_except_table13077
+ GCC_except_table13079
+ GCC_except_table13144
+ GCC_except_table13222
+ GCC_except_table13226
+ GCC_except_table13230
+ GCC_except_table13268
+ GCC_except_table13293
+ GCC_except_table13300
+ GCC_except_table13370
+ GCC_except_table13374
+ GCC_except_table13376
+ GCC_except_table13460
+ GCC_except_table13473
+ GCC_except_table13567
+ GCC_except_table13634
+ GCC_except_table13840
+ GCC_except_table13919
+ GCC_except_table13961
+ GCC_except_table14010
+ GCC_except_table14020
+ GCC_except_table14040
+ GCC_except_table14055
+ GCC_except_table14083
+ GCC_except_table14085
+ GCC_except_table14098
+ GCC_except_table14100
+ GCC_except_table14102
+ GCC_except_table14121
+ GCC_except_table14267
+ GCC_except_table14278
+ GCC_except_table14305
+ GCC_except_table14311
+ GCC_except_table14327
+ GCC_except_table14397
+ GCC_except_table14399
+ GCC_except_table14445
+ GCC_except_table14447
+ GCC_except_table14474
+ GCC_except_table14478
+ GCC_except_table14479
+ GCC_except_table14491
+ GCC_except_table14508
+ GCC_except_table14511
+ GCC_except_table14665
+ GCC_except_table4948
+ GCC_except_table4958
+ GCC_except_table5022
+ GCC_except_table5028
+ GCC_except_table5031
+ GCC_except_table5101
+ GCC_except_table5106
+ GCC_except_table5136
+ GCC_except_table5266
+ GCC_except_table5270
+ GCC_except_table5627
+ GCC_except_table5656
+ GCC_except_table5663
+ GCC_except_table5710
+ GCC_except_table5741
+ GCC_except_table5753
+ GCC_except_table5755
+ GCC_except_table5781
+ GCC_except_table5786
+ GCC_except_table5789
+ GCC_except_table5791
+ GCC_except_table5798
+ GCC_except_table5807
+ GCC_except_table5811
+ GCC_except_table5820
+ GCC_except_table5824
+ GCC_except_table5863
+ GCC_except_table5896
+ GCC_except_table5922
+ GCC_except_table5926
+ GCC_except_table5930
+ GCC_except_table5952
+ GCC_except_table5960
+ GCC_except_table5980
+ GCC_except_table6003
+ GCC_except_table6053
+ GCC_except_table6062
+ GCC_except_table6104
+ GCC_except_table6139
+ GCC_except_table6145
+ GCC_except_table6149
+ GCC_except_table6160
+ GCC_except_table6191
+ GCC_except_table6220
+ GCC_except_table6247
+ GCC_except_table6249
+ GCC_except_table6263
+ GCC_except_table6333
+ GCC_except_table6411
+ GCC_except_table6416
+ GCC_except_table6421
+ GCC_except_table6582
+ GCC_except_table6596
+ GCC_except_table6621
+ GCC_except_table6634
+ GCC_except_table6673
+ GCC_except_table6710
+ GCC_except_table6712
+ GCC_except_table7112
+ GCC_except_table7132
+ GCC_except_table7145
+ GCC_except_table7158
+ GCC_except_table7177
+ GCC_except_table7211
+ GCC_except_table7213
+ GCC_except_table7215
+ GCC_except_table7217
+ GCC_except_table7226
+ GCC_except_table7275
+ GCC_except_table7289
+ GCC_except_table7327
+ GCC_except_table7329
+ GCC_except_table7368
+ GCC_except_table7661
+ GCC_except_table7664
+ GCC_except_table7686
+ GCC_except_table7693
+ GCC_except_table7709
+ GCC_except_table7711
+ GCC_except_table7712
+ GCC_except_table7713
+ GCC_except_table7714
+ GCC_except_table7715
+ GCC_except_table7716
+ GCC_except_table7727
+ GCC_except_table7728
+ GCC_except_table7729
+ GCC_except_table7886
+ GCC_except_table8151
+ GCC_except_table8169
+ GCC_except_table8170
+ GCC_except_table8230
+ GCC_except_table8252
+ GCC_except_table8256
+ GCC_except_table8263
+ GCC_except_table8317
+ GCC_except_table8523
+ GCC_except_table8525
+ GCC_except_table8572
+ GCC_except_table8612
+ GCC_except_table8616
+ GCC_except_table8618
+ GCC_except_table8620
+ GCC_except_table8637
+ GCC_except_table8677
+ GCC_except_table8705
+ GCC_except_table8747
+ GCC_except_table8841
+ GCC_except_table8899
+ GCC_except_table8919
+ GCC_except_table8922
+ GCC_except_table8941
+ GCC_except_table9000
+ GCC_except_table9004
+ GCC_except_table9008
+ GCC_except_table9009
+ GCC_except_table9011
+ GCC_except_table9012
+ GCC_except_table9014
+ GCC_except_table9016
+ GCC_except_table9020
+ GCC_except_table9031
+ GCC_except_table9034
+ GCC_except_table9055
+ GCC_except_table9099
+ GCC_except_table9166
+ GCC_except_table9323
+ GCC_except_table9364
+ GCC_except_table9370
+ GCC_except_table9373
+ GCC_except_table9633
+ GCC_except_table9637
+ GCC_except_table9641
+ GCC_except_table9661
+ GCC_except_table9662
+ GCC_except_table9758
+ GCC_except_table9768
+ GCC_except_table9801
+ GCC_except_table9898
+ GCC_except_table9918
+ GCC_except_table9944
+ GCC_except_table9972
+ _OBJC_CLASS_$_PFAmbientPosterData
+ _OBJC_CLASS_$_PFAppleArchive
+ _OBJC_CLASS_$_PHAmbientPosterBundle
+ _OBJC_CLASS_$_PHAmbientPosterConfiguration
+ _OBJC_CLASS_$_PHAmbientPosterSelection
+ _OBJC_CLASS_$_PHImportAmbientPosterSource
+ _OBJC_CLASS_$_PLFileBackedThumbnailVirtualResource
+ _OBJC_IVAR_$_PHAmbientPosterBundle._configuration
+ _OBJC_IVAR_$_PHAmbientPosterBundle._resourceURLs
+ _OBJC_IVAR_$_PHAmbientPosterBundle._url
+ _OBJC_IVAR_$_PHAmbientPosterConfiguration._coldStartAssetLocalIdentifiers
+ _OBJC_IVAR_$_PHAmbientPosterConfiguration._posterSelection
+ _OBJC_IVAR_$_PHAmbientPosterConfiguration._posterType
+ _OBJC_IVAR_$_PHAmbientPosterConfiguration._version
+ _OBJC_IVAR_$_PHAmbientPosterSelection._assetCloudIdentifiers
+ _OBJC_IVAR_$_PHAmbientPosterSelection._assetCollectionCloudIdentifiers
+ _OBJC_IVAR_$_PHAmbientPosterSelection._frequency
+ _OBJC_IVAR_$_PHAmbientPosterSelection._memorySubtitle
+ _OBJC_IVAR_$_PHAmbientPosterSelection._memoryTitle
+ _OBJC_IVAR_$_PHAmbientPosterSelection._memoryType
+ _OBJC_IVAR_$_PHAmbientPosterSelection._mode
+ _OBJC_IVAR_$_PHAmbientPosterSelection._peopleCloudIdentifiers
+ _OBJC_IVAR_$_PHAmbientPosterSelection._sharedAlbumCloudIdentifiers
+ _OBJC_IVAR_$_PHAmbientPosterSelection._smartAlbumSubtypes
+ _OBJC_IVAR_$_PHAmbientPosterSelection._smartAlbums
+ _OBJC_IVAR_$_PHAmbientPosterSelection._socialGroupCloudIdentifiers
+ _OBJC_IVAR_$_PHFetchOptions._includePebblePlaceholderAssetsNumber
+ _OBJC_IVAR_$_PHImportAmbientPosterSource._bundle
+ _OBJC_IVAR_$_PHSocialGroupChangeRequest._verifyBySelectingInPicker
+ _OBJC_METACLASS_$_PHAmbientPosterBundle
+ _OBJC_METACLASS_$_PHAmbientPosterConfiguration
+ _OBJC_METACLASS_$_PHAmbientPosterSelection
+ _OBJC_METACLASS_$_PHImportAmbientPosterSource
+ _PFAppleArchiveExtension
+ _PFAssetBundlePathAmbientPosterDataKey
+ _PFAssetBundlePathSegmentationDataKey
+ _PHAmbientPosterMemoryTypeDescription
+ _PHAmbientPosterModeDescription
+ _PHAmbientPosterShuffleFrequencyDescription
+ _PHAmbientPosterShuffleSmartAlbumsDescription
+ _PHAmbientPosterTypeDescription
+ _UTTypeAudio
+ __OBJC_$_CLASS_METHODS_PHAmbientPosterBundle
+ __OBJC_$_CLASS_METHODS_PHAmbientPosterConfiguration
+ __OBJC_$_CLASS_METHODS_PHAmbientPosterSelection
+ __OBJC_$_CLASS_METHODS_PHImportAmbientPosterSource
+ __OBJC_$_CLASS_METHODS_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|ContentProvenance|OsMigration|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
+ __OBJC_$_CLASS_PROP_LIST_PHAmbientPosterConfiguration
+ __OBJC_$_CLASS_PROP_LIST_PHAmbientPosterSelection
+ __OBJC_$_INSTANCE_METHODS_PHAmbientPosterBundle
+ __OBJC_$_INSTANCE_METHODS_PHAmbientPosterConfiguration
+ __OBJC_$_INSTANCE_METHODS_PHAmbientPosterSelection
+ __OBJC_$_INSTANCE_METHODS_PHImportAmbientPosterSource
+ __OBJC_$_INSTANCE_METHODS_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|ContentProvenance|OsMigration|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
+ __OBJC_$_INSTANCE_VARIABLES_PHAmbientPosterBundle
+ __OBJC_$_INSTANCE_VARIABLES_PHAmbientPosterConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_PHAmbientPosterSelection
+ __OBJC_$_INSTANCE_VARIABLES_PHImportAmbientPosterSource
+ __OBJC_$_PROP_LIST_PHAmbientPosterBundle
+ __OBJC_$_PROP_LIST_PHAmbientPosterConfiguration
+ __OBJC_$_PROP_LIST_PHAmbientPosterSelection
+ __OBJC_CLASS_PROTOCOLS_$_PHAmbientPosterConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_PHAmbientPosterSelection
+ __OBJC_CLASS_PROTOCOLS_$_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|ContentProvenance|OsMigration|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
+ __OBJC_CLASS_RO_$_PHAmbientPosterBundle
+ __OBJC_CLASS_RO_$_PHAmbientPosterConfiguration
+ __OBJC_CLASS_RO_$_PHAmbientPosterSelection
+ __OBJC_CLASS_RO_$_PHImportAmbientPosterSource
+ __OBJC_METACLASS_RO_$_PHAmbientPosterBundle
+ __OBJC_METACLASS_RO_$_PHAmbientPosterConfiguration
+ __OBJC_METACLASS_RO_$_PHAmbientPosterSelection
+ __OBJC_METACLASS_RO_$_PHImportAmbientPosterSource
+ ___100-[PHAmbientPosterBundle writeToDestinationFolderURL:photoLibrary:compress:assetBundleHandler:error:]_block_invoke
+ ___37-[PHAmbientPosterBundle resourceURLs]_block_invoke
+ ___56-[PHPhotoLibrary(OsMigration) _assetBytesForOsMigration]_block_invoke
+ ___63-[PHAmbientPosterBundle ingestResourcesIntoPhotoLibrary:error:]_block_invoke
+ ___63-[PHAmbientPosterBundle ingestResourcesIntoPhotoLibrary:error:]_block_invoke_2
+ ___66+[PHAssetResource(Private) _masterThumbnailAssetResourceForAsset:]_block_invoke
+ ___88-[PHPhotoLibrary(OsMigration) _thumbnailOnlyAssetBytesForOsMigrationWithGroupedResults:]_block_invoke
+ ___89-[PHAmbientPosterConfiguration saveForPhotoLibrary:compress:coldStartAssetHandler:error:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e35_v24?0"PHAsset"8"PFAssetBundle"16ls32l8
+ ___block_descriptor_40_e8_32r_e27_B24?0"NSURL"8"NSError"16lr32l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e34_v24?0"UIImage"8"NSDictionary"16ls48l8s32l8s40l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r_e25_v16?0"PHImportResults"8ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r_e29_v24?0"NSArray"8"NSArray"16ls32l8s40l8s48l8r64l8s56l8
+ _additionalPropertiesToFetchOnPrimaryObject.pl_once_object_55
+ _additionalPropertiesToFetchOnPrimaryObject.pl_once_object_68
+ _additionalPropertiesToFetchOnPrimaryObject.pl_once_token_55
+ _additionalPropertiesToFetchOnPrimaryObject.pl_once_token_68
+ _propertiesToFetch.pl_once_object_50
+ _propertiesToFetch.pl_once_object_54
+ _propertiesToFetch.pl_once_object_67
+ _propertiesToFetch.pl_once_object_74
+ _propertiesToFetch.pl_once_token_50
+ _propertiesToFetch.pl_once_token_54
+ _propertiesToFetch.pl_once_token_67
+ _propertiesToFetch.pl_once_token_74
- -[PHPhotoLibrary _assetBytesForOsMigration]
- -[PHPhotoLibrary estimatedLibrarySizeForOsMigration]
- GCC_except_table10053
- GCC_except_table10144
- GCC_except_table10266
- GCC_except_table10276
- GCC_except_table10290
- GCC_except_table10291
- GCC_except_table10298
- GCC_except_table10301
- GCC_except_table10324
- GCC_except_table10325
- GCC_except_table10326
- GCC_except_table10327
- GCC_except_table10328
- GCC_except_table10329
- GCC_except_table10330
- GCC_except_table10331
- GCC_except_table10334
- GCC_except_table10337
- GCC_except_table10338
- GCC_except_table10339
- GCC_except_table10340
- GCC_except_table10341
- GCC_except_table10344
- GCC_except_table10345
- GCC_except_table10347
- GCC_except_table10348
- GCC_except_table10349
- GCC_except_table10350
- GCC_except_table10351
- GCC_except_table10352
- GCC_except_table10353
- GCC_except_table10354
- GCC_except_table10355
- GCC_except_table10356
- GCC_except_table10358
- GCC_except_table10359
- GCC_except_table10360
- GCC_except_table10361
- GCC_except_table10362
- GCC_except_table10363
- GCC_except_table10364
- GCC_except_table10365
- GCC_except_table10366
- GCC_except_table10368
- GCC_except_table10377
- GCC_except_table10378
- GCC_except_table10387
- GCC_except_table10402
- GCC_except_table10412
- GCC_except_table10553
- GCC_except_table10562
- GCC_except_table10563
- GCC_except_table10564
- GCC_except_table10565
- GCC_except_table10566
- GCC_except_table10567
- GCC_except_table10568
- GCC_except_table10579
- GCC_except_table10597
- GCC_except_table10630
- GCC_except_table10631
- GCC_except_table10632
- GCC_except_table10633
- GCC_except_table10634
- GCC_except_table10644
- GCC_except_table10662
- GCC_except_table10663
- GCC_except_table10664
- GCC_except_table10665
- GCC_except_table10666
- GCC_except_table10667
- GCC_except_table10668
- GCC_except_table10669
- GCC_except_table10670
- GCC_except_table10671
- GCC_except_table10733
- GCC_except_table10738
- GCC_except_table10820
- GCC_except_table10913
- GCC_except_table11081
- GCC_except_table11100
- GCC_except_table11103
- GCC_except_table11104
- GCC_except_table11130
- GCC_except_table11132
- GCC_except_table11222
- GCC_except_table11250
- GCC_except_table11784
- GCC_except_table11941
- GCC_except_table11944
- GCC_except_table11950
- GCC_except_table11958
- GCC_except_table11962
- GCC_except_table11964
- GCC_except_table11968
- GCC_except_table11974
- GCC_except_table12080
- GCC_except_table12100
- GCC_except_table12102
- GCC_except_table12104
- GCC_except_table12106
- GCC_except_table12141
- GCC_except_table12190
- GCC_except_table12197
- GCC_except_table12199
- GCC_except_table12201
- GCC_except_table12207
- GCC_except_table12244
- GCC_except_table12375
- GCC_except_table12401
- GCC_except_table12413
- GCC_except_table12455
- GCC_except_table12457
- GCC_except_table12470
- GCC_except_table12575
- GCC_except_table12579
- GCC_except_table12620
- GCC_except_table12624
- GCC_except_table12633
- GCC_except_table12634
- GCC_except_table12641
- GCC_except_table12679
- GCC_except_table12698
- GCC_except_table12703
- GCC_except_table12753
- GCC_except_table12845
- GCC_except_table12848
- GCC_except_table12854
- GCC_except_table12856
- GCC_except_table12896
- GCC_except_table12915
- GCC_except_table12988
- GCC_except_table12991
- GCC_except_table12999
- GCC_except_table13005
- GCC_except_table13007
- GCC_except_table13072
- GCC_except_table13150
- GCC_except_table13154
- GCC_except_table13158
- GCC_except_table13195
- GCC_except_table13220
- GCC_except_table13227
- GCC_except_table13367
- GCC_except_table13380
- GCC_except_table13474
- GCC_except_table13541
- GCC_except_table13747
- GCC_except_table13826
- GCC_except_table13868
- GCC_except_table13917
- GCC_except_table13927
- GCC_except_table13947
- GCC_except_table13962
- GCC_except_table13990
- GCC_except_table13992
- GCC_except_table14005
- GCC_except_table14007
- GCC_except_table14009
- GCC_except_table14028
- GCC_except_table14174
- GCC_except_table14185
- GCC_except_table14212
- GCC_except_table14218
- GCC_except_table14234
- GCC_except_table14304
- GCC_except_table14306
- GCC_except_table14352
- GCC_except_table14354
- GCC_except_table14381
- GCC_except_table14385
- GCC_except_table14386
- GCC_except_table14398
- GCC_except_table14415
- GCC_except_table14418
- GCC_except_table14572
- GCC_except_table4946
- GCC_except_table4956
- GCC_except_table5018
- GCC_except_table5024
- GCC_except_table5029
- GCC_except_table5099
- GCC_except_table5104
- GCC_except_table5134
- GCC_except_table5264
- GCC_except_table5268
- GCC_except_table5625
- GCC_except_table5657
- GCC_except_table5704
- GCC_except_table5723
- GCC_except_table5747
- GCC_except_table5749
- GCC_except_table5775
- GCC_except_table5780
- GCC_except_table5783
- GCC_except_table5785
- GCC_except_table5792
- GCC_except_table5801
- GCC_except_table5805
- GCC_except_table5814
- GCC_except_table5818
- GCC_except_table5857
- GCC_except_table5890
- GCC_except_table5895
- GCC_except_table5919
- GCC_except_table5923
- GCC_except_table5927
- GCC_except_table5949
- GCC_except_table5957
- GCC_except_table5971
- GCC_except_table6000
- GCC_except_table6050
- GCC_except_table6059
- GCC_except_table6101
- GCC_except_table6133
- GCC_except_table6142
- GCC_except_table6146
- GCC_except_table6157
- GCC_except_table6188
- GCC_except_table6217
- GCC_except_table6244
- GCC_except_table6246
- GCC_except_table6260
- GCC_except_table6330
- GCC_except_table6408
- GCC_except_table6413
- GCC_except_table6418
- GCC_except_table6576
- GCC_except_table6593
- GCC_except_table6618
- GCC_except_table6628
- GCC_except_table6670
- GCC_except_table6707
- GCC_except_table6709
- GCC_except_table7109
- GCC_except_table7129
- GCC_except_table7142
- GCC_except_table7155
- GCC_except_table7174
- GCC_except_table7205
- GCC_except_table7210
- GCC_except_table7212
- GCC_except_table7214
- GCC_except_table7223
- GCC_except_table7271
- GCC_except_table7285
- GCC_except_table7323
- GCC_except_table7325
- GCC_except_table7364
- GCC_except_table7617
- GCC_except_table7620
- GCC_except_table7642
- GCC_except_table7649
- GCC_except_table7665
- GCC_except_table7667
- GCC_except_table7668
- GCC_except_table7669
- GCC_except_table7670
- GCC_except_table7671
- GCC_except_table7672
- GCC_except_table7683
- GCC_except_table7684
- GCC_except_table7685
- GCC_except_table7842
- GCC_except_table8061
- GCC_except_table8124
- GCC_except_table8125
- GCC_except_table8185
- GCC_except_table8207
- GCC_except_table8211
- GCC_except_table8218
- GCC_except_table8272
- GCC_except_table8478
- GCC_except_table8480
- GCC_except_table8527
- GCC_except_table8567
- GCC_except_table8571
- GCC_except_table8573
- GCC_except_table8575
- GCC_except_table8587
- GCC_except_table8592
- GCC_except_table8660
- GCC_except_table8702
- GCC_except_table8796
- GCC_except_table8854
- GCC_except_table8874
- GCC_except_table8877
- GCC_except_table8896
- GCC_except_table8955
- GCC_except_table8959
- GCC_except_table8963
- GCC_except_table8964
- GCC_except_table8965
- GCC_except_table8966
- GCC_except_table8967
- GCC_except_table8969
- GCC_except_table8971
- GCC_except_table8975
- GCC_except_table8986
- GCC_except_table8989
- GCC_except_table9054
- GCC_except_table9121
- GCC_except_table9278
- GCC_except_table9319
- GCC_except_table9325
- GCC_except_table9328
- GCC_except_table9588
- GCC_except_table9592
- GCC_except_table9596
- GCC_except_table9616
- GCC_except_table9617
- GCC_except_table9713
- GCC_except_table9723
- GCC_except_table9756
- GCC_except_table9808
- GCC_except_table9873
- GCC_except_table9899
- GCC_except_table9927
- GCC_except_table9960
- GCC_except_table9962
- __OBJC_$_CLASS_METHODS_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|ContentProvenance|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
- __OBJC_$_INSTANCE_METHODS_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|ContentProvenance|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
- __OBJC_CLASS_PROTOCOLS_$_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|ContentProvenance|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
- ___43-[PHPhotoLibrary _assetBytesForOsMigration]_block_invoke
- ___56+[PHAsset fetchAssetObjectIdsForOsMigrationWithOptions:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_65_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
- _additionalPropertiesToFetchOnPrimaryObject.pl_once_object_54
- _additionalPropertiesToFetchOnPrimaryObject.pl_once_object_67
- _additionalPropertiesToFetchOnPrimaryObject.pl_once_token_54
- _additionalPropertiesToFetchOnPrimaryObject.pl_once_token_67
- _propertiesToFetch.pl_once_object_32
- _propertiesToFetch.pl_once_object_51
- _propertiesToFetch.pl_once_object_55
- _propertiesToFetch.pl_once_object_68
- _propertiesToFetch.pl_once_token_32
- _propertiesToFetch.pl_once_token_51
- _propertiesToFetch.pl_once_token_55
- _propertiesToFetch.pl_once_token_68
CStrings:
+ "%@ is not a valid Ambient poster bundle"
+ "%@ should be an instance inheriting from %@, but it is %@"
+ "%@ should be an instance inheriting from %@, but it is nil"
+ "%@, config: %p"
+ "%@.bundle"
+ "-[PHAmbientPosterBundle ingestResourcesIntoPhotoLibrary:error:]_block_invoke"
+ "-[PHAmbientPosterSelection initWithAssetCloudIdentifiers:frequency:]"
+ "-[PHAmbientPosterSelection initWithMemoryType:memoryTitle:memorySubtitle:]"
+ "-[PHAmbientPosterSelection initWithSharedAlbumCloudIdentifiers:]"
+ "-[PHAmbientPosterSelection initWithSmartAlbumSubtypes:assetCollectionCloudIdentifiers:sharedAlbumCloudIdentifiers:peopleCloudIdentifiers:socialGroupCloudIdentifiers:frequency:]"
+ "-[PHAmbientPosterSelection initWithSmartAlbums:peopleCloudIdentifiers:frequency:]"
+ "-[PHAmbientPosterSelection init]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/Projects/PhotoKit/Sources/PHAmbientPosterBundle.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/Projects/PhotoKit/Sources/PHAmbientPosterSelection.m"
+ "1-min"
+ "10-min"
+ "3-min"
+ "30-min"
+ "60-min"
+ "<%@: %p, smart-albums: %@, memory-type: %@, frequency: %@, mode: %@, memoryTitle: %lu, memorySubtitle: %lu, smart-album-subtypes: %lu, collections: %lu, shared-albums: %lu, people+pets: %lu, social-groups: %lu, assets: %lu>"
+ "<%@: %p, type: %@, selection: %@, assets: %lu, version: %lu>"
+ "Ambient Group"
+ "AmbientPoster"
+ "Archive extraction destination directory path exists but is not a directory %@"
+ "Attempted to ingest a duplicate asset. Using existing asset identifier {public}%@"
+ "Destination for asset bundle already exists: '%@'"
+ "Did write cold-start asset bundle for asset %{public}@ to %{public}@"
+ "Encountered error during enumeration of ambient poster bundle at URL '%@' (%@)"
+ "Error creating ambient poster bundle: %{public}@"
+ "Error creating pebble bundle: %{public}@"
+ "Failed to close the bundle archive for reading (%@)"
+ "Failed to close the bundle archive for writing (%@)"
+ "Failed to create PHAmbientPosterConfiguration from URL '%@' (%@)"
+ "Failed to create an ambient poster import source for URL '%@', resource count: %lu"
+ "Failed to decompress the bundle archive %@ (%@)"
+ "Failed to encode ambient poster configuration data at path:%@ error:%@"
+ "Failed to encode the bundle to archive (%@)"
+ "Failed to fetch assets for OS migration: %@"
+ "Failed to fetch assets for identifiers: %@"
+ "Failed to get an asset identifier for ingested record %{public}@"
+ "Failed to import ambient poster resources for bundle '%@'\n%@"
+ "Failed to initialize an ambient poster bundle for URL '%@'"
+ "Failed to initialize an ambient poster bundle: no file at the provided URL '%@'"
+ "Failed to open the bundle archive for reading (%@)"
+ "Failed to open the bundle archive for writing (%@)"
+ "Failed to read ambient poster configuration data at path:%@ error:%@"
+ "Failed to remove ambient poster bundle archive at URL '%@' after failing to close it (%@)."
+ "Failed to remove ambient poster bundle archive at URL '%@' after unarchiving it (%@)."
+ "Failed to remove ambient poster bundle at '%@' after import. (%@)"
+ "Failed to remove decoded ambient poster bundle at URL '%@' after failing to close the archive (%@)."
+ "Failed to set poster data for asset: %{public}@"
+ "Failed to unarchive ambient poster configuration data error:%@"
+ "Failed to update segmentation resource for assets: %{public}@, error: %{public}@"
+ "Failed to write ambient poster configuration data at path:%@ error:%@"
+ "Failed to write asset bundle (%@) to ambient poster bundle (%@) (%@)"
+ "Fetched %lu soon-to-be cold start assets"
+ "H"
+ "Invalid PHAmbientPosterMemoryType: %ld"
+ "Invalid PHAmbientPosterMode: %ld"
+ "Invalid PHAmbientPosterShuffleFrequency: %ld"
+ "Invalid PHAmbientPosterType: %ld"
+ "NOT %K IN %@"
+ "No poster data found for asset: %{public}@"
+ "OS migration estimate: failed to fetch thumbnail-only assets: %@"
+ "PHAmbientPosterBundle.m"
+ "PHAmbientPosterConfiguration.m"
+ "PHImportAmbientPosterSource.m"
+ "Pebble expunge after cold-start"
+ "PebbleBundle"
+ "Refusing to initialize an ambient poster bundle due to version mismatch. Current version number is %d and bundle version number is %lu"
+ "Setting asset identifiers on configuration: %{public}@, %{public}@"
+ "Successfully ingested asset identifier %{public}@"
+ "There were exceptions during asset loading for ambient poster bundle (%@):\n%@"
+ "Unable to create archive extraction destination directory %@: %@"
+ "Wallpaper Group"
+ "Wallpaper Top Group"
+ "Will write cold-start asset bundle for asset %{public}@ to %{public}@"
+ "[bundleURL.pathExtension isEqualToString:@\"bundle\"]"
+ "ambient-poster-%@.configuration"
+ "ambient-poster.configuration"
+ "asset.height"
+ "asset.width"
+ "assetCloudIdentifiers"
+ "assetCloudIdentifiers.count"
+ "assetCollectionCloudIdentifiers"
+ "assetIdentifiers.count > 0"
+ "bundle"
+ "cityscape"
+ "collections"
+ "configurationURL"
+ "daily"
+ "destinationFolderURL"
+ "destinationFolderURL.isFileURL"
+ "faceType"
+ "frequency"
+ "hasSmartAlbums || peopleCloudIdentifiers.count"
+ "landscape"
+ "memories"
+ "memorySubtitle"
+ "memoryTitle"
+ "memoryType"
+ "mode"
+ "peopleCloudIdentifiers"
+ "posterSelection"
+ "posterType"
+ "record.importAsset"
+ "shared-album"
+ "sharedAlbumCloudIdentifiers"
+ "sharedAlbumCloudIdentifiers.count"
+ "smart-albums"
+ "smartAlbumSubtypes"
+ "smartAlbumSubtypes.count || assetCollectionCloudIdentifiers.count || sharedAlbumCloudIdentifiers.count || peopleCloudIdentifiers.count || socialGroupCloudIdentifiers.count"
+ "smartAlbums"
+ "socialGroupCloudIdentifiers"
+ "v24@?0@\"PHAsset\"8@\"PFAssetBundle\"16"
+ "verifyBySelectingInPicker"
```
