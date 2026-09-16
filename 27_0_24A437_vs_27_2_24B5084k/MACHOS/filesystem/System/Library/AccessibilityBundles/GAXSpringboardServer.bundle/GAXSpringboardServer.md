## GAXSpringboardServer

> `/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1064.0.0.0.0
-  __TEXT.__text: 0x1577c
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_stubs: 0x2f00
+1067.3.0.0.0
+  __TEXT.__text: 0x15af4
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_stubs: 0x2f60
   __TEXT.__objc_methlist: 0x1edc
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x46c
-  __TEXT.__cstring: 0x5055
-  __TEXT.__objc_methname: 0x5938
-  __TEXT.__oslogstring: 0x1ac0
+  __TEXT.__gcc_except_tab: 0x464
+  __TEXT.__cstring: 0x50c2
+  __TEXT.__objc_methname: 0x599e
+  __TEXT.__oslogstring: 0x1ad7
   __TEXT.__objc_classname: 0xcff
-  __TEXT.__objc_methtype: 0xfbd
-  __TEXT.__unwind_info: 0x818
-  __DATA_CONST.__const: 0x1228
-  __DATA_CONST.__cfstring: 0x4ca0
+  __TEXT.__objc_methtype: 0x1000
+  __TEXT.__unwind_info: 0x820
+  __DATA_CONST.__const: 0x1238
+  __DATA_CONST.__cfstring: 0x4ce0
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA_CONST.__auth_got: 0x370
-  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__got: 0x260
   __DATA.__objc_const: 0x3d00
-  __DATA.__objc_selrefs: 0x14d0
+  __DATA.__objc_selrefs: 0x14e8
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x1b30
   __DATA.__data: 0x188

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 547
-  Symbols:   545
-  CStrings:  1591
+  Functions: 552
+  Symbols:   557
+  CStrings:  1596
 
Symbols:
+ _CACornerRadiiEqualToRadii
+ _CACornerRadiiZero
+ _GAXCornerRadiiFromRectCornerRadii
+ _GAXDisplayCornerRadiiForWindow
+ _GAXFixedSpaceCornerRadiiFromInterfaceCornerRadii
+ _GAXIPCPayloadKeyHostedApplicationCornerRadii
+ _GAXRectCornerRadiiFromCornerRadii
+ _GAXUIMessageKeyHostedApplicationCornerRadii
+ _UIRectCornerRadiiFromString
+ __UITraitCollectionDisplayCornerRadiusUnspecified
+ _deserializeGAXBackboardState
+ _kCACornerCurveContinuous
+ _objc_retain_x28
- _objc_retain_x27
CStrings:
+ "-[AXSpringBoardServer(GAXAdditions) gaxUpdateStateOfHostedApplicationWithIdentifier:scaleFactorNumber:centerStringRepresentation:cornerRadiiStringRepresentation:animationDurationNumber:]"
+ "GAXIPCPayloadKeyHostedApplicationCornerRadii"
+ "_handleUpdateHostedApplicationState: app=%{public}@ scaleFactor=%.3f center={%.1f,%.1f} cornerRadii=%{public}@ duration=%.2f"
+ "_updateStateOfHostedApplicationWithIdentifier:scaleFactor:center:cornerRadii:animationDuration:"
+ "effectiveRadiusForCorner:"
+ "gaxUpdateStateOfHostedApplicationWithIdentifier:scaleFactorNumber:centerStringRepresentation:cornerRadiiStringRepresentation:animationDurationNumber:"
+ "hosted application corner radii"
+ "setCornerCurve:"
+ "setCornerRadii:"
+ "v120@0:8@16d24{CGPoint=dd}32{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}}48d112"
+ "v56@0:8@16@24@32@40@48"
- "-[AXSpringBoardServer(GAXAdditions) gaxUpdateStateOfHostedApplicationWithIdentifier:scaleFactorNumber:centerStringRepresentation:animationDurationNumber:]"
- "_handleUpdateHostedApplicationState: app=%{public}@ scaleFactor=%.3f center={%.1f,%.1f} duration=%.2f"
- "_updateStateOfHostedApplicationWithIdentifier:scaleFactor:center:animationDuration:"
- "gaxUpdateStateOfHostedApplicationWithIdentifier:scaleFactorNumber:centerStringRepresentation:animationDurationNumber:"
- "v48@0:8@16@24@32@40"
- "v56@0:8@16d24{CGPoint=dd}32d48"
```
