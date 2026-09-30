## HeartRhythmUI

> `/System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x329e8
-  __TEXT.__objc_methlist: 0x4cd0
+7027.1.36.2.7
+  __TEXT.__text: 0x328b4
+  __TEXT.__objc_methlist: 0x4d10
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0x3b13
+  __TEXT.__cstring: 0x3ae0
   __TEXT.__oslogstring: 0x10b3
   __TEXT.__ustring: 0xa
   __TEXT.__gcc_except_tab: 0x1bc
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1040
+  __TEXT.__unwind_info: 0x1038
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x820
+  __DATA_CONST.__const: 0x7f8
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3008
+  __DATA_CONST.__objc_selrefs: 0x3030
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x660
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x3180
-  __AUTH_CONST.__objc_const: 0x6cf8
+  __AUTH_CONST.__objc_const: 0x6d58
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x428
   __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x4dc
+  __DATA.__objc_ivar: 0x4e4
   __DATA.__data: 0x668
   __DATA_DIRTY.__objc_data: 0x500
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/HealthFoundationUI.framework/HealthFoundationUI
   - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1514
-  Symbols:   3907
-  CStrings:  491
+  Functions: 1522
+  Symbols:   3919
+  CStrings:  490
 
Symbols:
+ -[HROnboardingElectrocardiogramTakeRecordingViewController initForOnboarding:isRecordingSkippable:shouldObserveForNewRecording:]
+ -[HROnboardingElectrocardiogramTakeRecordingViewController setShouldObserveForNewRecording:]
+ -[HROnboardingElectrocardiogramTakeRecordingViewController shouldObserveForNewRecording]
+ -[HRSpeedBumpViewController _scrollToContentBottom]
+ -[HRSpeedBumpViewController needsScrollToContentBottom]
+ -[HRSpeedBumpViewController setNeedsScrollToContentBottom:]
+ -[HRSpeedBumpViewController viewDidLayoutSubviews]
+ GCC_except_table16
+ _OBJC_CLASS_$_HKRegulatoryDomainManager
+ _OBJC_IVAR_$_HROnboardingElectrocardiogramTakeRecordingViewController._shouldObserveForNewRecording
+ _OBJC_IVAR_$_HRSpeedBumpViewController._needsScrollToContentBottom
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _objc_msgSend$_scrollToContentBottom
+ _objc_msgSend$currentEstimate
+ _objc_msgSend$initForOnboarding:isRecordingSkippable:shouldObserveForNewRecording:
+ _objc_msgSend$needsScrollToContentBottom
+ _objc_msgSend$setNeedsScrollToContentBottom:
+ _objc_msgSend$shouldObserveForNewRecording
- -[HRSpeedBumpViewController _scrollBubbleViewToVisible:]
- -[HRSpeedBumpViewController viewWillAppear:]
- _OBJC_CLASS_$_HKMobileCountryCodeManager
- ___133-[HRElectrocardiogramCurrentLocationOnboardingDeterminer isElectrocardiogramOnboardingAvailableInCurrentLocationForWatch:completion:]_block_invoke
- ___134-[HROnboardingAtrialFibrillationIntroViewController _isAtrialFibrillationDetectionOnboardingAvailableInCurrentLocationForActiveWatch:]_block_invoke
- ___block_descriptor_56_e8_32s40bs_e44_v24?0"<HKCurrentCountryCode>"8"NSError"16ls32l8s40l8
- _objc_msgSend$_scrollBubbleViewToVisible:
- _objc_msgSend$fetchMobileCountryCodeFromCellularWithCompletion:
CStrings:
+ "No location determined"
- "Unable to determine location"
- "v24@?0@\"<HKCurrentCountryCode>\"8@\"NSError\"16"
```
