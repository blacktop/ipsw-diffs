## AccessibilityControlsExtension

> `/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`

```diff

-3134.3.0.0.0
-  __TEXT.__text: 0x2f5b38
+3136.0.4.1.0
+  __TEXT.__text: 0x2f5b3c
   __TEXT.__auth_stubs: 0x18b0
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x5e044
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__cstring: 0x2ea4e
+  __TEXT.__cstring: 0x2eb4e
   __TEXT.__objc_methname: 0x2813
   __TEXT.__objc_classname: 0x15
   __TEXT.__objc_methtype: 0x40
   __TEXT.__dlopen_cstrs: 0x82
   __TEXT.__constg_swiftt: 0x99f0
-  __TEXT.__swift5_typeref: 0x1e9ee
-  __TEXT.__swift5_fieldmd: 0x7b84
+  __TEXT.__swift5_typeref: 0x1ea0e
+  __TEXT.__swift5_fieldmd: 0x7b78
   __TEXT.__swift5_types: 0xd28
-  __TEXT.__swift5_reflstr: 0x8ac3
+  __TEXT.__swift5_reflstr: 0x8a93
   __TEXT.__swift5_assocty: 0xf0e8
   __TEXT.__swift5_proto: 0x5854
   __TEXT.__oslogstring: 0x91

   __TEXT.__eh_frame: 0x15750
   __DATA_CONST.__auth_got: 0xc68
   __DATA_CONST.__got: 0x938
-  __DATA_CONST.__auth_ptr: 0x1c20
-  __DATA_CONST.__const: 0x12098
+  __DATA_CONST.__auth_ptr: 0x1d40
+  __DATA_CONST.__const: 0x120e0
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 22886
-  Symbols:   302
+  Symbols:   311
   CStrings:  3851
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "AXASTSoundActions"
+ "AXSystemSoundActions"
+ "AXVideoPassthrough"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS#COMMAND_AND_CONTROL_COMMANDS"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Accessibility"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/AdvancedDeletion"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/CreateNewCommand#CreateNewCommand"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/DragDropGestures"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Editing"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Gestures"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Hardware"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/ImportCustomCommands#ImportCustomCommands"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Movement"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Overlays"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Selection"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/System"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/TextDictation"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY#DELETE_ALL_VOCABULARY"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY#EXPORT_VOCABULARY"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY#IMPORT_VOCABULARY"
+ "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY/VOCABULARY#VOCABULARY"
- "AAXVideoPassthrough"
- "SOUND_ACTIONS_DESCRIPTION"
- "SOUND_ACTIONS_SOUND_ACTIONS_DESCRIPTION"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS#CUSTOMIZE_COMMANDS"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/Accessibility"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/AdvancedDeletion"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/CreateNewCommand#CreateNewCommand"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/DragDropGestures"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/Editing"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/Gestures"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/Hardware"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/ImportCustomCommands#ImportCustomCommands"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/Movement"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/Overlays"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/Selection"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/System"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/CUSTOMIZE_COMMANDS/TextDictation"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/vocabulary#DELETE_ALL_VOCABULARY"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/vocabulary#EXPORT_VOCABULARY"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/vocabulary#IMPORT_VOCABULARY"
- "settings-navigation://com.apple.Settings.Accessibility/CommandAndControlTitle/vocabulary/VOCABULARY#VOCABULARY"

```
