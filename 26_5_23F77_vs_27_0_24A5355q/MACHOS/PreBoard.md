## PreBoard

> `/Applications/PreBoard.app/PreBoard`

```diff

-4557.5.7.101.0
-  __TEXT.__text: 0xc938
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x3500
-  __TEXT.__objc_methlist: 0x1600
-  __TEXT.__objc_methname: 0x4b70
-  __TEXT.__objc_classname: 0x40f
-  __TEXT.__objc_methtype: 0x1460
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x68e
-  __TEXT.__gcc_except_tab: 0xf0
-  __TEXT.__oslogstring: 0x42a
-  __TEXT.__unwind_info: 0x4e8
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x768
-  __DATA_CONST.__cfstring: 0x600
+4615.3.107.0.0
+  __TEXT.__text: 0xca28
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_stubs: 0x3640
+  __TEXT.__objc_methlist: 0x15e8
+  __TEXT.__objc_methname: 0x4bed
+  __TEXT.__objc_classname: 0x3de
+  __TEXT.__objc_methtype: 0x136e
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x727
+  __TEXT.__gcc_except_tab: 0xec
+  __TEXT.__oslogstring: 0x5d6
+  __TEXT.__unwind_info: 0x4b8
+  __DATA_CONST.__const: 0x7d0
+  __DATA_CONST.__cfstring: 0x6c0
   __DATA_CONST.__objc_classlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x36b0
-  __DATA.__objc_selrefs: 0x1368
-  __DATA.__objc_ivar: 0x130
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__got: 0x330
+  __DATA.__objc_const: 0x36b8
+  __DATA.__objc_selrefs: 0x1390
+  __DATA.__objc_ivar: 0x138
   __DATA.__objc_data: 0x6e0
-  __DATA.__data: 0x548
+  __DATA.__data: 0x4e8
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter
   - /System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B739F9F-0CC4-396E-BA75-0FD1F7E88739
-  Functions: 391
-  Symbols:   213
-  CStrings:  1080
+  UUID: C88D1017-3E25-3F1F-9446-540CFE524DD2
+  Functions: 404
+  Symbols:   223
+  CStrings:  1103
 
Symbols:
+ _DMGetRequiredPreboardMode
+ _DMPreboardModeDescription
+ _OBJC_CLASS_$_FBSystemShell
+ _OBJC_CLASS_$_NSConstantDictionary
+ __UIFullScreenKeyboardEnabled
+ __bs_set_crash_log_message
+ __os_log_default
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
- __UIKeyboardArbiter_SceneIdentifier
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "Darkboot detected, keeping display dim"
+ "DataMigration launched PreBoard with DMPreboardModeNone"
+ "DataMigration requested preboard mode: %{public}@"
+ "Invalid condition not satisfying: %@"
+ "LAPreboard is required"
+ "Monitor mode: lighting display and exiting (reason:%{public}@)"
+ "Monitor mode: lighting display and exiting on lock button press"
+ "Monitor mode: lighting display and exiting on smart cover open"
+ "PBADataRecoveryViewController.m"
+ "T@\"SBFMobileKeyBag\",&,N,V_mobileKeyBag"
+ "TB,N,GisMonitorMode,V_monitorMode"
+ "UTF8String"
+ "_addKeyboardArbiterSceneToPresentationBinder"
+ "_exitMonitorModeForReason:"
+ "_mobileKeyBag"
+ "_monitorMode"
+ "_presentMonitorViewConroller"
+ "failure in %{public}@ of <%{public}@:%p> (%{public}@:%i) : %{public}@"
+ "initWithAssertionManager:policy:keybag:model:"
+ "initWithContainingStackViewController:authenticationPolicy:keybag:"
+ "initWithContainingStackViewController:keyBag:"
+ "initializationContext"
+ "isMonitorMode"
+ "keyBag"
+ "keyboardFocusTarget"
+ "mobileKeyBag"
+ "monitor"
+ "monitorMode"
+ "none"
+ "observeKeyboardSceneAvailability:"
+ "setMobileKeyBag:"
+ "setMonitorMode:"
+ "stringWithFormat:"
+ "v16@?0@\"FBScene\"8"
+ "wasBootedDark"
- "\v"
- "FBSceneManagerObserver"
- "focusedSceneIdentityDidChange:"
- "identifier"
- "initWithAssertionManager:policy:"
- "initWithContainingStackViewController:"
- "initWithContainingStackViewController:authenticationPolicy:"
- "sceneManager:didAddScene:"
- "sceneManager:didCommitUpdateForScene:transactionID:"
- "sceneManager:didDestroyScene:"
- "sceneManager:willCommitUpdateForScene:transactionID:"
- "sceneManager:willRemoveScene:"
- "sceneManager:willUpdateScene:withSettings:transitionContext:"
- "v24@0:8@\"FBSSceneIdentityToken\"16"
- "v32@0:8@\"FBSceneManager\"16@\"FBScene\"24"
- "v40@0:8@\"FBSceneManager\"16@\"FBScene\"24Q32"
- "v40@0:8@16@24Q32"
- "v48@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"FBSSceneSettings\"32@\"FBSSceneTransitionContext\"40"
- "v48@0:8@16@24@32@40"

```
