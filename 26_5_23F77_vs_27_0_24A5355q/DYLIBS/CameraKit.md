## CameraKit

> `/System/Library/PrivateFrameworks/CameraKit.framework/CameraKit`

```diff

-852.0.102.0.0
-  __TEXT.__text: 0x1d48
-  __TEXT.__auth_stubs: 0x180
+910.14.107.0.0
+  __TEXT.__text: 0x1c8c
   __TEXT.__objc_methlist: 0x228
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xa3
+  __TEXT.__cstring: 0xa5
   __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x24
-  __TEXT.__objc_methname: 0x82f
-  __TEXT.__objc_methtype: 0x235
-  __TEXT.__objc_stubs: 0x880
-  __DATA_CONST.__got: 0x68
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x2f8
   __AUTH_CONST.__objc_doubleobj: 0x20
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x24
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBFC7C6B-58D3-3736-A85F-5F628EE5FBBE
+  UUID: 06B92A5B-48D2-32F9-9B18-C7BC73E108B1
   Functions: 47
   Symbols:   230
-  CStrings:  160
+  CStrings:  21
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"UIActivityIndicatorView\""
- "@\"UIImageView\""
- "@\"UIView\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8q16"
- "@48@0:8{CAMShutterButtonSpec=dddd}16"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@48@0:8{CMKShutterButtonSpec=dddd}16"
- "B"
- "B16@0:8"
- "B24@0:8q16"
- "CAMShutterButton"
- "CGColor"
- "CMKShutterButton"
- "T@\"UIActivityIndicatorView\",R,N,V__progressActivityIndicatorView"
- "T@\"UIImageView\",R,N,V__outerImageView"
- "T@\"UIView\",R,N,V__innerView"
- "T@\"UIView\",R,N,V__outerView"
- "TB,N,GisPulsing,V_pulsing"
- "TB,N,GisSpinning,V_spinning"
- "TB,N,V_showDisabled"
- "Tq,D,N"
- "Tq,N,V_buttonMode"
- "T{CMKShutterButtonSpec=dddd},N,S_setSpec:,V_spec"
- "__innerView"
- "__outerImageView"
- "__outerView"
- "__progressActivityIndicatorView"
- "_borderWidthForMode:"
- "_buttonMode"
- "_colorForMode:"
- "_commonCMKShutterButtonInitialization"
- "_cornerRadiusForMode:"
- "_innerCircleDiameter"
- "_innerView"
- "_isStopMode:"
- "_outerImageForMode:"
- "_outerImageView"
- "_outerView"
- "_performHighlightAnimation"
- "_performModeSwitchAnimationFromMode:toMode:animated:"
- "_progressActivityIndicatorView"
- "_pulsing"
- "_setSpec:"
- "_shouldUseImageViewForMode:"
- "_shouldUseTimelapseOuterViewForMode:"
- "_showDisabled"
- "_sizeForMode:"
- "_spec"
- "_spinning"
- "_updateOuterAndInnerLayers"
- "_updateSpinningAnimations"
- "addAnimation:forKey:"
- "addSubview:"
- "alpha"
- "animateWithDuration:delay:options:animations:completion:"
- "animationWithKeyPath:"
- "bounds"
- "buttonMode"
- "colorWithRed:green:blue:alpha:"
- "convertTime:fromLayer:"
- "d16@0:8"
- "d24@0:8q16"
- "frame"
- "functionWithControlPoints::::"
- "functionWithName:"
- "initWithActivityIndicatorStyle:"
- "initWithCoder:"
- "initWithFrame:"
- "insertSubview:belowSubview:"
- "intrinsicContentSize"
- "isHighlighted"
- "isPulsing"
- "isSpinning"
- "layer"
- "layoutSubviews"
- "mode"
- "numberWithDouble:"
- "presentationLayer"
- "pulsing"
- "q"
- "q16@0:8"
- "removeAllAnimations"
- "removeFromSuperview"
- "setAdjustsImageWhenDisabled:"
- "setAdjustsImageWhenHighlighted:"
- "setAlpha:"
- "setAnimationDuration:"
- "setBackgroundColor:"
- "setBeginTime:"
- "setBorderColor:"
- "setBorderWidth:"
- "setButtonMode:"
- "setButtonMode:animated:"
- "setColor:"
- "setCornerRadius:"
- "setDuration:"
- "setFillMode:"
- "setFrame:"
- "setFromValue:"
- "setHighlighted:"
- "setImage:"
- "setMode:animated:"
- "setOpacity:"
- "setPulsing:"
- "setShowDisabled:"
- "setShowsTouchWhenHighlighted:"
- "setSpinning:"
- "setTimingFunction:"
- "setToValue:"
- "setUserInteractionEnabled:"
- "setValue:forKeyPath:"
- "showDisabled"
- "shutterButton"
- "shutterButtonWithDesiredSpec:"
- "shutterButtonWithSpec:"
- "sizeThatFits:"
- "smallShutterButton"
- "spec"
- "spinning"
- "startAnimating"
- "stopAnimating"
- "tinyShutterButton"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8q16"
- "v28@0:8q16B24"
- "v36@0:8q16q24B32"
- "v48@0:8{CMKShutterButtonSpec=dddd}16"
- "valueForKeyPath:"
- "valueWithCGSize:"
- "whiteColor"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}24@0:8q16"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "{CMKShutterButtonSpec=\"outerRingDiameter\"d\"outerRingStrokeWidth\"d\"stopSquareSideLength\"d\"stopSquareCornerRadius\"d}"
- "{CMKShutterButtonSpec=dddd}16@0:8"

```
