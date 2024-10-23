## AssistantSettingsControlsExtension

> `/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension`

```diff

-3401.31.5.11.15
-  __TEXT.__text: 0x5b54c
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__cstring: 0x4d42
-  __TEXT.__swift5_typeref: 0x3aaa
-  __TEXT.__swift5_reflstr: 0xff8
-  __TEXT.__swift5_assocty: 0x1740
-  __TEXT.__const: 0xac64
-  __TEXT.__constg_swiftt: 0x1404
-  __TEXT.__swift5_fieldmd: 0xba8
-  __TEXT.__objc_methname: 0x6bc
-  __TEXT.__swift5_proto: 0x978
-  __TEXT.__swift5_types: 0x184
+3402.58.5.1.18
+  __TEXT.__text: 0x5b6a0
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__cstring: 0x4d62
+  __TEXT.__swift5_typeref: 0x377a
+  __TEXT.__swift5_reflstr: 0x1108
+  __TEXT.__swift5_assocty: 0x1568
+  __TEXT.__const: 0xa3d4
+  __TEXT.__constg_swiftt: 0x139c
+  __TEXT.__swift5_fieldmd: 0xc38
+  __TEXT.__objc_methname: 0x692
+  __TEXT.__swift5_proto: 0x8fc
+  __TEXT.__swift5_types: 0x16c
   __TEXT.__oslogstring: 0x3
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2748
-  __TEXT.__eh_frame: 0x3220
-  __DATA_CONST.__auth_got: 0x6c0
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__auth_ptr: 0xa00
-  __DATA_CONST.__const: 0x1d68
+  __TEXT.__unwind_info: 0x22a0
+  __TEXT.__eh_frame: 0x2df0
+  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__auth_ptr: 0x9e0
+  __DATA_CONST.__const: 0x1bd0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x1b8
-  __DATA.__data: 0x2e28
-  __DATA.__common: 0xb18
-  __DATA.__bss: 0x131a8
+  __DATA.__objc_selrefs: 0x1a8
+  __DATA.__data: 0x3188
+  __DATA.__common: 0xa30
+  __DATA.__bss: 0x12208
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2869
+  Functions: 2664
   Symbols:   112
-  CStrings:  457
+  CStrings:  454
 
CStrings:
+ "/ACTIVATION_COMPACT_ID"
+ "/ANNOUNCE_CALLS"
+ "/ANNOUNCE_MESSAGES"
+ "/ASSISTANT_LOCK_SCREEN_ACCESS"
+ "/HISTORY"
+ "/LANGUAGE_ID"
+ "/MESSAGE_WITHOUT_CONFIRMATION"
+ "/MY_INFO"
+ "/SIRI_IN_CALL_ID"
+ "/VOICE_FEEDBACK_ID"
+ "/VOICE_ID"
+ "Always print siri responses control under root pane of Siri settings.  This setting controls user preference of settings always show responses for Siri"
+ "Messaging with Siri"
+ "Root settings pane of Siri"
+ "Siri configuration"
+ "com.apple.systempreferences"
+ "settings-navigation://com.apple.Settings.Siri"
+ "settings-navigation://com.apple.Settings.Siri/ALWAYS_PRINT_RESPONSE_GROUP_ID"
+ "settings-navigation://com.apple.Settings.Siri/ALWAYS_SHOW_RECOGNIZED_SPEECH_GROUP_ID"
+ "settings-navigation://com.apple.Settings.Siri/ANNOUNCE_CALLS"
+ "settings-navigation://com.apple.Settings.Siri/ANNOUNCE_MESSAGES"
+ "settings-navigation://com.apple.Settings.Siri/ASSISTANT_APPS_SETTINGS_ID"
+ "settings-navigation://com.apple.Settings.Siri/ASSISTANT_APPS_SETTINGS_ID/"
+ "settings-navigation://com.apple.Settings.Siri/ASSISTANT_APP_CLIPS_SETTINGS_ID"
+ "settings-navigation://com.apple.Settings.Siri/ASSISTANT_LOCK_SCREEN_ACCESS"
+ "settings-navigation://com.apple.Settings.Siri/HISTORY"
+ "settings-navigation://com.apple.Settings.Siri/LANGUAGE_ID"
+ "settings-navigation://com.apple.Settings.Siri/MESSAGE_WITHOUT_CONFIRMATION"
+ "settings-navigation://com.apple.Settings.Siri/MY_INFO"
+ "settings-navigation://com.apple.Settings.Siri/SIRI_IN_CALL_ID"
+ "settings-navigation://com.apple.Settings.Siri/VOICE_FEEDBACK_ID"
+ "settings-navigation://com.apple.Settings.Siri/VOICE_ID"
- "ASSISTANT_TYPE_TO_SIRI_SUBTITLE"
- "ASSISTANT_TYPE_TO_SIRI_TITLE"
- "ASSISTANT_TYPE_TO_SIRI_TITLE to update"
- "ASSISTANT_TYPE_TO_SIRI_TITLE to update on ASSISTANT_TYPE_TO_SIRI_TITLE"
- "App Entity title for 'Listen for' toggle"
- "App Entity title for 'Type To Siri' toggle"
- "Apple Intelligence & Siri → Apps"
- "Change Type To Siri to "
- "Change the ASSISTANT_TYPE_TO_SIRI_TITLE value of ASSISTANT_TYPE_TO_SIRI_TITLE"
- "Open Siri Voice Activation"
- "Set Type To Siri to "
- "Show what Siri says on screen."
- "Siri Voice Activation"
- "This is supported during phone and FaceTime calls. When a call is connected, voice input is processed on iPhone, and transcripts and audio are not sent to Apple."
- "Type To Siri Entity"
- "Update ASSISTANT_TYPE_TO_SIRI_TITLE"
- "UpdateTypeToSiriEntityValueIntent"
- "VOICE_ACTIVATION_COMPACT_TITLE"
- "Voice Activation Entity"
- "prefs:root=SIRI&path=ACTIVATION_COMPACT_ID"
- "prefs:root=SIRI&path=ANNOUNCE_CALLS"
- "prefs:root=SIRI&path=ANNOUNCE_MESSAGES"
- "prefs:root=SIRI&path=ASSISTANT_APPS_SETTINGS_ID"
- "prefs:root=SIRI&path=ASSISTANT_APPS_SETTINGS_ID/"
- "prefs:root=SIRI&path=ASSISTANT_APP_CLIPS_SETTINGS_ID"
- "prefs:root=SIRI&path=ASSISTANT_LOCK_SCREEN_ACCESS"
- "prefs:root=SIRI&path=HISTORY"
- "prefs:root=SIRI&path=LANGUAGE_ID"
- "prefs:root=SIRI&path=MESSAGE_WITHOUT_CONFIRMATION"
- "prefs:root=SIRI&path=MY_INFO"
- "prefs:root=SIRI&path=SIRI_IN_CALL_ID"
- "prefs:root=SIRI&path=VOICE_FEEDBACK_ID"
- "prefs:root=SIRI&path=VOICE_ID"
- "setTypeToSiriEnabled:"
- "typeToSiriIsEnabled"

```
