## ASDAccountNotficationPlugin

> `/System/Library/Accounts/Notification/ASDAccountNotficationPlugin.bundle/ASDAccountNotficationPlugin`

```diff

-12.5.8.0.0
-  __TEXT.__text: 0xf64
-  __TEXT.__auth_stubs: 0x1f0
+13.0.33.0.0
+  __TEXT.__text: 0x1060
   __TEXT.__objc_methlist: 0x18c
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0xf3
-  __TEXT.__oslogstring: 0x41b
-  __TEXT.__unwind_info: 0x60
-  __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methname: 0x3a4
-  __TEXT.__objc_methtype: 0x1f3
-  __TEXT.__objc_stubs: 0x1c0
-  __DATA_CONST.__got: 0x40
+  __TEXT.__oslogstring: 0x498
+  __TEXT.__unwind_info: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x150
+  __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x230
   __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F23442E-20B2-3270-9601-3FF32CC20F23
-  Functions: 4
-  Symbols:   47
-  CStrings:  103
+  UUID: EDCC9FFC-3EF9-3A35-A59C-966C15E0B2A1
+  Functions: 5
+  Symbols:   49
+  CStrings:  33
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x8
- _objc_release_x27
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x26
CStrings:
+ "[%{public}@] Attempting to post payload"
+ "[%{public}@] Failed to post payload: %{public}@"
+ "[%{public}@] Not processing sign out for account: %{public}@ changeType: %u"
+ "[%{public}@] Post payload successful"
+ "[%{public}@] Timed out attempting to sbsync"
+ "[%{public}@] sbsync finished with error: %{public}@"
+ "[%{public}@] sbsync finished with result: %d"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "ASDAccountNotificationPlugin"
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
- "[%{public}@] Not processing signout for account: %{public}@ changeType: %u"
- "[%{public}@] sbsync finished with error: %{pubic}@"
- "[%{public}@]: Timed out attempting to sbsync"
- "[%{public}@]: sbsync finished with result: %d"
- "^{_NSZone=}16@0:8"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "ams_DSID"
- "ams_isLocalAccount"
- "ams_isSandboxAccount"
- "ams_isiTunesAccount"
- "autorelease"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "conformsToProtocol:"
- "debugDescription"
- "defaultCenter"
- "description"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "hash"
- "identifier"
- "isActive"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postNotificationName:object:userInfo:deliverImmediately:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "sbsyncIfSubscribedWithAccount:completionBlock:"
- "self"
- "setObject:forKeyedSubscript:"
- "superclass"
- "username"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "zone"

```
