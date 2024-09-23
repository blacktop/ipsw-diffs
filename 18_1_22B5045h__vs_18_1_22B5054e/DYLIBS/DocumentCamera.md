## DocumentCamera

> `/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`

```diff

-180.0.0.0.0
-  __TEXT.__text: 0x8b050
+181.0.0.0.0
+  __TEXT.__text: 0x8a46c
   __TEXT.__auth_stubs: 0x1480
-  __TEXT.__objc_methlist: 0x7f7c
+  __TEXT.__objc_methlist: 0x7d84
   __TEXT.__const: 0x640
-  __TEXT.__gcc_except_tab: 0x8c40
-  __TEXT.__cstring: 0x359f
+  __TEXT.__gcc_except_tab: 0x8bf4
+  __TEXT.__cstring: 0x35b8
   __TEXT.__oslogstring: 0x1b80
   __TEXT.__ustring: 0x3a0
   __TEXT.__dlopen_cstrs: 0x2f6
-  __TEXT.__unwind_info: 0x28b0
-  __TEXT.__objc_classname: 0x1067
-  __TEXT.__objc_methname: 0x1b088
-  __TEXT.__objc_methtype: 0x40db
-  __TEXT.__objc_stubs: 0x12ca0
-  __DATA_CONST.__got: 0x8f0
-  __DATA_CONST.__const: 0x1618
-  __DATA_CONST.__objc_classlist: 0x318
+  __TEXT.__unwind_info: 0x2890
+  __TEXT.__objc_classname: 0xffd
+  __TEXT.__objc_methname: 0x1ab1b
+  __TEXT.__objc_methtype: 0x4049
+  __TEXT.__objc_stubs: 0x12a00
+  __DATA_CONST.__got: 0x8d8
+  __DATA_CONST.__const: 0x1640
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x148
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5990
+  __DATA_CONST.__objc_selrefs: 0x5890
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x270
-  __DATA_CONST.__objc_arraydata: 0x178
+  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__auth_got: 0xa58
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x418
   __AUTH_CONST.__cfstring: 0x38c0
-  __AUTH_CONST.__objc_const: 0x15378
+  __AUTH_CONST.__objc_const: 0x15010
   __AUTH_CONST.__objc_doubleobj: 0x130
-  __AUTH_CONST.__objc_intobj: 0x330
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x2a0
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_ivar: 0xa00
-  __DATA.__data: 0xfa8
+  __DATA.__objc_ivar: 0x9d8
+  __DATA.__data: 0xf48
   __DATA.__bss: 0x238
-  __DATA_DIRTY.__objc_data: 0x1ef0
+  __DATA_DIRTY.__objc_data: 0x1e50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3396
-  Symbols:   4132
-  CStrings:  5505
+  Functions: 3357
+  Symbols:   4088
+  CStrings:  5446
 
Symbols:
+ _OBJC_CLASS_$_AVCaptureEventInteraction
- __UIApplicationVolumeDownButtonUpNotification
- __UIApplicationVolumeUpButtonDownNotification
- __UIApplicationVolumeUpButtonUpNotification
- _OBJC_METACLASS_$_UIGestureRecognizer
- _OBJC_CLASS_$_UIGestureRecognizer
- __UIApplicationVolumeDownButtonDownNotification
CStrings:
+ "_captureEventInteraction"
+ "setCaptureEventInteraction:"
+ "createCaptureEventInteractionIfNecessary"
+ "handlePhysicalButtonPressed"
+ "captureEventInteraction"
+ "handlePhysicalButtonPressCancelled"
+ "@\"AVCaptureEventInteraction\""
+ "T@\"AVCaptureEventInteraction\",&,N,V_captureEventInteraction"
+ "initWithEventHandler:"
+ "handleCaptureEventInteractionEvent:"
+ "handlePhysicalButtonReleased"
+ "v16@?0@\"AVCaptureEvent\"8"
+ "\xf0\x82r\x81T#Qg#\x13\x17\"\x13!\x11Ad\x1d\x17\x11"
+ "\xf0q6(\x15B5\x16q\xf0\x92\x11\x14\x16\xf0\xd1"
- "_volumeUpButtonState"
- "\xf0\x82r\x81T#Qg#\x13\x17\"\x13!\x11Ad\x1e\x17\x11"
- "Tq,N,V_activeButton"
- "handleVolumeButtonPress:"
- "T@\"<ICDocCamPhysicalCaptureNotifierDelegate>\",W,N,V_delegate"
- "_desiredButtons"
- "\xf0q6(\x15B5\x16q\xf0\x92\x11\x14\x16\xf0\xe1"
- "@\"ICDocCamPhysicalCaptureRecognizer\""
- "ICDocCamPhysicalCaptureNotifier"
- "setActiveButton:"
- "__volumeDownButtonState"
- "physicalCaptureNotifier"
- "physicalCaptureNotifierDidChangeState:"
- "_updateApplicationButtonStatus"
- "T@\"NSArray\",C,N,V_desiredButtons"
- "setPhysicalButtonType:"
- "_activeButton"
- "useGestureRecognizerForVolumeButtons"
- "_enabled"
- "isSuspended"
- "__volumeUpButtonState"
- "reset"
- "setWantsVolumeButtonEvents:"
- "pressesCancelled:withEvent:"
- "desiredButtons"
- "_setState:"
- "physicalCaptureRecognizer"
- "setSuspended:"
- "Tq,N,S_setVolumeDownButtonState:,V__volumeDownButtonState"
- "_setVolumeUpButtonState:"
- "isUserInteractionEnabled"
- "setPhysicalCaptureNotifier:"
- "_updateStateAndNotifyDelegateIfNeeded"
- "_physicalCaptureNotifier"
- "@\"ICDocCamPhysicalCaptureNotifier\""
- "pressesBegan:withEvent:"
- "setDesiredButtons:"
- "setWantsLockEvents:"
- "ignorePress:forEvent:"
- "createPhysicalCaptureRecognizerOrNotifierIfNecessary"
- "@32@0:8@16:24"
- "T@\"ICDocCamPhysicalCaptureRecognizer\",&,N,V_physicalCaptureRecognizer"
- "v24@0:8@\"ICDocCamPhysicalCaptureNotifier\"16"
- "Tq,N,S_setVolumeUpButtonState:,V__volumeUpButtonState"
- "_suspended"
- "_updateCaptureButtonNotifications"
- "setAllowedPressTypes:"
- "_physicalButtonType"
- "@\"<ICDocCamPhysicalCaptureNotifierDelegate>\""
- "physicalButtonType"
- "_handleVolumeUpButtonDownNotification:"
- "activeButton"
- "_setVolumeDownButtonState:"
- "_handleVolumeDownButtonDownNotification:"
- "pressesEnded:withEvent:"
- "_captureButtonForPhysicalButtonType:"
- "_physicalCaptureRecognizer"
- "handlePhysicalButtonReleased:"
- "T@\"ICDocCamPhysicalCaptureNotifier\",&,N,V_physicalCaptureNotifier"
- "Tq,N,S_setState:,V_state"
- "TB,N,GisEnabled,V_enabled"
- "setPhysicalCaptureRecognizer:"
- "_handleVolumeDownButtonUpNotification:"
- "suspended"
- "Tq,N,V_physicalButtonType"
- "handlePhysicalButtonPressed:"
- "ICDocCamPhysicalCaptureRecognizer"
- "_handleVolumeUpButtonUpNotification:"
- "_volumeDownButtonState"
- "enabled"
- "TB,N,GisSuspended,V_suspended"
- "_state"
- "ICDocCamPhysicalCaptureNotifierDelegate"

```
