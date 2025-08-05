## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4557.0.6.103.0
-  __TEXT.__text: 0x9eb78
-  __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0xe154
-  __TEXT.__const: 0xa58
+4557.0.9.100.0
+  __TEXT.__text: 0x9fafc
+  __TEXT.__auth_stubs: 0x1620
+  __TEXT.__objc_methlist: 0xe23c
+  __TEXT.__const: 0x9f8
   __TEXT.__gcc_except_tab: 0x98c
-  __TEXT.__cstring: 0xa5c4
+  __TEXT.__cstring: 0xa597
   __TEXT.__dlopen_cstrs: 0x42e
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x43d8
-  __TEXT.__unwind_info: 0x2fe0
-  __TEXT.__objc_classname: 0x3dbc
-  __TEXT.__objc_methname: 0x23a7c
-  __TEXT.__objc_methtype: 0x60a5
-  __TEXT.__objc_stubs: 0x169c0
-  __DATA_CONST.__got: 0x1028
+  __TEXT.__unwind_info: 0x3030
+  __TEXT.__objc_classname: 0x3dbe
+  __TEXT.__objc_methname: 0x23cc8
+  __TEXT.__objc_methtype: 0x6112
+  __TEXT.__objc_stubs: 0x16b40
+  __DATA_CONST.__got: 0x1020
   __DATA_CONST.__const: 0x2c08
   __DATA_CONST.__objc_classlist: 0x900
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x4b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x79b0
+  __DATA_CONST.__objc_selrefs: 0x7a28
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x5c8
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0xb10
+  __AUTH_CONST.__auth_got: 0xb20
   __AUTH_CONST.__const: 0x960
-  __AUTH_CONST.__cfstring: 0x9dc0
-  __AUTH_CONST.__objc_const: 0x2c8d8
+  __AUTH_CONST.__cfstring: 0x9d60
+  __AUTH_CONST.__objc_const: 0x2c918
   __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH_CONST.__objc_doubleobj: 0x170
+  __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x4b00
-  __DATA.__objc_ivar: 0xcdc
+  __AUTH.__objc_data: 0x4d30
+  __DATA.__objc_ivar: 0xce4
   __DATA.__data: 0x38c8
   __DATA.__bss: 0x3d8
-  __DATA_DIRTY.__objc_data: 0xf00
+  __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CEFC1907-D82B-3E05-B0F1-C2BF0E1360E8
-  Functions: 4576
-  Symbols:   17345
-  CStrings:  9446
+  UUID: 06EC3B04-F0E0-3C92-BBFF-9AFEBDA5D867
+  Functions: 4600
+  Symbols:   17407
+  CStrings:  9462
 
