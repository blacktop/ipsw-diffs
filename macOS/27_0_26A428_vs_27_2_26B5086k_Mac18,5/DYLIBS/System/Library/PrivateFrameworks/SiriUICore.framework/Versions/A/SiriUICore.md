## SiriUICore

> `/System/Library/PrivateFrameworks/SiriUICore.framework/Versions/A/SiriUICore`

```diff

-3600.9.2.0.0
-  __TEXT.__text: 0x18874
+3605.4.1.0.0
+  __TEXT.__text: 0x188fc
   __TEXT.__objc_methlist: 0x29f8
-  __TEXT.__const: 0x7ef72
-  __TEXT.__cstring: 0x14ab
-  __TEXT.__oslogstring: 0xa25
+  __TEXT.__const: 0x68772
+  __TEXT.__cstring: 0x151c
+  __TEXT.__oslogstring: 0xa68
   __TEXT.__gcc_except_tab: 0x164
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__ustring: 0x14

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 655
+  Functions: 656
   Symbols:   2027
-  CStrings:  254
+  CStrings:  257
 
Symbols:
+ _precalcSUICILNoise3DTextureASTC5x5
- _precalcSUICILNoise3DTexture
Functions:
~ +[SUICIntelligentLightLayer createNoiseTextureWithDevice:commandQueue:] : 448 -> 516
+ -[SUICIntelligentLightLayer _drawFrame:].cold.1
CStrings:
+ "!\"ASTC5x5 3D texture failed to allocate\""
+ "%s Failed to create compressed noise texture. Requires Apple3 GPU."
+ "+[SUICIntelligentLightLayer createNoiseTextureWithDevice:commandQueue:]"
```
