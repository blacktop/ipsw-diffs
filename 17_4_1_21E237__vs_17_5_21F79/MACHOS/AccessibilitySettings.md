## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1726.15.0.0.0
-  __TEXT.__text: 0x14496c
-  __TEXT.__auth_stubs: 0x35f0
-  __TEXT.__objc_stubs: 0x21480
-  __TEXT.__objc_methlist: 0x1120c
+1726.20.0.0.0
+  __TEXT.__text: 0x145a58
+  __TEXT.__auth_stubs: 0x3640
+  __TEXT.__objc_stubs: 0x21640
+  __TEXT.__objc_methlist: 0x1129c
   __TEXT.__const: 0xfa4
-  __TEXT.__gcc_except_tab: 0x2adc
-  __TEXT.__objc_methname: 0x2ef25
-  __TEXT.__cstring: 0x15398
-  __TEXT.__oslogstring: 0x2f16
-  __TEXT.__objc_classname: 0x3e07
+  __TEXT.__gcc_except_tab: 0x2ae8
+  __TEXT.__objc_methname: 0x2f11f
+  __TEXT.__cstring: 0x154e8
+  __TEXT.__oslogstring: 0x2fad
+  __TEXT.__objc_classname: 0x3e0a
   __TEXT.__objc_methtype: 0x5bb7
   __TEXT.__dlopen_cstrs: 0x186
   __TEXT.__ustring: 0x2e

   __TEXT.__swift5_capture: 0x80
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x64
-  __TEXT.__unwind_info: 0x4b18
-  __DATA_CONST.__auth_got: 0x1b08
-  __DATA_CONST.__got: 0x1350
+  __TEXT.__unwind_info: 0x4b5c
+  __DATA_CONST.__auth_got: 0x1b30
+  __DATA_CONST.__got: 0x1358
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x4980
-  __DATA_CONST.__cfstring: 0x17d00
+  __DATA_CONST.__cfstring: 0x17ea0
   __DATA_CONST.__objc_classlist: 0xcf0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x1568
   __DATA_CONST.__objc_superrefs: 0xa40
-  __DATA_CONST.__objc_intobj: 0x15c0
+  __DATA_CONST.__objc_intobj: 0x15f0
   __DATA_CONST.__objc_arraydata: 0x1188
   __DATA_CONST.__objc_arrayobj: 0x6f0
   __DATA_CONST.__objc_doubleobj: 0x1b0
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x848
-  __DATA.__objc_const: 0x1e6e8
-  __DATA.__objc_selrefs: 0xae50
-  __DATA.__objc_ivar: 0xce8
+  __DATA.__objc_const: 0x1e740
+  __DATA.__objc_selrefs: 0xaed8
+  __DATA.__objc_ivar: 0xcf0
   __DATA.__objc_data: 0x8318
   __DATA.__data: 0x25fa
   __DATA.__bss: 0xf55

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7206
-  Symbols:   17765
-  CStrings:  11905
+  Functions: 7220
+  Symbols:   17803
+  CStrings:  11944
 
