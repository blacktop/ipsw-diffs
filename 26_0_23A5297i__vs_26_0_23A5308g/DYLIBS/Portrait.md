## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-490.0.0.0.0
-  __TEXT.__text: 0x9c4e0
+492.0.0.0.0
+  __TEXT.__text: 0x9c3e0
   __TEXT.__auth_stubs: 0x1390
   __TEXT.__delay_stubs: 0x2ec
   __TEXT.__delay_helper: 0x230
-  __TEXT.__objc_methlist: 0x980c
-  __TEXT.__const: 0x21260
+  __TEXT.__objc_methlist: 0x9834
+  __TEXT.__const: 0x21250
   __TEXT.__cstring: 0x6ed7
   __TEXT.__oslogstring: 0x47b0
-  __TEXT.__gcc_except_tab: 0x1804
+  __TEXT.__gcc_except_tab: 0x1818
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x20d0
+  __TEXT.__unwind_info: 0x20e8
   __TEXT.__objc_classname: 0x136b
-  __TEXT.__objc_methname: 0x1aaeb
-  __TEXT.__objc_methtype: 0x567c
+  __TEXT.__objc_methname: 0x1ab67
+  __TEXT.__objc_methtype: 0x570e
   __TEXT.__objc_stubs: 0xfa80
   __DATA_CONST.__got: 0x8f0
   __DATA_CONST.__const: 0x970

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5000
+  __DATA_CONST.__objc_selrefs: 0x5010
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4e8

   __AUTH_CONST.__auth_got: 0xa68
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x50e0
-  __AUTH_CONST.__objc_const: 0x1c9a0
+  __AUTH_CONST.__objc_const: 0x1c9c0
   __AUTH_CONST.__objc_intobj: 0xae0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x1b80
+  __AUTH.__objc_data: 0x1e50
   __AUTH.__data: 0x9e0
-  __DATA.__objc_ivar: 0x1748
+  __DATA.__objc_ivar: 0x174c
   __DATA.__data: 0x818
   __DATA.__bss: 0xe58
-  __DATA_DIRTY.__objc_data: 0x1b30
+  __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59234A06-B515-3968-A301-28988610BF99
-  Functions: 4035
-  Symbols:   14999
-  CStrings:  7573
+  UUID: 8D38E365-6EAB-3813-A08A-24B9DA966D34
+  Functions: 4036
+  Symbols:   14998
+  CStrings:  7577
 
Symbols:
+ +[PTEffectRelighting computeSmoothFaceRect:transform:weightHeadEye:eyeRadiusFactor:aspectRatio:]
+ -[PTCVMNetwork debugTexture]
+ -[PTEffectRelighting renderLightMask:lightMasks:smoothFaceRects:]
+ GCC_except_table14
+ _OBJC_IVAR_$_PTDisparityFilterDEMA_LKT._erodeMonocularDisparity
+ __OBJC_$_CLASS_METHODS_PTEffectRelighting
+ _objc_msgSend$computeSmoothFaceRect:transform:weightHeadEye:eyeRadiusFactor:aspectRatio:
+ _objc_msgSend$renderLightMask:lightMasks:smoothFaceRects:
- +[PTTexture createFromPixelbuffer:device:textureCache:metalYCBCRConversion:read:write:].cold.3
- +[PTTexture createFromPixelbuffer:device:textureCache:metalYCBCRConversion:read:write:].cold.4
- +[PTTexture createFromPixelbuffer:device:textureCache:metalYCBCRConversion:read:write:].cold.5
- -[PTEffectRelighting computeSmoothFaceRect:transform:]
- _objc_msgSend$computeSmoothFaceRect:transform:
- _objc_msgSend$setIntegratedStyleCoefficientsTextureArray:
CStrings:
+ "^{SmoothFaceRectData=ffff{?=[2]}[4{SmoothFaceRect=fffff}]}16@0:8"
+ "_erodeMonocularDisparity"
+ "computeSmoothFaceRect:transform:weightHeadEye:eyeRadiusFactor:aspectRatio:"
+ "debugTexture"
+ "renderLightMask:lightMasks:smoothFaceRects:"
+ "v40@0:8@16@24^{SmoothFaceRectData=ffff{?=[2]}[4{SmoothFaceRect=fffff}]}32"
+ "{SmoothFaceRectData=\"aspectRatioScale\"\"lightMaskExponent\"f\"preumbraBendFactor\"f\"lightMaskWidth\"f\"lightMaskFaceOffsetY\"f\"faceEyeWeight\"\"rotation\"{?=\"columns\"[2]}\"faces\"[4{SmoothFaceRect=\"faceCenter\"\"faceRadius\"f\"bodyPos\"\"bodySize\"\"leftEyeCenter\"\"leftEyeRadius\"f\"rightEyeCenter\"\"rightEyeRadius\"f\"preumbra\"f\"weight\"f}]}"
+ "{SmoothFaceRectData=ffff{?=[2]}[4{SmoothFaceRect=fffff}]}88@0:8@16{CGAffineTransform=dddddd}2472f80f84"
- "^{SmoothFaceRectData=fffff{?=[2]}[4{SmoothFaceRect=fffff}]}16@0:8"
- "computeSmoothFaceRect:transform:"
- "v72@0:8@16{CGAffineTransform=dddddd}24"
- "{SmoothFaceRectData=\"aspect\"f\"lightMaskExponent\"f\"preumbraBendFactor\"f\"lightMaskWidth\"f\"lightMaskFaceOffsetY\"f\"faceEyeWeight\"\"rotation\"{?=\"columns\"[2]}\"faces\"[4{SmoothFaceRect=\"faceCenter\"\"faceRadius\"f\"bodyPos\"\"bodySize\"\"leftEyeCenter\"\"leftEyeRadius\"f\"rightEyeCenter\"\"rightEyeRadius\"f\"preumbra\"f\"weight\"f}]}"

```
