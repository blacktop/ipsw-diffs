## SocialAccountNotificationPlugin

> `/System/Library/Accounts/Notification/SocialAccountNotificationPlugin.bundle/SocialAccountNotificationPlugin`

```diff

-772.0.0.0.0
-  __TEXT.__text: 0x6c8
-  __TEXT.__auth_stubs: 0x1c0
+774.0.0.0.0
+  __TEXT.__text: 0x6b8
   __TEXT.__objc_methlist: 0x1bc
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__ustring: 0x34
   __TEXT.__cstring: 0x105
   __TEXT.__unwind_info: 0x88
-  __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x4b7
-  __TEXT.__objc_methtype: 0x1f5
-  __TEXT.__objc_stubs: 0x300
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x298
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14F276E4-EFAE-37F9-B1F3-19BF194EC2F3
+  UUID: A2C0794B-A4A0-396C-891A-A33D5A1E90B1
   Functions: 8
-  Symbols:   46
-  CStrings:  103
+  Symbols:   47
+  CStrings:  15
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x4
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
Functions:
~ sub_2a6fabecc -> sub_23bf5decc : 336 -> 356
~ sub_2a6fac124 -> sub_23bf5e138 : 628 -> 592
~ sub_2a6fac398 -> sub_23bf5e388 : 196 -> 200
~ sub_2a6fac45c -> sub_23bf5e450 : 172 -> 168
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
- "NSObject"
- "Q16@0:8"
- "SLAccountNotificationPlugin"
- "SLAccountNotificationPluginAdditions"
- "SLTwitterCleanupPushDestinationsURL"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accountExistsForAccountTypeIdentifier:inStore:"
- "_accountState"
- "_urlEncodedString"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountType"
- "accountTypeWithIdentifier:handler:"
- "accountsWithAccountType:handler:"
- "accountsWithAccountTypeIdentifierExist:"
- "autorelease"
- "base64Encoding"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "cleanupTwitterPushDestinationsForAccount:accountStore:"
- "conformsToProtocol:"
- "count"
- "dataUsingEncoding:"
- "debugDescription"
- "description"
- "hash"
- "i"
- "identifier"
- "init"
- "initWithAccount:"
- "initWithEnvironmentName:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "mainRunLoop"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "publicToken"
- "release"
- "requestWithURL:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scheduleInRunLoop:"
- "self"
- "sendSynchronousRequest:returningResponse:error:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "signedURLRequestWithURLRequest:"
- "stringWithFormat:"
- "superclass"
- "username"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "zone"

```
