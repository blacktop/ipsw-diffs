## DonationAccountWatcher

> `/System/Library/Accounts/Notification/DonationAccountWatcher.bundle/DonationAccountWatcher`

```diff

-1123.500.31.0.0
-  __TEXT.__text: 0x3654
-  __TEXT.__auth_stubs: 0x440
+1130.100.1.0.0
+  __TEXT.__text: 0x35e0
   __TEXT.__objc_methlist: 0x284
   __TEXT.__const: 0x158
   __TEXT.__constg_swiftt: 0x110

   __TEXT.__cstring: 0x132
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x138
-  __TEXT.__unwind_info: 0x158
-  __TEXT.__objc_classname: 0x129
-  __TEXT.__objc_methname: 0x4ac
-  __TEXT.__objc_methtype: 0x2b1
-  __TEXT.__objc_stubs: 0x2a0
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1b0
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x228
-  __AUTH_CONST.__const: 0x2d0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__objc_const: 0x378
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH.__objc_data: 0xd8
-  __DATA.__data: 0x150
+  __DATA.__data: 0x148
   __DATA_DIRTY.__objc_data: 0x248
-  __DATA_DIRTY.__data: 0x198
+  __DATA_DIRTY.__data: 0x1a8
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4E4D1E59-2562-39B4-A638-7E3A97C6B2F1
-  Functions: 90
-  Symbols:   70
-  CStrings:  110
+  UUID: 565BCC8B-BE34-3273-9B8E-628D1E2B8B8E
+  Functions: 93
+  Symbols:   79
+  CStrings:  10
 
Symbols:
+ __swiftImmortalRefCount
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x28
+ _swift_release_x20
+ _swift_release_x22
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x9
- _objc_release_x26
- _objc_retain_x26
- _swift_retain
CStrings:
- "#16@0:8"
- ".cxx_destruct"
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
- "CNDonationAccountLogger"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC22DonationAccountWatcher21AccountPropertyParser"
- "_TtC22DonationAccountWatcher25AccountPropertyNameParser"
- "_TtC22DonationAccountWatcher26AccountPropertyEmailParser"
- "_TtC22DonationAccountWatcher6Plugin"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountAdded:"
- "accountChanged:"
- "accountLogger"
- "accountRemoved:"
- "accountType"
- "accountsDidNotChange"
- "addFailureBlock:"
- "autorelease"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "changeFromAccount:toAccount:"
- "class"
- "componentsFromString:"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "defaultProvider"
- "description"
- "donating:"
- "donationDate"
- "donationFailedWithError:"
- "donationValueWithEmailAddress:label:origin:"
- "donationValueWithNameComponents:origin:"
- "expirationDate"
- "firstEmailAddressInString:"
- "hash"
- "identifier"
- "init"
- "initWithBundleIdentifier:donationIdentifier:clusterIdentifier:donationDate:expirationDate:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "logger"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginLoaded"
- "pluginUnloaded"
- "release"
- "removalFailedWithError:"
- "removing:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "store"
- "superclass"
- "username"
- "v16@0:8"
- "v16@?0@\"NSError\"8"
- "v24@0:8@\"ACAccount\"16"
- "v24@0:8@\"CNDonationValue\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "zone"

```
