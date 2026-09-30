## SoundAndHapticsControls

> `/System/Library/ExtensionKit/Extensions/SoundAndHapticsControls.appex/SoundAndHapticsControls`

```diff

-1095.0.0.0.0
-  __TEXT.__text: 0xeeb0
-  __TEXT.__auth_stubs: 0x8b0
+1097.0.0.0.0
+  __TEXT.__text: 0xfa98
+  __TEXT.__auth_stubs: 0x980
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x1ce4
-  __TEXT.__cstring: 0x1637
-  __TEXT.__swift5_typeref: 0xc06
-  __TEXT.__swift5_reflstr: 0x398
-  __TEXT.__swift5_assocty: 0x418
-  __TEXT.__constg_swiftt: 0x370
-  __TEXT.__swift5_fieldmd: 0x254
-  __TEXT.__swift5_proto: 0x1a0
-  __TEXT.__swift5_types: 0x44
-  __TEXT.__objc_methname: 0xdc
+  __TEXT.__const: 0x1e84
+  __TEXT.__cstring: 0x1977
+  __TEXT.__swift5_typeref: 0xbba
+  __TEXT.__swift5_reflstr: 0x428
+  __TEXT.__swift5_assocty: 0x470
+  __TEXT.__constg_swiftt: 0x3a8
+  __TEXT.__swift5_fieldmd: 0x2d4
+  __TEXT.__objc_methname: 0x131
+  __TEXT.__swift5_proto: 0x1bc
+  __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x7b8
-  __TEXT.__eh_frame: 0x7d0
-  __DATA_CONST.__auth_got: 0x458
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__auth_ptr: 0x6a8
-  __DATA_CONST.__const: 0x688
+  __TEXT.__unwind_info: 0x838
+  __TEXT.__eh_frame: 0x8e8
+  __DATA_CONST.__auth_got: 0x4c0
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0x6a0
+  __DATA_CONST.__const: 0x818
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x150
-  __DATA.__objc_selrefs: 0x70
+  __DATA.__objc_selrefs: 0x88
   __DATA.__objc_data: 0xc0
-  __DATA.__data: 0x878
-  __DATA.__common: 0x180
-  __DATA.__bss: 0x3458
+  __DATA.__data: 0x8f0
+  __DATA.__common: 0x160
+  __DATA.__bss: 0x37d8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
-  Functions: 543
-  Symbols:   92
-  CStrings:  105
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 569
+  Symbols:   116
+  CStrings:  118
 
Symbols:
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceSupportsClosedLoopHaptics
+ _MobileGestalt_get_iPadCapability
+ _MobileGestalt_get_ringerButtonCapability
+ _MobileGestalt_get_ringerSwitchCapability
+ _MobileGestalt_get_telephonyCapability
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_UIDevice
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_retain_x25
+ _swift_errorRelease
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_willThrow
- _swift_bridgeObjectRelease_n
CStrings:
+ "#root"
+ "CHANGE_WITH_BUTTONS"
+ "Calendar%!A(MISSING)larm"
+ "Change with Buttons"
+ "DEFAULT_ALERTS"
+ "HAPTICS"
+ "HEADPHONE_LEVEL_LIMIT_SETTING"
+ "HEADPHONE_LEVEL_LIMIT_SETTING#SHSHeadphoneLevelLimitSwitchKey"
+ "KEYBOARD_FEEDBACK"
+ "Keyboard Feedback"
+ "LOCK_SOUND_SWITCH"
+ "NEW_MAIL"
+ "Personalized%!S(MISSING)patial%!A(MISSING)udio"
+ "Reminder%!A(MISSING)lerts"
+ "Ringtone"
+ "SENT_MAIL"
+ "SHOW_IN_STATUS_BAR"
+ "SILENT_MODE"
+ "SYSTEM_HAPTICS"
+ "Show in Status Bar"
+ "Sounds And Haptics Deep Links"
+ "Text_Messages"
+ "The 'Change with Buttons' setting is located within the 'Sounds & Haptics' in the iPhone iOS Settings app. This setting allows for changing value with buttons."
+ "The 'Haptics' setting is located within the 'Sounds & Haptics' in the iPhone iOS Settings app. This setting allows for changing when haptics play during ringtones and alerts"
+ "The 'Keyboard Feedback' setting is located within the 'Sounds & Haptics' in the iPhone iOS Settings app. This setting allows for changing of keyboard sound and haptic."
+ "The 'Lock Sound' setting is located within the 'Sounds & Haptics' in the iPhone iOS Settings app. This setting allows for changing lock sound."
+ "The 'Ringtone' setting is located within the 'Sounds & Haptics' in the iPhone iOS Settings app. This setting allows for changing the ringtone"
+ "The 'Show in Status Bar' setting is located within the 'Sounds & Haptics' in the iPhone iOS Settings app. This setting shwows your silent mode in the status bar."
+ "The 'System Haptics' setting is located within the 'Sounds & Haptics' in the iPhone iOS Settings app. This setting allows turning on system haptics."
+ "Voicemail"
+ "_feedbackSupportLevel"
+ "com.apple.Preferences"
+ "com.apple.mobilemail"
+ "currentDevice"
+ "haptics for ringtones and alerts"
+ "headphone audio sounds"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "settings-navigation://com.apple.Settings.Sounds/"
- "Sound & Haptics Setting"
- "calendarAlerts"
- "defaultAlerts"
- "headphoneSafety"
- "newMail"
- "newVoicemail"
- "personalizedSpatialAudio"
- "reduceLoudAudio"
- "reminderAlerts"
- "root"
- "sentMail"
- "settings-navigation://com.apple.Settings.Sounds"
- "settings-navigation://com.apple.Settings.Sounds/Calendar%!A(MISSING)larm"
- "settings-navigation://com.apple.Settings.Sounds/DEFAULT_ALERTS"
- "settings-navigation://com.apple.Settings.Sounds/HEADPHONE_LEVEL_LIMIT_SETTING"
- "settings-navigation://com.apple.Settings.Sounds/HEADPHONE_LEVEL_LIMIT_SETTING#SHSHeadphoneLevelLimitSwitchKey"
- "settings-navigation://com.apple.Settings.Sounds/NEW_MAIL"
- "settings-navigation://com.apple.Settings.Sounds/Personalized%!S(MISSING)patial%!A(MISSING)udio"
- "settings-navigation://com.apple.Settings.Sounds/Reminder%!A(MISSING)lerts"
- "settings-navigation://com.apple.Settings.Sounds/SENT_MAIL"
- "settings-navigation://com.apple.Settings.Sounds/SILENT_MODE"
- "settings-navigation://com.apple.Settings.Sounds/Text_Messages"
- "settings-navigation://com.apple.Settings.Sounds/Voicemail"
- "textTone"

```
