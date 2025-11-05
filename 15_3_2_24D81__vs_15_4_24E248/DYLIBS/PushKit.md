## PushKit

> `/System/Library/Frameworks/PushKit.framework/Versions/A/PushKit`

```diff

 108.200.1.0.0
-  __TEXT.__text: 0x4bb0
+  __TEXT.__text: 0x4c58
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x500
+  __TEXT.__objc_methlist: 0x778
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x84
   __TEXT.__cstring: 0x41b
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x220
   __TEXT.__objc_classname: 0x196
   __TEXT.__objc_methname: 0x1334
   __TEXT.__objc_methtype: 0x308

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_selrefs: 0x4f0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x2e0
-  __AUTH_CONST.__objc_const: 0x11a0
+  __AUTH_CONST.__objc_const: 0xd58
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x3c0

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F2D6F18B-955E-3D57-8C65-B51C8C1BD5B1
-  Functions: 168
-  Symbols:   475
+  UUID: 4236DE69-D019-3B91-AF70-838414F7A35E
+  Functions: 172
+  Symbols:   479
   CStrings:  331
 
Symbols:
+ +[PKUserNotificationsRemoteNotificationServiceConnection sharedInstance].cold.1
+ -[PKUserNotificationsRemoteNotificationServiceConnection initWithBundleIdentifier:].cold.1
+ -[PKUserNotificationsRemoteNotificationServiceConnection registerPushRegistry:completionHandler:].cold.1
+ -[PKUserNotificationsRemoteNotificationServiceConnection unregisterPushRegistry:].cold.1
Functions:
~ -[PKPushRegistry initWithQueue:] : 704 -> 680
~ +[PKUserNotificationsRemoteNotificationServiceConnection sharedInstance] : 84 -> 68
~ -[PKUserNotificationsRemoteNotificationServiceConnection initWithBundleIdentifier:] : 480 -> 416
~ -[PKUserNotificationsRemoteNotificationServiceConnection registerPushRegistry:completionHandler:] : 320 -> 248
~ -[PKUserNotificationsRemoteNotificationServiceConnection _queue_ensureConnection] : 672 -> 648
~ -[PKUserNotificationsRemoteNotificationServiceConnection unregisterPushRegistry:] : 264 -> 200
~ ___81-[PKUserNotificationsRemoteNotificationServiceConnection _queue_ensureConnection]_block_invoke : 176 -> 172
~ __81-[PKUserNotificationsRemoteNotificationServiceConnection _queue_ensureConnection]_block_invoke.91 : 176 -> 172
~ -[PKPublicChannel initWithDictionary:] : 716 -> 720
~ -[PKPublicChannel hash] : 196 -> 192

```
