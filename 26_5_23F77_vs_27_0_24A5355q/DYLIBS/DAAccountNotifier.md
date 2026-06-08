## DAAccountNotifier

> `/System/Library/Accounts/Notification/DAAccountNotifier.bundle/DAAccountNotifier`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0x2cb4
-  __TEXT.__auth_stubs: 0x230
+2703.0.0.0.0
+  __TEXT.__text: 0x29bc
   __TEXT.__objc_methlist: 0x31c
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x88d
+  __TEXT.__cstring: 0x891
   __TEXT.__oslogstring: 0x79e
-  __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x93
-  __TEXT.__objc_methname: 0xc49
-  __TEXT.__objc_methtype: 0x2e1
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0x160
+  __TEXT.__unwind_info: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x390
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x160
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xac0
   __AUTH_CONST.__objc_const: 0x430
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/Message.framework/Message
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DFF4B03B-F8C3-3024-BFCE-490BBF556A20
+  UUID: BC0BC4D9-2A7F-3094-9EA9-C5DF359149CC
   Functions: 39
-  Symbols:   88
-  CStrings:  366
+  Symbols:   89
+  CStrings:  199
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
Functions:
~ sub_2a6f3ff10 -> sub_23bf07f10 : 708 -> 620
~ sub_2a6f401d4 -> sub_23bf0817c : 484 -> 464
~ sub_2a6f403b8 -> sub_23bf0834c : 84 -> 68
~ sub_2a6f404b4 -> sub_23bf08438 : 324 -> 304
~ sub_2a6f405f8 -> sub_23bf08568 : 544 -> 472
~ sub_2a6f40818 -> sub_23bf08740 : 260 -> 212
~ sub_2a6f4091c -> sub_23bf08814 : 548 -> 488
~ sub_2a6f40b64 -> sub_23bf08a20 : 1428 -> 1304
~ sub_2a6f410fc -> sub_23bf08f3c : 352 -> 308
~ sub_2a6f4125c -> sub_23bf09070 : 1168 -> 1064
~ sub_2a6f4171c -> sub_23bf094c8 : 128 -> 120
~ sub_2a6f4179c -> sub_23bf09540 : 2064 -> 1980
~ sub_2a6f41fac -> sub_23bf09cfc : 84 -> 68
~ sub_2a6f42000 -> sub_23bf09d40 : 200 -> 192
~ sub_2a6f420c8 -> sub_23bf09e00 : 84 -> 68
~ sub_2a6f4211c -> sub_23bf09e44 : 1524 -> 1484
~ sub_2a6f42764 -> sub_23bf0a464 : 144 -> 152
~ sub_2a6f427f4 -> sub_23bf0a4fc : 124 -> 128
~ sub_2a6f4295c -> sub_23bf0a668 : 124 -> 128
~ sub_2a6f42a44 -> sub_23bf0a754 : 108 -> 104
~ sub_2a6f42ab0 -> sub_23bf0a7bc : 108 -> 104
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"ACAccount\""
- "@\"ACDAccountStore\""
- "@\"NSCountedSet\""
- "@\"NSMutableDictionary\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8^Q16i24"
- "B32@0:8@\"ACAccount\"16@\"ACDAccountStore\"24"
- "B32@0:8@16@24"
- "B36@0:8i16@20@28"
- "B40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24^@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "B44@0:8@16i24@28@36"
- "CalDAVSubscribedCalendarsKey"
- "DAAccountChangeHandlerAccountStoreUpdater"
- "DAAccountChangeUpdaterACDAccountStoreWrapper"
- "DAAccountDoNotSaveReason"
- "DAAccountIdentifiersToIgnoreForUniquenessCheck"
- "DAAccountNotifier"
- "DAAccountPrincipalPath"
- "DAAccountSavePreflighted"
- "NSObject"
- "Q16@0:8"
- "SubCalFilterAlarmsKey"
- "SubCalInsecureConnectionApproved"
- "SubCalSubscriptionURLKey"
- "SubCalTitleKey"
- "T#,R"
- "T@\"NSCountedSet\",R,N,V_inFlightChangesPerAccount"
- "T@\"NSMutableDictionary\",R,N,V_stopMonitoringAgentsTokens"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,R,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_account"
- "_accountPropertiesThatTriggerRefresh"
- "_daAccountChangeType:forACAccountChangeType:"
- "_dataclassesWeCareAbout"
- "_disableLocalStoreIfNeedForAccount:"
- "_handleAccount:didChangeWithType:inStore:oldAccount:"
- "_inFlightChangesPerAccount"
- "_isStore:fromClient:"
- "_isStoreFromCalaccessd:"
- "_isStoreFromCalendarMigrationTool:"
- "_isStoreFromDataAccess:"
- "_isStoreFromRemindd:"
- "_modifiedDataclassesForAccount:oldAccount:"
- "_propertiesThatTriggerRefresh"
- "_shouldRefreshForChangeOfType:forAccount:oldAccount:"
- "_stopMonitoringAgentsForAccountWithIdentifier:"
- "_stopMonitoringAgentsTokens"
- "_stopMonitoringAgentsTokensLock"
- "_store"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountProperties"
- "accountPropertyForKey:"
- "accountTypeWithIdentifier:"
- "accountsWithAccountTypeIdentifier:"
- "addAccount:withCompletionHandler:"
- "addAccountNoSave:error:"
- "addInFlightChangeForAccountIdentifier:"
- "addObject:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "autorelease"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "canSaveWithAccountProvider:"
- "class"
- "client"
- "conformsToProtocol:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "currentHandler"
- "daAccountSubclassWithBackingAccountInfo:"
- "debugDescription"
- "deleteAccountNoSave:error:"
- "description"
- "handleAccountDidChange:withChangeInfo:store:"
- "handleAccountWillChange:withChangeInfo:store:accountUpdater:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "inFlightChangesPerAccount"
- "init"
- "initWithAccount:store:"
- "initWithChangeType:accountIdentifier:accountTypeIdentifier:oldAccountProperties:username:password:oldUsername:oldPassword:modifiedDataClasses:clientName:"
- "intersectSet:"
- "isEnabledForDataclass:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProvisionedForDataclass:"
- "isProxy"
- "leafAccountTypes"
- "leafAccountTypesToCheckForEquality"
- "minusSet:"
- "mutableCopy"
- "name"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "parentAccountTypes"
- "password"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "propertiesForDataclass:"
- "release"
- "removeAccount:completion:"
- "removeInFlightChangeForAccountIdentifier:"
- "removeObject:"
- "removeObjectForKey:"
- "requestDaemonStartMonitoringAgentsWithToken:"
- "requestDaemonStopMonitoringAgents"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAccountType:"
- "setObject:forKeyedSubscript:"
- "setWithArray:"
- "sharedConnection"
- "shouldProcessAccountChanges"
- "stopMonitoringAgentsTokens"
- "superclass"
- "unionSet:"
- "unsignedIntegerValue"
- "updateAccount:withCompletionHandler:"
- "updateAccountNoSave:error:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@\"ACAccount\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "valueForKey:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
