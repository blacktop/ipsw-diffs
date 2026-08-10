## SystemApertureUI

> `/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__objc_const`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x270c
-  __TEXT.__objc_methlist: 0x3d4
+3048.0.0.0.0
+  __TEXT.__text: 0x2950
+  __TEXT.__objc_methlist: 0x3fc
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__cstring: 0x5de
-  __TEXT.__unwind_info: 0x150
+  __TEXT.__cstring: 0x5be
+  __TEXT.__unwind_info: 0x160
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x208
+  __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a8
+  __DATA_CONST.__objc_selrefs: 0x3c0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0xb8
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x740
+  __DATA_CONST.__got: 0xb0
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x5f0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x180
+  __DATA.__data: 0x190
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 68
-  Symbols:   318
-  CStrings:  71
+  Functions: 71
+  Symbols:   325
+  CStrings:  69
 
Symbols:
+ -[SAUIElementViewControllerAccessibility _accessibilityShouldPostScreenChangedOnPresentation]
+ -[SAUIElementViewControllerAccessibility _axAnnounceLiveActivityContent]
+ -[SAUIElementViewControllerAccessibility accessibilityPostScreenChangedForChildViewController:isAddition:]
+ _CFAbsoluteTimeGetCurrent
+ _MACancelDownloadErrorDomain_block_invoke.kLastFocusedPowerAlertKey
+ _OBJC_CLASS_$_AXAttributedString
+ _OBJC_CLASS_$_NSNumber
+ _UIAccessibilityAnnouncementNotification
+ ___53-[SAUIElementViewControllerAccessibility viewDidLoad]_block_invoke
+ ___93-[SAUIElementViewControllerAccessibility viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke
+ __axAnnounceLiveActivityContent.kLastAnnounceTimeKey
+ _objc_getAssociatedObject
+ _objc_msgSend$_accessibilityViewIsVisible
+ _objc_msgSend$_axAnnounceLiveActivityContent
+ _objc_msgSend$axAttributedStringWithString:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$numberWithDouble:
+ _objc_release_x28
+ _objc_setAssociatedObject
- _AXImageExplorerGenerativeModelsAvailable
- _OBJC_CLASS_$_AXSettings
- _OBJC_CLASS_$_AXVoiceOverServer
- ___58-[SAUIElementViewAccessibility accessibilityCustomActions]_block_invoke_12
- ___58-[SAUIElementViewAccessibility accessibilityCustomActions]_block_invoke_13
- ___block_descriptor_32_e37_B16?0"UIAccessibilityCustomAction"8l
- _kVOTEventCommandActivateScreenExplorer
- _kVOTEventCommandAskAboutScreen
- _objc_msgSend$imageExplorerAskAboutScreenDynamicIslandActionEnabled
- _objc_msgSend$imageExplorerScreenExplorerDynamicIslandActionEnabled
- _objc_msgSend$server
- _objc_msgSend$triggerEventCommand:
CStrings:
- "ask.about.screen"
- "explore.screen"
```
