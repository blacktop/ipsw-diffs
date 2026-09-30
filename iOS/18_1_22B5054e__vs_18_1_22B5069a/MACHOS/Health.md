## Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

-5200.1.9.1.2
-  __TEXT.__text: 0xc2230
-  __TEXT.__auth_stubs: 0x4950
+5200.1.15.1.2
+  __TEXT.__text: 0xc261c
+  __TEXT.__auth_stubs: 0x4940
   __TEXT.__objc_methlist: 0x6dc
   __TEXT.__const: 0x5404
   __TEXT.__cstring: 0x7fd5

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x27d0
   __TEXT.__eh_frame: 0x2130
-  __DATA_CONST.__auth_got: 0x24a8
+  __DATA_CONST.__auth_got: 0x24a0
   __DATA_CONST.__got: 0x1160
-  __DATA_CONST.__auth_ptr: 0x10f0
-  __DATA_CONST.__const: 0x4960
+  __DATA_CONST.__auth_ptr: 0x1108
+  __DATA_CONST.__const: 0x4968
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__objc_data: 0x2780
   __DATA.__data: 0x4a20
   __DATA.__objc_stublist: 0x58
-  __DATA.__common: 0x440
+  __DATA.__common: 0x458
   __DATA.__bss: 0x7480
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3485
+  Functions: 3486
   Symbols:   2086
-  CStrings:  1694
+  CStrings:  1695
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- _$s10AppIntents0A6IntentPAAE11descriptionAA0C11DescriptionVSgvgZ
CStrings:
+ "A type of health data, such as Steps."
+ "For a given health data type such as Steps, opens the view in Health that shows the data for the type."
+ "Opens Health to your sleep schedule."
+ "Opens the specified view in Health."
- "For a given health data type such as Steps, open the view in Health that shows the data for the type."
- "Opens Health to show the given type of health data, such as Steps"
- "Opens Health to your sleep schedule within the Sleep Data Type."

```
