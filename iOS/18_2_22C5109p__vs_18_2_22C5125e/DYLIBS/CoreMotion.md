## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-2953.0.19.0.0
-  __TEXT.__text: 0x340420
+2953.0.25.0.0
+  __TEXT.__text: 0x340e1c
   __TEXT.__auth_stubs: 0x2960
-  __TEXT.__objc_methlist: 0xb4fc
+  __TEXT.__objc_methlist: 0xb59c
   __TEXT.__const: 0xa1c8
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e

   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__cstring: 0x3e915
-  __TEXT.__oslogstring: 0x25a17
+  __TEXT.__cstring: 0x3ea11
+  __TEXT.__oslogstring: 0x25aae
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__gcc_except_tab: 0xaef8
-  __TEXT.__unwind_info: 0xaa00
+  __TEXT.__unwind_info: 0xaa20
   __TEXT.__eh_frame: 0x1d0
   __TEXT.__objc_classname: 0x189d
-  __TEXT.__objc_methname: 0x19017
-  __TEXT.__objc_methtype: 0x855d
+  __TEXT.__objc_methname: 0x192aa
+  __TEXT.__objc_methtype: 0x856f
   __TEXT.__objc_stubs: 0xcf60
   __DATA_CONST.__got: 0x788
   __DATA_CONST.__const: 0x36f8
   __DATA_CONST.__objc_classlist: 0x7e8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4bc8
+  __DATA_CONST.__objc_selrefs: 0x4c28
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x14c8
   __AUTH_CONST.__auth_ptr: 0xc0
   __AUTH_CONST.__const: 0x127a8
-  __AUTH_CONST.__cfstring: 0x11640
-  __AUTH_CONST.__objc_const: 0x1b988
+  __AUTH_CONST.__cfstring: 0x11680
+  __AUTH_CONST.__objc_const: 0x1bab8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0xaa0
   __AUTH.__data: 0x210
-  __DATA.__objc_ivar: 0x1550
+  __DATA.__objc_ivar: 0x1568
   __DATA.__data: 0xe58
   __DATA.__bss: 0x480
   __DATA.__common: 0x158

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11411
+  Functions: 11424
   Symbols:   1720
-  CStrings:  14729
+  CStrings:  14761
 
CStrings:
+ "%!@(MISSING), <version, %!l(MISSING)u, fetchType, %!l(MISSING)u, startTime, %!f(MISSING), endTime, %!f(MISSING), tables, %!@(MISSING)>"
+ "-[CLHidManager activateClientDevice:]_block_invoke"
+ "03:12:49"
+ "@60@0:8B16d20d28f36f40f44f48f52f56"
+ "Bad motion report input state %!l(MISSING)d, expected %!l(MISSING)u"
+ "Oct 27 2024"
+ "Tf,N,V_faceDownAngleDeg"
+ "Tf,N,V_faceUpAngleDeg"
+ "Tf,N,V_landscapeLeftAngleDeg"
+ "Tf,N,V_landscapeRightAngleDeg"
+ "Tf,N,V_portraitAngleDeg"
+ "Tf,N,V_portraitUpsideDownAngleDeg"
+ "[CLHidManager], HID report length %!l(MISSING)u exceeds %!z(MISSING)u byte maximum"
+ "[HistoricalFetch] Fetching cardio samples from: %!f(MISSING) to: %!f(MISSING). Received token: %!@(MISSING)"
+ "[HistoricalFetch] Fetching mobility samples from: %!f(MISSING) to: %!f(MISSING). Received token: %!@(MISSING)"
+ "_faceDownAngleDeg"
+ "_faceUpAngleDeg"
+ "_landscapeLeftAngleDeg"
+ "_landscapeRightAngleDeg"
+ "_portraitAngleDeg"
+ "_portraitUpsideDownAngleDeg"
+ "calculationTimestamp"
+ "dramMaxTimestamp"
+ "dramMinTimestamp"
+ "faceDownAngleDeg"
+ "faceUpAngleDeg"
+ "initWithIsStatic:timeInStaticState:timeInMovingState:portraitAngle:portraitUpsideDownAngle:landscapeLeftAngle:landscapeRightAngle:faceUpAngle:faceDownAngle:"
+ "isStatic,%!u(MISSING),timeInStaticState,%!f(MISSING),timeInMovingState,%!f(MISSING),p,%!f(MISSING),pud,%!f(MISSING),ll,%!f(MISSING),lr,%!f(MISSING),fu,%!f(MISSING),fd,%!f(MISSING)"
+ "kCMHistoricalFetchTokenCodingKeyEndTime"
+ "kCMHistoricalFetchTokenCodingKeyStartTime"
+ "landscapeLeftAngleDeg"
+ "landscapeRightAngleDeg"
+ "portraitAngleDeg"
+ "portraitUpsideDownAngleDeg"
+ "setFaceDownAngleDeg:"
+ "setFaceUpAngleDeg:"
+ "setLandscapeLeftAngleDeg:"
+ "setLandscapeRightAngleDeg:"
+ "setPortraitAngleDeg:"
+ "setPortraitUpsideDownAngleDeg:"
- "%!@(MISSING), <version, %!l(MISSING)u, fetchType, %!l(MISSING)u, tables, %!@(MISSING)>"
- "13:39:56"
- "@36@0:8B16d20d28"
- "Oct 16 2024"
- "[HistoricalFetch] Fetching cardio samples from: %!f(MISSING) to: %!f(MISSING)"
- "[HistoricalFetch] Fetching mobility samples from: %!f(MISSING) to: %!f(MISSING)"
- "initWithIsStatic:timeInStaticState:timeInMovingState:"
- "isStatic,%!u(MISSING),timeInStaticState,%!f(MISSING),timeInMovingState,%!f(MISSING)"

```
