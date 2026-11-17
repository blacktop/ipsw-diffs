## AccessibilitySettingsLoader

> `/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader`

```diff

-3245.8.14.0.0
-  __TEXT.__text: 0x11800
-  __TEXT.__objc_methlist: 0x1204
+3245.8.23.0.0
+  __TEXT.__text: 0x130b0
+  __TEXT.__objc_methlist: 0x13ec
   __TEXT.__dlopen_cstrs: 0x70c
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x514
-  __TEXT.__cstring: 0x2065
-  __TEXT.__oslogstring: 0x8aa
-  __TEXT.__unwind_info: 0x850
+  __TEXT.__gcc_except_tab: 0x534
+  __TEXT.__cstring: 0x22aa
+  __TEXT.__oslogstring: 0xcbf
+  __TEXT.__unwind_info: 0x8d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x548
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__const: 0x568
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf0
+  __DATA_CONST.__objc_selrefs: 0xf10
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x280
-  __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x1540
-  __AUTH_CONST.__objc_const: 0x2400
+  __DATA_CONST.__got: 0x298
+  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__cfstring: 0x1760
+  __AUTH_CONST.__objc_const: 0x2850
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x3c
+  __AUTH.__objc_data: 0xcd0
+  __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x130
+  __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 406
-  Symbols:   1029
-  CStrings:  336
+  Functions: 456
+  Symbols:   1121
+  CStrings:  368
 
Symbols:
+ +[AccessibilityFloatingUIKeyboardHelper keyboardSuppressionDidChange:]
+ +[AccessibilityFloatingUIKeyboardHelper remoteKeyboardDidChangeOnScreen:isRestore:]
+ +[ZoomServicesUI _shouldUnmapPointsForFluidGesturesOnScreen:]
+ +[ZoomServicesUI _unMappedZoomPoint:onScreen:]
+ +[ZoomUI_SBReachabilityController(SafeCategory) safeCategoryBaseClass]
+ +[ZoomUI_SBReachabilityController(SafeCategory) safeCategoryTargetClassName]
+ +[_UIRemoteKeyboardsAccessibility_SettingsLoader _accessibilityPerformValidations:]
+ +[_UIRemoteKeyboardsAccessibility_SettingsLoader(SafeCategory) safeCategoryBaseClass]
+ +[_UIRemoteKeyboardsAccessibility_SettingsLoader(SafeCategory) safeCategoryTargetClassName]
+ +[_UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader _accessibilityPerformValidations:]
+ +[_UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader(SafeCategory) safeCategoryBaseClass]
+ +[_UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader(SafeCategory) safeCategoryTargetClassName]
+ -[AccessibilityFloatingUIKeyboardHelper _beginHomeTransitionShowSuppression]
+ -[AccessibilityFloatingUIKeyboardHelper _canReportVisibleKeyboard]
+ -[AccessibilityFloatingUIKeyboardHelper _endHomeTransitionShowSuppression]
+ -[AccessibilityFloatingUIKeyboardHelper _handleApplicationWillResignActiveNotification:]
+ -[AccessibilityFloatingUIKeyboardHelper _reportKeyboardHidden]
+ -[AccessibilityFloatingUIKeyboardHelper _reportOnScreenKeyboardToAssistiveTouch]
+ -[AccessibilityFloatingUIKeyboardHelper _scheduleDeferredKeyboardHiddenReread]
+ -[AccessibilityFloatingUIKeyboardHelper _scheduleOnScreenKeyboardReport:]
+ -[AccessibilityFloatingUIKeyboardHelper _startObservingAppActivation]
+ -[AccessibilityFloatingUIKeyboardHelper _stopObservingAppActivation]
+ -[AccessibilityFloatingUIKeyboardHelper homeTransitionGeneration]
+ -[AccessibilityFloatingUIKeyboardHelper keyboardRereadGeneration]
+ -[AccessibilityFloatingUIKeyboardHelper observingAppActivation]
+ -[AccessibilityFloatingUIKeyboardHelper reportedKeyboardVisible]
+ -[AccessibilityFloatingUIKeyboardHelper setHomeTransitionGeneration:]
+ -[AccessibilityFloatingUIKeyboardHelper setKeyboardRereadGeneration:]
+ -[AccessibilityFloatingUIKeyboardHelper setObservingAppActivation:]
+ -[AccessibilityFloatingUIKeyboardHelper setReportedKeyboardVisible:]
+ -[AccessibilityFloatingUIKeyboardHelper setSuppressingShowsForHomeTransition:]
+ -[AccessibilityFloatingUIKeyboardHelper suppressingShowsForHomeTransition]
+ -[ZoomUI_SBReachabilityController _shouldHorizontalReachabilityGestureReceiveTouch:]
+ -[_UIRemoteKeyboardsAccessibility_SettingsLoader queue_keyboardChanged:onComplete:]
+ -[_UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader setSuppressingKeyboard:forScene:]
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table154
+ GCC_except_table168
+ GCC_except_table169
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table193
+ GCC_except_table195
+ GCC_except_table213
+ GCC_except_table243
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table263
+ GCC_except_table271
+ GCC_except_table324
+ GCC_except_table332
+ GCC_except_table338
+ GCC_except_table347
+ GCC_except_table371
+ GCC_except_table373
+ GCC_except_table383
+ GCC_except_table389
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table399
+ GCC_except_table410
+ GCC_except_table412
+ GCC_except_table420
+ GCC_except_table450
+ GCC_except_table58
+ GCC_except_table72
+ GCC_except_table86
+ _AXFUIKKeyboardSuppressed
+ _AXLogUI
+ _AXPerformBlockOnMainThread
+ _Helper
+ _OBJC_CLASS_$_UITextEffectsWindow
+ _OBJC_CLASS_$_UITouch
+ _OBJC_CLASS_$_ZoomUI_SBReachabilityController
+ _OBJC_CLASS_$__UIRemoteKeyboardsAccessibility_SettingsLoader
+ _OBJC_CLASS_$__UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader
+ _OBJC_CLASS_$___ZoomUI_SBReachabilityController_super
+ _OBJC_CLASS_$____UIRemoteKeyboardsAccessibility_SettingsLoader_super
+ _OBJC_CLASS_$____UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader_super
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._homeTransitionGeneration
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._keyboardRereadGeneration
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._observingAppActivation
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._reportedKeyboardVisible
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._suppressingShowsForHomeTransition
+ _OBJC_METACLASS_$_ZoomUI_SBReachabilityController
+ _OBJC_METACLASS_$__UIRemoteKeyboardsAccessibility_SettingsLoader
+ _OBJC_METACLASS_$__UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader
+ _OBJC_METACLASS_$___ZoomUI_SBReachabilityController_super
+ _OBJC_METACLASS_$____UIRemoteKeyboardsAccessibility_SettingsLoader_super
+ _OBJC_METACLASS_$____UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader_super
+ _UIApplicationWillResignActiveNotification
+ __AXFUIKKeyboardScreenFrameInWindow
+ __AXFUIKKeyboardWindow
+ __OBJC_$_CLASS_METHODS_ZoomUI_SBReachabilityController(SafeCategory)
+ __OBJC_$_CLASS_METHODS__UIRemoteKeyboardsAccessibility_SettingsLoader(SafeCategory)
+ __OBJC_$_CLASS_METHODS__UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_ZoomUI_SBReachabilityController
+ __OBJC_$_INSTANCE_METHODS__UIRemoteKeyboardsAccessibility_SettingsLoader
+ __OBJC_$_INSTANCE_METHODS__UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader
+ __OBJC_CLASS_RO_$_ZoomUI_SBReachabilityController
+ __OBJC_CLASS_RO_$__UIRemoteKeyboardsAccessibility_SettingsLoader
+ __OBJC_CLASS_RO_$__UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader
+ __OBJC_CLASS_RO_$___ZoomUI_SBReachabilityController_super
+ __OBJC_CLASS_RO_$____UIRemoteKeyboardsAccessibility_SettingsLoader_super
+ __OBJC_CLASS_RO_$____UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader_super
+ __OBJC_METACLASS_RO_$_ZoomUI_SBReachabilityController
+ __OBJC_METACLASS_RO_$__UIRemoteKeyboardsAccessibility_SettingsLoader
+ __OBJC_METACLASS_RO_$__UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader
+ __OBJC_METACLASS_RO_$___ZoomUI_SBReachabilityController_super
+ __OBJC_METACLASS_RO_$____UIRemoteKeyboardsAccessibility_SettingsLoader_super
+ __OBJC_METACLASS_RO_$____UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader_super
+ ___70+[AccessibilityFloatingUIKeyboardHelper keyboardSuppressionDidChange:]_block_invoke
+ ___72-[AccessibilitySettingsLoader _initializeImmediateAccessibilitySettings]_block_invoke_4
+ ___72-[AccessibilitySettingsLoader _initializeImmediateAccessibilitySettings]_block_invoke_5
+ ___72-[AccessibilitySettingsLoader _initializeImmediateAccessibilitySettings]_block_invoke_6
+ ___72-[AccessibilitySettingsLoader _initializeImmediateAccessibilitySettings]_block_invoke_7
+ ___72-[AccessibilitySettingsLoader _initializeImmediateAccessibilitySettings]_block_invoke_8
+ ___72-[AccessibilitySettingsLoader _initializeImmediateAccessibilitySettings]_block_invoke_9
+ ___73-[AccessibilityFloatingUIKeyboardHelper _scheduleOnScreenKeyboardReport:]_block_invoke
+ ___75-[AccessibilityFloatingUIKeyboardHelper _installSpringBoardTransitionHooks]_block_invoke_4
+ ___76-[AccessibilityFloatingUIKeyboardHelper _beginHomeTransitionShowSuppression]_block_invoke
+ ___78-[AccessibilityFloatingUIKeyboardHelper _scheduleDeferredKeyboardHiddenReread]_block_invoke
+ ___83+[AccessibilityFloatingUIKeyboardHelper remoteKeyboardDidChangeOnScreen:isRestore:]_block_invoke
+ ___block_descriptor_33_e5_v8?0l
+ _objc_retain_x23
- GCC_except_table100
- GCC_except_table104
- GCC_except_table137
- GCC_except_table140
- GCC_except_table141
- GCC_except_table149
- GCC_except_table156
- GCC_except_table163
- GCC_except_table171
- GCC_except_table172
- GCC_except_table173
- GCC_except_table175
- GCC_except_table178
- GCC_except_table180
- GCC_except_table200
- GCC_except_table230
- GCC_except_table236
- GCC_except_table239
- GCC_except_table250
- GCC_except_table258
- GCC_except_table292
- GCC_except_table293
- GCC_except_table294
- GCC_except_table306
- GCC_except_table313
- GCC_except_table325
- GCC_except_table327
- GCC_except_table339
- GCC_except_table343
- GCC_except_table344
- GCC_except_table349
- GCC_except_table360
- GCC_except_table362
- GCC_except_table370
- GCC_except_table400
- GCC_except_table60
- GCC_except_table66
- GCC_except_table84
- _initializeMonitoring.Helper
CStrings:
+ "AXFUIKKeyboardSuppressionDidEndNotification"
+ "AXSBSwitcherTransitionToHomeOrAppSwitcherNotification"
+ "AXSettingsLoader RemoteKeyboards"
+ "AXSettingsLoader RemoteKeyboards Suppression"
+ "FloatingUIKB: application resigning active with a reported keyboard, reporting hidden"
+ "FloatingUIKB: deferring keyboard show, application is not active"
+ "FloatingUIKB: dropping deferred keyboard re-read superseded=%d"
+ "FloatingUIKB: dropping keyboard re-query during home transition"
+ "FloatingUIKB: dropping keyboard show during home transition"
+ "FloatingUIKB: home transition keyboard hidden, ending show suppression"
+ "FloatingUIKB: home transition suppression timed out, re-reading keyboard"
+ "FloatingUIKB: home transition, suppressing keyboard shows reportedVisible=%d"
+ "FloatingUIKB: keyboard show has an empty frame, retracting this process's keyboard=%d"
+ "FloatingUIKB: not re-reporting keyboard to AST while the system suppresses it"
+ "FloatingUIKB: not reporting keyboard hidden, this process did not report one"
+ "FloatingUIKB: re-reporting keyboard to AST: %{public}@"
+ "FloatingUIKB: will re-report keyboard to AST after %{public}@"
+ "FloatingUIKB: zero-duration keyboard hide, deferring to re-read"
+ "FloatingUIKB: zero-duration keyboard show, deferring to re-read"
+ "SBReachabilityController"
+ "ZoomUI_SBReachabilityController"
+ "_UIKeyboardChangedInformation"
+ "_UIKeyboardUIInformation"
+ "_UIRemoteKeyboards"
+ "_UIRemoteKeyboardsAccessibility_SettingsLoader"
+ "_UIRemoteKeyboardsSuppressionAccessibility_SettingsLoader"
+ "_shouldHorizontalReachabilityGestureReceiveTouch:"
+ "keyboardOnScreen"
+ "queue_keyboardChanged:onComplete:"
+ "setSuppressingKeyboard:forScene:"
+ "shouldRestoreKeyboard"
+ "visibleFrame"
```
