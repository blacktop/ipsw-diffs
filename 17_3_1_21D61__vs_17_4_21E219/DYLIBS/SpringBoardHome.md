## SpringBoardHome

> `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-4416.41.0.0.0
-  __TEXT.__text: 0x239ff4
-  __TEXT.__auth_stubs: 0x1640
+4416.132.102.0.0
+  __TEXT.__text: 0x23b5c0
+  __TEXT.__auth_stubs: 0x1660
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x2923c
+  __TEXT.__objc_methlist: 0x29434
   __TEXT.__const: 0x3f70
-  __TEXT.__oslogstring: 0xcf74
-  __TEXT.__cstring: 0x14bb3
-  __TEXT.__gcc_except_tab: 0x2b98
+  __TEXT.__oslogstring: 0xd048
+  __TEXT.__cstring: 0x14e56
+  __TEXT.__gcc_except_tab: 0x2bac
   __TEXT.__dlopen_cstrs: 0x39a
   __TEXT.__ustring: 0x31c
-  __TEXT.__unwind_info: 0xa010
-  __TEXT.__objc_classname: 0x573e
-  __TEXT.__objc_methname: 0x78757
-  __TEXT.__objc_methtype: 0x151db
-  __TEXT.__objc_stubs: 0x48f20
+  __TEXT.__unwind_info: 0xa068
+  __TEXT.__objc_classname: 0x5777
+  __TEXT.__objc_methname: 0x7934b
+  __TEXT.__objc_methtype: 0x15251
+  __TEXT.__objc_stubs: 0x492c0
   __DATA_CONST.__got: 0x540
-  __DATA_CONST.__const: 0x73c8
-  __DATA_CONST.__objc_classlist: 0xe18
+  __DATA_CONST.__const: 0x74a8
+  __DATA_CONST.__objc_classlist: 0xe20
   __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x860
+  __DATA_CONST.__objc_protolist: 0x868
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x79d78
-  __DATA_CONST.__objc_selrefs: 0x155a0
+  __DATA_CONST.__objc_const: 0x7a058
+  __DATA_CONST.__objc_selrefs: 0x156e0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x1538
+  __DATA_CONST.__objc_superrefs: 0xb70
   __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__cfstring: 0x13420
-  __AUTH_CONST.__objc_const: 0xa788
+  __AUTH_CONST.__cfstring: 0x13660
+  __AUTH_CONST.__objc_const: 0xa7d0
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_arrayobj: 0x150
-  __AUTH_CONST.__const: 0x1a00
+  __AUTH_CONST.__const: 0x1a20
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xb30
+  __AUTH_CONST.__auth_got: 0xb40
   __AUTH.__objc_data: 0x2e90
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x1538
-  __DATA.__objc_superrefs: 0xb68
-  __DATA.__objc_ivar: 0x2fdc
-  __DATA.__data: 0x6558
-  __DATA.__bss: 0x270
-  __DATA_DIRTY.__objc_data: 0x5e60
+  __DATA.__objc_ivar: 0x3008
+  __DATA.__data: 0x65c8
+  __DATA.__bss: 0x260
+  __DATA_DIRTY.__objc_data: 0x5eb0
   __DATA_DIRTY.__bss: 0x4b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices
   - /System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreMaterial.framework/CoreMaterial
   - /System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15896
-  Symbols:   53031
-  CStrings:  22382
+  Functions: 15944
+  Symbols:   53203
+  CStrings:  22517
 
Symbols:
+ -[SBHAnalyticsEventsController .cxx_destruct]
+ -[SBHAnalyticsEventsController addProvider:]
+ -[SBHAnalyticsEventsController allProviders]
+ -[SBHAnalyticsEventsController dealloc]
+ -[SBHAnalyticsEventsController eventsControllerDomain]
+ -[SBHAnalyticsEventsController initWithEventsControllerDomain:]
+ -[SBHAnalyticsEventsController removeProvider:]
+ -[SBHAnalyticsEventsController sendEventsForProvidersWhenSignificantTimeChanged]
+ -[SBHAnalyticsEventsController setAllProviders:]
+ -[SBHBookmarkIcon isWebAppIcon]
+ -[SBHFocusMode dockList]
+ -[SBHFocusMode setDockList:]
+ -[SBHFocusMode setSource:]
+ -[SBHFocusMode source]
+ -[SBHFocusModeManager _notifyObserversOfActiveFocusModeChange]
+ -[SBHFocusModeManager _updateDockWithActiveFocusMode:rootFolder:]
+ -[SBHFocusModeManager addObserver:]
+ -[SBHFocusModeManager applyFocusMode:]
+ -[SBHFocusModeManager cachedDock]
+ -[SBHFocusModeManager computeCurrentFocusMode]
+ -[SBHFocusModeManager donateFocusMode:fromSource:]
+ -[SBHFocusModeManager focusModesBySourceNumber]
+ -[SBHFocusModeManager observers]
+ -[SBHFocusModeManager removeObserver:]
+ -[SBHFocusModeManager setCachedDock:]
+ -[SBHIconManager configureFeedbackView:]
+ -[SBHIconManager editingDidChangeWithFeedbackBehavior:location:]
+ -[SBHIconManager setEditing:withFeedbackBehavior:location:]
+ -[SBHIconManager setIconEditingFeedbackBehavior:]
+ -[SBHLibraryPodFolderView _updateCycleIdleUntil:]
+ -[SBHLibraryPodFolderView extraIdleScrollVisibleRows]
+ -[SBHLibraryPodFolderView isRegisteredForPodScrollIdleUpdates]
+ -[SBHLibraryPodFolderView scrollingStartOffset]
+ -[SBHLibraryPodFolderView setExtraIdleScrollVisibleRows:]
+ -[SBHLibraryPodFolderView setRegisteredForPodScrollIdleUpdates:]
+ -[SBHLibraryPodFolderView setScrollingStartOffset:]
+ -[SBHSimpleApplication initWithBundleIdentifier:forcePlaceholder:]
+ -[SBHStackConfigurationInteraction stackConfigurationViewControllerShouldDisallowLabelArea:]
+ -[SBIcon(SBBookmarkIcon) isWebAppIcon]
+ -[SBIconDragManager placeholderMovementForDragHitRegion:onGridCellIndex:inListView:forDragWithIdentifier:draggedIconIdentifiers:]
+ -[SBIconListView clearDraggedIconViews]
+ -[SBIconListView removeIconView:force:]
+ -[SBIconView isAddedToDrag]
+ -[SBIconView setAddedToDrag:]
+ GCC_except_table138
+ GCC_except_table175
+ GCC_except_table185
+ GCC_except_table272
+ GCC_except_table301
+ GCC_except_table305
+ GCC_except_table335
+ GCC_except_table337
+ GCC_except_table342
+ GCC_except_table381
+ GCC_except_table485
+ GCC_except_table535
+ GCC_except_table543
+ GCC_except_table74
+ GCC_except_table97
+ _OBJC_CLASS_$_SBHAnalyticsEventsController
+ _OBJC_IVAR_$_SBHAnalyticsEventsController._allProviders
+ _OBJC_IVAR_$_SBHAnalyticsEventsController._eventsControllerDomain
+ _OBJC_IVAR_$_SBHFocusMode._dockList
+ _OBJC_IVAR_$_SBHFocusMode._source
+ _OBJC_IVAR_$_SBHFocusModeManager._cachedDock
+ _OBJC_IVAR_$_SBHFocusModeManager._focusModesBySourceNumber
+ _OBJC_IVAR_$_SBHFocusModeManager._observers
+ _OBJC_IVAR_$_SBHLibraryPodFolderView._extraIdleScrollVisibleRows
+ _OBJC_IVAR_$_SBHLibraryPodFolderView._registeredForPodScrollIdleUpdates
+ _OBJC_IVAR_$_SBHLibraryPodFolderView._scrollingStartOffset
+ _OBJC_IVAR_$_SBIconView._isAddedToDrag
+ _OBJC_METACLASS_$_SBHAnalyticsEventsController
+ _SBHAnalyticsControlCenterInvocation
+ _SBHAnalyticsControlCenterInvocationActiveDuration
+ _SBHAnalyticsControlCenterInvocationSessionID
+ _SBHAnalyticsControlCenterModuleExpansion
+ _SBHAnalyticsControlCenterModuleExpansionModuleIdentifier
+ _SBHAnalyticsControlCenterModuleExpansionSessionID
+ _SBHAnalyticsControlCenterModuleOrganization
+ _SBHAnalyticsControlCenterModuleOrganizationModuleIdentifier
+ _SBHAnalyticsControlCenterModuleOrganizationModuleRanking
+ _SBHAnalyticsDomainControlCenter
+ _SBHAnalyticsDomainHomeScreenIconLayouts
+ _SBHAnalyticsDomainHomeScreenLayoutOptimizedHomeScreen
+ _SBHAnalyticsDomainHomeScreenLayoutOptimizedHomeScreenAppsResidentInHomePercentage
+ _SBHAnalyticsDomainHomeScreenLayoutOptimizedHomeScreenNewlyDownloadedAppsToLibraryOnly
+ _SBHAnalyticsDomainSpotlight
+ _SBHAnalyticsSpotlightInvocation
+ _SBHAnalyticsSpotlightInvocationLocation
+ _SBHAnalyticsSpotlightInvocationMethod
+ __OBJC_$_INSTANCE_METHODS_SBHAnalyticsEventsController
+ __OBJC_$_INSTANCE_VARIABLES_SBHAnalyticsEventsController
+ __OBJC_$_PROP_LIST_SBHAnalyticsEventsController
+ __OBJC_$_PROP_LIST_SBHIconLaunchContext.64
+ __OBJC_$_PROP_LIST_SBHTestWidgetIconDescriptor.105
+ __OBJC_$_PROP_LIST_SBIconLabelAccessoryView.84
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIUpdateCycleIdleObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIUpdateCycleIdleObserver
+ __OBJC_$_PROTOCOL_REFS__UIUpdateCycleIdleObserver
+ __OBJC_CLASS_RO_$_SBHAnalyticsEventsController
+ __OBJC_LABEL_PROTOCOL_$__UIUpdateCycleIdleObserver
+ __OBJC_METACLASS_RO_$_SBHAnalyticsEventsController
+ __OBJC_PROTOCOL_$__UIUpdateCycleIdleObserver
+ __UIUpdateCycleRegisterIdleObserver
+ __UIUpdateCycleUnregisterIdleObserver
+ ___112-[SBIconDragManager old_iconDropSessionWithIdentifier:draggedIconIdentifiers:didPauseAtLocation:inIconListView:]_block_invoke.350
+ ___43-[SBHIconManager _precacheDataForRootIcons]_block_invoke.123
+ ___43-[SBHIconManager _precacheDataForRootIcons]_block_invoke.125
+ ___43-[SBHIconManager _precacheDataForRootIcons]_block_invoke_2.126
+ ___46-[SBHFocusModeManager computeCurrentFocusMode]_block_invoke
+ ___53-[SBHIconImageVariantCache realImageForIcon:options:]_block_invoke.223
+ ___53-[SBIconDragManager _stopTrackingDragWithIdentifier:]_block_invoke.168
+ ___53-[SBIconDragManager _stopTrackingDragWithIdentifier:]_block_invoke_3
+ ___58-[SBIconDragManager captureInitialIconStateToDragContext:]_block_invoke.228
+ ___58-[SBIconDragManager captureInitialIconStateToDragContext:]_block_invoke.228.cold.1
+ ___59-[SBHIconManager setEditing:withFeedbackBehavior:location:]_block_invoke
+ ___64-[SBHIconManager editingDidChangeWithFeedbackBehavior:location:]_block_invoke
+ ___64-[SBHSelectedApplicationDataSource applicationInstallsDidStart:]_block_invoke_2
+ ___65-[SBIconView dragInteraction:item:willAnimateCancelWithAnimator:]_block_invoke
+ ___75-[SBIconDragManager iconListView:iconDragItem:willAnimateDropWithAnimator:]_block_invoke.371
+ ___75-[SBIconDragManager iconListView:iconDragItem:willAnimateDropWithAnimator:]_block_invoke_2.372
+ ___77-[SBHFileWidgetExtensionProvider filesWidgetViewControllerWithConfiguration:]_block_invoke.130
+ ___77-[SBHIconManager _ensureWidgetIsVisibleForDebuggingWithDescriptor:sizeClass:]_block_invoke.154
+ ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.409
+ ___80-[SBHAnalyticsEventsController sendEventsForProvidersWhenSignificantTimeChanged]_block_invoke
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.492
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.495
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.498
+ ___90-[SBIconDragManager old_performIconDrop:identifier:draggedIconIdentifiers:inIconListView:]_block_invoke.363
+ ___90-[SBIconDragManager old_performIconDrop:identifier:draggedIconIdentifiers:inIconListView:]_block_invoke.364
+ ___98-[SBIconDragManager predictable_performIconDrop:identifier:draggedIconIdentifiers:inIconListView:]_block_invoke.362
+ ___block_descriptor_40_e8_32s_e37_v32?0"NSString"8"NSProgress"16^B24ls32l8
+ ___block_descriptor_48_e8_32r40r_e39_v32?0"NSNumber"8"SBHFocusMode"16^B24lr32l8r40l8
+ ___block_literal_global.1013
+ ___block_literal_global.167
+ ___block_literal_global.171
+ ___block_literal_global.174
+ ___block_literal_global.175
+ ___block_literal_global.187
+ ___block_literal_global.207
+ ___block_literal_global.2145
+ ___block_literal_global.269
+ ___block_literal_global.272
+ ___block_literal_global.274
+ ___block_literal_global.276
+ ___block_literal_global.286
+ ___block_literal_global.292
+ ___block_literal_global.299
+ ___block_literal_global.313
+ ___block_literal_global.342
+ ___block_literal_global.354
+ ___block_literal_global.366
+ ___block_literal_global.391
+ ___block_literal_global.497
+ ___block_literal_global.677
+ ___block_literal_global.706
+ ___block_literal_global.753
+ ___block_literal_global.857
+ ___block_literal_global.890
+ ___block_literal_global.960
+ _defaultContentImage.__image.171
+ _defaultContentImage.onceToken.172
+ _objc_msgSend$_notifyObserversOfActiveFocusModeChange
+ _objc_msgSend$_updateDockWithActiveFocusMode:rootFolder:
+ _objc_msgSend$allProviders
+ _objc_msgSend$applyFocusMode:
+ _objc_msgSend$clearDraggedIconViews
+ _objc_msgSend$computeCurrentFocusMode
+ _objc_msgSend$dockList
+ _objc_msgSend$donateFocusMode:fromSource:
+ _objc_msgSend$editingDidChangeWithFeedbackBehavior:location:
+ _objc_msgSend$extraIdleScrollVisibleRows
+ _objc_msgSend$focusModeManagerDidUpdateActiveFocusMode:
+ _objc_msgSend$focusModesBySourceNumber
+ _objc_msgSend$iconAtCoordinate:
+ _objc_msgSend$impactOccurredWithIntensity:atLocation:
+ _objc_msgSend$initWithBundleIdentifier:forcePlaceholder:
+ _objc_msgSend$initWithConfiguration:view:
+ _objc_msgSend$isAddedToDrag
+ _objc_msgSend$isRegisteredForPodScrollIdleUpdates
+ _objc_msgSend$isWebAppIcon
+ _objc_msgSend$needsWebAppDeletionStrings
+ _objc_msgSend$observers
+ _objc_msgSend$placeholderMovementForDragHitRegion:onGridCellIndex:inListView:forDragWithIdentifier:draggedIconIdentifiers:
+ _objc_msgSend$removeIconView:force:
+ _objc_msgSend$scrollingStartOffset
+ _objc_msgSend$setAddedToDrag:
+ _objc_msgSend$setEditing:withFeedbackBehavior:location:
+ _objc_msgSend$setExtraIdleScrollVisibleRows:
+ _objc_msgSend$setRegisteredForPodScrollIdleUpdates:
+ _objc_msgSend$setScrollingStartOffset:
+ _objc_msgSend$setSource:
+ _objc_msgSend$significantTimeChanged
+ _objc_msgSend$stackConfigurationInteractionShouldDisallowLabelArea:
+ _objc_msgSend$stackConfigurationViewControllerShouldDisallowLabelArea:
+ _sharedInstance.onceToken.77
- -[SBHIconManager editingDidChangeWithFeedbackBehavior:]
- -[SBHIconManager setEditing:withFeedbackBehavior:]
- -[SBIconDragManager placeholderMovementForDragHitRegion:onGridCellIndex:iconIndex:inListView:forDragWithIdentifier:draggedIconIdentifiers:]
- GCC_except_table137
- GCC_except_table174
- GCC_except_table184
- GCC_except_table222
- GCC_except_table246
- GCC_except_table253
- GCC_except_table271
- GCC_except_table282
- GCC_except_table299
- GCC_except_table304
- GCC_except_table333
- GCC_except_table336
- GCC_except_table380
- GCC_except_table482
- GCC_except_table532
- GCC_except_table540
- GCC_except_table58
- __OBJC_$_PROP_LIST_SBHIconLaunchContext.63
- __OBJC_$_PROP_LIST_SBHTestWidgetIconDescriptor.104
- __OBJC_$_PROP_LIST_SBIconLabelAccessoryView.83
- ___112-[SBIconDragManager old_iconDropSessionWithIdentifier:draggedIconIdentifiers:didPauseAtLocation:inIconListView:]_block_invoke.347
- ___43-[SBHIconManager _precacheDataForRootIcons]_block_invoke.122
- ___43-[SBHIconManager _precacheDataForRootIcons]_block_invoke.124
- ___43-[SBHIconManager _precacheDataForRootIcons]_block_invoke_2.125
- ___50-[SBHIconManager setEditing:withFeedbackBehavior:]_block_invoke
- ___53-[SBHIconImageVariantCache realImageForIcon:options:]_block_invoke.222
- ___53-[SBIconDragManager _stopTrackingDragWithIdentifier:]_block_invoke.167
- ___55-[SBHIconManager editingDidChangeWithFeedbackBehavior:]_block_invoke
- ___58-[SBIconDragManager captureInitialIconStateToDragContext:]_block_invoke.225
- ___58-[SBIconDragManager captureInitialIconStateToDragContext:]_block_invoke.225.cold.1
- ___75-[SBIconDragManager iconListView:iconDragItem:willAnimateDropWithAnimator:]_block_invoke.368
- ___75-[SBIconDragManager iconListView:iconDragItem:willAnimateDropWithAnimator:]_block_invoke_2.369
- ___77-[SBHFileWidgetExtensionProvider filesWidgetViewControllerWithConfiguration:]_block_invoke.129
- ___77-[SBHIconManager _ensureWidgetIsVisibleForDebuggingWithDescriptor:sizeClass:]_block_invoke.153
- ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.408
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.491
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.494
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.497
- ___90-[SBIconDragManager old_performIconDrop:identifier:draggedIconIdentifiers:inIconListView:]_block_invoke.360
- ___90-[SBIconDragManager old_performIconDrop:identifier:draggedIconIdentifiers:inIconListView:]_block_invoke.361
- ___98-[SBIconDragManager predictable_performIconDrop:identifier:draggedIconIdentifiers:inIconListView:]_block_invoke.356
- ___block_literal_global.1012
- ___block_literal_global.166
- ___block_literal_global.172
- ___block_literal_global.186
- ___block_literal_global.194
- ___block_literal_global.204
- ___block_literal_global.2138
- ___block_literal_global.268
- ___block_literal_global.270
- ___block_literal_global.271
- ___block_literal_global.283
- ___block_literal_global.289
- ___block_literal_global.296
- ___block_literal_global.312
- ___block_literal_global.339
- ___block_literal_global.351
- ___block_literal_global.363
- ___block_literal_global.388
- ___block_literal_global.496
- ___block_literal_global.676
- ___block_literal_global.705
- ___block_literal_global.752
- ___block_literal_global.78
- ___block_literal_global.856
- ___block_literal_global.889
- ___block_literal_global.959
- _defaultContentImage.__image.170
- _defaultContentImage.onceToken.171
- _objc_msgSend$_impactOccurredWithIntensity:
- _objc_msgSend$editingDidChangeWithFeedbackBehavior:
- _objc_msgSend$placeholderMovementForDragHitRegion:onGridCellIndex:iconIndex:inListView:forDragWithIdentifier:draggedIconIdentifiers:
- _objc_msgSend$setEditing:withFeedbackBehavior:
- _sharedInstance.onceToken.76
CStrings:
+ "\b\x1a8\x15!\x12\x11Q\x1d\x1f\x0e\x13\x11\x11\""
+ "\x11\x17"
+ "B24@0:8@\"SBHStackConfigurationInteraction\"16"
+ "B24@0:8@\"SBHStackConfigurationViewController\"16"
+ "SBHAnalyticsDomainControlCenter"
+ "SBHAnalyticsDomainHomeScreenIconLayouts"
+ "SBHAnalyticsDomainSpotlight"
+ "SBHAnalyticsEventsController"
+ "T@\"<SBIconListLayout>\",?,&,N"
+ "T@\"<SBIconListLayout>\",?,&,N,V_listLayout"
+ "T@\"<SBIconListViewQuerying>\",?,R"
+ "T@\"<SBIconLocationPresenting>\",?,R"
+ "T@\"<SBIconViewQuerying>\",?,R"
+ "T@\"<SBLeafIconDataSource>\",?,R,N"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSArray\",?,R,N,V_tags"
+ "T@\"NSHashTable\",&,N,V_allProviders"
+ "T@\"NSHashTable\",R,N,V_observers"
+ "T@\"NSMutableDictionary\",R,N,V_focusModesBySourceNumber"
+ "T@\"NSSet\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,C,N,V_uniqueIdentifier"
+ "T@\"NSString\",R,N,V_eventsControllerDomain"
+ "T@\"SBFParallaxSettings\",?,&,N"
+ "T@\"SBFParallaxSettings\",?,&,N,V_parallaxSettings"
+ "T@\"SBFolderIconImageCache\",?,&,N"
+ "T@\"SBHAppLibraryVisualConfiguration\",?,R,C,N"
+ "T@\"SBHFloatingDockVisualConfiguration\",?,R,C,N"
+ "T@\"SBHFloatyFolderVisualConfiguration\",?,R,C,N"
+ "T@\"SBHFolderIconVisualConfiguration\",?,R,C,N"
+ "T@\"SBHIconAccessoryVisualConfiguration\",?,R,C,N"
+ "T@\"SBHIconModel\",?,R,N"
+ "T@\"SBHLibrarySearchController\",?,W,N"
+ "T@\"SBHLibrarySearchController\",?,W,N,V_searchController"
+ "T@\"SBHRootFolderVisualConfiguration\",?,R,C,N"
+ "T@\"SBHSidebarVisualConfiguration\",?,R,C,N"
+ "T@\"SBIcon\",?,R,N"
+ "T@\"SBIcon\",?,R,N,V_icon"
+ "T@\"SBIconListModel\",&,N,V_cachedDock"
+ "T@\"SBIconListModel\",C,N,V_dockList"
+ "T@\"SBIconView\",?,&,N"
+ "T@\"SBRootFolder\",?,&,N"
+ "T@\"UIFocusEffect\",?,R,C,N"
+ "T@\"UIImpactFeedbackGenerator\",&,N,V_iconEditingFeedbackBehavior"
+ "T@\"UITapGestureRecognizer\",?,&,N"
+ "T@\"UITapGestureRecognizer\",?,&,N,V_actionTapGestureRecognizer"
+ "T@\"UIView\",?,R,N"
+ "T@\"UIView\",?,R,W,N"
+ "T@\"UIViewController\",?,&,N"
+ "T@\"UIViewController\",?,&,N,V_avocadoViewController"
+ "T@\"_UILegibilitySettings\",?,&,N"
+ "T@\"_UILegibilitySettings\",?,&,N,V_legibilitySettings"
+ "T@,?,&,N"
+ "T@,?,&,N,V_badgeValue"
+ "T@?,?,C,N"
+ "T@?,?,C,N,V_backgroundViewConfigurator"
+ "T@?,?,C,N,V_backgroundViewProvider"
+ "TB,?,N"
+ "TB,?,N,GisDropping"
+ "TB,?,N,GisEditing"
+ "TB,?,N,GisEditing,V_editing"
+ "TB,?,N,GisMainDisplayLibraryViewVisible"
+ "TB,?,N,GisOverlapping"
+ "TB,?,N,GisOverlapping,V_overlapping"
+ "TB,?,N,GisOverlayTodayViewVisible"
+ "TB,?,N,GisScrolling"
+ "TB,?,N,GisShowingContextMenu"
+ "TB,?,N,GisShowingContextMenu,V_showingContextMenu"
+ "TB,?,N,GisTrackingScroll"
+ "TB,?,N,GisUserInteractionEnabled"
+ "TB,?,N,GisUserInteractionEnabled,V_userInteractionEnabled"
+ "TB,?,N,V_automaticallyUpdatesVisiblySettled"
+ "TB,?,N,V_forcesEdgeAntialiasing"
+ "TB,?,N,V_showsSnapshotWhenDeactivated"
+ "TB,?,N,V_wantsEditingDisplayStyle"
+ "TB,?,R,N"
+ "TB,?,R,N,GisActive"
+ "TB,?,R,N,GisAppClip"
+ "TB,?,R,N,GisAppleApplication"
+ "TB,?,R,N,GisCancelable"
+ "TB,?,R,N,GisCloudDemoted"
+ "TB,?,R,N,GisDownloading"
+ "TB,?,R,N,GisFailed"
+ "TB,?,R,N,GisIconContentPossiblyVisibleOverApplication"
+ "TB,?,R,N,GisInstalling"
+ "TB,?,R,N,GisInternalApplication"
+ "TB,?,R,N,GisInternalApplication,V_internalApplication"
+ "TB,?,R,N,GisNewAppInstallFromStore"
+ "TB,?,R,N,GisPausable"
+ "TB,?,R,N,GisPaused"
+ "TB,?,R,N,GisPrioritizable"
+ "TB,?,R,N,GisRootFolderContentVisible"
+ "TB,?,R,N,GisSystemApplication"
+ "TB,?,R,N,GisSystemApplication,V_systemApplication"
+ "TB,?,R,N,GisWaiting"
+ "TB,N,GisRegisteredForPodScrollIdleUpdates,V_registeredForPodScrollIdleUpdates"
+ "TQ,?,N"
+ "TQ,?,N,V_imageViewAlignment"
+ "TQ,?,N,V_pauseReasons"
+ "TQ,?,N,V_presentationMode"
+ "TQ,?,N,V_userVisibilityStatus"
+ "TQ,?,R,N"
+ "TQ,N,V_extraIdleScrollVisibleRows"
+ "Td,?,N"
+ "Td,?,N,V_brightness"
+ "Td,?,R,N"
+ "Tq,?,R,N"
+ "Tq,N,V_source"
+ "T{CGPoint=dd},?,R,N"
+ "T{CGPoint=dd},N,V_scrollingStartOffset"
+ "T{SBHIconGridSizeClassSizes={SBHIconGridSize=SS}{SBHIconGridSize=SS}{SBHIconGridSize=SS}{SBHIconGridSize=SS}{SBHIconGridSize=SS}},?,R,N"
+ "T{SBIconApproximateLayoutPosition=QQ},?,N"
+ "T{SBIconApproximateLayoutPosition=QQ},?,N,V_approximateLayoutPosition"
+ "T{UIEdgeInsets=dddd},?,R,N"
+ "UNINSTALL_WEBAPP_BODY_DELETE_DATA"
+ "UNINSTALL_WEBAPP_TITLE"
+ "[%@] Caching original dock configuration"
+ "[%@] Configuring the dock for the active focus mode"
+ "[%@] Restoring original dock configuration"
+ "[%@] applying focus mode: %{public}@"
+ "_UIUpdateCycleIdleObserver"
+ "_allProviders"
+ "_cachedDock"
+ "_dockList"
+ "_eventsControllerDomain"
+ "_extraIdleScrollVisibleRows"
+ "_focusModesBySourceNumber"
+ "_isAddedToDrag"
+ "_notifyObserversOfActiveFocusModeChange"
+ "_registeredForPodScrollIdleUpdates"
+ "_scrollingStartOffset"
+ "_source"
+ "_updateCycleIdleUntil:"
+ "_updateDockWithActiveFocusMode:rootFolder:"
+ "activeDuration"
+ "addProvider:"
+ "allProviders"
+ "applyFocusMode:"
+ "appsResidentInHomePercentageAsInteger"
+ "cachedDock"
+ "clearDraggedIconViews"
+ "com.apple.springboardhome.controlcenter.invocation"
+ "com.apple.springboardhome.controlcenter.moduleexpansion"
+ "com.apple.springboardhome.controlcenter.moduleorganization"
+ "com.apple.springboardhome.homescreen.layout.optimizedhomescreen"
+ "com.apple.springboardhome.spotlight.invocation"
+ "computeCurrentFocusMode"
+ "configureFeedbackView:"
+ "dockList"
+ "donateFocusMode:fromSource:"
+ "editingDidChangeWithFeedbackBehavior:location:"
+ "eventsControllerDomain"
+ "extraIdleScrollVisibleRows"
+ "focusModeManagerDidUpdateActiveFocusMode:"
+ "focusModesBySourceNumber"
+ "impactOccurredWithIntensity:atLocation:"
+ "initWithBundleIdentifier:forcePlaceholder:"
+ "initWithConfiguration:view:"
+ "initWithEventsControllerDomain:"
+ "invocationLocation"
+ "invocationMethod"
+ "isAddedToDrag"
+ "isRegisteredForPodScrollIdleUpdates"
+ "isWebAppIcon"
+ "moduleIdentifier"
+ "moduleRanking"
+ "needsWebAppDeletionStrings"
+ "newlyDownloadedAppsToLibraryOnly"
+ "paused over icon = %@, coordinate = %@"
+ "placeholderMovementForDragHitRegion:onGridCellIndex:inListView:forDragWithIdentifier:draggedIconIdentifiers:"
+ "q56@0:8Q16Q24@32@40@48"
+ "registeredForPodScrollIdleUpdates"
+ "removeIconView:force:"
+ "removeProvider:"
+ "scrollingStartOffset"
+ "sendEventsForProvidersWhenSignificantTimeChanged"
+ "sessionID"
+ "setAddedToDrag:"
+ "setAllProviders:"
+ "setCachedDock:"
+ "setDockList:"
+ "setEditing:withFeedbackBehavior:location:"
+ "setExtraIdleScrollVisibleRows:"
+ "setIconEditingFeedbackBehavior:"
+ "setRegisteredForPodScrollIdleUpdates:"
+ "setScrollingStartOffset:"
+ "setSource:"
+ "significantTimeChanged"
+ "stackConfigurationInteractionShouldDisallowLabelArea:"
+ "stackConfigurationViewControllerShouldDisallowLabelArea:"
+ "v32@?0@\"NSNumber\"8@\"SBHFocusMode\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSProgress\"16^B24"
+ "v44@0:8B16@20{CGPoint=dd}28"
+ "\xf0\xf0\x91\xa1\xf0\xf0\xf0!"
- "\t\x1a8\x15!\x12\x11Q\x1c\x1f\x0e\x13\x11\x11\""
- "\x17"
- "T@\"<SBIconListLayout>\",&,N"
- "T@\"<SBIconListViewQuerying>\",R"
- "T@\"<SBIconLocationPresenting>\",R"
- "T@\"<SBIconViewQuerying>\",R"
- "T@\"NSArray\",R,N,V_tags"
- "T@\"NSSet\",C,N"
- "T@\"SBFParallaxSettings\",&,N"
- "T@\"SBFParallaxSettings\",&,N,V_parallaxSettings"
- "T@\"SBHAppLibraryVisualConfiguration\",R,C,N"
- "T@\"SBHFloatingDockVisualConfiguration\",R,C,N"
- "T@\"SBHFloatyFolderVisualConfiguration\",R,C,N"
- "T@\"SBHFolderIconVisualConfiguration\",R,C,N"
- "T@\"SBHIconAccessoryVisualConfiguration\",R,C,N"
- "T@\"SBHLibrarySearchController\",W,N"
- "T@\"SBHLibrarySearchController\",W,N,V_searchController"
- "T@\"SBHRootFolderVisualConfiguration\",R,C,N"
- "T@\"SBHSidebarVisualConfiguration\",R,C,N"
- "T@\"SBIconView\",&,N"
- "T@\"SBRootFolder\",&,N"
- "T@\"UIFocusEffect\",R,C,N"
- "T@\"UIImpactFeedbackGenerator\",R,N"
- "T@\"UITapGestureRecognizer\",&,N"
- "T@\"UIViewController\",&,N,V_avocadoViewController"
- "T@,&,N,V_badgeValue"
- "T@?,C,N,V_backgroundViewConfigurator"
- "TB,N,GisDropping"
- "TB,N,GisMainDisplayLibraryViewVisible"
- "TB,N,GisOverlayTodayViewVisible"
- "TB,N,GisScrolling"
- "TB,N,GisShowingContextMenu"
- "TB,N,GisShowingContextMenu,V_showingContextMenu"
- "TB,N,GisTrackingScroll"
- "TB,N,GisUserInteractionEnabled"
- "TB,N,GisUserInteractionEnabled,V_userInteractionEnabled"
- "TB,N,V_automaticallyUpdatesVisiblySettled"
- "TB,N,V_wantsEditingDisplayStyle"
- "TB,R,N,GisActive"
- "TB,R,N,GisAppClip"
- "TB,R,N,GisAppleApplication"
- "TB,R,N,GisCloudDemoted"
- "TB,R,N,GisDownloading"
- "TB,R,N,GisFailed"
- "TB,R,N,GisInstalling"
- "TB,R,N,GisInternalApplication"
- "TB,R,N,GisInternalApplication,V_internalApplication"
- "TB,R,N,GisNewAppInstallFromStore"
- "TB,R,N,GisPaused"
- "TB,R,N,GisSystemApplication"
- "TB,R,N,GisSystemApplication,V_systemApplication"
- "TB,R,N,GisWaiting"
- "TQ,N,V_imageViewAlignment"
- "TQ,N,V_pauseReasons"
- "TQ,N,V_presentationMode"
- "T{SBIconApproximateLayoutPosition=QQ},N"
- "_impactOccurredWithIntensity:"
- "editingDidChangeWithFeedbackBehavior:"
- "placeholderMovementForDragHitRegion:onGridCellIndex:iconIndex:inListView:forDragWithIdentifier:draggedIconIdentifiers:"
- "q64@0:8Q16Q24Q32@40@48@56"
- "setEditing:withFeedbackBehavior:"
- "\xf0\xf0\xa1\xa1\xf0\xf0\xf0\x11"

```
