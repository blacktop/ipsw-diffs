## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-52.0.0.0.0
-  __TEXT.__text: 0x2968c
-  __TEXT.__auth_stubs: 0x580
+54.0.0.0.0
+  __TEXT.__text: 0x299bc
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_methlist: 0x1aac
   __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x3d62
-  __TEXT.__cstring: 0x235d
-  __TEXT.__gcc_except_tab: 0x94c
+  __TEXT.__oslogstring: 0x3e07
+  __TEXT.__cstring: 0x237e
+  __TEXT.__gcc_except_tab: 0x980
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x8d0
-  __TEXT.__objc_classname: 0x21c
-  __TEXT.__objc_methname: 0x8569
-  __TEXT.__objc_methtype: 0x971
-  __TEXT.__objc_stubs: 0x6280
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x1258
+  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__objc_classname: 0x21b
+  __TEXT.__objc_methname: 0x865e
+  __TEXT.__objc_methtype: 0x9ae
+  __TEXT.__objc_stubs: 0x62e0
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0x1280
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ae8
+  __DATA_CONST.__objc_selrefs: 0x1b00
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x470
-  __AUTH_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__objc_arraydata: 0x480
+  __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1780
   __AUTH_CONST.__objc_const: 0x1dc0
-  __AUTH_CONST.__objc_intobj: 0x990
+  __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_arrayobj: 0x438
   __AUTH_CONST.__objc_dictobj: 0x28
   __DATA.__objc_ivar: 0x170

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2675A634-BFF9-316E-8ABA-AA402511EB80
-  Functions: 774
-  Symbols:   3002
-  CStrings:  1914
+  UUID: 8BDE5974-28E7-3870-A92E-EAA9609A4D6C
+  Functions: 776
+  Symbols:   3010
+  CStrings:  1924
 
