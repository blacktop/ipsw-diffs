## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

```diff

-479.3.0.0.0
-  __TEXT.__text: 0x4575c
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x3774
+479.5.0.0.0
+  __TEXT.__text: 0x45984
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x37a4
   __TEXT.__const: 0x3c2
   __TEXT.__gcc_except_tab: 0xba0
-  __TEXT.__cstring: 0x5812
+  __TEXT.__cstring: 0x5842
   __TEXT.__ustring: 0x1366
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0xc

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1090
+  __TEXT.__unwind_info: 0x1098
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x572
-  __TEXT.__objc_methname: 0x854b
+  __TEXT.__objc_methname: 0x85ff
   __TEXT.__objc_methtype: 0x115e
-  __TEXT.__objc_stubs: 0x7b00
+  __TEXT.__objc_stubs: 0x7b80
   __DATA_CONST.__got: 0x530
   __DATA_CONST.__const: 0x8d8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23d8
+  __DATA_CONST.__objc_selrefs: 0x23f8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x3c28
-  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__auth_got: 0x6a0
   __AUTH_CONST.__const: 0x608
-  __AUTH_CONST.__cfstring: 0x114a0
-  __AUTH_CONST.__objc_const: 0x49b0
+  __AUTH_CONST.__cfstring: 0x11500
+  __AUTH_CONST.__objc_const: 0x4a10
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xbb8
   __AUTH_CONST.__objc_arrayobj: 0x390

   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH.__objc_data: 0xdb8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2a8
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x2f0
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: F1D8229C-6A3E-3C1A-A505-8CB79932ABFA
-  Functions: 1294
-  Symbols:   4608
-  CStrings:  5285
+  UUID: 5221E699-504B-3517-A848-F4EAE7C1801A
+  Functions: 1298
+  Symbols:   4623
+  CStrings:  5298
 
Symbols:
+ -[TypistKeyboard setTapVectorAngle:]
+ -[TypistKeyboard setTapVectorDistance:]
+ -[TypistKeyboard tapVectorAngle]
+ -[TypistKeyboard tapVectorDistance]
+ _OBJC_IVAR_$_TypistKeyboard._tapVectorAngle
+ _OBJC_IVAR_$_TypistKeyboard._tapVectorDistance
+ ___sincos_stret
+ _objc_msgSend$setTapVectorAngle:
+ _objc_msgSend$setTapVectorDistance:
+ _objc_msgSend$tapVectorAngle
+ _objc_msgSend$tapVectorDistance
Functions:
~ -[TypistKeyboard setTapStyleNoise:] : 200 -> 228
~ -[TypistKeyboard _setKeyboardUserPreferences:] : 2096 -> 2208
~ -[TypistKeyboard setupKeyboardInfo:options:] : 5216 -> 5332
~ -[TypistKeyboard generateKeystrokeStream:] : 5860 -> 5988
+ -[TypistKeyboard setTapVectorDistance:]
+ -[TypistKeyboard setTapVectorAngle:]
- -[TypistKeyboard setCandidatebar:]
+ -[TypistKeyboard setCandidatebar:]
- -[TypistKeyboard setSwipeSigma:]
+ -[TypistKeyboard swipeSigma]
+ -[TypistKeyboard setSwipeConvexSigma:]
+ -[TypistKeyboard hardwareKeyboard]
~ -[TypistKeyboard .cxx_destruct] : 368 -> 392
CStrings:
+ "######## SPECIFIED KEYBOARD OPTIONS FOR %@\n%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%d;%@=%d;"
+ "T@\"NSNumber\",&,N,V_tapVectorAngle"
+ "T@\"NSNumber\",&,N,V_tapVectorDistance"
+ "_tapVectorAngle"
+ "_tapVectorDistance"
+ "setTapVectorAngle:"
+ "setTapVectorDistance:"
+ "tapNoiseVectorAngle"
+ "tapNoiseVectorDistance"
+ "tapVectorAngle"
+ "tapVectorDistance"
+ "vector"
- "######## SPECIFIED KEYBOARD OPTIONS FOR %@\n%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@"
- "?\f"

```
