## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/Versions/A/MDMClientLibrary`

```diff

-5.2.7.0.0
-  __TEXT.__text: 0x193c8
+20.4.18.0.0
+  __TEXT.__text: 0x19dc0
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x12d4
+  __TEXT.__objc_methlist: 0x177c
   __TEXT.__const: 0xb9
   __TEXT.__gcc_except_tab: 0x3dc
-  __TEXT.__cstring: 0x1ed4
-  __TEXT.__oslogstring: 0x1d6e
+  __TEXT.__cstring: 0x1f8e
+  __TEXT.__oslogstring: 0x1ea2
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x510
-  __TEXT.__objc_classname: 0x301
-  __TEXT.__objc_methname: 0x445c
-  __TEXT.__objc_methtype: 0x85c
-  __TEXT.__objc_stubs: 0x2f20
-  __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0x9a8
+  __TEXT.__unwind_info: 0x538
+  __TEXT.__objc_classname: 0x303
+  __TEXT.__objc_methname: 0x4600
+  __TEXT.__objc_methtype: 0x871
+  __TEXT.__objc_stubs: 0x2fe0
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1018
+  __DATA_CONST.__objc_selrefs: 0x1110
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x278
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0x2ec0
-  __AUTH_CONST.__objc_const: 0x3a70
+  __AUTH_CONST.__const: 0x8c0
+  __AUTH_CONST.__cfstring: 0x2f60
+  __AUTH_CONST.__objc_const: 0x3438
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_ivar: 0x114
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x160
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFA479F3-4847-336B-8AB2-C68F0AFCCAB2
-  Functions: 517
-  Symbols:   1856
-  CStrings:  1709
+  UUID: 46E8822C-D7BA-333C-936F-8AE82A5A6053
+  Functions: 550
+  Symbols:   1910
+  CStrings:  1741
 
Symbols:
+ +[MDMClient sharedClient].cold.1
+ +[MDMCloudConfiguration _provisionalEnrollmentExpirationDateFromCloudConfig:]
+ +[MDMCloudConfiguration isProvisionallyEnrolledWithCloudConfig:]
+ +[MDMCloudConfiguration sharedConfiguration].cold.1
+ +[MDMConfiguration isRapidReturnToService]
+ +[MDMConfiguration sharedConfiguration].cold.1
+ +[MDMDeviceQueryUtilities allowedDeviceQueriesForAccessRights:isDataSeparated:].cold.1
+ +[MDMDeviceQueryUtilities allowedDeviceQueriesOnUserChannelForAccessRights:].cold.1
+ +[MDMDeviceQueryUtilities allowedDeviceQueriesWithUserEnrollment].cold.1
+ +[MDMOptionsUtilities validatedMDMOptionsFromOptionsDictionary:].cold.1
+ +[MDMUserClient sharedClient].cold.1
+ -[MDMClientCore monitorDEPPushTokenIfNeededWithCompletion:]
+ -[MDMClientCore monitorDEPPushTokenWithCompletion:]
+ -[MDMClientCore simulateDEPPushWithCompletion:]
+ -[MDMClientCore syncDEPPushTokenWithDelay:completion:]
+ -[MDMCloudConfiguration initWithCloudConfigDetails:]
+ -[MDMCloudConfiguration isRapidReturnToService]
+ -[MDMCloudConfiguration isSingleton]
+ -[MDMCloudConfiguration mdmServerUID]
+ -[MDMCloudConfiguration setIsSingleton:]
+ -[MDMESSODetails declarations]
+ -[MDMESSODetails initWithiTunesStoreID:appIDs:associatedDomains:associatedDomainsEnableDirectDownloads:configurationProfile:declarations:]
+ -[MDMESSODetails setDeclarations:]
+ -[MDMMAIDAuthenticator _appleIDContext].cold.1
+ -[MDMMAIDAuthenticator authenticateRequest:error:].cold.1
+ -[MDMMAIDAuthenticator authenticateRequest:error:].cold.2
+ -[MDMMAIDAuthenticator authenticateRequest:error:].cold.3
+ -[MDMMAIDAuthenticator authenticateRequest:error:].cold.4
+ GCC_except_table10
+ GCC_except_table31
+ GCC_except_table35
+ GCC_except_table38
+ GCC_except_table64
+ GCC_except_table72
+ GCC_except_table79
+ OBJC_IVAR_$_MDMCloudConfiguration._isSingleton
+ OBJC_IVAR_$_MDMESSODetails._declarations
+ _MDMDEPPushReceivedNotification
+ _MDMPendingMigrationCloudConfigurationDetailsChangedNotification
+ _MDMSendDEPPushReceivedNotification
+ _MDMSendPendingMigrationCloudConfigurationDetailsChangedNotification
+ __26-[MDMClientCore uprootMDM]_block_invoke.23
+ __41-[MDMClientCore isAwaitingUserConfigured]_block_invoke.36
+ __54-[MDMClientCore _queue_createAndStartMDMXPCConnection]_block_invoke.130
+ __65+[MDMDeviceQueryUtilities allowedDeviceQueriesWithUserEnrollment]_block_invoke.cold.1
+ ___47-[MDMClientCore simulateDEPPushWithCompletion:]_block_invoke
+ ___51-[MDMClientCore monitorDEPPushTokenWithCompletion:]_block_invoke
+ ___54-[MDMClientCore syncDEPPushTokenWithDelay:completion:]_block_invoke
+ ___59-[MDMClientCore monitorDEPPushTokenIfNeededWithCompletion:]_block_invoke
+ __block_literal_global.27
+ __block_literal_global.31
+ __block_literal_global.33
+ __block_literal_global.35
+ __sortKeysAndMakeCommaSeparatedString_block_invoke.cold.1
+ _alwaysAllowedQueries.cold.1
+ _appInstallationQueries.cold.1
+ _deviceInformationQueries.cold.1
+ _kCCIsRapidReturnToServiceKey
+ _kCCMDMServerUIDKey
+ _kMDMEnrollmentSSOAppStoreIDKey
+ _kMDMOptionIdleRebootAllowed
+ _networkInformationQueries.cold.1
+ _objc_msgSend$_provisionalEnrollmentExpirationDateFromCloudConfig:
+ _objc_msgSend$init
+ _objc_msgSend$initWithiTunesStoreID:appIDs:associatedDomains:associatedDomainsEnableDirectDownloads:configurationProfile:declarations:
+ _objc_msgSend$isProvisionallyEnrolledWithCloudConfig:
+ _objc_msgSend$monitorDEPPushTokenIfNeededWithCompletion:
+ _objc_msgSend$monitorDEPPushTokenWithCompletion:
+ _objc_msgSend$setIsSingleton:
+ _objc_msgSend$simulateDEPPushWithCompletion:
+ _objc_msgSend$syncDEPPushTokenWithDelay:completion:
- -[MDMClientCore syncDEPPushTokenWithCompletion:]
- -[MDMESSODetails initWithiTunesStoreID:appIDs:associatedDomains:associatedDomainsEnableDirectDownloads:configurationProfile:]
- GCC_except_table19
- GCC_except_table30
- GCC_except_table34
- GCC_except_table42
- GCC_except_table58
- GCC_except_table66
- GCC_except_table73
- GCC_except_table9
- __26-[MDMClientCore uprootMDM]_block_invoke.27
- __41-[MDMClientCore isAwaitingUserConfigured]_block_invoke.30
- __54-[MDMClientCore _queue_createAndStartMDMXPCConnection]_block_invoke.120
- ___48-[MDMClientCore syncDEPPushTokenWithCompletion:]_block_invoke
- __block_literal_global.24
- __block_literal_global.26
- _objc_msgSend$initWithiTunesStoreID:appIDs:associatedDomains:associatedDomainsEnableDirectDownloads:configurationProfile:
- _objc_msgSend$provisionalEnrollmentExpirationDate
- _objc_msgSend$syncDEPPushTokenWithCompletion:
CStrings:
+ "@64@0:8@16@24@32@40@48@56"
+ "Declarations"
+ "ESSO details declaration data is invalid or missing: %{public}@"
+ "ESSO details declarations data is missing: %{public}@"
+ "ESSO details: a configuration profile and/or declarations must be present"
+ "EnrollmentSSOAppStoreID"
+ "IdleRebootAllowed"
+ "Sending DEP push received notification."
+ "Sending pending migration cloud configuration details changed notification."
+ "T@\"NSArray\",&,N,V_declarations"
+ "TB,N,V_isSingleton"
+ "_declarations"
+ "_isSingleton"
+ "_provisionalEnrollmentExpirationDateFromCloudConfig:"
+ "com.apple.devicemanagementclient.depPushReceived"
+ "com.apple.devicemanagementclient.pendingMigrationCloudConfigurationDetailsChanged"
+ "declarations"
+ "initWithCloudConfigDetails:"
+ "initWithiTunesStoreID:appIDs:associatedDomains:associatedDomainsEnableDirectDownloads:configurationProfile:declarations:"
+ "isProvisionallyEnrolledWithCloudConfig:"
+ "isRapidReturnToService"
+ "isSingleton"
+ "mdmServerUID"
+ "monitorDEPPushTokenIfNeededWithCompletion:"
+ "monitorDEPPushTokenWithCompletion:"
+ "setDeclarations:"
+ "setIsSingleton:"
+ "simulateDEPPushWithCompletion:"
+ "syncDEPPushTokenWithDelay:completion:"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "@56@0:8@16@24@32@40@48"
- "initWithiTunesStoreID:appIDs:associatedDomains:associatedDomainsEnableDirectDownloads:configurationProfile:"
- "syncDEPPushTokenWithCompletion:"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"

```
