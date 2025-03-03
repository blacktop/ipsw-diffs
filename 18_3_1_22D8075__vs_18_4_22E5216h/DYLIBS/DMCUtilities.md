## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-5.2.7.0.0
-  __TEXT.__text: 0x2cd08
-  __TEXT.__auth_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x23f8
-  __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x6ec
-  __TEXT.__cstring: 0x313f
-  __TEXT.__oslogstring: 0x4445
+20.4.16.0.0
+  __TEXT.__text: 0x31534
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x2a0c
+  __TEXT.__const: 0x148
+  __TEXT.__gcc_except_tab: 0x734
+  __TEXT.__cstring: 0x335d
+  __TEXT.__oslogstring: 0x4afc
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0xb90
-  __TEXT.__objc_classname: 0x401
-  __TEXT.__objc_methname: 0x8392
-  __TEXT.__objc_methtype: 0x11a5
-  __TEXT.__objc_stubs: 0x5300
-  __DATA_CONST.__got: 0x618
-  __DATA_CONST.__const: 0xe80
-  __DATA_CONST.__objc_classlist: 0x140
+  __TEXT.__unwind_info: 0xd40
+  __TEXT.__objc_classname: 0x450
+  __TEXT.__objc_methname: 0x8f61
+  __TEXT.__objc_methtype: 0x12c5
+  __TEXT.__objc_stubs: 0x59e0
+  __DATA_CONST.__got: 0x658
+  __DATA_CONST.__const: 0x1088
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ee0
-  __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x750
-  __AUTH_CONST.__const: 0xc40
-  __AUTH_CONST.__cfstring: 0x38c0
-  __AUTH_CONST.__objc_const: 0x3cd8
-  __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH.__objc_data: 0xc30
-  __DATA.__objc_ivar: 0x1b0
+  __DATA_CONST.__objc_selrefs: 0x2270
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __AUTH_CONST.__auth_got: 0x740
+  __AUTH_CONST.__const: 0xcc0
+  __AUTH_CONST.__cfstring: 0x3b80
+  __AUTH_CONST.__objc_const: 0x3d60
+  __AUTH_CONST.__objc_intobj: 0x180
+  __AUTH.__objc_data: 0xd70
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__data: 0x2b1
-  __DATA.__bss: 0x910
+  __DATA.__bss: 0x950
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
+  - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1109
-  Symbols:   1750
-  CStrings:  2357
+  Functions: 1298
+  Symbols:   1979
+  CStrings:  2533
 