Symbols:
+ -[AccessibilityPencilSettingsController dealloc]
+ -[AccessibilityPencilSettingsController extendedSqueezeRange:]
+ -[AccessibilityPencilSettingsController productID]
+ -[AccessibilityPencilSettingsController setExtendedSqueezeRange:specifier:]
+ -[AccessibilityPencilSettingsController setProductID:]
+ -[AccessibilityPencilSettingsController viewDidLoad]
+ -[AccessibilitySettingsController _monitorPencilSupport]
+ -[AccessibilitySettingsController willBecomeActive]
+ -[SCATSwitchActionsController _shortcutSpecifiers]
+ -[SCATSwitchActionsController dealloc]
+ -[SCATSwitchesController ignoreInvalidSwitchConfiguration:]
+ -[SCATSwitchesController setIgnoreInvalidSwitchConfiguration:specifier:]
+ GCC_except_table59
+ OBJC_IVAR_$_AccessibilityPencilSettingsController._productID
+ OBJC_IVAR_$_SCATSwitchActionsController._siriShortcutToken
+ _AXDeviceIsKShotMedinaEnabled
+ _AXDeviceSupportsMedina
+ _AXRuntimeCheck_SoundRecognitionMedinaSupportEnabled
+ __AXSPencilExtendedSqueezeRangeEnabled
+ __AXSSetPencilExtendedSqueezeRangeEnabled
+ __OBJC_$_PROP_LIST_AccessibilityPencilSettingsController
+ ___39-[AccessibilitySettingsController init]_block_invoke_7
+ ___46-[SCATSwitchActionsController initWithSwitch:]_block_invoke
+ __block_literal_global.395
+ __block_literal_global.401
+ __block_literal_global.410
+ __block_literal_global.420
+ __block_literal_global.422
+ __block_literal_global.434
+ __block_literal_global.485
+ __block_literal_global.487
+ __block_literal_global.506
+ __block_literal_global.739
+ __pencilSettingsChanged
+ _kAXSPencilExtendedSqueezeRangeEnabledChangedNotification
+ _objc_msgSend$_monitorPencilSupport
+ _objc_msgSend$_shortcutSpecifiers
+ _objc_msgSend$deviceMonitorDidDetectDeviceEvent:
+ _objc_msgSend$forceMedinaSupport
+ _objc_msgSend$longPressShortcutIdentifier
+ _objc_msgSend$setLongPressShortcutIdentifier:
+ _objc_msgSend$setProductID:
+ _objc_msgSend$setShortcutIdentifier:
+ _objc_msgSend$setSwitchControlIgnoreInvalidSwitchConfiguration:
+ _objc_msgSend$shortcutForIdentifier:
+ _objc_msgSend$shortcutIdentifier
+ _objc_msgSend$shortcutName
+ _objc_msgSend$shortcuts
+ _objc_msgSend$switchControlIgnoreInvalidSwitchConfiguration
- GCC_except_table57
- __39-[AccessibilitySettingsController init]_block_invoke.299
- __block_literal_global.392
- __block_literal_global.394
- __block_literal_global.398
- __block_literal_global.417
- __block_literal_global.419
- __block_literal_global.429
- __block_literal_global.431
- __block_literal_global.482
- __block_literal_global.484
- __block_literal_global.503
- __block_literal_global.505
- __block_literal_global.736
CStrings:
+ "\x01\x13"
+ "Accessibility-B532"
+ "Already showing pencil"
+ "DotMini"
+ "EnableExtendedSqueezeRange"
+ "Found pencil product: %@"
+ "IGNORE_INVALID_SWITCH"
+ "IGNORE_INVALID_SWITCH_FOOTER"
+ "IgnoreInvalidSwitchConfiguration"
+ "Inserting pencil specifier"
+ "Monitoring for pencils: %@"
+ "PENCIL_SQUEEZE_THRESHOLD_FOOTNOTE"
+ "PENCIL_SQUEEZE_THRESHOLD_TITLE"
+ "PNPSqueezeThresholdSliderCell"
+ "Pencil devices: %@"
+ "SWITCH_SHORTCUTS_ACTIONS_LABEL"
+ "Setting pencil product ID: %@"
+ "ShortcutActionKey"
+ "T@\"NSString\",&,N,V_productID"
+ "_monitorPencilSupport"
+ "_productID"
+ "_shortcutSpecifiers"
+ "extendedRange"
+ "extendedSqueezeRange:"
+ "forceMedinaSupport"
+ "ignoreInvalidSwitchConfiguration:"
+ "longPressShortcutIdentifier"
+ "setExtendedSqueezeRange:specifier:"
+ "setIgnoreInvalidSwitchConfiguration:specifier:"
+ "setLongPressShortcutIdentifier:"
+ "setProductID:"
+ "setShortcutIdentifier:"
+ "setSwitchControlIgnoreInvalidSwitchConfiguration:"
+ "shortcutForIdentifier:"
+ "shortcutIdentifier"
+ "shortcutName"
+ "shortcuts"
+ "supportsPitchWithoutSpeak"
+ "switchControlIgnoreInvalidSwitchConfiguration"

```
