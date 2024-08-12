## BackBoard

> `/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard`

```diff

-2952.1.0.0.0
-  __TEXT.__text: 0x1f830
-  __TEXT.__auth_stubs: 0x1220
-  __TEXT.__objc_methlist: 0x1bc4
-  __TEXT.__const: 0xda
-  __TEXT.__gcc_except_tab: 0x578
-  __TEXT.__cstring: 0x1f4d
-  __TEXT.__oslogstring: 0x13f5
+2955.4.0.0.0
+  __TEXT.__text: 0x1e87c
+  __TEXT.__auth_stubs: 0x11c0
+  __TEXT.__objc_methlist: 0x1a54
+  __TEXT.__const: 0xe2
+  __TEXT.__gcc_except_tab: 0x584
+  __TEXT.__cstring: 0x1ef7
+  __TEXT.__oslogstring: 0x13fd
   __TEXT.__dlopen_cstrs: 0x2d9
-  __TEXT.__unwind_info: 0xa70
+  __TEXT.__unwind_info: 0xa18
   __TEXT.__objc_classname: 0x439
-  __TEXT.__objc_methname: 0x62d9
+  __TEXT.__objc_methname: 0x5e3e
   __TEXT.__objc_methtype: 0x93b
-  __TEXT.__objc_stubs: 0x58e0
+  __TEXT.__objc_stubs: 0x5320
   __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__const: 0x850
+  __DATA_CONST.__const: 0x7e0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a00
+  __DATA_CONST.__objc_selrefs: 0x1878
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x920
-  __AUTH_CONST.__const: 0xb00
-  __AUTH_CONST.__cfstring: 0x1be0
-  __AUTH_CONST.__objc_const: 0x2f78
+  __AUTH_CONST.__auth_got: 0x8f0
+  __AUTH_CONST.__const: 0xac0
+  __AUTH_CONST.__cfstring: 0x1b60
+  __AUTH_CONST.__objc_const: 0x2f28
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x138
+  __DATA.__objc_ivar: 0x130
   __DATA.__data: 0x2b8
   __DATA.__bss: 0x175
   __DATA_DIRTY.__objc_data: 0xa00

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 843
-  Symbols:   1378
-  CStrings:  1531
+  Functions: 807
+  Symbols:   1338
+  CStrings:  1480
 
Symbols:
+ _CFNotificationCenterRemoveEveryObserver
+ _kAXSContinuityDisplayStateChangedNotification
- _OBJC_CLASS_$_AXSubsystemInvertColors
- __AXDarkenSystemColors
- __AXSAssistiveTouchSetUIEnabled
- __AXSEnhanceBackgroundContrastEnabled
- __AXSReduceMotionEnabled
- __AXSSetDarkenSystemColors
- __AXSSetEnhanceBackgroundContrastEnabled
- __AXSSetReduceMotionEnabled
CStrings:
+ "\x01\x12"
+ "%!s(MISSING) isContinuitySessionActive: %!@(MISSING)"
+ "-[AXBHardwareManager _updateForContinuityStateChange]"
+ "Initialize AX backboard server"
+ "NO"
+ "Started AX Backboard server %!@(MISSING)"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_springboardContinuityCheckQueue"
+ "YES"
+ "_springboardContinuityCheckQueue"
+ "_updateForContinuityStateChange"
+ "com.apple.AXBackBoard.ContinuitySessionCheck"
+ "isContinuitySessionActive"
+ "setIgnoreEventsForContinuitySession:"
+ "setSpringboardContinuityCheckQueue:"
+ "springboardContinuityCheckQueue"
- "\x01\x11"
- "/System/Library/AccessibilityBundles/BackBoardExtras.axbundle"
- "AXAssetAndDataServer"
- "AXAssetClient-hearingaidmodule"
- "TB,N,VswitchControlHasScreenSwitch"
- "TB,N,VswitchControlRendersDeviceUnusable"
- "Telling client to fade for smart"
- "Toggling Guided Access via triple click home."
- "Trying to turn on hearing aid module: %!d(MISSING)"
- "Waiting %!f(MISSING) before toggling"
- "_disableSwitchControlWithHandler:"
- "_isDisableSwitchAlertVisible"
- "_toggleAssistiveTouch"
- "_toggleAssistiveTouchOffMainThread"
- "_toggleBackgroundSounds"
- "_toggleClassicInvertColors"
- "_toggleColorFilter"
- "_toggleCommandAndControl"
- "_toggleDisplayAppearance"
- "_toggleGrayscale"
- "_toggleGuidedAccess"
- "_toggleHoverText"
- "_toggleHoverTextTyping"
- "_toggleIncreaseContrast"
- "_toggleLeftRightAudioBalance"
- "_toggleLiveSpeech"
- "_toggleLiveTranscription"
- "_toggleLocalizationCaptionPanel"
- "_toggleReduceMotion"
- "_toggleReduceTransparency"
- "_toggleReduceWhitePoint"
- "_toggleSwitchOver"
- "_toggleSwitchOverOffMainThread"
- "_toggleTouchAccommodations"
- "_toggleTwiceRemoteScreeen"
- "_toggleWatchControl"
- "_toggleWhiteOnBlack"
- "_toggleWhiteOnBlackOffMainThread"
- "_toggleZoom"
- "_toggleZoomOffMainThread"
- "_turnOnHearingControlCenterModule"
- "animationDuration"
- "attemptToEnterClarityBoard"
- "attemptToPresentNearbyDeviceControlPicker"
- "attemptToToggleConversationBoost"
- "attemptToToggleTwiceRemoteScreen"
- "leftRightBalanceEnabled"
- "load"
- "performSelectorInBackground:withObject:"
- "setClassicInvertColors:"
- "setLastSmartInvertColorsEnablement:"
- "setLeftRightBalanceEnabled:"
- "setLocalizationQACaptionMode:"
- "setTouchAccommodationsEnabled:"
- "switchControlHasScreenSwitch"
- "toggleBackgroundSounds"
- "toggleColorFilter"
- "toggleDarkMode"
- "toggleFullKeyboardAccess"
- "toggleGuidedAccess"
- "toggleHoverText"
- "toggleHoverTextTyping"
- "toggleLiveSpeech"
- "toggleLiveTranscription"
- "toggleReduceWhitePoint"
- "toggleZoomOffMainThread"

```
