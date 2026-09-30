## GeneralSettingsIntents

> `/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents`

```diff

-1226.0.0.0.0
-  __TEXT.__text: 0xde3c
-  __TEXT.__auth_stubs: 0xad0
+1230.0.0.0.0
+  __TEXT.__text: 0xe040
+  __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_methlist: 0x19c
   __TEXT.__const: 0x1280
-  __TEXT.__cstring: 0x2af1
+  __TEXT.__cstring: 0x29f1
   __TEXT.__constg_swiftt: 0x270
   __TEXT.__swift5_typeref: 0x74d
-  __TEXT.__swift5_fieldmd: 0x2cc
+  __TEXT.__swift5_fieldmd: 0x2c0
   __TEXT.__objc_methname: 0x285
   __TEXT.__swift5_types: 0x38
   __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methtype: 0xd2
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0x410
+  __TEXT.__swift5_reflstr: 0x400
   __TEXT.__swift5_assocty: 0x268
   __TEXT.__swift5_proto: 0xe8
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__unwind_info: 0x4c8
   __TEXT.__eh_frame: 0x600
-  __DATA_CONST.__auth_got: 0x568
+  __DATA_CONST.__auth_got: 0x578
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x618
-  __DATA_CONST.__const: 0x778
+  __DATA_CONST.__const: 0x758
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__common: 0xa8
   __DATA.__bss: 0x1d10
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MatterSupport.framework/MatterSupport
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 93D7CC44-D21A-3F56-95B5-2672E9185C38
+  UUID: C6160F3D-9EDD-3325-A592-A1384EC84779
   Functions: 361
-  Symbols:   120
-  CStrings:  228
+  Symbols:   121
+  CStrings:  224
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
Functions:
~ sub_100001b28 -> sub_100001b88 : 912 -> 880
~ sub_100001eb8 -> sub_100001ef8 : 132 -> 128
~ sub_100002bd0 -> sub_100002c0c : 14812 -> 14364
~ sub_1000065ac -> sub_100006428 : 132 -> 128
~ sub_1000080f8 -> sub_100007f70 : 32 -> 144
~ sub_100008118 -> sub_100008000 : 1272 -> 1484
~ sub_100008610 -> sub_1000085cc : 28 -> 140
~ sub_10000862c -> sub_100008658 : 1276 -> 1496
~ sub_100008c48 -> sub_100008d50 : 28 -> 140
~ sub_100008c64 -> sub_100008ddc : 1024 -> 1260
CStrings:
+ "com.apple.demo-settings"
- "SOFTWARE_UPDATE_LINK"
- "The “Software Update” setting is in the iOS Settings app under the “General” pane. This setting allows users to check and install software updates."
- "automatic updates"
- "check for update"
- "security updates"

```