Symbols:
+ -[DMCEnrollmentFlowController _askForMDMUsernameAndCredentialWithError:]
+ -[DMCEnrollmentFlowController _createEnterprisePersonaWithDevicePasscode:devicePasscodeContext:]
+ -[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:]
+ -[DMCEnrollmentFlowController _installESSOConfigurationWithProfileData:declarations:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:]
+ -[DMCEnrollmentFlowController _installESSODeclarations:chosenBundleID:personaID:enrollmentType:]
+ -[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]
+ -[DMCEnrollmentFlowController credentialsError]
+ -[DMCEnrollmentFlowController devicePasscodeExtractable]
+ -[DMCEnrollmentFlowController setCredentialsError:]
+ -[DMCEnrollmentFlowController setDevicePasscodeContext:]
+ -[DMCEnrollmentFlowController setDevicePasscodeExtractable:]
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table119
+ GCC_except_table126
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table140
+ GCC_except_table177
+ GCC_except_table18
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table187
+ GCC_except_table192
+ GCC_except_table197
+ GCC_except_table200
+ GCC_except_table203
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table7
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table80
+ GCC_except_table94
+ GCC_except_table97
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._credentialsError
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._devicePasscodeExtractable
+ ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.90
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.102
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.110
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.103
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.111
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_3.104
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.126
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.127
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.128
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.129
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.131
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.130
+ ___138-[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:]_block_invoke
+ ___138-[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:]_block_invoke_2
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2
+ ___56-[DMCUnenrollmentFlowController _askForPasscodeIfNeeded]_block_invoke_3
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.165
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.166
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.167
+ ___72-[DMCEnrollmentFlowController _askForMDMUsernameAndCredentialWithError:]_block_invoke
+ ___72-[DMCEnrollmentFlowController _askForMDMUsernameAndCredentialWithError:]_block_invoke_2
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke.64
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_2.68
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_3
+ ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.149
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.141
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.142
+ ___96-[DMCEnrollmentFlowController _installESSODeclarations:chosenBundleID:personaID:enrollmentType:]_block_invoke
+ ___96-[DMCEnrollmentFlowController _installESSODeclarations:chosenBundleID:personaID:enrollmentType:]_block_invoke_2
+ ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke.179
+ ___block_descriptor_40_e8_32bs_e22_v24?0"NSData"8B16B20ls32l8
+ ___block_descriptor_48_e8_32s40w_e35_v32?0"NSData"8B16"NSString"20B28ls32l8w40l8
+ ___block_descriptor_58_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_literal_global.161
+ ___block_literal_global.190
+ ___block_literal_global.93
+ _kDMCErrorLoginPromptKey
+ _objc_msgSend$_askForMDMUsernameAndCredentialWithError:
+ _objc_msgSend$_createEnterprisePersonaWithDevicePasscode:devicePasscodeContext:
+ _objc_msgSend$_installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:
+ _objc_msgSend$_installESSOConfigurationWithProfileData:declarations:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:
+ _objc_msgSend$_installESSODeclarations:chosenBundleID:personaID:enrollmentType:
+ _objc_msgSend$_installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:
+ _objc_msgSend$credentialsError
+ _objc_msgSend$devicePasscodeExtractable
+ _objc_msgSend$installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:
+ _objc_msgSend$requestDevicePasscodeContextNeedsExtractable:completionHandler:
+ _objc_msgSend$requestMDMUsernameAndPasswordWithErrorMessage:completionHandler:
+ _objc_msgSend$setCredentialsError:
+ _objc_msgSend$setDevicePasscodeContext:
+ _objc_msgSend$setDevicePasscodeExtractable:
- -[DMCEnrollmentFlowController _askForMDMUsernameAndCredential]
- -[DMCEnrollmentFlowController _createEnterprisePersonaWithDevicePasscode:devicePasscodeData:devicePasscodeDataType:]
- -[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:]
- -[DMCEnrollmentFlowController _installESSOConfigurationWithProfileData:declarations:devicePasscode:devicePasscodeContext:personaID:]
- -[DMCEnrollmentFlowController _installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:]
- -[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]
- -[DMCEnrollmentFlowController devicePasscodeDataType]
- -[DMCEnrollmentFlowController devicePasscodeData]
- -[DMCEnrollmentFlowController setDevicePasscodeData:]
- -[DMCEnrollmentFlowController setDevicePasscodeDataType:]
- -[DMCEnrollmentFlowController(Utilities) devicePasscodeContext]
- GCC_except_table104
- GCC_except_table109
- GCC_except_table112
- GCC_except_table118
- GCC_except_table125
- GCC_except_table128
- GCC_except_table131
- GCC_except_table139
- GCC_except_table176
- GCC_except_table179
- GCC_except_table182
- GCC_except_table186
- GCC_except_table19
- GCC_except_table190
- GCC_except_table196
- GCC_except_table199
- GCC_except_table202
- GCC_except_table64
- GCC_except_table67
- GCC_except_table70
- GCC_except_table72
- GCC_except_table75
- GCC_except_table79
- GCC_except_table8
- GCC_except_table93
- GCC_except_table96
- GCC_except_table99
- _OBJC_IVAR_$_DMCEnrollmentFlowController._devicePasscodeData
- _OBJC_IVAR_$_DMCEnrollmentFlowController._devicePasscodeDataType
- ___111-[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:]_block_invoke
- ___111-[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:]_block_invoke_2
- ___111-[DMCEnrollmentFlowController _installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:]_block_invoke
- ___111-[DMCEnrollmentFlowController _installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:]_block_invoke_2
- ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.87
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.107
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.96
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.108
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.97
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_3.101
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.123
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.124
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.125
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.126
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.128
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.127
- ___232-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke
- ___232-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2
- ___62-[DMCEnrollmentFlowController _askForMDMUsernameAndCredential]_block_invoke
- ___62-[DMCEnrollmentFlowController _askForMDMUsernameAndCredential]_block_invoke_2
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.160
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.161
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.162
- ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke.65
- ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_2.69
- ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.146
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.135
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.136
- ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke.174
- ___block_descriptor_48_e8_32s40w_e35_v36?0"NSData"8Q16"NSString"24B32ls32l8w40l8
- ___block_descriptor_65_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_literal_global.159
- ___block_literal_global.188
- ___block_literal_global.91
- _objc_getProperty
- _objc_msgSend$_askForMDMUsernameAndCredential
- _objc_msgSend$_createEnterprisePersonaWithDevicePasscode:devicePasscodeData:devicePasscodeDataType:
- _objc_msgSend$_installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:
- _objc_msgSend$_installESSOConfigurationWithProfileData:declarations:devicePasscode:devicePasscodeContext:personaID:
- _objc_msgSend$_installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:
- _objc_msgSend$_installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:
- _objc_msgSend$devicePasscodeData
- _objc_msgSend$devicePasscodeDataType
- _objc_msgSend$installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:
- _objc_msgSend$setDevicePasscodeData:
- _objc_msgSend$setDevicePasscodeDataType:
CStrings:
+ "-[DMCEnrollmentFlowController _askForMDMUsernameAndCredentialWithError:]_block_invoke_2"
+ "@\"NSError\""
+ "Creating Enterprise persona with passcode data context"
+ "Creating Enterprise persona with passcode string"
+ "No pending cloud config dictionary. Skipping unenrollment..."
+ "T@\"NSData\",&,N,V_devicePasscodeContext"
+ "T@\"NSError\",&,N,V_credentialsError"
+ "TB,N,V_devicePasscodeExtractable"
+ "_askForMDMUsernameAndCredentialWithError:"
+ "_createEnterprisePersonaWithDevicePasscode:devicePasscodeContext:"
+ "_credentialsError"
+ "_devicePasscodeExtractable"
+ "_installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:"
+ "_installESSOConfigurationWithProfileData:declarations:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:"
+ "_installESSODeclarations:chosenBundleID:personaID:enrollmentType:"
+ "_installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:"
+ "credentialsError"
+ "devicePasscodeExtractable"
+ "installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
+ "requestDevicePasscodeContextNeedsExtractable:completionHandler:"
+ "requestMDMUsernameAndPasswordWithErrorMessage:completionHandler:"
+ "setCredentialsError:"
+ "setDevicePasscodeContext:"
+ "setDevicePasscodeExtractable:"
+ "v100@0:8@16@24@32B40@44@52B60@64@72@80Q88B96"
+ "v24@?0@\"NSData\"8B16B20"
+ "v32@?0@\"NSData\"8B16@\"NSString\"20B28"
+ "v48@0:8@16@24@32Q40"
+ "v52@0:8@16@24@32B40@44"
+ "v60@0:8@16@24@32@40B48@52"
- "-[DMCEnrollmentFlowController _askForMDMUsernameAndCredential]_block_invoke_2"
- "T@\"NSData\",&,N,V_devicePasscodeData"
- "T@\"NSData\",R,V_devicePasscodeContext"
- "TQ,N,V_devicePasscodeDataType"
- "_askForMDMUsernameAndCredential"
- "_createEnterprisePersonaWithDevicePasscode:devicePasscodeData:devicePasscodeDataType:"
- "_devicePasscodeData"
- "_devicePasscodeDataType"
- "_installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:"
- "_installESSOConfigurationWithProfileData:declarations:devicePasscode:devicePasscodeContext:personaID:"
- "_installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:"
- "_installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:"
- "devicePasscodeData"
- "devicePasscodeDataType"
- "installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
- "setDevicePasscodeData:"
- "setDevicePasscodeDataType:"
- "v36@?0@\"NSData\"8Q16@\"NSString\"24B32"
- "v56@0:8@16@24@32@40Q48"
- "v96@0:8@16@24@32@40@48B56@60@68@76Q84B92"

```
