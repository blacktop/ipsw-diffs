## SiriUICore

> `/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore`

```diff

-3403.6.1.0.0
-  __TEXT.__text: 0x29ca0
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x2dd0
-  __TEXT.__const: 0x7f19a
-  __TEXT.__cstring: 0x8666
-  __TEXT.__oslogstring: 0xca1
-  __TEXT.__gcc_except_tab: 0x440
+3404.33.1.0.0
+  __TEXT.__text: 0x2a96c
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_methlist: 0x3390
+  __TEXT.__const: 0x7f182
+  __TEXT.__cstring: 0x8750
+  __TEXT.__oslogstring: 0xc81
+  __TEXT.__gcc_except_tab: 0x434
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0xb88
-  __TEXT.__objc_classname: 0x758
-  __TEXT.__objc_methname: 0x9204
-  __TEXT.__objc_methtype: 0x1c7c
-  __TEXT.__objc_stubs: 0x6d60
-  __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0xaf8
-  __DATA_CONST.__objc_classlist: 0x188
+  __TEXT.__constg_swiftt: 0x48
+  __TEXT.__swift5_typeref: 0x1c
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0xbc0
+  __TEXT.__objc_classname: 0x759
+  __TEXT.__objc_methname: 0x94b6
+  __TEXT.__objc_methtype: 0x1d12
+  __TEXT.__objc_stubs: 0x6f40
+  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__const: 0xaf0
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22b8
+  __DATA_CONST.__objc_selrefs: 0x2410
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x16c0
-  __AUTH_CONST.__objc_const: 0x9dc8
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__cfstring: 0x1700
+  __AUTH_CONST.__objc_const: 0x9530
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH.__objc_data: 0xaf0
+  __AUTH_CONST.__objc_doubleobj: 0x70
+  __AUTH.__objc_data: 0xba8
+  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x730
   __DATA.__data: 0x770
   __DATA.__bss: 0x110

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1099
-  Symbols:   1623
-  CStrings:  2392
+  Functions: 1126
+  Symbols:   1656
+  CStrings:  2429
 
Symbols:
+ _CGRectGetMaxY
+ _CGRectGetMinX
+ _CGRectOffset
+ _NSUnderlineColorAttributeName
+ _NSUnderlineStyleAttributeName
+ _OBJC_CLASS_$_AFSystemAssistantExperienceStatusManager
+ _OBJC_CLASS_$__TtC10SiriUICore26SUICStreamingLayoutManager
+ _OBJC_METACLASS_$_NSLayoutManager
+ _OBJC_METACLASS_$__TtC10SiriUICore26SUICStreamingLayoutManager
+ _objc_allocWithZone
+ _objc_opt_self
+ _swift_isaMask
+ _swift_lookUpClassMethod
- _AFDeviceSupportsSystemAssistantExperience
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "\x06\x11\x11!\x12\x12"
+ "\r\xf0\xf0\xf0\xf0\xa1"
+ "%s IntelligentLight reduced framerate is not supported"
+ "%s Siri Edge Light was set to a nil screen. Defaulting to backup values."
+ "-[SUICIntelligentLightLayer endReducedFramerateForPerformance]"
+ "@\"_TtC10SiriUICore26SUICStreamingLayoutManager\""
+ "@76@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{_NSRange=QQ}48@64B72"
+ "@max.wordLayer.frame.origin.y"
+ "@max.wordLayer.frame.size.height"
+ "EdgeLightFragment"
+ "EdgeLightFragment2"
+ "T{_NSRange=QQ},N,V_underlinedRange"
+ "_TtC10SiriUICore26SUICStreamingLayoutManager"
+ "_animateWordInSAE:displacement:"
+ "_calculateCornerRadiusRatio"
+ "_carouselWordOut:speed:displacement:"
+ "_carouselWordsToDelete"
+ "_createGlyphImage:glyphRange:layoutManager:isUnderlined:"
+ "_fullTextViewLayer"
+ "_renderByWord"
+ "_renderInFull"
+ "_renderPipeline2"
+ "_setShowEditTextImageWithoutRelayout:"
+ "_underlinedRange"
+ "addAttributes:range:"
+ "addLineToPoint:"
+ "colorWithAlphaComponent:"
+ "doubleValue"
+ "drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:"
+ "getBaseLocale:"
+ "isEqualToArray:"
+ "isSAEEnabled"
+ "moveOut"
+ "moveToPoint:"
+ "removeAttribute:range:"
+ "setLineCapStyle:"
+ "setLineDash:count:phase:"
+ "setUnderlinedRange:"
+ "setWords:showEditImage:useCarouselAnimation:"
+ "stroke"
+ "textContainerForGlyphAtIndex:effectiveRange:"
+ "underlineThickness"
+ "underlinedRange"
+ "updateLastWord"
+ "v112@0:8{_NSRange=QQ}16q32d40{CGRect={CGPoint=dd}{CGSize=dd}}48{_NSRange=QQ}80{CGPoint=dd}96"
+ "v32@0:8@16B24B28"
+ "v32@0:8@16d24"
+ "v40@0:8@16d24d32"
+ "valueForKeyPath:"
+ "{?=\"common\"{?=\"physicsRate\"Q\"maxPhysicsIterationsPerFrame\"i\"physicsTickDelta\"f\"framerateEnergyModifier\"f\"micPowerLevel\"f\"chipRandomOffset\"[33f]\"chipRotation\"f\"drawingVeryLastFrame\"B\"reduceMotion\"B}\"flameSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"onSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"volumeSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"glowSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"zoning\"Q\"isBuddy\"B\"slowAudioReactivity\"B\"energySpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"lightnessSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"flameDrawnSize\"f\"baseRotationSlowdownModifier\"f\"extraRotationSlowdownModifier\"f\"lights\"[11]}"
+ "{?=\"resolution\"\"yxRatio\"f\"screenRadiusRatio\"f\"falloffCoefficient\"f\"flameScale\" \"burstOpacity\" \"contrast\" }"
+ "\xb1"
+ "\xf0\xf0\xf0\xf0cT"
- "\x06\x11!\x12\x12"
- "\x0e\xf0\xf0\xf0\xf0\x81"
- "%s #edgeLight screen corner radius (%.2f) calculated: %f (%f unpadded), default was: %f"
- "%s Siri EdgeLight was set to a nil screen. Defaulting to backup values."
- "-[SUICEdgeLightMaskMetalLayer _calculateCornerRadiusRatio:]"
- "@\"NSLayoutManager\""
- "@72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{_NSRange=QQ}48@64"
- "EdgeLightBorder"
- "EdgeLightBorderRound"
- "EdgeLightBorderRound2"
- "_calculateCornerRadiusRatio:"
- "_createGlyphImage:glyphRange:layoutManager:"
- "_round2RenderPipeline"
- "_roundRenderPipeline"
- "_useRoundPipeline"
- "{?=\"common\"{?=\"physicsRate\"Q\"maxPhysicsIterationsPerFrame\"i\"physicsTickDelta\"f\"framerateEnergyModifier\"f\"micPowerLevel\"f\"chipRandomOffset\"[33f]\"chipRotation\"f\"drawingVeryLastFrame\"B\"reduceMotion\"B}\"flameSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"onSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"volumeSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"glowSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"zoning\"Q\"isBuddy\"B\"energySpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"lightnessSpring\"{?=\"value\"f\"curVelocity\"f\"maxAcceleration\"f\"springAmount\"f}\"flameDrawnSize\"f\"lights\"[11]}"
- "{?=\"resolution\"\"yxRatio\"f\"screenRadius\"f\"screenRadiusRound\"f\"falloffCoefficient\"f\"flameScale\" \"burstOpacity\" \"contrast\" }"
- "\x91"
- "\xf0\xf0\xf0\xf0Ct"

```
