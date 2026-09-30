## LockScreen

> `/System/Library/ExtensionKit/Extensions/LockScreen.appex/Contents/MacOS/LockScreen`

```diff

-15.0.0.0.0
-  __TEXT.__text: 0x37b9c
-  __TEXT.__auth_stubs: 0x1310
+17.0.0.0.0
+  __TEXT.__text: 0x38c34
+  __TEXT.__auth_stubs: 0x1410
   __TEXT.__objc_methlist: 0x88
-  __TEXT.__cstring: 0x27aa
-  __TEXT.__const: 0x2514
-  __TEXT.__constg_swiftt: 0x111c
-  __TEXT.__swift5_typeref: 0x2ec2
+  __TEXT.__cstring: 0x28ca
+  __TEXT.__const: 0x25a4
+  __TEXT.__constg_swiftt: 0x116c
+  __TEXT.__swift5_typeref: 0x2f58
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xb38
+  __TEXT.__swift5_reflstr: 0xb68
   __TEXT.__swift5_assocty: 0x1c8
-  __TEXT.__swift5_fieldmd: 0x60c
-  __TEXT.__swift5_capture: 0xac4
+  __TEXT.__swift5_fieldmd: 0x624
+  __TEXT.__swift5_capture: 0xad4
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x64
-  __TEXT.__objc_methname: 0xa60
+  __TEXT.__objc_methname: 0xa6e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__oslogstring: 0x85
   __TEXT.__objc_classname: 0x29
   __TEXT.__objc_methtype: 0xdc
-  __TEXT.__unwind_info: 0xe38
+  __TEXT.__unwind_info: 0xe50
   __TEXT.__eh_frame: 0xf78
-  __DATA_CONST.__auth_got: 0x988
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__auth_ptr: 0x7d0
-  __DATA_CONST.__const: 0x1d00
+  __DATA_CONST.__auth_got: 0xa08
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__auth_ptr: 0x7f8
+  __DATA_CONST.__const: 0x1d28
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA.__objc_const: 0x1148
-  __DATA.__objc_selrefs: 0x2d0
+  __DATA.__objc_const: 0x1188
+  __DATA.__objc_selrefs: 0x2d8
   __DATA.__objc_data: 0x400
-  __DATA.__data: 0x2238
-  __DATA.__bss: 0x1280
-  __DATA.__common: 0x78
+  __DATA.__data: 0x22f0
+  __DATA.__bss: 0x12a0
+  __DATA.__common: 0x80
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
+  - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /System/Library/Frameworks/ScreenSaver.framework/Versions/A/ScreenSaver
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
   - /System/Library/PrivateFrameworks/LocalAuthenticationUI.framework/Versions/A/LocalAuthenticationUI
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1296
-  Symbols:   177
-  CStrings:  240
+  Functions: 1310
+  Symbols:   180
+  CStrings:  247
 
Symbols:
+ _NSApplicationDidBecomeActiveNotification
+ _OBJC_CLASS_$_NSNotificationCenter
+ __swiftEmptySetSingleton
CStrings:
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/LockScreenSettings/Lock Screen/LockScreenController.swift"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/LockScreenSettings/Shared/Authentication.swift"
+ "Could not change device grace period. (Error: "
+ "Fetched device grace period ("
+ "Password immediately required when iPhone Mirroring is set to automatically authenticate."
+ "Successfully changed device grace period from "
+ "_iPhoneMirroringInAutoMode"
+ "fetchDeviceGracePeriod()"
+ "subscriptions"
+ "syncPreboot()"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/LockScreenSettings/Lock Screen/LockScreenController.swift"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/LockScreenSettings/Shared/Authentication.swift"
- "changeLockScreen(message:)"

```
