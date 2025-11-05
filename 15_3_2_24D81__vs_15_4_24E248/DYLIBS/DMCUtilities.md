## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/Versions/A/DMCUtilities`

```diff

-5.2.7.0.0
-  __TEXT.__text: 0x27d14
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x20e8
-  __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x440
-  __TEXT.__cstring: 0x2463
-  __TEXT.__oslogstring: 0x3889
+20.4.18.0.0
+  __TEXT.__text: 0x2d78c
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_methlist: 0x26fc
+  __TEXT.__const: 0x128
+  __TEXT.__gcc_except_tab: 0x594
+  __TEXT.__cstring: 0x28ff
+  __TEXT.__oslogstring: 0x3fb8
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x9e0
-  __TEXT.__objc_classname: 0x401
-  __TEXT.__objc_methname: 0x76ba
-  __TEXT.__objc_methtype: 0xfd9
-  __TEXT.__objc_stubs: 0x4560
-  __DATA_CONST.__got: 0x5b0
+  __TEXT.__unwind_info: 0xb88
+  __TEXT.__objc_classname: 0x450
+  __TEXT.__objc_methname: 0x82d7
+  __TEXT.__objc_methtype: 0x10f9
+  __TEXT.__objc_stubs: 0x4c80
+  __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__const: 0x618
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b80
-  __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x500
-  __AUTH_CONST.__const: 0x11c0
-  __AUTH_CONST.__cfstring: 0x2f40
-  __AUTH_CONST.__objc_const: 0x3c48
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xc80
-  __DATA.__objc_ivar: 0x1a4
+  __DATA_CONST.__objc_selrefs: 0x1f18
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__const: 0x1540
+  __AUTH_CONST.__cfstring: 0x3220
+  __AUTH_CONST.__objc_const: 0x3cd0
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0xdc0
+  __DATA.__objc_ivar: 0x1c4
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x5f0
+  __DATA.__bss: 0x630
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F5248D8-EA57-3371-9234-0A093F313B9B
-  Functions: 994
-  Symbols:   2796
-  CStrings:  2439
+  UUID: 9710130E-D62E-3B83-8C21-CF29B430A49C
+  Functions: 1182
+  Symbols:   3149
+  CStrings:  2648
 
Symbols:
+ +[DMCBundleLookupUtilities bundleIDFromAuditToken:]
+ +[DMCBundleLookupUtilities teamIDFromAuditToken:]
+ +[DMCCodeIdentity supportsSecureCoding]
+ +[DMCCodeUtilities _checkValidityOfStaticCode:path:]
+ +[DMCCodeUtilities _codeIdentityForSigningInfo:path:]
+ +[DMCCodeUtilities _codeIdentityFromSecTask:path:]
+ +[DMCCodeUtilities _codeSigningIDFromSecTask:]
+ +[DMCCodeUtilities _pathFromAuditToken:]
+ +[DMCCodeUtilities _signingInfoForStaticCode:path:]
+ +[DMCCodeUtilities _staticCodeFromPath:]
+ +[DMCCodeUtilities _teamIDFromSecTask:]
+ +[DMCCodeUtilities _verifyCodeIdentity:composedIdentifier:]
+ +[DMCCodeUtilities _verifyCodeIdentity:other:]
+ +[DMCCodeUtilities codeIdentityForAuditToken:]
+ +[DMCCodeUtilities codeIdentityForPath:]
+ +[DMCCodeUtilities verifySignatureForAuditToken:codeIdentity:]
+ +[DMCCodeUtilities verifySignatureForAuditToken:composedIdentifier:]
+ +[DMCCodeUtilities verifySignatureForPath:codeIdentity:]
+ +[DMCCodeUtilities verifySignatureForPath:composedIdentifier:]
+ +[DMCComposedIdentifier newComposedIdentifier:]
+ +[DMCComposedIdentifier newComposedIdentifierWithBundleID:]
+ +[DMCComposedIdentifier newComposedIdentifierWithBundleID:requirement:]
+ +[DMCComposedIdentifier newComposedIdentifierWithBundleID:teamID:]
+ +[DMCDateFormatterFactory isoDateFormatter].cold.1
+ +[DMCDateFormatterFactory isoLocalTimeZoneDateFormatter].cold.1
+ +[DMCFeatureFlags hasT2].cold.1
+ +[DMCFeatureFlags isMDMMigrationEnabled]
+ +[DMCFeatureFlags isSetDefaultCallingAndMessagingAppsEnabled]
+ +[DMCHTTPRequestor _parsePlatformSSORequiredErrorWithMessage:details:outError:]
+ +[DMCKeychain _copyTypeRefWithQuery:useSystemKeychain:enforcePersonalPersona:]
+ +[DMCKeychain copyDataWithPersistentID:useSystemKeychain:enforcePersonalPersona:]
+ +[DMCKeychain copyPasswordWithPersistentID:useSystemKeychain:enforcePersonalPersona:]
+ +[DMCMobileGestalt hasBatteryInformationCapability]
+ +[DMCMobileGestalt isAppleSiliconMac].cold.1
+ +[MDMPowerAssertion _currentAssertions].cold.1
+ +[MDMPowerAssertion _dateFormatter].cold.1
+ +[NSDateFormatter(RemoteManagementModel) rmmodel_sharedRFC3339DateFormatter].cold.1
+ -[DMCCodeIdentity .cxx_destruct]
+ -[DMCCodeIdentity codeSigningID]
+ -[DMCCodeIdentity description]
+ -[DMCCodeIdentity encodeWithCoder:]
+ -[DMCCodeIdentity initWithCodeSigningID:teamID:path:]
+ -[DMCCodeIdentity initWithCoder:]
+ -[DMCCodeIdentity isEqual:]
+ -[DMCCodeIdentity isEqualToCodeIdentity:]
+ -[DMCCodeIdentity path]
+ -[DMCCodeIdentity teamID]
+ -[DMCCodeIdentity verifyAgainst:]
+ -[DMCComposedIdentifier .cxx_destruct]
+ -[DMCComposedIdentifier bundleID]
+ -[DMCComposedIdentifier composedIdentifier]
+ -[DMCComposedIdentifier description]
+ -[DMCComposedIdentifier designatedRequirement]
+ -[DMCComposedIdentifier initWithBundleID:teamID:requirement:]
+ -[DMCComposedIdentifier isEqual:]
+ -[DMCComposedIdentifier isEqualToComposedIdentifier:]
+ -[DMCComposedIdentifier requirement]
+ -[DMCComposedIdentifier teamID]
+ -[DMCDictionaryWriter initWithDictionary:path:writeOptions:]
+ -[DMCDictionaryWriter options]
+ -[DMCHangDetectionQueue queueBlock:].cold.1
+ -[DMCObliterationShelter _postConfigChangedNotification]
+ -[DMCObliterationShelter init]
+ -[DMCPropertyListStorage .cxx_destruct]
+ -[DMCPropertyListStorage _accessor_removeFileAtPath:]
+ -[DMCPropertyListStorage _accessor_updateDictionaryAtReadPath:writePath:updateBlock:]
+ -[DMCPropertyListStorage _accessor_valueForKey:atPath:]
+ -[DMCPropertyListStorage _ensureDirectoryExistsForFilePath:]
+ -[DMCPropertyListStorage _optionForFileModificationAtPath:isDeletion:]
+ -[DMCPropertyListStorage _performFileActionAtPath:asynchronously:hasRead:hasWrite:isDeletion:action:]
+ -[DMCPropertyListStorage _updateDictionaryAtPath:updateBlock:completionHandler:]
+ -[DMCPropertyListStorage _updateDictionaryAtPath:updateBlock:error:]
+ -[DMCPropertyListStorage clearAllKeyValueStorage:]
+ -[DMCPropertyListStorage clearAllKeyValueStorageWithError:]
+ -[DMCPropertyListStorage clearKeys:completionHandler:]
+ -[DMCPropertyListStorage clearKeys:error:]
+ -[DMCPropertyListStorage filePath]
+ -[DMCPropertyListStorage initWithFilePath:]
+ -[DMCPropertyListStorage retrieveDictionaryWithCompletionHandler:]
+ -[DMCPropertyListStorage retrieveDictionaryWithError:]
+ -[DMCPropertyListStorage retrieveValueForKey:completionHandler:]
+ -[DMCPropertyListStorage retrieveValueForKey:error:]
+ -[DMCPropertyListStorage saveKeyValuePairs:completionHandler:]
+ -[DMCPropertyListStorage saveKeyValuePairs:error:]
+ -[DMCPropertyListStorage saveValue:forKey:completionHandler:]
+ -[DMCPropertyListStorage saveValue:forKey:error:]
+ -[DMCPropertyListStorage setFilePath:]
+ -[DMCPropertyListStorage setStorageQueue:]
+ -[DMCPropertyListStorage storageQueue]
+ -[NSData(DMCUtilities) DMCAtomicWriteToPath:writeOptions:error:]
+ -[NSData(DMCUtilities) DMCAtomicWriteToURL:writeOptions:error:]
+ -[NSDictionary(DMCUtilities) DMCWriteToBinaryFile:protectionType:]
+ -[NSDictionary(DMCUtilities) _writingOptionsFromProtectionType:]
+ AppleIDSSOAuthenticationBundle.cold.1
+ AuthKitBundle.cold.1
+ DMCAKAppleIDSession.cold.1
+ DMCConfigurationProfilesSystemGroupContainerMetadataFilePath.cold.1
+ DMCDeviceIsNetworkTethered.cold.1
+ DMCDiskManagementDirectory.cold.1
+ DMCDiskRestrictionFilePath.cold.1
+ DMCEventsFilePath.cold.1
+ DMCHangTracerDirectory.cold.1
+ DMCHasMDMMigrated.cold.1
+ DMCLogObjects.cold.1
+ DMCLoggingDirectory.cold.1
+ DMCManagedEventsDaemonKeepAliveFilePath.cold.1
+ DMCMultiUserDeviceConfigurationFilePath.cold.1
+ DMCMultiUserUserConfigurationFilePath.cold.1
+ DMCSystemFeaturesDirectory.cold.1
+ DMCSystemFeaturesDirectory.once
+ DMCSystemFeaturesDirectory.str
+ DMCSystemLostModeRequestPath.cold.1
+ DMCSystemRootDirectory.cold.1
+ DMCUSEnglishLocale.cold.1
+ DMCUSEnglishNumberFormatter.cold.1
+ GCC_except_table10
+ GCC_except_table17
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table37
+ GCC_except_table51
+ MCConfigurationProfilesSystemGroupContainer.cold.1
+ MCLegacyMetadataFilePath.cold.1
+ MCSystemMetadataFilePath.cold.1
+ MCUserMetadataFilePath.cold.1
+ MDMAppManagementFilePath.cold.1
+ MDMAuthenticationResultsCacheFilePath.cold.1
+ MDMCloudConfigurationDetailsFilePath.cold.1
+ MDMCloudConfigurationPendingMigrationDetailsFilePath.cold.1
+ MDMCloudConfigurationPendingMigrationDetailsFilePath.once
+ MDMCloudConfigurationPendingMigrationDetailsFilePath.str
+ MDMCloudConfigurationSetAsideDetailsFilePath.cold.1
+ MDMDEPPushServiceDirectory.cold.1
+ MDMDEPPushServiceDirectory.once
+ MDMDEPPushServiceDirectory.str
+ MDMDEPTokenSyncActivitiesFilePath.cold.1
+ MDMDEPTokenSyncPropertiesFilePath.cold.1
+ MDMDEPTokenSyncPropertiesFilePath.once
+ MDMDEPTokenSyncPropertiesFilePath.str
+ MDMDirtyEnrollmentStateFilePath.cold.1
+ MDMDirtyPersonaFilePath.cold.1
+ MDMEventsFilePath.cold.1
+ MDMFilePath.cold.1
+ MDMLegacyManagedNonStoreBooksDirectory.cold.1
+ MDMManagedNonStoreBooksDirectory.cold.1
+ MDMManagedNonStoreBooksManifestPath.cold.1
+ MDMManagedStoreBooksManifestPath.cold.1
+ MDMMigrationDirectory.cold.1
+ MDMMigrationDirectory.once
+ MDMMigrationDirectory.str
+ MDMOutstandingActivitiesFilePath.cold.1
+ MDMPostSetupAutoInstallProfilePath.cold.1
+ MDMPostSetupAutoInstallSetAsideProfilePath.cold.1
+ MDMPropertiesFilePath.cold.1
+ MDMPropertiesUserFilePath.cold.1
+ MDMSetupAssistantSettingsFilePath.cold.1
+ MDMSystemRestartLogPath.cold.1
+ MDMSystemReturnToServiceStorageDirectory.cold.1
+ MDMSystemShutDownLogPath.cold.1
+ MDMUserFilePath.cold.1
+ MDMUserOutstandingActivitiesFilePath.cold.1
+ MDMUserReturnToServiceStorageDirectory.cold.1
+ MDMUserSetupAssistantSettingsFilePath.cold.1
+ MTiPCUKeychainMapPath.cold.1
+ OBJC_IVAR_$_DMCCodeIdentity._codeSigningID
+ OBJC_IVAR_$_DMCCodeIdentity._path
+ OBJC_IVAR_$_DMCCodeIdentity._teamID
+ OBJC_IVAR_$_DMCComposedIdentifier._bundleID
+ OBJC_IVAR_$_DMCComposedIdentifier._requirement
+ OBJC_IVAR_$_DMCComposedIdentifier._teamID
+ OBJC_IVAR_$_DMCDictionaryWriter._options
+ OBJC_IVAR_$_DMCPropertyListStorage._filePath
+ OBJC_IVAR_$_DMCPropertyListStorage._storageQueue
+ _CFURLCopyFileSystemPath
+ _DMCHTTP403ResponseErrorCodePlatformSSORequired
+ _DMCSystemFeaturesDirectory
+ _MDMCloudConfigurationPendingMigrationDetailsFilePath
+ _MDMDEPPushServiceDirectory
+ _MDMDEPTokenSyncPropertiesFilePath
+ _MDMMigrationDirectory
+ _NSFileProtectionComplete
+ _NSFileProtectionCompleteUnlessOpen
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSFileProtectionNone
+ _OBJC_CLASS_$_DMCBundleLookupUtilities
+ _OBJC_CLASS_$_DMCCodeIdentity
+ _OBJC_CLASS_$_DMCCodeUtilities
+ _OBJC_CLASS_$_DMCComposedIdentifier
+ _OBJC_CLASS_$_DMCPropertyListStorage
+ _OBJC_CLASS_$_NSFileAccessIntent
+ _OBJC_CLASS_$_NSFileCoordinator
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_METACLASS_$_DMCBundleLookupUtilities
+ _OBJC_METACLASS_$_DMCCodeIdentity
+ _OBJC_METACLASS_$_DMCCodeUtilities
+ _OBJC_METACLASS_$_DMCComposedIdentifier
+ _OBJC_METACLASS_$_DMCPropertyListStorage
+ _SecCodeCopyGuestWithAttributes
+ _SecCodeCopyPath
+ _SecCodeCopySigningInformation
+ _SecRequirementCreateWithStringAndErrors
+ _SecStaticCodeCheckValidity
+ _SecStaticCodeCreateWithPath
+ _SecTaskCopySigningIdentifier
+ _SecTaskCopyTeamIdentifier
+ _SecTaskCreateWithAuditToken
+ _SecTaskValidateForRequirement
+ __101-[DMCPropertyListStorage _performFileActionAtPath:asynchronously:hasRead:hasWrite:isDeletion:action:]_block_invoke.13
+ __101-[DMCPropertyListStorage _performFileActionAtPath:asynchronously:hasRead:hasWrite:isDeletion:action:]_block_invoke.17
+ __101-[DMCPropertyListStorage _performFileActionAtPath:asynchronously:hasRead:hasWrite:isDeletion:action:]_block_invoke.21
+ __DMCHangTracerDirectory_block_invoke.cold.1
+ __DMCLoggingDirectory_block_invoke.cold.1
+ __DMCMultiUserDeviceConfigurationFilePath_block_invoke.cold.1
+ __DMCMultiUserUserConfigurationFilePath_block_invoke.cold.1
+ __DMCSystemFeaturesDirectory_block_invoke.cold.1
+ __DMCSystemLostModeRequestPath_block_invoke.cold.1
+ __MCLegacyMetadataFilePath_block_invoke.cold.1
+ __MCSystemMetadataFilePath_block_invoke.cold.1
+ __MCSystemProfileStorageDirectory_block_invoke.cold.1
+ __MCSystemPublicInfoDirectory_block_invoke.cold.1
+ __MCUserMetadataFilePath_block_invoke.cold.1
+ __MCUserPublicInfoDirectory_block_invoke.cold.1
+ __MDMAppManagementFilePath_block_invoke.cold.1
+ __MDMAuthenticationResultsCacheFilePath_block_invoke.cold.1
+ __MDMCloudConfigurationDetailsFilePath_block_invoke.cold.1
+ __MDMCloudConfigurationSetAsideDetailsFilePath_block_invoke.cold.1
+ __MDMDirtyEnrollmentStateFilePath_block_invoke.cold.1
+ __MDMDirtyPersonaFilePath_block_invoke.cold.1
+ __MDMEventsFilePath_block_invoke.cold.1
+ __MDMFilePath_block_invoke.cold.1
+ __MDMManagedStoreBooksManifestPath_block_invoke.cold.1
+ __MDMOutstandingActivitiesFilePath_block_invoke.cold.1
+ __MDMPostSetupAutoInstallProfilePath_block_invoke.cold.1
+ __MDMPostSetupAutoInstallSetAsideProfilePath_block_invoke.cold.1
+ __MDMPropertiesFilePath_block_invoke.cold.1
+ __MDMPropertiesUserFilePath_block_invoke.cold.1
+ __MDMSystemRestartLogPath_block_invoke.cold.1
+ __MDMSystemReturnToServiceStorageDirectory_block_invoke.cold.1
+ __MDMSystemShutDownLogPath_block_invoke.cold.1
+ __MDMUserFilePath_block_invoke.cold.1
+ __MDMUserOutstandingActivitiesFilePath_block_invoke.cold.1
+ __MTiPCUKeychainMapPath_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_DMCBundleLookupUtilities
+ __OBJC_$_CLASS_METHODS_DMCCodeIdentity
+ __OBJC_$_CLASS_METHODS_DMCCodeUtilities
+ __OBJC_$_CLASS_METHODS_DMCComposedIdentifier
+ __OBJC_$_CLASS_PROP_LIST_DMCCodeIdentity
+ __OBJC_$_INSTANCE_METHODS_DMCCodeIdentity
+ __OBJC_$_INSTANCE_METHODS_DMCComposedIdentifier
+ __OBJC_$_INSTANCE_METHODS_DMCPropertyListStorage
+ __OBJC_$_INSTANCE_VARIABLES_DMCCodeIdentity
+ __OBJC_$_INSTANCE_VARIABLES_DMCComposedIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_DMCPropertyListStorage
+ __OBJC_$_PROP_LIST_DMCCodeIdentity
+ __OBJC_$_PROP_LIST_DMCComposedIdentifier
+ __OBJC_$_PROP_LIST_DMCPropertyListStorage
+ __OBJC_CLASS_PROTOCOLS_$_DMCCodeIdentity
+ __OBJC_CLASS_RO_$_DMCBundleLookupUtilities
+ __OBJC_CLASS_RO_$_DMCCodeIdentity
+ __OBJC_CLASS_RO_$_DMCCodeUtilities
+ __OBJC_CLASS_RO_$_DMCComposedIdentifier
+ __OBJC_CLASS_RO_$_DMCPropertyListStorage
+ __OBJC_METACLASS_RO_$_DMCBundleLookupUtilities
+ __OBJC_METACLASS_RO_$_DMCCodeIdentity
+ __OBJC_METACLASS_RO_$_DMCCodeUtilities
+ __OBJC_METACLASS_RO_$_DMCComposedIdentifier
+ __OBJC_METACLASS_RO_$_DMCPropertyListStorage
+ ___101-[DMCPropertyListStorage _performFileActionAtPath:asynchronously:hasRead:hasWrite:isDeletion:action:]_block_invoke
+ ___109+[DMCKeychain removeItemForService:account:label:description:useSystemKeychain:enforcePersonalPersona:group:]_block_invoke
+ ___113+[DMCKeychain dataFromService:account:label:description:group:useSystemKeychain:enforcePersonalPersona:outError:]_block_invoke
+ ___30-[DMCObliterationShelter init]_block_invoke
+ ___42-[DMCPropertyListStorage clearKeys:error:]_block_invoke
+ ___49-[DMCPropertyListStorage saveValue:forKey:error:]_block_invoke
+ ___50-[DMCPropertyListStorage clearAllKeyValueStorage:]_block_invoke
+ ___50-[DMCPropertyListStorage saveKeyValuePairs:error:]_block_invoke
+ ___52-[DMCPropertyListStorage retrieveValueForKey:error:]_block_invoke
+ ___54-[DMCPropertyListStorage clearKeys:completionHandler:]_block_invoke
+ ___54-[DMCPropertyListStorage retrieveDictionaryWithError:]_block_invoke
+ ___59-[DMCPropertyListStorage clearAllKeyValueStorageWithError:]_block_invoke
+ ___61-[DMCPropertyListStorage saveValue:forKey:completionHandler:]_block_invoke
+ ___62-[DMCPropertyListStorage saveKeyValuePairs:completionHandler:]_block_invoke
+ ___64-[DMCPropertyListStorage retrieveValueForKey:completionHandler:]_block_invoke
+ ___66-[DMCPropertyListStorage retrieveDictionaryWithCompletionHandler:]_block_invoke
+ ___68-[DMCPropertyListStorage _updateDictionaryAtPath:updateBlock:error:]_block_invoke
+ ___78+[DMCKeychain _copyTypeRefWithQuery:useSystemKeychain:enforcePersonalPersona:]_block_invoke
+ ___80-[DMCPropertyListStorage _updateDictionaryAtPath:updateBlock:completionHandler:]_block_invoke
+ ___88+[DMCKeychain copyCertificateWithPersistentID:useSystemKeychain:enforcePersonalPersona:]_block_invoke
+ ___DMCSystemFeaturesDirectory_block_invoke
+ ___MDMCloudConfigurationPendingMigrationDetailsFilePath_block_invoke
+ ___MDMDEPPushServiceDirectory_block_invoke
+ ___MDMDEPTokenSyncPropertiesFilePath_block_invoke
+ ___MDMMigrationDirectory_block_invoke
+ ___block_descriptor_40_e8_32bs_e15_v16?0"NSURL"8l
+ ___block_descriptor_40_e8_32bs_e25_v24?0"NSURL"8"NSURL"16l
+ ___block_descriptor_40_e8_32bs_e43_v32?0"NSString"8"NSString"16"NSError"24l
+ ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8l
+ ___block_descriptor_40_e8_32s_e29_v16?0"NSMutableDictionary"8l
+ ___block_descriptor_48_e8_32r40r_e43_v32?0"NSString"8"NSString"16"NSError"24l
+ ___block_descriptor_48_e8_32r_e5_v8?0l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40bs_e43_v32?0"NSString"8"NSString"16"NSError"24l
+ ___block_descriptor_48_e8_32s40r_e43_v32?0"NSString"8"NSString"16"NSError"24l
+ ___block_descriptor_48_e8_32s40s_e29_v16?0"NSMutableDictionary"8l
+ ___block_descriptor_56_e8_32r40r_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs48bs_e43_v32?0"NSString"8"NSString"16"NSError"24l
+ ___block_descriptor_56_e8_32s40bs48r_e43_v32?0"NSString"8"NSString"16"NSError"24l
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48bs_e43_v32?0"NSString"8"NSString"16"NSError"24l
+ ___block_descriptor_64_e8_32s40s48r56r_e43_v32?0"NSString"8"NSString"16"NSError"24l
+ ___copy_helper_block_e8_32r40r
+ ___copy_helper_block_e8_32s40b48b
+ ___copy_helper_block_e8_32s40b48r
+ ___destroy_helper_block_e8_32r40r
+ __block_literal_global.149
+ __block_literal_global.154
+ __block_literal_global.159
+ __block_literal_global.164
+ __block_literal_global.169
+ __block_literal_global.197
+ __block_literal_global.207
+ __block_literal_global.212
+ __block_literal_global.217
+ __block_literal_global.219
+ __block_literal_global.227
+ __block_literal_global.233
+ __block_literal_global.238
+ __block_literal_global.240
+ __block_literal_global.76
+ __block_literal_global.83
+ _assertionQueue.cold.1
+ _bundle.cold.1
+ _kDMCErrorDetailsErrorDetailsKey
+ _kSecCodeInfoIdentifier
+ _kSecCodeInfoTeamIdentifier
+ _kSecGuestAttributeAudit
+ _objc_msgSend$DMCAtomicWriteToPath:writeOptions:error:
+ _objc_msgSend$DMCWriteToBinaryFile:protectionType:
+ _objc_msgSend$_accessor_removeFileAtPath:
+ _objc_msgSend$_accessor_updateDictionaryAtReadPath:writePath:updateBlock:
+ _objc_msgSend$_accessor_valueForKey:atPath:
+ _objc_msgSend$_checkValidityOfStaticCode:path:
+ _objc_msgSend$_codeIdentityForSigningInfo:path:
+ _objc_msgSend$_codeIdentityFromSecTask:path:
+ _objc_msgSend$_codeSigningIDFromSecTask:
+ _objc_msgSend$_copyTypeRefWithQuery:useSystemKeychain:enforcePersonalPersona:
+ _objc_msgSend$_ensureDirectoryExistsForFilePath:
+ _objc_msgSend$_optionForFileModificationAtPath:isDeletion:
+ _objc_msgSend$_parsePlatformSSORequiredErrorWithMessage:details:outError:
+ _objc_msgSend$_pathFromAuditToken:
+ _objc_msgSend$_performFileActionAtPath:asynchronously:hasRead:hasWrite:isDeletion:action:
+ _objc_msgSend$_postConfigChangedNotification
+ _objc_msgSend$_signingInfoForStaticCode:path:
+ _objc_msgSend$_staticCodeFromPath:
+ _objc_msgSend$_teamIDFromSecTask:
+ _objc_msgSend$_updateDictionaryAtPath:updateBlock:completionHandler:
+ _objc_msgSend$_updateDictionaryAtPath:updateBlock:error:
+ _objc_msgSend$_verifyCodeIdentity:composedIdentifier:
+ _objc_msgSend$_verifyCodeIdentity:other:
+ _objc_msgSend$_writingOptionsFromProtectionType:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$bundleID
+ _objc_msgSend$codeIdentityForAuditToken:
+ _objc_msgSend$codeIdentityForPath:
+ _objc_msgSend$codeSigningID
+ _objc_msgSend$composedIdentifier
+ _objc_msgSend$coordinateAccessWithIntents:queue:byAccessor:
+ _objc_msgSend$coordinateReadingItemAtURL:options:error:byAccessor:
+ _objc_msgSend$coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:
+ _objc_msgSend$coordinateWritingItemAtURL:options:error:byAccessor:
+ _objc_msgSend$copyDataWithPersistentID:useSystemKeychain:enforcePersonalPersona:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$designatedRequirement
+ _objc_msgSend$filePath
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initWithBundleID:teamID:requirement:
+ _objc_msgSend$initWithCodeSigningID:teamID:path:
+ _objc_msgSend$initWithDictionary:path:writeOptions:
+ _objc_msgSend$isEqualToCodeIdentity:
+ _objc_msgSend$isEqualToComposedIdentifier:
+ _objc_msgSend$options
+ _objc_msgSend$performBlockUnderPersonalPersona:
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$readingIntentWithURL:options:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$requirement
+ _objc_msgSend$retrieveWithError:
+ _objc_msgSend$storageQueue
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$teamID
+ _objc_msgSend$verifyAgainst:
+ _objc_msgSend$writingIntentWithURL:options:
+ _objc_unsafeClaimAutoreleasedReturnValue
+ syncQueue.cold.1
+ syncQueueAlertQueue.cold.1
+ syncQueueiTunesLoginCompletionBlocks.cold.1
- +[DMCBackgroundActivityManager cancelActivity:]
- +[DMCBackgroundActivityManager scheduleOneShotActivity:interval:gracePeriod:callback:]
- +[DMCBackgroundActivityManager sharedInstance]
- -[DMCBackgroundActivityManager .cxx_destruct]
- -[DMCBackgroundActivityManager activities]
- -[DMCBackgroundActivityManager initPrivate]
- -[DMCBackgroundActivityManager setActivities:]
- -[NSData(DMCUtilities) DMCAtomicWriteToPath:error:]
- -[NSData(DMCUtilities) DMCAtomicWriteToURL:error:]
- OBJC_IVAR_$_DMCBackgroundActivityManager._activities
- _OBJC_CLASS_$_DMCBackgroundActivityManager
- _OBJC_METACLASS_$_DMCBackgroundActivityManager
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
- __OBJC_$_CLASS_METHODS_DMCBackgroundActivityManager
- __OBJC_$_INSTANCE_METHODS_DMCBackgroundActivityManager
- __OBJC_$_INSTANCE_VARIABLES_DMCBackgroundActivityManager
- __OBJC_$_PROP_LIST_DMCBackgroundActivityManager
- __OBJC_CLASS_RO_$_DMCBackgroundActivityManager
- __OBJC_METACLASS_RO_$_DMCBackgroundActivityManager
- ___46+[DMCBackgroundActivityManager sharedInstance]_block_invoke
- ___86+[DMCBackgroundActivityManager scheduleOneShotActivity:interval:gracePeriod:callback:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e33_v16?0"NSObject<OS_xpc_object>"8l
- __block_literal_global.152
- __block_literal_global.157
- __block_literal_global.162
- __block_literal_global.167
- __block_literal_global.172
- __block_literal_global.194
- __block_literal_global.208
- __block_literal_global.213
- __block_literal_global.215
- __block_literal_global.73
- __block_literal_global.80
- _kDMCErrorDetailsBuildVersionKey
- _kDMCErrorDetailsOSVersionKey
- _objc_msgSend$DMCAtomicWriteToPath:error:
- _objc_msgSend$activities
- _objc_msgSend$initWithDictionary:path:
- _objc_msgSend$sharedInstance
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_state
- _xpc_activity_should_defer
- _xpc_activity_unregister
- _xpc_dictionary_create
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
- sharedInstance.instance
CStrings:
+ " "
+ "%@ (%@)"
+ "%@ (%@) '%@'"
+ "%@ {%@}"
+ "%s: Failed to execute the block under personal persona. Error: %@"
+ "%s: Failed to execute the block under personal persona. Error: %{public}@"
+ "("
+ "(){}"
+ ")"
+ "+[DMCKeychain _copyTypeRefWithQuery:useSystemKeychain:enforcePersonalPersona:]"
+ "+[DMCKeychain copyCertificateWithPersistentID:useSystemKeychain:enforcePersonalPersona:]"
+ "+[DMCKeychain dataFromService:account:label:description:group:useSystemKeychain:enforcePersonalPersona:outError:]"
+ "+[DMCKeychain removeItemForService:account:label:description:useSystemKeychain:enforcePersonalPersona:group:]"
+ "+[DMCKeychain saveItem:withLabel:group:useSystemKeychain:enforcePersonalPersona:]"
+ "+[DMCKeychain setData:forService:account:label:description:access:group:useSystemKeychain:sysBound:enforcePersonalPersona:outError:]"
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
+ "Cannot verify audit token for %{public}@, against %{public}@, result %@"
+ "Cannot verify code signing identifiers: %{public}@ - %{public}@"
+ "Cannot verify identifiers: %{public}@ - %{public}@"
+ "CloudConfigurationPendingMigrationDetails.plist"
+ "Could not create code identity for path: %{public}@"
+ "Could not create code identity using audit token"
+ "Could not create requirement for: %{public}@: %{public}@"
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
+ "Failed to get path URL with error: %d"
+ "Failed to get path code ref with error: %d"
+ "Failed to get path from audit token"
+ "Failed to look up bundle ID using SecTask with error: %{public}@"
+ "Failed to look up code signing ID using SecTask with error: %{public}@"
+ "Failed to look up team ID using SecTask with error: %{public}@"
+ "Failed to validate SecStaticCodeRef error: %@"
+ "Features"
+ "HTTP_ERROR_403_RESPONSE_PLATFORM_SSO_REQUIRED"
+ "Invalid composed identifier %{public}@"
+ "Looked up bundle ID %{public}@ using SecTask"
+ "Looked up code signing ID %{public}@ using SecTask"
+ "Looked up team ID %{public}@ using SecTask"
+ "MDMMigration"
+ "MDMMigrationEnabled"
+ "Missing team-id when verifying composed identifier: %{public}@"
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
+ "Verified audit token for %{public}@"
+ "Verified code signing identifier and composed identifier"
+ "Verified code signing identifiers"
+ "Verified composed identifier: %{public}@"
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
+ "coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:"
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
+ "v24@?0@\"NSURL\"8@\"NSURL\"16"
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
