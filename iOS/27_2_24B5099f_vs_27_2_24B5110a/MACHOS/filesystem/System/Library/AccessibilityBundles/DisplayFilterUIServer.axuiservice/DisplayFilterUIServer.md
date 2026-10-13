## DisplayFilterUIServer

> `System/Library/AccessibilityBundles/DisplayFilterUIServer.axuiservice/DisplayFilterUIServer`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3245.8.4.2.0
-  __TEXT.__text: 0x20d8
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x484
+3245.8.9.0.0
+  __TEXT.__text: 0x2960
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x4d4
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x172
+  __TEXT.__cstring: 0x284
   __TEXT.__oslogstring: 0xb
   __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0xf74
-  __TEXT.__objc_methtype: 0x4b6
-  __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__const: 0x110
-  __DATA_CONST.__cfstring: 0x1a0
+  __TEXT.__objc_methname: 0x1178
+  __TEXT.__objc_methtype: 0x4d7
+  __TEXT.__unwind_info: 0x138
+  __DATA_CONST.__const: 0x138
+  __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0xd0
-  __DATA.__objc_const: 0x640
-  __DATA.__objc_selrefs: 0x450
-  __DATA.__objc_ivar: 0x24
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0xe8
+  __DATA.__objc_const: 0x6a0
+  __DATA.__objc_selrefs: 0x4e8
+  __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 51
-  Symbols:   93
-  CStrings:  233
+  Functions: 57
+  Symbols:   108
+  CStrings:  265
 
Symbols:
+ _AXInvertColorsSettingsEventFeatureClassicInvert
+ _AXInvertColorsSettingsEventFeatureSmartInvert
+ _CFAbsoluteTimeGetCurrent
+ _CGPathGetBoundingBox
+ _CGRectIsNull
+ _CGRectNull
+ _NSStringFromCGRect
+ _NSStringFromClass
+ __AXSInvertColorsSetEnabled
+ _objc_opt_class
+ _objc_opt_new
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x4
- _objc_retain
CStrings:
+ "@\"NSMutableArray\""
+ "B"
+ "Mask fully opaque; applying invert colors change"
+ "System aperture frames %@ -> exclusion %@"
+ "T@\"NSMutableArray\",&,N,V__pendingInvertColorsChanges"
+ "TB,N,V__invertColorsChangeInFlight"
+ "Transition mask state: rootView=%@ maskView=%@ alpha=%.2f hidden=%d aperture=%@ maskPathBounds=%@ window=%@ windowHidden=%d windowAlpha=%.2f windowLevel=%f"
+ "__invertColorsChangeInFlight"
+ "__pendingInvertColorsChanges"
+ "_applyInvertColorsChangeIsSmart:value:source:"
+ "_invertColorsChangeInFlight"
+ "_logMaskState"
+ "_pendingInvertColorsChanges"
+ "_processNextInvertColorsChangeIfNeeded"
+ "alpha"
+ "firstObject"
+ "frame"
+ "isHidden"
+ "isSmartInvert"
+ "layoutIfNeeded"
+ "mask"
+ "path"
+ "registerInvertColorsSettingsEventWithFeature:state:source:"
+ "removeObjectAtIndex:"
+ "setClassicInvertColors:"
+ "setLastSmartInvertColorsEnablement:"
+ "set_invertColorsChangeInFlight:"
+ "set_pendingInvertColorsChanges:"
+ "source"
+ "v20@0:8B16"
+ "v32@0:8B16B20@24"
+ "value"
+ "window"
+ "windowLevel"
- "_fadeDisplayForSmartInvertStartWithDuration:maskOpaqueCompletion:"
- "v32@0:8d16@?24"
```
