## AccessibilitySettings

> `/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-3001.4.0.0.0
-  __TEXT.__text: 0x33e3c
-  __TEXT.__auth_stubs: 0x1040
+3003.1.0.0.0
+  __TEXT.__text: 0x33d64
+  __TEXT.__auth_stubs: 0x1030
   __TEXT.__objc_methlist: 0x2640
   __TEXT.__const: 0x3f4
   __TEXT.__oslogstring: 0x22a
-  __TEXT.__cstring: 0x42b5
+  __TEXT.__cstring: 0x4265
   __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__constg_swiftt: 0x318
   __TEXT.__swift5_typeref: 0x2ce

   __TEXT.__unwind_info: 0xc18
   __TEXT.__eh_frame: 0x410
   __TEXT.__objc_classname: 0xa27
-  __TEXT.__objc_methname: 0x5a11
+  __TEXT.__objc_methname: 0x59e2
   __TEXT.__objc_methtype: 0xa02
-  __TEXT.__objc_stubs: 0x4b20
-  __DATA_CONST.__got: 0x988
-  __DATA_CONST.__const: 0x758
+  __TEXT.__objc_stubs: 0x4ae0
+  __DATA_CONST.__got: 0x980
+  __DATA_CONST.__const: 0x750
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1aa8
+  __DATA_CONST.__objc_selrefs: 0x1aa0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__auth_got: 0x828
   __AUTH_CONST.__const: 0x518
-  __AUTH_CONST.__cfstring: 0x4740
+  __AUTH_CONST.__cfstring: 0x46c0
   __AUTH_CONST.__objc_const: 0x34b0
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x40

   __AUTH.__objc_data: 0x16e0
   __AUTH.__data: 0x298
   __DATA.__objc_ivar: 0x78
-  __DATA.__data: 0x6c8
+  __DATA.__data: 0x6b0
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1e0
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 51B7F8B9-E03B-318E-85F2-1E5C4CEA4309
-  Functions: 1002
-  Symbols:   3294
-  CStrings:  2290
+  UUID: 2630C982-EDE9-3D32-BB4E-042925F92761
+  Functions: 1001
+  Symbols:   3288
+  CStrings:  2281
 
Symbols:
+ -[WristFlickController _wristFlickSpeedFromSpecifierKey:]
+ _AXGetWristFlickSpeed
+ _AXSetWristFlickSpeed
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.369
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_AccessibilitySettings
+ _objc_msgSend$_wristFlickSpeedFromSpecifierKey:
- -[WristFlickController _wristFlickSpeedOptionFromSpecifierKey:]
- _AXCurrentFlickSpeedOption
- _AXIdentifierForFlickSpeed
- _AXSetFlickSpeedOption
- _AXSpeedForFlickSpeedOption
- _AXWristFlickSpeedDefault
- _AXWristFlickSpeedSlow
- _AXWristFlickSpeedSlowest
- _CFPreferencesGetAppBooleanValue
- ___block_literal_global.300
- ___block_literal_global.305
- ___block_literal_global.366
- _objc_msgSend$_wristFlickSpeedOptionFromSpecifierKey:
- _objc_msgSend$doubleForKey:keyExistsAndHasValidFormat:
- _objc_msgSend$removeObjectForKey:
CStrings:
+ "CLFlickGestureMaxGestureLengthSyncNotification"
+ "_wristFlickSpeedFromSpecifierKey:"
- "FlickMaxGestureLengthSec"
- "ShowFlickSpeedSettings"
- "WRIST_FLICK_SPEED_SLOWEST"
- "_wristFlickSpeedOptionFromSpecifierKey:"
- "com.apple.locationd"
- "doubleForKey:keyExistsAndHasValidFormat:"
- "wristFlickSpeedSlowest"

```
