## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-616.0.1.0.0
-  __TEXT.__text: 0x3812c
+623.0.0.0.0
+  __TEXT.__text: 0x38274
   __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_methlist: 0x223c
+  __TEXT.__objc_methlist: 0x225c
   __TEXT.__const: 0x2b4
   __TEXT.__oslogstring: 0x625a
   __TEXT.__cstring: 0x14a7

   __TEXT.__unwind_info: 0xd88
   __TEXT.__eh_frame: 0x220
   __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0xb0bc
-  __TEXT.__objc_methtype: 0x19cf
-  __TEXT.__objc_stubs: 0x91c0
+  __TEXT.__objc_methname: 0xb194
+  __TEXT.__objc_methtype: 0x19dd
+  __TEXT.__objc_stubs: 0x9260
   __DATA_CONST.__got: 0x898
-  __DATA_CONST.__const: 0x1110
+  __DATA_CONST.__const: 0x10f8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2980
+  __DATA_CONST.__objc_selrefs: 0x29b0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x888
   __AUTH_CONST.__const: 0x5b0
   __AUTH_CONST.__cfstring: 0xb20
-  __AUTH_CONST.__objc_const: 0x5988
+  __AUTH_CONST.__objc_const: 0x5990
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd8
   __AUTH.__data: 0x98

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
+  - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore
   - /System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 583543EC-8683-3202-AC9B-699F0D74FC7D
-  Functions: 1032
-  Symbols:   4159
-  CStrings:  2262
+  UUID: 1F2FBAC0-A442-394C-AFC9-8B48BD8CC198
+  Functions: 1034
+  Symbols:   4162
+  CStrings:  2269
 
Symbols:
+ -[UNSNotificationSettingsService notificationSettingsForBundleIdentifier:calculatedSettings:]
+ -[UNSUserNotificationServerSettingsConnectionListener getNotificationSettingsForSourceIdentifier:withCompletionHandler:]
+ GCC_except_table20
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_UserNotificationsServer
+ _objc_msgSend$iconDateComponents
+ _objc_msgSend$iconUTI
+ _objc_msgSend$notificationSettingsForBundleIdentifier:calculatedSettings:
+ _objc_msgSend$variantWithFormat:dateComponentDetails:
+ _objc_msgSend$variantWithFormat:uti:
- GCC_except_table17
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_UserNotificationsServer
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_UserNotificationsServer
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_UserNotificationsServer
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_UserNotificationsServer
Functions:
~ -[UNSNotificationSettingsService notificationSettingsForBundleIdentifier:] : 104 -> 8
+ -[UNSNotificationSettingsService notificationSettingsForBundleIdentifier:calculatedSettings:]
~ -[UNSDefaultDataProvider _queue_bulletinForNotification:] : 6300 -> 6388
+ -[UNSUserNotificationServerSettingsConnectionListener getNotificationSettingsForSourceIdentifier:withCompletionHandler:]
CStrings:
+ "@28@0:8@16B24"
+ "getNotificationSettingsForSourceIdentifier:withCompletionHandler:"
+ "iconDateComponents"
+ "iconUTI"
+ "notificationSettingsForBundleIdentifier:calculatedSettings:"
+ "variantWithFormat:dateComponentDetails:"
+ "variantWithFormat:uti:"

```
