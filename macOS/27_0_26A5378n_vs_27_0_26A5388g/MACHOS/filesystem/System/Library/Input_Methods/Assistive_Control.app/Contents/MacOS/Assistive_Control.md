## Assistive Control

> `/System/Library/Input Methods/Assistive Control.app/Contents/MacOS/Assistive Control`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-417.0.0.0.0
-  __TEXT.__text: 0x5f1f4
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_stubs: 0x12a60
-  __TEXT.__objc_methlist: 0x8044
+418.0.0.0.0
+  __TEXT.__text: 0x5f98c
+  __TEXT.__auth_stubs: 0x12f0
+  __TEXT.__objc_stubs: 0x12ba0
+  __TEXT.__objc_methlist: 0x80ac
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x65c
-  __TEXT.__cstring: 0x2144
-  __TEXT.__objc_methname: 0x16ce4
-  __TEXT.__objc_classname: 0xd16
+  __TEXT.__cstring: 0x2299
+  __TEXT.__objc_methname: 0x16e30
+  __TEXT.__objc_classname: 0xd28
   __TEXT.__objc_methtype: 0x2c8f
   __TEXT.__oslogstring: 0x83b
   __TEXT.__ustring: 0x6a
-  __TEXT.__unwind_info: 0x19b8
-  __DATA_CONST.__const: 0x1c90
-  __DATA_CONST.__cfstring: 0x2840
-  __DATA_CONST.__objc_classlist: 0x398
+  __TEXT.__unwind_info: 0x19d0
+  __DATA_CONST.__const: 0x1cb0
+  __DATA_CONST.__cfstring: 0x2960
+  __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA_CONST.__auth_got: 0x980
+  __DATA_CONST.__auth_got: 0x988
   __DATA_CONST.__got: 0xa28
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA.__objc_const: 0xa418
-  __DATA.__objc_selrefs: 0x5710
-  __DATA.__objc_ivar: 0x61c
-  __DATA.__objc_data: 0x23f0
+  __DATA.__objc_const: 0xa4f0
+  __DATA.__objc_selrefs: 0x5760
+  __DATA.__objc_ivar: 0x624
+  __DATA.__objc_data: 0x2440
   __DATA.__data: 0x978
-  __DATA.__bss: 0x228
+  __DATA.__bss: 0x238
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/AccessibilitySupport
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/Versions/A/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AssistiveControlSupport.framework/Versions/A/AssistiveControlSupport
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI
   - /System/Library/PrivateFrameworks/DisplayServices.framework/Versions/A/DisplayServices
   - /System/Library/PrivateFrameworks/MachineSettings.framework/Versions/A/MachineSettings

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2643
-  Symbols:   674
-  CStrings:  4490
+  Functions: 2651
+  Symbols:   675
+  CStrings:  4512
 
Symbols:
+ _AnalyticsSendEvent
CStrings:
+ "ACAPCoreAnalytics"
+ "ACSH.systemPanel.window"
+ "AssistiveControlGlidingCursorInteractions"
+ "AssistiveControlIsAppItemModePresent"
+ "AssistiveControlIsCustomPanel"
+ "AssistiveControlIsDefaultPanel"
+ "AssistiveControlIsSuggestionsToolbarPresent"
+ "AssistiveControlItemModeInteractions"
+ "_glidingCursorInteractionCount"
+ "_itemModeInteractionCount"
+ "_panelElementContainsSuggestions:"
+ "assistiveControlPanelChanged"
+ "com.apple.assistivecontrol.panelinformation"
+ "com.apple.assistivecontrol.switchcontrolinteraction"
+ "isAppItemModeActioninPanel:"
+ "isSystemPanel"
+ "logGlidingCursorInteractionForAnalytics"
+ "logItemModeInteractionForAnalytics"
+ "sendPanelInformationEvent"
+ "sendSwitchControlInteractionEvent"
+ "setBool:forKey:"
+ "setInteger:forKey:"
```
