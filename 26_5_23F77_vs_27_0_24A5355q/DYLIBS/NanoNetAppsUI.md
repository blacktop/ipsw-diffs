## NanoNetAppsUI

> `/System/Library/PrivateFrameworks/NanoNetAppsUI.framework/NanoNetAppsUI`

```diff

 8.0.0.0.0
-  __TEXT.__text: 0x8f6c
-  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__text: 0x8a28
   __TEXT.__objc_methlist: 0x594
   __TEXT.__const: 0x3a6
-  __TEXT.__cstring: 0x9e
+  __TEXT.__cstring: 0xb5
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x10
   __TEXT.__swift5_reflstr: 0x7
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__objc_classname: 0x10d
-  __TEXT.__objc_methname: 0xfcd
-  __TEXT.__objc_methtype: 0x35c
-  __TEXT.__objc_stubs: 0xce0
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x138
+  __TEXT.__unwind_info: 0x228
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x450
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x888
-  __AUTH_CONST.__auth_got: 0x278
+  __DATA_CONST.__got: 0xe8
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0xf08
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0xfc0
   __AUTH_CONST.__objc_arrayobj: 0x888
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0xd8
   __DATA.__data: 0x10

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 92B46991-624B-3290-8DD5-83547B366FAD
+  UUID: EDE945F5-0436-319A-8F9E-9049ABDE4D40
   Functions: 166
-  Symbols:   670
-  CStrings:  297
+  Symbols:   673
+  CStrings:  12
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x3
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_NanoNetAppsUI
- _objc_retain_x24
Functions:
~ _SGSplineVector_print : 152 -> 156
~ _SGSplineMatrix_print : 168 -> 172
~ _SGSplineMatrix_times_SGSplineVector_float : 112 -> 120
~ _SGInterpolateBetweenBezierPaths : 2140 -> 2116
~ -[UIView(SGGeometryUtilities) SG_setBoundsAndPositionFromFrame:] : 156 -> 152
~ +[SGSiderealData _geoLocationForLocation:] : 80 -> 76
~ -[SGSiderealData initWithStartOfDay:location:useXR:] : 496 -> 504
~ -[SGSiderealData gradientWithSunsetFilterForDayProgress:] : 496 -> 456
~ -[SGColorPalette getSolarColorsForLocation:atDate:] : 200 -> 196
~ +[NNASoftNTKGossamerColorPaletteWrapper sharedPalette] : 84 -> 68
~ -[SGColorCurveElement initWithColor:fraction:] : 196 -> 192
~ -[SGColorCurveElement setColor:] : 64 -> 12
~ -[SGColorCurveElement setTimingFunction:] : 64 -> 12
~ -[SGColorCurve initWithColorCurveElements:] : 136 -> 132
~ ___43-[SGColorCurve initWithColorCurveElements:]_block_invoke : 136 -> 140
~ -[SGColorCurve colorForFraction:] : 628 -> 572
~ _SGBuildPathElement : 188 -> 180
~ +[SGSiderealColorManager sharedInstance] : 84 -> 68
~ -[SGSiderealColorManager _init] : 108 -> 104
~ -[SGSiderealColorManager _notifyHandlers] : 244 -> 248
~ -[SGSiderealColorManager _createElementsFromDict:] : 696 -> 640
~ -[SGSiderealColorManager dayGradientCurveP3] : 1220 -> 1188
~ -[SGSiderealColorManager dialBackgroundColorCurve] : 1568 -> 1464
~ __elementWithColorAtAltitude : 148 -> 144
~ -[SGSiderealColorManager dayGradientColorCurves] : 4920 -> 4612
~ -[SGSiderealColorManager civilTwilightColorCurve] : 1640 -> 1532
~ -[SGSiderealColorManager nauticalTwilightColorCurve] : 1640 -> 1532
~ -[SGSiderealColorManager astronomicalTwilightColorCurve] : 1612 -> 1504
~ -[SGSiderealColorManager innerComplicationColorCurve] : 1672 -> 1560
~ -[SGSiderealColorManager outerComplicationColorCurve] : 1652 -> 1540
~ -[SGSiderealColorManager dayDiskBloomColorCurve] : 776 -> 724
~ -[SGCubicColorCurve initWithCubicColorCurveElements:] : 448 -> 468
~ ___53-[SGCubicColorCurve initWithCubicColorCurveElements:]_block_invoke : 164 -> 156
~ -[SGCubicColorCurve initWithColorCurveElements:] : 468 -> 484
~ ___48-[SGCubicColorCurve initWithColorCurveElements:]_block_invoke : 164 -> 156
~ -[SGCubicColorCurve dealloc] : 100 -> 108
~ -[SGCubicColorCurve rgbfColorForFraction:] : 260 -> 280
~ +[SGCubicSplineMatrixCache sharedInstance] : 84 -> 68
~ -[SGCubicSplineMatrixCache splineMatrixWithDimension:cache:matrixGenerator:] : 244 -> 252
~ ___76-[SGCubicSplineMatrixCache splineMatrixWithDimension:cache:matrixGenerator:]_block_invoke : 344 -> 328
~ -[SGCubicSpline initWithNumberOfControlPoints:isClosed:] : 192 -> 188
~ _SGStartOfDayForDate : 132 -> 124
~ _SGStartOfNextDayForDate : 164 -> 160
~ _SGPercentageOfDayDoneForDateWithStartAndEnd : 160 -> 168
~ _SGCircleSectorPath : 172 -> 168
CStrings:
- ".cxx_destruct"
- "16@0:8"
- "20@0:8f16"
- "24@0:8d16"
- "28@0:8f16^20"
- "@\"CAMediaTimingFunction\""
- "@\"CLLocation\""
- "@\"NSArray\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"SGColorPalette\""
- "@\"SGCubicColorCurve\""
- "@\"SGCubicSpline\""
- "@\"UIColor\""
- "@16@0:8"
- "@20@0:8f16"
- "@24@0:8@16"
- "@24@0:8d16"
- "@24@0:8i16B20"
- "@28@0:8@16f24"
- "@32@0:8@16@24"
- "@36@0:8d16@24B32"
- "@40@0:8d1624"
- "@40@0:8{CGPoint=dd}16r^{CGPathElement=i^{CGPoint}}32"
- "B"
- "B16@0:8"
- "CGPath"
- "NNASoftNTKGossamerColorPaletteWrapper"
- "Q"
- "Q16@0:8"
- "Q20@0:8i16"
- "SGBezierPathElement"
- "SGColorCurve"
- "SGColorCurveElement"
- "SGColorPalette"
- "SGCubicColorCurve"
- "SGCubicColorCurveElement"
- "SGCubicSpline"
- "SGCubicSplineMatrixCache"
- "SGGeometryUtilities"
- "SGSiderealColorManager"
- "SGSiderealData"
- "SG_setBoundsAndPositionFromFrame:"
- "T,N,V_color"
- "T@\"CAMediaTimingFunction\",&,N,V_timingFunction"
- "T@\"CLLocation\",R,N,V_location"
- "T@\"NSArray\",R,N,V_colorCurveElements"
- "T@\"UIColor\",&,N,V_color"
- "TB,R,N,V_sunsetFilterEnabled"
- "TB,R,N,V_sunsetFollowsSunrise"
- "TB,R,N,V_useXR"
- "TQ,N,V_pointCount"
- "T^{CGPoint=dd},N,V_points"
- "Td,N,V_fraction"
- "Td,N,V_length"
- "Td,R,N,V_solarNoonTime"
- "Td,R,N,V_startOfDay"
- "Td,R,N,V_sunriseTime"
- "Td,R,N,V_sunsetFilterRampDownStartProgress"
- "Td,R,N,V_sunsetFilterRampUpStartProgress"
- "Td,R,N,V_sunsetTime"
- "Tf,N,V_fraction"
- "Ti,N,V_type"
- "T{CGPoint=dd},R,N"
- "[361f]"
- "^"
- "^f"
- "^{?=^d^fi}"
- "^{?=^d^fi}20@0:8i16"
- "^{?=^d^fi}36@0:8i16@20@?28"
- "^{?=^i}"
- "^{?=^i}16@0:8"
- "^{CGPoint=dd}"
- "^{CGPoint=dd}16@0:8"
- "_a"
- "_absoluteTimeToJulianDay:"
- "_altitudes"
- "_applySunsetFilter:toColor:"
- "_astronomicalTwilight"
- "_astronomicalTwilightCurve_p3"
- "_b"
- "_c"
- "_civilTwilight"
- "_civilTwilightCurve_p3"
- "_closed"
- "_closedMatrixCache"
- "_color"
- "_colorCurveElements"
- "_colorPalette"
- "_colors"
- "_controlPoints"
- "_count"
- "_createElementsFromDict:"
- "_d"
- "_dayDiskBloom"
- "_dayGradient"
- "_dayGradientCurve_p3"
- "_dialBackground"
- "_dialBackgroundCurve_p3"
- "_fraction"
- "_fractions"
- "_geoLocationForLocation:"
- "_init"
- "_innerComplication"
- "_internalQueue"
- "_length"
- "_location"
- "_nauticalTwilight"
- "_nauticalTwilightCurve_p3"
- "_notifyHandlers"
- "_openMatrixCache"
- "_outerComplication"
- "_pointCount"
- "_points"
- "_processClosedSpline"
- "_processOpenSpline"
- "_processSpline"
- "_processedPoints"
- "_solarNoonTime"
- "_solveForInput:"
- "_spline"
- "_splineMatrix"
- "_startIndex"
- "_startOfDay"
- "_sunriseTime"
- "_sunsetFilterEnabled"
- "_sunsetFilterRampDownStartProgress"
- "_sunsetFilterRampUpStartProgress"
- "_sunsetFollowsSunrise"
- "_sunsetTime"
- "_timingFunction"
- "_type"
- "_updateHandlers"
- "_useXR"
- "_workspace"
- "addArcWithCenter:radius:startAngle:endAngle:clockwise:"
- "addColorUpdateHandler:"
- "addCurveToPoint:controlPoint1:controlPoint2:"
- "addLineToPoint:"
- "addObject:"
- "addQuadCurveToPoint:controlPoint:"
- "allKeys"
- "altitude"
- "anchorPoint"
- "array"
- "arrayWithObjects:count:"
- "assertColor:closeTo:"
- "assertDouble:closeTo:"
- "astronomicalTwilightColorCurve"
- "astronomicalTwilightCurveP3"
- "bezierPath"
- "blackColor"
- "bounds"
- "civilTwilightColorCurve"
- "civilTwilightCurveP3"
- "closePath"
- "closedSplineMatrixWithDimension:"
- "color"
- "colorCurveElements"
- "colorForFraction:"
- "colorWithHue:saturation:brightness:alpha:"
- "colorWithRed:green:blue:alpha:"
- "compare:"
- "computeLength"
- "controlPointsBuffer"
- "coordinate"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentCalendar"
- "d"
- "d16@0:8"
- "d24@0:8d16"
- "dateByAddingUnit:value:toDate:options:"
- "dayDiskBloomColorCurve"
- "dayGradientColorCurves"
- "dayGradientCurveP3"
- "dealloc"
- "description"
- "dialBackgroundColorCurve"
- "dialBackgroundCurveP3"
- "dictionaryWithObjects:forKeys:count:"
- "endPoint"
- "f"
- "f16@0:8"
- "firstObject"
- "floatValue"
- "fraction"
- "functionWithName:"
- "getControlPoints:processedPoints:"
- "getRed:green:blue:alpha:"
- "getSolarColorsForLocation:atDate:"
- "gradientWithSunsetFilterForDayProgress:"
- "i16@0:8"
- "init"
- "initWithColor:fraction:"
- "initWithColorCurveElements:"
- "initWithCubicColorCurveElements:"
- "initWithLocation:julianDay:body:useHighPrecision:"
- "initWithLocation:time:altitudeInDegrees:accuracy:"
- "initWithNumberOfControlPoints:isClosed:"
- "initWithStartOfDay:location:useXR:"
- "initWithStartPoint:pathElement:"
- "innerComplicationColorCurve"
- "interpolateAt:"
- "interpolateAt:derivative:"
- "interpolateWithSteps:interpolation:"
- "isClosed"
- "lastObject"
- "layer"
- "length"
- "location"
- "moveToPoint:"
- "nauticalTwilightColorCurve"
- "nauticalTwilightCurveP3"
- "nextEventOfType:"
- "numberOfPointsForCGPathElementType:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "openSplineMatrixWithDimension:"
- "outerComplicationColorCurve"
- "pointCount"
- "pointOnPathForX:"
- "pointerValue"
- "points"
- "process"
- "pseudoAltitudeForProgress:"
- "rgbfColorForFraction:"
- "screenBounds"
- "screenCornerRadius"
- "setBounds:"
- "setCenter:"
- "setColor:"
- "setFraction:"
- "setLength:"
- "setObject:forKeyedSubscript:"
- "setPointCount:"
- "setPoints:"
- "setSunAltitude:"
- "setTimingFunction:"
- "setType:"
- "sharedInstance"
- "sharedPalette"
- "solarNoonTime"
- "sortedArrayUsingComparator:"
- "splineMatrixWithDimension:cache:matrixGenerator:"
- "startOfDay"
- "startOfDayForDate:"
- "startPoint"
- "stringWithFormat:"
- "sunriseTime"
- "sunsetFilter:"
- "sunsetFilterEnabled"
- "sunsetFilterRampDownStartProgress"
- "sunsetFilterRampUpStartProgress"
- "sunsetFollowsSunrise"
- "sunsetTime"
- "timeIntervalSinceReferenceDate"
- "timeToProgress:"
- "timingFunction"
- "type"
- "useXR"
- "v16@0:8"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^{CGPoint=dd}16"
- "v24@0:8d16"
- "v28@0:8i16@?20"
- "v32@0:816"
- "v32@0:8@16@24"
- "v32@0:8^^16^^24"
- "v32@0:8d16d24"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "valueWithPointer:"
- "{?=dd}24@0:8@16"
- "{CGPoint=dd}16@0:8"
- "{CGPoint=dd}24@0:8d16"

```
