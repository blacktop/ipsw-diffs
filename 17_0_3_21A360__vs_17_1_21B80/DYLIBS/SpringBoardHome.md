## SpringBoardHome

> `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-4416.11.7.0.0
-  __TEXT.__text: 0x237d14
+4416.25.105.0.0
+  __TEXT.__text: 0x2392e4
   __TEXT.__auth_stubs: 0x1640
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x28fb4
+  __TEXT.__objc_methlist: 0x2914c
   __TEXT.__const: 0x3f70
-  __TEXT.__oslogstring: 0xcee8
-  __TEXT.__cstring: 0x14a8f
-  __TEXT.__gcc_except_tab: 0x2be0
+  __TEXT.__oslogstring: 0xcfd4
+  __TEXT.__cstring: 0x14adc
+  __TEXT.__gcc_except_tab: 0x2bcc
   __TEXT.__dlopen_cstrs: 0x39a
   __TEXT.__ustring: 0x31c
-  __TEXT.__unwind_info: 0x9fa4
-  __TEXT.__objc_classname: 0x573c
-  __TEXT.__objc_methname: 0x77bc3
-  __TEXT.__objc_methtype: 0x150e2
-  __TEXT.__objc_stubs: 0x48a00
+  __TEXT.__unwind_info: 0x9ff0
+  __TEXT.__objc_classname: 0x573d
+  __TEXT.__objc_methname: 0x7816f
+  __TEXT.__objc_methtype: 0x15114
+  __TEXT.__objc_stubs: 0x48d20
   __DATA_CONST.__got: 0x540
   __DATA_CONST.__const: 0x7448
   __DATA_CONST.__objc_classlist: 0xe18
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x860
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x79518
-  __DATA_CONST.__objc_selrefs: 0x15430
+  __DATA_CONST.__objc_const: 0x79b08
+  __DATA_CONST.__objc_selrefs: 0x15500
   __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__cfstring: 0x13300
+  __AUTH_CONST.__cfstring: 0x13340
   __AUTH_CONST.__objc_const: 0xa788
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_arrayobj: 0x150

   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xb30
-  __AUTH.__objc_data: 0x2e40
+  __AUTH.__objc_data: 0x2e90
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x1530
+  __DATA.__objc_classrefs: 0x1538
   __DATA.__objc_superrefs: 0xb68
-  __DATA.__objc_ivar: 0x2f90
+  __DATA.__objc_ivar: 0x2fbc
   __DATA.__data: 0x6558
   __DATA.__bss: 0x270
-  __DATA_DIRTY.__objc_data: 0x5eb0
+  __DATA_DIRTY.__objc_data: 0x5e60
   __DATA_DIRTY.__bss: 0x4b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3AE0A6FC-A688-34B1-8759-19419CA759C2
-  Functions: 15834
-  Symbols:   52847
-  CStrings:  24746
+  UUID: 0B6AAFD4-0394-37B0-BC66-49B28CD88BCF
+  Functions: 15875
+  Symbols:   52968
+  CStrings:  24797
 
Symbols:
+ -[SBFolderController setWasFolderCancelable:]
+ -[SBFolderController wasFolderCancelable]
+ -[SBHIconManager verticalMarginPercentageForConfigurationOfIconView:]
+ -[SBHLibraryZoomAnimator pauseLayoutAssertions]
+ -[SBHLibraryZoomAnimator setPauseLayoutAssertions:]
+ -[SBHStackConfigurationViewController verticalMarginPercentageForConfigurationOfIconView:]
+ -[SBHWidgetContainerViewController _addDeactivationSnapshotViewIfNecessary]
+ -[SBHWidgetContainerViewController isWidgetControllerActive]
+ -[SBHWidgetContainerViewController setWidgetControllerActive:]
+ -[SBIconDragContext destinationStackIconViewPauseLayoutAssertion]
+ -[SBIconDragContext setDestinationStackIconViewPauseLayoutAssertion:]
+ -[SBIconDragManager adjustedLocationForDropSession:inView:]
+ -[SBIconDragManager configureIconView:]
+ -[SBIconListModel canUseFastGridLayoutValidity]
+ -[SBIconListModel countOfNonDefaultSizeClassIcons]
+ -[SBIconListModel isGridLayoutValidWithOptions:outOfBoundsIcons:]
+ -[SBIconListModel setCountOfNonDefaultSizeClassIcons:]
+ -[SBIconListView folder:didAddIcons:removedIcons:]
+ -[SBIconListView folderCancelableDidChange:]
+ -[SBIconListView pauseLayoutForIconView:forReason:]
+ -[SBIconListView removePauseLayoutAssertion:]
+ -[SBIconListViewPauseLayoutAssertion .cxx_destruct]
+ -[SBIconListViewPauseLayoutAssertion dealloc]
+ -[SBIconListViewPauseLayoutAssertion dealloc].cold.1
+ -[SBIconListViewPauseLayoutAssertion descriptionBuilderWithMultilinePrefix:]
+ -[SBIconListViewPauseLayoutAssertion descriptionWithMultilinePrefix:]
+ -[SBIconListViewPauseLayoutAssertion description]
+ -[SBIconListViewPauseLayoutAssertion iconView]
+ -[SBIconListViewPauseLayoutAssertion initWithListView:iconView:reason:]
+ -[SBIconListViewPauseLayoutAssertion invalidate]
+ -[SBIconListViewPauseLayoutAssertion isInvalidated]
+ -[SBIconListViewPauseLayoutAssertion listView]
+ -[SBIconListViewPauseLayoutAssertion reason]
+ -[SBIconListViewPauseLayoutAssertion setInvalidated:]
+ -[SBIconListViewPauseLayoutAssertion succinctDescriptionBuilder]
+ -[SBIconListViewPauseLayoutAssertion succinctDescription]
+ -[SBIconRotationContainer borrowExistingIconViewForIcon:]
+ -[SBIconRotationContainer borrowedIconView]
+ -[SBIconRotationContainer existingIconPauseLayoutAssertion]
+ -[SBIconRotationContainer initWithFrame:startIcon:endIcon:listView:coordinate:location:transitionAnimation:offscreen:]
+ -[SBIconRotationContainer listView]
+ -[SBIconRotationContainer setBorrowedIconView:]
+ -[SBIconRotationContainer setExistingIconPauseLayoutAssertion:]
+ -[SBIconRotationContainer setListView:]
+ -[SBIconView verticalMarginPercentageForConfigurationInteraction:]
+ GCC_except_table110
+ GCC_except_table121
+ GCC_except_table133
+ GCC_except_table174
+ GCC_except_table187
+ GCC_except_table192
+ GCC_except_table196
+ GCC_except_table230
+ GCC_except_table237
+ GCC_except_table242
+ GCC_except_table247
+ GCC_except_table254
+ GCC_except_table263
+ GCC_except_table269
+ GCC_except_table271
+ GCC_except_table282
+ GCC_except_table283
+ GCC_except_table296
+ GCC_except_table300
+ GCC_except_table304
+ GCC_except_table315
+ GCC_except_table317
+ GCC_except_table318
+ GCC_except_table329
+ GCC_except_table330
+ GCC_except_table337
+ GCC_except_table348
+ GCC_except_table354
+ GCC_except_table37
+ GCC_except_table380
+ GCC_except_table479
+ GCC_except_table529
+ GCC_except_table537
+ GCC_except_table555
+ GCC_except_table565
+ GCC_except_table571
+ GCC_except_table573
+ GCC_except_table575
+ GCC_except_table577
+ GCC_except_table579
+ GCC_except_table582
+ GCC_except_table584
+ GCC_except_table586
+ GCC_except_table588
+ GCC_except_table593
+ GCC_except_table596
+ GCC_except_table599
+ GCC_except_table602
+ GCC_except_table65
+ GCC_except_table662
+ GCC_except_table67
+ GCC_except_table711
+ GCC_except_table771
+ GCC_except_table791
+ GCC_except_table808
+ GCC_except_table826
+ GCC_except_table84
+ _OBJC_CLASS_$_SBFTestUtilities
+ _OBJC_CLASS_$_SBIconListViewPauseLayoutAssertion
+ _OBJC_IVAR_$_SBFolderController._wasFolderCancelable
+ _OBJC_IVAR_$_SBHIconLibraryQuery._queryId
+ _OBJC_IVAR_$_SBHLibraryZoomAnimator._pauseLayoutAssertions
+ _OBJC_IVAR_$_SBHWidgetContainerViewController._widgetControllerActive
+ _OBJC_IVAR_$_SBIconDragContext._destinationStackIconViewPauseLayoutAssertion
+ _OBJC_IVAR_$_SBIconListModel._countOfNonDefaultSizeClassIcons
+ _OBJC_IVAR_$_SBIconListView._pausedLayoutAssertionsForIconViews
+ _OBJC_IVAR_$_SBIconListViewPauseLayoutAssertion._iconView
+ _OBJC_IVAR_$_SBIconListViewPauseLayoutAssertion._invalidated
+ _OBJC_IVAR_$_SBIconListViewPauseLayoutAssertion._listView
+ _OBJC_IVAR_$_SBIconListViewPauseLayoutAssertion._reason
+ _OBJC_IVAR_$_SBIconRotationContainer._borrowedIconView
+ _OBJC_IVAR_$_SBIconRotationContainer._existingIconPauseLayoutAssertion
+ _OBJC_IVAR_$_SBIconRotationContainer._listView
+ _OBJC_METACLASS_$_SBIconListViewPauseLayoutAssertion
+ __OBJC_$_INSTANCE_METHODS_SBIconListViewPauseLayoutAssertion
+ __OBJC_$_INSTANCE_VARIABLES_SBIconListViewPauseLayoutAssertion
+ __OBJC_$_PROP_LIST_SBHLibraryZoomAnimator
+ __OBJC_$_PROP_LIST_SBIconListViewPauseLayoutAssertion
+ __OBJC_CLASS_PROTOCOLS_$_SBIconListViewPauseLayoutAssertion
+ __OBJC_CLASS_RO_$_SBIconListViewPauseLayoutAssertion
+ __OBJC_METACLASS_RO_$_SBIconListViewPauseLayoutAssertion
+ ___115-[SBIconListModel iconGridCellInfoBySimulatingInsertionOfIcons:ignoringPlaceholders:gridCellInfoOptions:iconOrder:]_block_invoke.67
+ ___39-[SBIconDragManager configureIconView:]_block_invoke
+ ___50-[SBFloatingDockViewController libraryPodIconView]_block_invoke
+ ___59-[SBIconListView layoutIconsIfNeededUsingAnimator:options:]_block_invoke.83
+ ___59-[SBIconListView layoutIconsIfNeededUsingAnimator:options:]_block_invoke_2.89
+ ___62-[SBIconListView regenerateTemporaryDisplayedModelIfNecessary]_block_invoke_4
+ ___62-[SBIconListView regenerateTemporaryDisplayedModelIfNecessary]_block_invoke_5
+ ___64-[SBIconListModel setIcons:gridCellInfoOptions:mutationOptions:]_block_invoke_2
+ ___65-[SBIconListModel isGridLayoutValidWithOptions:outOfBoundsIcons:]_block_invoke
+ ___76-[SBIconListModel _invalidateLayoutWithGridCellInfoOptions:mutationOptions:]_block_invoke_2
+ ___block_descriptor_96_e8_32s40s48s56s_e50_v40?0"SBIcon"8"SBIcon"16{SBIconCoordinate=qq}24ls32l8s40l8s48l8s56l8
+ ___block_literal_global.1007
+ ___block_literal_global.103
+ ___block_literal_global.114
+ ___block_literal_global.128
+ ___block_literal_global.152
+ ___block_literal_global.160
+ ___block_literal_global.162
+ ___block_literal_global.165
+ ___block_literal_global.182
+ ___block_literal_global.184
+ ___block_literal_global.193
+ ___block_literal_global.195
+ ___block_literal_global.198
+ ___block_literal_global.208
+ ___block_literal_global.2129
+ ___block_literal_global.233
+ ___block_literal_global.306
+ ___block_literal_global.312
+ ___block_literal_global.674
+ ___block_literal_global.745
+ ___block_literal_global.81
+ ___block_literal_global.849
+ ___block_literal_global.884
+ ___block_literal_global.954
+ _objc_msgSend$_addDeactivationSnapshotViewIfNecessary
+ _objc_msgSend$_notifyListObserversDidReplaceIcon:withIcon:
+ _objc_msgSend$borrowExistingIconViewForIcon:
+ _objc_msgSend$borrowedIconView
+ _objc_msgSend$canUseFastGridLayoutValidity
+ _objc_msgSend$configureIconView:
+ _objc_msgSend$countOfNonDefaultSizeClassIcons
+ _objc_msgSend$destinationStackIconViewPauseLayoutAssertion
+ _objc_msgSend$existingIconPauseLayoutAssertion
+ _objc_msgSend$folderCancelableDidChange:
+ _objc_msgSend$iconManager:backgroundViewForComponentsOfType:forIconView:
+ _objc_msgSend$iconManager:verticalMarginPercentageForConfigurationOfIconView:
+ _objc_msgSend$initWithFrame:startIcon:endIcon:listView:coordinate:location:transitionAnimation:offscreen:
+ _objc_msgSend$initWithListView:iconView:reason:
+ _objc_msgSend$isGridLayoutValidWithOptions:outOfBoundsIcons:
+ _objc_msgSend$isRunningXCTest
+ _objc_msgSend$isWidgetControllerActive
+ _objc_msgSend$pauseLayoutAssertions
+ _objc_msgSend$pauseLayoutForIconView:forReason:
+ _objc_msgSend$pointScale
+ _objc_msgSend$removePauseLayoutAssertion:
+ _objc_msgSend$setBorrowedIconView:
+ _objc_msgSend$setCountOfNonDefaultSizeClassIcons:
+ _objc_msgSend$setDestinationStackIconViewPauseLayoutAssertion:
+ _objc_msgSend$setExistingIconPauseLayoutAssertion:
+ _objc_msgSend$setListView:
+ _objc_msgSend$setPauseLayoutAssertions:
+ _objc_msgSend$setWasFolderCancelable:
+ _objc_msgSend$setWidgetControllerActive:
+ _objc_msgSend$verticalMarginPercentageForConfigurationInteraction:
+ _objc_msgSend$verticalMarginPercentageForConfigurationOfIconView:
+ _objc_msgSend$wasFolderCancelable
- -[SBIconListRotationIconViewProvider .cxx_destruct]
- -[SBIconListRotationIconViewProvider configureIconView:forIcon:]
- -[SBIconListRotationIconViewProvider dequeueReusableIconViewOfClass:]
- -[SBIconListRotationIconViewProvider initWithListView:]
- -[SBIconListRotationIconViewProvider isIconViewRecycled:]
- -[SBIconListRotationIconViewProvider listView]
- -[SBIconListRotationIconViewProvider recycleIconView:]
- -[SBIconListView pauseLayout:forIconView:withReason:]
- -[SBIconRotationContainer iconViewProvider]
- -[SBIconRotationContainer initWithFrame:startIcon:endIcon:iconViewProvider:coordinate:location:transitionAnimation:offscreen:]
- -[SBIconRotationContainer setIconViewProvider:]
- GCC_except_table109
- GCC_except_table130
- GCC_except_table132
- GCC_except_table156
- GCC_except_table158
- GCC_except_table168
- GCC_except_table186
- GCC_except_table191
- GCC_except_table195
- GCC_except_table212
- GCC_except_table229
- GCC_except_table236
- GCC_except_table241
- GCC_except_table250
- GCC_except_table262
- GCC_except_table268
- GCC_except_table279
- GCC_except_table292
- GCC_except_table297
- GCC_except_table301
- GCC_except_table303
- GCC_except_table314
- GCC_except_table316
- GCC_except_table324
- GCC_except_table325
- GCC_except_table327
- GCC_except_table340
- GCC_except_table347
- GCC_except_table353
- GCC_except_table377
- GCC_except_table478
- GCC_except_table528
- GCC_except_table536
- GCC_except_table554
- GCC_except_table564
- GCC_except_table570
- GCC_except_table572
- GCC_except_table574
- GCC_except_table576
- GCC_except_table578
- GCC_except_table581
- GCC_except_table583
- GCC_except_table585
- GCC_except_table587
- GCC_except_table592
- GCC_except_table595
- GCC_except_table598
- GCC_except_table601
- GCC_except_table661
- GCC_except_table710
- GCC_except_table770
- GCC_except_table790
- GCC_except_table807
- GCC_except_table825
- GCC_except_table83
- _OBJC_CLASS_$_SBIconListRotationIconViewProvider
- _OBJC_IVAR_$_SBIconListRotationIconViewProvider._listView
- _OBJC_IVAR_$_SBIconListView._pausedLayoutForIconViews
- _OBJC_IVAR_$_SBIconRotationContainer._iconViewProvider
- _OBJC_METACLASS_$_SBIconListRotationIconViewProvider
- __OBJC_$_INSTANCE_METHODS_SBIconListRotationIconViewProvider
- __OBJC_$_INSTANCE_VARIABLES_SBIconListRotationIconViewProvider
- __OBJC_$_PROP_LIST_SBIconListRotationIconViewProvider
- __OBJC_CLASS_PROTOCOLS_$_SBIconListRotationIconViewProvider
- __OBJC_CLASS_RO_$_SBIconListRotationIconViewProvider
- __OBJC_METACLASS_RO_$_SBIconListRotationIconViewProvider
- ___115-[SBIconListModel iconGridCellInfoBySimulatingInsertionOfIcons:ignoringPlaceholders:gridCellInfoOptions:iconOrder:]_block_invoke.63
- ___58-[SBIconListModel directlyContainsNonDefaultSizeClassIcon]_block_invoke
- ___59-[SBIconListView layoutIconsIfNeededUsingAnimator:options:]_block_invoke.81
- ___59-[SBIconListView layoutIconsIfNeededUsingAnimator:options:]_block_invoke_2.87
- ___block_descriptor_104_e8_32s40s48s56s64s_e50_v40?0"SBIcon"8"SBIcon"16{SBIconCoordinate=qq}24ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.100
- ___block_literal_global.1003
- ___block_literal_global.111
- ___block_literal_global.113
- ___block_literal_global.124
- ___block_literal_global.150
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.164
- ___block_literal_global.169
- ___block_literal_global.181
- ___block_literal_global.190
- ___block_literal_global.192
- ___block_literal_global.194
- ___block_literal_global.197
- ___block_literal_global.2125
- ___block_literal_global.266
- ___block_literal_global.304
- ___block_literal_global.310
- ___block_literal_global.672
- ___block_literal_global.741
- ___block_literal_global.845
- ___block_literal_global.880
- ___block_literal_global.950
- _objc_msgSend$initWithFrame:startIcon:endIcon:iconViewProvider:coordinate:location:transitionAnimation:offscreen:
- _objc_msgSend$initWithListView:
- _objc_msgSend$insertSubview:above:
- _objc_msgSend$insertSubview:below:
- _objc_msgSend$isTrackingDragWithGhostTreatmentForIcon:
- _objc_msgSend$pauseLayout:forIconView:withReason:
- _objc_msgSend$setClipsSubviews:
CStrings:
+ "\x0f\x05D\x18\x12\x13"
+ "\x11\x13\x11"
+ "Clearing recipient icon"
+ "Drag preview target does not have a window"
+ "SBIconListViewPauseLayoutAssertion"
+ "SBIconListViewPauseLayoutAssertion deallocated but not invalidated! Reason: %@"
+ "SBIconListViewPauseLayoutAssertion deallocated but not invalidated! Reason: %{public}@"
+ "T@\"<BSInvalidatable>\",&,N,V_destinationStackIconViewPauseLayoutAssertion"
+ "T@\"<BSInvalidatable>\",&,N,V_existingIconPauseLayoutAssertion"
+ "T@\"NSArray\",C,N,V_pauseLayoutAssertions"
+ "T@\"SBIconListView\",W,N,V_listView"
+ "T@\"SBIconView\",&,N,V_borrowedIconView"
+ "TB,N,GisWidgetControllerActive,V_widgetControllerActive"
+ "TB,N,V_wasFolderCancelable"
+ "TQ,N,V_countOfNonDefaultSizeClassIcons"
+ "U\x11\xd6"
+ "_addDeactivationSnapshotViewIfNecessary"
+ "_borrowedIconView"
+ "_countOfNonDefaultSizeClassIcons"
+ "_destinationStackIconViewPauseLayoutAssertion"
+ "_existingIconPauseLayoutAssertion"
+ "_pauseLayoutAssertions"
+ "_pausedLayoutAssertionsForIconViews"
+ "_queryId"
+ "_wasFolderCancelable"
+ "_widgetControllerActive"
+ "adjustedLocationForDropSession:inView:"
+ "borrowExistingIconViewForIcon:"
+ "borrowedIconView"
+ "canUseFastGridLayoutValidity"
+ "configureIconView:"
+ "countOfNonDefaultSizeClassIcons"
+ "d24@0:8@\"<SBHIconViewConfigurationInteraction>\"16"
+ "destinationStackIconViewPauseLayoutAssertion"
+ "existingIconPauseLayoutAssertion"
+ "folderCancelableDidChange:"
+ "iconManager:backgroundViewForComponentsOfType:forIconView:"
+ "iconManager:verticalMarginPercentageForConfigurationOfIconView:"
+ "initWithFrame:startIcon:endIcon:listView:coordinate:location:transitionAnimation:offscreen:"
+ "initWithListView:iconView:reason:"
+ "isGridLayoutValidWithOptions:outOfBoundsIcons:"
+ "isRunningXCTest"
+ "isWidgetControllerActive"
+ "missing folder"
+ "moving drag placeholder movement to 'overlapping' due to proximity to placeholder"
+ "pauseLayoutAssertions"
+ "pauseLayoutForIconView:forReason:"
+ "pointScale"
+ "queryId"
+ "removePauseLayoutAssertion:"
+ "rotation"
+ "setBorrowedIconView:"
+ "setCountOfNonDefaultSizeClassIcons:"
+ "setDestinationStackIconViewPauseLayoutAssertion:"
+ "setExistingIconPauseLayoutAssertion:"
+ "setListView:"
+ "setPauseLayoutAssertions:"
+ "setWasFolderCancelable:"
+ "setWidgetControllerActive:"
+ "verticalMarginPercentageForConfigurationInteraction:"
+ "verticalMarginPercentageForConfigurationOfIconView:"
+ "wasFolderCancelable"
+ "widgetControllerActive"
- "\x0f\x05D\x18\x12\x12"
- "\x11\x12"
- "SBIconListRotationIconViewProvider"
- "T@\"SBIconListView\",R,W,N,V_listView"
- "U\x11\xd5"
- "_pausedLayoutForIconViews"
- "initWithFrame:startIcon:endIcon:iconViewProvider:coordinate:location:transitionAnimation:offscreen:"
- "initWithListView:"
- "insertSubview:above:"
- "insertSubview:below:"
- "pauseLayout:forIconView:withReason:"
- "setClipsSubviews:"

```
