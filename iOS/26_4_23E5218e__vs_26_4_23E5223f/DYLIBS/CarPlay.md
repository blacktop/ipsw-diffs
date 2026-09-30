## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-515.14.1.0.0
-  __TEXT.__text: 0x68be0
+515.16.1.2.0
+  __TEXT.__text: 0x68ffc
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x89a0
-  __TEXT.__const: 0x532
-  __TEXT.__cstring: 0x4ee6
-  __TEXT.__oslogstring: 0x2dab
+  __TEXT.__objc_methlist: 0x89c8
+  __TEXT.__const: 0x562
+  __TEXT.__cstring: 0x4f26
+  __TEXT.__oslogstring: 0x2e7b
   __TEXT.__gcc_except_tab: 0x968
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_typeref: 0x12f
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0xc4
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x14
+  __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x1f30
+  __TEXT.__unwind_info: 0x1f38
   __TEXT.__objc_classname: 0x127b
-  __TEXT.__objc_methname: 0x11f8b
+  __TEXT.__objc_methname: 0x11fcb
   __TEXT.__objc_methtype: 0x2d49
-  __TEXT.__objc_stubs: 0xaf20
+  __TEXT.__objc_stubs: 0xaf60
   __DATA_CONST.__got: 0x7f0
-  __DATA_CONST.__const: 0x1df0
+  __DATA_CONST.__const: 0x1e00
   __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bd8
+  __DATA_CONST.__objc_selrefs: 0x3bf8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x2e8
   __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0xae8
-  __AUTH_CONST.__cfstring: 0x4be0
-  __AUTH_CONST.__objc_const: 0x1ec48
+  __AUTH_CONST.__cfstring: 0x4c00
+  __AUTH_CONST.__objc_const: 0x1ec78
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x1ce0
   __AUTH.__data: 0x230
-  __DATA.__objc_ivar: 0x920
+  __DATA.__objc_ivar: 0x924
   __DATA.__data: 0x1fa0
-  __DATA.__bss: 0x4d0
+  __DATA.__bss: 0x550
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 556EE648-153E-308E-95F2-AB48493D7144
-  Functions: 3013
-  Symbols:   11225
-  CStrings:  5035
+  UUID: 6277ED61-C47B-3829-ACEA-CC562025153C
+  Functions: 3019
+  Symbols:   11250
+  CStrings:  5045
 
Symbols:
+ -[CPNavigationManager routeChangedWithReason:routeInfo:].cold.1
+ -[CPNavigationManager stopNavigation]
+ -[CPVoiceControlTemplate backgroundImage]
+ -[CPVoiceControlTemplate setBackgroundImage:]
+ GCC_except_table96
+ _$sSQ2eeoiySbx_xtFZTq
+ _$sSQMp
+ _$sSo13CAFRouteStateVSQSCMc
+ _$sSo13CAFRouteStateVSQSCMcMK
+ _$sSo13CAFRouteStateVSQSCSQ2eeoiySbx_xtFZTW
+ _$sSo21CPVehicleStateManagerC7CarPlayE013resetGuidanceB0yyFTo
+ _OBJC_IVAR_$_CPVoiceControlTemplate._backgroundImage
+ _OUTLINED_FUNCTION_17
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_CarPlay
+ _objc_msgSend$backgroundImage
+ _objc_msgSend$resetGuidanceState
+ _objc_msgSend$stopNavigation
- GCC_except_table95
- _objc_msgSend$resetRouteGuidance
CStrings:
+ "%s rerouting and guidance state is not active or loading, not sending guidance state update"
+ "T@\"UIImage\",&,N,V_backgroundImage"
+ "_backgroundImage"
+ "backgroundImage"
+ "kCPVoiceControlBackgroundImageKey"
+ "resetGuidanceState"
+ "routeChangedWithReason: resuming reroute request"
+ "routeChangedWithReason: startRerouting not called, fixing on behalf of calling app"
+ "send(guidanceState:)"
+ "setBackgroundImage:"
+ "stopNavigation"
- "("
- "startNavigation: route reset"

```
