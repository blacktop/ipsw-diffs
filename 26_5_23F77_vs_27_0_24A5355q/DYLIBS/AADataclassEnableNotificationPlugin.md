## AADataclassEnableNotificationPlugin

> `/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/AADataclassEnableNotificationPlugin`

```diff

-1037.575.5.0.0
-  __TEXT.__text: 0x61ac
-  __TEXT.__auth_stubs: 0x330
+1059.1.1.0.0
+  __TEXT.__text: 0x5a78
   __TEXT.__objc_methlist: 0x504
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x67d
-  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__cstring: 0x681
+  __TEXT.__gcc_except_tab: 0x58
   __TEXT.__oslogstring: 0xd84
-  __TEXT.__unwind_info: 0x1f8
-  __TEXT.__objc_classname: 0xcc
-  __TEXT.__objc_methname: 0x10f1
-  __TEXT.__objc_methtype: 0x2da
-  __TEXT.__objc_stubs: 0xdc0
-  __DATA_CONST.__got: 0x240
+  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1f0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x500
+  __DATA_CONST.__objc_selrefs: 0x4f8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x240
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x640
   __AUTH_CONST.__objc_const: 0xa78
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59A59570-2C2B-3286-B548-1906117AD3A7
-  Functions: 150
-  Symbols:   140
-  CStrings:  400
+  UUID: 035094EB-301C-3281-BA06-B532F14BAD23
+  Functions: 148
+  Symbols:   145
+  CStrings:  177
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AAAccountStoreProxyProtocol>\""
- "@\"AAAppState\"24@0:8@\"NSString\"16"
- "@\"ACAccountStore\""
- "@\"NSString\"16@0:8"
- "@\"NSUserDefaults\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8B16B20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "AAAppState"
- "AAAppStateProvider"
- "AACloudPolicyRestrictions"
- "AADataclassEnableNotificationPlugin"
- "AADataclassManager"
- "AADeviceModelHelper"
- "ACDAccountNotificationPlugin"
- "AppStateProviding"
- "AppleAccount"
- "B"
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
- "T@\"<AAAccountStoreProxyProtocol>\",&,N,V_storeProxy"
- "T@\"AADataclassManager\",R"
- "T@\"ACAccountStore\",&,N,V_store"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSUserDefaults\",&,N,V_userDefaults"
- "TB,R,N,V_isInstalled"
- "TB,R,N,V_isRestricted"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_appStatusRestrictsProvisioningForDataclass:"
- "_buildAutoEnableableDataclassesAndActionsForAccount:dataclassesForEnablement:completion:"
- "_enableBYOEWithDataclassActionsAndSaveAccount:store:completion:"
- "_filteredDataclassesForAccountClass:"
- "_hideDataclassWhenAppRemoved:"
- "_isInstalled"
- "_isRestricted"
- "_isRestrictedForDataclass:account:"
- "_managedIcloudPolicyIdentifierForDataclass"
- "_nonVisibleServiceDataclass"
- "_policyRestrictionIdentifierForDataclass:"
- "_processAppleAccount:didChangeWithType:inStore:oldAccount:"
- "_processIMAPMailAccount:didChangeWithType:inStore:oldAccount:"
- "_saveAccount:store:withDataclassActions:doVerify:completion:"
- "_shouldProvisionNotesForAccount:"
- "_shouldProvisionRemindersForAccount:"
- "_shouldShowDataclassWhenAppIsRemoved:"
- "_shouldVerifyAccountSave"
- "_store"
- "_storeProxy"
- "_userDefaults"
- "_userVisibleDataclasses"
- "aa_accountClass"
- "aa_arrayByRemovingObject:"
- "aa_filter:"
- "aa_firstObjectPassingTest:"
- "aa_isAccountClass:"
- "aa_isManagedAppleID"
- "aa_isNotesMigrated"
- "aa_isPrimaryEmailVerified"
- "aa_isRemindersMigrated"
- "aa_isSubsetOfArray:"
- "aa_map:"
- "aa_mapNullable:"
- "aa_needsEmailConfiguration"
- "aa_removeFirstObject"
- "aa_removeLastObject"
- "aa_serverDisabledDataclass:"
- "aa_setByRemovingObject:"
- "aa_setByRemovingObjectsFromSet:"
- "aa_setPrimaryEmailVerified:"
- "aaf_filter:"
- "aaf_setByRemovingObjectsFromSet:"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountType"
- "addObject:"
- "allObjects"
- "allowListedDataclassesForAppleAccountClassBasic"
- "allowListedDataclassesForAppleAccountClassFull"
- "appBundleIdentifierForDataclass:"
- "appStateForBundleID:"
- "applicationState"
- "arrayWithObjects:count:"
- "autorelease"
- "boolRestrictionForFeature:"
- "bundleIdentifier"
- "canAutoEnableDataclass:forAccount:"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "dataclassActionsForAccountSave:error:"
- "dataclassBundleMap"
- "debugDescription"
- "defaultStore"
- "denyListedMacOSDataclasses"
- "description"
- "deviceIsAudioAccessory"
- "dictionaryWithObjects:forKeys:count:"
- "enableDataclassesWithoutLocalDataDataclassActionsForAccount:completion:"
- "enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "filterDataclassesForPossibleAutoEnablementForAccount:"
- "filteredServerProvidedFeatures:forAccount:"
- "firstObject"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "identifier"
- "indexOfObjectPassingTest:"
- "init"
- "initWithAccountStore:"
- "initWithArray:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithCapacity:"
- "initWithInstalled:isRestricted:"
- "initWithSuiteName:"
- "isDataclassActionSafeForAutoEnablement:"
- "isDeviceEqualTo:"
- "isDeviceiPad"
- "isDeviceiPhone"
- "isEnabledForDataclass:"
- "isEqual:"
- "isEqualToString:"
- "isInstalled"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMomentsDataclassEnabled"
- "isPropertyDirty:"
- "isProvisionedForDataclass:"
- "isProxy"
- "isRestricted"
- "isRunningInStoreDemoMode"
- "isSafeForAutoEnablement"
- "isSubsetOfSet:"
- "isSystemAppMCRestrictedOrRemovedForDataclass:forAccount:"
- "isSystemAppRestrictedOrRemovedForDataclass:"
- "lastObject"
- "mainBundle"
- "minusSet:"
- "mutableCopy"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "parentAccount"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "policyRestrictsDataclass:"
- "provisionedDataclasses"
- "release"
- "removeLastObject"
- "removeObject:"
- "removeObjectAtIndex:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "saveAccount:onAccountStore:withCompletionHandler:"
- "saveAccount:onAccountStore:withDataclassActions:doVerify:completion:"
- "self"
- "setByAddingObject:"
- "setByAddingObjectsFromArray:"
- "setEnabled:forDataclass:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setStore:"
- "setStoreProxy:"
- "setUserDefaults:"
- "setWithArray:"
- "setWithSet:"
- "sharedConnection"
- "sharedManager"
- "shouldProvisionDataclass:forAccount:"
- "store"
- "storeProxy"
- "stringWithFormat:"
- "superclass"
- "type"
- "userDefaults"
- "userDefaultsDisabledDataclasses"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "v52@0:8@16@24@32B40@?44"
- "valueForKey:"
- "zone"

```
