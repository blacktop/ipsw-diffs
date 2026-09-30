## SpringBoardHome

> `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-179.3.4.2.100
-  __TEXT.__text: 0x3318dc
-  __TEXT.__auth_stubs: 0x2d50
-  __TEXT.__objc_methlist: 0x3c2ac
-  __TEXT.__const: 0x6854
-  __TEXT.__cstring: 0x1b79f
-  __TEXT.__gcc_except_tab: 0x3fb4
-  __TEXT.__oslogstring: 0xde90
+179.3.9.1.0
+  __TEXT.__text: 0x34e294
+  __TEXT.__auth_stubs: 0x2d20
+  __TEXT.__objc_methlist: 0x3c3cc
+  __TEXT.__const: 0x6844
+  __TEXT.__cstring: 0x170c3
+  __TEXT.__gcc_except_tab: 0x3dd4
+  __TEXT.__oslogstring: 0xe170
   __TEXT.__dlopen_cstrs: 0x4c6
   __TEXT.__ustring: 0x620
-  __TEXT.__swift5_typeref: 0x17e2
+  __TEXT.__swift5_typeref: 0x1758
   __TEXT.__constg_swiftt: 0x86c
   __TEXT.__swift5_reflstr: 0x46a
   __TEXT.__swift5_fieldmd: 0x5a0
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_assocty: 0x378
-  __TEXT.__swift5_proto: 0xe8
+  __TEXT.__swift5_proto: 0xf0
   __TEXT.__swift5_types: 0x9c
-  __TEXT.__swift5_capture: 0xffc
+  __TEXT.__swift5_capture: 0xfdc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0xe4b8
-  __TEXT.__eh_frame: 0x990
-  __TEXT.__objc_classname: 0x6e39
-  __TEXT.__objc_methname: 0x9ae58
-  __TEXT.__objc_methtype: 0x195b6
-  __TEXT.__objc_stubs: 0x59b20
-  __DATA_CONST.__got: 0x2290
-  __DATA_CONST.__const: 0x9740
-  __DATA_CONST.__objc_classlist: 0x1280
-  __DATA_CONST.__objc_catlist: 0x128
+  __TEXT.__unwind_info: 0xf650
+  __TEXT.__eh_frame: 0x7e0
+  __TEXT.__objc_classname: 0x742f
+  __TEXT.__objc_methname: 0x9e0b3
+  __TEXT.__objc_methtype: 0x1a747
+  __TEXT.__objc_stubs: 0x5c340
+  __DATA_CONST.__got: 0x2298
+  __DATA_CONST.__const: 0x95b0
+  __DATA_CONST.__objc_classlist: 0x1288
+  __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0xb28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bb08
+  __DATA_CONST.__objc_selrefs: 0x1bb80
   __DATA_CONST.__objc_protorefs: 0x148
-  __DATA_CONST.__objc_superrefs: 0xe48
+  __DATA_CONST.__objc_superrefs: 0xe58
   __DATA_CONST.__objc_arraydata: 0x6d8
-  __AUTH_CONST.__auth_got: 0x16b8
-  __AUTH_CONST.__const: 0x63c8
-  __AUTH_CONST.__cfstring: 0x15fc0
-  __AUTH_CONST.__objc_const: 0x55898
-  __AUTH_CONST.__objc_intobj: 0x8e8
+  __AUTH_CONST.__auth_got: 0x16a0
+  __AUTH_CONST.__const: 0x6378
+  __AUTH_CONST.__cfstring: 0x15ca0
+  __AUTH_CONST.__objc_const: 0x55a38
+  __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH.__objc_data: 0x6218
+  __AUTH.__objc_data: 0x6268
   __AUTH.__data: 0x568
-  __DATA.__objc_ivar: 0x3b7c
-  __DATA.__data: 0x8888
-  __DATA.__bss: 0x2488
+  __DATA.__objc_ivar: 0x3b90
+  __DATA.__data: 0x88b8
+  __DATA.__bss: 0x2588
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x5c58
   __DATA_DIRTY.__data: 0xc8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EE61B415-121C-3768-928D-D2E2CCCFE965
-  Functions: 22613
-  Symbols:   64436
-  CStrings:  30775
+  UUID: AFB0E9C0-64F5-3689-9596-DFA9FD238BEF
+  Functions: 22663
+  Symbols:   64985
+  CStrings:  30486
 
Symbols:
+ +[SBHIconImageCacheConfiguration supportsSecureCoding]
+ +[SBSApplicationShortcutSystemIcon(SBHAdditions) sbh_defaultSystemImageName]
+ -[CALayer(SBHIconServiceUtilities) sbh_isIconServicesPlaceholder]
+ -[CALayer(SBHIconServiceUtilitiesInternal) sbh_setIconServicesPlaceholder:]
+ -[SBHFileStackIcon initWithLeafIdentifier:applicationBundleID:preferredDisplayName:]
+ -[SBHFileStackIcon initWithPreferredDisplayName:]
+ -[SBHFileStackIcon preferredDisplayName]
+ -[SBHFileStackIcon setPreferredDisplayName:]
+ -[SBHIconImageCacheConfiguration .cxx_destruct]
+ -[SBHIconImageCacheConfiguration copyWithZone:]
+ -[SBHIconImageCacheConfiguration description]
+ -[SBHIconImageCacheConfiguration encodeWithCoder:]
+ -[SBHIconImageCacheConfiguration hash]
+ -[SBHIconImageCacheConfiguration iconSize]
+ -[SBHIconImageCacheConfiguration initWithCoder:]
+ -[SBHIconImageCacheConfiguration initWithStyleConfiguration:iconSize:]
+ -[SBHIconImageCacheConfiguration isEqual:]
+ -[SBHIconImageCacheConfiguration styleConfiguration]
+ -[SBHIconManager _iconImageAppearancesForCacheConfiguration:]
+ -[SBHIconManager _iconImageInfoForCacheConfigurationSize:]
+ -[SBHIconManager _iconImageInfoForCacheConfigurationSize:].cold.1
+ -[SBHIconManager _precacheExtraIconImages]
+ -[SBHIconManager addFileStackWithURL:preferredDisplayName:]
+ -[SBHIconShareSheetActivityItemProvider applicationBundleIdentifier]
+ -[SBHIconShareSheetActivityItemProvider setApplicationBundleIdentifier:]
+ -[SBIcon loadRealIconContentLayerWithInfo:traitCollection:reason:options:priority:placeholderHandler:completionHandler:]
+ -[SBIcon setPlaceholderIconLayer:onLayerView:iconImageInfo:traitCollection:options:]
+ -[SBRootFolderController effectiveContentVisibility]
+ -[SBRootFolderController updateContentViewOcclusion]
+ -[SBSApplicationShortcutSystemIcon(SBHAdditions) sbh_systemImageName]
+ -[UIImage(SBHIconServiceUtilities) sbh_isIconServicesPlaceholder]
+ -[UIImage(SBHIconServiceUtilitiesInternal) sbh_setIconServicesPlaceholder:]
+ -[_SBHLibraryPodCategoryIconListView initWithModel:layoutProvider:iconLocation:orientation:iconViewProvider:]
+ GCC_except_table1003
+ GCC_except_table1039
+ GCC_except_table1062
+ GCC_except_table130
+ GCC_except_table150
+ GCC_except_table448
+ GCC_except_table461
+ GCC_except_table499
+ GCC_except_table519
+ GCC_except_table524
+ GCC_except_table546
+ GCC_except_table575
+ GCC_except_table604
+ GCC_except_table691
+ GCC_except_table701
+ GCC_except_table713
+ GCC_except_table724
+ GCC_except_table728
+ GCC_except_table730
+ GCC_except_table738
+ GCC_except_table741
+ GCC_except_table744
+ GCC_except_table839
+ GCC_except_table895
+ GCC_except_table966
+ GCC_except_table986
+ _OBJC_CLASS_$_SBHIconImageCacheConfiguration
+ _OBJC_IVAR_$_SBHFileStackIcon._preferredDisplayName
+ _OBJC_IVAR_$_SBHIconImageCacheConfiguration._iconSize
+ _OBJC_IVAR_$_SBHIconImageCacheConfiguration._styleConfiguration
+ _OBJC_IVAR_$_SBHIconManager._precacheImagesAfterChangeRunLoopObserver
+ _OBJC_IVAR_$_SBHIconShareSheetActivityItemProvider._applicationBundleIdentifier
+ _OBJC_METACLASS_$_SBHIconImageCacheConfiguration
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _SBHIconServicesCachingTintColor
+ _SBHStringForIconImageCacheConfigurationSize
+ __OBJC_$_CLASS_METHODS_SBHIconImageCacheConfiguration
+ __OBJC_$_CLASS_PROP_LIST_SBHIconImageCacheConfiguration
+ __OBJC_$_INSTANCE_METHODS_CALayer(SBHAdditions|SBHIconServiceUtilities|SBHIconServiceUtilitiesInternal)
+ __OBJC_$_INSTANCE_METHODS_SBHIconImageCacheConfiguration
+ __OBJC_$_INSTANCE_METHODS_UIImage(SBHIconImageCacheUtilities|SBHIconServiceUtilities|SBHIconServiceUtilitiesInternal)
+ __OBJC_$_INSTANCE_VARIABLES_SBHIconImageCacheConfiguration
+ __OBJC_$_PROP_LIST_SBHIconImageCacheConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_SBHIconImageCacheConfiguration
+ __OBJC_CLASS_RO_$_SBHIconImageCacheConfiguration
+ __OBJC_METACLASS_RO_$_SBHIconImageCacheConfiguration
+ ___101-[SBIcon loadRealIconContentLayerForLayerView:iconImageInfo:traitCollection:reason:options:priority:]_block_invoke_2
+ ___101-[SBRootFolderController _internalDismissWidgetAddSheet:clearAddSheetViewController:notifyObservers:]_block_invoke.124
+ ___128-[SBRootFolderController presentWidgetEditingViewControllerFromViewController:withAllowedSizeClasses:allowingNonStackableItems:]_block_invoke.123
+ ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke.1107
+ ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke_2.1109
+ ___42-[SBHIconManager _precacheExtraIconImages]_block_invoke
+ ___42-[SBHIconManager _precacheExtraIconImages]_block_invoke.195
+ ___42-[SBHIconManager _precacheExtraIconImages]_block_invoke_2
+ ___51-[SBHIconManager _engageWallpaperTintColorDropper:]_block_invoke.983
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke.215
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke.215.cold.1
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke.215.cold.2
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke.215.cold.3
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke.215.cold.4
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke.215.cold.5
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke.217
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke_2.218
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke_3.219
+ ___68-[SBHIconManager _precacheDataForRootIconsAfterIconAppearanceChange]_block_invoke
+ ___77-[SBHIconManager _ensureWidgetIsVisibleForDebuggingWithDescriptor:sizeClass:]_block_invoke.253
+ ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.545
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.617
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.620
+ ___SBHGetIconLayerWithImageAppearance_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56r_e17_v16?0"CALayer"8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_224_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_48_e5_v8?0l
+ ___block_literal_global.1027
+ ___block_literal_global.1068
+ ___block_literal_global.1186
+ ___block_literal_global.1239
+ ___block_literal_global.139
+ ___block_literal_global.197
+ ___block_literal_global.208
+ ___block_literal_global.211
+ ___block_literal_global.274
+ ___block_literal_global.276
+ ___block_literal_global.278
+ ___block_literal_global.283
+ ___block_literal_global.285
+ ___block_literal_global.292
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.297
+ ___block_literal_global.300
+ ___block_literal_global.356
+ ___block_literal_global.381
+ ___block_literal_global.384
+ ___block_literal_global.386
+ ___block_literal_global.388
+ ___block_literal_global.425
+ ___block_literal_global.56
+ ___block_literal_global.619
+ ___block_literal_global.70
+ ___block_literal_global.801
+ ___block_literal_global.827
+ ___block_literal_global.894
+ __precacheImagesForRootIconsForStyleConfiguration:.precachingGeneration
+ _block_copy_helper.100
+ _block_copy_helper.102
+ _block_copy_helper.112
+ _block_copy_helper.122
+ _block_copy_helper.132
+ _block_copy_helper.14
+ _block_copy_helper.142
+ _block_copy_helper.152
+ _block_copy_helper.162
+ _block_copy_helper.165
+ _block_copy_helper.175
+ _block_copy_helper.184
+ _block_copy_helper.193
+ _block_copy_helper.20
+ _block_copy_helper.217
+ _block_copy_helper.22
+ _block_copy_helper.227
+ _block_copy_helper.24
+ _block_copy_helper.244
+ _block_copy_helper.253
+ _block_copy_helper.26
+ _block_copy_helper.261
+ _block_copy_helper.269
+ _block_copy_helper.307
+ _block_copy_helper.33
+ _block_copy_helper.35
+ _block_copy_helper.428
+ _block_copy_helper.43
+ _block_copy_helper.44
+ _block_copy_helper.459
+ _block_copy_helper.469
+ _block_copy_helper.479
+ _block_copy_helper.489
+ _block_copy_helper.495
+ _block_copy_helper.50
+ _block_copy_helper.505
+ _block_copy_helper.515
+ _block_copy_helper.52
+ _block_copy_helper.525
+ _block_copy_helper.535
+ _block_copy_helper.54
+ _block_copy_helper.545
+ _block_copy_helper.555
+ _block_copy_helper.574
+ _block_copy_helper.585
+ _block_copy_helper.595
+ _block_copy_helper.606
+ _block_copy_helper.617
+ _block_copy_helper.62
+ _block_copy_helper.627
+ _block_copy_helper.637
+ _block_copy_helper.64
+ _block_copy_helper.647
+ _block_copy_helper.65
+ _block_copy_helper.657
+ _block_copy_helper.668
+ _block_copy_helper.678
+ _block_copy_helper.688
+ _block_copy_helper.699
+ _block_copy_helper.710
+ _block_copy_helper.72
+ _block_copy_helper.721
+ _block_copy_helper.732
+ _block_copy_helper.743
+ _block_copy_helper.754
+ _block_copy_helper.76
+ _block_copy_helper.80
+ _block_copy_helper.815
+ _block_copy_helper.82
+ _block_copy_helper.90
+ _block_copy_helper.92
+ _block_descriptor.102
+ _block_descriptor.104
+ _block_descriptor.114
+ _block_descriptor.124
+ _block_descriptor.134
+ _block_descriptor.144
+ _block_descriptor.154
+ _block_descriptor.16
+ _block_descriptor.164
+ _block_descriptor.167
+ _block_descriptor.177
+ _block_descriptor.186
+ _block_descriptor.195
+ _block_descriptor.219
+ _block_descriptor.22
+ _block_descriptor.229
+ _block_descriptor.24
+ _block_descriptor.246
+ _block_descriptor.255
+ _block_descriptor.26
+ _block_descriptor.263
+ _block_descriptor.271
+ _block_descriptor.28
+ _block_descriptor.309
+ _block_descriptor.35
+ _block_descriptor.37
+ _block_descriptor.430
+ _block_descriptor.45
+ _block_descriptor.46
+ _block_descriptor.461
+ _block_descriptor.471
+ _block_descriptor.481
+ _block_descriptor.491
+ _block_descriptor.497
+ _block_descriptor.507
+ _block_descriptor.517
+ _block_descriptor.52
+ _block_descriptor.527
+ _block_descriptor.537
+ _block_descriptor.54
+ _block_descriptor.547
+ _block_descriptor.557
+ _block_descriptor.56
+ _block_descriptor.576
+ _block_descriptor.587
+ _block_descriptor.597
+ _block_descriptor.608
+ _block_descriptor.619
+ _block_descriptor.629
+ _block_descriptor.639
+ _block_descriptor.64
+ _block_descriptor.649
+ _block_descriptor.659
+ _block_descriptor.66
+ _block_descriptor.67
+ _block_descriptor.670
+ _block_descriptor.680
+ _block_descriptor.690
+ _block_descriptor.701
+ _block_descriptor.712
+ _block_descriptor.723
+ _block_descriptor.734
+ _block_descriptor.74
+ _block_descriptor.745
+ _block_descriptor.756
+ _block_descriptor.78
+ _block_descriptor.817
+ _block_descriptor.82
+ _block_descriptor.84
+ _block_descriptor.92
+ _block_descriptor.94
+ _block_destroy_helper.101
+ _block_destroy_helper.103
+ _block_destroy_helper.113
+ _block_destroy_helper.123
+ _block_destroy_helper.133
+ _block_destroy_helper.143
+ _block_destroy_helper.15
+ _block_destroy_helper.153
+ _block_destroy_helper.163
+ _block_destroy_helper.166
+ _block_destroy_helper.176
+ _block_destroy_helper.185
+ _block_destroy_helper.194
+ _block_destroy_helper.21
+ _block_destroy_helper.218
+ _block_destroy_helper.228
+ _block_destroy_helper.23
+ _block_destroy_helper.245
+ _block_destroy_helper.25
+ _block_destroy_helper.254
+ _block_destroy_helper.262
+ _block_destroy_helper.27
+ _block_destroy_helper.270
+ _block_destroy_helper.308
+ _block_destroy_helper.34
+ _block_destroy_helper.36
+ _block_destroy_helper.429
+ _block_destroy_helper.44
+ _block_destroy_helper.45
+ _block_destroy_helper.460
+ _block_destroy_helper.470
+ _block_destroy_helper.480
+ _block_destroy_helper.490
+ _block_destroy_helper.496
+ _block_destroy_helper.506
+ _block_destroy_helper.51
+ _block_destroy_helper.516
+ _block_destroy_helper.526
+ _block_destroy_helper.53
+ _block_destroy_helper.536
+ _block_destroy_helper.546
+ _block_destroy_helper.55
+ _block_destroy_helper.556
+ _block_destroy_helper.575
+ _block_destroy_helper.586
+ _block_destroy_helper.596
+ _block_destroy_helper.607
+ _block_destroy_helper.618
+ _block_destroy_helper.628
+ _block_destroy_helper.63
+ _block_destroy_helper.638
+ _block_destroy_helper.648
+ _block_destroy_helper.65
+ _block_destroy_helper.658
+ _block_destroy_helper.66
+ _block_destroy_helper.669
+ _block_destroy_helper.679
+ _block_destroy_helper.689
+ _block_destroy_helper.700
+ _block_destroy_helper.711
+ _block_destroy_helper.722
+ _block_destroy_helper.73
+ _block_destroy_helper.733
+ _block_destroy_helper.744
+ _block_destroy_helper.755
+ _block_destroy_helper.77
+ _block_destroy_helper.81
+ _block_destroy_helper.816
+ _block_destroy_helper.83
+ _block_destroy_helper.91
+ _block_destroy_helper.93
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA10_ShapeViewVyAA4PathVAA8MaterialVGAA30_EnvironmentKeyWritingModifierVyAA15LayoutDirectionOGGAA0F0HPAjaQHPyHC_AoA0fL0HPyHCHC.20
+ _kSBHIconServicesPlaceholderKey
+ _kSBIconStateFileStackIconPreferredDisplayNameKey
+ _objc_msgSend$_changeFolderDuringCopy:
+ _objc_msgSend$_didAddList:informObservers:
+ _objc_msgSend$_didExplicitlyRemoveHiddenLists:
+ _objc_msgSend$_didRemoveList:atIndex:informObservers:
+ _objc_msgSend$_iconImageAppearancesForCacheConfiguration:
+ _objc_msgSend$_iconImageInfoForCacheConfigurationSize:
+ _objc_msgSend$_isResizing
+ _objc_msgSend$_precacheExtraIconImages
+ _objc_msgSend$_preferredFontForTextStyle:variant:
+ _objc_msgSend$_preferredFontForTextStyle:weight:
+ _objc_msgSend$_setInvisibilitySuppressesGlass:
+ _objc_msgSend$_updateModelByRepairingGapsIfNecessary
+ _objc_msgSend$_willRemoveList:atIndex:informObservers:
+ _objc_msgSend$addApplicationInfoProviderObserver:
+ _objc_msgSend$addEmptyListWithIdentifier:
+ _objc_msgSend$addFileStackWithURL:preferredDisplayName:
+ _objc_msgSend$addIcon:options:listGridCellInfoOptions:
+ _objc_msgSend$addInstalledWebClipsObserver:
+ _objc_msgSend$addListWithIcons:removingHiddenListsIfNecessary:
+ _objc_msgSend$addObserver:inView:
+ _objc_msgSend$addWithApplication:force:
+ _objc_msgSend$allowedGridSizeClassesForDockForIconModel:
+ _objc_msgSend$allowedGridSizeClassesForDockForRootFolder:
+ _objc_msgSend$allowedGridSizeClassesForTodayListForIconModel:
+ _objc_msgSend$allowedGridSizeClassesForTodayListForRootFolder:
+ _objc_msgSend$allowedIconsForByReplacingContentsWithIcons:
+ _objc_msgSend$allowsAddingIcons:
+ _objc_msgSend$applicationIconClass
+ _objc_msgSend$applicationInfoProvider
+ _objc_msgSend$applicationPlaceholders
+ _objc_msgSend$archiveRootFolderInModel:metadata:
+ _objc_msgSend$archiveVersionForIconModel:
+ _objc_msgSend$automaticallyAddsWebClips
+ _objc_msgSend$blueColor
+ _objc_msgSend$bookmarkClass
+ _objc_msgSend$bookmarkIconClass
+ _objc_msgSend$bookmarkIconForWebClipIdentifier:
+ _objc_msgSend$bookmarkIcons
+ _objc_msgSend$boostsGlassWhitePoint
+ _objc_msgSend$bumpedIconsFallbackList
+ _objc_msgSend$canAcceptIconContentInLayerView:
+ _objc_msgSend$canAddIconCount:
+ _objc_msgSend$canBeAddedToSubfolder
+ _objc_msgSend$canSaveIconState:
+ _objc_msgSend$changeGridSizeClassOfContainedIcon:toGridSizeClass:gridCellInfoOptions:
+ _objc_msgSend$changeGridSizeClassOfIcon:toGridSizeClass:options:listGridCellInfoOptions:
+ _objc_msgSend$changeGridSizeOfList:toGridSize:options:
+ _objc_msgSend$checkIgnoredListConsistency
+ _objc_msgSend$clearDesiredIconStateIfPossible
+ _objc_msgSend$columnCountForTodayListForRootFolder:
+ _objc_msgSend$compactOverflowLists
+ _objc_msgSend$compactsFirstList
+ _objc_msgSend$containsWidgetIconWithExtensionBundleIdentifier:
+ _objc_msgSend$contentsScale
+ _objc_msgSend$currentLeafIdentifiers
+ _objc_msgSend$currentLocaleDidChangeNotificationName
+ _objc_msgSend$debugDescription
+ _objc_msgSend$decodeCGSizeForKey:
+ _objc_msgSend$defaultApplicationDataSource
+ _objc_msgSend$defaultIconStateForIconModel:
+ _objc_msgSend$deleteCurrentIconStateWithOptions:error:
+ _objc_msgSend$deleteDesiredIconStateWithOptions:error:
+ _objc_msgSend$deleteIconState
+ _objc_msgSend$desiredIconState
+ _objc_msgSend$desiredIconStateFlattened
+ _objc_msgSend$desiredIndexPathForIconWithIdentifier:
+ _objc_msgSend$didAddFolder:
+ _objc_msgSend$didDeleteIconState:
+ _objc_msgSend$didRemoveFolder:
+ _objc_msgSend$didSaveIconState:
+ _objc_msgSend$didUnarchiveMetadata:
+ _objc_msgSend$directlyContainsIconWithIdentifier:
+ _objc_msgSend$effectiveGeometry
+ _objc_msgSend$enumerateApplicationIconsForBundleIdentifier:usingBlock:
+ _objc_msgSend$enumerateDirectlyContainedIconsUsingBlock:
+ _objc_msgSend$enumerateExtraListsUsingBlock:
+ _objc_msgSend$enumerateTodayListsUsingBlock:
+ _objc_msgSend$firstFolderWithUniqueIdentifier:
+ _objc_msgSend$firstFolderWithUniqueIdentifier:displayName:defaultDisplayName:
+ _objc_msgSend$firstIconPassingTest2:
+ _objc_msgSend$firstIconPassingTest:
+ _objc_msgSend$folder:didAddIcons:removedIcons:
+ _objc_msgSend$folder:didAddList:
+ _objc_msgSend$folder:didMoveIcon:
+ _objc_msgSend$folder:didMoveList:fromIndex:toIndex:
+ _objc_msgSend$folder:didRemoveLists:atIndexes:
+ _objc_msgSend$folder:didReplaceIcon:withIcon:
+ _objc_msgSend$folder:list:didInvalidateLayoutWithGridCellInfoOptions:
+ _objc_msgSend$folder:listHiddenDidChange:
+ _objc_msgSend$folder:listHiddenWillChange:
+ _objc_msgSend$folder:willAddIcon:
+ _objc_msgSend$folder:willRemoveLists:atIndexes:
+ _objc_msgSend$folder:willRestoreOverflowIcon:toList:
+ _objc_msgSend$folderCancelableDidChange:
+ _objc_msgSend$folderContainingIndexPath:
+ _objc_msgSend$folderDisplayNameDidChange:
+ _objc_msgSend$folderIconStateDidDirty:
+ _objc_msgSend$glassIdentifier
+ _objc_msgSend$gridCellIndexForIconIndex:gridCellInfoOptions:
+ _objc_msgSend$gridPathForFirstFreeSlotAvoidingFirstList:listGridCellInfoOptions:
+ _objc_msgSend$gridPathForIndexPath:listGridCellInfoOptions:
+ _objc_msgSend$gridPathForRelativePath:
+ _objc_msgSend$gridPathWithListAtIndexPath:gridCellIndex:listGridCellInfoOptions:
+ _objc_msgSend$gridSizeClassDomainForIconModel:
+ _objc_msgSend$gridSizeClassSizes
+ _objc_msgSend$gridSizeClassSizesForIconModel:
+ _objc_msgSend$hasDesiredIconState
+ _objc_msgSend$hasMultipleContiguousRegionsInGridRange:
+ _objc_msgSend$headerLeadingConstraint
+ _objc_msgSend$headerTrailingConstraint
+ _objc_msgSend$hiddenApplications
+ _objc_msgSend$hiddenIconTags
+ _objc_msgSend$hiddenTagsThatAffectBookmarkIcons
+ _objc_msgSend$iconAtGridPath:
+ _objc_msgSend$iconFor:
+ _objc_msgSend$iconForIdentifier:
+ _objc_msgSend$iconImageStyleConfiguration
+ _objc_msgSend$iconLayerContentLayerDidChange:
+ _objc_msgSend$iconLayerContentTypeDidChange:
+ _objc_msgSend$iconLayerViewContentLayerDidChange:
+ _objc_msgSend$iconLayerViewContentTypeDidChange:
+ _objc_msgSend$iconManager:extraIconImageCacheConfigurationsForPrecachingWithCompletion:
+ _objc_msgSend$iconModel:allowedGridSizeClassesForFolderClass:
+ _objc_msgSend$iconModel:archiveRepresentationForIcon:
+ _objc_msgSend$iconModel:archiveRepresentationForIconDataSource:
+ _objc_msgSend$iconModel:customInsertionGridPathForIcon:inRootFolder:
+ _objc_msgSend$iconModel:customInsertionIndexPathForIcon:inRootFolder:
+ _objc_msgSend$iconModel:customInsertionRelativePathForIcon:inRootFolder:
+ _objc_msgSend$iconModel:didAddIcon:
+ _objc_msgSend$iconModel:iconDataSourceForArchiveRepresentation:
+ _objc_msgSend$iconModel:iconForArchiveRepresentation:
+ _objc_msgSend$iconModel:launchIcon:fromLocation:context:
+ _objc_msgSend$iconModel:listGridSizeForFolderClass:
+ _objc_msgSend$iconModel:listWithNonDefaultSizedIconsGridSizeForFolderClass:
+ _objc_msgSend$iconModel:listsAllowRotatedLayoutForFolderClass:
+ _objc_msgSend$iconModel:listsFixedIconLocationBehaviorForFolderClass:
+ _objc_msgSend$iconModel:listsIconDisplacementBehaviorForFolderClass:
+ _objc_msgSend$iconModel:listsIconLayoutBehaviorForFolderClass:
+ _objc_msgSend$iconModel:localizedFolderNameForDefaultDisplayName:
+ _objc_msgSend$iconModel:maxColumnCountForListInRootFolderWithInterfaceOrientation:
+ _objc_msgSend$iconModel:maxRowCountForListInRootFolderWithInterfaceOrientation:
+ _objc_msgSend$iconModel:shouldAvoidPlacingIconOnFirstPage:
+ _objc_msgSend$iconModel:shouldLeaveGapForMissingArchivedIconWithIdentifier:
+ _objc_msgSend$iconModel:shouldPlaceIconOnIgnoredList:
+ _objc_msgSend$iconModel:shouldRemoveIcon:
+ _objc_msgSend$iconModel:shouldUseAbsolutePositionForDesiredIconWithIdentifier:
+ _objc_msgSend$iconModel:supportedGridSizeClassesForWidgetWithKind:extensionBundleIdentifier:containerBundleIdentifier:
+ _objc_msgSend$iconModel:validatedFileStackIconForFileStackIcon:
+ _objc_msgSend$iconModel:validatedWidgetIconForWidgetIcon:
+ _objc_msgSend$iconModel:willRemoveIcon:
+ _objc_msgSend$iconModelMetadata
+ _objc_msgSend$iconRelativePathWithFolderIdentifier:listIdentifier:
+ _objc_msgSend$iconRelativePathWithGridCellIndex:
+ _objc_msgSend$iconRepository:didAddIcon:
+ _objc_msgSend$iconRepository:didAddPlaceholderToApplicationIcon:
+ _objc_msgSend$iconRepository:didChangeVisibilityForIconsToVisible:hidden:
+ _objc_msgSend$iconRepository:didRemoveIcon:
+ _objc_msgSend$iconRepository:didRemovePlaceholderFromApplicationIcon:
+ _objc_msgSend$iconRepository:willRemoveIcon:
+ _objc_msgSend$iconStateByReplacingTodayListsInIconState:withTodayListsFromIconState:
+ _objc_msgSend$ignoresIconsNotInIconState
+ _objc_msgSend$imageHeightConstraint
+ _objc_msgSend$imageWidthConstraint
+ _objc_msgSend$indexOfFirstEmptyGridCellRangeOfSize:flipped:
+ _objc_msgSend$indexOfFirstEmptyGridCellRangeOfSize:inGridRange:flipped:
+ _objc_msgSend$indexOfFirstGridCellRangeOfSize:inGridCellIndexRange:passingTest:
+ _objc_msgSend$indexOfListWithIdentifier:
+ _objc_msgSend$indexPathForGridPath:
+ _objc_msgSend$indexPathForRelativePath:
+ _objc_msgSend$initWithApplicationInfoProvider:
+ _objc_msgSend$initWithApplicationPlaceholder:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithDynamicProvider:
+ _objc_msgSend$initWithFolder:options:
+ _objc_msgSend$initWithLeafIdentifier:application:
+ _objc_msgSend$initWithLeafIdentifier:applicationBundleID:preferredDisplayName:
+ _objc_msgSend$initWithMetrics:iconImageInfo:backgroundView:material:
+ _objc_msgSend$initWithName:sourceView:configuration:
+ _objc_msgSend$initWithName:viewBuilder:
+ _objc_msgSend$initWithObject:
+ _objc_msgSend$initWithPreferredDisplayName:
+ _objc_msgSend$initWithStore:applicationDataSource:
+ _objc_msgSend$initWithStore:iconRepository:
+ _objc_msgSend$initWithStyleConfiguration:iconSize:
+ _objc_msgSend$initWithWebClip:
+ _objc_msgSend$insertIcon:beforeIcon:gridCellInfoOptions:mutationOptions:
+ _objc_msgSend$insertSublayer:above:
+ _objc_msgSend$isCheckingModelConsistency
+ _objc_msgSend$isDockUtilitiesSupportedForIconModel:
+ _objc_msgSend$isEmptyIgnoringPlaceholders
+ _objc_msgSend$isExtraListIndex:
+ _objc_msgSend$isIconAtIndexPathInDock:includingDockFolders:
+ _objc_msgSend$isIconWithIdentifierInIgnoredList:
+ _objc_msgSend$isKindOfClass:
+ _objc_msgSend$isOutOfBoundsAtIconIndex:
+ _objc_msgSend$isRestoring
+ _objc_msgSend$isTrackingIcon:
+ _objc_msgSend$isValidIndexPath:
+ _objc_msgSend$isValidIndexPath:forInsertion:
+ _objc_msgSend$labelNumberOfLines
+ _objc_msgSend$labelViewsForIconViews
+ _objc_msgSend$lastList
+ _objc_msgSend$lastUsedRow
+ _objc_msgSend$lastVisibleList
+ _objc_msgSend$leading
+ _objc_msgSend$leafIconIdentifiers
+ _objc_msgSend$leafIdentifiersFromArchive:
+ _objc_msgSend$leastRecentlyHiddenList
+ _objc_msgSend$listAllowedGridSizeClasses
+ _objc_msgSend$listAtIndexPath:
+ _objc_msgSend$listAtVisibleIndex:
+ _objc_msgSend$listContainerViewTopConstraint
+ _objc_msgSend$listRotatedLayoutClusterGridSizeClass
+ _objc_msgSend$listRotatedLayoutClusterGridSizeClassForIconModel:
+ _objc_msgSend$listWithIdentifier:inFolderWithIdentifier:
+ _objc_msgSend$listWithNonDefaultSizedIconsGridSize
+ _objc_msgSend$listsAllowIndependentRotatedLayout
+ _objc_msgSend$listsAllowRotatedLayout
+ _objc_msgSend$listsIconLayoutBehavior
+ _objc_msgSend$loadAllIcons
+ _objc_msgSend$loadDesiredIconState:
+ _objc_msgSend$loadRealIconContentLayerWithInfo:traitCollection:reason:options:priority:placeholderHandler:completionHandler:
+ _objc_msgSend$localeChanged
+ _objc_msgSend$magentaColor
+ _objc_msgSend$makeFolderWithDisplayName:uniqueIdentifier:
+ _objc_msgSend$makeNewList
+ _objc_msgSend$makeNewListWithIcons:
+ _objc_msgSend$mask
+ _objc_msgSend$matchesWidgetIcon:
+ _objc_msgSend$maxColumnCountForTodayList
+ _objc_msgSend$maxColumnCountForTodayListForIconModel:
+ _objc_msgSend$maxIconCountForDockForIconModel:
+ _objc_msgSend$maxIconCountForDockForRootFolder:
+ _objc_msgSend$maxIconCountForDockUtilitiesForIconModel:
+ _objc_msgSend$maxIconCountForDockUtilitiesForRootFolder:
+ _objc_msgSend$maxListCountForFoldersForIconModel:
+ _objc_msgSend$modernizeRootArchive:
+ _objc_msgSend$noteContainedIcon:replacedIcon:
+ _objc_msgSend$noteContainedIconsAdded:removed:
+ _objc_msgSend$numberOfGapsInGridRange:
+ _objc_msgSend$numberOfUsedGridCellsInColumn:rowRange:
+ _objc_msgSend$objectWithUniqueIdentifier:
+ _objc_msgSend$postsDidAddIconNotification
+ _objc_msgSend$preferredDisplayName
+ _objc_msgSend$prependIcon:toListAtIndex:options:
+ _objc_msgSend$prependIcons:options:
+ _objc_msgSend$rectForCellAtIconCoordinate:metrics:
+ _objc_msgSend$removeApplicationPlaceholder:pruneEmptyIcons:
+ _objc_msgSend$removeApplicationWithBundleIdentifier:
+ _objc_msgSend$removeApplicationWithBundleIdentifier:pruneEmptyIcons:
+ _objc_msgSend$removeLastList
+ _objc_msgSend$removeLeastRecentlyHiddenList
+ _objc_msgSend$replaceApplicationDataSourcesWithApplication:
+ _objc_msgSend$replaceApplicationPlaceholderDataSourcesWithApplicationPlaceholder:
+ _objc_msgSend$replaceIconDataSourcesWithApplicationPlaceholder:
+ _objc_msgSend$replaceLayoutWithGridCellInfo:mutationOptions:
+ _objc_msgSend$requiredTrailingEmptyListCount
+ _objc_msgSend$resolvedComponentsForIndexPath:
+ _objc_msgSend$respondsToSelector:
+ _objc_msgSend$rootFolder:canAddIcon:toIconList:inFolder:
+ _objc_msgSend$rootFolder:canBounceIcon:
+ _objc_msgSend$rootFolder:isGridLayoutValid:forIconList:inFolder:
+ _objc_msgSend$rootFolder:shouldBounceIcon:afterInsertingIcons:forIconList:inFolder:
+ _objc_msgSend$rootFolderAllowedGridSizeClasses
+ _objc_msgSend$rotatedGridSizeClassSizesForIconModel:
+ _objc_msgSend$saveDesiredIconState
+ _objc_msgSend$saveDesiredIconState:error:
+ _objc_msgSend$sb_firstIconPathComponent
+ _objc_msgSend$sb_iconPathCount
+ _objc_msgSend$sb_indexPathByRemovingFirstIconPathComponent
+ _objc_msgSend$sb_indexPathByReplacingLastIconIndex:
+ _objc_msgSend$sb_lastListIndex
+ _objc_msgSend$sbh_applyFolderGlassWithGrouping:
+ _objc_msgSend$sbh_defaultSystemImageName
+ _objc_msgSend$sbh_isIconServicesPlaceholder
+ _objc_msgSend$sbh_setIconServicesPlaceholder:
+ _objc_msgSend$sbh_systemImageName
+ _objc_msgSend$separatorView
+ _objc_msgSend$setAdjustsFontForContentSizeCategory:
+ _objc_msgSend$setAllowsIndependentRotatedLayout:
+ _objc_msgSend$setBackgroundMaterial:
+ _objc_msgSend$setBookmark:
+ _objc_msgSend$setContentContainsInteractiveUIControls:
+ _objc_msgSend$setDesiredIconStateFlattened:
+ _objc_msgSend$setGridSizeClassForContentWidth:
+ _objc_msgSend$setIconContentGeneration:
+ _objc_msgSend$setIconContentLayer:generation:imageAppearance:type:animated:
+ _objc_msgSend$setIconContentType:
+ _objc_msgSend$setIconSource:
+ _objc_msgSend$setIsCheckingModelConsistency:
+ _objc_msgSend$setLeavesGapsForMissingIcons:
+ _objc_msgSend$setListViewClass:
+ _objc_msgSend$setMatchesAlpha:
+ _objc_msgSend$setMaximumNumberOfPages:
+ _objc_msgSend$setPlaceholderIconLayer:onLayerView:iconImageInfo:traitCollection:options:
+ _objc_msgSend$setPreferredDisplayName:
+ _objc_msgSend$setPreferredSymbolConfiguration:
+ _objc_msgSend$setRemovedIcons:
+ _objc_msgSend$setRemovesEmptyFolders:
+ _objc_msgSend$setSearchPlaceholderText:
+ _objc_msgSend$setSearchTintColor:
+ _objc_msgSend$setStyle:
+ _objc_msgSend$setVisibilityOfIconsWithVisibleTags:hiddenTags:
+ _objc_msgSend$setWantsCustomApplicationsSection:
+ _objc_msgSend$setWantsGlassGroupAppliedToGalleryContents:
+ _objc_msgSend$set_isResizing:
+ _objc_msgSend$shapeLayer
+ _objc_msgSend$sheenEffectDebugUIEnabled
+ _objc_msgSend$sheenEffectMinimumMovementToBecomeVisible
+ _objc_msgSend$sheenEffectStrength
+ _objc_msgSend$shouldAvoidCreatingIconForApplication:
+ _objc_msgSend$styleConfiguration
+ _objc_msgSend$styleConfigurationWithTintColor:
+ _objc_msgSend$supportsBadging
+ _objc_msgSend$symbolImageView
+ _objc_msgSend$systemFillColor
+ _objc_msgSend$titleStackView
+ _objc_msgSend$titleStackViewBottomConstraint
+ _objc_msgSend$todayListsStore
+ _objc_msgSend$unarchiveRootFolderFromArchive:withIconSource:
+ _objc_msgSend$unarchivedIdentifiers
+ _objc_msgSend$updateTraitsIfNeeded
+ _objc_msgSend$validatedIndexPathForInsertionIndexPath:avoidingFirstList:
+ _objc_msgSend$viewBuilder
+ _objc_msgSend$visibleIconTags
+ _objc_msgSend$willLayout
+ _swift_release_n
+ _swift_willThrowTypedImpl
+ _symbolic _____Sg_ABt 10Foundation9IndexPathV
+ _symbolic ______p s5ErrorP
- +[SBSApplicationShortcutSystemIcon(SBHAdditions) sbh_defaultImage]
- +[SBSApplicationShortcutSystemIcon(SBHAdditions) sbh_defaultImage].cold.1
- +[SBSApplicationShortcutSystemPrivateIcon(SBHAdditions) sbh_defaultImage]
- -[SBIcon loadRealIconContentLayerWithInfo:traitCollection:reason:options:priority:completionHandler:]
- -[SBSApplicationShortcutSystemIcon(SBHAdditions) sbh_image]
- -[SBSApplicationShortcutSystemIcon(SBHAdditions) sbh_systemImage]
- -[SBSApplicationShortcutSystemPrivateIcon(SBHAdditions) sbh_image]
- -[SBSApplicationShortcutSystemPrivateIcon(SBHAdditions) sbh_systemImage]
- GCC_except_table1030
- GCC_except_table1053
- GCC_except_table122
- GCC_except_table142
- GCC_except_table255
- GCC_except_table283
- GCC_except_table300
- GCC_except_table434
- GCC_except_table439
- GCC_except_table452
- GCC_except_table490
- GCC_except_table510
- GCC_except_table515
- GCC_except_table537
- GCC_except_table566
- GCC_except_table595
- GCC_except_table682
- GCC_except_table692
- GCC_except_table695
- GCC_except_table706
- GCC_except_table708
- GCC_except_table710
- GCC_except_table712
- GCC_except_table729
- GCC_except_table732
- GCC_except_table830
- GCC_except_table886
- GCC_except_table95
- GCC_except_table957
- GCC_except_table977
- GCC_except_table994
- __OBJC_$_CATEGORY_CLASS_METHODS_SBSApplicationShortcutSystemPrivateIcon_$_SBHAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_CALayer_$_SBHAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_SBSApplicationShortcutSystemPrivateIcon_$_SBHAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UIImage_$_SBHIconImageCacheUtilities
- __OBJC_$_CATEGORY_SBSApplicationShortcutSystemPrivateIcon_$_SBHAdditions
- __OBJC_$_PROP_LIST_UIImage_$_SBHIconImageCacheUtilities
- ___101-[SBRootFolderController _internalDismissWidgetAddSheet:clearAddSheetViewController:notifyObservers:]_block_invoke.118
- ___128-[SBRootFolderController presentWidgetEditingViewControllerFromViewController:withAllowedSizeClasses:allowingNonStackableItems:]_block_invoke.117
- ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke.1094
- ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke_2.1096
- ___51-[SBHIconManager _engageWallpaperTintColorDropper:]_block_invoke.970
- ___66+[SBSApplicationShortcutSystemIcon(SBHAdditions) sbh_defaultImage]_block_invoke
- ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke_6
- ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke_7
- ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke_8
- ___77-[SBHIconManager _ensureWidgetIsVisibleForDebuggingWithDescriptor:sizeClass:]_block_invoke.240
- ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.532
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.604
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.607
- ___block_descriptor_152_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_200_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1014
- ___block_literal_global.1055
- ___block_literal_global.1173
- ___block_literal_global.1226
- ___block_literal_global.200
- ___block_literal_global.203
- ___block_literal_global.206
- ___block_literal_global.268
- ___block_literal_global.273
- ___block_literal_global.275
- ___block_literal_global.277
- ___block_literal_global.279
- ___block_literal_global.282
- ___block_literal_global.287
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.343
- ___block_literal_global.368
- ___block_literal_global.371
- ___block_literal_global.373
- ___block_literal_global.375
- ___block_literal_global.412
- ___block_literal_global.55
- ___block_literal_global.59
- ___block_literal_global.606
- ___block_literal_global.788
- ___block_literal_global.814
- ___block_literal_global.881
- _block_copy_helper.107
- _block_copy_helper.117
- _block_copy_helper.12
- _block_copy_helper.127
- _block_copy_helper.137
- _block_copy_helper.147
- _block_copy_helper.157
- _block_copy_helper.160
- _block_copy_helper.170
- _block_copy_helper.179
- _block_copy_helper.188
- _block_copy_helper.19
- _block_copy_helper.208
- _block_copy_helper.21
- _block_copy_helper.224
- _block_copy_helper.23
- _block_copy_helper.254
- _block_copy_helper.263
- _block_copy_helper.271
- _block_copy_helper.28
- _block_copy_helper.29
- _block_copy_helper.30
- _block_copy_helper.309
- _block_copy_helper.39
- _block_copy_helper.427
- _block_copy_helper.458
- _block_copy_helper.468
- _block_copy_helper.47
- _block_copy_helper.478
- _block_copy_helper.488
- _block_copy_helper.49
- _block_copy_helper.498
- _block_copy_helper.504
- _block_copy_helper.51
- _block_copy_helper.514
- _block_copy_helper.524
- _block_copy_helper.534
- _block_copy_helper.544
- _block_copy_helper.554
- _block_copy_helper.57
- _block_copy_helper.573
- _block_copy_helper.583
- _block_copy_helper.59
- _block_copy_helper.594
- _block_copy_helper.60
- _block_copy_helper.604
- _block_copy_helper.61
- _block_copy_helper.615
- _block_copy_helper.626
- _block_copy_helper.636
- _block_copy_helper.646
- _block_copy_helper.656
- _block_copy_helper.666
- _block_copy_helper.67
- _block_copy_helper.677
- _block_copy_helper.687
- _block_copy_helper.698
- _block_copy_helper.709
- _block_copy_helper.71
- _block_copy_helper.720
- _block_copy_helper.731
- _block_copy_helper.742
- _block_copy_helper.75
- _block_copy_helper.753
- _block_copy_helper.77
- _block_copy_helper.81
- _block_copy_helper.814
- _block_copy_helper.825
- _block_copy_helper.85
- _block_copy_helper.87
- _block_copy_helper.96
- _block_copy_helper.97
- _block_descriptor.109
- _block_descriptor.119
- _block_descriptor.129
- _block_descriptor.139
- _block_descriptor.14
- _block_descriptor.149
- _block_descriptor.159
- _block_descriptor.162
- _block_descriptor.172
- _block_descriptor.181
- _block_descriptor.190
- _block_descriptor.21
- _block_descriptor.210
- _block_descriptor.226
- _block_descriptor.23
- _block_descriptor.25
- _block_descriptor.256
- _block_descriptor.265
- _block_descriptor.273
- _block_descriptor.30
- _block_descriptor.31
- _block_descriptor.311
- _block_descriptor.32
- _block_descriptor.41
- _block_descriptor.429
- _block_descriptor.460
- _block_descriptor.470
- _block_descriptor.480
- _block_descriptor.49
- _block_descriptor.490
- _block_descriptor.500
- _block_descriptor.506
- _block_descriptor.51
- _block_descriptor.516
- _block_descriptor.526
- _block_descriptor.53
- _block_descriptor.536
- _block_descriptor.546
- _block_descriptor.556
- _block_descriptor.575
- _block_descriptor.585
- _block_descriptor.59
- _block_descriptor.596
- _block_descriptor.606
- _block_descriptor.61
- _block_descriptor.617
- _block_descriptor.62
- _block_descriptor.628
- _block_descriptor.63
- _block_descriptor.638
- _block_descriptor.648
- _block_descriptor.658
- _block_descriptor.668
- _block_descriptor.679
- _block_descriptor.689
- _block_descriptor.69
- _block_descriptor.700
- _block_descriptor.711
- _block_descriptor.722
- _block_descriptor.73
- _block_descriptor.733
- _block_descriptor.744
- _block_descriptor.755
- _block_descriptor.77
- _block_descriptor.79
- _block_descriptor.816
- _block_descriptor.827
- _block_descriptor.83
- _block_descriptor.87
- _block_descriptor.89
- _block_descriptor.98
- _block_descriptor.99
- _block_destroy_helper.108
- _block_destroy_helper.118
- _block_destroy_helper.128
- _block_destroy_helper.13
- _block_destroy_helper.138
- _block_destroy_helper.148
- _block_destroy_helper.158
- _block_destroy_helper.161
- _block_destroy_helper.171
- _block_destroy_helper.180
- _block_destroy_helper.189
- _block_destroy_helper.20
- _block_destroy_helper.209
- _block_destroy_helper.22
- _block_destroy_helper.225
- _block_destroy_helper.24
- _block_destroy_helper.255
- _block_destroy_helper.264
- _block_destroy_helper.272
- _block_destroy_helper.29
- _block_destroy_helper.30
- _block_destroy_helper.31
- _block_destroy_helper.310
- _block_destroy_helper.40
- _block_destroy_helper.428
- _block_destroy_helper.459
- _block_destroy_helper.469
- _block_destroy_helper.479
- _block_destroy_helper.48
- _block_destroy_helper.489
- _block_destroy_helper.499
- _block_destroy_helper.50
- _block_destroy_helper.505
- _block_destroy_helper.515
- _block_destroy_helper.52
- _block_destroy_helper.525
- _block_destroy_helper.535
- _block_destroy_helper.545
- _block_destroy_helper.555
- _block_destroy_helper.574
- _block_destroy_helper.58
- _block_destroy_helper.584
- _block_destroy_helper.595
- _block_destroy_helper.60
- _block_destroy_helper.605
- _block_destroy_helper.61
- _block_destroy_helper.616
- _block_destroy_helper.62
- _block_destroy_helper.627
- _block_destroy_helper.637
- _block_destroy_helper.647
- _block_destroy_helper.657
- _block_destroy_helper.667
- _block_destroy_helper.678
- _block_destroy_helper.68
- _block_destroy_helper.688
- _block_destroy_helper.699
- _block_destroy_helper.710
- _block_destroy_helper.72
- _block_destroy_helper.721
- _block_destroy_helper.732
- _block_destroy_helper.743
- _block_destroy_helper.754
- _block_destroy_helper.76
- _block_destroy_helper.78
- _block_destroy_helper.815
- _block_destroy_helper.82
- _block_destroy_helper.826
- _block_destroy_helper.86
- _block_destroy_helper.88
- _block_destroy_helper.97
- _block_destroy_helper.98
- _get_witness_table 7SwiftUI15ModifiedContentVyAA10_ShapeViewVyAA4PathVAA8MaterialVGAA30_EnvironmentKeyWritingModifierVyAA15LayoutDirectionOGGAA0F0HPAjaQHPyHC_AoA0fL0HPyHCHC.19
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$imageNamed:inBundle:compatibleWithTraitCollection:
- _objc_msgSend$loadRealIconContentLayerWithInfo:traitCollection:reason:options:priority:completionHandler:
- _objc_msgSend$sbh_defaultImage
- _objc_msgSend$sbh_image
- _objc_msgSend$sbh_systemImage
- _objc_retain_x10
- _objc_retain_x6
- _objc_retain_x7
- _sbh_defaultImage.__defaultImage
- _sbh_defaultImage.onceToken
- _symbolic _____ySSSgGSg 7SwiftUI11AnyLocationC
- _symbolic _____y_____G s23_ContiguousArrayStorageC 7SwiftUI4AxisO3SetV
- _symbolic _____y______Qo_ 7SwiftUI4ViewPAAE22containerRelativeFrame_9alignmentQrAA4AxisO3SetV_AA9AlignmentVtFQO 15SpringBoardHome08IconListC0V
- _symbolic _____y______Qo_ 7SwiftUI4ViewPAAE22containerRelativeFrame_9alignmentQrAA4AxisO3SetV_AA9AlignmentVtFQO 15SpringBoardHome19IconListPageControlV
- _symbolic _____y_____y_____y_____y_____ySaySo15SBIconListModelCGSS_____y_____y______Qo_SSGGG_Qo_G______Qo_ 7SwiftUI4ViewPAAE20scrollTargetBehavioryQrqd__AA06ScrolleF0Rd__lFQO AA0gC0V AcAE0dE6Layout9isEnabledQrSb_tFQO AA10LazyHStackV AA7ForEachV AA6IDViewV AcAE22containerRelativeFrame_9alignmentQrAA4AxisO3SetV_AA9AlignmentVtFQO 15SpringBoardHome08IconListC0V AA0c7AlignedgeF0V
CStrings:
+ "Cached additional app library images for %@ at %fx%f (%llu)"
+ "Cached folder mini images for %@ at %fx%f (%llu)"
+ "Cached high-priority app images for %@ at %fx%f (%llu)"
+ "Cached medium-priority app images for %@ at %fx%f (%llu)"
+ "Cached top-level app library images for %@ at %fx%f (%llu)"
+ "Cannot get icon image info for different size with non-default layout provider, using current size"
+ "Finished high-priority pre-caching in %fs (%llu)"
+ "Finished pre-caching in %fs (%llu)"
+ "Finished precaching %lu extra icon image cache configurations in %fs"
+ "Precaching extra configuration %@ "
+ "Received %lu extra icon image cache configurations for precaching"
+ "SBFolder"
+ "SBHIconImageCacheConfiguration"
+ "SBHIconServiceUtilities"
+ "SBHIconServiceUtilitiesInternal"
+ "Starting pre-caching for appearances %{public}@ (%llu)"
+ "T@\"NSString\",&,N,V_applicationBundleIdentifier"
+ "T@\"NSString\",C,N,V_preferredDisplayName"
+ "T@\"SBHIconImageStyleConfiguration\",R,C,N,V_styleConfiguration"
+ "Tq,R,N,V_iconSize"
+ "Will precache %lu configuration(s) after deduplication"
+ "_iconImageAppearancesForCacheConfiguration:"
+ "_iconImageInfoForCacheConfigurationSize:"
+ "_precacheExtraIconImages"
+ "_precacheImagesAfterChangeRunLoopObserver"
+ "_preferredDisplayName"
+ "_setInvisibilitySuppressesGlass:"
+ "_styleConfiguration"
+ "addFileStackWithURL:preferredDisplayName:"
+ "blueColor"
+ "circle"
+ "com.apple.visionproapp"
+ "fileStackIconPreferredDisplayName"
+ "https://apps.apple.com/app/id6502614761"
+ "iconManager:extraIconImageCacheConfigurationsForPrecachingWithCompletion:"
+ "initWithLeafIdentifier:applicationBundleID:preferredDisplayName:"
+ "initWithPreferredDisplayName:"
+ "initWithStyleConfiguration:iconSize:"
+ "inset.filled.circle"
+ "loadRealIconContentLayerWithInfo:traitCollection:reason:options:priority:placeholderHandler:completionHandler:"
+ "preferredDisplayName"
+ "sbh_defaultSystemImageName"
+ "sbh_isIconServicesPlaceholder"
+ "sbh_setIconServicesPlaceholder:"
+ "sbh_systemImageName"
+ "setPlaceholderIconLayer:onLayerView:iconImageInfo:traitCollection:options:"
+ "setPreferredDisplayName:"
+ "styleConfiguration"
+ "updateTraitsIfNeeded"
+ "v80@0:8@16@24{SBIconImageInfo={CGSize=dd}dd}32@64Q72"
+ "v96@0:8{SBIconImageInfo={CGSize=dd}dd}16@48@56Q64q72@?80@?88"
+ "{SBIconImageInfo={CGSize=dd}dd}24@0:8q16"
+ "\xf0\xf0\x91\xf0\xd1\xf01\xc1\xf0q"
- "Add"
- "Alarm"
- "Audio"
- "Bookmark"
- "CapturePhoto"
- "CaptureVideo"
- "Cloud"
- "ComposeNew"
- "Confirmation"
- "Contact"
- "Date"
- "Favorite"
- "Home"
- "Invitation"
- "Location"
- "Love"
- "Mail"
- "MarkLocation"
- "Message"
- "Pause"
- "Play"
- "Prohibit"
- "SBSApplicationShortcutSystemIcon_%@"
- "SBSApplicationShortcutSystemIcon_UnreadDot"
- "Share"
- "Shuffle"
- "Task"
- "TaskCompleted"
- "Time"
- "UnreadDot"
- "Update"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "loadRealIconContentLayerWithInfo:traitCollection:reason:options:priority:completionHandler:"
- "sbh_defaultImage"
- "sbh_image"
- "sbh_systemImage"
- "v88@0:8{SBIconImageInfo={CGSize=dd}dd}16@48@56Q64q72@?80"
- "\xf0\xf0\x91\xf0\xc1\xf01\xc1\xf0q"

```
