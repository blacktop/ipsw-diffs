## UserNotificationCenter

> `/System/Library/CoreServices/UserNotificationCenter.app/Contents/MacOS/UserNotificationCenter`

```diff

-103.0.0.0.0
-  __TEXT.__text: 0xa0f4
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0x80c
-  __TEXT.__const: 0x68
-  __TEXT.__oslogstring: 0x353
-  __TEXT.__cstring: 0x5d4
-  __TEXT.__objc_methname: 0x2062
-  __TEXT.__objc_classname: 0x15f
-  __TEXT.__objc_methtype: 0x482
-  __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__unwind_info: 0x298
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0xa40
-  __DATA_CONST.__objc_classlist: 0x50
+106.0.0.0.0
+  __TEXT.__text: 0xbf10
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_stubs: 0x2ae0
+  __TEXT.__objc_methlist: 0xbac
+  __TEXT.__const: 0x78
+  __TEXT.__oslogstring: 0x354
+  __TEXT.__cstring: 0x6a6
+  __TEXT.__objc_methname: 0x2999
+  __TEXT.__objc_classname: 0x17f
+  __TEXT.__objc_methtype: 0x545
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__unwind_info: 0x300
+  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__cfstring: 0xb20
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __DATA.__objc_const: 0x1818
-  __DATA.__objc_selrefs: 0x960
-  __DATA.__objc_ivar: 0xe0
-  __DATA.__objc_data: 0x320
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x1a08
+  __DATA.__objc_selrefs: 0xcd8
+  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x20
   __DATA.__common: 0x8

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/IconFoundation.framework/Versions/A/IconFoundation
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices

   - /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 46093AFF-26C8-3A2B-A5D4-788DE7C589E3
-  Functions: 219
-  Symbols:   148
-  CStrings:  713
+  UUID: 9E01CB15-60AA-3ED5-AE32-D00C78081BFB
+  Functions: 267
+  Symbols:   165
+  CStrings:  874
 
Symbols:
+ _NSFontAttributeName
+ _NSFontWeightRegular
+ _NSForegroundColorAttributeName
+ _NSInvalidArgumentException
+ _NSStringFromClass
+ _OBJC_CLASS_$_CABasicAnimation
+ _OBJC_CLASS_$_NSColor
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSFont
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_NSShadow
+ _OBJC_CLASS_$_NSStackView
+ _OBJC_CLASS_$_NSValue
+ _objc_autorelease
+ _objc_exception_throw
+ _objc_retainAutorelease
CStrings:
+ "@\"NSColor\""
+ "@\"NSFont\""
+ "@\"NSStackView\""
+ "@\"OTPView\""
+ "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "All numbers must be single-digit (0-9)!"
+ "CGColor"
+ "Invalid class in digit array! (class: %@)"
+ "OTPCharacterView"
+ "OTPDigitCount"
+ "OTPDigits"
+ "OTPFailed"
+ "OTPHighlightedDigitCount"
+ "OTPView"
+ "S"
+ "S16@0:8"
+ "T@\"NSArray\",&,N,V_digits"
+ "T@\"NSArray\",&,N,V_paddingConstraints"
+ "T@\"NSArray\",R,V_digits"
+ "T@\"NSColor\",&,N,V_backgroundColor"
+ "T@\"NSColor\",&,N,V_foregroundColor"
+ "T@\"NSDictionary\",&,N,V_characterAttributes"
+ "T@\"NSFont\",&,N,V_font"
+ "T@\"NSStackView\",&,N,V_digitStackView"
+ "TB,N,GisHighlighted,V_highlighted"
+ "TB,R,V_otpFailed"
+ "TQ,N,V_digitCount"
+ "TQ,N,V_highlightedDigitCount"
+ "TQ,R,V_digitCount"
+ "TQ,R,V_highlightedDigitCount"
+ "TS,N,V_character"
+ "Td,N,V_horizontalPadding"
+ "Td,N,V_padding"
+ "Td,N,V_verticalPadding"
+ "_backgroundColor"
+ "_character"
+ "_characterAttributes"
+ "_digitCount"
+ "_digitStackView"
+ "_digits"
+ "_font"
+ "_foregroundColor"
+ "_highlighted"
+ "_highlightedDigitCount"
+ "_horizontalPadding"
+ "_otpFailed"
+ "_otpView"
+ "_padding"
+ "_paddingConstraints"
+ "_verticalPadding"
+ "activateConstraints:"
+ "addAnimation:forKey:"
+ "addArrangedSubview:"
+ "addSubview:"
+ "animationWithKeyPath:"
+ "arrangedSubviews"
+ "arrayWithArray:"
+ "backgroundColor"
+ "blackColor"
+ "boolForValue:"
+ "boolValue"
+ "bottomAnchor"
+ "boundingRectWithSize:options:attributes:"
+ "centerXAnchor"
+ "centerYAnchor"
+ "character"
+ "characterAttributes"
+ "colorWithAlphaComponent:"
+ "config dict = %{private}@"
+ "configureDigitViews"
+ "constraintEqualToAnchor:"
+ "constraintEqualToAnchor:constant:"
+ "controlBackgroundColor"
+ "controlTextColor"
+ "d"
+ "d16@0:8"
+ "deactivateConstraints:"
+ "dictionaryWithObjects:forKeys:count:"
+ "digitCount"
+ "digitStackView"
+ "digits"
+ "drawAtPoint:withAttributes:"
+ "drawRect:"
+ "exceptionWithName:reason:userInfo:"
+ "font"
+ "foregroundColor"
+ "highlighted"
+ "highlightedDigitCount"
+ "horizontalPadding"
+ "initWithFrame:"
+ "insertObject:atIndex:"
+ "intValue"
+ "invalidateIntrinsicContentSize"
+ "isHighlighted"
+ "layer"
+ "leadingAnchor"
+ "monospacedSystemFontOfSize:weight:"
+ "mutableCopy"
+ "numbersForValue:"
+ "otpFailed"
+ "padding"
+ "paddingConstraints"
+ "position"
+ "removeArrangedSubview:"
+ "removeFromSuperview"
+ "removeObjectAtIndex:"
+ "removeObjectForKey:"
+ "setAlphaValue:"
+ "setAutoreverses:"
+ "setBackgroundColor:"
+ "setCharacter:"
+ "setCharacterAttributes:"
+ "setCornerRadius:"
+ "setDigitCount:"
+ "setDigitStackView:"
+ "setDigits:"
+ "setDistribution:"
+ "setDuration:"
+ "setFont:"
+ "setForegroundColor:"
+ "setFromValue:"
+ "setHighlighted:"
+ "setHighlightedDigitCount:"
+ "setHorizontalPadding:"
+ "setMasksToBounds:"
+ "setNeedsDisplay:"
+ "setOrientation:"
+ "setPadding:"
+ "setPaddingConstraints:"
+ "setRepeatCount:"
+ "setShadow:"
+ "setShadowBlurRadius:"
+ "setShadowColor:"
+ "setShadowOffset:"
+ "setSpacing:"
+ "setToValue:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "setVerticalPadding:"
+ "setWantsLayer:"
+ "shake"
+ "stringWithCharacters:length:"
+ "subviews"
+ "topAnchor"
+ "trailingAnchor"
+ "v20@0:8B16"
+ "v20@0:8S16"
+ "v24@0:8Q16"
+ "v24@0:8d16"
+ "v32@?0@\"NSView\"8Q16^B24"
+ "v32@?0@\"OTPCharacterView\"8Q16^B24"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "valueWithPoint:"
+ "verticalPadding"
+ "\x81"
- "config dict = %{public}@"

```
