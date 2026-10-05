## SceneKit

> `/System/Library/Frameworks/SceneKit.framework/SceneKit`

```diff

-612.0.0.0.0
-  __TEXT.__text: 0x3884f0
+612.101.0.0.0
+  __TEXT.__text: 0x38877c
   __TEXT.__objc_methlist: 0x1785c
   __TEXT.__const: 0x26298
-  __TEXT.__oslogstring: 0x166fc
-  __TEXT.__cstring: 0x99c1f
-  __TEXT.__gcc_except_tab: 0x402c
+  __TEXT.__oslogstring: 0x1679c
+  __TEXT.__cstring: 0x99bc0
+  __TEXT.__gcc_except_tab: 0x4094
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x11e78
+  __TEXT.__unwind_info: 0x11e90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7a00
+  __DATA_CONST.__const: 0x79e0
   __DATA_CONST.__objc_classlist: 0x6c8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x338

   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1758
+  __AUTH_CONST.__auth_got: 0x1768
   __AUTH.__objc_data: 0x4290
   __AUTH.__data: 0x4d70
   __DATA.__objc_ivar: 0x1c5c
-  __DATA.__data: 0x293c
+  __DATA.__data: 0x2944
   __DATA.__common: 0x1d1
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 19668
-  Symbols:   24479
+  Functions: 19675
+  Symbols:   24481
   CStrings:  8037
 
Symbols:
+ _objc_exception_rethrow
+ _objc_terminate
Functions:
+ sub_24bf9eb30
+ sub_24bf9f550
~ _C3DSceneSourceCreateSceneAtIndex : 532 -> 680
~ _C3DColor4InitWithPropertyList : 180 -> 184
~ _C3DMeshElementEnumeratePrimitiveRanges : 132 -> 140
~ _C3DMeshElementGetPrimitiveCountByEvaluatingPrimitiveRanges : 92 -> 100
~ _C3DMeshElementEnumeratePrimitiveIndicesByEvaluatingPrimitiveRanges : 208 -> 216
~ _C3DIndicesContentEnumeratePrimitivesByEvaluatingPrimitiveRanges : 3592 -> 3640
~ _C3DCreateTangentsWithGeometryOptimized : 1800 -> 1852
+ _C3DVector4InitWithPropertyList
~ __C3DKeyframeControllerInitWithPropertyList : 5180 -> 5188
~ -[NSData(SCNExtensions) scn_indexedDataDecodingTrianglePairsWithBytesPerIndex:] : 472 -> 448
~ _C3DInitFloatArrayWithPropertyList : 4 -> 8
~ _C3DConvertToPlatformIndependentData : 1040 -> 1016
~ _C3DConvertFromPlatformIndependentData : 1128 -> 1136
~ _C3DBaseTypeGetCompoundType : 1004 -> 996
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_5
~ _C3DMeshGetBoundingBox : 452 -> 448
- _OUTLINED_FUNCTION_2
+ _C3DCreateTangentsWithGeometryOptimized.cold.8
+ _C3DBaseTypeGetCompoundType.cold.2
+ _C3DBaseTypeGetCompoundType.cold.14
- _C3DBaseTypeDescription.cold.2
~ _C3DAddBaseType.cold.5 : 68 -> 64
~ _C3DSubBaseType.cold.5 : 68 -> 64
~ _C3DJsonNamed.cold.2 : 72 -> 80
~ _C3DDeduceSphericalHarmonicsOrderFromDataLength.cold.2 : 108 -> 100
~ __C3DGenericSourceInitWithPropertyList.cold.3 : 68 -> 44
CStrings:
+ "Error: Cannot generate valid tangents with ill-formed normal source"
+ "Error: ERROR: GenericSource deserialize => we used to support only floats, but another type was encountered"
+ "Unreachable code: Compound type %@×%d is not supported"
+ "Unreachable code: Compound type C3DBaseType(%d)×%d is not supported"
+ "Welcome to SceneKit 612.101 (Sep 26 2026 05:57:37)"
- "(numberType == kCFNumberFloatType) || (numberType == kCFNumberFloat32Type)"
- "Assertion '%s' failed. Only one compound type per vector"
- "Assertion '%s' failed. We used to support only floats, but another type was encountered"
- "Welcome to SceneKit 612 (Sep 12 2026 06:32:54)"
- "componentCount == 1"
```
