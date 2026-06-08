## PrivacyDisclosureCore

> `/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore`

```diff

 49.0.0.0.0
-  __TEXT.__text: 0x4158
-  __TEXT.__auth_stubs: 0x460
+  __TEXT.__text: 0x3e24
   __TEXT.__objc_methlist: 0x704
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x437
-  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__cstring: 0x444
+  __TEXT.__gcc_except_tab: 0x74
   __TEXT.__oslogstring: 0x244
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x200
-  __TEXT.__objc_classname: 0x1c6
-  __TEXT.__objc_methname: 0x11d4
-  __TEXT.__objc_methtype: 0x4f1
-  __TEXT.__objc_stubs: 0xc20
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0xe8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x1e10
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x420

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9FC156D0-67B4-38B2-B20A-82DBE47BAA2A
-  Functions: 135
+  UUID: D51DEE47-1C51-39AD-A739-7147CC07424E
+  Functions: 133
   Symbols:   686
-  CStrings:  339
+  CStrings:  68
 
Symbols:
+ ___block_literal_global.41
+ ___block_literal_global.46
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- ___block_literal_global.42
- ___block_literal_global.47
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PDCApplicationEnvironment>\""
- "@\"<PDCApplicationEnvironmentMonitoring>\""
- "@\"<PDCApplicationEnvironmentMonitoringHandle>\""
- "@\"<PDCApplicationEnvironmentMonitoringHandle>\"32@0:8@\"<PDCApplicationEnvironmentMonitoring>\"16@\"NSObject<OS_dispatch_queue>\"24"
- "@\"<PDCApplicationIdentity>\"24@0:8@\"NSString\"16"
- "@\"<PDCApplicationRecord>\"24@0:8@\"NSString\"16"
- "@\"<PDCApplicationRecord>\"24@0:8^@16"
- "@\"<PDCConsentStore>\""
- "@\"LSApplicationWorkspace\""
- "@\"NSArray\"16@0:8"
- "@\"NSEnumerator\"16@0:8"
- "@\"NSError\"32@0:8@\"NSString\"16@\"NSString\"24"
- "@\"NSMapTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSURL\""
- "@\"NSURL\"16@0:8"
- "@\"SBSRemoteAlertHandle\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "LSApplicationWorkspaceObserverProtocol"
- "NSObject"
- "PDCApplicationEnvironment"
- "PDCApplicationEnvironmentMonitoring"
- "PDCApplicationEnvironmentMonitoringHandle"
- "PDCApplicationEventListener"
- "PDCApplicationIdentity"
- "PDCApplicationRecord"
- "PDCConsentStore"
- "PDCFileBackedConsentStore"
- "PDCLSBackedApplicationEnvironment"
- "PDCPreflightManager"
- "PDCPreflightRequestCanceling"
- "PDCPreflightRequestHandle"
- "PDCPrivacyAlertPresenter"
- "PDCSettings"
- "Q16@0:8"
- "SBSRemoteAlertHandleObserver"
- "T#,R"
- "T@\"<PDCApplicationEnvironmentMonitoring>\",W,V_delegate"
- "T@\"<PDCConsentStore>\",&,N,V_consentStore"
- "T@\"NSArray\",R,N"
- "T@\"NSEnumerator\",R,C,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSSet\",R,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N"
- "T@\"NSURL\",R,C,N,V_storeURL"
- "T@\"NSURL\",R,N"
- "T@?,C,N,V_changeObserver"
- "TB,R,N,GisPreflightFeatureEnabled"
- "TB,V_cancelled"
- "TQ,R"
- "URL"
- "URLByAppendingPathComponent:"
- "URLByDeletingLastPathComponent"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activateAlertHandleForIdentity:settings:repsonseHandler:"
- "_activated"
- "_alertHandle"
- "_applicationEnvironment"
- "_cancelled"
- "_changeObserver"
- "_completionHandler"
- "_consentStore"
- "_delegate"
- "_ensureAppIsLaunchableWithIdentity:completion:"
- "_environmentMonitoringHandle"
- "_isComplete"
- "_preflightLaunchForApplication:withCompletionHandler:"
- "_queue"
- "_requestToAlertMap"
- "_requiresPreflightForApplication:"
- "_requiresPreflightForApplicationRecord:"
- "_storeURL"
- "_workspace"
- "activate"
- "activateRemoteAlertWithIdentity:requestHandle:forcePresent:completionHandler:"
- "activateWithContext:"
- "addObject:"
- "addObserver:"
- "allApplications"
- "alreadyCompletedRequestHandle"
- "applicationDidUninstall:"
- "applicationIconDidChange:"
- "applicationIdentityForIdentityString:"
- "applicationInstallsArePrioritized:arePaused:"
- "applicationInstallsDidCancel:"
- "applicationInstallsDidChange:"
- "applicationInstallsDidPause:"
- "applicationInstallsDidPrioritize:"
- "applicationInstallsDidResume:"
- "applicationInstallsDidStart:"
- "applicationInstallsDidUpdateIcon:"
- "applicationMissingRequiredSINF"
- "applicationRecordForBundleIdentifier:"
- "applicationStateDidChange:"
- "applicationsDidChangePersonas:"
- "applicationsDidFailToInstall:"
- "applicationsDidFailToUninstall:"
- "applicationsDidInstall:"
- "applicationsDidUninstall:"
- "applicationsDidUpdateMetadata:"
- "applicationsWillInstall:"
- "applicationsWillUninstall:"
- "array"
- "autorelease"
- "backupFileAtPath:"
- "bundleIdentifier"
- "bundleWithURL:"
- "cancel"
- "cancelled"
- "changeObserver"
- "checkForStaleConsentRecords"
- "class"
- "completeRequestWithResponse:"
- "conformsToProtocol:"
- "consentRecordURLForBundleIdentifier:"
- "consentStore"
- "consentedBundleIdentifiers"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "databaseWasRebuilt"
- "debugDescription"
- "defaultManager"
- "defaultService"
- "defaultWorkspace"
- "delegate"
- "description"
- "deviceManagementPolicyDidChange:"
- "didCancelRequestHandle:"
- "enumeratorWithOptions:"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "findApplicationRecordWithError:"
- "hash"
- "helperPlaceholdersInstalled:"
- "helperPlaceholdersUninstalled:"
- "identities"
- "identityString"
- "info"
- "infoDictionary"
- "init"
- "initWithBundleID:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithConsentStore:applicationEnvironment:targetQueue:"
- "initWithConsentStoreURL:"
- "initWithDomain:code:userInfo:"
- "initWithIdentityString:"
- "initWithInfo:responder:"
- "initWithQueue:completionHandler:"
- "initWithServiceName:viewControllerClassName:"
- "initWithSuiteName:"
- "initWithTargetPredicate:"
- "initWithTargetQueue:"
- "initWithTargetQueue:consentStore:"
- "initWithWorkspace:delegate:queue:"
- "instancesRespondToSelector:"
- "integerForKey:"
- "integerValue"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPreflightFeatureEnabled"
- "isProxy"
- "localizedName"
- "monitorAppEventsWithDelegate:onQueue:"
- "networkUsageChanged:"
- "newHandleWithDefinition:configurationContext:"
- "numberWithBool:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectForSetting:"
- "observeLaunchProhibitedApps"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginsDidInstall:"
- "pluginsDidUninstall:"
- "pluginsWillUninstall:"
- "predicateForLaunchingApplicationIdentity:"
- "preflightFeatureEnabled"
- "preflightLaunchForApplication:withCompletionHandler:"
- "q24@0:8@\"NSString\"16"
- "q24@0:8@16"
- "queue"
- "registerObserver:"
- "regulatoryPrivacyDisclosureVersion"
- "release"
- "remoteAlertHandle:didInvalidateWithError:"
- "remoteAlertHandleDidActivate:"
- "remoteAlertHandleDidDeactivate:"
- "removeObjectForKey:"
- "removeObserver:"
- "repairAppWithOptions:replyHandler:"
- "requiresPreflightForApplication:"
- "requiresPreflightForApplicationRecord:"
- "responderWithHandler:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setActions:"
- "setCancelled:"
- "setChangeObserver:"
- "setConsentStore:"
- "setDelegate:"
- "setExitReason:"
- "setInteger:forKey:"
- "setObject:forKey:"
- "setObject:forSetting:"
- "setPresentationTarget:"
- "setQueue:"
- "setShouldDismissInSwitcher:"
- "setWithArray:"
- "setWithObject:"
- "sharedInstance"
- "sharedPresenter"
- "storeURL"
- "stringWithContentsOfURL:encoding:error:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "userConsentedRegulatoryDisclosureVersionForBundleIdentifier:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"SBSRemoteAlertHandle\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"SBSRemoteAlertHandle\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8q16@\"NSString\"24"
- "v32@0:8q16@24"
- "v40@0:8@16@24@?32"
- "v44@0:8@16@24B32@?36"
- "weakToWeakObjectsMapTable"
- "writeToURL:atomically:encoding:error:"
- "writeUserConsentedRegulatoryDisclosureVersion:forBundleIdentifier:"
- "zone"
- "{atomic_flag=\"_Value\"AB}"

```
