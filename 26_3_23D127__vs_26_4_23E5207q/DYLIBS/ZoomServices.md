## ZoomServices

> `/System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x53c8
-  __TEXT.__auth_stubs: 0x4d0
+3191.19.0.0.0
+  __TEXT.__text: 0x57e0
+  __TEXT.__auth_stubs: 0x4b0
   __TEXT.__objc_methlist: 0x70c
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__cstring: 0x7c7
+  __TEXT.__cstring: 0x806
   __TEXT.__oslogstring: 0x4c
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__unwind_info: 0x1e8
   __TEXT.__objc_classname: 0x91
   __TEXT.__objc_methname: 0x1819
   __TEXT.__objc_methtype: 0x4ae

   __DATA_CONST.__objc_selrefs: 0x6a0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0x640

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E4488AA9-80B2-3855-9FE2-75D567338DCF
+  UUID: BED767EF-0A65-3D6D-AFA1-3530E927A4A4
   Functions: 139
-  Symbols:   618
+  Symbols:   616
   CStrings:  438
 
Symbols:
+ ___block_literal_global.474
+ ___block_literal_global.729
+ ___block_literal_global.742
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x23
- ___block_literal_global.435
- ___block_literal_global.690
- ___block_literal_global.703
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x25
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[AXZoomListenerContainer setIdentifier:] : 12 -> 64
~ +[ZoomServices sharedInstance] : 68 -> 84
~ -[ZoomServices init] : 520 -> 532
~ __registerObservers : 112 -> 120
~ -[ZoomServices dealloc] : 112 -> 116
~ -[ZoomServices _checkSpringBoardStarted] : 284 -> 288
~ -[ZoomServices _zoomChanged:] : 604 -> 628
~ -[ZoomServices _applicationWillSuspend:] : 360 -> 376
~ -[ZoomServices zoomWindowClient] : 300 -> 320
~ -[ZoomServices registerForCoalescedZoomAttributesWithChangedHandler:onDisplay:] : 364 -> 380
~ -[ZoomServices removeCoalescedZoomAttributesChangedHandler:] : 536 -> 548
~ ___60-[ZoomServices removeCoalescedZoomAttributesChangedHandler:]_block_invoke : 68 -> 72
~ -[ZoomServices registerForZoomAttributes:onDisplay:updatesImmediatelyWithChangedHandler:] : 680 -> 704
~ -[ZoomServices removeZoomAttributesChangedHandler:] : 988 -> 1024
~ ___51-[ZoomServices removeZoomAttributesChangedHandler:]_block_invoke : 68 -> 72
~ -[ZoomServices notifyZoomFocusDidChangeWithType:rect:contextId:displayId:] : 252 -> 256
~ -[ZoomServices notifyZoomFocusDidChangeWithType:rect:contextId:keyboardFrame:displayId:] : 560 -> 596
~ -[ZoomServices notifyZoomKeyboardWillBecomeVisibleWithFrame:inAppWithBundleID:displayID:] : 380 -> 396
~ -[ZoomServices notifyZoomKeyboardWillHideInAppWithBundleID:displayID:] : 256 -> 264
~ -[ZoomServices notifyZoomKeyboardDidHideInAppWithBundleID:displayID:] : 256 -> 264
~ -[ZoomServices notifyZoomLockButtonWasPressed] : 92 -> 96
~ -[ZoomServices notifyZoomDeviceWasUnlocked] : 92 -> 96
~ -[ZoomServices notifyZoomDeviceWillWake] : 92 -> 96
~ -[ZoomServices notifyZoomHomeButtonWasPressed] : 92 -> 96
~ -[ZoomServices notifyZoomLensModeWasChangedInSettingsTo:] : 220 -> 228
~ -[ZoomServices notifyZoomDockPositionWasChangedInSettingsTo:] : 220 -> 228
~ -[ZoomServices notifyZoomIdleSlugOpacityChangedTo:] : 248 -> 260
~ -[ZoomServices notifyZoomFluidSwitcherGestureWillBegin] : 92 -> 96
~ -[ZoomServices notifyZoomAppActivationAnimationWillBegin] : 92 -> 96
~ -[ZoomServices notifyZoomAppDeactivationAnimationWillBegin] : 92 -> 96
~ -[ZoomServices notifyZoomAppSwitcherRevealAnimationWillBegin] : 92 -> 96
~ -[ZoomServices notifyZoomReturnedToClockFaceAtIdle] : 92 -> 96
~ -[ZoomServices notifyZoomCarouselLockBegan] : 92 -> 96
~ -[ZoomServices notifyZoomCarouselLockEnded] : 92 -> 96
~ -[ZoomServices notifyZoomFluidSwitcherGestureDidFinish] : 92 -> 96
~ -[ZoomServices notifyZoomFluidSwitcherGestureDidFinishWithDock] : 92 -> 96
~ -[ZoomServices notifyZoomAppActivationAnimationDidFinish] : 92 -> 96
~ -[ZoomServices notifyZoomAppDidBecomeActive:keyboardFrameIfVisible:] : 340 -> 352
~ -[ZoomServices notifyZoomAppDidEnterBackground:] : 252 -> 260
~ -[ZoomServices notifyZoomWillShowBrailleInputUI] : 92 -> 96
~ -[ZoomServices notifyZoomSOSMedicalIDShown] : 120 -> 124
~ -[ZoomServices notifyZoomWillHideBrailleInputUI] : 92 -> 96
~ -[ZoomServices notifyZoomDragWillStart] : 92 -> 96
~ -[ZoomServices notifyZoomDragWillEnd] : 92 -> 96
~ -[ZoomServices _handleChangedAttributes:] : 1688 -> 1816
~ ___41-[ZoomServices _handleChangedAttributes:]_block_invoke : 84 -> 88
~ -[ZoomServices reachabilityScaleFactor] : 152 -> 160
~ -[ZoomServices zoomFrameOnDisplay:] : 180 -> 188
~ -[ZoomServices zoomLevelOnDisplay:] : 136 -> 144
~ -[ZoomServices getCurrentZoomLevelOnDisplay:] : 288 -> 308
~ -[ZoomServices getCurrentZoomFrameOnDisplay:] : 332 -> 352
~ -[ZoomServices getLastSpeakUnderFingerPhrase] : 148 -> 160
~ -[ZoomServices toggleZoomMenu] : 124 -> 128
~ -[ZoomServices setZoomLevel:onDisplay:] : 272 -> 288
~ -[ZoomServices _panWithDirection:onDisplay:] : 248 -> 260
~ -[ZoomServices autoPanZoomUsingLocation:withPanningStyle:onDisplay:] : 332 -> 352
~ -[ZoomServices activeZoomModeOnDisplay:] : 136 -> 144
~ -[ZoomServices inStandbyModeOnDisplay:] : 136 -> 144
~ -[ZoomServices setZoomWindowClient:] : 12 -> 64
~ -[ZoomServices(PrimaryClientOnly) showZoomLens] : 288 -> 296
~ -[ZoomServices(PrimaryClientOnly) hideZoomLens] : 232 -> 240
~ -[ZoomServices(PrimaryClientOnly) showMagnifier] : 156 -> 160
~ -[ZoomServices(PrimaryClientOnly) isMagnifierVisibleWithCompletion:] : 204 -> 212
~ -[ZoomServices(PrimaryClientOnly) startMagnifierChangeTripleClickMenu:] : 128 -> 136
~ ___71-[ZoomServices(PrimaryClientOnly) startMagnifierChangeTripleClickMenu:]_block_invoke : 128 -> 136
~ -[ZoomServices(PrimaryClientOnly) userInterfaceClient:processMessageFromServer:withIdentifier:error:] : 296 -> 300
~ ___101-[ZoomServices(PrimaryClientOnly) userInterfaceClient:processMessageFromServer:withIdentifier:error:]_block_invoke : 1076 -> 1116
~ -[ZoomServices(PrimaryClientOnly) connectionWithServiceWasInterruptedForUserInterfaceClient:] : 380 -> 392
~ _ZOTWindowServerDisplay : 128 -> 148
~ +[ZoomServicesGreyCommandInfo defaultCustomizeGestures] : 180 -> 184
~ +[ZoomServicesGreyCommandInfo isZoomGreyFeatureOn] : 140 -> 144
~ +[ZoomServicesGreyCommandInfo _pairedDevice] : 176 -> 208
~ +[ZoomServicesKeyboardManager sharedInstance] : 160 -> 176
~ -[ZoomServicesKeyboardManager keyboardCommandForEvent:] : 1136 -> 1232
CStrings:
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/AccessibilityUmbrellaFramework/Frameworks/ZoomServices/Source/ZoomServices.m"
+ "1FD8E157-332F-481C-B7DE-7E80973B07BF"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/AccessibilityUmbrellaFramework/Frameworks/ZoomServices/Source/ZoomServices.m"
- "1FD8E157-2B7C-45B6-B939-FFB8BE14E27F"

```
