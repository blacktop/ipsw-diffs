## FindMyDeviceAccountNotificationPlugin

> `/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin`

```diff

-455.35.2.23.5
-  __TEXT.__text: 0x1c6c
-  __TEXT.__auth_stubs: 0x1c0
+479.30.5.16.3
+  __TEXT.__text: 0x1b64
   __TEXT.__objc_methlist: 0x1c4
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__oslogstring: 0x16b
-  __TEXT.__cstring: 0x1eb7
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0x4b6
-  __TEXT.__objc_methtype: 0x1fe
-  __TEXT.__objc_stubs: 0x3e0
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0xb28
+  __TEXT.__cstring: 0x1f8a
+  __TEXT.__unwind_info: 0xa0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xb50
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e0
-  __AUTH_CONST.__auth_got: 0xf0
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x2c00
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x2ca0
   __AUTH_CONST.__objc_const: 0x270
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x1f0
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x120
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AB002AE6-B152-3153-8466-75C30163117F
-  Functions: 61
-  Symbols:   48
-  CStrings:  825
+  UUID: 94814CB4-48C0-3A3D-9CA2-21DE539053B3
+  Functions: 67
+  Symbols:   49
+  CStrings:  744
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
CStrings:
+ "com.apple.FindMyDevice.PartnerFinancing.access"
+ "com.apple.findmy.RepairCFUChangedNotification"
+ "com.apple.icloud.FindMyDevice.RepairDeviceLookup.access"
+ "fmEnterpriseLockType"
+ "mock"
+ "partnerFinance"
+ "partnerFinanceVerify"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8B16"
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
- "FMIPAdditions"
- "FindMyDeviceAccountNotificationPlugin"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_quickFetchFMIPEnabledstate"
- "aa_altDSID"
- "aa_authToken"
- "aa_fmipToken"
- "aa_isAccountClass:"
- "aa_isSuspended"
- "aa_personID"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountType"
- "autorelease"
- "boolForKey:inDomain:"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "conformsToProtocol:"
- "copy"
- "dataclassProperties"
- "debugDescription"
- "description"
- "dictionary"
- "didChangeFMIPAccountInfo:"
- "fm_safelyMapKey:toObject:"
- "fmipAccountInfoForProactiveChanges"
- "fmipAccountInfoWithTokens:"
- "fmipStateWithCompletion:"
- "fmwAccountInfoForProactiveChanges"
- "fmwAccountInfoWithTokens:"
- "hash"
- "identifier"
- "initWithDescription:andTimeout:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPropertyDirty:"
- "isProxy"
- "mutableCopy"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "primaryAppleAccountRemoved"
- "release"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sharedInstance"
- "signal"
- "stringForKey:inDomain:"
- "superclass"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "wait"
- "zone"

```
