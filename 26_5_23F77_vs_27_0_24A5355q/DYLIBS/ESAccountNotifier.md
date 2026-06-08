## ESAccountNotifier

> `/System/Library/Accounts/Notification/ESAccountNotifier.bundle/ESAccountNotifier`

```diff

-2074.80.2.0.0
-  __TEXT.__text: 0x1574
-  __TEXT.__auth_stubs: 0x220
+2075.0.0.0.0
+  __TEXT.__text: 0x1348
   __TEXT.__objc_methlist: 0x234
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__cstring: 0x64
+  __TEXT.__gcc_except_tab: 0x1c
+  __TEXT.__cstring: 0x66
   __TEXT.__oslogstring: 0x32e
   __TEXT.__unwind_info: 0xb0
-  __TEXT.__objc_classname: 0x3a
-  __TEXT.__objc_methname: 0x77c
-  __TEXT.__objc_methtype: 0x22b
-  __TEXT.__objc_stubs: 0x5a0
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_const: 0x268
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/Message.framework/Message
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59BBFFBA-BA68-341B-BB33-0EBE23FF69AD
+  UUID: 49F0C7E9-EAA8-390D-B48A-216C03F39151
   Functions: 22
-  Symbols:   64
-  CStrings:  129
+  Symbols:   66
+  CStrings:  14
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x23
- _objc_retain_x24
CStrings:
- "#16@0:8"
- ".cxx_destruct"
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
- "B32@0:8@\"ACAccount\"16@\"ACDAccountStore\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24^@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "B44@0:8@16i24@28@36"
- "ESAccountNotifier"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSMutableDictionary\",R,N,V_stopMonitoringAgentsTokens"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accountTypeWithIdentifier:inStore:"
- "_dataclassesWeCareAbout"
- "_hasEasAccountInStore:"
- "_leafAccountTypesToCheckForEquality"
- "_leafExchangeAccountTypes"
- "_modifiedDataclassesForAccount:oldAccount:"
- "_parentAccountTypes"
- "_sanityCheckEnabledDataclassesOnExchangeAccountInfo:"
- "_startMonitoringAgentsIfNeededForAccountWithIdentifier:"
- "_stopMonitoringAgentsForAccountWithIdentifier:"
- "_stopMonitoringAgentsTokens"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountDidChangeFromOldAccountInfo:"
- "accountProperties"
- "accountType"
- "accountTypeWithAccountTypeIdentifier:"
- "accountTypeWithIdentifier:"
- "accountTypeWithIdentifier:handler:"
- "accountsWithAccountType:"
- "accountsWithAccountTypeIdentifier:"
- "addObject:"
- "autorelease"
- "backingAccountInfo"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "description"
- "enabledDataclasses"
- "esAccountSubclassWithBackingAccountInfo:"
- "hash"
- "identifier"
- "init"
- "initWithObjects:"
- "intersectSet:"
- "isEnabledForDataclass:"
- "isEqual:"
- "isEqualToAccount:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastObject"
- "minusSet:"
- "mutableCopy"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "removeLastObject"
- "removeObject:"
- "removeObjectForKey:"
- "requestDaemonStartMonitoringAgentsWithToken:"
- "requestDaemonStopMonitoringAgents"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAccountType:"
- "setEnabled:forDataclass:"
- "setObject:forKeyedSubscript:"
- "sharedConnection"
- "stopMonitoringAgentsTokens"
- "superclass"
- "unionSet:"
- "unsignedIntegerValue"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "zone"

```
