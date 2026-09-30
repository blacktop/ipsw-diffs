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
- __UIApplicationVolumeDownButtonDownNotification
- _OBJC_CLASS_$_UIGestureRecognizer
- _OBJC_METACLASS_$_UIGestureRecognizer
- __UIApplicationVolumeUpButtonUpNotification
- __UIApplicationVolumeDownButtonUpNotification
- __UIApplicationVolumeUpButtonDownNotification
CStrings:
+ "handlePhysicalButtonPressed"
+ "\xf0\x82r\x81T#Qg#\x13\x17\"\x13!\x11Ad\x1d\x17\x11"
+ "handlePhysicalButtonReleased"
+ "@\"AVCaptureEventInteraction\""
+ "initWithEventHandler:"
+ "handlePhysicalButtonPressCancelled"
+ "captureEventInteraction"
+ "\xf0q6(\x15B5\x16q\xf0\x92\x11\x14\x16\xf0\xd1"
+ "setCaptureEventInteraction:"
+ "createCaptureEventInteractionIfNecessary"
+ "T@\"AVCaptureEventInteraction\",&,N,V_captureEventInteraction"
+ "_captureEventInteraction"
+ "handleCaptureEventInteractionEvent:"
+ "v16@?0@\"AVCaptureEvent\"8"
- "physicalCaptureNotifierDidChangeState:"
- "_updateCaptureButtonNotifications"
- "_setState:"
- "Tq,N,S_setVolumeDownButtonState:,V__volumeDownButtonState"
- "T@\"ICDocCamPhysicalCaptureNotifier\",&,N,V_physicalCaptureNotifier"
- "isSuspended"
- "setWantsVolumeButtonEvents:"
- "_setVolumeUpButtonState:"
- "handleVolumeButtonPress:"
- "physicalCaptureRecognizer"
- "_captureButtonForPhysicalButtonType:"
- "_updateApplicationButtonStatus"
- "handlePhysicalButtonPressed:"
- "_handleVolumeDownButtonUpNotification:"
- "_physicalCaptureNotifier"
- "_volumeUpButtonState"
- "ICDocCamPhysicalCaptureRecognizer"
- "enabled"
- "physicalCaptureNotifier"
- "isUserInteractionEnabled"
- "pressesBegan:withEvent:"
- "__volumeUpButtonState"
- "reset"
- "Tq,N,S_setVolumeUpButtonState:,V__volumeUpButtonState"
- "_handleVolumeUpButtonUpNotification:"
- "physicalButtonType"
- "setPhysicalCaptureRecognizer:"
- "TB,N,GisEnabled,V_enabled"
- "_physicalCaptureRecognizer"
- "suspended"
- "setAllowedPressTypes:"
- "desiredButtons"
- "__volumeDownButtonState"
- "@\"ICDocCamPhysicalCaptureRecognizer\""
- "_physicalButtonType"
- "setSuspended:"
- "Tq,N,V_activeButton"
- "_state"
- "_handleVolumeDownButtonDownNotification:"
- "@\"ICDocCamPhysicalCaptureNotifier\""
- "setPhysicalCaptureNotifier:"
- "setPhysicalButtonType:"
- "pressesEnded:withEvent:"
- "\xf0q6(\x15B5\x16q\xf0\x92\x11\x14\x16\xf0\xe1"
- "handlePhysicalButtonReleased:"
- "@\"<ICDocCamPhysicalCaptureNotifierDelegate>\""
- "ICDocCamPhysicalCaptureNotifierDelegate"
- "_desiredButtons"
- "createPhysicalCaptureRecognizerOrNotifierIfNecessary"
- "T@\"ICDocCamPhysicalCaptureRecognizer\",&,N,V_physicalCaptureRecognizer"
- "_setVolumeDownButtonState:"
- "_handleVolumeUpButtonDownNotification:"
- "@32@0:8@16:24"
- "Tq,N,V_physicalButtonType"
- "Tq,N,S_setState:,V_state"
- "ignorePress:forEvent:"
- "_activeButton"
- "setDesiredButtons:"
- "v24@0:8@\"ICDocCamPhysicalCaptureNotifier\"16"
- "T@\"NSArray\",C,N,V_desiredButtons"
- "setActiveButton:"
- "TB,N,GisSuspended,V_suspended"
- "\xf0\x82r\x81T#Qg#\x13\x17\"\x13!\x11Ad\x1e\x17\x11"
- "T@\"<ICDocCamPhysicalCaptureNotifierDelegate>\",W,N,V_delegate"
- "pressesCancelled:withEvent:"
- "activeButton"
- "_updateStateAndNotifyDelegateIfNeeded"
- "ICDocCamPhysicalCaptureNotifier"
- "_volumeDownButtonState"
- "useGestureRecognizerForVolumeButtons"
- "_enabled"
- "_suspended"
- "setWantsLockEvents:"

```
