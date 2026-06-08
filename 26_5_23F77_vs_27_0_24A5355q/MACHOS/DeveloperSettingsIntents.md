## DeveloperSettingsIntents

> `/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents`

```diff

-1150.4.4.0.0
-  __TEXT.__text: 0x8b50
-  __TEXT.__auth_stubs: 0x7a0
+1163.0.100.0.0
+  __TEXT.__text: 0x8e18
+  __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_stubs: 0x160
-  __TEXT.__const: 0xae2
+  __TEXT.__const: 0xb02
   __TEXT.__objc_classname: 0x43
   __TEXT.__objc_methname: 0x18d
   __TEXT.__objc_methtype: 0x2e
   __TEXT.__constg_swiftt: 0x118
   __TEXT.__swift5_typeref: 0x356
-  __TEXT.__swift5_reflstr: 0x65a
+  __TEXT.__swift5_reflstr: 0x63a
   __TEXT.__swift5_fieldmd: 0x35c
-  __TEXT.__cstring: 0x346e
+  __TEXT.__cstring: 0x34be
   __TEXT.__oslogstring: 0x2b
   __TEXT.__swift5_proto: 0x84
   __TEXT.__swift5_types: 0x20

   __TEXT.__swift5_capture: 0x6c
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__unwind_info: 0x298
   __TEXT.__eh_frame: 0x2b0
-  __DATA_CONST.__auth_got: 0x3d8
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__auth_ptr: 0x478
   __DATA_CONST.__const: 0x940
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x428
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_ptr: 0x488
   __DATA.__objc_const: 0x130
   __DATA.__objc_selrefs: 0x58
   __DATA.__objc_data: 0x50

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 583123AC-0F42-3C2B-AB01-40B805D48241
-  Functions: 199
-  Symbols:   103
-  CStrings:  190
+  UUID: 4C6BF8EC-78C2-306E-94E9-669F9D928EE2
+  Functions: 201
+  Symbols:   111
+  CStrings:  192
 
Symbols:
+ _PSBundlePathForPreferenceBundle
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ _objc_retain_x26
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x28
+ _swift_retain_x2
+ _swift_retain_x25
+ _swift_retain_x28
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_release_x24
- _objc_retain_x25
- _swift_retain
CStrings:
+ "PAIRED_MACS"
+ "PHOTOS_UPLOAD_DEVELOPER_MODE"
+ "PairedMacsDeveloperSettings"
+ "Resource Upload Test Mode"
+ "The “Paired Macs” setting is in the iOS Settings app under “Developer” pane. This setting allows users to see audit history and manage Macs that have paired with their device."
+ "The “Resource Upload Test Mode” setting is in the iOS Settings app under “Developer” pane. This setting allows developers to enable developer overrides for testing Background Resource Upload extensions."
+ "background resource upload"
+ "upload overrides"
- "CLEAR_TRUSTED_COMPUTERS"
- "Clear Trusted Computers"
- "NFC Pass Key Optional"
- "NFC_PASS_KEY_OPTIONAL"
- "The “Clear Trusted Computers” setting is in the iOS Settings app under “Developer” pane. This setting allows users to clear trusted computers"
- "The “NFC Pass Key Optional” setting is in the iOS Settings app under “Developer” pane. This setting allows users to turn on or turn off enabling NFC Pass Key optional for Wallet testing."

```
