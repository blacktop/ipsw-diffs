## AppProtectionUI

> `/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0x127fc
-  __TEXT.__auth_stubs: 0xb10
+35.0.0.0.0
+  __TEXT.__text: 0x143f0
+  __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_methlist: 0x8e8
-  __TEXT.__const: 0x458
-  __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__oslogstring: 0x528
-  __TEXT.__cstring: 0x14f7
-  __TEXT.__constg_swiftt: 0x3c4
-  __TEXT.__swift5_typeref: 0x482
+  __TEXT.__const: 0x468
+  __TEXT.__gcc_except_tab: 0x54
+  __TEXT.__oslogstring: 0x5f3
+  __TEXT.__cstring: 0x1617
+  __TEXT.__constg_swiftt: 0x3cc
+  __TEXT.__swift5_typeref: 0x49a
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x144
   __TEXT.__swift5_fieldmd: 0x218
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x30
-  __TEXT.__swift5_capture: 0x284
+  __TEXT.__swift5_capture: 0x2f4
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x570
+  __TEXT.__unwind_info: 0x598
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_classname: 0x282
-  __TEXT.__objc_methname: 0x2ff2
+  __TEXT.__objc_methname: 0x30cb
   __TEXT.__objc_methtype: 0xfc6
-  __TEXT.__objc_stubs: 0x1c40
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x350
+  __TEXT.__objc_stubs: 0x1c60
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x3b8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa10
+  __DATA_CONST.__objc_selrefs: 0xa58
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x598
-  __AUTH_CONST.__auth_ptr: 0xa0
-  __AUTH_CONST.__const: 0xd88
-  __AUTH_CONST.__cfstring: 0x980
+  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_ptr: 0xb0
+  __AUTH_CONST.__const: 0xec8
+  __AUTH_CONST.__cfstring: 0x9a0
   __AUTH_CONST.__objc_const: 0x28d8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xb28
-  __AUTH.__data: 0x1c0
   __DATA.__objc_ivar: 0xd4
   __DATA.__data: 0x650
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xc0
   __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0xb28
+  __DATA_DIRTY.__data: 0x1e8
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 508
-  Symbols:   499
-  CStrings:  856
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 538
+  Symbols:   527
+  CStrings:  877
 
Symbols:
+ _MKBGetDeviceLockState
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_UNNotificationSettingsCenter
+ _OBJC_CLASS_$__LSOpenConfiguration
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_bridgeErrorToNSError
- __os_log_debug_impl
CStrings:
+ "APBaseShieldView setShieldStyle:%!l(MISSING)u for %!@(MISSING)"
+ "Could not cancel ongoing auth. Error: %!@(MISSING)"
+ "Error opening notifications settings %!@(MISSING)"
+ "Error opening passcode settings %!@(MISSING)"
+ "GO_TO_PASSCODE_SETTINGS"
+ "PASSCODE_REQUIRED"
+ "PASSCODE_REQUIRED_MESSAGE_"
+ "TURN_OFF_CA_MESSAGE"
+ "TURN_OFF_CA_TO_HIDE_X"
+ "WALLET_AND_APPLE_PAY"
+ "abortOngoingAuthWithCompletion:"
+ "criticalAlertSetting"
+ "currentNotificationSettingsCenter"
+ "defaultWorkspace"
+ "notificationSettings"
+ "openURL:configuration:completionHandler:"
+ "prefs:root=PASSCODE#CHANGE_PASSCODE"
+ "setSensitive:"
+ "sourceSettings"
+ "sourceWithIdentifier:"
+ "unknown return %!d(MISSING) from MKBGetDeviceLockState"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "Setting style to: %!l(MISSING)u"

```
