## UnityPoster

> `/System/Library/PrivateFrameworks/UnityPoster.framework/UnityPoster`

```diff

-46.0.0.0.0
-  __TEXT.__text: 0x3eb0
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x438
+47.0.0.0.0
+  __TEXT.__text: 0x44a0
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_methlist: 0x5ec
   __TEXT.__const: 0x3d0
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__cstring: 0x74
-  __TEXT.__unwind_info: 0x174
-  __TEXT.__objc_classname: 0x63
-  __TEXT.__objc_methname: 0x13d7
-  __TEXT.__objc_methtype: 0x33a
-  __TEXT.__objc_stubs: 0xa80
+  __TEXT.__cstring: 0x66
+  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__objc_classname: 0xb9
+  __TEXT.__objc_methname: 0x1826
+  __TEXT.__objc_methtype: 0x365
+  __TEXT.__objc_stubs: 0xba0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x48
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x978
-  __DATA_CONST.__objc_selrefs: 0x468
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_const: 0x1b0
+  __DATA_CONST.__objc_const: 0xd48
+  __DATA_CONST.__objc_selrefs: 0x520
+  __AUTH_CONST.__objc_const: 0x2d0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__auth_got: 0x198
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x1a0
+  __AUTH.__objc_data: 0x140
   __DATA.__objc_classrefs: 0x70
-  __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_superrefs: 0x30
+  __DATA.__objc_ivar: 0xf0
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7E84B78-2A2F-302D-99C9-56BB4044770F
-  Functions: 120
-  Symbols:   461
-  CStrings:  279
+  UUID: 6A19DF6A-9F8D-30E3-9B7C-1D239FE2E94F
+  Functions: 156
+  Symbols:   585
+  CStrings:  328
 
Symbols:
+ -[UPQuiltConfiguration initRandomizer]
+ -[UPQuiltConfiguration randomizer]
+ -[UPQuiltConfiguration setIsSnapshotConfiguration:]
+ -[UPQuiltConfiguration setLineVariance:]
+ -[UPQuiltConfiguration setRandomizationSeedValue:]
+ -[UPQuiltConfiguration setRandomizer:]
+ -[UPQuiltConfiguration setTimeBounds:]
+ -[UPQuiltConfiguration setViewport:]
+ -[UPQuiltConfigurationPad .cxx_destruct]
+ -[UPQuiltConfigurationPad _generateQuiltPaths]
+ -[UPQuiltConfigurationPad bottomQuiltLockedPath]
+ -[UPQuiltConfigurationPad bottomQuiltUnlockedPath]
+ -[UPQuiltConfigurationPad bottomRightQuiltUnlockedPath]
+ -[UPQuiltConfigurationPad initWithRandomizationSeedValue:viewport:timeBounds:lineVariance:]
+ -[UPQuiltConfigurationPad intersectionPieceLockedPath]
+ -[UPQuiltConfigurationPad leftQuiltLockedPath]
+ -[UPQuiltConfigurationPad leftQuiltUnlockedPath]
+ -[UPQuiltConfigurationPad rightQuiltLockedPath]
+ -[UPQuiltConfigurationPad rightQuiltUnlockedPath]
+ -[UPQuiltConfigurationPad setBottomQuiltLockedPath:]
+ -[UPQuiltConfigurationPad setBottomQuiltUnlockedPath:]
+ -[UPQuiltConfigurationPad setBottomRightQuiltUnlockedPath:]
+ -[UPQuiltConfigurationPad setIntersectionPieceLockedPath:]
+ -[UPQuiltConfigurationPad setLeftQuiltLockedPath:]
+ -[UPQuiltConfigurationPad setLeftQuiltUnlockedPath:]
+ -[UPQuiltConfigurationPad setRightQuiltLockedPath:]
+ -[UPQuiltConfigurationPad setRightQuiltUnlockedPath:]
+ -[UPQuiltConfigurationPad setTopQuiltLockedPath:]
+ -[UPQuiltConfigurationPad setTopQuiltUnlockedPath:]
+ -[UPQuiltConfigurationPad topQuiltLockedPath]
+ -[UPQuiltConfigurationPad topQuiltUnlockedPath]
+ -[UPQuiltConfigurationPhone .cxx_destruct]
+ -[UPQuiltConfigurationPhone _generateQuiltPaths]
+ -[UPQuiltConfigurationPhone _quiltVariationValuesForSideLength:variance:fromKeyFraction:toKeyFraction:]
+ -[UPQuiltConfigurationPhone bottomLeftQuiltAsleepPath]
+ -[UPQuiltConfigurationPhone bottomLeftQuiltAwakeLockedPath]
+ -[UPQuiltConfigurationPhone bottomLeftQuiltUnlockedPath]
+ -[UPQuiltConfigurationPhone bottomRightQuiltAwakeLockedPath]
+ -[UPQuiltConfigurationPhone bottomRightQuiltUnlockedPath]
+ -[UPQuiltConfigurationPhone initWithRandomizationSeedValue:viewport:timeBounds:lineVariance:]
+ -[UPQuiltConfigurationPhone intersectionPieceAwakeLockedPath]
+ -[UPQuiltConfigurationPhone setBottomLeftQuiltAsleepPath:]
+ -[UPQuiltConfigurationPhone setBottomLeftQuiltAwakeLockedPath:]
+ -[UPQuiltConfigurationPhone setBottomLeftQuiltUnlockedPath:]
+ -[UPQuiltConfigurationPhone setBottomRightQuiltAwakeLockedPath:]
+ -[UPQuiltConfigurationPhone setBottomRightQuiltUnlockedPath:]
+ -[UPQuiltConfigurationPhone setIntersectionPieceAwakeLockedPath:]
+ -[UPQuiltConfigurationPhone setTopQuiltAsleepPath:]
+ -[UPQuiltConfigurationPhone setTopQuiltAwakeLockedPath:]
+ -[UPQuiltConfigurationPhone setTopQuiltUnlockedPath:]
+ -[UPQuiltConfigurationPhone topQuiltAsleepPath]
+ -[UPQuiltConfigurationPhone topQuiltAwakeLockedPath]
+ -[UPQuiltConfigurationPhone topQuiltUnlockedPath]
+ -[UPQuiltView setTimeRect:]
+ -[UPQuiltView timeRect]
+ -[UPQuiltViewPad .cxx_destruct]
+ -[UPQuiltViewPad description]
+ -[UPQuiltViewPad getOffsetForDeviceInterfaceOrientation:]
+ -[UPQuiltViewPad identifier]
+ -[UPQuiltViewPad initWithFrame:identifier:]
+ -[UPQuiltViewPad originTranslationValueForLandscapeMode]
+ -[UPQuiltViewPad originTranslationValueForPortraitMode]
+ -[UPQuiltViewPad scaleValueForLandscapeMode]
+ -[UPQuiltViewPad setIdentifier:]
+ -[UPQuiltViewPad setupLayerForIdentifier:]
+ -[UPQuiltViewPad updateQuiltsWithIdentifier:deviceInterfaceOrientation:unlockProgress:]
+ -[UPQuiltViewPhone .cxx_destruct]
+ -[UPQuiltViewPhone bottomLeftQuiltColor]
+ -[UPQuiltViewPhone bottomLeftQuiltPathRef]
+ -[UPQuiltViewPhone bottomLeftQuiltPieceLayer]
+ -[UPQuiltViewPhone bottomRightQuiltColor]
+ -[UPQuiltViewPhone bottomRightQuiltPathRef]
+ -[UPQuiltViewPhone bottomRightQuiltPieceLayer]
+ -[UPQuiltViewPhone cleanupQuiltPaths]
+ -[UPQuiltViewPhone configuration]
+ -[UPQuiltViewPhone dealloc]
+ -[UPQuiltViewPhone description]
+ -[UPQuiltViewPhone initWithFrame:]
+ -[UPQuiltViewPhone intersectionPieceColor]
+ -[UPQuiltViewPhone intersectionPiecePathRef]
+ -[UPQuiltViewPhone layoutSubviews]
+ -[UPQuiltViewPhone setBottomLeftQuiltColor:]
+ -[UPQuiltViewPhone setBottomLeftQuiltPieceLayer:]
+ -[UPQuiltViewPhone setBottomRightQuiltColor:]
+ -[UPQuiltViewPhone setBottomRightQuiltPieceLayer:]
+ -[UPQuiltViewPhone setColors]
+ -[UPQuiltViewPhone setConfiguration:]
+ -[UPQuiltViewPhone setIntersectionPieceColor:]
+ -[UPQuiltViewPhone setTopQuiltColor:]
+ -[UPQuiltViewPhone setTopQuiltPieceLayer:]
+ -[UPQuiltViewPhone topQuiltColor]
+ -[UPQuiltViewPhone topQuiltPathRef]
+ -[UPQuiltViewPhone topQuiltPieceLayer]
+ -[UPQuiltViewPhone updateQuiltsWithUnlockProgress:wakeProgress:]
+ _OBJC_CLASS_$_UPQuiltConfigurationPad
+ _OBJC_CLASS_$_UPQuiltConfigurationPhone
+ _OBJC_CLASS_$_UPQuiltViewPad
+ _OBJC_CLASS_$_UPQuiltViewPhone
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._bottomQuiltLockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._bottomQuiltUnlockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._bottomRightQuiltUnlockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._fromInterpolatedConfiguration
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._intersectionPieceLockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._leftQuiltLockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._leftQuiltUnlockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._rightQuiltLockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._rightQuiltUnlockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._toInterpolatedConfiguration
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._topQuiltLockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPad._topQuiltUnlockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._bottomLeftQuiltAsleepPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._bottomLeftQuiltAwakeLockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._bottomLeftQuiltUnlockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._bottomRightQuiltAwakeLockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._bottomRightQuiltUnlockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._fromInterpolatedConfiguration
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._intersectionPieceAwakeLockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._toInterpolatedConfiguration
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._topQuiltAsleepPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._topQuiltAwakeLockedPath
+ _OBJC_IVAR_$_UPQuiltConfigurationPhone._topQuiltUnlockedPath
+ _OBJC_IVAR_$_UPQuiltView._timeRect
+ _OBJC_IVAR_$_UPQuiltViewPad._heightRatioToHero
+ _OBJC_IVAR_$_UPQuiltViewPad._identifier
+ _OBJC_IVAR_$_UPQuiltViewPad._originalFrame
+ _OBJC_IVAR_$_UPQuiltViewPad._quiltImageLayer
+ _OBJC_IVAR_$_UPQuiltViewPad._transitionLayer
+ _OBJC_IVAR_$_UPQuiltViewPad._widthRatioToHero
+ _OBJC_IVAR_$_UPQuiltViewPhone._bottomLeftQuiltColor
+ _OBJC_IVAR_$_UPQuiltViewPhone._bottomLeftQuiltPieceLayer
+ _OBJC_IVAR_$_UPQuiltViewPhone._bottomLeftQuiltPieceTargetPathRef
+ _OBJC_IVAR_$_UPQuiltViewPhone._bottomRightQuiltColor
+ _OBJC_IVAR_$_UPQuiltViewPhone._bottomRightQuiltPieceLayer
+ _OBJC_IVAR_$_UPQuiltViewPhone._configuration
+ _OBJC_IVAR_$_UPQuiltViewPhone._intersectionPieceColor
+ _OBJC_IVAR_$_UPQuiltViewPhone._intersectionPieceLayer
+ _OBJC_IVAR_$_UPQuiltViewPhone._intersectionPieceTargetPathRef
+ _OBJC_IVAR_$_UPQuiltViewPhone._thirdPieceTargetPathRef
+ _OBJC_IVAR_$_UPQuiltViewPhone._topQuiltColor
+ _OBJC_IVAR_$_UPQuiltViewPhone._topQuiltPieceLayer
+ _OBJC_IVAR_$_UPQuiltViewPhone._topQuiltPieceTargetPathRef
+ _OBJC_METACLASS_$_UPQuiltConfigurationPad
+ _OBJC_METACLASS_$_UPQuiltConfigurationPhone
+ _OBJC_METACLASS_$_UPQuiltViewPad
+ _OBJC_METACLASS_$_UPQuiltViewPhone
+ __OBJC_$_INSTANCE_METHODS_UPQuiltConfigurationPad
+ __OBJC_$_INSTANCE_METHODS_UPQuiltConfigurationPhone
+ __OBJC_$_INSTANCE_METHODS_UPQuiltViewPad
+ __OBJC_$_INSTANCE_METHODS_UPQuiltViewPhone
+ __OBJC_$_INSTANCE_VARIABLES_UPQuiltConfigurationPad
+ __OBJC_$_INSTANCE_VARIABLES_UPQuiltConfigurationPhone
+ __OBJC_$_INSTANCE_VARIABLES_UPQuiltViewPad
+ __OBJC_$_INSTANCE_VARIABLES_UPQuiltViewPhone
+ __OBJC_$_PROP_LIST_UPQuiltConfigurationPad
+ __OBJC_$_PROP_LIST_UPQuiltConfigurationPhone
+ __OBJC_$_PROP_LIST_UPQuiltViewPad
+ __OBJC_$_PROP_LIST_UPQuiltViewPhone
+ __OBJC_CLASS_RO_$_UPQuiltConfigurationPad
+ __OBJC_CLASS_RO_$_UPQuiltConfigurationPhone
+ __OBJC_CLASS_RO_$_UPQuiltViewPad
+ __OBJC_CLASS_RO_$_UPQuiltViewPhone
+ __OBJC_METACLASS_RO_$_UPQuiltConfigurationPad
+ __OBJC_METACLASS_RO_$_UPQuiltConfigurationPhone
+ __OBJC_METACLASS_RO_$_UPQuiltViewPad
+ __OBJC_METACLASS_RO_$_UPQuiltViewPhone
+ _objc_msgSend$randomizationSeedValue
+ _objc_msgSend$randomizer
+ _objc_msgSend$setLineVariance:
+ _objc_msgSend$setRandomizationSeedValue:
+ _objc_msgSend$setRandomizer:
+ _objc_msgSend$setTimeBounds:
+ _objc_msgSend$setViewport:
+ _objc_msgSend$timeBounds
+ _objc_msgSend$timeRect
+ _objc_msgSend$viewport
+ _objc_release_x9
- -[UPQuiltConfiguration _generateQuiltPaths]
- -[UPQuiltConfiguration _quiltVariationValuesForSideLength:variance:fromKeyFraction:toKeyFraction:]
- -[UPQuiltConfiguration bottomLeftQuiltAsleepPath]
- -[UPQuiltConfiguration bottomLeftQuiltAwakeLockedPath]
- -[UPQuiltConfiguration bottomLeftQuiltUnlockedPath]
- -[UPQuiltConfiguration bottomRightQuiltAwakeLockedPath]
- -[UPQuiltConfiguration bottomRightQuiltUnlockedPath]
- -[UPQuiltConfiguration intersectionPieceAwakeLockedPath]
- -[UPQuiltConfiguration setBottomLeftQuiltAsleepPath:]
- -[UPQuiltConfiguration setBottomLeftQuiltAwakeLockedPath:]
- -[UPQuiltConfiguration setBottomLeftQuiltUnlockedPath:]
- -[UPQuiltConfiguration setBottomRightQuiltAwakeLockedPath:]
- -[UPQuiltConfiguration setBottomRightQuiltUnlockedPath:]
- -[UPQuiltConfiguration setIntersectionPieceAwakeLockedPath:]
- -[UPQuiltConfiguration setTopQuiltAsleepPath:]
- -[UPQuiltConfiguration setTopQuiltAwakeLockedPath:]
- -[UPQuiltConfiguration setTopQuiltUnlockedPath:]
- -[UPQuiltConfiguration topQuiltAsleepPath]
- -[UPQuiltConfiguration topQuiltAwakeLockedPath]
- -[UPQuiltConfiguration topQuiltUnlockedPath]
- -[UPQuiltView bottomLeftQuiltColor]
- -[UPQuiltView bottomLeftQuiltPathRef]
- -[UPQuiltView bottomLeftQuiltPieceLayer]
- -[UPQuiltView bottomRightQuiltColor]
- -[UPQuiltView bottomRightQuiltPathRef]
- -[UPQuiltView bottomRightQuiltPieceLayer]
- -[UPQuiltView cleanupQuiltPaths]
- -[UPQuiltView configuration]
- -[UPQuiltView dealloc]
- -[UPQuiltView description]
- -[UPQuiltView getOffsetForDeviceInterfaceOrientation:]
- -[UPQuiltView identifier]
- -[UPQuiltView initWithFrame:]
- -[UPQuiltView initWithFrame:identifier:]
- -[UPQuiltView intersectionPieceColor]
- -[UPQuiltView intersectionPiecePathRef]
- -[UPQuiltView layoutSubviews]
- -[UPQuiltView originTranslationValueForLandscapeMode]
- -[UPQuiltView originTranslationValueForPortraitMode]
- -[UPQuiltView scaleValueForLandscapeMode]
- -[UPQuiltView setBottomLeftQuiltColor:]
- -[UPQuiltView setBottomLeftQuiltPieceLayer:]
- -[UPQuiltView setBottomRightQuiltColor:]
- -[UPQuiltView setBottomRightQuiltPieceLayer:]
- -[UPQuiltView setColors]
- -[UPQuiltView setConfiguration:]
- -[UPQuiltView setIdentifier:]
- -[UPQuiltView setIntersectionPieceColor:]
- -[UPQuiltView setTimeView:]
- -[UPQuiltView setTopQuiltColor:]
- -[UPQuiltView setTopQuiltPieceLayer:]
- -[UPQuiltView setupLayerForIdentifier:]
- -[UPQuiltView timeView]
- -[UPQuiltView topQuiltColor]
- -[UPQuiltView topQuiltPathRef]
- -[UPQuiltView topQuiltPieceLayer]
- -[UPQuiltView updateQuiltsWithIdentifier:deviceInterfaceOrientation:unlockProgress:]
- -[UPQuiltView updateQuiltsWithUnlockProgress:wakeProgress:]
- _OBJC_IVAR_$_UPQuiltConfiguration._bottomLeftQuiltAsleepPath
- _OBJC_IVAR_$_UPQuiltConfiguration._bottomLeftQuiltAwakeLockedPath
- _OBJC_IVAR_$_UPQuiltConfiguration._bottomLeftQuiltUnlockedPath
- _OBJC_IVAR_$_UPQuiltConfiguration._bottomRightQuiltAwakeLockedPath
- _OBJC_IVAR_$_UPQuiltConfiguration._bottomRightQuiltUnlockedPath
- _OBJC_IVAR_$_UPQuiltConfiguration._fromInterpolatedConfiguration
- _OBJC_IVAR_$_UPQuiltConfiguration._intersectionPieceAwakeLockedPath
- _OBJC_IVAR_$_UPQuiltConfiguration._toInterpolatedConfiguration
- _OBJC_IVAR_$_UPQuiltConfiguration._topQuiltAsleepPath
- _OBJC_IVAR_$_UPQuiltConfiguration._topQuiltAwakeLockedPath
- _OBJC_IVAR_$_UPQuiltConfiguration._topQuiltUnlockedPath
- _OBJC_IVAR_$_UPQuiltView._bottomLeftQuiltColor
- _OBJC_IVAR_$_UPQuiltView._bottomLeftQuiltPieceLayer
- _OBJC_IVAR_$_UPQuiltView._bottomLeftQuiltPieceTargetPathRef
- _OBJC_IVAR_$_UPQuiltView._bottomRightQuiltColor
- _OBJC_IVAR_$_UPQuiltView._bottomRightQuiltPieceLayer
- _OBJC_IVAR_$_UPQuiltView._configuration
- _OBJC_IVAR_$_UPQuiltView._heightRatioToHero
- _OBJC_IVAR_$_UPQuiltView._identifier
- _OBJC_IVAR_$_UPQuiltView._intersectionPieceColor
- _OBJC_IVAR_$_UPQuiltView._intersectionPieceLayer
- _OBJC_IVAR_$_UPQuiltView._intersectionPieceTargetPathRef
- _OBJC_IVAR_$_UPQuiltView._thirdPieceTargetPathRef
- _OBJC_IVAR_$_UPQuiltView._timeView
- _OBJC_IVAR_$_UPQuiltView._topQuiltColor
- _OBJC_IVAR_$_UPQuiltView._topQuiltPieceLayer
- _OBJC_IVAR_$_UPQuiltView._topQuiltPieceTargetPathRef
- _OBJC_IVAR_$_UPQuiltView._transitionLayer
- _OBJC_IVAR_$_UPQuiltView._widthRatioToHero
- _objc_msgSend$timeView
CStrings:
+ "\x01\x11\x11\x11\x15"
+ "\x02a"
+ "\v"
+ "\f"
+ "\x11"
+ "!"
+ "@\"UPQuiltConfigurationPad\""
+ "@\"UPQuiltConfigurationPhone\""
+ "T@\"UIBezierPath\",&,N,V_bottomQuiltLockedPath"
+ "T@\"UIBezierPath\",&,N,V_bottomQuiltUnlockedPath"
+ "T@\"UIBezierPath\",&,N,V_intersectionPieceLockedPath"
+ "T@\"UIBezierPath\",&,N,V_leftQuiltLockedPath"
+ "T@\"UIBezierPath\",&,N,V_leftQuiltUnlockedPath"
+ "T@\"UIBezierPath\",&,N,V_rightQuiltLockedPath"
+ "T@\"UIBezierPath\",&,N,V_rightQuiltUnlockedPath"
+ "T@\"UIBezierPath\",&,N,V_topQuiltLockedPath"
+ "T@\"UPQuiltConfigurationPhone\",&,N,V_configuration"
+ "T@\"UPSeededRandomizer\",&,N,V_randomizer"
+ "TB,N,V_isSnapshotConfiguration"
+ "TQ,N,V_randomizationSeedValue"
+ "Td,N,V_lineVariance"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_timeBounds"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_timeRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_viewport"
+ "UPQuilt = memory:%p"
+ "UPQuiltConfigurationPad"
+ "UPQuiltConfigurationPhone"
+ "UPQuiltViewPad"
+ "UPQuiltViewPhone"
+ "_bottomQuiltLockedPath"
+ "_bottomQuiltUnlockedPath"
+ "_intersectionPieceLockedPath"
+ "_leftQuiltLockedPath"
+ "_leftQuiltUnlockedPath"
+ "_rightQuiltLockedPath"
+ "_rightQuiltUnlockedPath"
+ "_timeRect"
+ "_topQuiltLockedPath"
+ "bottomQuiltLockedPath"
+ "bottomQuiltUnlockedPath"
+ "intersectionPieceLockedPath"
+ "leftQuiltLockedPath"
+ "leftQuiltUnlockedPath"
+ "randomizer"
+ "rightQuiltLockedPath"
+ "rightQuiltUnlockedPath"
+ "setBottomQuiltLockedPath:"
+ "setBottomQuiltUnlockedPath:"
+ "setIntersectionPieceLockedPath:"
+ "setIsSnapshotConfiguration:"
+ "setLeftQuiltLockedPath:"
+ "setLeftQuiltUnlockedPath:"
+ "setLineVariance:"
+ "setRandomizationSeedValue:"
+ "setRandomizer:"
+ "setRightQuiltLockedPath:"
+ "setRightQuiltUnlockedPath:"
+ "setTimeBounds:"
+ "setTimeRect:"
+ "setTopQuiltLockedPath:"
+ "setViewport:"
+ "timeRect"
+ "topQuiltLockedPath"
+ "v24@0:8d16"
- "\x02a\x11\x11\x116"
- "\x039"
- "@\"UPQuiltConfiguration\""
- "T@\"UPQuiltConfiguration\",&,N,V_configuration"
- "TB,R,N,V_isSnapshotConfiguration"
- "TQ,R,N,V_randomizationSeedValue"
- "Td,R,N,V_lineVariance"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_timeView"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_timeBounds"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_viewport"
- "UPQuilt = memory:%p identifier:%@"
- "_timeView"
- "setTimeView:"
- "timeView"
- "\xf0!"

```
