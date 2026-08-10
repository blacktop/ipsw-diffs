## AccessibilitySettingsLoader

> `/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-3237.1.0.0.0
-  __TEXT.__text: 0x12b24
-  __TEXT.__objc_methlist: 0x11fc
-  __TEXT.__dlopen_cstrs: 0x7e4
+3240.3.0.0.0
+  __TEXT.__text: 0x113b0
+  __TEXT.__objc_methlist: 0x11cc
+  __TEXT.__dlopen_cstrs: 0x70c
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x598
-  __TEXT.__cstring: 0x20cb
-  __TEXT.__oslogstring: 0x6a4
-  __TEXT.__unwind_info: 0x770
+  __TEXT.__gcc_except_tab: 0x510
+  __TEXT.__cstring: 0x2036
+  __TEXT.__oslogstring: 0x613
+  __TEXT.__unwind_info: 0x730
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5d8
-  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc0
+  __DATA_CONST.__objc_selrefs: 0xdb8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x290
-  __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x14e0
-  __AUTH_CONST.__objc_const: 0x2410
+  __DATA_CONST.__got: 0x278
+  __AUTH_CONST.__const: 0x5e0
+  __AUTH_CONST.__cfstring: 0x1500
+  __AUTH_CONST.__objc_const: 0x23d0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x2e8
-  __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0x128
+  __DATA.__bss: 0x2a0
+  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 419
-  Symbols:   1302
-  CStrings:  330
+  Functions: 399
+  Symbols:   1266
+  CStrings:  323
 
Symbols:
+ -[AccessibilityFloatingUIKeyboardHelper _installSpringBoardTransitionHooks]
+ -[AccessibilityFloatingUIKeyboardHelper _keyboardSceneFrameFromNotification:]
+ -[AccessibilityFloatingUIKeyboardHelper _scheduleDeferredKeyboardVisibleReread]
+ -[AccessibilityFloatingUIKeyboardHelper _sendCurrentKeyboardStateToAssistiveTouch]
+ -[AccessibilityFloatingUIKeyboardHelper _sendKeyboardVisibleWithSceneFrame:keyboardWindow:]
+ -[AccessibilityFloatingUIKeyboardHelper astDispatchQueue]
+ -[AccessibilityFloatingUIKeyboardHelper loadBuddyBundles]
+ -[AccessibilityFloatingUIKeyboardHelper setAstDispatchQueue:]
+ GCC_except_table100
+ GCC_except_table103
+ GCC_except_table137
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table149
+ GCC_except_table156
+ GCC_except_table161
+ GCC_except_table166
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table190
+ GCC_except_table199
+ GCC_except_table229
+ GCC_except_table235
+ GCC_except_table238
+ GCC_except_table249
+ GCC_except_table257
+ GCC_except_table289
+ GCC_except_table290
+ GCC_except_table291
+ GCC_except_table303
+ GCC_except_table310
+ GCC_except_table318
+ GCC_except_table320
+ GCC_except_table326
+ GCC_except_table332
+ GCC_except_table337
+ GCC_except_table342
+ GCC_except_table353
+ GCC_except_table355
+ GCC_except_table363
+ GCC_except_table393
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._astDispatchQueue
+ _OBJC_IVAR_$___ZoomServices.__CAPoint3D__
+ ___57-[AccessibilityFloatingUIKeyboardHelper loadBuddyBundles]_block_invoke
+ ___75-[AccessibilityFloatingUIKeyboardHelper _installSpringBoardTransitionHooks]_block_invoke
+ ___75-[AccessibilityFloatingUIKeyboardHelper _installSpringBoardTransitionHooks]_block_invoke_2
+ ___75-[AccessibilityFloatingUIKeyboardHelper _installSpringBoardTransitionHooks]_block_invoke_3
+ ___79-[AccessibilityFloatingUIKeyboardHelper _scheduleDeferredKeyboardVisibleReread]_block_invoke
+ _objc_msgSend$_installSpringBoardTransitionHooks
+ _objc_msgSend$_keyboardSceneFrameFromNotification:
+ _objc_msgSend$_scheduleDeferredKeyboardVisibleReread
+ _objc_msgSend$_sendCurrentKeyboardStateToAssistiveTouch
+ _objc_msgSend$_sendKeyboardVisibleWithSceneFrame:keyboardWindow:
+ _objc_msgSend$astDispatchQueue
+ _objc_msgSend$safeIvarForKey:
+ _objc_msgSend$safeValueForKeyPath:
- +[AssistiveTouchHelper initializeMonitoring]
- -[AssistiveTouchHelper _astDispatchQueue]
- -[AssistiveTouchHelper _sendKeyboardStatusUpdate:]
- -[AssistiveTouchHelper _sendKeyboardStatusUpdateHidden]
- -[AssistiveTouchHelper _sendKeyboardStatusUpdate]
- -[AssistiveTouchHelper dealloc]
- -[AssistiveTouchHelper enable]
- -[AssistiveTouchHelper init]
- -[AssistiveTouchHelper installKeyboardListener]
- -[AssistiveTouchHelper loadBuddyBundles]
- GCC_except_table107
- GCC_except_table139
- GCC_except_table142
- GCC_except_table143
- GCC_except_table151
- GCC_except_table158
- GCC_except_table165
- GCC_except_table168
- GCC_except_table175
- GCC_except_table176
- GCC_except_table182
- GCC_except_table192
- GCC_except_table201
- GCC_except_table231
- GCC_except_table237
- GCC_except_table240
- GCC_except_table251
- GCC_except_table259
- GCC_except_table281
- GCC_except_table282
- GCC_except_table293
- GCC_except_table294
- GCC_except_table307
- GCC_except_table323
- GCC_except_table329
- GCC_except_table346
- GCC_except_table352
- GCC_except_table356
- GCC_except_table357
- GCC_except_table362
- GCC_except_table373
- GCC_except_table375
- GCC_except_table383
- GCC_except_table413
- GCC_except_table97
- GCC_except_table98
- _ASTNotificationCenter
- _NSStringFromRect
- _OBJC_CLASS_$_AssistiveTouchHelper
- _OBJC_CLASS_$_UIViewController
- _OBJC_METACLASS_$_AssistiveTouchHelper
- _SBHomescreenDisplayChangedNotification
- _SBUIAppSwitcherRevealedNotification
- _UIKeyboardDidShowNotification
- __OBJC_$_CLASS_METHODS_AssistiveTouchHelper
- __OBJC_$_INSTANCE_METHODS_AssistiveTouchHelper
- __OBJC_CLASS_RO_$_AssistiveTouchHelper
- __OBJC_METACLASS_RO_$_AssistiveTouchHelper
- ___30-[AssistiveTouchHelper enable]_block_invoke
- ___40-[AssistiveTouchHelper loadBuddyBundles]_block_invoke
- ___41-[AssistiveTouchHelper _astDispatchQueue]_block_invoke
- ___44+[AssistiveTouchHelper initializeMonitoring]_block_invoke
- ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke
- ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke_2
- ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke_3
- ___50-[AssistiveTouchHelper _sendKeyboardStatusUpdate:]_block_invoke
- ___55-[AssistiveTouchHelper _sendKeyboardStatusUpdateHidden]_block_invoke
- ____accessibilityASTEnabled_block_invoke
- ___block_descriptor_40_e8_32bs_e24_v16?0"NSNotification"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e5_v8?0l
- ___getAXUIKeyboardScreenFrameSymbolLoc_block_invoke
- ___get__UIAccessibilityCastAsClassSymbolLoc_block_invoke
- __accessibilityASTEnabled
- __astDispatchQueue.bgQueue
- __astDispatchQueue.onceToken
- _enable.onceToken
- _getAXUIKeyboardScreenFrameSymbolLoc.ptr
- _get__UIAccessibilityCastAsClassSymbolLoc.ptr
- _objc_msgSend$_astDispatchQueue
- _objc_msgSend$_sendKeyboardStatusUpdate
- _objc_msgSend$_sendKeyboardStatusUpdate:
- _objc_msgSend$_sendKeyboardStatusUpdateHidden
- _objc_msgSend$floatValue
- _objc_msgSend$installKeyboardListener
- _objc_msgSend$rectValue
- _objc_msgSend$safeCGFloatForKey:
- _objc_msgSend$safeCGPointForKey:
- _objc_msgSend$setObject:forKey:
- _objc_release_x27
- _objc_release_x28
- _soft_AXProcessIsAssistiveTouch
- _soft___UIAccessibilityCastAsClass
CStrings:
+ "AccessibilityFloatingUIKeyboardHelper-AST"
+ "SBFluidSwitcherPersonality"
+ "__CAPoint3D__"
+ "personality"
+ "personality.rootModifier"
- "ASTDispatch"
- "AXUIKeyboardScreenFrame"
- "CGRect soft_AXUIKeyboardScreenFrame(void)"
- "Home Screen displayed: %{public}@"
- "Keyboard active notification "
- "Keyboard hidden notification: %{public}@"
- "Keyboard shown notification: %{public}@"
- "__CGPoint__"
- "__UIAccessibilityCastAsClass"
- "activateReachabilityGestureRecognizer"
- "id soft___UIAccessibilityCastAsClass(__unsafe_unretained Class, __strong id, BOOL, BOOL *)"
- "reachabilitySettings"
```
