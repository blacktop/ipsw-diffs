## VisionKitCore

> `/System/Library/PrivateFrameworks/VisionKitCore.framework/Versions/A/VisionKitCore`

```diff

-344.0.0.0.0
-  __TEXT.__text: 0xa28f8
-  __TEXT.__objc_methlist: 0xb2e8
+347.1.3.502.0
+  __TEXT.__text: 0xa3ebc
+  __TEXT.__objc_methlist: 0xb488
   __TEXT.__const: 0xa9c
   __TEXT.__gcc_except_tab: 0x17fc
-  __TEXT.__cstring: 0x68b4
+  __TEXT.__cstring: 0x68d4
   __TEXT.__dlopen_cstrs: 0x37a
   __TEXT.__oslogstring: 0x2d5d
-  __TEXT.__ustring: 0x4e
+  __TEXT.__ustring: 0x5e
   __TEXT.__constg_swiftt: 0x254
   __TEXT.__swift5_typeref: 0x156
   __TEXT.__swift5_reflstr: 0xa3

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x3008
+  __TEXT.__unwind_info: 0x3078
   __TEXT.__eh_frame: 0x158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc38
-  __DATA_CONST.__objc_classlist: 0x3c0
+  __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6950
+  __DATA_CONST.__objc_selrefs: 0x6a40
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x230
+  __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x2d0
-  __DATA_CONST.__got: 0x948
+  __DATA_CONST.__got: 0x958
   __AUTH_CONST.__const: 0x3088
-  __AUTH_CONST.__cfstring: 0x5e20
-  __AUTH_CONST.__objc_const: 0x13670
+  __AUTH_CONST.__cfstring: 0x5e80
+  __AUTH_CONST.__objc_const: 0x13878
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x300

   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0xa18
   __AUTH_CONST.__auth_ptr: 0x110
-  __AUTH.__objc_data: 0x1110
+  __AUTH.__objc_data: 0x1160
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0xb70
+  __DATA.__objc_ivar: 0xb78
   __DATA.__data: 0x10a0
-  __DATA.__bss: 0x630
+  __DATA.__bss: 0x610
   __DATA_DIRTY.__objc_data: 0x16e8
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4823
-  Symbols:   10303
-  CStrings:  1284
+  Functions: 4855
+  Symbols:   10370
+  CStrings:  1287
 
Symbols:
+ +[VKCActionInfoButton cellClass]
+ +[VKCInternalSettings usesGestureInputHandlingSettingsValue]
+ +[VKCInternalSettings usesGestureInputHandling]
+ +[VKImageAnalysisButton cellClass]
+ -[VKCActionInfoButton vk_setPressed:]
+ -[VKCImageAnalysisBaseView _overridesRequireMouseDownFallback]
+ -[VKCImageAnalysisBaseView gestureRecognizer:shouldAttemptToRecognizeWithEvent:]
+ -[VKCImageAnalysisBaseView gestureRecognizer:shouldReceiveTouch:]
+ -[VKCImageAnalysisBaseView gestureRecognizerShouldBegin:]
+ -[VKCImageAnalysisBaseView visualIntelligenceView:didLaunchExternalApplicationForURL:]
+ -[VKCImageAnalysisBaseView vk_eventHasMouseSubtype:]
+ -[VKCImageAnalysisBaseView vk_eventIsDirectTouch:]
+ -[VKCImageAnalysisBaseView vk_handleTextClickGesture:]
+ -[VKCImageAnalysisBaseView vk_handleTextPanGesture:]
+ -[VKCImageAnalysisBaseView vk_installTextGestureRecognizers]
+ -[VKCImageAnalysisBaseView vk_shouldRecognizeTextGestureForHitTestView:]
+ -[VKCImageAnalysisBaseView vk_textClickHasTargetForGestureRecognizer:]
+ -[VKCImageAnalysisOverlayView visualIntelligenceDidLaunchExternalApplicationForURL:]
+ -[VKCImageAnalyzerRequestVIConfiguration invocationType]
+ -[VKCImageAnalyzerRequestVIConfiguration setInvocationType:]
+ -[VKCImageDataDetectorView_macOS _overridesRequireMouseDownFallback]
+ -[VKCImageDataDetectorView_macOS vk_handleClickGestureWithEvent:]
+ -[VKCImageTextSelectionView_macOS _overridesRequireMouseDownFallback]
+ -[VKCImageTextSelectionView_macOS selectionDragInProgress]
+ -[VKCImageTextSelectionView_macOS setSelectionDragInProgress:]
+ -[VKCImageTextSelectionView_macOS usesGestureInputHandling]
+ -[VKCImageTextSelectionView_macOS vk_handleClickGesture:]
+ -[VKCImageTextSelectionView_macOS vk_handlePanGesture:]
+ -[VKCImageVisualSearchView vk_handleClickGestureWithEvent:]
+ -[VKCPressFeedbackButtonCell highlight:withFrame:inView:]
+ -[VKCVisualSearchResultItemView _overridesRequireMouseDownFallback]
+ -[VKCVisualSearchResultItemView vk_handleClickGestureWithEvent:]
+ -[VKImageAnalysisButton vk_setPressed:]
+ GCC_except_table149
+ GCC_except_table152
+ GCC_except_table162
+ GCC_except_table194
+ GCC_except_table222
+ GCC_except_table231
+ GCC_except_table249
+ GCC_except_table265
+ GCC_except_table266
+ GCC_except_table57
+ OBJC_IVAR_$_VKCImageAnalyzerRequestVIConfiguration._invocationType
+ OBJC_IVAR_$_VKCImageTextSelectionView_macOS._selectionDragInProgress
+ _OBJC_CLASS_$_NSButtonCell
+ _OBJC_CLASS_$_NSClickGestureRecognizer
+ _OBJC_CLASS_$_NSPanGestureRecognizer
+ _OBJC_CLASS_$_VKCPressFeedbackButtonCell
+ _OBJC_METACLASS_$_NSButtonCell
+ _OBJC_METACLASS_$_VKCPressFeedbackButtonCell
+ __OBJC_$_CLASS_METHODS_VKImageAnalysisButton
+ __OBJC_$_INSTANCE_METHODS_VKCPressFeedbackButtonCell
+ __OBJC_CLASS_RO_$_VKCPressFeedbackButtonCell
+ __OBJC_METACLASS_RO_$_VKCPressFeedbackButtonCell
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0l
+ _objc_msgSend$imageAnalysisOverlay:didLaunchExternalApplicationForURL:
+ _objc_msgSend$invocationType
+ _objc_msgSend$numberOfClicksRequired
+ _objc_msgSend$selectionDragInProgress
+ _objc_msgSend$setAllowedTouchTypes:
+ _objc_msgSend$setButtonMask:
+ _objc_msgSend$setInvocationType:
+ _objc_msgSend$setNumberOfClicksRequired:
+ _objc_msgSend$setSelectionDragInProgress:
+ _objc_msgSend$subtype
+ _objc_msgSend$touchesMatchingPhase:inView:
+ _objc_msgSend$translationInView:
+ _objc_msgSend$usesGestureInputHandling
+ _objc_msgSend$visualIntelligenceDidLaunchExternalApplicationForURL:
+ _objc_msgSend$vk_eventHasMouseSubtype:
+ _objc_msgSend$vk_eventIsDirectTouch:
+ _objc_msgSend$vk_handleClickGesture:
+ _objc_msgSend$vk_handleClickGestureWithEvent:
+ _objc_msgSend$vk_handlePanGesture:
+ _objc_msgSend$vk_installTextGestureRecognizers
+ _objc_msgSend$vk_setPressed:
+ _objc_msgSend$vk_shouldRecognizeTextGestureForHitTestView:
+ _objc_msgSend$vk_textClickHasTargetForGestureRecognizer:
+ _vk_overridesRequireMouseDownFallbackForGestureInput
- -[VKCActionInfoButton mouseDown:]
- -[VKImageAnalysisButton mouseDown:]
- GCC_except_table138
- GCC_except_table151
- GCC_except_table161
- GCC_except_table183
- GCC_except_table211
- GCC_except_table220
- GCC_except_table237
- GCC_except_table253
- GCC_except_table254
- GCC_except_table55
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0l
CStrings:
+ "usesGestureInputHandling"
+ "🆕"
+ "👴🏼"
```
