## CompassUI

> `/System/Library/PrivateFrameworks/CompassUI.framework/CompassUI`

```diff

-338.35.2.9.2
-  __TEXT.__text: 0x4e90
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x3ac
-  __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x3b3
+363.30.5.8.1
+  __TEXT.__text: 0x52e4
+  __TEXT.__objc_methlist: 0x55c
+  __TEXT.__const: 0x1f0
+  __TEXT.__cstring: 0x3bb
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x198
-  __TEXT.__objc_classname: 0xab
-  __TEXT.__objc_methname: 0x1172
-  __TEXT.__objc_methtype: 0x21c
-  __TEXT.__objc_stubs: 0x1540
-  __DATA_CONST.__got: 0x160
+  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x8
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x640
+  __DATA_CONST.__objc_selrefs: 0x748
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1c8
-  __AUTH_CONST.__const: 0x40
+  __DATA_CONST.__got: 0x158
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0x9e8
+  __AUTH_CONST.__objc_const: 0xc30
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xb0
-  __DATA.__data: 0x68
-  __DATA.__bss: 0x20
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0xb4
+  __DATA.__data: 0x120
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreText.framework/CoreText

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F406A80F-8326-3072-81C8-312CEA4E711B
-  Functions: 101
-  Symbols:   151
-  CStrings:  382
+  UUID: 81756665-20F5-3854-9359-3CBEDC78EC7B
+  Functions: 107
+  Symbols:   154
+  CStrings:  87
 
Symbols:
+ _CGPointRoundToPixelWithScale
+ _UIFontWeightThin
+ _compassThinFontWithSize
+ _kCompassMediumFontSize
+ _kCompassThinFontSize
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- _CGPointRoundToPixel
- _OBJC_CLASS_$_CATransaction
- _OBJC_CLASS_$_UIScreen
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x24
CStrings:
+ "*\x81"
- "*"
- ".cxx_destruct"
- "@\"CALayer\""
- "@\"CAReplicatorLayer\""
- "@\"CAShapeLayer\""
- "@\"CalibrationBallView\""
- "@\"CompassBackgroundView\""
- "@\"NSMutableArray\""
- "@\"UIButton\""
- "@\"UILabel\""
- "@\"UIView\""
- "@16@0:8"
- "@32@0:8@16d24"
- "@32@0:8{CGPoint=dd}16"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@52@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16B48"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16d48"
- "AccessibilityCompassExtras"
- "B"
- "B16@0:8"
- "B32@0:8{CGSize=dd}16"
- "CGColor"
- "CGPath"
- "CUICalibration"
- "CalibrationBallView"
- "CalibrationViewController"
- "CompassBackgroundView"
- "CompassCalibrationProtocol"
- "CompassRotatingView"
- "Extras"
- "Q"
- "T@\"CALayer\",R,N"
- "Td,N,SsetAngle:,V_currentAngle"
- "Td,N,V_ballRadius"
- "Td,N,V_bearing"
- "Td,N,V_compassHeading"
- "Td,N,V_ticRadius"
- "Td,N,V_trackRadius"
- "Td,R,N,V_angle"
- "Td,R,N,V_ticLength"
- "^f"
- "_accessibilityConvertDecimalDegreeToDMS:degreesPtr:minutesPtr:secondsPtr:"
- "_angle"
- "_angleToRim"
- "_ballRadius"
- "_ballView"
- "_bearing"
- "_bearingLayer"
- "_bearingLength"
- "_bubbleLayer"
- "_calibrationAngle"
- "_calibrationConstraints"
- "_cancelButton"
- "_compassBackgroundViewMask"
- "_compassCenter"
- "_compassHeading"
- "_compassOriginPoint"
- "_compassRadius"
- "_compass_scaledValueForValue:"
- "_correctedAngleForCurrentOrientation:"
- "_crosshairLayer"
- "_crosshairLayerWithBounds:"
- "_crosshairPathInRect:"
- "_currentAngle"
- "_currentHeadingLayer"
- "_currentHeadingLength"
- "_currentOffset"
- "_fontScaledLikeTextStyle:maximumPointSize:compatibleWithTraitCollection:forIB:"
- "_ignoreMotionUpdates"
- "_instructionLabel"
- "_largeCompassTicLayers"
- "_numCompleteTics"
- "_previousGravity"
- "_previousHorizontalAngle"
- "_previousTimestamp"
- "_prototypeLargeTicLayer"
- "_prototypeSmallTicLayer"
- "_quantizationType"
- "_rotatingLayer"
- "_scaledValueForValue:"
- "_shouldCompleteTics"
- "_shownInCompass"
- "_smallCompassTicLayers"
- "_startTicAngle"
- "_staticLayer"
- "_ticLength"
- "_ticRadius"
- "_ticsShowingArray"
- "_trackRadius"
- "_updateSizes"
- "addAnimation:forKey:"
- "addConstraints"
- "addConstraints:"
- "addLineToPoint:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addSublayer:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "angle"
- "animationWithKeyPath:"
- "arrayWithObjects:count:"
- "autoupdatingCurrentLocale"
- "ballRadius"
- "ballView"
- "bearing"
- "bearingLayer"
- "begin"
- "bezierPath"
- "bezierPathWithOvalInRect:"
- "blackColor"
- "boldSystemFontOfSize:"
- "boolForKey:"
- "bounds"
- "bubbleLayer"
- "buttonWithType:"
- "cancel"
- "center"
- "circleIsCompleted"
- "clearColor"
- "colorWithWhite:alpha:"
- "commit"
- "compassHeading"
- "completeCircle"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "constraintsWithVisualFormat:options:metrics:views:"
- "count"
- "crosshairLayer"
- "currentAngle"
- "currentHeadingLayer"
- "currentLayer"
- "currentThread"
- "d"
- "d16@0:8"
- "d24@0:8d16"
- "dealloc"
- "defaultCenter"
- "dictionaryWithObjects:forKeys:count:"
- "dismissCalibrationAlert"
- "doubleForKey:"
- "doubleValue"
- "f32@0:8d16d24"
- "filterWithType:"
- "fontDescriptor"
- "fontDescriptorByAddingAttributes:"
- "fontWithDescriptor:size:"
- "frame"
- "gravity"
- "grayColor"
- "hideAllTics"
- "horizontalSizeClass"
- "init"
- "initWithFormat:"
- "initWithFrame:"
- "initWithFrame:ballRadius:"
- "initWithFrame:forCompass:"
- "initWithObjects:"
- "initWithOriginPoint:"
- "initWithServiceName:"
- "initWithSuiteName:"
- "integerForKey:"
- "interfaceOrientation"
- "interfaceWithProtocol:"
- "invalidate"
- "isInternalInstall"
- "largeCompassTicLayers"
- "layer"
- "layoutIfNeeded"
- "layoutSubviews"
- "localizedStringForKey:value:table:"
- "localizedStringFromNumber:numberStyle:"
- "mainBundle"
- "mainScreen"
- "moveToPoint:"
- "numberWithDouble:"
- "numberWithInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "pointSize"
- "preferredFontForTextStyle:"
- "prefersStatusBarHidden"
- "presentationLayer"
- "prototypeLargeTicLayer"
- "prototypeSmallTicLayer"
- "quantizedPercentage:forAngle:"
- "redColor"
- "remoteObjectProxy"
- "removeAllObjects"
- "removeConstraints:"
- "removeObserver:"
- "reset"
- "resume"
- "rotateView:byAngle:"
- "rotatingLayer"
- "scale"
- "setAdjustsFontSizeToFitWidth:"
- "setAllowsEdgeAntialiasing:"
- "setAngle:"
- "setBackgroundColor:"
- "setBallAngle:tiltAngle:"
- "setBallRadius:"
- "setBearing:"
- "setBeginTime:"
- "setBorderColor:"
- "setBorderWidth:"
- "setBounds:"
- "setCenter:"
- "setCompassHeading:"
- "setCompositingFilter:"
- "setCornerRadius:"
- "setCrosshairOffset:"
- "setDamping:"
- "setDisableActions:"
- "setDuration:"
- "setFillColor:"
- "setFillMode:"
- "setFont:"
- "setFrame:"
- "setFromValue:"
- "setHidden:"
- "setInstanceCount:"
- "setInstanceTransform:"
- "setLineWidth:"
- "setLocale:"
- "setMasksToBounds:"
- "setMass:"
- "setMinimumScaleFactor:"
- "setMotion:"
- "setNeedsLayout"
- "setNegativePrefix:"
- "setNumberOfLines:"
- "setNumberStyle:"
- "setObject:forKey:"
- "setOpacity:"
- "setPath:"
- "setPosition:"
- "setRemoteObjectInterface:"
- "setStiffness:"
- "setStrokeColor:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTicRadius:"
- "setTitle:forState:"
- "setTitleColor:forState:"
- "setToValue:"
- "setTrackRadius:"
- "setTransform:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setValue:forKeyPath:"
- "sharedPlatform"
- "showCalibrationAlert"
- "showCalibrationAlert:"
- "showTicAtAngle:withCredit:"
- "showTicsBetweenStartAngle:endAngle:withCredit:"
- "smallCompassTicLayers"
- "standardUserDefaults"
- "staticLayer"
- "systemFontOfSize:"
- "systemFontOfSize:weight:"
- "threadDictionary"
- "ticLength"
- "ticRadius"
- "timestamp"
- "titleLabel"
- "trackRadius"
- "traitCollection"
- "updateMaskingPath"
- "updatedMaskingPath"
- "userDefaultsChanged:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8d16"
- "v32@0:8d16d24"
- "v40@0:8d16d24d32"
- "v48@0:8d16^q24^q32^d40"
- "verticalSizeClass"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillLayoutSubviews"
- "whiteColor"
- "window"
- "windowScene"
- "{CGPoint=\"x\"d\"y\"d}"

```
