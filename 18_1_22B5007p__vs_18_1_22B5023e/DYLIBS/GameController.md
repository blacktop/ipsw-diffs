## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-12.0.36.0.0
-  __TEXT.__text: 0xe95b4
+12.1.2.0.0
+  __TEXT.__text: 0xe8ea0
   __TEXT.__auth_stubs: 0x1850
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xc224
+  __TEXT.__objc_methlist: 0xc18c
   __TEXT.__const: 0x3324
   __TEXT.__cstring: 0x90f0
-  __TEXT.__gcc_except_tab: 0x4be8
-  __TEXT.__oslogstring: 0x98c9
+  __TEXT.__gcc_except_tab: 0x4c50
+  __TEXT.__oslogstring: 0x9866
   __TEXT.__dlopen_cstrs: 0x15a
   __TEXT.__swift5_typeref: 0x3be
   __TEXT.__swift5_reflstr: 0x17f

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x42d0
+  __TEXT.__unwind_info: 0x42bc
   __TEXT.__eh_frame: 0xc8
-  __TEXT.__objc_classname: 0x3d0b
-  __TEXT.__objc_methname: 0x17e30
-  __TEXT.__objc_methtype: 0x7518
-  __TEXT.__objc_stubs: 0xea80
+  __TEXT.__objc_classname: 0x3d26
+  __TEXT.__objc_methname: 0x17c94
+  __TEXT.__objc_methtype: 0x7531
+  __TEXT.__objc_stubs: 0xeb40
   __DATA_CONST.__got: 0x570
-  __DATA_CONST.__const: 0x2d00
-  __DATA_CONST.__objc_classlist: 0x830
+  __DATA_CONST.__const: 0x2d38
+  __DATA_CONST.__objc_classlist: 0x838
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x770
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3eba0
-  __DATA_CONST.__objc_selrefs: 0x4d50
+  __DATA_CONST.__objc_const: 0x3eb08
+  __DATA_CONST.__objc_selrefs: 0x4d18
   __DATA_CONST.__objc_protorefs: 0x480
-  __DATA_CONST.__objc_classrefs: 0x9a0
-  __DATA_CONST.__objc_superrefs: 0x7b8
+  __DATA_CONST.__objc_classrefs: 0x9a8
+  __DATA_CONST.__objc_superrefs: 0x7c0
   __DATA_CONST.__objc_arraydata: 0x770
-  __AUTH_CONST.__objc_const: 0x6960
+  __AUTH_CONST.__objc_const: 0x69f0
   __AUTH_CONST.__cfstring: 0xa520
-  __AUTH_CONST.__const: 0x1828
+  __AUTH_CONST.__const: 0x1868
   __AUTH_CONST.__objc_intobj: 0x1458
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__auth_ptr: 0x10

   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__auth_got: 0xc40
-  __AUTH.__objc_data: 0x45b0
+  __AUTH.__objc_data: 0x4600
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x15bc
+  __DATA.__objc_ivar: 0x15b0
   __DATA.__data: 0x5920
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1580
+  __DATA.__bss: 0x1590
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5973
-  Symbols:   7383
-  CStrings:  7941
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 5952
+  Symbols:   7368
+  CStrings:  7923
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _OBJC_CLASS_$_GCKeyboardAndMouseEmulatedController
- _OBJC_METACLASS_$_GCKeyboardAndMouseEmulatedController
CStrings:
+ "\x03D!1"
+ "@\"<GCKeyboardControllerWindowManager>\""
+ "@\"_GCGamepadEventImpl\""
+ "GCKeyboardControllerManager"
+ "_leftThumbstickValue"
+ "_rightThumbstickValue"
+ "_windowManager"
+ "ensureEmulatedControllerWithDevice:added:"
+ "initEmulatedControllerWithMapping:windowManager:"
+ "keyDown:"
+ "mouseDown:"
+ "mouseMoved"
+ "onKeyboardOrMouseConnectionStateChanged:"
+ "releasePointer"
+ "setEnablePointerCapture:"
- "\x02u"
- "\x04\x13"
- "TB,N,V_captureAwaitingMouseUp"
- "TB,N,V_mouseThumbstickEnabled"
- "TB,N,V_pointerHidden"
- "Ti,V_emulatedControllerMapping"
- "_captureAwaitingMouseUp"
- "_lastPointerLocation"
- "_mainWindowIsKey"
- "_mouseThumbstickEnabled"
- "_onqueue_ensureEmulatedControllerWithDevice:added:"
- "_pointerHidden"
- "_restorePointerLocation"
- "captureAwaitingMouseUp"
- "insertMappingForInput:withKey:withKeyboard:toDictionary:"
- "mouseThumbstickEnabled"
- "notifyButtonIfNeeded:pressed:onQueue:"
- "notifyElementChangedOnQueue:queue:"
- "pointerHidden"
- "setCaptureAwaitingMouseUp:"
- "setEmulatedControllerEnabled:"
- "setMouseThumbstickEnabled:"
- "setPointerHidden:"
- "v36@0:8@16B24@28"
- "v48@0:8q16@24@32@40"
- "windowDidBecomeKey %!@(MISSING)"
- "windowDidBecomeKey:"
- "windowDidEnterFullScreen %!@(MISSING)"
- "windowDidEnterFullScreen:"
- "windowDidExitFullScreen %!@(MISSING)"
- "windowDidExitFullScreen:"
- "windowDidResignKey %!@(MISSING)"
- "windowDidResignKey:"

```
