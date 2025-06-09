## CameraEffectsKit

> `/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`

```diff

-6307.0.1.0.0
-  __TEXT.__text: 0x10ab88
-  __TEXT.__auth_stubs: 0x1c50
-  __TEXT.__objc_methlist: 0x12764
-  __TEXT.__const: 0x1a80
+6309.0.0.0.0
+  __TEXT.__text: 0x109788
+  __TEXT.__auth_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0x124b4
+  __TEXT.__const: 0x1a90
   __TEXT.__gcc_except_tab: 0x277c
-  __TEXT.__cstring: 0x67ac
-  __TEXT.__oslogstring: 0x803e
-  __TEXT.__unwind_info: 0x4608
-  __TEXT.__objc_classname: 0x208b
-  __TEXT.__objc_methname: 0x38095
-  __TEXT.__objc_methtype: 0xab2e
-  __TEXT.__objc_stubs: 0x24780
-  __DATA_CONST.__got: 0x1a20
-  __DATA_CONST.__const: 0x36d0
-  __DATA_CONST.__objc_classlist: 0x6c0
+  __TEXT.__cstring: 0x6821
+  __TEXT.__oslogstring: 0x8146
+  __TEXT.__unwind_info: 0x45b0
+  __TEXT.__objc_classname: 0x1fe9
+  __TEXT.__objc_methname: 0x37c2c
+  __TEXT.__objc_methtype: 0xaad1
+  __TEXT.__objc_stubs: 0x243a0
+  __DATA_CONST.__got: 0x1a28
+  __DATA_CONST.__const: 0x36f0
+  __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x2f8
+  __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf60
-  __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x580
+  __DATA_CONST.__objc_selrefs: 0xae68
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0x240
-  __AUTH_CONST.__auth_got: 0xe40
-  __AUTH_CONST.__const: 0x12a8
-  __AUTH_CONST.__cfstring: 0x6680
-  __AUTH_CONST.__objc_const: 0x29848
+  __AUTH_CONST.__auth_got: 0xe38
+  __AUTH_CONST.__const: 0x12e8
+  __AUTH_CONST.__cfstring: 0x6660
+  __AUTH_CONST.__objc_const: 0x29880
   __AUTH_CONST.__objc_intobj: 0x720
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0x4060
-  __DATA.__objc_ivar: 0x14e4
-  __DATA.__data: 0x2790
-  __DATA.__bss: 0xa80
+  __DATA.__objc_ivar: 0x14b4
+  __DATA.__data: 0x2670
+  __DATA.__bss: 0xa70
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/ARKit.framework/ARKit
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E538BA7C-0D85-3D6A-936E-ADEE2E68FB79
-  Functions: 7223
-  Symbols:   25383
-  CStrings:  11960
+  UUID: 5F642B5A-147D-367D-8174-A7EA42A4F63E
+  Functions: 7182
+  Symbols:   25200
+  CStrings:  11906
 
Symbols:
+ -[CFXCameraViewController showMemojiPicker:]
+ -[CFXCameraViewController showMemojiPicker:].cold.1
+ -[CFXEffectBrowserViewController CFX_updateAVTAvatarPickerforViewController:]
+ -[CFXEffectBrowserViewController compactDetentIdentifier]
+ -[CFXEffectBrowserViewController didDismissMemojiPicker]
+ -[CFXEffectBrowserViewController didDismissMemojiPicker].cold.1
+ -[CFXEffectBrowserViewController hideBrowserAnimated:completion:].cold.1
+ -[CFXEffectBrowserViewController memojiPicker]
+ -[CFXEffectBrowserViewController refreshEffectBrowserForCameraFlip].cold.1
+ -[CFXEffectBrowserViewController setCompactDetentIdentifier:]
+ -[CFXEffectBrowserViewController setMemojiPicker:]
+ -[CFXEffectBrowserViewController showMemojiPicker:]
+ -[CFXEffectBrowserViewController showMemojiPicker:].cold.1
+ -[CFXMemojiPickerViewController .cxx_destruct]
+ -[CFXMemojiPickerViewController avatarPickerDelegate]
+ -[CFXMemojiPickerViewController avatarPicker]
+ -[CFXMemojiPickerViewController beginHidingInterfaceWithMessage:]
+ -[CFXMemojiPickerViewController close:]
+ -[CFXMemojiPickerViewController delegate]
+ -[CFXMemojiPickerViewController effectType]
+ -[CFXMemojiPickerViewController endHidingInterface]
+ -[CFXMemojiPickerViewController init]
+ -[CFXMemojiPickerViewController messagePrompt]
+ -[CFXMemojiPickerViewController selectAvatarRecordWithIdentifier:animated:]
+ -[CFXMemojiPickerViewController setAvatarPicker:]
+ -[CFXMemojiPickerViewController setAvatarPickerDelegate:]
+ -[CFXMemojiPickerViewController setDelegate:]
+ -[CFXMemojiPickerViewController setMessagePrompt:]
+ -[CFXMemojiPickerViewController viewDidDisappear:]
+ -[CFXMemojiPickerViewController viewDidLayoutSubviews]
+ -[CFXMemojiPickerViewController viewDidLoad]
+ -[CFXReviewViewController showMemojiPicker:]
+ -[CFXReviewViewController showMemojiPicker:].cold.1
+ -[JFXAnimojiEffectRenderer JFX_focalLengthForFrame:renderer:workingSize:interfaceOrientation:]
+ GCC_except_table32
+ _OBJC_CLASS_$_AVTFunCamAvatarPickerController
+ _OBJC_CLASS_$_AVTFunCamAvatarPickerStyle
+ _OBJC_CLASS_$_AVTUIColorRepository
+ _OBJC_CLASS_$_CFXMemojiPickerViewController
+ _OBJC_CLASS_$_UISheetPresentationControllerDetent
+ _OBJC_IVAR_$_CFXEffectBrowserViewController._compactDetentIdentifier
+ _OBJC_IVAR_$_CFXEffectBrowserViewController._memojiPicker
+ _OBJC_IVAR_$_CFXMemojiPickerViewController._avatarPicker
+ _OBJC_IVAR_$_CFXMemojiPickerViewController._delegate
+ _OBJC_IVAR_$_CFXMemojiPickerViewController._messagePrompt
+ _OBJC_METACLASS_$_CFXMemojiPickerViewController
+ __OBJC_$_INSTANCE_METHODS_CFXMemojiPickerViewController
+ __OBJC_$_INSTANCE_VARIABLES_CFXMemojiPickerViewController
+ __OBJC_$_PROP_LIST_CFXMemojiPickerViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CFXMemojiPickerViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CFXMemojiPickerViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CFXMemojiPickerViewController
+ __OBJC_CLASS_RO_$_CFXMemojiPickerViewController
+ __OBJC_LABEL_PROTOCOL_$_CFXMemojiPickerViewControllerDelegate
+ __OBJC_METACLASS_RO_$_CFXMemojiPickerViewController
+ __OBJC_PROTOCOL_$_CFXMemojiPickerViewControllerDelegate
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__111__sift_downB8ne200100INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_OT0_NS_15iterator_traitsIS6_E15difference_typeES6_
+ __ZNSt3__116__insertion_sortB8ne200100INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_S6_T0_
+ __ZNSt3__117__assoc_sub_state15__attach_futureB8ne200100Ev
+ __ZNSt3__117__floyd_sift_downB8ne200100INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEET1_S6_OT0_NS_15iterator_traitsIS6_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI8EdgeLineEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__partial_sort_implB8ne200100INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineS5_EET1_S6_S6_T2_OT0_
+ __ZNSt3__120__throw_future_errorB8ne200100ENS_11future_errcE
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__126__insertion_sort_unguardedB8ne200100INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_S6_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEbT1_S6_T0_
+ __ZNSt3__131__partition_with_equals_on_leftB8ne200100INS_17_ClassicAlgPolicyEP8EdgeLineR11cmpEdgeLineEET0_S6_S6_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8ne200100INS_17_ClassicAlgPolicyEP8EdgeLineR11cmpEdgeLineEENS_4pairIT0_bEES7_S7_T1_
+ __ZNSt3__14swapB8ne200100IU8__strongPU21objcproto10MTLTexture11objc_objectEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS5_EE5valueEvE4typeERS5_S8_
+ __ZNSt3__16vectorI8EdgeLineNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI8EdgeLineNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB8ne200100ERKi
+ __ZNSt3__17__sort3B8ne200100INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineLi0EEEbT1_S6_S6_T0_
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineLi0EEEvT1_S6_S6_S6_S6_T0_
+ __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_S6_OT0_NS_15iterator_traitsIS6_E15difference_typeE
+ __ZSt18make_exception_ptrB8ne200100INSt3__112future_errorEESt13exception_ptrT_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZZSt18make_exception_ptrB8ne200100INSt3__112future_errorEESt13exception_ptrT_ENUlPvE_8__invokeES4_
+ ___39-[CFXMemojiPickerViewController close:]_block_invoke
+ ___51-[CFXEffectBrowserViewController showMemojiPicker:]_block_invoke
+ ___51-[CFXEffectBrowserViewController showMemojiPicker:]_block_invoke_2
+ ___59-[CFXEffectBrowserViewController compactCurrentMessagesApp]_block_invoke
+ ___65-[CFXEffectBrowserViewController hideBrowserAnimated:completion:]_block_invoke
+ ___77-[CFXEffectBrowserViewController CFX_updateAVTAvatarPickerforViewController:]_block_invoke
+ ___77-[CFXEffectBrowserViewController CFX_updateAVTAvatarPickerforViewController:]_block_invoke_2
+ ___block_descriptor_32_e64_d16?0"<UISheetPresentationControllerDetentResolutionContext>"8l
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e41_v32?0"NSString"8^B16?<v?"NSArray">24ls32l8
+ _objc_msgSend$CFX_updateAVTAvatarPickerforViewController:
+ _objc_msgSend$JFX_focalLengthForFrame:renderer:workingSize:interfaceOrientation:
+ _objc_msgSend$_cek_applyBlendshapeWeightsInHierarchyUsingBlock:
+ _objc_msgSend$_cek_beginTransaction
+ _objc_msgSend$_cek_commitTransaction
+ _objc_msgSend$_cek_currentPointOfViewSensorHeight
+ _objc_msgSend$_cek_fetchBlendshapeWeightsInHierarchyUsingBlock:
+ _objc_msgSend$_cek_renderAtTime:enableAntialiasing:viewport:commandBuffer:passDescriptor:
+ _objc_msgSend$_cek_rendererWithDevice:options:
+ _objc_msgSend$_cek_setCurrentPointOfViewFocalLength:
+ _objc_msgSend$addConstraints:
+ _objc_msgSend$animateChanges:
+ _objc_msgSend$appBackgroundColor
+ _objc_msgSend$avatarPicker
+ _objc_msgSend$avatarPickerDelegate
+ _objc_msgSend$boldSystemFontOfSize:
+ _objc_msgSend$compactDetentIdentifier
+ _objc_msgSend$customDetentWithIdentifier:resolver:
+ _objc_msgSend$didDismissMemojiPicker
+ _objc_msgSend$didSelectAppWithBundleIdentifier:
+ _objc_msgSend$dismissViewControllerAnimated:completion:
+ _objc_msgSend$funCamAvatarPickerControllerForStore:style:allowsCreation:
+ _objc_msgSend$initWithCellSize:engagedCellSize:interitemSpacing:gridEdgeInsets:
+ _objc_msgSend$largeDetent
+ _objc_msgSend$memojiPicker
+ _objc_msgSend$messagePrompt
+ _objc_msgSend$popoverPresentationController
+ _objc_msgSend$presentViewController:animated:completion:
+ _objc_msgSend$setAvatarPicker:
+ _objc_msgSend$setCompactDetentIdentifier:
+ _objc_msgSend$setDetents:
+ _objc_msgSend$setExtendedLayoutIncludesOpaqueBars:
+ _objc_msgSend$setLargestUndimmedDetentIdentifier:
+ _objc_msgSend$setMemojiPicker:
+ _objc_msgSend$setMessagePrompt:
+ _objc_msgSend$setModalPresentationStyle:
+ _objc_msgSend$setMode:
+ _objc_msgSend$setPermittedArrowDirections:
+ _objc_msgSend$setPrefersGrabberVisible:
+ _objc_msgSend$setPrefersScrollingExpandsWhenScrolledToEdge:
+ _objc_msgSend$setSelectedDetentIdentifier:
+ _objc_msgSend$setSourceView:
+ _objc_msgSend$sheetPresentationController
+ _objc_msgSend$showMemojiPicker:
+ _objc_msgSend$systemBackgroundColor
+ _objc_msgSend$systemGray4Color
+ _objc_msgSend$systemGrayColor
- +[CFXFilterPickerCollectionViewCell selectionColor]
- +[CFXFilterPickerCollectionViewCell selectionColor].cold.1
- -[CFXEffectBrowserViewController CFX_updateAVTAvatarPickerforMessagesAppViewController:]
- -[CFXEffectPickerViewController filterPickerPresentationModeDidChange]
- -[CFXEffectPickerViewController selectedFilterIndexForFilterPickerView:]
- -[CFXEffectPickerViewController shouldDisplayExpandedModeForFilterPickerView:]
- -[CFXFilterEffectPickerView .cxx_destruct]
- -[CFXFilterEffectPickerView CFX_selectInitialItem]
- -[CFXFilterEffectPickerView CFX_selectItemAtCellIndex:animated:]
- -[CFXFilterEffectPickerView CFX_updateTitleForCenterItemAtIndex:]
- -[CFXFilterEffectPickerView buildCompactSelectionViews]
- -[CFXFilterEffectPickerView cachedEffectCount]
- -[CFXFilterEffectPickerView collectionViewLayout]
- -[CFXFilterEffectPickerView collectionView]
- -[CFXFilterEffectPickerView compactSelectedTitleView]
- -[CFXFilterEffectPickerView compactSelectionView]
- -[CFXFilterEffectPickerView configureCell:]
- -[CFXFilterEffectPickerView configureCollectionViewLayout]
- -[CFXFilterEffectPickerView configureCollectionViewLayout].cold.1
- -[CFXFilterEffectPickerView contentView]
- -[CFXFilterEffectPickerView dataSource]
- -[CFXFilterEffectPickerView delegate]
- -[CFXFilterEffectPickerView didScrollCollectionView]
- -[CFXFilterEffectPickerView didSelectItemAtCellIndex:]
- -[CFXFilterEffectPickerView effectPickerCellNibName]
- -[CFXFilterEffectPickerView effectPickerCellReuseIdentifier]
- -[CFXFilterEffectPickerView effectPickerNibName]
- -[CFXFilterEffectPickerView indexPathForCenterOfCollectionView]
- -[CFXFilterEffectPickerView isDisplayingCompactLayout]
- -[CFXFilterEffectPickerView isDisplayingExpandedLayout]
- -[CFXFilterEffectPickerView lastScrollIndexPath]
- -[CFXFilterEffectPickerView lastViewSize]
- -[CFXFilterEffectPickerView layoutAttributesForNearestItemToCenterWithOffset:]
- -[CFXFilterEffectPickerView layoutSubviews]
- -[CFXFilterEffectPickerView orientationDidChange]
- -[CFXFilterEffectPickerView previousScrollOffset]
- -[CFXFilterEffectPickerView reloadData]
- -[CFXFilterEffectPickerView removeCompactSelectionViews]
- -[CFXFilterEffectPickerView scrollViewDidEndDecelerating:]
- -[CFXFilterEffectPickerView scrollViewDidEndDragging:willDecelerate:]
- -[CFXFilterEffectPickerView scrollViewWillBeginDragging:]
- -[CFXFilterEffectPickerView scrollViewWillEndDragging:withVelocity:targetContentOffset:]
- -[CFXFilterEffectPickerView selectCenterItem]
- -[CFXFilterEffectPickerView selectEffectWithIdentifier:]
- -[CFXFilterEffectPickerView selectedIndex]
- -[CFXFilterEffectPickerView selectionFeedbackGenerator]
- -[CFXFilterEffectPickerView setCachedEffectCount:]
- -[CFXFilterEffectPickerView setCollectionView:]
- -[CFXFilterEffectPickerView setCollectionViewLayout:]
- -[CFXFilterEffectPickerView setCompactSelectedTitleView:]
- -[CFXFilterEffectPickerView setCompactSelectionView:]
- -[CFXFilterEffectPickerView setContentView:]
- -[CFXFilterEffectPickerView setDataSource:]
- -[CFXFilterEffectPickerView setDelegate:]
- -[CFXFilterEffectPickerView setDisplayExpandedLayout:]
- -[CFXFilterEffectPickerView setLastScrollIndexPath:]
- -[CFXFilterEffectPickerView setLastViewSize:]
- -[CFXFilterEffectPickerView setPreviousScrollOffset:]
- -[CFXFilterEffectPickerView setSelectionFeedbackGenerator:]
- -[CFXFilterEffectPickerView subviewsDidLoad]
- -[CFXFilterEffectPickerView updatePreviewEffectsWhenReloadComplete]
- -[CFXFilterPickerCollectionView enableInfiniteHorizontalScrolling]
- -[CFXFilterPickerCollectionView layoutSubviews]
- -[CFXFilterPickerCollectionView setEnableInfiniteHorizontalScrolling:]
- -[CFXFilterPickerCollectionViewCell .cxx_destruct]
- -[CFXFilterPickerCollectionViewCell CFX_updateLayerProperties]
- -[CFXFilterPickerCollectionViewCell CFX_updateSelectionView]
- -[CFXFilterPickerCollectionViewCell CFX_updateTitle]
- -[CFXFilterPickerCollectionViewCell configureCellAppearence]
- -[CFXFilterPickerCollectionViewCell isInCompactMode]
- -[CFXFilterPickerCollectionViewCell prepareForReuse]
- -[CFXFilterPickerCollectionViewCell selectionView]
- -[CFXFilterPickerCollectionViewCell setCompactMode:]
- -[CFXFilterPickerCollectionViewCell setEffect:]
- -[CFXFilterPickerCollectionViewCell setSelected:]
- -[CFXFilterPickerCollectionViewCell setSelectionView:]
- -[CFXFilterPickerCollectionViewCell setTitleView:]
- -[CFXFilterPickerCollectionViewCell titleView]
- -[JFXAnimojiEffectRenderer JFX_focalLengthForFrame:workingSize:interfaceOrientation:]
- _OBJC_CLASS_$_CFXFilterEffectPickerView
- _OBJC_CLASS_$_CFXFilterPickerCollectionView
- _OBJC_CLASS_$_CFXFilterPickerCollectionViewCell
- _OBJC_CLASS_$_NSIndexPath
- _OBJC_CLASS_$_SCNTransaction
- _OBJC_IVAR_$_CFXFilterEffectPickerView._cachedEffectCount
- _OBJC_IVAR_$_CFXFilterEffectPickerView._collectionView
- _OBJC_IVAR_$_CFXFilterEffectPickerView._collectionViewLayout
- _OBJC_IVAR_$_CFXFilterEffectPickerView._compactSelectedTitleView
- _OBJC_IVAR_$_CFXFilterEffectPickerView._compactSelectionView
- _OBJC_IVAR_$_CFXFilterEffectPickerView._contentView
- _OBJC_IVAR_$_CFXFilterEffectPickerView._displayExpandedLayout
- _OBJC_IVAR_$_CFXFilterEffectPickerView._lastScrollIndexPath
- _OBJC_IVAR_$_CFXFilterEffectPickerView._lastViewSize
- _OBJC_IVAR_$_CFXFilterEffectPickerView._previousScrollOffset
- _OBJC_IVAR_$_CFXFilterEffectPickerView._selectionFeedbackGenerator
- _OBJC_IVAR_$_CFXFilterEffectPickerView.dataSource
- _OBJC_IVAR_$_CFXFilterEffectPickerView.delegate
- _OBJC_IVAR_$_CFXFilterPickerCollectionView._enableInfiniteHorizontalScrolling
- _OBJC_IVAR_$_CFXFilterPickerCollectionViewCell._compactMode
- _OBJC_IVAR_$_CFXFilterPickerCollectionViewCell._selectionView
- _OBJC_IVAR_$_CFXFilterPickerCollectionViewCell._titleView
- _OBJC_METACLASS_$_CFXFilterEffectPickerView
- _OBJC_METACLASS_$_CFXFilterPickerCollectionView
- _OBJC_METACLASS_$_CFXFilterPickerCollectionViewCell
- __OBJC_$_CLASS_METHODS_CFXFilterPickerCollectionViewCell
- __OBJC_$_CLASS_PROP_LIST_CFXFilterPickerCollectionViewCell
- __OBJC_$_INSTANCE_METHODS_CFXFilterEffectPickerView
- __OBJC_$_INSTANCE_METHODS_CFXFilterPickerCollectionView
- __OBJC_$_INSTANCE_METHODS_CFXFilterPickerCollectionViewCell
- __OBJC_$_INSTANCE_VARIABLES_CFXFilterEffectPickerView
- __OBJC_$_INSTANCE_VARIABLES_CFXFilterPickerCollectionView
- __OBJC_$_INSTANCE_VARIABLES_CFXFilterPickerCollectionViewCell
- __OBJC_$_PROP_LIST_CFXFilterEffectPickerView
- __OBJC_$_PROP_LIST_CFXFilterPickerCollectionView
- __OBJC_$_PROP_LIST_CFXFilterPickerCollectionViewCell
- __OBJC_$_PROP_LIST_FunCameraFilterPickerHost
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CFXFilterEffectPickerViewDataSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CFXFilterEffectPickerViewDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FunCamFilterPickerPresentationDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FunCameraFilterPickerHost
- __OBJC_$_PROTOCOL_METHOD_TYPES_CFXFilterEffectPickerViewDataSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_CFXFilterEffectPickerViewDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_FunCamFilterPickerPresentationDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_FunCameraFilterPickerHost
- __OBJC_$_PROTOCOL_REFS_CFXFilterEffectPickerViewDataSource
- __OBJC_$_PROTOCOL_REFS_CFXFilterEffectPickerViewDelegate
- __OBJC_$_PROTOCOL_REFS_FunCamFilterPickerPresentationDelegate
- __OBJC_$_PROTOCOL_REFS_FunCameraFilterPickerHost
- __OBJC_CLASS_RO_$_CFXFilterEffectPickerView
- __OBJC_CLASS_RO_$_CFXFilterPickerCollectionView
- __OBJC_CLASS_RO_$_CFXFilterPickerCollectionViewCell
- __OBJC_LABEL_PROTOCOL_$_CFXFilterEffectPickerViewDataSource
- __OBJC_LABEL_PROTOCOL_$_CFXFilterEffectPickerViewDelegate
- __OBJC_LABEL_PROTOCOL_$_FunCamFilterPickerPresentationDelegate
- __OBJC_LABEL_PROTOCOL_$_FunCameraFilterPickerHost
- __OBJC_METACLASS_RO_$_CFXFilterEffectPickerView
- __OBJC_METACLASS_RO_$_CFXFilterPickerCollectionView
- __OBJC_METACLASS_RO_$_CFXFilterPickerCollectionViewCell
- __OBJC_PROTOCOL_$_CFXFilterEffectPickerViewDataSource
- __OBJC_PROTOCOL_$_CFXFilterEffectPickerViewDelegate
- __OBJC_PROTOCOL_$_FunCamFilterPickerPresentationDelegate
- __OBJC_PROTOCOL_$_FunCameraFilterPickerHost
- __OBJC_PROTOCOL_REFERENCE_$_FunCameraFilterPickerHost
- __ZNKSt3__16vectorI8EdgeLineNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__111__sift_downB8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_OT0_NS_15iterator_traitsIS6_E15difference_typeES6_
- __ZNSt3__116__insertion_sortB8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_S6_T0_
- __ZNSt3__117__assoc_sub_state15__attach_futureB8ne190102Ev
- __ZNSt3__117__floyd_sift_downB8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEET1_S6_OT0_NS_15iterator_traitsIS6_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI8EdgeLineEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__partial_sort_implB8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineS5_EET1_S6_S6_T2_OT0_
- __ZNSt3__120__throw_future_errorB8ne190102ENS_11future_errcE
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__126__insertion_sort_unguardedB8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_S6_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEbT1_S6_T0_
- __ZNSt3__131__partition_with_equals_on_leftB8ne190102INS_17_ClassicAlgPolicyEP8EdgeLineR11cmpEdgeLineEET0_S6_S6_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8ne190102INS_17_ClassicAlgPolicyEP8EdgeLineR11cmpEdgeLineEENS_4pairIT0_bEES7_S7_T1_
- __ZNSt3__14swapB8ne190102IU8__strongPU21objcproto10MTLTexture11objc_objectEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS5_EE5valueEvE4typeERS5_S8_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEjT1_S6_S6_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_S6_S6_S6_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_S6_S6_S6_S6_T0_
- __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyER11cmpEdgeLineP8EdgeLineEEvT1_S6_OT0_NS_15iterator_traitsIS6_E15difference_typeE
- __ZSt18make_exception_ptrB8ne190102INSt3__112future_errorEESt13exception_ptrT_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZZSt18make_exception_ptrB8ne190102INSt3__112future_errorEESt13exception_ptrT_ENUlPvE_8__invokeES4_
- __Znwm
- ___51+[CFXFilterPickerCollectionViewCell selectionColor]_block_invoke
- ___88-[CFXEffectBrowserViewController CFX_updateAVTAvatarPickerforMessagesAppViewController:]_block_invoke
- ___88-[CFXEffectBrowserViewController CFX_updateAVTAvatarPickerforMessagesAppViewController:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e21_v24?0"SCNNode"8^B16ls32l8
- ___block_descriptor_48_e8_32s40s_e21_v24?0"SCNNode"8^B16ls32l8s40l8
- _kCFXFilterPickerInfiniteScrollingCenterCopyIndex
- _kCFXFilterPickerInfiniteScrollingItemCountMultiplier
- _objc_msgSend$CFX_selectInitialItem
- _objc_msgSend$CFX_selectItemAtCellIndex:animated:
- _objc_msgSend$CFX_updateAVTAvatarPickerforMessagesAppViewController:
- _objc_msgSend$CFX_updateLayerProperties
- _objc_msgSend$CFX_updateSelectionView
- _objc_msgSend$CFX_updateTitle
- _objc_msgSend$CFX_updateTitleForCenterItemAtIndex:
- _objc_msgSend$JFX_focalLengthForFrame:workingSize:interfaceOrientation:
- _objc_msgSend$_setTransfersScrollToContainer:
- _objc_msgSend$buildCompactSelectionViews
- _objc_msgSend$childNodeWithName:recursively:
- _objc_msgSend$compactSelectedTitleView
- _objc_msgSend$compactSelectionView
- _objc_msgSend$configureCollectionViewLayout
- _objc_msgSend$contentOffset
- _objc_msgSend$contentSize
- _objc_msgSend$effectPickerView:effectTitleAtIndex:
- _objc_msgSend$effectPickerView:indexForEffectID:
- _objc_msgSend$enableInfiniteHorizontalScrolling
- _objc_msgSend$enumerateHierarchyUsingBlock:
- _objc_msgSend$indexPath
- _objc_msgSend$indexPathForCenterOfCollectionView
- _objc_msgSend$indexPathForItem:inSection:
- _objc_msgSend$indexPathForItemAtPoint:
- _objc_msgSend$isDecelerating
- _objc_msgSend$isDeviceInterfaceLandscape
- _objc_msgSend$isDisplayingCompactLayout
- _objc_msgSend$isDisplayingExpandedLayout
- _objc_msgSend$isInCompactMode
- _objc_msgSend$isTracking
- _objc_msgSend$lastBaselineAnchor
- _objc_msgSend$lastScrollIndexPath
- _objc_msgSend$lastViewSize
- _objc_msgSend$layoutAttributesForElementsInRect:
- _objc_msgSend$layoutAttributesForNearestItemToCenterWithOffset:
- _objc_msgSend$layoutPresentationStyle
- _objc_msgSend$morpher
- _objc_msgSend$numberOfItemsInSection:
- _objc_msgSend$pickerDidChangePresentationMode
- _objc_msgSend$presentationNode
- _objc_msgSend$previousScrollOffset
- _objc_msgSend$removeCompactSelectionViews
- _objc_msgSend$renderAtTime:viewport:commandBuffer:passDescriptor:
- _objc_msgSend$rendererWithDevice:options:
- _objc_msgSend$rootNode
- _objc_msgSend$scene
- _objc_msgSend$scrollToItemAtIndexPath:atScrollPosition:animated:
- _objc_msgSend$sectionInset
- _objc_msgSend$selectCenterItem
- _objc_msgSend$selectItemAtIndexPath:animated:scrollPosition:
- _objc_msgSend$selectedFilterIdentifierForEffectPickerViewController:
- _objc_msgSend$selectedFilterIndexForFilterPickerView:
- _objc_msgSend$selectedIndex
- _objc_msgSend$selectionColor
- _objc_msgSend$selectionFeedbackGenerator
- _objc_msgSend$selectionView
- _objc_msgSend$sensorHeight
- _objc_msgSend$setAllowsMultipleSelection:
- _objc_msgSend$setAnimationDuration:
- _objc_msgSend$setAvt_antialiasingMode:
- _objc_msgSend$setCachedEffectCount:
- _objc_msgSend$setCompactMode:
- _objc_msgSend$setCompactSelectedTitleView:
- _objc_msgSend$setCompactSelectionView:
- _objc_msgSend$setContentOffset:
- _objc_msgSend$setDisplayExpandedLayout:
- _objc_msgSend$setFilterPickerPresentationDelegate:
- _objc_msgSend$setLastScrollIndexPath:
- _objc_msgSend$setLastViewSize:
- _objc_msgSend$setPreviousScrollOffset:
- _objc_msgSend$setScrollDirection:
- _objc_msgSend$setSectionInset:
- _objc_msgSend$setShowsHorizontalScrollIndicator:
- _objc_msgSend$setWeights:
- _objc_msgSend$shouldDisplayExpandedModeForFilterPickerView:
- _objc_msgSend$systemYellowColor
- _objc_msgSend$titleView
- _objc_msgSend$weights
- _selectionColor.onceToken
- _selectionColor.selectionColor
- _setShapeLayerPathFromPointsWithStyle
CStrings:
+ "@\"<CFXMemojiPickerViewControllerDelegate>\""
+ "@\"AVTFunCamAvatarPickerController\""
+ "@\"CFXMemojiPickerViewController\""
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "ButtonShelf"
+ "CFXMemojiPickerViewController"
+ "CFXMemojiPickerViewControllerDelegate"
+ "CFX_updateAVTAvatarPickerforViewController:"
+ "ConversationKit"
+ "Failed to show Mempji Picker, effectBrowserViewController is nil, so this view didn't load properly."
+ "JFX_focalLengthForFrame:renderer:workingSize:interfaceOrientation:"
+ "MEMOJI Name"
+ "No effect browser picker to refresh."
+ "No picker browser to hide?"
+ "Not configured for internal Memoji picker mode."
+ "T@\"<CFXMemojiPickerViewControllerDelegate>\",W,N,V_delegate"
+ "T@\"AVTFunCamAvatarPickerController\",&,N,V_avatarPicker"
+ "T@\"CFXMemojiPickerViewController\",&,N,V_memojiPicker"
+ "T@\"NSString\",&,N,V_compactDetentIdentifier"
+ "T@\"UILabel\",&,N,V_messagePrompt"
+ "This delegate callback should only happen from the internal Memoji picker, but it is nil?"
+ "_avatarPicker"
+ "_cek_applyBlendshapeWeightsInHierarchyUsingBlock:"
+ "_cek_beginTransaction"
+ "_cek_commitTransaction"
+ "_cek_currentPointOfViewSensorHeight"
+ "_cek_fetchBlendshapeWeightsInHierarchyUsingBlock:"
+ "_cek_renderAtTime:enableAntialiasing:viewport:commandBuffer:passDescriptor:"
+ "_cek_rendererWithDevice:options:"
+ "_cek_setCurrentPointOfViewFocalLength:"
+ "_compactDetentIdentifier"
+ "_memojiPicker"
+ "_messagePrompt"
+ "addConstraints:"
+ "animateChanges:"
+ "appBackgroundColor"
+ "avatarPicker"
+ "boldSystemFontOfSize:"
+ "close:"
+ "com.apple.FunCamera.Animoji"
+ "compactDetentIdentifier"
+ "customDetentWithIdentifier:resolver:"
+ "d16@?0@\"<UISheetPresentationControllerDetentResolutionContext>\"8"
+ "d56@0:8@16@24{CGSize=dd}32q48"
+ "didDismissMemojiPicker"
+ "dismissViewControllerAnimated:completion:"
+ "funCamAvatarPickerControllerForStore:style:allowsCreation:"
+ "initWithCellSize:engagedCellSize:interitemSpacing:gridEdgeInsets:"
+ "largeDetent"
+ "memojiPicker"
+ "messagePrompt"
+ "popoverPresentationController"
+ "presentViewController:animated:completion:"
+ "setAvatarPicker:"
+ "setCompactDetentIdentifier:"
+ "setDetents:"
+ "setExtendedLayoutIncludesOpaqueBars:"
+ "setLargestUndimmedDetentIdentifier:"
+ "setMemojiPicker:"
+ "setMessagePrompt:"
+ "setModalPresentationStyle:"
+ "setMode:"
+ "setPermittedArrowDirections:"
+ "setPrefersGrabberVisible:"
+ "setPrefersScrollingExpandsWhenScrolledToEdge:"
+ "setSelectedDetentIdentifier:"
+ "setSourceView:"
+ "sheetPresentationController"
+ "showMemojiPicker:"
+ "shutterControlDidUpdateLiquidShutter:"
+ "systemBackgroundColor"
+ "systemGray4Color"
+ "systemGrayColor"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:shouldChangeTextInRanges:replacementText:"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v32@?0@\"NSString\"8^B16@?<v@?@\"NSArray\">24"
+ "xmark"
- "@\"<CFXFilterEffectPickerViewDataSource>\""
- "@\"<CFXFilterEffectPickerViewDelegate>\""
- "@\"<FunCamFilterPickerPresentationDelegate>\"16@0:8"
- "@\"NSIndexPath\""
- "@32@0:8{CGPoint=dd}16"
- "B24@0:8@\"CFXFilterEffectPickerView\"16"
- "CFXFilterEffectPickerView"
- "CFXFilterEffectPickerViewDataSource"
- "CFXFilterEffectPickerViewDelegate"
- "CFXFilterPickerCollectionView"
- "CFXFilterPickerCollectionViewCell"
- "CFX_selectInitialItem"
- "CFX_selectItemAtCellIndex:animated:"
- "CFX_updateAVTAvatarPickerforMessagesAppViewController:"
- "CFX_updateLayerProperties"
- "CFX_updateSelectionView"
- "CFX_updateTitle"
- "CFX_updateTitleForCenterItemAtIndex:"
- "FunCamFilterPickerPresentationDelegate"
- "FunCameraFilterPickerHost"
- "JFX_focalLengthForFrame:workingSize:interfaceOrientation:"
- "Q24@0:8@\"CFXFilterEffectPickerView\"16"
- "T@\"<CFXFilterEffectPickerViewDataSource>\",W,N,VdataSource"
- "T@\"<CFXFilterEffectPickerViewDelegate>\",W,N,Vdelegate"
- "T@\"<FunCamFilterPickerPresentationDelegate>\",W,N"
- "T@\"NSIndexPath\",&,N,V_lastScrollIndexPath"
- "T@\"UILabel\",&,N,V_compactSelectedTitleView"
- "T@\"UILabel\",&,V_titleView"
- "T@\"UISelectionFeedbackGenerator\",&,N,V_selectionFeedbackGenerator"
- "T@\"UIView\",&,N,V_compactSelectionView"
- "T@\"UIView\",W,N,V_selectionView"
- "TB,N,GisDisplayingExpandedLayout,V_displayExpandedLayout"
- "TB,N,GisInCompactMode,V_compactMode"
- "TB,N,V_enableInfiniteHorizontalScrolling"
- "TQ,N,V_cachedEffectCount"
- "T{CGPoint=dd},N,V_previousScrollOffset"
- "T{CGSize=dd},N,V_lastViewSize"
- "_cachedEffectCount"
- "_compactMode"
- "_compactSelectedTitleView"
- "_compactSelectionView"
- "_displayExpandedLayout"
- "_enableInfiniteHorizontalScrolling"
- "_lastScrollIndexPath"
- "_lastViewSize"
- "_previousScrollOffset"
- "_selectionFeedbackGenerator"
- "_selectionView"
- "_setTransfersScrollToContainer:"
- "_titleView"
- "buildCompactSelectionViews"
- "cachedEffectCount"
- "childNodeWithName:recursively:"
- "compact"
- "compactMode"
- "compactSelectedTitleView"
- "compactSelectionView"
- "configureCollectionViewLayout"
- "contentOffset"
- "contentSize"
- "d48@0:8@16{CGSize=dd}24q40"
- "displayExpandedLayout"
- "enableInfiniteHorizontalScrolling"
- "enumerateHierarchyUsingBlock:"
- "expanded"
- "filter picker transitioning to %@ mode"
- "filterPickerPresentationDelegate"
- "filterPickerPresentationModeDidChange"
- "indexPath"
- "indexPathForCenterOfCollectionView"
- "indexPathForItem:inSection:"
- "indexPathForItemAtPoint:"
- "isDecelerating"
- "isDisplayingCompactLayout"
- "isDisplayingExpandedLayout"
- "isInCompactMode"
- "isTracking"
- "lastBaselineAnchor"
- "lastScrollIndexPath"
- "lastViewSize"
- "layoutAttributesForElementsInRect:"
- "layoutAttributesForNearestItemToCenterWithOffset:"
- "layoutPresentationStyle"
- "morpher"
- "numberOfItemsInSection:"
- "presentationNode"
- "previousScrollOffset"
- "removeCompactSelectionViews"
- "renderAtTime:viewport:commandBuffer:passDescriptor:"
- "rendererWithDevice:options:"
- "rootNode"
- "scene"
- "scrollToItemAtIndexPath:atScrollPosition:animated:"
- "sectionInset"
- "selectCenterItem"
- "selectEffectWithIdentifier:"
- "selectItemAtIndexPath:animated:scrollPosition:"
- "selectedFilterIndexForFilterPickerView:"
- "selectedIndex"
- "selectionColor"
- "selectionFeedbackGenerator"
- "selectionView"
- "sensorHeight"
- "setAllowsMultipleSelection:"
- "setAvt_antialiasingMode:"
- "setCachedEffectCount:"
- "setCompactMode:"
- "setCompactSelectedTitleView:"
- "setCompactSelectionView:"
- "setContentOffset:"
- "setDisplayExpandedLayout:"
- "setEnableInfiniteHorizontalScrolling:"
- "setFilterPickerPresentationDelegate:"
- "setLastScrollIndexPath:"
- "setLastViewSize:"
- "setPreviousScrollOffset:"
- "setScrollDirection:"
- "setSectionInset:"
- "setSelectionFeedbackGenerator:"
- "setSelectionView:"
- "setShowsHorizontalScrollIndicator:"
- "setTitleView:"
- "setWeights:"
- "shouldDisplayExpandedModeForFilterPickerView:"
- "systemYellowColor"
- "titleView"
- "v24@0:8@\"<FunCamFilterPickerPresentationDelegate>\"16"
- "v24@?0@\"SCNNode\"8^B16"
- "v28@0:8Q16B24"
- "weights"

```
