## CinematicFraming

> `/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming`

```diff

-655.0.0.122.4
-  __TEXT.__text: 0x30de4
+659.0.0.0.4
+  __TEXT.__text: 0x30ea0
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x2424
-  __TEXT.__const: 0x660
+  __TEXT.__objc_methlist: 0x243c
+  __TEXT.__const: 0x680
   __TEXT.__gcc_except_tab: 0x122c
-  __TEXT.__oslogstring: 0x5756
+  __TEXT.__oslogstring: 0x5762
   __TEXT.__cstring: 0x323f
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x990
+  __TEXT.__unwind_info: 0x998
   __TEXT.__objc_classname: 0x2df
-  __TEXT.__objc_methname: 0x7868
+  __TEXT.__objc_methname: 0x7893
   __TEXT.__objc_methtype: 0x21d0
-  __TEXT.__objc_stubs: 0x4360
+  __TEXT.__objc_stubs: 0x43a0
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1680
+  __DATA_CONST.__objc_selrefs: 0x1690
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x478

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1271E2D4-A8A6-3123-9814-9C953632D777
-  Functions: 847
-  Symbols:   3145
-  CStrings:  2259
+  UUID: F56191B0-8FCF-3C99-BAC7-E4C75CCFDC94
+  Functions: 849
+  Symbols:   3151
+  CStrings:  2261
 
Symbols:
+ -[DeskCamRenderingSession _setPitchNominalValue]
+ -[DeskCamRenderingSession _setRollNominalValue]
+ _objc_msgSend$_setPitchNominalValue
+ _objc_msgSend$_setRollNominalValue
CStrings:
+ "<<<< DeskCamRenderingSession >>>> %s: No roll and pitch data available."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>init] Configuration: Is front facing camera = %d. Camera orientation = %d. device type = %d"
+ "_setPitchNominalValue"
+ "_setRollNominalValue"
- "<<<< DeskCamRenderingSession >>>> %s: No valid gravity vector available yet."
- "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>init] Configuration: Is front facing camera = %d. Camera orientation = %d."

```