Symbols:
+ _CPCopyBundleIdentifierAndTeamFromAuditToken
+ _DMCHTTP403ResponseErrorCodePlatformSSORequired
+ _DMCSystemFeaturesDirectory
+ _MDMCloudConfigurationPendingMigrationDetailsFilePath
+ _MDMDEPPushServiceDirectory
+ _MDMDEPTokenSyncPropertiesFilePath
+ _MDMMigrationDirectory
+ _MISValidateSignature
+ _NSFileProtectionComplete
+ _NSFileProtectionCompleteUnlessOpen
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSFileProtectionCompleteWhenUserInactive
+ _NSFileProtectionNone
+ _OBJC_CLASS_$_DMCBundleLookupUtilities
+ _OBJC_CLASS_$_DMCCodeIdentity
+ _OBJC_CLASS_$_DMCCodeUtilities
+ _OBJC_CLASS_$_DMCComposedIdentifier
+ _OBJC_CLASS_$_DMCPropertyListStorage
+ _OBJC_CLASS_$_NSFileAccessIntent
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_METACLASS_$_DMCBundleLookupUtilities
+ _OBJC_METACLASS_$_DMCCodeIdentity
+ _OBJC_METACLASS_$_DMCCodeUtilities
+ _OBJC_METACLASS_$_DMCComposedIdentifier
+ _OBJC_METACLASS_$_DMCPropertyListStorage
+ _SecCodeCopySigningInformation
+ _SecStaticCodeCheckValidity
+ _SecStaticCodeCreateWithPath
+ _SecTaskCopySigningIdentifier
+ _SecTaskCopyTeamIdentifier
+ _SecTaskCreateWithAuditToken
+ _kCFBooleanFalse
+ _kDMCErrorDetailsErrorDetailsKey
+ _kMISValidationOptionRespectUppTrustAndAuthorization
+ _kMISValidationOptionUnauthoritativeLaunch
+ _kMISValidationOptionValidateSignatureOnly
+ _kSecCodeInfoIdentifier
+ _kSecCodeInfoTeamIdentifier
- _OBJC_CLASS_$_DMCBackgroundActivityManager
- _OBJC_METACLASS_$_DMCBackgroundActivityManager
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
- _kDMCErrorDetailsBuildVersionKey
- _kDMCErrorDetailsOSVersionKey
- _objc_retain_x27
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_state
- _xpc_activity_should_defer
- _xpc_activity_unregister
- _xpc_dictionary_create
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
CStrings:
+ "\x03"
+ "\x03\x14"
+ "%@ (%@)"
+ "%@ (%@) '%@'"
+ "%@ {%@}"
+ "%s: Failed to execute the block under personal persona. Error: %{public}@"
+ "("
+ "(){}"
+ ")"
+ "+[DMCKeychain _copyTypeRefWithQuery:useSystemKeychain:enforcePersonalPersona:]"
+ "@24@0:8^{?=[8I]}16"
+ "@24@0:8^{__SecTask=}16"
+ "@32@0:8^{__SecCode=}16@24"
+ "@32@0:8^{__SecTask=}16@24"
+ "@40@0:8@16@24Q32"
+ "@48@0:8{?=[8I]}16"
+ "B32@0:8^{__SecCode=}16@24"
+ "B40@0:8@16@?24^@32"
+ "B40@0:8@16Q24^@32"
+ "B56@0:8{?=[8I]}16@48"
+ "Cannot retrieve item with query %{public}@"
+ "Cannot verify code signing identifiers: %{public}@ - %{public}@"
+ "Cannot verify identifiers: %{public}@ - %{public}@"
+ "CloudConfigurationPendingMigrationDetails.plist"
+ "Could not create code identity for path: %{public}@"
+ "Could not create code identity using audit token"
+ "Could not create signing info for path: %{public}@"
+ "Could not create static code ref for path: %{public}@"
+ "Could not look up bundle identifier using audit token"
+ "Could not look up code signing identifier using sec task"
+ "Could not look up code signing identifier using signing info"
+ "Could not look up team identifier using audit token"
+ "Could not look up team identifier using signing info"
+ "Couldn't find item with query: %{public}@ system keychain: %d"
+ "DEPPushTokenSyncProperties.plist"
+ "DMCAtomicWriteToPath:writeOptions:error:"
+ "DMCAtomicWriteToURL:writeOptions:error:"
+ "DMCBundleLookupUtilities"
+ "DMCCodeIdentity"
+ "DMCCodeUtilities"
+ "DMCComposedIdentifier"
+ "DMCObliterationShelterConfigChanged"
+ "DMCPropertyListStorage"
+ "DMCPropertyListStorage: Failed to access file at (%{public}@) with error: %{public}@"
+ "DMCPropertyListStorage: Failed to create file directory with error: %{public}@"
+ "DMCWriteToBinaryFile:protectionType:"
+ "DeviceSupportsBatteryInformation"
+ "Empty code signing ID using SecTask"
+ "Empty team ID using SecTask"
+ "ErrorDetails"
+ "Failed to copy signing info error: %@"
+ "Failed to create SecStaticCodeRef from path: %{public}@, error: %@"
+ "Failed to create SecTask from audit token"
+ "Failed to get path from audit token"
+ "Failed to look up bundle ID using SecTask with error: %{public}@"
+ "Failed to look up code signing ID using SecTask with error: %{public}@"
+ "Failed to look up team ID using SecTask with error: %{public}@"
+ "Failed to validate SecStaticCodeRef error: %@"
+ "Failed to validate path via MISValidateSignature error: %@"
+ "Features"
+ "HTTP_ERROR_403_RESPONSE_PLATFORM_SSO_REQUIRED"
+ "Invalid composed identifier %{public}@"
+ "Looked up bundle ID %{public}@ from audit token using entitlement"
+ "Looked up bundle ID %{public}@ using SecTask"
+ "Looked up code signing ID %{public}@ using SecTask"
+ "Looked up team ID %{public}@ from audit token using entitlement"
+ "Looked up team ID %{public}@ using SecTask"
+ "MDMMigration"
+ "MDMMigrationEnabled"
+ "Missing team-id when verifying composed identifier: %{public}@"
+ "Need to validate path using MIS: %{public}@"
+ "Password with persistent ID: %{public}@ has unexpected type: %{public}@"
+ "Q24@0:8@16"
+ "Q28@0:8@16B24"
+ "Response from server does not contain valid details dict."
+ "SetDefaultCallingAndMessagingApps"
+ "SetDefaultCallingAndMessagingAppsEnabled"
+ "T@\"NSOperationQueue\",&,N,V_storageQueue"
+ "T@\"NSString\",&,N,V_filePath"
+ "T@\"NSString\",R,N,V_bundleID"
+ "T@\"NSString\",R,N,V_codeSigningID"
+ "T@\"NSString\",R,N,V_path"
+ "T@\"NSString\",R,N,V_requirement"
+ "T@\"NSString\",R,N,V_teamID"
+ "TB,R,N,GisMDMMigrationEnabled"
+ "TB,R,N,GisSetDefaultCallingAndMessagingAppsEnabled"
+ "TQ,R,N,V_options"
+ "Verified code signing identifier and composed identifier"
+ "Verified code signing identifiers"
+ "^{__SecCode=}24@0:8@16"
+ "_accessor_removeFileAtPath:"
+ "_accessor_updateDictionaryAtReadPath:writePath:updateBlock:"
+ "_accessor_valueForKey:atPath:"
+ "_bundleID"
+ "_checkValidityOfStaticCode:path:"
+ "_codeIdentityForSigningInfo:path:"
+ "_codeIdentityFromSecTask:path:"
+ "_codeSigningID"
+ "_codeSigningIDFromSecTask:"
+ "_copyTypeRefWithQuery:useSystemKeychain:enforcePersonalPersona:"
+ "_ensureDirectoryExistsForFilePath:"
+ "_filePath"
+ "_optionForFileModificationAtPath:isDeletion:"
+ "_options"
+ "_parsePlatformSSORequiredErrorWithMessage:details:outError:"
+ "_pathFromAuditToken:"
+ "_performFileActionAtPath:asynchronously:hasRead:hasWrite:isDeletion:action:"
+ "_postConfigChangedNotification"
+ "_requirement"
+ "_signingInfoForStaticCode:path:"
+ "_staticCodeFromPath:"
+ "_storageQueue"
+ "_teamID"
+ "_teamIDFromSecTask:"
+ "_updateDictionaryAtPath:updateBlock:completionHandler:"
+ "_updateDictionaryAtPath:updateBlock:error:"
+ "_verifyCodeIdentity:composedIdentifier:"
+ "_verifyCodeIdentity:other:"
+ "_writingOptionsFromProtectionType:"
+ "addObserverForName:object:queue:usingBlock:"
+ "anchor apple and identifier \"%@\""
+ "anchor apple generic and identifier \"%@\" and certificate leaf[subject.OU] = \"%@\""
+ "bundleID"
+ "bundleIDFromAuditToken:"
+ "clearAllKeyValueStorage:"
+ "clearAllKeyValueStorageWithError:"
+ "clearKeys:completionHandler:"
+ "clearKeys:error:"
+ "code-signing-id"
+ "codeIdentityForAuditToken:"
+ "codeIdentityForPath:"
+ "codeSigningID"
+ "com.apple.psso.required"
+ "composedIdentifier"
+ "coordinateAccessWithIntents:queue:byAccessor:"
+ "coordinateReadingItemAtURL:options:error:byAccessor:"
+ "coordinateWritingItemAtURL:options:error:byAccessor:"
+ "copyDataWithPersistentID:useSystemKeychain:enforcePersonalPersona:"
+ "copyPasswordWithPersistentID:useSystemKeychain:enforcePersonalPersona:"
+ "decodeObjectOfClass:forKey:"
+ "defaultCenter"
+ "designatedRequirement"
+ "filePath"
+ "hasBatteryInformationCapability"
+ "hasPrefix:"
+ "hasSuffix:"
+ "initWithBundleID:teamID:requirement:"
+ "initWithCodeSigningID:teamID:path:"
+ "initWithDictionary:path:writeOptions:"
+ "initWithFilePath:"
+ "isEqualToCodeIdentity:"
+ "isEqualToComposedIdentifier:"
+ "isMDMMigrationEnabled"
+ "isSetDefaultCallingAndMessagingAppsEnabled"
+ "newComposedIdentifier:"
+ "newComposedIdentifierWithBundleID:"
+ "newComposedIdentifierWithBundleID:requirement:"
+ "newComposedIdentifierWithBundleID:teamID:"
+ "options"
+ "postNotificationName:object:"
+ "rangeOfCharacterFromSet:"
+ "rangeOfString:"
+ "readingIntentWithURL:options:"
+ "removeObjectsForKeys:"
+ "requirement"
+ "retrieveDictionaryWithCompletionHandler:"
+ "retrieveDictionaryWithError:"
+ "retrieveValueForKey:completionHandler:"
+ "retrieveValueForKey:error:"
+ "saveKeyValuePairs:completionHandler:"
+ "saveKeyValuePairs:error:"
+ "saveValue:forKey:completionHandler:"
+ "saveValue:forKey:error:"
+ "setFilePath:"
+ "setStorageQueue:"
+ "storageQueue"
+ "stringByDeletingLastPathComponent"
+ "substringFromIndex:"
+ "team-id"
+ "teamID"
+ "teamIDFromAuditToken:"
+ "v16@?0@\"NSMutableDictionary\"8"
+ "v16@?0@\"NSNotification\"8"
+ "v16@?0@\"NSURL\"8"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"NSError\"24"
+ "v40@0:8@16@?24@?32"
+ "v48@0:8@16B24B28B32B36@?40"
+ "verifyAgainst:"
+ "verifySignatureForAuditToken:codeIdentity:"
+ "verifySignatureForAuditToken:composedIdentifier:"
+ "verifySignatureForPath:codeIdentity:"
+ "verifySignatureForPath:composedIdentifier:"
+ "writingIntentWithURL:options:"
+ "{"
+ "}"
- "+[DMCKeychain copyItemWithPersistentID:useSystemKeychain:enforcePersonalPersona:]"
- "Background activity canceled. name %@"
- "Background activity done. name %@ result %i"
- "Background activity fired but deferred. name %@ result %i"
- "Background activity ready to run. name %@"
- "Background activity registered. name %@ interval %f tolerance %f"
- "Cannot retrieve item with persistent ID %{public}@"
- "Couldn't get item with ID: %{public}@ system keychain: %d"
- "DMCAtomicWriteToPath:error:"
- "DMCAtomicWriteToURL:error:"
- "DMCBackgroundActivityManager"
- "OSVersion"
- "Response from server does not contain OSVersion key."
- "T@\"NSMutableDictionary\",&,N,V_activities"
- "_activities"
- "activities"
- "cancelActivity:"
- "scheduleOneShotActivity:interval:gracePeriod:callback:"
- "setActivities:"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "v48@0:8@16d24d32@?40"

```
