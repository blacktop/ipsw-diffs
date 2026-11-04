## PreBoard

> `/Applications/PreBoard.app/PreBoard`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-4637.1.14.103.0
-  __TEXT.__text: 0xc314
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x3640
-  __TEXT.__objc_methlist: 0x15e8
-  __TEXT.__objc_methname: 0x4bed
-  __TEXT.__objc_classname: 0x3de
-  __TEXT.__objc_methtype: 0x136e
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x727
-  __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__oslogstring: 0x5d6
-  __TEXT.__unwind_info: 0x5e0
-  __DATA_CONST.__const: 0x7d0
-  __DATA_CONST.__cfstring: 0x6c0
-  __DATA_CONST.__objc_classlist: 0xb0
+4637.2.11.104.0
+  __TEXT.__text: 0xd030
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0x3b60
+  __TEXT.__objc_methlist: 0x16f0
+  __TEXT.__objc_methname: 0x52d9
+  __TEXT.__objc_classname: 0x3f1
+  __TEXT.__objc_methtype: 0x13d3
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x83b
+  __TEXT.__gcc_except_tab: 0x114
+  __TEXT.__oslogstring: 0x6f6
+  __TEXT.__unwind_info: 0x628
+  __DATA_CONST.__const: 0x888
+  __DATA_CONST.__cfstring: 0x760
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0x338
-  __DATA.__objc_const: 0x36b8
-  __DATA.__objc_selrefs: 0x1390
-  __DATA.__objc_ivar: 0x138
-  __DATA.__objc_data: 0x6e0
+  __DATA_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0x370
+  __DATA.__objc_const: 0x38d8
+  __DATA.__objc_selrefs: 0x1540
+  __DATA.__objc_ivar: 0x158
+  __DATA.__objc_data: 0x730
   __DATA.__data: 0x4e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 404
-  Symbols:   224
-  CStrings:  1049
+  Functions: 436
+  Symbols:   236
+  CStrings:  1142
 
Symbols:
+ _BSEqualObjects
+ _BSFloatGreaterThanOrEqualToFloat
+ _OBJC_CLASS_$_BKSDisplayService
+ _OBJC_CLASS_$_BKSHIDUISensorMode
+ _OBJC_CLASS_$_BKSHIDUISensorService
+ _OBJC_CLASS_$_BLSDisplayReference
+ _OBJC_CLASS_$_CADisplay
+ _OBJC_CLASS_$_CMAngleManager
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_CLASS_$__UIKeyboardInputRehostingSceneSpecification
+ _dispatch_group_wait
+ _notify_post
+ _notify_register_check
+ _notify_set_state
+ _objc_retain_x26
- _BKSHIDServicesSetHIDUILockedStateWithSource
- _OBJC_CLASS_$_FBSceneManager
- _OBJC_CLASS_$_UIKeyboard
- _OBJC_CLASS_$_UIScreen
- __UIFullScreenKeyboardEnabled
CStrings:
+ "\""
+ "<main>"
+ "@\"BKSHIDUISensorService\""
+ "@\"BLSBacklight\""
+ "@\"FBSDisplayConfiguration\""
+ "@\"PBADisplayResolver\""
+ "@24@0:8d16"
+ "Angle %@ -> bringup = %{BOOL}u"
+ "B16@?0@\"CADisplay\"8"
+ "B16@?0@\"FBSDisplayIdentity\"8"
+ "Common"
+ "DisplayResolution"
+ "Forcing bringup display"
+ "Forcing main display"
+ "PBADisplayResolver"
+ "PBAForceDisplaySelection"
+ "PreBoard HIDUILockedState"
+ "PreBoard updating digitizer mode"
+ "Requested sensor mode %{public}@ on service %{public}@ (uiLockEnabled %{BOOL}u)"
+ "Resolved display configuration: %@"
+ "T@\"<BSInvalidatable>\",&,N,V_digitizerSensorModeAssertion"
+ "T@\"BKSHIDUISensorService\",&,N,V_sensorService"
+ "T@\"BLSBacklight\",&,N,V_backlight"
+ "T@\"FBSDisplayConfiguration\",&,N,V_displayConfiguration"
+ "T@\"FBSDisplayConfiguration\",R,N,V_resolvedDisplayConfiguration"
+ "T@\"PBADisplayResolver\",&,N,V_displayResolver"
+ "T@\"UIWindow\",W,N,V_buttonEventDestinationWindow"
+ "TB,N,V_hidUILockedState"
+ "Timed out waiting for angle update"
+ "_applyHIDUILockedState:"
+ "_backlight"
+ "_buttonEventDestinationWindow"
+ "_defaultConfiguration"
+ "_digitizerSensorModeAssertion"
+ "_displayConfiguration"
+ "_displayConfigurationForAngle:"
+ "_displayResolver"
+ "_hidUILockedState"
+ "_resolvedDisplayConfiguration"
+ "_sensorService"
+ "_updateScreenBlankNotificationSuppressionForDisplayUUID:"
+ "_windowForSystemAppButtonEventsForScreen:"
+ "acquireTransactionForReason:"
+ "alwaysConnectedIdentities"
+ "angleDegrees"
+ "bs_filter:"
+ "bs_firstObjectPassingTest:"
+ "buildModeForReason:builder:"
+ "buttonEventDestinationWindow"
+ "com.apple.preboard.keyboardNamespace"
+ "com.apple.springboard.hasBlankedScreen"
+ "configurationForIdentity:"
+ "connectionType"
+ "digitizerSensorModeAssertion"
+ "displayConfiguration"
+ "displayResolver"
+ "displays"
+ "firstObject"
+ "hardwareIdentifier"
+ "hasBlankedScreen: notify_register_check failed with status %u"
+ "hidUILockedState"
+ "integerForKey:"
+ "isAngleValid"
+ "isAvailable"
+ "mainDisplay"
+ "referenceForCADisplay:"
+ "requestUISensorMode:"
+ "resolveWithTimeout:"
+ "resolvedDisplayConfiguration"
+ "sensorService"
+ "serviceForDisplayUUID:"
+ "setAllowsUnknownDisplays:"
+ "setAngleUpdateInterval:"
+ "setBacklight:"
+ "setButtonEventDestinationWindow:"
+ "setChangeSource:"
+ "setDigitizerEnabled:"
+ "setDigitizerSensorModeAssertion:"
+ "setDisplayResolver:"
+ "setDisplayState:"
+ "setHidUILockedState:"
+ "setKeyboardNamespaceIdentifier:"
+ "setMaxConcurrentOperationCount:"
+ "setPocketTouchesExpected:"
+ "setPreferredKeyboardNamespaceIdentifier:"
+ "setProximityDetectionMode:"
+ "setQualityOfService:"
+ "setScreenBlankNotificationSuppressedDisplayUUIDs:"
+ "setSensorService:"
+ "setTapToWakeEnabled:"
+ "setWithObject:"
+ "sharedApplication"
+ "sharedBacklightForDisplay:"
+ "startAngleUpdatesToQueue:handler:"
+ "stopAngleUpdates"
+ "ui_inputRehostingScene"
+ "ui_inputScenePairing"
+ "uniqueId"
+ "v16@?0@\"BKSMutableHIDUISensorMode\"8"
+ "v16@?0@\"CMAngle\"8"
- "_addKeyboardArbiterSceneToPresentationBinder"
- "_referenceBounds"
- "common"
- "mainScreen"
- "observeKeyboardSceneAvailability:"
- "usesInputSystemUI"
- "v16@?0@\"FBScene\"8"
```
