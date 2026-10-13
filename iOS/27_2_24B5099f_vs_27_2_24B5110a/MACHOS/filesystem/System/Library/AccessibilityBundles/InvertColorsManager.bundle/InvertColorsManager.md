## InvertColorsManager

> `System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA.__data`

```diff

-3245.8.4.2.0
-  __TEXT.__text: 0x1fc5c
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x28c0
-  __TEXT.__objc_methlist: 0x779c
-  __TEXT.__const: 0xd0
+3245.8.9.0.0
+  __TEXT.__text: 0x211e0
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x2a80
+  __TEXT.__objc_methlist: 0x783c
+  __TEXT.__const: 0xe0
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__gcc_except_tab: 0x1d8
-  __TEXT.__objc_classname: 0xa17e
-  __TEXT.__cstring: 0x8cc4
-  __TEXT.__objc_methname: 0x2cfb
-  __TEXT.__objc_methtype: 0x334
-  __TEXT.__oslogstring: 0xdb4
-  __TEXT.__unwind_info: 0x11c8
-  __DATA_CONST.__const: 0x818
-  __DATA_CONST.__cfstring: 0x8d00
-  __DATA_CONST.__objc_classlist: 0x1aa8
+  __TEXT.__gcc_except_tab: 0x200
+  __TEXT.__objc_classname: 0xa264
+  __TEXT.__cstring: 0x8ebf
+  __TEXT.__objc_methname: 0x2ea7
+  __TEXT.__objc_methtype: 0x357
+  __TEXT.__oslogstring: 0xfa9
+  __TEXT.__unwind_info: 0x1230
+  __DATA_CONST.__const: 0x930
+  __DATA_CONST.__cfstring: 0x8f40
+  __DATA_CONST.__objc_classlist: 0x1ac8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x600
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0x190
-  __DATA.__objc_const: 0x214c8
-  __DATA.__objc_selrefs: 0xe40
-  __DATA.__objc_data: 0x10a90
+  __DATA_CONST.__objc_superrefs: 0x610
+  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0x1a0
+  __DATA.__objc_const: 0x21708
+  __DATA.__objc_selrefs: 0xeb8
+  __DATA.__objc_data: 0x10bd0
   __DATA.__data: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1917
-  Symbols:   1893
-  CStrings:  2142
+  Functions: 1939
+  Symbols:   1906
+  CStrings:  2186
 
Symbols:
+ _OBJC_CLASS_$_AXDispatchTimer
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_SBFLegacyWallpaperWakeAnimatorInvertColorsAccessibility
+ _OBJC_CLASS_$_SBTraitsSingleSceneWindowInvertColorsAccessibility
+ _OBJC_CLASS_$_UIWindowScene
+ _OBJC_CLASS_$___SBFLegacyWallpaperWakeAnimatorInvertColorsAccessibility_super
+ _OBJC_CLASS_$___SBTraitsSingleSceneWindowInvertColorsAccessibility_super
+ _OBJC_METACLASS_$_SBFLegacyWallpaperWakeAnimatorInvertColorsAccessibility
+ _OBJC_METACLASS_$_SBTraitsSingleSceneWindowInvertColorsAccessibility
+ _OBJC_METACLASS_$___SBFLegacyWallpaperWakeAnimatorInvertColorsAccessibility_super
+ _OBJC_METACLASS_$___SBTraitsSingleSceneWindowInvertColorsAccessibility_super
+ _objc_release_x9
+ _objc_retain_x4
CStrings:
+ "AXInvertColorsManager.trailingStatusChange"
+ "AXInvertColors_CoverSheet.backgroundStyleDebounce"
+ "AXWakeEffectToken"
+ "B16@?0#8"
+ "BackgroundStyleDebounceTimer"
+ "CoverSheet: non-dark backgroundStyle %ld observed, debouncing before un-ignoring invert colors"
+ "CoverSheet: wake effect layer %@, dark mode: %d, invert: %d"
+ "FBScene"
+ "FBSceneClientHandle"
+ "IC status change too soon, deferring"
+ "PBUIPosterFloatingLayerReplica"
+ "PBUIPosterWallpaperRemoteViewController appeared, re-evaluating dark window invert for %@"
+ "SBFLegacyWallpaperWakeAnimatorInvertColorsAccessibility"
+ "SBHomeScreenWindow"
+ "SBStatusBarWindow"
+ "SBTraitsOrientedContentViewControllerView"
+ "SBTraitsSingleSceneWindow"
+ "SBTraitsSingleSceneWindow: hosting Siri AI, no dark mode window filter: %@"
+ "SBTraitsSingleSceneWindowInvertColorsAccessibility"
+ "WakeAnimator: %{public}@ invert on %lu floating layer replica(s)"
+ "_UIScenePresentationView"
+ "__SBFLegacyWallpaperWakeAnimatorInvertColorsAccessibility_super"
+ "__SBTraitsSingleSceneWindowInvertColorsAccessibility_super"
+ "_accessibilityApplyBackgroundIsDark:toView:invertEnabled:"
+ "_accessibilityApplyFloatingLayerInvert:"
+ "_accessibilitySetUnsignedIntegerValue:forKey:"
+ "_accessibilityUnsignedIntegerValueForKey:"
+ "_axHostsSiriAIScene"
+ "_isSecure"
+ "_isSpringBoardHomeScreenWindow:"
+ "_scene"
+ "afterDelay:processBlock:"
+ "applying"
+ "cancel"
+ "clientHandle"
+ "com.apple.campo"
+ "connectedScenes"
+ "initWithTargetSerialQueue:"
+ "removing"
+ "setLabel:"
+ "toggleSpringBoardHomeScreenWindowInvert Apply window: %@"
+ "toggleSpringBoardHomeScreenWindowInvert Remove window: %@"
+ "toggleSpringBoardHomeScreenWindowInvert:"
+ "updateWakeEffectsForWake:animated:completion:"
+ "v32@0:8B16@20B28"
+ "v32@0:8B16B20@?24"
+ "windows"
- "Ignoring IC status change: too soon"
- "_screenWakeAnimationController"
- "target"
```
