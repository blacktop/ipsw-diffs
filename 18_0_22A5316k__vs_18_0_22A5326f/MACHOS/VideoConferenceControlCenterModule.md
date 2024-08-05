## VideoConferenceControlCenterModule

> `/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule`

```diff

-558.46.0.0.0
-  __TEXT.__text: 0x461c0
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__objc_stubs: 0x5d00
-  __TEXT.__objc_methlist: 0x3158
-  __TEXT.__const: 0xa28
-  __TEXT.__objc_methname: 0x8920
-  __TEXT.__cstring: 0x268d
-  __TEXT.__oslogstring: 0x23f8
+558.51.0.0.0
+  __TEXT.__text: 0x47518
+  __TEXT.__auth_stubs: 0x11d0
+  __TEXT.__objc_stubs: 0x5d40
+  __TEXT.__objc_methlist: 0x3194
+  __TEXT.__const: 0xa38
+  __TEXT.__objc_methname: 0x89db
+  __TEXT.__cstring: 0x26ad
+  __TEXT.__oslogstring: 0x2511
   __TEXT.__objc_classname: 0x7f2
   __TEXT.__objc_methtype: 0x19dc
   __TEXT.__gcc_except_tab: 0x3e4
   __TEXT.__constg_swiftt: 0x5e4
   __TEXT.__swift5_typeref: 0x478
   __TEXT.__swift5_reflstr: 0x61a
-  __TEXT.__swift5_fieldmd: 0x434
+  __TEXT.__swift5_fieldmd: 0x440
   __TEXT.__swift5_types: 0x40
-  __TEXT.__swift5_capture: 0xf4
+  __TEXT.__swift5_capture: 0xfc
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_proto: 0x3c
-  __TEXT.__unwind_info: 0x1350
+  __TEXT.__unwind_info: 0x13a0
   __TEXT.__eh_frame: 0xb8
-  __DATA_CONST.__auth_got: 0x8d8
-  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__auth_got: 0x8f8
+  __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA_CONST.__const: 0x10b0
-  __DATA_CONST.__cfstring: 0xe40
+  __DATA_CONST.__const: 0x10f0
+  __DATA_CONST.__cfstring: 0xe80
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0xd648
-  __DATA.__objc_selrefs: 0x1e48
-  __DATA.__objc_ivar: 0x4b0
-  __DATA.__objc_data: 0x13b8
-  __DATA.__data: 0x1000
-  __DATA.__bss: 0x988
+  __DATA.__objc_const: 0xd708
+  __DATA.__objc_selrefs: 0x1e78
+  __DATA.__objc_ivar: 0x4b4
+  __DATA.__objc_data: 0x13c8
+  __DATA.__data: 0x1010
+  __DATA.__bss: 0x998
   __DATA.__common: 0x2e0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftSpatial.dylib
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
-  Functions: 1752
-  Symbols:   442
-  CStrings:  2119
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1776
+  Symbols:   450
+  CStrings:  2135
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ " [ERROR] %!{(MISSING)public}s:%!d(MISSING) bundle id nil or zero length"
+ " [INFO] %!{(MISSING)public}s:%!d(MISSING) backgroundBlurAvailable=%!d(MISSING) centerStageAvailable=%!d(MISSING) StudioLightingAvailable=%!d(MISSING) reactionsAvailable=%!d(MISSING) gesturesAvailable=%!d(MISSING)"
+ " [INFO] %!{(MISSING)public}s:%!d(MISSING) currentCameraSupportsCenterStage=%!@(MISSING)"
+ "%!s(MISSING) captureFrameReceiverDidChange no videoView, skipping start"
+ "%!s(MISSING) setting %!s(MISSING) highlighted=%!{(MISSING)bool}d, isAlternateHighlight=%!{(MISSING)bool}d, isInteractionEnabled=%!{(MISSING)bool}d"
+ "-[VideoEffects updateSupportedWithBundleID:]"
+ "NO"
+ "TB,N,V_isSupported"
+ "YES"
+ "_TtC34VideoConferenceControlCenterModule28CaptureFrameReceiverObserver"
+ "_isSupported"
+ "allTargets"
+ "isInteractionEnabled"
+ "isSupported"
+ "keyPath"
+ "promptsForUserConfiguration"
+ "removeTarget:action:forControlEvents:"
+ "setBackgroundViewHighlighted(_:isAlternateHighlight:isInteractionEnabled:)"
+ "setIsSupported:"
+ "updateSupportedWithBundleID:"
- " [ERROR] %!{(MISSING)public}s:%!d(MISSING) bundle id nil"
- "%!s(MISSING) setting %!s(MISSING) highlighted=%!{(MISSING)bool}d, isAlternateHighlight=%!{(MISSING)bool}d, isSupported=%!{(MISSING)bool}d"
- "_TtC34VideoConferenceControlCenterModuleP33_3A0BDB1D8E4D3FB0CB422F516429011C28CaptureFrameReceiverObserver"
- "setBackgroundViewHighlighted(_:isAlternateHighlight:isSupported:)"

```
