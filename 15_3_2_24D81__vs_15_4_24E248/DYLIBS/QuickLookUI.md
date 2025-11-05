## QuickLookUI

> `/System/Library/Frameworks/QuickLookUI.framework/Versions/A/QuickLookUI`

```diff

-1002.3.3.0.0
-  __TEXT.__text: 0xd0754
-  __TEXT.__auth_stubs: 0x25a0
-  __TEXT.__objc_methlist: 0xe824
-  __TEXT.__gcc_except_tab: 0x12d4
-  __TEXT.__const: 0x726
-  __TEXT.__cstring: 0x7a0b
+1002.5.2.0.0
+  __TEXT.__text: 0xcfad8
+  __TEXT.__auth_stubs: 0x2580
+  __TEXT.__objc_methlist: 0x10578
+  __TEXT.__gcc_except_tab: 0x1268
+  __TEXT.__const: 0x6f6
+  __TEXT.__cstring: 0x75ab
   __TEXT.__oslogstring: 0x3873
   __TEXT.__ustring: 0x26
-  __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__constg_swiftt: 0x9c
-  __TEXT.__swift5_typeref: 0x84
+  __TEXT.__swift5_typeref: 0x7c
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x8
   __TEXT.__dof_QLSeamles: 0x8e7
-  __TEXT.__unwind_info: 0x3ad0
+  __TEXT.__unwind_info: 0x3b38
   __TEXT.__objc_classname: 0x1ca7
   __TEXT.__objc_methname: 0x1eabe
   __TEXT.__objc_methtype: 0x5c90
   __TEXT.__objc_stubs: 0x19080
-  __DATA_CONST.__got: 0xf50
-  __DATA_CONST.__const: 0x5d8
+  __DATA_CONST.__got: 0xf80
+  __DATA_CONST.__const: 0x590
   __DATA_CONST.__objc_classlist: 0x6a8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d18
+  __DATA_CONST.__objc_selrefs: 0x80e8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x12e8
-  __AUTH_CONST.__const: 0x21a8
-  __AUTH_CONST.__cfstring: 0x7a60
-  __AUTH_CONST.__objc_const: 0x1a5f8
+  __AUTH_CONST.__auth_got: 0x12d8
+  __AUTH_CONST.__const: 0x20c8
+  __AUTH_CONST.__cfstring: 0x7a20
+  __AUTH_CONST.__objc_const: 0x16f28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x42c0
-  __AUTH.__data: 0xf0
+  __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0xf2c
-  __DATA.__data: 0x19a8
-  __DATA.__bss: 0x519
+  __DATA.__data: 0x19a0
+  __DATA.__bss: 0x461
   __DATA.__common: 0x40
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/Frameworks/SafariServices.framework/Versions/A/SafariServices
   - /System/Library/Frameworks/ScreenCaptureKit.framework/Versions/A/ScreenCaptureKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/Categories.framework/Versions/A/Categories
+  - /System/Library/PrivateFrameworks/DeviceManagement.framework/Versions/A/DeviceManagement
   - /System/Library/PrivateFrameworks/PerformanceAnalysis.framework/Versions/A/PerformanceAnalysis
   - /System/Library/PrivateFrameworks/QuickLookNonBaseSystem.framework/Versions/A/QuickLookNonBaseSystem
   - /System/Library/PrivateFrameworks/QuickLookSupport.framework/Versions/A/QuickLookSupport
+  - /System/Library/PrivateFrameworks/ScreenTimeUI.framework/Versions/A/ScreenTimeUI
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/Versions/A/UIIntelligenceSupport
   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 506FB023-1499-3EAB-B597-F30CFF3F9400
-  Functions: 5605
-  Symbols:   13339
-  CStrings:  8938
+  UUID: FF768B65-CB05-3A72-8CFE-14A5F428E6A3
+  Functions: 5675
+  Symbols:   13385
+  CStrings:  8903
 
Symbols:
+ +[QLArchivingHelper allowedClasses].cold.1
+ +[QLConfiguration sharedConfiguration].cold.1
+ +[QLCustomTextLayer _sharedStringDrawingContext].cold.1
+ +[QLDisplayBundleLoader useBlankDisplayBundleForPerformanceTesting].cold.1
+ +[QLGenericAnimationEffect genericAnimationForObject:key:duration:].cold.1
+ +[QLPreviewExtensionServiceContext_mac _extensionAuxiliaryHostProtocol].cold.1
+ +[QLPreviewExtensionServiceContext_mac _extensionAuxiliaryVendorProtocol].cold.1
+ +[QLPreviewExtensionServiceContext_mac _extensionIsGenerationBased].cold.1
+ +[QLPreviewPanelController _defaultNoItemsTitle].cold.1
+ +[QLPreviewView pushAbortModalSessionEvent].cold.2
+ +[QLSeamlessDocumentOpener _isUIHelperMaybeRunning].cold.1
+ +[QLSeamlessOpener seamlessOpenerWithDelegate:].cold.1
+ +[QLWindowEffect QLEaseInLongEaseOutValueForProgress:isInverted:].cold.1
+ -[QLDisplayBundle accommodatePresentedItemEvictionWithCompletionHandler:].cold.1
+ -[QLDisplayBundle activate].cold.2
+ -[QLDisplayBundle deactivate].cold.3
+ -[QLDisplayBundle dealloc].cold.1
+ -[QLDisplayBundle dealloc].cold.2
+ -[QLDisplayBundle dealloc].cold.3
+ -[QLDisplayBundle dealloc].cold.4
+ -[QLDisplayBundle didDesistRemoteWithExpectedDisplayBundleID:].cold.2
+ -[QLDisplayBundle didFailLoadingWithError:].cold.2
+ -[QLDisplayBundle didLoad].cold.1
+ -[QLDisplayBundle didMismatchLoadingWithHints:expectedDisplayBundleID:].cold.1
+ -[QLDisplayBundle discard].cold.1
+ -[QLDisplayBundleLoader _lookForDisplayBundles].cold.1
+ -[QLDisplayBundleViewController teardownMarkup:needsSave:].cold.1
+ -[QLExtensionUIManager _viewControllerForExtension:context:requestIdentifier:hints:withCompletionHandler:].cold.1
+ -[QLExtensionUIManager _viewControllerForExtension:context:requestIdentifier:hints:withCompletionHandler:].cold.2
+ -[QLExtensionUIManager remoteViewControllerForPreview:restrictToFirstParty:withHints:completionHandler:].cold.1
+ -[QLFadeWindowEffect animation:valueForProgress:].cold.1
+ -[QLFullscreenController _disableDisplaySleep].cold.1
+ -[QLFullscreenController _enableDisplaySleep].cold.1
+ -[QLPathWatcher addWatchedURL:client:].cold.2
+ -[QLPathWatcher removeWatchedURL:client:].cold.2
+ -[QLPreviewCacheManager cacheRecentDocument:].cold.4
+ -[QLPreviewCustomDocument startLoadingWithForcedDisplayBundleID:hints:].cold.1
+ -[QLPreviewDocument _loadPreviewFailedWithError:].cold.2
+ -[QLPreviewDocument _loadPreviewMismatchedWithExpectedDisplayBundleID:hints:].cold.1
+ -[QLPreviewDocument _loadPreviewSucceeded].cold.2
+ -[QLPreviewDocument _loadWithDisplayBundleID:hints:remoteMode:].cold.1
+ -[QLPreviewDocument _setupPreviewCommon].cold.1
+ -[QLPreviewDocument dealloc].cold.2
+ -[QLPreviewDocument generateThumbnailForPage:maxSize:completionBlock:].cold.1
+ -[QLPreviewDocumentDisplayBundle copyPageAsImageType:maximumSize:pageNumber:].cold.1
+ -[QLPreviewExtensionDisplayBundle loadWithHints:].cold.1
+ -[QLPreviewExtensionViewController hookUpToExtensionContextWithUUID:withHints:completionHandler:].cold.1
+ -[QLPreviewExtensionViewController hookUpToExtensionContextWithUUID:withHints:completionHandler:].cold.2
+ -[QLPreviewExtensionViewController previewViewController].cold.1
+ -[QLPreviewExtensionViewController previewViewController].cold.2
+ -[QLPreviewPanelController _defaultUserActionForEvent:].cold.2
+ -[QLPreviewPanelController _flushCaches].cold.2
+ -[QLPreviewPanelController _performUserAction:forEvent:].cold.1
+ -[QLPreviewPanelController _performUserAction:forEvent:].cold.2
+ -[QLPreviewPanelController _setCurrentPreviewItem:withTransition:blocking:].cold.1
+ -[QLPreviewPanelController _setCurrentPreviewItemIndex:withTransition:blocking:].cold.2
+ -[QLPreviewPanelController _setDisplayState:updatePreviewView:].cold.1
+ -[QLPreviewPanelController _setDisplayState:updatePreviewView:].cold.2
+ -[QLPreviewPanelController activateIndexSheetWithAnimation:].cold.1
+ -[QLPreviewPanelController adjustedPanelFrame:ignoringCurrentFrame:].cold.1
+ -[QLPreviewPanelController deactivateIndexSheetWithAnimation:].cold.1
+ -[QLPreviewPanelController didClose].cold.1
+ -[QLPreviewPanelController didClose].cold.2
+ -[QLPreviewPanelController didFinishOpeningTransition].cold.1
+ -[QLPreviewPanelController didFinishOpeningTransition].cold.2
+ -[QLPreviewPanelController didFinishOpeningTransition].cold.3
+ -[QLPreviewPanelController didOpen].cold.1
+ -[QLPreviewPanelController fullscreenFrame].cold.1
+ -[QLPreviewPanelController fullscreenFrame].cold.2
+ -[QLPreviewPanelController fullscreenTransitionTargetFrameInPreviewViewWithParentBounds:].cold.1
+ -[QLPreviewPanelController indexSheet:titleForPreviewItem:].cold.1
+ -[QLPreviewPanelController indexSheetDidDeactivate:].cold.1
+ -[QLPreviewPanelController indexSheetDidDeactivate:].cold.2
+ -[QLPreviewPanelController indexSheetDidDeactivate:].cold.3
+ -[QLPreviewPanelController indexSheetWillActivate:].cold.1
+ -[QLPreviewPanelController indexSheetWillActivate:].cold.2
+ -[QLPreviewPanelController refreshCurrentPreviewItem].cold.1
+ -[QLPreviewPanelController setCurrentPreviewItemIndex:withTransition:blocking:].cold.2
+ -[QLPreviewPanelController setupForFullscreen:].cold.1
+ -[QLPreviewPanelController showItemWithDelta:transition:].cold.1
+ -[QLPreviewPanelController startInlineSlideshow].cold.1
+ -[QLPreviewPanelController willClose].cold.1
+ -[QLPreviewPanelController willOpen].cold.2
+ -[QLPreviewPanelController willOpen].cold.3
+ -[QLPreviewPanelController willOpen].cold.4
+ -[QLPreviewSchemeHandler_distantfs icon].cold.1
+ -[QLPreviewSchemeHandler_tel icon].cold.1
+ -[QLPreviewSlideshow _startSlideshow].cold.1
+ -[QLPreviewSwipeController swipeWithEvent:containingView:options:beginBlock:previewFrameBlock:progressBlock:completionBlock:].cold.2
+ -[QLPreviewTitleBarView updateWindowButtons].cold.1
+ -[QLPreviewView _recycleDocument:restore:].cold.2
+ -[QLPreviewView _startLoadingPreviewItem:timeoutDate:].cold.3
+ -[QLPreviewView activate].cold.1
+ -[QLPreviewView deactivate].cold.1
+ -[QLPreviewView dealloc].cold.1
+ -[QLPreviewView dealloc].cold.2
+ -[QLPreviewView dealloc].cold.3
+ -[QLPreviewView dealloc].cold.4
+ -[QLPreviewView dealloc].cold.5
+ -[QLPreviewView setPreviewItem:blockingUntilLoading:timeoutDate:transition:].cold.1
+ -[QLPreviewWindowController _updateContentViewConstraintsInRootView].cold.1
+ -[QLPreviewWindowController _updateTitleBarConstraintsInRootView].cold.1
+ -[QLSeamlessItemOpener _invalidateWithSuccess:].cold.2
+ -[QLTimeSlider startControlWithDataSource:].cold.1
+ -[QLUIHelperObject setPort:].cold.1
+ -[QLUIServiceHostViewController previewLoaded:].cold.1
+ -[QLWarpingWindowEffect prepare].cold.1
+ -[QLWarpingWindowEffect prepare].cold.2
+ GCC_except_table185
+ GCC_except_table484
+ QLExpectedClassesForPropertiesDictionaries.cold.1
+ QLInitUILogging.cold.1
+ QLPreviewExtensionUIServiceInterface.cold.1
+ QLScarlettEnabled.cold.1
+ QLScarlettQuickActionsEnabled.cold.1
+ QLScarlettRemoveBackgroundEnabled.cold.1
+ QLUIServiceBaseHostInterface.cold.1
+ QLUIServiceBaseInterface.cold.1
+ QLUIServiceEditToolbarInterface.cold.1
+ QLUIServiceHostInterface.cold.1
+ QLUIServiceInterface.cold.1
+ _CTCategoryIdentifierEntertainment
+ _NSSavePanelCopyWindowOrderingGroup.cold.1
+ _NSSavePanelCopyWindowOrderingGroup.cold.2
+ _OBJC_CLASS_$_DMFApplicationPolicyMonitor
+ _OBJC_CLASS_$_DMFCategoryPolicyMonitor
+ _OBJC_CLASS_$_NSViewService
+ _OBJC_CLASS_$_STBlockingViewController
+ _OUTLINED_FUNCTION_13
+ _QLUseRTLLayout.cold.1
+ __112+[QLRemoteViewController connectToUIServiceViewControllerWithServiceName:serviceViewControllerClass:completion:]_block_invoke.cold.1
+ __125+[QLWindowEffectsLibrary morphEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke.21
+ __125+[QLWindowEffectsLibrary morphEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke.27
+ __125+[QLWindowEffectsLibrary morphEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke_2.34
+ __125+[QLWindowEffectsLibrary morphEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke_3.35
+ __125+[QLWindowEffectsLibrary scaleEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke.13
+ __34-[QLPreviewSchemeHandler _getIcon]_block_invoke.cold.1
+ __38-[QLPathWatcher addWatchedURL:client:]_block_invoke.cold.4
+ __40-[QLDisplayBundle checkScreenTimePolicy]_block_invoke.340
+ __42-[QLRemoteDisplayBundle updateProperties:]_block_invoke.55.cold.1
+ __48-[QLDisplayBundle startWatchingScreenTimePolicy]_block_invoke.332
+ __49-[QLRemoteDisplayBundle _setupToolbarRemoteView:]_block_invoke.cold.1
+ __62-[QLSeamlessOpener _checkToCloseTransientWindowWithAnimation:]_block_invoke.22
+ __62-[QLSeamlessOpener _openItems:async:local:realAppPID:options:]_block_invoke.61
+ __62-[QLSeamlessOpener _openItems:async:local:realAppPID:options:]_block_invoke.63
+ __62-[QLSeamlessOpener _openItems:async:local:realAppPID:options:]_block_invoke.71
+ __72-[QLRemoteDisplayBundle updatePropertiesForSize:previewMode:completion:]_block_invoke.50.cold.1
+ __79-[QLPreviewExtensionServiceContext_mac loadWithPreview:isAnimating:completion:]_block_invoke_3.cold.2
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_6vectorIdNS_9allocatorIdEEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIdNS1_IdEEEEEEPS4_EclB8ne190102Ev
+ __ZNKSt3__16vectorIN24QLParametricInterpolator4knotENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110__function12__value_funcIFvP21QLSplineInspectorView6CGRectEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvP21QLSplineInspectorView7CGPointEED2B8ne190102Ev
+ __ZNSt3__114__split_bufferINS_6vectorIdNS_9allocatorIdEEEERNS2_IS4_EEE17__destruct_at_endB8ne190102EPS4_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN24QLParametricInterpolator4knotEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_6vectorIdNS1_IdEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__125__throw_bad_function_callB8ne190102Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIdNS2_IdEEEEEEPS5_EEED2B8ne190102Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorIdNS1_IdEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE18__assign_with_sizeB8ne190102IPS3_S7_EEvT_T0_l
+ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ne190102IPdS5_EEvT_T0_m
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE18__assign_with_sizeB8ne190102IPdS5_EEvT_T0_l
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_QuickLookUI
+ _getClassForOptions.cold.1
+ _getSeamlessOpeningQueue.cold.1
+ _memcpy
- CategoriesLibrary.frameworkLibrary
- CategoriesLibrary.onceToken
- DeviceManagementLibrary.cold.1
- DeviceManagementLibrary.frameworkLibrary
- DeviceManagementLibrary.onceToken
- DeviceManagementLibraryCore.frameworkLibrary
- GCC_except_table184
- GCC_except_table35
- GCC_except_table38
- GCC_except_table477
- GCC_except_table70
- ScreenTimeUILibraryCore.frameworkLibrary
- ViewBridgeLibrary.frameworkLibrary
- ViewBridgeLibrary.onceToken
- _CTCategoryIdentifierEntertainmentFunction
- _DMFApplicationPolicyMonitorFunction
- _DMFCategoryPolicyMonitorFunction
- _DeviceManagementLibrary
- _NSViewServiceFunction
- __125+[QLWindowEffectsLibrary morphEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke.20
- __125+[QLWindowEffectsLibrary morphEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke.26
- __125+[QLWindowEffectsLibrary morphEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke_2.33
- __125+[QLWindowEffectsLibrary morphEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke_3.34
- __125+[QLWindowEffectsLibrary scaleEffectWithWindow:itemFrame:image:itemContentFrame:windowContentFrame:duration:transitionOnTop:]_block_invoke.12
- __40-[QLDisplayBundle checkScreenTimePolicy]_block_invoke.336
- __48-[QLDisplayBundle startWatchingScreenTimePolicy]_block_invoke.330
- __62-[QLSeamlessOpener _checkToCloseTransientWindowWithAnimation:]_block_invoke.21
- __62-[QLSeamlessOpener _openItems:async:local:realAppPID:options:]_block_invoke.60
- __62-[QLSeamlessOpener _openItems:async:local:realAppPID:options:]_block_invoke.62
- __62-[QLSeamlessOpener _openItems:async:local:realAppPID:options:]_block_invoke.69
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPNS_6vectorIdNS_9allocatorIdEEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIdNS1_IdEEEEEENS_16reverse_iteratorIPS4_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIdNS1_IdEEEEEEPS4_EclB8ne180100Ev
- __ZNKSt3__16vectorIN24QLParametricInterpolator4knotENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9exception4whatEv
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110__function12__value_funcIFvP21QLSplineInspectorView6CGRectEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvP21QLSplineInspectorView7CGPointEED2B8ne180100Ev
- __ZNSt3__114__split_bufferINS_6vectorIdNS_9allocatorIdEEEERNS2_IS4_EEE17__destruct_at_endB8ne180100EPS4_
- __ZNSt3__117bad_function_callD0Ev
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN24QLParametricInterpolator4knotEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_6vectorIdNS1_IdEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__125__throw_bad_function_callB8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIdNS2_IdEEEEEENS_16reverse_iteratorIPS5_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIdNS2_IdEEEEEEPS5_EEED2B8ne180100Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_6vectorIdNS1_IdEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_6vectorIdNS1_IdEEEEEENS_16reverse_iteratorIPS4_EES8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__16vectorIN24QLParametricInterpolator4knotENS_9allocatorIS2_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS2_RS4_EEPS2_
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE18__assign_with_sizeB8ne180100IPS3_S7_EEvT_T0_l
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS4_EE
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ne180100IPdS5_EEvT_T0_m
- __ZNSt3__16vectorIdNS_9allocatorIdEEE18__assign_with_sizeB8ne180100IPdS5_EEvT_T0_l
- __ZNSt9exceptionD2Ev
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZTISt9exception
- __ZTSNSt3__117bad_function_callE
- ___CategoriesLibrary_block_invoke
- ___DeviceManagementLibraryCore_block_invoke
- ___DeviceManagementLibrary_block_invoke
- ___ScreenTimeUILibraryCore_block_invoke
- ___ViewBridgeLibrary_block_invoke
- ___assert_rtn
- ___getDMFApplicationPolicyMonitorClass_block_invoke
- ___getDMFCategoryPolicyMonitorClass_block_invoke
- ___getSTBlockingViewControllerClass_block_invoke
- __block_literal_global.353
- __block_literal_global.47
- __getDMFApplicationPolicyMonitorClass_block_invoke.cold.1
- __getDMFCategoryPolicyMonitorClass_block_invoke.cold.1
- __getSTBlockingViewControllerClass_block_invoke.cold.1
- __getSTBlockingViewControllerClass_block_invoke.cold.2
- __sl_dlopen
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_QuickLookUI
- _audit_stringDeviceManagement
- _audit_stringScreenTimeUI
- _classDMFApplicationPolicyMonitor
- _classDMFCategoryPolicyMonitor
- _classNSViewService
- _constantCTCategoryIdentifierEntertainment
- _getCTCategoryIdentifierEntertainment
- _getDMFApplicationPolicyMonitorClass
- _getDMFCategoryPolicyMonitorClass
- _getNSViewServiceClass
- _initCTCategoryIdentifierEntertainment
- _initDMFApplicationPolicyMonitor
- _initDMFCategoryPolicyMonitor
- _initNSViewService
- _symbolic _____Sg 10Foundation3URLV
- getDMFApplicationPolicyMonitorClass.softClass
- getDMFCategoryPolicyMonitorClass.softClass
- getSTBlockingViewControllerClass.softClass
- initCTCategoryIdentifierEntertainment.cold.1
- initCTCategoryIdentifierEntertainment.cold.2
- initDMFApplicationPolicyMonitor.cold.1
- initDMFCategoryPolicyMonitor.cold.1
- initNSViewService.cold.1
CStrings:
- "%s"
- "/System/Library/PrivateFrameworks/Categories.framework/Categories"
- "/System/Library/PrivateFrameworks/DeviceManagement.framework/Contents/MacOS/DeviceManagement"
- "/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement"
- "/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Contents/MacOS/ScreenTimeUI"
- "/System/Library/PrivateFrameworks/ViewBridge.framework/ViewBridge"
- "CTCategoryIdentifierEntertainment"
- "CategoriesLibrary"
- "Class getDMFApplicationPolicyMonitorClass(void)_block_invoke"
- "Class getDMFCategoryPolicyMonitorClass(void)_block_invoke"
- "Class getSTBlockingViewControllerClass(void)_block_invoke"
- "DMFApplicationPolicyMonitor"
- "DMFCategoryPolicyMonitor"
- "DeviceManagementLibrary"
- "NSViewService"
- "QLInlinePreviewController.m"
- "QLPreviewPanel.m"
- "QLWindowEffectsLibrary.m"
- "STBlockingViewController"
- "Unable to find class %s"
- "classDMFApplicationPolicyMonitor"
- "classDMFCategoryPolicyMonitor"
- "classNSViewService"
- "frameworkLibrary"
- "initCTCategoryIdentifierEntertainment"
- "initDMFApplicationPolicyMonitor"
- "initDMFCategoryPolicyMonitor"
- "initNSViewService"
- "softlink:r:path:/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement"
- "softlink:r:path:/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI"
- "void *DeviceManagementLibrary(void)"
- "void *ScreenTimeUILibrary(void)"

```
