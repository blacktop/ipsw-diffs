## AppleMediaServicesUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Versions/A/AppleMediaServicesUI`

```diff

-8.0.44.0.0
-  __TEXT.__text: 0x1e15a0
-  __TEXT.__objc_methlist: 0x10b2c
-  __TEXT.__const: 0xe254
-  __TEXT.__cstring: 0xdb10
-  __TEXT.__oslogstring: 0x961b
+8.0.52.1.3
+  __TEXT.__text: 0x1e40e4
+  __TEXT.__objc_methlist: 0x10be4
+  __TEXT.__const: 0xe374
+  __TEXT.__cstring: 0xdbb0
+  __TEXT.__oslogstring: 0x964b
   __TEXT.__ustring: 0x13a
   __TEXT.__gcc_except_tab: 0x11bc
   __TEXT.__dlopen_cstrs: 0x9b8
-  __TEXT.__constg_swiftt: 0x59d8
-  __TEXT.__swift5_typeref: 0x10bb6
+  __TEXT.__constg_swiftt: 0x59fc
+  __TEXT.__swift5_typeref: 0x10cb2
   __TEXT.__swift5_builtin: 0x1e0
-  __TEXT.__swift5_reflstr: 0x2d15
-  __TEXT.__swift5_fieldmd: 0x336c
+  __TEXT.__swift5_reflstr: 0x2d35
+  __TEXT.__swift5_fieldmd: 0x33a0
   __TEXT.__swift5_assocty: 0x1180
-  __TEXT.__swift5_proto: 0x540
-  __TEXT.__swift5_types: 0x44c
-  __TEXT.__swift5_capture: 0x1848
+  __TEXT.__swift5_proto: 0x54c
+  __TEXT.__swift5_types: 0x450
+  __TEXT.__swift5_capture: 0x18d0
   __TEXT.__swift5_protos: 0x2c
-  __TEXT.__swift_as_entry: 0x1cc
-  __TEXT.__swift_as_ret: 0x224
-  __TEXT.__swift_as_cont: 0x568
+  __TEXT.__swift_as_entry: 0x1d4
+  __TEXT.__swift_as_ret: 0x22c
+  __TEXT.__swift_as_cont: 0x574
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x83d8
-  __TEXT.__eh_frame: 0x6a58
+  __TEXT.__unwind_info: 0x8498
+  __TEXT.__eh_frame: 0x6bf0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3b48
-  __DATA_CONST.__objc_classlist: 0xac8
+  __DATA_CONST.__const: 0x3bc0
+  __DATA_CONST.__objc_classlist: 0xad0
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x3c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x89f0
+  __DATA_CONST.__objc_selrefs: 0x8a90
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x658
   __DATA_CONST.__objc_arraydata: 0x340
-  __DATA_CONST.__got: 0x1a88
-  __AUTH_CONST.__const: 0x92c8
-  __AUTH_CONST.__cfstring: 0xa840
-  __AUTH_CONST.__objc_const: 0x20ea8
+  __DATA_CONST.__got: 0x1ab8
+  __AUTH_CONST.__const: 0x9510
+  __AUTH_CONST.__cfstring: 0xa8c0
+  __AUTH_CONST.__objc_const: 0x20fa8
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__auth_got: 0x25f0
-  __AUTH.__objc_data: 0x8578
-  __AUTH.__data: 0x56a0
-  __DATA.__objc_ivar: 0x1104
-  __DATA.__data: 0x67d8
+  __AUTH_CONST.__auth_got: 0x2648
+  __AUTH.__objc_data: 0x85c0
+  __AUTH.__data: 0x56c0
+  __DATA.__objc_ivar: 0x1108
+  __DATA.__data: 0x6888
   __DATA.__objc_stublist: 0x10
-  __DATA.__bss: 0xaef0
+  __DATA.__bss: 0xb070
   __DATA.__common: 0x2f8
   __DATA_DIRTY.__objc_data: 0x1088
-  __DATA_DIRTY.__data: 0x138
+  __DATA_DIRTY.__data: 0x148
   __DATA_DIRTY.__bss: 0x58
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14417
-  Symbols:   15985
-  CStrings:  2730
+  Functions: 14493
+  Symbols:   16046
+  CStrings:  2737
 
Symbols:
+ +[AMSUIEngagementAttributionCore _URLToAttributeForOptIn:URL:]
+ +[AMSUIEngagementAttributionCore _skippedPromise]
+ +[AMSUIWebView _runAction:context:depth:completion:]
+ +[AMSUIWebView runAction:context:completion:]
+ -[AMSUIEngagementTaskViewController _processCampaignAttributionIfNeeded]
+ -[AMSUIToastPresentationController _accessibilityElement:isWithinView:]
+ -[AMSUIToastPresentationController _beginObservingVoiceOverFocus]
+ -[AMSUIToastPresentationController _endObservingVoiceOverFocus]
+ -[AMSUIToastPresentationController _isVoiceOverFocusedOnToast]
+ -[AMSUIToastPresentationController _voiceOverFocusDidChange:]
+ -[AMSUIToastPresentationController _voiceOverStatusDidChange:]
+ -[AMSUIToastPresentationController dealloc]
+ -[AMSUIToastPresentationController isDismissalPausedForVoiceOver]
+ -[AMSUIToastPresentationController setDismissalPausedForVoiceOver:]
+ -[AMSUIWebContainerViewController _applyNavigationModel]
+ GCC_except_table51
+ GCC_except_table57
+ GCC_except_table60
+ OBJC_IVAR_$_AMSUIToastPresentationController._dismissalPausedForVoiceOver
+ _OBJC_CLASS_$_AMSUIEngagementAttributionCore
+ _OBJC_METACLASS_$_AMSUIEngagementAttributionCore
+ _UIAccessibilityElementFocusedNotification
+ _UIAccessibilityFocusedElement
+ _UIAccessibilityFocusedElementKey
+ _UIAccessibilityNotificationVoiceOverIdentifier
+ __OBJC_$_CLASS_METHODS_AMSUIEngagementAttributionCore
+ __OBJC_CLASS_RO_$_AMSUIEngagementAttributionCore
+ __OBJC_METACLASS_RO_$_AMSUIEngagementAttributionCore
+ ___40-[AMSUIWebODIAssessmentAction runAction]_block_invoke_2
+ ___50-[AMSUIEngagementTaskViewController _preloadChild]_block_invoke_2
+ ___52+[AMSUIWebView _runAction:context:depth:completion:]_block_invoke
+ ___56-[AMSUIWebContainerViewController _applyNavigationModel]_block_invoke
+ ___72-[AMSUIEngagementTaskViewController _processCampaignAttributionIfNeeded]_block_invoke
+ ___block_descriptor_40_e8_32w_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8lw32l8
+ ___block_descriptor_48_e8_32s40s_e50_v24?0"AMSCampaignAttributionResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs_e20_v24?08"NSError"16ls32l8s48l8s40l8
+ _associated conformance 20AppleMediaServicesUI26ReviewExtensionHostServiceC0G5Error33_18C8CE08C0219173CFCAE077BAD3B917LLOSHAASQ
+ _objc_msgSend$_URLToAttributeForOptIn:URL:
+ _objc_msgSend$_accessibilityElement:isWithinView:
+ _objc_msgSend$_applyNavigationModel
+ _objc_msgSend$_beginObservingVoiceOverFocus
+ _objc_msgSend$_endObservingVoiceOverFocus
+ _objc_msgSend$_isVoiceOverFocusedOnToast
+ _objc_msgSend$_processCampaignAttributionIfNeeded
+ _objc_msgSend$_runAction:context:depth:completion:
+ _objc_msgSend$_skippedPromise
+ _objc_msgSend$accessibilityContainer
+ _objc_msgSend$createODISession
+ _objc_msgSend$isDescendantOfView:
+ _objc_msgSend$isDismissalPausedForVoiceOver
+ _objc_msgSend$runAction:context:completion:
+ _objc_msgSend$setDismissalPausedForVoiceOver:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setShouldRunCampaignAttribution:
+ _objc_msgSend$shouldRunCampaignAttribution
+ _swift_deallocBox
+ _symbolic So32AMSUIAuthenticateTaskCoordinatorC
+ _symbolic _____ 20AppleMediaServicesUI26ReviewExtensionHostServiceC0G5Error33_18C8CE08C0219173CFCAE077BAD3B917LLO
+ _symbolic _____SgXw 20AppleMediaServicesUI26ReviewExtensionHostServiceC
+ _symbolic _____XDXMT 20AppleMediaServicesUI22FetchBundleImageActionC
+ _symbolic _____yAAyAAy__________G_____y_____GG_____y_____GG 7SwiftUI15ModifiedContentV 018AppleMediaServicesB029_AMSUICommonNavigationBarViewV AA14_PaddingLayoutV AA16_OverlayModifierV AA7DividerV AA016_BackgroundStyleO0V AA8MaterialV
+ _symbolic _____yAAyAAy__________G_____y_____SgGG_____yAAyAAyAAyAF_____GAEy_____GG_____y_____GGSgGG 7SwiftUI15ModifiedContentV 018AppleMediaServicesB043_AMSUICommonNavigationRepresentableProviderV AA30_SafeAreaRegionsIgnoringLayoutV AA16_OverlayModifierV AD01_hI7BarViewV AA06_InsettR0V AA08_PaddingP0V AA7DividerV AA016_BackgroundStyleR0V AA8MaterialV
+ _symbolic _____yScCy___________pGSgG 15Synchronization5MutexVAARi_zrlE 20AppleMediaServicesUI12ReviewResultO s5ErrorP
+ _symbolic _____yScCy___________pGSgG 15Synchronization5_CellVAARi_zrlE 20AppleMediaServicesUI12ReviewResultO s5ErrorP
+ _symbolic _____y_____G 7SwiftUI24_BackgroundStyleModifierV AA8MaterialV
+ _symbolic _____y_____yAAyAAy__________G_____y_____SgGG_____yAAyAAyAAyAF_____GAEy_____GG_____y_____GGSgGG_Qo_ 7SwiftUI4ViewPAAE7toolbar_3forQrAA10VisibilityO_AA16ToolbarPlacementVdtFQO AA15ModifiedContentV 018AppleMediaServicesB043_AMSUICommonNavigationRepresentableProviderV AA30_SafeAreaRegionsIgnoringLayoutV AA16_OverlayModifierV AL01_no3BarC0V AA06_InsetcX0V AA08_PaddingV0V AA7DividerV AA016_BackgroundStyleX0V AA8MaterialV
+ _symbolic _____y_____yAByABy__________G_____y_____GG_____y_____GGSgG 7SwiftUI18_InsetViewModifierV AA15ModifiedContentV 018AppleMediaServicesB0025_AMSUICommonNavigationBarD0V AA14_PaddingLayoutV AA08_OverlayE0V AA7DividerV AA016_BackgroundStyleE0V AA8MaterialV
+ _symbolic _____z_Xx 10Foundation3URLV
+ get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE7toolbar_3forQrAA10VisibilityO_AA16ToolbarPlacementVdtFQOyAA15ModifiedContentVyAKyAKy018AppleMediaServicesB043_AMSUICommonNavigationRepresentableProviderVAA30_SafeAreaRegionsIgnoringLayoutVGAA16_OverlayModifierVyAL01_no3BarC0VSgGGAA06_InsetcX0VyAKyAKyAKyAuA08_PaddingV0VGASyAA7DividerVGGAA016_BackgroundStyleX0VyAA8MaterialVGGSgGG_Qo_HO
- -[AMSUIBubbleTipViewController _transferBackgroundColorForPopover]
- GCC_except_table36
- GCC_except_table45
- GCC_except_table58
- _objc_msgSend$_transferBackgroundColorForPopover
- _symbolic _____yAAyAAy__________G_____y_____SgGG_____yAAyAAyAF_____GAEy_____GGSgGG 7SwiftUI15ModifiedContentV 018AppleMediaServicesB043_AMSUICommonNavigationRepresentableProviderV AA30_SafeAreaRegionsIgnoringLayoutV AA16_OverlayModifierV AD01_hI7BarViewV AA06_InsettR0V AA08_PaddingP0V AA7DividerV
- _symbolic _____y_____yAAyAAy__________G_____y_____SgGG_____yAAyAAyAF_____GAEy_____GGSgGG_Qo_ 7SwiftUI4ViewPAAE7toolbar_3forQrAA10VisibilityO_AA16ToolbarPlacementVdtFQO AA15ModifiedContentV 018AppleMediaServicesB043_AMSUICommonNavigationRepresentableProviderV AA30_SafeAreaRegionsIgnoringLayoutV AA16_OverlayModifierV AL01_no3BarC0V AA06_InsetcX0V AA08_PaddingV0V AA7DividerV
- _symbolic _____y_____yABy__________G_____y_____GGSgG 7SwiftUI18_InsetViewModifierV AA15ModifiedContentV 018AppleMediaServicesB0025_AMSUICommonNavigationBarD0V AA14_PaddingLayoutV AA08_OverlayE0V AA7DividerV
- get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE7toolbar_3forQrAA10VisibilityO_AA16ToolbarPlacementVdtFQOyAA15ModifiedContentVyAKyAKy018AppleMediaServicesB043_AMSUICommonNavigationRepresentableProviderVAA30_SafeAreaRegionsIgnoringLayoutVGAA16_OverlayModifierVyAL01_no3BarC0VSgGGAA06_InsetcX0VyAKyAKyAuA08_PaddingV0VGASyAA7DividerVGGSgGG_Qo_HO
CStrings:
+ "%{public}@: [%{public}@] Campaign attribution resolved"
+ "Biometrics availability check: "
+ "Campaign attribution resolved"
+ "Maximum chain depth exceeded"
+ "No handler for authentication. Presenting interactive authentication."
+ "failureAction"
+ "nextAction"
+ "successAction"
- "Could not handle AMSAuthenticateRequest"
```
