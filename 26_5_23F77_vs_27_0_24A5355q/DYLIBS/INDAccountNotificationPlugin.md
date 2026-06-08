## INDAccountNotificationPlugin

> `/System/Library/Accounts/Notification/INDAccountNotificationPlugin.bundle/INDAccountNotificationPlugin`

```diff

-301.23.4.7.0
-  __TEXT.__text: 0x5c0
-  __TEXT.__auth_stubs: 0x130
+301.24.0.19.0
+  __TEXT.__text: 0x550
   __TEXT.__objc_methlist: 0x19c
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x7d
   __TEXT.__oslogstring: 0x13d
   __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x3a0
-  __TEXT.__objc_methtype: 0x1fb
-  __TEXT.__objc_stubs: 0x160
-  __DATA_CONST.__got: 0x30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x138
-  __AUTH_CONST.__auth_got: 0xa0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x230
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA8A1DBA-E8E0-3EBA-A5C9-F3DDB2AF5AA9
+  UUID: 38E27F3B-4EA4-34D5-8BD2-1E04B5B1E2BD
   Functions: 7
-  Symbols:   33
-  CStrings:  87
+  Symbols:   34
+  CStrings:  16
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x5
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x24
Functions:
~ sub_2a6f69de0 -> sub_23bf27de0 : 1068 -> 1008
~ sub_2a6f6a214 -> sub_23bf281d8 : 244 -> 196
~ sub_2a6f6a308 -> sub_23bf2829c : 72 -> 68
CStrings:
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"ACAccount\"16@\"ACDAccountStore\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24^@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "B44@0:8@16i24@28@36"
- "INAccountNotificationPlugin"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountPropertyForKey:"
- "autorelease"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "clearCacheAndNotify"
- "conformsToProtocol:"
- "containsObject:"
- "date"
- "debugDescription"
- "description"
- "dirtyProperties"
- "hash"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "notifyCloudSubscriptionFeatures"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "registerAccount:foriCloudNotificationsWithReason:completion:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAccountProperty:forKey:"
- "superclass"
- "teardownOffersForAccount:withCompletion:"
- "timeIntervalSinceDate:"
- "unregisterAccount:fromiCloudNotificationsWithCompletion:"
- "v16@0:8"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "zone"

```
