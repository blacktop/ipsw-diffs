## AMSAccountSyncNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountSyncNotificationPlugin.bundle/AMSAccountSyncNotificationPlugin`

```diff

-9.5.8.2.2
-  __TEXT.__text: 0x1f30
-  __TEXT.__auth_stubs: 0x270
+10.0.40.4.1
+  __TEXT.__text: 0x1c34
   __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x19e
+  __TEXT.__cstring: 0x1a0
   __TEXT.__oslogstring: 0x610
-  __TEXT.__unwind_info: 0xc0
-  __TEXT.__objc_classname: 0x54
-  __TEXT.__objc_methname: 0x8d5
-  __TEXT.__objc_methtype: 0x296
-  __TEXT.__objc_stubs: 0x6e0
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x310
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34737FE8-D93E-314D-9662-4A12F94583AF
+  UUID: B0F0E6AC-D714-32A3-A45A-4FF72574EA0A
   Functions: 21
-  Symbols:   83
-  CStrings:  190
+  Symbols:   86
+  CStrings:  55
 
Symbols:
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "AMSAccount"
- "AMSAccountSyncNotificationPlugin"
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
- "B44@0:8@16@24i32@36"
- "B44@0:8@16i24@28@36"
- "B48@0:8@16@24@32^@40"
- "B52@0:8@16@24@32B40^@44"
- "NSObject"
- "OSLogObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSDate\",&,N,Sams_setLastAuthenticated:"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_processingQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,D,N,Sams_setLastAuthenticationCredentialSource:"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_aa_rawPassword"
- "_aa_setRawPassword:"
- "_processingQueue"
- "_sendRemoteDeviceCommand:forAccount:inStore:attachCompanionInfo:error:"
- "_sendRemoteDeviceCommand:forAccount:inStore:error:"
- "_shouldConsiderAccountActive:"
- "_shouldProcessChangeForAccount:oldAccount:changeType:store:"
- "_syncIDMSAccountForiTunesAccount:inStore:"
- "_synciTunesAccountAddition:inStore:allowAccountRepair:"
- "_synciTunesAccountDeletion:inStore:"
- "_synciTunesAccountModification:oldAccount:inStore:allowAccountRepair:"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountPropertyForKey:"
- "addErrorBlock:"
- "addSuccessBlock:"
- "ams_IDMSAccountForAccount:"
- "ams_activeiTunesAccount"
- "ams_bagForProcessInfo:"
- "ams_delta:"
- "ams_hasDomain:code:"
- "ams_isHSA2"
- "ams_isLocalAccount"
- "ams_isSandboxAccount"
- "ams_isiTunesAccount"
- "ams_lastAuthenticated"
- "ams_lastAuthenticationCredentialSource"
- "ams_saveAccount:"
- "ams_setLastAuthenticated:"
- "ams_setNullableObject:forKey:"
- "ams_sharedAccountStore"
- "ams_sharedAccountStoreForMediaType:"
- "autorelease"
- "bagForProfile:profileVersion:processInfo:"
- "boolValue"
- "bundleID"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "client"
- "conformsToProtocol:"
- "copy"
- "count"
- "credentialWithError:"
- "currentDevice"
- "debugDescription"
- "description"
- "deviceIsiPhone"
- "finishWithSuccess:error:"
- "hash"
- "identifier"
- "init"
- "isActive"
- "isAuthenticated"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processingQueue"
- "release"
- "remoteDeviceProxy"
- "respondsToSelector:"
- "resultWithTimeout:error:"
- "retain"
- "retainCount"
- "self"
- "sendCommand:withAccount:options:completion:"
- "serverFriendlyDescription"
- "setAccountProperty:forKey:"
- "setAuthenticated:"
- "setDirty:forProperty:"
- "setFlushTimerEnabled:"
- "setObject:forKeyedSubscript:"
- "setProcessingQueue:"
- "sharedAccountsSyncPluginConfig"
- "sharedConfig"
- "stringWithFormat:"
- "superclass"
- "uniqueDeviceIdentifier"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v36@0:8@16@24B32"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16i24@28@36"
- "zone"

```
