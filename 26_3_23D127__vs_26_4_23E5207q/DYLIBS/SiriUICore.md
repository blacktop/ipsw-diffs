## SiriUICore

> `/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore`

```diff

-3515.3.1.0.0
-  __TEXT.__text: 0x2aba8
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x33d8
-  __TEXT.__const: 0x7f162
-  __TEXT.__cstring: 0x8780
-  __TEXT.__oslogstring: 0xcbc
-  __TEXT.__gcc_except_tab: 0x434
+3520.19.1.0.0
+  __TEXT.__text: 0x2c230
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x3448
+  __TEXT.__const: 0x7f172
+  __TEXT.__cstring: 0x8785
+  __TEXT.__oslogstring: 0xd3d
+  __TEXT.__gcc_except_tab: 0x440
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__ustring: 0xc
+  __TEXT.__ustring: 0x14
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x1c
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xbe8
-  __TEXT.__objc_classname: 0x75a
-  __TEXT.__objc_methname: 0x9613
-  __TEXT.__objc_methtype: 0x1d12
-  __TEXT.__objc_stubs: 0x7040
-  __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0xaa8
+  __TEXT.__unwind_info: 0xc60
+  __TEXT.__objc_classname: 0x78d
+  __TEXT.__objc_methname: 0x98a3
+  __TEXT.__objc_methtype: 0x1e3d
+  __TEXT.__objc_stubs: 0x72e0
+  __DATA_CONST.__got: 0x508
+  __DATA_CONST.__const: 0xa78
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2460
+  __DATA_CONST.__objc_selrefs: 0x24e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__const: 0x230
-  __AUTH_CONST.__cfstring: 0x1700
-  __AUTH_CONST.__objc_const: 0x95b0
+  __AUTH_CONST.__auth_got: 0x630
+  __AUTH_CONST.__const: 0x250
+  __AUTH_CONST.__cfstring: 0x1720
+  __AUTH_CONST.__objc_const: 0x9610
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0xba8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x73c
+  __DATA.__objc_ivar: 0x744
   __DATA.__data: 0x770
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x460

   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI
   - /System/Library/PrivateFrameworks/PhysicsKit.framework/PhysicsKit
   - /System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 553CDA8B-2D06-39B5-8363-6A9C8B2C81E8
-  Functions: 1130
-  Symbols:   4694
-  CStrings:  2612
+  UUID: 03A9EB80-A3FF-3B69-BA38-46F9F550B5C2
+  Functions: 1156
+  Symbols:   4760
+  CStrings:  2643
 
Symbols:
+ -[SUICEdgeLightMaskMetalLayer _commonInitWithScreen:commandQueue:].cold.2
+ -[SUICEdgeLightMaskMetalLayer setIntelligenctLightStatic:]
+ -[SUICEdgeLightMaskMetalLayer setIntelligentLightNoiseSpeedReducer:]
+ -[SUICIntelligentLightLayer _commonInitWithScreen:commandQueue:].cold.2
+ -[SUICOrbView _loadMetalPipelines].cold.2
+ -[SUICStreamingTextView _animateWordIn:displacement:delay:]
+ -[SUICStreamingTextView _animateWordInSAE:displacement:isUpdatingExistingAnimation:delay:]
+ -[SUICStreamingTextView _animateWordOut:delay:]
+ -[SUICStreamingTextView _carouselWordOut:speed:delay:displacement:]
+ -[SUICStreamingTextView _crossfadeAnimateWordIn:]
+ -[SUICStreamingTextView _wordHasInFlightAnimation:]
+ -[SUICStreamingTextView preferredLeadingIconBundleIdentifier]
+ -[SUICStreamingTextView setPreferredLeadingIconBundleIdentifier:]
+ -[SUICStreamingTextView setWords:showEditImage:useCarouselAnimation:preferredLeadingIconBundleIdentifier:]
+ -[_SUICStreamingWord createWordLayer]
+ -[_SUICStreamingWord glyphWidthInWordX]
+ -[_SUICStreamingWord setGlyphWidthInWordX:]
+ GCC_except_table64
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_IVAR_$_SUICStreamingTextView._preferredLeadingIconBundleIdentifier
+ _OBJC_IVAR_$__SUICStreamingWord._glyphWidthInWordX
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ ___39-[SUICStreamingTextView _animateLayers]_block_invoke_2
+ _objc_msgSend$_animateWordIn:displacement:delay:
+ _objc_msgSend$_animateWordInSAE:displacement:isUpdatingExistingAnimation:delay:
+ _objc_msgSend$_animateWordOut:delay:
+ _objc_msgSend$_carouselWordOut:speed:delay:displacement:
+ _objc_msgSend$_crossfadeAnimateWordIn:
+ _objc_msgSend$_wordHasInFlightAnimation:
+ _objc_msgSend$addLineToPoint:
+ _objc_msgSend$animationForKey:
+ _objc_msgSend$capHeight
+ _objc_msgSend$createWordLayer
+ _objc_msgSend$floatValue
+ _objc_msgSend$fromValue
+ _objc_msgSend$glyphWidthInWordX
+ _objc_msgSend$init
+ _objc_msgSend$initWithBundleIdentifier:
+ _objc_msgSend$initWithCGImage:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$moveToPoint:
+ _objc_msgSend$pointSize
+ _objc_msgSend$preferredLeadingIconBundleIdentifier
+ _objc_msgSend$prepareImageForDescriptor:
+ _objc_msgSend$setGlyphWidthInWordX:
+ _objc_msgSend$setLineCapStyle:
+ _objc_msgSend$setLineDash:count:phase:
+ _objc_msgSend$stroke
+ _objc_msgSend$textContainerForGlyphAtIndex:effectiveRange:
+ _objc_retain_x28
- -[SUICStreamingTextView _animateWordIn:]
- -[SUICStreamingTextView _animateWordInSAE:displacement:]
- -[SUICStreamingTextView _animateWordOut:]
- -[SUICStreamingTextView _carouselWordOut:speed:displacement:]
- -[_SUICStreamingWord setWordLayer:]
- GCC_except_table58
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_SiriUICore
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_SiriUICore
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_SiriUICore
- __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftCoreLocation_$_SiriUICore
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMIDI_$_SiriUICore
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SiriUICore
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_animateWordIn:
- _objc_msgSend$_animateWordInSAE:displacement:
- _objc_msgSend$_animateWordOut:
- _objc_msgSend$_carouselWordOut:speed:displacement:
- _objc_msgSend$setWordLayer:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "\r\xf0\xf0\xf0\xf0\xc1"
+ "%s #edgeLight: setIntelligentLightNoiseSpeedReducer:%f"
+ "%s #edgeLight: setIntelligentLightToStatic:%d"
+ "%s siri_signpost_begin `%s`"
+ "-[SUICEdgeLightMaskMetalLayer setIntelligenctLightStatic:]"
+ "-[SUICEdgeLightMaskMetalLayer setIntelligentLightNoiseSpeedReducer:]"
+ "B40@0:8q16q24@\"SUICProgressIndicatorViewController\"32"
+ "B40@0:8q16q24@32"
+ "T@\"CALayer\",R,N,V_wordLayer"
+ "T@\"NSString\",&,N,V_preferredLeadingIconBundleIdentifier"
+ "Td,N,V_glyphWidthInWordX"
+ "Tq,R"
+ "_animateWordIn:displacement:delay:"
+ "_animateWordInSAE:displacement:isUpdatingExistingAnimation:delay:"
+ "_animateWordOut:delay:"
+ "_carouselWordOut:speed:delay:displacement:"
+ "_crossfadeAnimateWordIn:"
+ "_glyphWidthInWordX"
+ "_preferredLeadingIconBundleIdentifier"
+ "_wordHasInFlightAnimation:"
+ "animationForKey:"
+ "capHeight"
+ "createWordLayer"
+ "floatValue"
+ "fromValue"
+ "glyphWidthInWordX"
+ "initWithBundleIdentifier:"
+ "initWithCGImage:"
+ "pointSize"
+ "preferredLeadingIconBundleIdentifier"
+ "prepareImageForDescriptor:"
+ "setGlyphWidthInWordX:"
+ "setIntelligenctLightStatic:"
+ "setIntelligentLightNoiseSpeedReducer:"
+ "setPreferredLeadingIconBundleIdentifier:"
+ "setWords:showEditImage:useCarouselAnimation:preferredLeadingIconBundleIdentifier:"
+ "v32@0:8@\"SUICProgressStateMachine\"16q24"
+ "v32@0:8@16q24"
+ "v40@0:8@16B24B28@32"
+ "v44@0:8@16d24B32d36"
+ "v48@0:8@\"SUICProgressStateMachine\"16q24q32q40"
+ "v48@0:8@16d24d32d40"
+ "v48@0:8@16q24q32q40"
+ "{?=\"common\"{?=\"physicsRate\"Q\"maxPhysicsIterationsPerFrame\"i\"physicsTickDelta\"f\"framerateEnergyModifier\"f\"micPowerLevel\"f\"chipRandomOffset\"[33f]\"chipRotation\"f\"drawingVeryLastFrame\"B\"reduceMotion\"B}\"flameSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"onSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"volumeSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"glowSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"noiseSpeedReducerSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"zoning\"Q\"isBuddy\"B\"slowAudioReactivity\"B\"energySpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"lightnessSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"noiseSpeedReducer\"f\"flameDrawnSize\"f\"baseRotationSlowdownModifier\"f\"extraRotationSlowdownModifier\"f\"lights\"[11]}"
+ "{?=\"resolution\"\"yxRatio\"f\"screenRadiusRatio\"f\"falloffCoefficient\"f\"flameScale\" \"flameScaleDucked\" \"burstOpacity\" \"contrast\" }"
+ "\u00a0\u00a0\u00a0"
- "\r\xf0\xf0\xf0\xf0\x91"
- "B40@0:8Q16Q24@\"SUICProgressIndicatorViewController\"32"
- "B40@0:8Q16Q24@32"
- "T@\"CALayer\",&,N,V_wordLayer"
- "_animateWordIn:"
- "_animateWordInSAE:displacement:"
- "_animateWordOut:"
- "_carouselWordOut:speed:displacement:"
- "setWordLayer:"
- "v32@0:8@\"SUICProgressStateMachine\"16Q24"
- "v48@0:8@\"SUICProgressStateMachine\"16Q24Q32Q40"
- "v48@0:8@16Q24Q32Q40"
- "{?=\"common\"{?=\"physicsRate\"Q\"maxPhysicsIterationsPerFrame\"i\"physicsTickDelta\"f\"framerateEnergyModifier\"f\"micPowerLevel\"f\"chipRandomOffset\"[33f]\"chipRotation\"f\"drawingVeryLastFrame\"B\"reduceMotion\"B}\"flameSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"onSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"volumeSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"glowSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"zoning\"Q\"isBuddy\"B\"slowAudioReactivity\"B\"energySpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"lightnessSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"flameDrawnSize\"f\"baseRotationSlowdownModifier\"f\"extraRotationSlowdownModifier\"f\"lights\"[11]}"
- "{?=\"resolution\"\"yxRatio\"f\"screenRadiusRatio\"f\"falloffCoefficient\"f\"flameScale\" \"burstOpacity\" \"contrast\" }"

```
