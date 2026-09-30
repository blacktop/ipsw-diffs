## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-59.120.4.0.0
-  __TEXT.__text: 0x2da70
+59.160.4.0.0
+  __TEXT.__text: 0x2dc4c
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x1c34
+  __TEXT.__objc_methlist: 0x1c3c
   __TEXT.__const: 0xf8
   __TEXT.__oslogstring: 0x42f7
-  __TEXT.__cstring: 0x25e6
+  __TEXT.__cstring: 0x25ea
   __TEXT.__gcc_except_tab: 0xa5c
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0xad0
+  __TEXT.__unwind_info: 0xad8
   __TEXT.__objc_classname: 0x21c
-  __TEXT.__objc_methname: 0x8c95
+  __TEXT.__objc_methname: 0x8d24
   __TEXT.__objc_methtype: 0x9f5
-  __TEXT.__objc_stubs: 0x6780
-  __DATA_CONST.__got: 0x4c0
+  __TEXT.__objc_stubs: 0x6820
+  __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__const: 0x12e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c48
+  __DATA_CONST.__objc_selrefs: 0x1c70
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x508
   __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1840
+  __AUTH_CONST.__cfstring: 0x1860
   __AUTH_CONST.__objc_const: 0x1fa0
   __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_arrayobj: 0x498

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE6AB6A1-F491-3686-9E08-0939C10D44CE
-  Functions: 822
-  Symbols:   3154
-  CStrings:  2029
+  UUID: 94120D4D-7571-3B99-99BC-4217E70AD15F
+  Functions: 823
+  Symbols:   3163
+  CStrings:  2036
 
Symbols:
+ +[DMCReturnToServiceHelper reconstructedLanguageFromLanguageString:localeIdentifier:]
+ _NSLocaleLanguageCode
+ _NSLocaleScriptCode
+ ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.99
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.108
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.113
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.116
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.124
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.109
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.114
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.117
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.125
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_3.118
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.157
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.158
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.159
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.161
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.160
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke.135
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke.150
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2.141
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2.151
+ ___65-[DMCEnrollmentFlowController _flowTerminatedWithError:canceled:]_block_invoke.38
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke.73
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_2.77
+ ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.177
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.168
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.171
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.169
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.172
+ ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke.206
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$componentsFromLocaleIdentifier:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$reconstructedLanguageFromLanguageString:localeIdentifier:
+ _objc_msgSend$regionCode
- ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.98
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.107
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.112
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.115
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.123
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.108
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.113
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.116
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.124
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_3.117
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.155
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.157
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.158
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.160
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.159
- ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke.134
- ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke.149
- ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2.140
- ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2.150
- ___65-[DMCEnrollmentFlowController _flowTerminatedWithError:canceled:]_block_invoke.37
- ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke.72
- ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_2.76
- ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.176
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.167
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.170
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.168
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.171
- ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke.205
Functions:
~ -[DMCEnrollmentFlowController _workerQueue_performFlowStep:] : 5524 -> 5616
+ +[DMCReturnToServiceHelper reconstructedLanguageFromLanguageString:localeIdentifier:]
CStrings:
+ "-%@"
+ "appendFormat:"
+ "componentsFromLocaleIdentifier:"
+ "localeWithLocaleIdentifier:"
+ "reconstructedLanguageFromLanguageString:localeIdentifier:"
+ "regionCode"

```
