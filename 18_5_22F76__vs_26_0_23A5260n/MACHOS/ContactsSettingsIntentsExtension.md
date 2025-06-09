## ContactsSettingsIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ContactsSettingsIntentsExtension.appex/ContactsSettingsIntentsExtension`

```diff

-1389.600.1.0.0
-  __TEXT.__text: 0x55bc
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__cstring: 0x75c
+1413.100.3.2.5
+  __TEXT.__text: 0x5358
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__cstring: 0x79a
   __TEXT.__swift5_typeref: 0x307
-  __TEXT.__const: 0x7fe
+  __TEXT.__const: 0x86a
   __TEXT.__swift5_reflstr: 0x112
   __TEXT.__swift5_assocty: 0x118
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__unwind_info: 0x258
-  __TEXT.__eh_frame: 0x230
-  __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__auth_ptr: 0x420
-  __DATA_CONST.__const: 0x330
+  __TEXT.__eh_frame: 0x1f8
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__auth_ptr: 0x428
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x1d0
+  __DATA.__data: 0x178
   __DATA.__bss: 0xe80
   __DATA.__common: 0x60
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 80B34044-831D-3EEC-BC4B-5F8E03E88E9A
-  Functions: 165
-  Symbols:   69
-  CStrings:  44
+  UUID: B07CB324-1DAC-31FF-B472-00E82C7473EF
+  Functions: 164
+  Symbols:   67
+  CStrings:  45
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_coroFrameAlloc
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x23
CStrings:
+ "#SIMImport"
+ "/"
+ "/ContactProvider"
+ "/ContactsSortOrder"
+ "/MeCard"
+ "/PersonNameOrder"
+ "/PersonShortName"
+ "/SharedNameAndPhoto"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.MobileAddressBook"
- "ContactsSortOrder"
- "DefaultContacts"
- "ImportSimContacts"
- "MeCard"
- "PersonNameOrder"
- "PersonShortName"
- "SharedNameAndPhoto"
- "prefs://root=CONTACTS&path="

```
