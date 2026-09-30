## NanoNetAppsUI

> `/System/Library/PrivateFrameworks/NanoNetAppsUI.framework/NanoNetAppsUI`

```diff

 8.0.0.0.0
-  __TEXT.__text: 0x8a14
-  __TEXT.__auth_stubs: 0x540
+  __TEXT.__text: 0x8f6c
+  __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x594
   __TEXT.__const: 0x3a6
   __TEXT.__cstring: 0x9e

   __TEXT.__swift5_reflstr: 0x7
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x228
+  __TEXT.__unwind_info: 0x230
   __TEXT.__objc_classname: 0x10d
   __TEXT.__objc_methname: 0xfcd
   __TEXT.__objc_methtype: 0x35c
-  __TEXT.__objc_stubs: 0xcc0
+  __TEXT.__objc_stubs: 0xce0
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x450
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x888
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0xf08

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 962CB6B7-106A-3B1F-89C0-55DA3041AD1A
+  UUID: 6E53A115-CE06-32C8-B3A6-4F7B7D68F9C1
   Functions: 166
-  Symbols:   676
+  Symbols:   670
   CStrings:  297
 
Symbols:
+ _objc_msgSend$sharedPalette
+ _objc_retain_x24
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_NanoNetAppsUI
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x3
Functions:
~ _SGInterpolateBetweenBezierPaths : 2132 -> 2140
~ _SGScreenRadiusAtAngleWithInset : 552 -> 548
~ -[UIView(SGGeometryUtilities) SG_setBoundsAndPositionFromFrame:] : 152 -> 156
~ +[SGSiderealData _geoLocationForLocation:] : 76 -> 80
~ -[SGSiderealData initWithStartOfDay:location:useXR:] : 504 -> 496
~ -[SGSiderealData gradientWithSunsetFilterForDayProgress:] : 456 -> 496
~ -[SGColorPalette getSolarColorsForLocation:atDate:] : 196 -> 200
~ +[NNASoftNTKGossamerColorPaletteWrapper sharedPalette] : 68 -> 84
~ -[SGColorCurveElement initWithColor:fraction:] : 192 -> 196
~ -[SGColorCurveElement setColor:] : 12 -> 64
~ -[SGColorCurveElement setTimingFunction:] : 12 -> 64
~ -[SGColorCurve initWithColorCurveElements:] : 132 -> 136
~ ___43-[SGColorCurve initWithColorCurveElements:]_block_invoke : 140 -> 136
~ -[SGColorCurve colorForFraction:] : 572 -> 628
~ _SGBuildPathElement : 180 -> 188
~ +[SGSiderealColorManager sharedInstance] : 68 -> 84
~ -[SGSiderealColorManager _init] : 104 -> 108
~ -[SGSiderealColorManager _createElementsFromDict:] : 640 -> 696
~ -[SGSiderealColorManager dayGradientCurveP3] : 1188 -> 1220
~ -[SGSiderealColorManager dialBackgroundColorCurve] : 1468 -> 1568
~ __elementWithColorAtAltitude : 144 -> 148
~ -[SGSiderealColorManager dayGradientColorCurves] : 4616 -> 4920
~ -[SGSiderealColorManager civilTwilightColorCurve] : 1536 -> 1640
~ -[SGSiderealColorManager nauticalTwilightColorCurve] : 1536 -> 1640
~ -[SGSiderealColorManager astronomicalTwilightColorCurve] : 1508 -> 1612
~ -[SGSiderealColorManager innerComplicationColorCurve] : 1564 -> 1672
~ -[SGSiderealColorManager outerComplicationColorCurve] : 1544 -> 1652
~ -[SGSiderealColorManager dayDiskBloomColorCurve] : 728 -> 776
~ -[SGCubicColorCurve initWithCubicColorCurveElements:] : 440 -> 448
~ ___53-[SGCubicColorCurve initWithCubicColorCurveElements:]_block_invoke : 156 -> 164
~ -[SGCubicColorCurve initWithColorCurveElements:] : 456 -> 468
~ ___48-[SGCubicColorCurve initWithColorCurveElements:]_block_invoke : 156 -> 164
~ +[SGCubicSplineMatrixCache sharedInstance] : 68 -> 84
~ -[SGCubicSplineMatrixCache splineMatrixWithDimension:cache:matrixGenerator:] : 252 -> 244
~ ___76-[SGCubicSplineMatrixCache splineMatrixWithDimension:cache:matrixGenerator:]_block_invoke : 328 -> 344
~ -[SGCubicSpline initWithNumberOfControlPoints:isClosed:] : 188 -> 192
~ _SGStartOfDayForDate : 124 -> 132
~ _SGStartOfNextDayForDate : 160 -> 164
~ _SGPercentageOfDayDoneForDateWithStartAndEnd : 168 -> 160
~ _SGCircleSectorPath : 168 -> 172
~ sub_25fc24ea0 -> sub_2669bb3d0 : 548 -> 516

```