Symbols:
+ +[SBUIPasscodeLockViewFactory _passcodeLockViewForStyle:withLightStyle:dimmed:]
+ +[SBUIPasscodeLockViewFactory undimmedLightPasscodeLockViewForStyle:]
+ +[SBUIPasscodeLockViewFactory undimmedLightPasscodeLockViewForUsersCurrentStyle]
+ +[SBUIPasscodeLockViewFactory undimmedPasscodeLockViewForStyle:]
+ +[SBUIPasscodeLockViewFactory undimmedPasscodeLockViewForUsersCurrentStyle]
+ +[SBUIPasscodeLockViewWithKeypad providesDimmingByDefault]
+ -[SBUIPasscodeLockNumberPad _animateBounceIn]
+ -[SBUIPasscodeLockNumberPad _animateFlyOut]
+ -[SBUIPasscodeLockNumberPad _bounceInResponseForPoint:center:]
+ -[SBUIPasscodeLockNumberPad _flyOutResponseForPoint:center:]
+ -[SBUIPasscodeLockNumberPad _isBoundsPortraitOriented]
+ -[SBUIPasscodeLockNumberPad _numberPadOffsetFromTopOfScreen]
+ -[SBUIPasscodeLockNumberPad _responseForPoint:withCenter:curveFactor:]
+ -[SBUIPasscodeLockNumberPad _setButtonsVisible:]
+ -[SBUIPasscodeLockViewInstallTonightLongNumericKeypad initWithLightStyle:providesDimming:]
+ -[SBUIPasscodeLockViewInstallTonightSimpleFixedDigitKeypad initWithLightStyle:providesDimming:numberOfDigits:]
+ -[SBUIPasscodeLockViewLongNumericKeypad initWithLightStyle:providesDimming:]
+ -[SBUIPasscodeLockViewSimpleFixedDigitKeypad initWithLightStyle:providesDimming:numberOfDigits:]
+ -[SBUIPasscodeLockViewWithKeypad initWithLightStyle:providesDimming:]
+ GCC_except_table137
+ _OBJC_IVAR_$_SBUIPasscodeLockNumberPad._originalNumberPadBounds
+ _OBJC_IVAR_$_SBUIPasscodeLockViewWithKeypad._numberPadDimmingView
+ _UIDistanceBetweenPoints
+ __OBJC_$_CLASS_METHODS_SBUIPasscodeLockViewWithKeypad
+ ___43-[SBUIPasscodeLockNumberPad _animateFlyOut]_block_invoke
+ ___43-[SBUIPasscodeLockNumberPad _animateFlyOut]_block_invoke_2
+ ___43-[SBUIPasscodeLockNumberPad _animateFlyOut]_block_invoke_3
+ ___45-[SBUIPasscodeLockNumberPad _animateBounceIn]_block_invoke
+ ___45-[SBUIPasscodeLockNumberPad _animateBounceIn]_block_invoke_2
+ ___45-[SBUIPasscodeLockNumberPad _animateBounceIn]_block_invoke_3
+ _clampmap
+ _convertDampingRatioAndResponseToTensionAndFriction
+ _objc_msgSend$_animateBounceIn
+ _objc_msgSend$_animateFlyOut
+ _objc_msgSend$_animateUsingSpringWithTension:friction:interactive:animations:completion:
+ _objc_msgSend$_bounceInResponseForPoint:center:
+ _objc_msgSend$_flyOutResponseForPoint:center:
+ _objc_msgSend$_numberPadOffsetFromTopOfScreen
+ _objc_msgSend$_passcodeLockViewForStyle:withLightStyle:dimmed:
+ _objc_msgSend$_responseForPoint:withCenter:curveFactor:
+ _objc_msgSend$_setButtonsVisible:
+ _objc_msgSend$initWithLightStyle:providesDimming:
+ _objc_msgSend$initWithLightStyle:providesDimming:numberOfDigits:
+ _objc_msgSend$providesDimmingByDefault
+ _objc_msgSend$setOpacity:
+ _objc_msgSend$setSublayerTransform:
+ _objc_msgSend$setZPosition:
+ _objc_msgSend$sublayerTransform
+ _objc_msgSend$undimmedLightPasscodeLockViewForStyle:
+ _objc_msgSend$undimmedPasscodeLockViewForStyle:
+ _objc_msgSend$valueWithNonretainedObject:
- +[SBUIPasscodeLockViewFactory _passcodeLockViewForStyle:withLightStyle:]
- GCC_except_table138
- ___63-[SBUIPasscodeLockViewBase _setPasscodeLockViewState:animated:]_block_invoke_5
- _kCAAnimationRelative
- _objc_msgSend$_auxiliaryButtonCenteringOffset
- _objc_msgSend$_passcodeLockViewForStyle:withLightStyle:
- _objc_msgSend$insertObject:atIndex:
- _objc_msgSend$setBeginTimeMode:
- _objc_msgSend$setHighFrameRateReason:
- _objc_msgSend$subarrayWithRange:
- _objc_msgSend$valueWithCATransform3D:
- _setVisible:animated:.rowParametersIn
CStrings:
+ "@24@0:8B16B20"
+ "@28@0:8i16B20B24"
+ "@32@0:8B16B20Q24"
+ "_animateBounceIn"
+ "_animateFlyOut"
+ "_animateUsingSpringWithTension:friction:interactive:animations:completion:"
+ "_bounceInResponseForPoint:center:"
+ "_flyOutResponseForPoint:center:"
+ "_numberPadDimmingView"
+ "_numberPadOffsetFromTopOfScreen"
+ "_originalNumberPadBounds"
+ "_passcodeLockViewForStyle:withLightStyle:dimmed:"
+ "_responseForPoint:withCenter:curveFactor:"
+ "_setButtonsVisible:"
+ "d48@0:8{CGPoint=dd}16{CGPoint=dd}32"
+ "d56@0:8{CGPoint=dd}16{CGPoint=dd}32d48"
+ "initWithLightStyle:providesDimming:"
+ "initWithLightStyle:providesDimming:numberOfDigits:"
+ "providesDimmingByDefault"
+ "setOpacity:"
+ "setSublayerTransform:"
+ "setZPosition:"
+ "sublayerTransform"
+ "undimmedLightPasscodeLockViewForStyle:"
+ "undimmedLightPasscodeLockViewForUsersCurrentStyle"
+ "undimmedPasscodeLockViewForStyle:"
+ "undimmedPasscodeLockViewForUsersCurrentStyle"
+ "valueWithNonretainedObject:"
+ "\xd1"
- "@24@0:8i16B20"
- "_passcodeLockViewForStyle:withLightStyle:"
- "insertObject:atIndex:"
- "numberPadButton"
- "setBeginTimeMode:"
- "setHighFrameRateReason:"
- "sideButtonsOpacity"
- "subarrayWithRange:"
- "valueWithCATransform3D:"

```
