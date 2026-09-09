## Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__data`

```diff

 150.0.2.0.0
-  __TEXT.__text: 0x1e77c
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_stubs: 0x6220
-  __TEXT.__objc_methlist: 0x2d90
+  __TEXT.__text: 0x1facc
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_stubs: 0x6500
+  __TEXT.__objc_methlist: 0x2eb8
   __TEXT.__const: 0xa8
-  __TEXT.__objc_methname: 0x8b1c
-  __TEXT.__oslogstring: 0x35e9
-  __TEXT.__cstring: 0x35b5
-  __TEXT.__objc_classname: 0x689
-  __TEXT.__objc_methtype: 0x257a
-  __TEXT.__gcc_except_tab: 0x118
+  __TEXT.__objc_methname: 0x8dc2
+  __TEXT.__oslogstring: 0x3956
+  __TEXT.__cstring: 0x36a7
+  __TEXT.__objc_classname: 0x699
+  __TEXT.__objc_methtype: 0x2597
+  __TEXT.__gcc_except_tab: 0x150
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x6f8
-  __DATA_CONST.__const: 0xa08
-  __DATA_CONST.__cfstring: 0x1960
-  __DATA_CONST.__objc_classlist: 0x118
+  __TEXT.__unwind_info: 0x748
+  __DATA_CONST.__const: 0xa80
+  __DATA_CONST.__cfstring: 0x1980
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x4c0
-  __DATA.__objc_const: 0x6558
-  __DATA.__objc_selrefs: 0x22c0
-  __DATA.__objc_ivar: 0x20c
-  __DATA.__objc_data: 0xaf0
+  __DATA_CONST.__auth_got: 0x438
+  __DATA_CONST.__got: 0x4d8
+  __DATA.__objc_const: 0x6718
+  __DATA.__objc_selrefs: 0x2390
+  __DATA.__objc_ivar: 0x224
+  __DATA.__objc_data: 0xb40
   __DATA.__data: 0xce0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/CoreText.framework/CoreText

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 793
-  Symbols:   307
-  CStrings:  2355
+  Functions: 822
+  Symbols:   310
+  CStrings:  2410
 
Symbols:
+ _NSStringFromCGRect
+ _OBJC_CLASS_$_CMAngleManager
+ _OBJC_CLASS_$_NSOperationQueue
CStrings:
+ "%{public}s: [DREHingeManager] CMAngleManager unavailable (no hinge on this hardware); not observing."
+ "%{public}s: [DREHingeManager] Display: name=%{public}@ device=%{public}@ main=%d bounds=%{public}@"
+ "%{public}s: [DREHingeManager] Hinge state %ld -> %ld (angle=%.1f°)"
+ "%{public}s: [DREHingeManager] No display configuration for hinge state %ld; not switching."
+ "%{public}s: [DREHingeManager] Only %lu always-connected display(s); nothing to switch between."
+ "%{public}s: [DREHingeManager] Started observing hinge angle."
+ "%{public}s: [DisplayManager] No configuration for always-connected display %{public}@; skipping."
+ "%{public}s: [SceneManager] Moving %lu scene(s) from %{public}@ to %{public}@ (%{public}@)"
+ "%{public}s: [SceneManager] Scenes already on display %{public}@; no move needed"
+ "%{public}s: [SceneManager] moveToDisplayConfiguration: called with nil configuration; ignoring"
+ "+[DREHingeManager shouldMonitorHingeAngle]"
+ "-[DREHingeManager _handleAngle:]"
+ "-[DREHingeManager start]"
+ "-[DisplayManager internalDisplayConfigurations]"
+ "-[SceneManager moveToDisplayConfiguration:]"
+ "@\"CMAngleManager\""
+ "@\"DREHingeManager\""
+ "@\"NSOperationQueue\""
+ "@24@0:8q16"
+ "DREHingeManager"
+ "T@\"CMAngleManager\",&,N,V_angleManager"
+ "T@\"DREHingeManager\",&,V_hingeManager"
+ "T@\"NSMutableDictionary\",&,V_presentationBindersByIdentity"
+ "T@\"NSOperationQueue\",&,N,V_angleQueue"
+ "Tq,N,V_currentState"
+ "_angleManager"
+ "_angleQueue"
+ "_currentState"
+ "_displayConfigurationForHingeState:"
+ "_handleAngle:"
+ "_hingeManager"
+ "_presentationBinderForConfiguration:"
+ "_presentationBindersByIdentity"
+ "allValues"
+ "alwaysConnectedIdentities"
+ "angleDegrees"
+ "angleManager"
+ "angleQueue"
+ "com.apple.devicerecovery.hinge"
+ "configurationForIdentity:"
+ "currentState"
+ "deviceName"
+ "hingeManager"
+ "identity"
+ "internalDisplayConfigurations"
+ "isAvailable"
+ "isMainDisplay"
+ "moveToDisplayConfiguration:"
+ "presentationBindersByIdentity"
+ "setAngleManager:"
+ "setAngleQueue:"
+ "setCurrentState:"
+ "setHingeManager:"
+ "setMaxConcurrentOperationCount:"
+ "setPresentationBindersByIdentity:"
+ "shouldMonitorHingeAngle"
+ "startAngleUpdatesToQueue:handler:"
+ "stopAngleUpdates"
+ "updateActiveDisplayConfiguration:"
+ "v16@?0@\"CMAngle\"8"
- "@\"UIRootWindowScenePresentationBinder\""
- "T@\"UIRootWindowScenePresentationBinder\",&,V_rootWindowScenePresentationBinder"
- "_rootWindowScenePresentationBinder"
- "rootWindowScenePresentationBinder"
- "setRootWindowScenePresentationBinder:"
```
