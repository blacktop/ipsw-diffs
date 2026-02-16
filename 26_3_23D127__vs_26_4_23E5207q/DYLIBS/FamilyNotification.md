## FamilyNotification

> `/System/Library/PrivateFrameworks/FamilyNotification.framework/FamilyNotification`

```diff

-254.325.7.0.0
-  __TEXT.__text: 0x23b4
-  __TEXT.__auth_stubs: 0x2c0
+254.475.11.0.0
+  __TEXT.__text: 0x252c
+  __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_methlist: 0x55c
   __TEXT.__cstring: 0x401
   __TEXT.__const: 0x28

   __DATA_CONST.__objc_selrefs: 0x418
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x170
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x8b8

   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BF9B60E-6EBB-317F-B9CB-EFF91C2E21B3
+  UUID: 9F6F17D5-FCD8-3B57-BB3C-595423401BCF
   Functions: 87
-  Symbols:   388
+  Symbols:   383
   CStrings:  309
 
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_release_x23
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ __FALogSystem : 68 -> 84
~ -[FAFamilyNotifier initWithIdentifier:machServiceName:] : 216 -> 208
~ -[FAFamilyNotifier deliverNotification:] : 204 -> 208
~ ___40-[FAFamilyNotifier deliverNotification:]_block_invoke : 216 -> 220
~ -[FAFamilyNotifier removeNotificationWithIdentifier:] : 204 -> 208
~ ___53-[FAFamilyNotifier removeNotificationWithIdentifier:]_block_invoke : 216 -> 220
~ -[FAFamilyNotifier removeAllNotifications] : 100 -> 108
~ ___42-[FAFamilyNotifier removeAllNotifications]_block_invoke : 192 -> 196
~ -[FAFamilyNotifier _pendingNotificationsWithClientIdentifier:] : 468 -> 464
~ ___62-[FAFamilyNotifier _pendingNotificationsWithClientIdentifier:]_block_invoke : 212 -> 216
~ ___62-[FAFamilyNotifier _pendingNotificationsWithClientIdentifier:]_block_invoke.2 : 96 -> 112
~ -[FAFamilyNotifier pendingNotifications] : 88 -> 96
~ -[FAFamilyNotifier agentConnection] : 720 -> 744
~ ___35-[FAFamilyNotifier agentConnection]_block_invoke_3 : 220 -> 224
~ -[FAFamilyNotifier _agentConnectionWasInterrupted] : 200 -> 204
~ -[FAFamilyNotifier _agentConnectionWasInvalidated] : 200 -> 204
~ -[FAFamilyNotifier _agentConnectionFailedToBootstrap] : 200 -> 204
~ -[FAFamilyNotifier listener:shouldAcceptNewConnection:] : 128 -> 132
~ -[FAFamilyNotifier didActivateNotification:] : 144 -> 152
~ -[FAFamilyNotifier didDismissNotification:] : 144 -> 152
~ -[FAFamilyNotifier didClearNotification:] : 144 -> 152
~ -[FAFamilyNotification init] : 124 -> 128
~ -[FAFamilyNotification initWithCoder:] : 1024 -> 1088
~ -[FAFamilyNotification encodeWithCoder:] : 468 -> 476
~ -[FAFamilyNotification cacheDictionaryRepresentation] : 812 -> 848
~ -[FAFamilyNotification initWithCacheDictionaryRepresentation:] : 968 -> 1076
~ -[FAFamilyNotification description] : 296 -> 324

```
