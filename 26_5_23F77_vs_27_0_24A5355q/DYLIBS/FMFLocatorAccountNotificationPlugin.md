## FMFLocatorAccountNotificationPlugin

> `/System/Library/Accounts/Notification/FMFLocatorAccountNotificationPlugin.bundle/FMFLocatorAccountNotificationPlugin`

```diff

-97.35.2.23.2
-  __TEXT.__text: 0x1884
-  __TEXT.__auth_stubs: 0x220
+101.30.3.1.1
+  __TEXT.__text: 0x162c
   __TEXT.__objc_methlist: 0x24c
-  __TEXT.__cstring: 0x18f
+  __TEXT.__cstring: 0x1c0
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x2b2
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0x632
-  __TEXT.__objc_methtype: 0x2a5
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x60
+  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x308
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x128
   __DATA.__bss: 0x40

   - /System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9661D51C-83B2-3BA7-9715-19C5BFA748FC
+  UUID: E89CB99A-C9FE-3BC9-8F26-D72129AAFFC4
   Functions: 52
-  Symbols:   74
-  CStrings:  179
+  Symbols:   79
+  CStrings:  68
 
Symbols:
+ __os_feature_enabled_impl
+ _isFeatureFindMyQuickSwitchEnabled
+ _isFeatureQuickSwitchEnabled
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x22
CStrings:
+ "CoreTelephony"
+ "FindMy"
+ "QuickSwitch"
+ "quickSwitchFM"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
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
- "FMFAdditions"
- "FMFLocatorAccountNotificationPlugin"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_xpcConnectionCreationQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "TQ,R"
- "Vv16@0:8"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?@\"NSError\">16"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@16@?24"
- "XPCServerProtocol"
- "^{_NSZone=}16@0:8"
- "_currentXPCConnection"
- "_destroyXPCConnection"
- "_xpcConnection"
- "_xpcConnectionCreationQueue"
- "aa_fmfAccount"
- "aa_isPrimaryAccount"
- "aa_personID"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountType"
- "autorelease"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "conformsToProtocol:"
- "copy"
- "credentialForAccount:error:"
- "credentialItemForKey:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionary"
- "didChangeFMFAccountInfo:usingCallback:"
- "fm_safelyMapKey:toObject:"
- "fmfAccountInfoForProactiveChanges"
- "fmfAccountInfoWithTokens:"
- "hash"
- "identifier"
- "init"
- "initWithDescription:andTimeout:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPropertyDirty:"
- "isProvisionedForDataclass:"
- "isProxy"
- "mutableCopy"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "propertiesForDataclass:"
- "refreshMyLocationWithCallback:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "setXpcConnection:"
- "setXpcConnectionCreationQueue:"
- "signal"
- "superclass"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "wait"
- "willDeleteiCloudAccountUsingCallback:"
- "xpcConnection"
- "xpcConnectionCreationQueue"
- "zone"

```
