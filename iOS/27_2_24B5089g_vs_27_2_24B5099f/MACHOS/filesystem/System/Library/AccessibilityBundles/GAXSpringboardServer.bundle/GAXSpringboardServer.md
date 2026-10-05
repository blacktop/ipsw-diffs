## GAXSpringboardServer

> `/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1067.3.1.0.0
-  __TEXT.__text: 0x15ba0
+1067.3.3.0.0
+  __TEXT.__text: 0x15c84
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x2f60
-  __TEXT.__objc_methlist: 0x1edc
+  __TEXT.__objc_methlist: 0x1ef4
   __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0x464
-  __TEXT.__cstring: 0x50c2
-  __TEXT.__objc_methname: 0x599e
-  __TEXT.__oslogstring: 0x1bc8
+  __TEXT.__cstring: 0x50fd
+  __TEXT.__objc_methname: 0x5a0a
+  __TEXT.__oslogstring: 0x1c59
   __TEXT.__objc_classname: 0xcff
-  __TEXT.__objc_methtype: 0x1000
+  __TEXT.__objc_methtype: 0x1062
   __TEXT.__unwind_info: 0x820
   __DATA_CONST.__const: 0x1238
-  __DATA_CONST.__cfstring: 0x4ce0
+  __DATA_CONST.__cfstring: 0x4d00
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x260
-  __DATA.__objc_const: 0x3d00
-  __DATA.__objc_selrefs: 0x14e8
+  __DATA.__objc_const: 0x3d10
+  __DATA.__objc_selrefs: 0x14f8
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x1b30
   __DATA.__data: 0x188

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 552
-  Symbols:   557
-  CStrings:  1599
+  Functions: 554
+  Symbols:   559
+  CStrings:  1605
 
Symbols:
+ _GAXBackboardStateAllowsAllTouchByOverride
+ _GAXBackboardStateAllowsAllTouchForTransientSystemUI
CStrings:
+ "  overrideAllowsAllTouchAuthenticatingWithBiometrics: %ld\n"
+ "Home grabber still suppressed with no active Guided Access session; clearing stale suppression and applying mode %ld."
+ "SpringBoard wants to update Home Grabber display mode but Guided Access is suppressing it. Will apply when Guided Access ends."
+ "switchNativeFocusedApplicationToProcessIdentifier:sceneIdentifier:"
+ "toggleLiveRecognitionWithServerInstance:"
+ "v28@0:8i16@\"NSString\"20"
+ "v28@0:8i16@20"
+ "v44@0:8{?=IIIIIIb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
+ "v52@0:8{?=IIIIIIb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@?44"
+ "v60@0:8I16B20{?=IIIIIIb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24q52"
+ "{?=\"mode\"I\"passcodeWindowContextID\"I\"voiceOverItemChooserWindowContextID\"I\"tripleClickSheetWindowContextID\"I\"assistiveTouchPort\"I\"profileConfiguration\"I\"shouldBlockAllEvents\"b1\"restartingAndWasActiveBeforeRestart\"b1\"verifyingDeviceUnlockInSAM\"b1\"isPasscodeViewVisible\"b1\"isRestricted\"b1\"overrideAllowsAllTouchSBMiniAlertIsShowing\"b1\"overrideAllowsAllTouchCallStateIsChanging\"b1\"overrideAllowsAllTouchMakingEmergencyCall\"b1\"overrideAllowsAllTouchAuthenticatingWithBiometrics\"b1\"overrideIgnoresAllTouchAllowedAppNotFound\"b1\"overrideIgnoresAllTouchVerifyingIntegrity\"b1\"allowsTouch\"b1\"allowsLockButton\"b1\"allowsAppExit\"b1\"allowsHomeButton\"b1\"allowsVolumeButtons\"b1\"allowsRingerSwitch\"b1\"allowsMotion\"b1\"allowsAutolock\"b1\"allowsKeyboardTextInput\"b1\"allowsProximity\"b1\"allowsLayoutTransitions\"b1\"allowsDisplayChanges\"b1}"
- "Unexpectedly tried to update home grabber display mode change for a floating window after creation."
- "v44@0:8{?=IIIIIIb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
- "v52@0:8{?=IIIIIIb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@?44"
- "v60@0:8I16B20{?=IIIIIIb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24q52"
- "{?=\"mode\"I\"passcodeWindowContextID\"I\"voiceOverItemChooserWindowContextID\"I\"tripleClickSheetWindowContextID\"I\"assistiveTouchPort\"I\"profileConfiguration\"I\"shouldBlockAllEvents\"b1\"restartingAndWasActiveBeforeRestart\"b1\"verifyingDeviceUnlockInSAM\"b1\"isPasscodeViewVisible\"b1\"isRestricted\"b1\"overrideAllowsAllTouchSBMiniAlertIsShowing\"b1\"overrideAllowsAllTouchCallStateIsChanging\"b1\"overrideAllowsAllTouchMakingEmergencyCall\"b1\"overrideIgnoresAllTouchAllowedAppNotFound\"b1\"overrideIgnoresAllTouchVerifyingIntegrity\"b1\"allowsTouch\"b1\"allowsLockButton\"b1\"allowsAppExit\"b1\"allowsHomeButton\"b1\"allowsVolumeButtons\"b1\"allowsRingerSwitch\"b1\"allowsMotion\"b1\"allowsAutolock\"b1\"allowsKeyboardTextInput\"b1\"allowsProximity\"b1\"allowsLayoutTransitions\"b1\"allowsDisplayChanges\"b1}"
```
