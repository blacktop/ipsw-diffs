## GAXSpringboardServer

> `/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-1061.0.0.0.0
-  __TEXT.__text: 0x158bc
+1064.0.0.0.0
+  __TEXT.__text: 0x15b8c
   __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_stubs: 0x2e80
-  __TEXT.__objc_methlist: 0x1f04
+  __TEXT.__objc_stubs: 0x2f00
+  __TEXT.__objc_methlist: 0x1ec4
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x42c
+  __TEXT.__gcc_except_tab: 0x46c
   __TEXT.__cstring: 0x4fd7
-  __TEXT.__objc_methname: 0x58cb
-  __TEXT.__oslogstring: 0x19d7
-  __TEXT.__objc_classname: 0xd4f
-  __TEXT.__objc_methtype: 0xf7a
-  __TEXT.__unwind_info: 0x6c8
-  __DATA_CONST.__const: 0x1188
-  __DATA_CONST.__cfstring: 0x4bc0
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __TEXT.__objc_methname: 0x590b
+  __TEXT.__oslogstring: 0x1ac0
+  __TEXT.__objc_classname: 0xcff
+  __TEXT.__objc_methtype: 0xf7e
+  __TEXT.__unwind_info: 0x6d8
+  __DATA_CONST.__const: 0x1218
+  __DATA_CONST.__cfstring: 0x4c20
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0x28

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x248
-  __DATA.__objc_const: 0x3df8
-  __DATA.__objc_selrefs: 0x14a8
+  __DATA.__objc_const: 0x3ce0
+  __DATA.__objc_selrefs: 0x14c0
   __DATA.__objc_ivar: 0x5c
-  __DATA.__objc_data: 0x1bd0
+  __DATA.__objc_data: 0x1b30
   __DATA.__data: 0x188
   __DATA.__bss: 0x5a
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 544
-  Symbols:   546
-  CStrings:  1578
+  Functions: 543
+  Symbols:   543
+  CStrings:  1585
 
Symbols:
+ _GAXUIMessageKeyShouldDriveSiriAssessmentRestriction
- _OBJC_CLASS_$_GAXSBSBLockScreenOrientationManager
- _OBJC_CLASS_$___GAXSBSBLockScreenOrientationManager_super
- _OBJC_METACLASS_$_GAXSBSBLockScreenOrientationManager
- _OBJC_METACLASS_$___GAXSBSBLockScreenOrientationManager_super
CStrings:
+ "Could not make SpringBoard frontmost within %.0f seconds; failing fast so GAX releases the input block"
+ "Guided Access orientation restore"
+ "Guided Access restoring TraitsArbiter orientation on exit (userLocked=%d orientation=%ld)"
+ "SBHomeButtonPressHandler"
+ "SBOrientationLockManager"
+ "SBPolicyAggregator"
+ "SBReachabilityController"
+ "Session app (%@) is already foreground and running; skipping making SpringBoard frontmost"
+ "TRAArbiter"
+ "TRAArbiterUpdateContext"
+ "configureWithWorkspaceEntity:referenceFrame:contentOrientation:containerOrientation:layoutRole:sbsDisplayLayoutRole:zOrderIndex:spaceConfiguration:floatingConfiguration:hasClassicAppOrientationMismatch:sizingPolicy:"
+ "homeButtonPressHandler"
+ "iconModel"
+ "idleTimerGlobalCoordinator"
+ "initWithBuilder:"
+ "isUserLocked"
+ "reduceAmbientFullScreenLiveActivityWithServerInstance:"
+ "setNeedsUpdateArbitrationWithContext:"
+ "setReason:"
+ "setUserInteractionEnabled:"
+ "should drive siri assessment restriction"
+ "systemGestureManager"
+ "userLockOrientation"
+ "v124@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24q56q64q72q80q88q96q104B112q116"
+ "validateClass:hasProperty:withType:"
- "GAXSBSBLockScreenOrientationManager"
- "Guided Access orientation unlock"
- "Guided Access unlocking TraitsArbiter orientation"
- "SBLockScreenOrientationManager"
- "SBMainDisplayPolicyAggregator"
- "SBReachabilityManager"
- "SBUIController"
- "TRAArbitrator"
- "__GAXSBSBLockScreenOrientationManager_super"
- "_shouldBeginFloatingApplicationPinGesture:"
- "_uiController"
- "appSwitcherHeaderIconImageCache"
- "configureWithWorkspaceEntity:referenceFrame:contentOrientation:containerOrientation:layoutRole:sbsDisplayLayoutRole:spaceConfiguration:floatingConfiguration:hasClassicAppOrientationMismatch:sizingPolicy:"
- "model"
- "scene:didReceiveActions:"
- "setNeedsUpdateArbitrationWithReason:"
- "updateInterfaceOrientationWithRequestedOrientation:animated:"
- "v116@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24q56q64q72q80q88q96B104q108"
```
