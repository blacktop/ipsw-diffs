## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-491.0.0.0.0
-  __TEXT.__text: 0x56f58
+491.2.1.0.0
+  __TEXT.__text: 0x56fbc
   __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x45f4
+  __TEXT.__objc_methlist: 0x45fc
   __TEXT.__cstring: 0x4726
   __TEXT.__oslogstring: 0x6fad
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x488
-  __TEXT.__unwind_info: 0x1288
+  __TEXT.__unwind_info: 0x128c
   __TEXT.__objc_classname: 0xae6
-  __TEXT.__objc_methname: 0x12ee6
-  __TEXT.__objc_methtype: 0x1f2d
-  __TEXT.__objc_stubs: 0xd6a0
+  __TEXT.__objc_methname: 0x12f6e
+  __TEXT.__objc_methtype: 0x1f30
+  __TEXT.__objc_stubs: 0xd6e0
   __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x1828
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb440
-  __DATA_CONST.__objc_selrefs: 0x38e0
+  __DATA_CONST.__objc_const: 0xb470
+  __DATA_CONST.__objc_selrefs: 0x38f0
   __AUTH_CONST.__cfstring: 0x4620
   __AUTH_CONST.__objc_const: 0x13e8
   __AUTH_CONST.__const: 0x760

   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x568
   __DATA.__objc_superrefs: 0x168
-  __DATA.__objc_ivar: 0x75c
+  __DATA.__objc_ivar: 0x760
   __DATA.__data: 0xc98
   __DATA.__bss: 0x1
   __DATA_DIRTY.__objc_data: 0x1090

   - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1989
-  Symbols:   7485
-  CStrings:  3957
+  Functions: 1990
+  Symbols:   7490
+  CStrings:  3961
 
Symbols:
+ +[UNSNotificationRecordRemoveUpdate updateWithNotificationRecord:shouldSync:]
+ -[UNSDefaultDataProvider _queue_withdrawBulletinForNotification:shouldSync:]
+ -[UNSDefaultDataProvider _queue_withdrawBulletinForNotification:shouldSync:].cold.1
+ -[UNSNotificationRecordUpdate _initWithNotificationRecord:shouldSync:]
+ -[UNSNotificationRecordUpdate shouldSync]
+ -[UNSNotificationRepository _queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSyncForRemoval:forBundleIdentifier:]
+ _OBJC_IVAR_$_UNSNotificationRecordUpdate._shouldSync
+ ___205-[UNSNotificationRepository _queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSyncForRemoval:forBundleIdentifier:]_block_invoke
+ _objc_msgSend$_initWithNotificationRecord:shouldSync:
+ _objc_msgSend$_queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSyncForRemoval:forBundleIdentifier:
+ _objc_msgSend$_queue_withdrawBulletinForNotification:shouldSync:
+ _objc_msgSend$shouldSync
+ _objc_msgSend$updateWithNotificationRecord:shouldSync:
+ _objc_msgSend$withdrawBulletinWithPublisherBulletinID:shouldSync:
- +[UNSNotificationRecordRemoveUpdate updateWithNotificationRecord:]
- -[UNSDefaultDataProvider _queue_withdrawBulletinForNotification:]
- -[UNSDefaultDataProvider _queue_withdrawBulletinForNotification:].cold.1
- -[UNSNotificationRecordUpdate _initWithNotificationRecord:]
- -[UNSNotificationRepository _queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:forBundleIdentifier:]
- ___184-[UNSNotificationRepository _queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:forBundleIdentifier:]_block_invoke
- _objc_msgSend$_initWithNotificationRecord:
- _objc_msgSend$_queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:forBundleIdentifier:
- _objc_msgSend$_queue_withdrawBulletinForNotification:
- _objc_msgSend$withdrawBulletinWithPublisherBulletinID:
CStrings:
+ "TB,R,N,V_shouldSync"
+ "_initWithNotificationRecord:shouldSync:"
+ "_queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSyncForRemoval:forBundleIdentifier:"
+ "_queue_withdrawBulletinForNotification:shouldSync:"
+ "_shouldSync"
+ "shouldSync"
+ "updateWithNotificationRecord:shouldSync:"
+ "v64@0:8@16@24@32@40B48B52@56"
+ "withdrawBulletinWithPublisherBulletinID:shouldSync:"
- "_initWithNotificationRecord:"
- "_queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:forBundleIdentifier:"
- "_queue_withdrawBulletinForNotification:"
- "v60@0:8@16@24@32@40B48@52"
- "withdrawBulletinWithPublisherBulletinID:"

```
