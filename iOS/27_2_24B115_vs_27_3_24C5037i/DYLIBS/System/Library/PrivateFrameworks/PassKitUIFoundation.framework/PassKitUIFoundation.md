## PassKitUIFoundation

> `/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation`

```diff

-1696.2.9.0.0
-  __TEXT.__text: 0x25c44
-  __TEXT.__objc_methlist: 0x1d1c
-  __TEXT.__const: 0x680
-  __TEXT.__cstring: 0xe9a
-  __TEXT.__oslogstring: 0x138d
-  __TEXT.__gcc_except_tab: 0x7f0
-  __TEXT.__unwind_info: 0xc90
+1696.3.2.0.0
+  __TEXT.__text: 0x28984
+  __TEXT.__objc_methlist: 0x1d5c
+  __TEXT.__const: 0x700
+  __TEXT.__cstring: 0x11a2
+  __TEXT.__oslogstring: 0x13e3
+  __TEXT.__gcc_except_tab: 0x854
+  __TEXT.__unwind_info: 0xd10
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe50
+  __DATA_CONST.__const: 0xf18
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c10
+  __DATA_CONST.__objc_selrefs: 0x1c58
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xa8
-  __DATA_CONST.__got: 0x5e8
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x46a0
+  __DATA_CONST.__got: 0x600
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x10c0
+  __AUTH_CONST.__objc_const: 0x4810
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x498
+  __AUTH_CONST.__auth_got: 0x698
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x4c0
   __DATA.__data: 0x4e0
-  __DATA_DIRTY.__objc_data: 0x550
+  __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libAccessibility.dylib
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 827
-  Symbols:   1929
-  CStrings:  254
+  Functions: 862
+  Symbols:   1986
+  CStrings:  265
 
Symbols:
+ +[PKAuthenticator resetSharedRootContextForSpringBoardWithCompletion:]
+ -[PKAuthenticatorEvaluationContext _createContextWithExternalizedContext:requireExternalizedContext:]
+ -[PKAuthenticatorSharedRootContext _consumeWithCompletion:reset:useSpringBoard:]
+ -[PKAuthenticatorSharedRootContext accessExternalizedContext:]
+ -[PKAuthenticatorSharedRootContext isPending]
+ -[PKAuthenticatorSharedRootContext resetForSpringBoardWithCompletion:]
+ -[PKDeviceGlyphLayer .cxx_destruct]
+ -[PKDeviceGlyphLayer _applyEffectivePrimaryColorToQRCodeAnimated:]
+ -[PKDeviceGlyphLayer _endPhoneWiggle]
+ -[PKDeviceGlyphLayer _restartPhoneWiggleIfNecessary]
+ -[PKDeviceGlyphLayer _startPhoneWiggle]
+ -[PKDeviceGlyphLayer dealloc]
+ -[PKDeviceGlyphLayer initWithDeviceType:]
+ -[PKDeviceGlyphLayer initWithFrame:package:]
+ -[PKDeviceGlyphLayer init]
+ -[PKDeviceGlyphLayer isHighlighted]
+ -[PKDeviceGlyphLayer layerDidBecomeVisible:]
+ -[PKDeviceGlyphLayer layoutSublayers]
+ -[PKDeviceGlyphLayer setHighlighted:animated:]
+ -[PKDeviceGlyphLayer setPrimaryColor:animated:]
+ -[PKDeviceGlyphLayer setShowQRCode:]
+ -[PKDeviceGlyphLayer showQRCode]
+ -[PKGlyphView _device:positionDeltaWhileShownFromRotationPercentage:toPercentage:]
+ -[PKGlyphView _device:positionWhileShownWithRotationPercentage:]
+ -[PKGlyphView _device:transformDeltaWhileShownFromRotationPercentage:toPercentage:]
+ -[PKGlyphView _pushRotation]
+ -[PKGlyphView _updateCoaching]
+ -[PKGlyphView coachingState]
+ GCC_except_table105
+ GCC_except_table170
+ GCC_except_table178
+ GCC_except_table182
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table67
+ GCC_except_table78
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table88
+ _CFDataGetBytePtr
+ _CFDataGetTypeID
+ _CFGetTypeID
+ _CGRectStandardize
+ _MGCopyAnswer
+ _MGCopyAnswerForDisplayAtIndex
+ _MGGetLogicalDeviceDisplayCount
+ _OBJC_CLASS_$_PKDeviceGlyphLayer
+ _OBJC_IVAR_$_PKAuthenticatorSharedRootContext._counter
+ _OBJC_IVAR_$_PKAuthenticatorSharedRootContext._pending
+ _OBJC_IVAR_$_PKAuthenticatorSharedRootContext._pendingAccessors
+ _OBJC_IVAR_$_PKDeviceGlyphLayer._QRCodeColorFilter
+ _OBJC_IVAR_$_PKDeviceGlyphLayer._QRCodeLayer
+ _OBJC_IVAR_$_PKDeviceGlyphLayer._highlightLayer
+ _OBJC_IVAR_$_PKDeviceGlyphLayer._highlightOffscreenPosition
+ _OBJC_IVAR_$_PKDeviceGlyphLayer._highlightOnscreenPosition
+ _OBJC_IVAR_$_PKDeviceGlyphLayer._highlighted
+ _OBJC_IVAR_$_PKDeviceGlyphLayer._phoneWiggleAnimationKey
+ _OBJC_IVAR_$_PKDeviceGlyphLayer._primaryColor
+ _OBJC_IVAR_$_PKDeviceGlyphLayer._showQRCode
+ _OBJC_IVAR_$_PKGlyphView._coachingState
+ _OBJC_IVAR_$_PKGlyphView._currentDevice
+ _OBJC_IVAR_$_PKGlyphView._currentIntentLayer
+ _OBJC_IVAR_$_PKGlyphView._deviceOrientationAnimationKey
+ _OBJC_IVAR_$_PKGlyphView._primaryDevice
+ _OBJC_IVAR_$_PKGlyphView._primaryIntentLayer
+ _OBJC_IVAR_$_PKGlyphView._secondaryDevice
+ _OBJC_IVAR_$_PKGlyphView._secondaryIntentLayer
+ _OBJC_IVAR_$_PKGlyphView._secondaryScreenSupported
+ _OBJC_IVAR_$_PKGlyphView._usePrimaryDeviceLayer
+ _OBJC_IVAR_$_PKGlyphView._usePrimaryIntentLayer
+ _OBJC_METACLASS_$_PKDeviceGlyphLayer
+ _PKScreenSize
+ _PhysicalButtonNormalizedFrame.frame
+ _PhysicalButtonNormalizedFrame.onceToken
+ _PhysicalButtonPrimaryNormalizedFrame.frame
+ _PhysicalButtonPrimaryNormalizedFrame.onceToken
+ _PhysicalButtonSecondaryNormalizedFrame.frame
+ _PhysicalButtonSecondaryNormalizedFrame.onceToken
+ _TouchIDColor
+ __OBJC_$_INSTANCE_METHODS_PKDeviceGlyphLayer
+ __OBJC_$_INSTANCE_VARIABLES_PKDeviceGlyphLayer
+ __OBJC_$_PROP_LIST_PKDeviceGlyphLayer
+ __OBJC_CLASS_RO_$_PKDeviceGlyphLayer
+ __OBJC_METACLASS_RO_$_PKDeviceGlyphLayer
+ __Z27_PKPassScreenSize_Normalize6CGSize31_PKPassNormalizedScreenSizeType
+ ___29-[PKGlyphView initWithStyle:]_block_invoke_4
+ ___29-[PKGlyphView initWithStyle:]_block_invoke_5
+ ___30-[PKGlyphView _endPhoneWiggle]_block_invoke_2
+ ___36-[PKDeviceGlyphLayer setShowQRCode:]_block_invoke
+ ___37-[PKDeviceGlyphLayer _endPhoneWiggle]_block_invoke
+ ___39-[PKDeviceGlyphLayer _startPhoneWiggle]_block_invoke
+ ___47-[PKGlyphView _updateUserIntentLayoutAnimated:]_block_invoke_3
+ ___62-[PKGlyphView _updatePhoneLayoutWithTransitionIndex:animated:]_block_invoke
+ ___80-[PKAuthenticatorSharedRootContext _consumeWithCompletion:reset:useSpringBoard:]_block_invoke
+ ___87-[PKAuthenticatorEvaluationContext initWithRequest:completionHandler:forAuthenticator:]_block_invoke_4
+ ___87-[PKAuthenticatorEvaluationContext initWithRequest:completionHandler:forAuthenticator:]_block_invoke_5
+ ___PKGlyphViewScreenIsPrimary
+ ___PKGlyphViewSupportsSecondaryEmbeddedDisplay
+ ___PKGlyphViewSupportsSecondaryEmbeddedDisplay.onceToken
+ ___PKGlyphViewSupportsSecondaryEmbeddedDisplay.supports
+ ___PhysicalButtonNormalizedFrame_block_invoke
+ ___PhysicalButtonPrimaryNormalizedFrame_block_invoke
+ ___PhysicalButtonSecondaryNormalizedFrame_block_invoke
+ _____PKGlyphViewSupportsSecondaryEmbeddedDisplay_block_invoke
+ ___block_descriptor_40_e8_32s_e241_v128?0^{?={?={?={?={CGPoint=dd}{CGPoint=dd}}ccd}{?=cd}{?={CGPoint=dd}{CGPoint=dd}}{?={CGPoint=dd}{CGPoint=dd}}}{CGSize=dd}{CGSize=dd}IIC}8I16{?={?={CGPoint=dd}{CGPoint=dd}}ccd}20{CGPoint=dd}68{CGPoint=dd}84{CGPoint=dd}100"NSURL"116I124ls32l8
+ ___block_descriptor_41_e8_32s_e146_v16?0^{?={?={?={?={CGPoint=dd}{CGPoint=dd}}ccd}{?=B{?=II}{?=II{?={CGPoint=dd}{CGPoint=dd}}}}}{CGSize=dd}IICC{CGRect={CGPoint=dd}{CGSize=dd}}}8ls32l8
+ ___block_descriptor_50_e8_32s40w_e16_v16?0"NSData"8lw40l8s32l8
+ ___block_descriptor_57_e8_32s40bs48bs_e142_v16?0^{?={?={?={?={CGPoint=dd}{CGPoint=dd}}ccd}{?=cd}{?={CGPoint=dd}{CGPoint=dd}}{?={CGPoint=dd}{CGPoint=dd}}}{CGSize=dd}{CGSize=dd}IIC}8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s_e55_"CAAnimation"32?0"NSString"8"NSValue"16"NSValue"24ls32l8s40l8
+ ___destructor_8_s0_s8_s16
+ ___destructor_8_s0_s8_s16_s24
+ _kCAMediaTimingFunctionEaseInEaseOut
+ _kMGDisplayIndexedQueryUserIntentPhysicalButtonNormalizedCGRect
- -[PKAuthenticatorEvaluationContext _createContextWithExternalizedContext:]
- -[PKAuthenticatorSharedRootContext _consumeWithCompletion:reset:]
- -[PKGlyphView _phonePositionDeltaWhileShownFromRotationPercentage:toPercentage:]
- -[PKGlyphView _phonePositionWhileShownWithRotationPercentage:]
- -[PKGlyphView _phoneTransformDeltaWhileShownFromRotationPercentage:toPercentage:]
- -[PKGlyphView _updateUserIntentLayerRotation]
- -[PKPhoneGlyphLayer .cxx_destruct]
- -[PKPhoneGlyphLayer _applyEffectivePrimaryColorToQRCodeAnimated:]
- -[PKPhoneGlyphLayer _endPhoneWiggle]
- -[PKPhoneGlyphLayer _restartPhoneWiggleIfNecessary]
- -[PKPhoneGlyphLayer _startPhoneWiggle]
- -[PKPhoneGlyphLayer dealloc]
- -[PKPhoneGlyphLayer initWithFrame:package:]
- -[PKPhoneGlyphLayer init]
- -[PKPhoneGlyphLayer layerDidBecomeVisible:]
- -[PKPhoneGlyphLayer layoutSublayers]
- -[PKPhoneGlyphLayer setHighlighted:animated:]
- -[PKPhoneGlyphLayer setPrimaryColor:animated:]
- -[PKPhoneGlyphLayer setShowQRCode:]
- -[PKPhoneGlyphLayer showQRCode]
- GCC_except_table163
- GCC_except_table171
- GCC_except_table175
- GCC_except_table183
- GCC_except_table185
- GCC_except_table42
- GCC_except_table43
- GCC_except_table57
- GCC_except_table59
- GCC_except_table60
- GCC_except_table66
- GCC_except_table70
- GCC_except_table71
- GCC_except_table82
- GCC_except_table89
- _LAUIPhysicalButtonNormalizedFrame
- _OBJC_CLASS_$_PKPhoneGlyphLayer
- _OBJC_IVAR_$_PKGlyphView._phoneAspectRatio
- _OBJC_IVAR_$_PKGlyphView._phoneLayer
- _OBJC_IVAR_$_PKGlyphView._userIntentArrowLayer
- _OBJC_IVAR_$_PKGlyphView._userIntentDeviceLayer
- _OBJC_IVAR_$_PKGlyphView._userIntentLayer
- _OBJC_IVAR_$_PKPhoneGlyphLayer._QRCodeColorFilter
- _OBJC_IVAR_$_PKPhoneGlyphLayer._QRCodeLayer
- _OBJC_IVAR_$_PKPhoneGlyphLayer._highlightLayer
- _OBJC_IVAR_$_PKPhoneGlyphLayer._highlightOffscreenPosition
- _OBJC_IVAR_$_PKPhoneGlyphLayer._highlightOnscreenPosition
- _OBJC_IVAR_$_PKPhoneGlyphLayer._phoneWiggleAnimationKey
- _OBJC_IVAR_$_PKPhoneGlyphLayer._primaryColor
- _OBJC_IVAR_$_PKPhoneGlyphLayer._showQRCode
- _OBJC_METACLASS_$_PKPhoneGlyphLayer
- __OBJC_$_INSTANCE_METHODS_PKPhoneGlyphLayer
- __OBJC_$_INSTANCE_VARIABLES_PKPhoneGlyphLayer
- __OBJC_$_PROP_LIST_PKPhoneGlyphLayer
- __OBJC_CLASS_RO_$_PKPhoneGlyphLayer
- __OBJC_METACLASS_RO_$_PKPhoneGlyphLayer
- ___35-[PKPhoneGlyphLayer setShowQRCode:]_block_invoke
- ___36-[PKPhoneGlyphLayer _endPhoneWiggle]_block_invoke
- ___38-[PKPhoneGlyphLayer _startPhoneWiggle]_block_invoke
- ___65-[PKAuthenticatorSharedRootContext _consumeWithCompletion:reset:]_block_invoke
CStrings:
+ "@\"CAAnimation\"32@?0@\"NSString\"8@\"NSValue\"16@\"NSValue\"24"
+ "PKAuthenticatorSharedRootContext (%{public}p): creating shared root with SpringBoard."
+ "Payment_glyph_D76"
+ "Payment_glyph_intent_phone-D76"
+ "Payment_glyph_intent_phone-D77"
+ "Payment_glyph_phone-D76"
+ "Payment_glyph_phone-D77"
+ "UserIntentPhysicalButtonNormalizedCGRect"
+ "v128@?0^{?=@@@@{?={?={?={CGPoint=dd}{CGPoint=dd}}ccd}{?=cd}{?={CGPoint=dd}{CGPoint=dd}}{?={CGPoint=dd}{CGPoint=dd}}}{CGSize=dd}{CGSize=dd}IIC}8I16{?={?={CGPoint=dd}{CGPoint=dd}}ccd}20{CGPoint=dd}68{CGPoint=dd}84{CGPoint=dd}100@\"NSURL\"116I124"
+ "v16@?0^{?=@@@@{?={?={?={CGPoint=dd}{CGPoint=dd}}ccd}{?=cd}{?={CGPoint=dd}{CGPoint=dd}}{?={CGPoint=dd}{CGPoint=dd}}}{CGSize=dd}{CGSize=dd}IIC}8"
+ "v16@?0^{?=@@@{?={?={?={CGPoint=dd}{CGPoint=dd}}ccd}{?=B{?=II}{?=II{?={CGPoint=dd}{CGPoint=dd}}}}}{CGSize=dd}IICC{CGRect={CGPoint=dd}{CGSize=dd}}}8"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa1"
- "\xf0\xf1"
```
