## SiriUICore

> `/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore`

```diff

-3600.9.2.0.0
-  __TEXT.__text: 0x2ac14
+3605.4.1.0.0
+  __TEXT.__text: 0x2ac9c
   __TEXT.__objc_methlist: 0x3448
-  __TEXT.__const: 0x7f172
-  __TEXT.__cstring: 0x87ea
-  __TEXT.__oslogstring: 0xd3d
+  __TEXT.__const: 0x68972
+  __TEXT.__cstring: 0x885b
+  __TEXT.__oslogstring: 0xd80
   __TEXT.__gcc_except_tab: 0x380
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__ustring: 0x14

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1151
+  Functions: 1152
   Symbols:   3467
-  CStrings:  374
+  CStrings:  377
 
Symbols:
+ _precalcSUICILNoise3DTextureASTC5x5
- _precalcSUICILNoise3DTexture
Functions:
~ +[SUICIntelligentLightLayer createNoiseTextureWithDevice:commandQueue:] : 416 -> 484
+ -[SUICIntelligentLightLayer _drawFrame:].cold.1
CStrings:
+ "!\"ASTC5x5 3D texture failed to allocate\""
+ "%s Failed to create compressed noise texture. Requires Apple3 GPU."
+ "+[SUICIntelligentLightLayer createNoiseTextureWithDevice:commandQueue:]"
```
