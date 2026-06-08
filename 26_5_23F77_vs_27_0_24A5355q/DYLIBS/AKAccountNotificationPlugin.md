## AKAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AKAccountNotificationPlugin.bundle/AKAccountNotificationPlugin`

```diff

-525.575.8.0.0
-  __TEXT.__text: 0x5494
-  __TEXT.__auth_stubs: 0x160
+550.0.0.0.0
+  __TEXT.__text: 0x4ea8
   __TEXT.__objc_methlist: 0x304
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__cstring: 0x148
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__cstring: 0x14a
   __TEXT.__oslogstring: 0x948
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x7b
-  __TEXT.__objc_methname: 0xca5
-  __TEXT.__objc_methtype: 0x397
-  __TEXT.__objc_stubs: 0xaa0
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__unwind_info: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3b0
-  __AUTH_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x688
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A3D2DCD-3078-30D1-8534-191694512C8D
+  UUID: D1A3501D-253C-3BF7-86A0-BAA4273B16FE
   Functions: 44
   Symbols:   63
-  CStrings:  240
+  CStrings:  74
 
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AKFollowUpProvider>\""
- "@\"AKAppleIDAuthenticationController\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "AKAccountNotificationPlugin"
- "AKAppleIDAuthenticationDelegate"
- "AKFollowUpSynchronizer"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"ACAccount\"16@\"ACDAccountStore\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24^@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "B44@0:8@16i24@28@36"
- "B48@0:8@\"AKAppleIDAuthenticationController\"16@\"NSMutableDictionary\"24@\"NSError\"32@\"AKAppleIDAuthenticationContext\"40"
- "B48@0:8@16@24@32@40"
- "DSIDForAccount:"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<AKFollowUpProvider>\",&,N,V_followupProvider"
- "T@\"AKAppleIDAuthenticationController\",&,N,V_controller"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accountsWithAcountType:error:"
- "_authController"
- "_controller"
- "_followupProvider"
- "_isAccount:ofAccountType:"
- "_isFullAppleAccount:"
- "_isPrimaryAppleAccount:"
- "_isValidAuthKitAccount:"
- "_isValidChangeForAccount:oldAccount:"
- "_notifyPeerDevicesOfSecurityUpgradeIfNecessaryWithStore:account:oldAccount:"
- "_processAppleAccountModification:oldAccount:inStore:changeType:"
- "_processAuthKitAccountChange:oldAccount:inStore:"
- "_processDeletionForAccount:"
- "_removeAllProtoAccountsInStore:"
- "_removePCSAuthCredential"
- "_removePrivateEmailDatabase"
- "_saveOptionsForCompanionDeviceAuth"
- "_synchronizeItemsForAccount:altDSID:inStore:"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountPropertyForKey:"
- "accountType"
- "accountTypeWithIdentifier:"
- "accountWithIdentifier:"
- "actions"
- "ak_errorWithCode:"
- "altDSIDForAccount:"
- "authKitAccountWithAltDSID:error:"
- "authenticationController:shouldContinueWithAuthenticationResults:error:forContext:"
- "authenticationController:shouldContinueWithAuthenticationResults:error:forContext:completion:"
- "autorelease"
- "bundleID"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "client"
- "compare:options:"
- "conformsToProtocol:"
- "continuationTokenForAccount:"
- "controller"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "credentialItemForKey:"
- "credentialWithError:"
- "currentDevice"
- "date"
- "debugDescription"
- "deleteAccountNoSave:error:"
- "deleteAuthorizationDatabaseWithAltDSID:error:"
- "deletePrivateEmailDatabaseWithCompletion:"
- "description"
- "enumerateObjectsUsingBlock:"
- "followupProvider"
- "getUserInformationForAltDSID:completion:"
- "hash"
- "hearbeatTokenForAccount:"
- "iCloudAccountForAltDSID:"
- "identifier"
- "informativeText"
- "isAgeAttestationPhase1Enabled"
- "isEqual:"
- "isEqualToString:"
- "isFulliCloudAccount:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPrimaryiCloudAccount:"
- "isProxy"
- "numberWithDouble:"
- "passwordResetTokenForAccount:"
- "pendingFollowUpItems:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "primaryiCloudAccount"
- "release"
- "remoteDeviceProxy"
- "removeAllFollowUpItems:"
- "removeAllPCSAuthCredentialWithCompletion:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "saveAccount:withCompletionHandler:"
- "saveVerifiedAccount:withCompletionHandler:"
- "securityLevelForAccount:"
- "self"
- "sendCommand:withAccount:options:completion:"
- "serverFriendlyDescription"
- "setAccountProperty:forKey:"
- "setAltDSID:"
- "setAuthenticationType:"
- "setController:"
- "setDelegate:"
- "setFollowupProvider:"
- "setObject:forKeyedSubscript:"
- "sharedAuthKitFollowupProvider"
- "sharedInstance"
- "sharedManager"
- "shouldSynchronizeForAccount:"
- "store"
- "superclass"
- "synchronizeFollowUpItemsForContext:completion:"
- "synchronizeFollowUpItemsForContext:error:"
- "synchronizeFollowUpsForAccount:error:"
- "synchronizeFollowUpsForAccount:inStore:error:"
- "timeIntervalSinceDate:"
- "triggerAutoBugCaptureWithSubType:andBundleID:userInfo:"
- "uniqueDeviceIdentifier"
- "updateSynchronizeTimeForAccount:inStore:"
- "updateSynchronizeTimeNoSaveForAccount:"
- "userInfoFromAccount:"
- "username"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v40@0:8@16@24@32"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16@24@32i40"
- "v44@0:8@16i24@28@36"
- "v56@0:8@\"AKAppleIDAuthenticationController\"16@\"NSMutableDictionary\"24@\"NSError\"32@\"AKAppleIDAuthenticationContext\"40@?<v@?B>48"
- "v56@0:8@16@24@32@40@?48"
- "warmUpVerificationSessionWithCompletion:"
- "zone"

```
