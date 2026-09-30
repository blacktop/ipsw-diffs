## Eyedropper

> `/System/Library/PrivateFrameworks/Eyedropper.framework/Eyedropper`

```diff

-8074.0.0.0.0
-  __TEXT.__text: 0x5630
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0xc1c
+9067.0.0.0.0
+  __TEXT.__text: 0x5ffc
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_methlist: 0xc6c
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x155
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x210
+  __TEXT.__cstring: 0x180
+  __TEXT.__gcc_except_tab: 0x3c
+  __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x16f
-  __TEXT.__objc_methname: 0x2757
-  __TEXT.__objc_methtype: 0x144f
-  __TEXT.__objc_stubs: 0x1760
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x1c0
+  __TEXT.__objc_methname: 0x297a
+  __TEXT.__objc_methtype: 0x1524
+  __TEXT.__objc_stubs: 0x1920
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa90
+  __DATA_CONST.__objc_selrefs: 0xb18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x1098
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_const: 0x1118
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x90
+  __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x488
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B3C6A800-74B6-3C85-ADAB-48441ECA647D
-  Functions: 138
-  Symbols:   776
-  CStrings:  587
+  UUID: 20E75CE3-A33E-329B-B364-2BF4F9876C3E
+  Functions: 145
+  Symbols:   822
+  CStrings:  615
 
Symbols:
+ -[EDAppDelegate _updateDynamicRangeSamplingModesFromClientSettings]
+ -[EDAppDelegate beginShowingEyeDropper:settings:]
+ -[EDAppDelegate lensView:didSelectColorsBySamplingMode:]
+ -[EDAppDelegate lensViewDynamicRangeSamplingModes:]
+ -[EDLensView _colorAtCenterForHeadroomMode:]
+ GCC_except_table26
+ _CAToneMapModeAutomatic
+ _CFRelease
+ _CGColorCreate
+ _CGColorCreateWithContentHeadroom
+ _CGColorSpaceCopyFromIOSurface
+ _CGColorSpaceCreateLinearized
+ _CGColorTransformConvertColorComponents
+ _CGColorTransformCreate
+ _ColorUIColorWithColorSpace
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_IVAR_$_EDAppDelegate._activeDynamicRangeSamplingModes
+ _OBJC_IVAR_$_EDAppDelegate._settingsByConnection
+ _OBJC_IVAR_$_EDLensView._hoverColorsBySamplingMode
+ ___44-[EDLensView _colorAtCenterForHeadroomMode:]_block_invoke
+ ___49-[EDAppDelegate beginShowingEyeDropper:settings:]_block_invoke
+ ___49-[EDAppDelegate beginShowingEyeDropper:settings:]_block_invoke_2
+ ___52-[EDAppDelegate listener:shouldAcceptNewConnection:]_block_invoke_3
+ ___52-[EDAppDelegate listener:shouldAcceptNewConnection:]_block_invoke_4
+ ___56-[EDAppDelegate lensView:didSelectColorsBySamplingMode:]_block_invoke
+ ___block_descriptor_32_e54_v24?0"<EDServerClient>"8"_UIColorSamplerSettings"16l
+ ___block_descriptor_40_e8_32s_e54_v24?0"<EDServerClient>"8"_UIColorSamplerSettings"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e12_v24?0Q8^B16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.19
+ ___block_literal_global.78
+ ___block_literal_global.87
+ _kUIRenderingDestinationHDR
+ _objc_msgSend$_colorAtCenterForHeadroomMode:
+ _objc_msgSend$_updateDynamicRangeSamplingModesFromClientSettings
+ _objc_msgSend$addIndex:
+ _objc_msgSend$currentConnection
+ _objc_msgSend$enumerateIndexesUsingBlock:
+ _objc_msgSend$headroomMode
+ _objc_msgSend$indexSet
+ _objc_msgSend$initWithCGColor:
+ _objc_msgSend$lensView:didSelectColorsBySamplingMode:
+ _objc_msgSend$lensViewDynamicRangeSamplingModes:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$setToneMapMode:
+ _objc_msgSend$setWantsExtendedDynamicRangeContent:
+ _objc_msgSend$weakToStrongObjectsMapTable
+ _objc_retain_x23
- -[EDAppDelegate beginShowingEyeDropper:]
- -[EDAppDelegate lensView:didSelectColor:]
- ___40-[EDAppDelegate beginShowingEyeDropper:]_block_invoke
- ___40-[EDAppDelegate beginShowingEyeDropper:]_block_invoke_2
- ___41-[EDAppDelegate lensView:didSelectColor:]_block_invoke
- ___block_descriptor_32_e26_v16?0"<EDServerClient>"8l
- ___block_descriptor_40_e8_32s_e26_v16?0"<EDServerClient>"8ls32l8
- ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_literal_global.17
- ___block_literal_global.71
- ___block_literal_global.79
- _objc_msgSend$lensView:didSelectColor:
CStrings:
+ "@\"NSIndexSet\""
+ "@\"NSIndexSet\"24@0:8@\"EDLensView\"16"
+ "@\"NSMapTable\""
+ "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
+ "@24@0:8Q16"
+ "Q"
+ "_activeDynamicRangeSamplingModes"
+ "_colorAtCenterForHeadroomMode:"
+ "_hoverColorsBySamplingMode"
+ "_settingsByConnection"
+ "_updateDynamicRangeSamplingModesFromClientSettings"
+ "addIndex:"
+ "beginShowingEyeDropper:settings:"
+ "currentConnection"
+ "enumerateIndexesUsingBlock:"
+ "headroomMode"
+ "indexSet"
+ "initWithCGColor:"
+ "lensView:didSelectColorsBySamplingMode:"
+ "lensViewDynamicRangeSamplingModes:"
+ "numberWithUnsignedInteger:"
+ "objectEnumerator"
+ "preferredWindowingControlStyleForScene:"
+ "setToneMapMode:"
+ "setWantsExtendedDynamicRangeContent:"
+ "v24@?0@\"<EDServerClient>\"8@\"_UIColorSamplerSettings\"16"
+ "v24@?0Q8^B16"
+ "v32@0:8@\"EDLensView\"16@\"NSDictionary\"24"
+ "v32@0:8@\"NSString\"16@\"_UIColorSamplerSettings\"24"
+ "v32@0:8@\"UIWindowScene\"16@\"UIWindowSceneGeometry\"24"
+ "weakToStrongObjectsMapTable"
+ "windowScene:didUpdateEffectiveGeometry:"
+ "\xd1"
- "lensView:didSelectColor:"
- "v16@?0@\"<EDServerClient>\"8"
- "v32@0:8@\"EDLensView\"16@\"UIColor\"24"
- "{EDColor=\"r\"d\"g\"d\"b\"d}"
- "\xe1"

```
