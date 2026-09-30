## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-492.40.6.0.0
-  __TEXT.__text: 0x9d3ec
-  __TEXT.__auth_stubs: 0x13d0
+492.60.4.0.1
+  __TEXT.__text: 0x9d4f0
+  __TEXT.__auth_stubs: 0x13e0
   __TEXT.__delay_stubs: 0x2ec
   __TEXT.__delay_helper: 0x230
-  __TEXT.__objc_methlist: 0x98dc
+  __TEXT.__objc_methlist: 0x98e4
   __TEXT.__const: 0x21260
   __TEXT.__cstring: 0x6f41
   __TEXT.__oslogstring: 0x4908
   __TEXT.__gcc_except_tab: 0x1844
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x2130
+  __TEXT.__unwind_info: 0x2138
   __TEXT.__objc_classname: 0x1390
-  __TEXT.__objc_methname: 0x1ae1f
-  __TEXT.__objc_methtype: 0x5797
-  __TEXT.__objc_stubs: 0xfc40
-  __DATA_CONST.__got: 0x920
+  __TEXT.__objc_methname: 0x1ae79
+  __TEXT.__objc_methtype: 0x57e2
+  __TEXT.__objc_stubs: 0xfc60
+  __DATA_CONST.__got: 0x928
   __DATA_CONST.__const: 0x970
   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5080
+  __DATA_CONST.__objc_selrefs: 0x5088
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x768
   __DATA_CONST.__vfx_script_tbl: 0x50
   __DATA_CONST.__vfx_script_tbx: 0x48
-  __AUTH_CONST.__auth_got: 0xa88
+  __AUTH_CONST.__auth_got: 0xa90
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x5180
-  __AUTH_CONST.__objc_const: 0x1cbf0
+  __AUTH_CONST.__objc_const: 0x1cbc0
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0x1e50
   __AUTH.__data: 0x9e0
-  __DATA.__objc_ivar: 0x1780
+  __DATA.__objc_ivar: 0x177c
   __DATA.__data: 0x818
   __DATA.__bss: 0xe5c
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DE5FAD2B-674D-3793-A6D2-B328D5E52A69
-  Functions: 4059
-  Symbols:   15087
-  CStrings:  7626
+  UUID: 4A34218A-4DBD-39EE-A16F-8348C9FDC3AD
+  Functions: 4060
+  Symbols:   15091
+  CStrings:  7628
 
Symbols:
+ +[PTEffectUtil applyDeadZoneOnValue:deadZoneFactor:valueRange:newValue:edgeEMACoefficient:]
+ +[PTEffectUtil applyStepFunctionOnValue:min:max:levels:]
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:enforceSRGB:]
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:enforceSRGB:].cold.1
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:enforceSRGB:].cold.2
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:enforceSRGB:].cold.3
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:enforceSRGB:].cold.4
+ _CGColorSpaceSupportsOutput
+ _kCIImageColorSpace
+ _objc_msgSend$readPixelBufferFromFile:pixelFormat:ciOptions:enforceSRGB:
- -[PTEffectRenderRequest ambientLightSensor]
- -[PTEffectRenderRequest setAmbientLightSensor:]
- -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:].cold.1
- -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:].cold.2
- -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:].cold.3
- -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:].cold.4
- _OBJC_IVAR_$_PTEffectRenderRequest._ambientLightSensor
CStrings:
+ "^{__CVBuffer=}40@0:8@16I24@28B36"
+ "applyDeadZoneOnValue:deadZoneFactor:valueRange:newValue:edgeEMACoefficient:"
+ "applyStepFunctionOnValue:min:max:levels:"
+ "f32@0:8f16f20f24i28"
+ "f40@0:8f16f2024f32f36"
+ "readPixelBufferFromFile:pixelFormat:ciOptions:enforceSRGB:"
- "Tf,V_ambientLightSensor"
- "_ambientLightSensor"
- "ambientLightSensor"
- "setAmbientLightSensor:"

```
