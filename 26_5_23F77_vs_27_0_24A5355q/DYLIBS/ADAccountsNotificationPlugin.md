## ADAccountsNotificationPlugin

> `/System/Library/Accounts/Notification/ADAccountsNotificationPlugin.bundle/ADAccountsNotificationPlugin`

```diff

-637.5.1.0.0
-  __TEXT.__text: 0xa5c
-  __TEXT.__auth_stubs: 0x1f0
+638.0.7.0.0
+  __TEXT.__text: 0x9d0
   __TEXT.__objc_methlist: 0x1a4
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x255
   __TEXT.__oslogstring: 0x45
   __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methname: 0x451
-  __TEXT.__objc_methtype: 0x204
-  __TEXT.__objc_stubs: 0x320
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x230
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x8

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ABE78A89-8620-3B48-8C1F-729E6ACD8FFF
+  UUID: 5C5AA9C3-072A-3DFC-8486-9A181E298DB8
   Functions: 7
-  Symbols:   53
-  CStrings:  124
+  Symbols:   52
+  CStrings:  38
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x3
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x28
Functions:
~ sub_2a6ef4ec4 -> sub_23beccec4 : 1696 -> 1588
~ sub_2a6ef55a0 -> sub_23becd534 : 284 -> 272
~ sub_2a6ef56f8 -> sub_23becd680 : 384 -> 364
CStrings:
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "ADAccountsNotificationPlugin"
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
- "accountType"
- "ams_storefront"
- "autorelease"
- "boolValue"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "checkForStorefrontChangeWithAccount:andOldAccount:"
- "class"
- "conformsToProtocol:"
- "debugDescription"
- "description"
- "getReturnValue:"
- "hash"
- "identifier"
- "init"
- "initWithSuiteName:"
- "invocationWithMethodSignature:"
- "invoke"
- "isActive"
- "isAuthenticated"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "methodSignatureForSelector:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postNotificationForChangeWithAccount:andOldAccount:withType:"
- "protoAccount"
- "purpleBuddyWillRun"
- "release"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setBool:forKey:"
- "setBoolValue:forSetting:"
- "setSelector:"
- "setTarget:"
- "sharedConnection"
- "sharedInstance"
- "stringWithFormat:"
- "superclass"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v40@0:8@16@24@32"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "zone"

```
