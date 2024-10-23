## SafetyCheckAppIntents

> `/System/Library/ExtensionKit/Extensions/SafetyCheckAppIntents.appex/SafetyCheckAppIntents`

```diff

-422.0.27.0.0
-  __TEXT.__text: 0x3614
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__const: 0x6f4
-  __TEXT.__cstring: 0x805
-  __TEXT.__constg_swiftt: 0xc0
-  __TEXT.__swift5_typeref: 0x346
-  __TEXT.__swift5_fieldmd: 0x80
-  __TEXT.__swift5_proto: 0x60
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_reflstr: 0x9f
-  __TEXT.__swift5_assocty: 0xc0
+423.0.44.0.0
+  __TEXT.__text: 0x3eb4
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__const: 0x904
+  __TEXT.__cstring: 0x745
+  __TEXT.__constg_swiftt: 0xf8
+  __TEXT.__swift5_typeref: 0x3b4
+  __TEXT.__swift5_fieldmd: 0xac
+  __TEXT.__swift5_proto: 0x80
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift5_reflstr: 0xcd
+  __TEXT.__swift5_assocty: 0x130
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1e0
-  __TEXT.__eh_frame: 0x68
-  __DATA_CONST.__auth_got: 0x260
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x3b8
-  __DATA_CONST.__const: 0x290
+  __TEXT.__objc_methname: 0x40
+  __TEXT.__unwind_info: 0x278
+  __TEXT.__eh_frame: 0x1c8
+  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x4a8
+  __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__data: 0x238
-  __DATA.__bss: 0xc10
-  __DATA.__common: 0x50
+  __DATA.__objc_selrefs: 0x20
+  __DATA.__data: 0x298
+  __DATA.__bss: 0x1010
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI
+  - /System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 126
-  Symbols:   60
-  CStrings:  26
+  Functions: 159
+  Symbols:   72
+  CStrings:  28
 
Symbols:
+ _OBJC_CLASS_$_PUIContinuityLayoutManager
+ _OBJC_CLASS_$_UIDevice
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_msgSend
+ _objc_release_x22
+ _objc_retainAutoreleasedReturnValue
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_task_switch
- __swiftEmptyDictionarySingleton
- _swift_bridgeObjectRelease_n
- _swift_retain
CStrings:
+ "#root"
+ "EMERGENCY_RESET"
+ "MANAGE_SHARING"
+ "currentDevice"
+ "isPhoneMirroringActive"
+ "sf_isiPhone"
+ "sharedInstance"
- "emergencyReset"
- "manageSharing"
- "root"
- "settings-navigation://com.apple.Settings.PrivacyAndSecurity/SAFETY_CHECK/EMERGENCY_RESET"
- "settings-navigation://com.apple.Settings.PrivacyAndSecurity/SAFETY_CHECK/MANAGE_SHARING"

```
