## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-638.0.5.0.0
-  __TEXT.__text: 0x6688c
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_stubs: 0x7700
-  __TEXT.__objc_methlist: 0x36dc
-  __TEXT.__const: 0xd20
-  __TEXT.__gcc_except_tab: 0x20b0
-  __TEXT.__cstring: 0x52a0
-  __TEXT.__objc_methname: 0x89f1
-  __TEXT.__objc_classname: 0x7d8
-  __TEXT.__objc_methtype: 0x1281
-  __TEXT.__oslogstring: 0x9abf
-  __TEXT.__info_plist: 0x66e
-  __TEXT.__unwind_info: 0x1188
-  __DATA_CONST.__auth_got: 0x9c8
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1c58
-  __DATA_CONST.__cfstring: 0x4a60
-  __DATA_CONST.__objc_classlist: 0x200
-  __DATA_CONST.__objc_catlist: 0x30
+638.40.5.0.0
+  __TEXT.__text: 0x497e8
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_stubs: 0x6440
+  __TEXT.__objc_methlist: 0x25d4
+  __TEXT.__const: 0x148
+  __TEXT.__gcc_except_tab: 0x1b1c
+  __TEXT.__cstring: 0x3b27
+  __TEXT.__objc_methname: 0x6cbb
+  __TEXT.__oslogstring: 0x7acf
+  __TEXT.__objc_classname: 0x70d
+  __TEXT.__objc_methtype: 0xf29
+  __TEXT.__info_plist: 0x66f
+  __TEXT.__unwind_info: 0xbc0
+  __DATA_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__got: 0x618
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x1438
+  __DATA_CONST.__cfstring: 0x36e0
+  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x168
-  __DATA_CONST.__objc_intobj: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__objc_arraydata: 0x1a0
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0x7178
-  __DATA.__objc_selrefs: 0x2200
-  __DATA.__objc_ivar: 0x3ec
-  __DATA.__objc_data: 0x1400
-  __DATA.__data: 0x5b0
-  __DATA.__bss: 0x150
+  __DATA.__objc_const: 0x5838
+  __DATA.__objc_selrefs: 0x1c20
+  __DATA.__objc_ivar: 0x284
+  __DATA.__objc_data: 0x10e0
+  __DATA.__data: 0x5a8
+  __DATA.__bss: 0x120
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1909
-  Symbols:   449
-  CStrings:  3467
+  Functions: 1265
+  Symbols:   457
+  CStrings:  2724
 
Symbols:
+ _CloudServicesAnalyticsBackupForViewName
+ _CloudServicesAnalyticsBackupWithChangesFull
+ _CloudServicesAnalyticsBackupWithChangesIncremental
+ _CloudServicesAnalyticsDoubleCreateBlob
+ _CloudServicesAnalyticsDoubleEnrollment
+ _CloudServicesAnalyticsDoubleGetClubCert
+ _CloudServicesAnalyticsDoubleRecovery
+ _CloudServicesAnalyticsDoubleRecoveryDataMatch3
+ _CloudServicesAnalyticsDoubleRecoveryPCS
+ _CloudServicesAnalyticsDoubleRecoveryPCSDataMatch
+ _CloudServicesAnalyticsGestalt
+ _CloudServicesAnalyticsLakituResponse
+ _CloudServicesAnalyticsRecoverRequest
+ _CloudServicesAnalyticsRequestV1
+ _CloudServicesAnalyticsRequestV1Fallback
+ _CloudServicesAnalyticsRequestV1ToV0Fallback
+ _CloudServicesAnalyticsRequestV2
+ _CloudServicesAnalyticsRequestV2Fallback
+ _CloudServicesAnalyticsRequestV2ToV0Fallback
+ _CloudServicesAnalyticsRestoreBackupName
+ _CloudServicesAnalyticsRestoreKeychainWithBackupBag
+ _CloudServicesAnalyticsSetConfirmedManifest
+ _CloudServicesAnalyticsiCDPKeybag
+ _CloudServicesAnalyticsiCDPKeybagRecoveryKey
+ _CloudServicesInitializeLogging
+ _CloudServicesLog
+ _CloudServicesRecoverEscrowWithRequest
+ _CloudServicesSOSRestoreMetrics
+ _CloudServicesiCloudIdentity
+ _OBJC_CLASS_$_CSCertOperations
+ _OBJC_CLASS_$_CSDateUtilities
+ _OBJC_CLASS_$_CSSESWrapper
+ _OBJC_CLASS_$_CloudServicesAnalytics
+ _OBJC_CLASS_$_CloudServicesError
+ _OBJC_CLASS_$_SecureBackup
+ _OBJC_CLASS_$_SecureBackupBeginPasscodeRequestResults
+ _SECURE_BACKUP_CONCURRENT_SERVICE_NAME
+ _SECURE_BACKUP_SERVICE_NAME
+ _SecureBackupPasscodeRequestNotifyTokenName
+ _SecureBackupSetupConcurrentProtocol
+ _SecureBackupSetupProtocol
+ _kEscrowServiceErrorDomain
+ _kEscrowServiceRecordDataKey
+ _kSecureBackupAccountIsHighSecurityKey
+ _kSecureBackupAlliCDPRecordsKey
+ _kSecureBackupBackOffDateKey
+ _kSecureBackupBagPasswordKey
+ _kSecureBackupBottleIDKey
+ _kSecureBackupBottleValidityKey
+ _kSecureBackupBuildVersionKey
+ _kSecureBackupClientMetadataKey
+ _kSecureBackupContainsEMCSDataKey
+ _kSecureBackupContainsiCloudIdentityKey
+ _kSecureBackupCoolOffEndKey
+ _kSecureBackupCountrySMSCodesKey
+ _kSecureBackupErrorDomain
+ _kSecureBackupEscrowDateKey
+ _kSecureBackupEscrowDigestKey
+ _kSecureBackupEscrowTimestampKey
+ _kSecureBackupEscrowedSPKIKey
+ _kSecureBackupFMiPDataKey
+ _kSecureBackupIDMSDataKey
+ _kSecureBackupIsEnabledKey
+ _kSecureBackupKeybagDigestKey
+ _kSecureBackupLastBackupDateKey
+ _kSecureBackupLastBackupTimestampKey
+ _kSecureBackupMetadataKey
+ _kSecureBackupNumericPassphraseLengthKey
+ _kSecureBackupPasscodeGenerationKey
+ _kSecureBackupPassphraseKey
+ _kSecureBackupPeerInfoDataKey
+ _kSecureBackupPeerInfoOSVersionKey
+ _kSecureBackupPeerInfoSerialNumberKey
+ _kSecureBackupRecordIDKey
+ _kSecureBackupRecordLabelKey
+ _kSecureBackupRecordStatusInvalid
+ _kSecureBackupRecordStatusKey
+ _kSecureBackupRecordStatusValid
+ _kSecureBackupRecoveryRequiresVerificationTokenKey
+ _kSecureBackupRecoveryStatusKey
+ _kSecureBackupRecoveryVerificationTokenLengthKey
+ _kSecureBackupRemainingAttemptsKey
+ _kSecureBackupSMSTargetInfoKey
+ _kSecureBackupSerialNumberKey
+ _kSecureBackupStingrayMetadataHashKey
+ _kSecureBackupStingrayMetadataKey
+ _kSecureBackupTriggerUpdateKey
+ _kSecureBackupUsesComplexPassphraseKey
+ _kSecureBackupUsesMultipleiCSCKey
+ _kSecureBackupUsesNumericPassphraseKey
+ _kSecureBackupUsesRandomPassphraseKey
+ _kSecureBackupUsesRecoveryKeyKey
+ _kSecureBackupiCDPDoubleEnrollmentRecordIDsKey
+ _kSecureBackupiCDPRecordsKey
+ _kSecureBackupiCloudIdentityDataKey
- _CFArrayGetCount
- _CFArrayGetValueAtIndex
- _CFDataCreateWithBytesNoCopy
- _NSCocoaErrorDomain
- _NSFilePathErrorKey
- _NSURLErrorDomain
- _NSURLErrorKey
- _OBJC_CLASS_$_NSProcessInfo
- _OBJC_CLASS_$_NSScanner
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_OTEscrowRecord
- _OBJC_CLASS_$_OTICDPRecordContext
- _OBJC_CLASS_$_SFAnalytics
- _OBJC_METACLASS_$_SFAnalytics
- _SecCertificateCopyEscrowRoots
- _SecCertificateCopyProperties
- _SecKeyCopyPublicBytes
- _SecKeyCreateWithData
- _SecPolicyCreateWithProperties
- _SecTrustCopyKey
- _SecTrustCreateWithCertificates
- _SecTrustEvaluateWithError
- _SecTrustSetAnchorCertificates
- ___memcpy_chk
- _abort
- _cc_clear
- _cc_cmp_safe
- _ccaes_cbc_decrypt_mode
- _ccaes_cbc_encrypt_mode
- _ccaes_gcm_decrypt_mode
- _ccaes_gcm_encrypt_mode
- _cccbc_init
- _cccbc_set_iv
- _ccdh_ccn_size
- _ccdh_gp_n
- _ccdigest
- _ccgcm_one_shot
- _cchmac_final
- _cchmac_init
- _cchmac_update
- _ccpad_pkcs7_decrypt
- _ccpad_pkcs7_encrypt
- _ccpbkdf2_hmac
- _ccrng
- _ccrsa_block_size
- _ccrsa_ctx_public
- _ccrsa_decrypt_oaep
- _ccrsa_encrypt_oaep
- _ccrsa_export_priv
- _ccrsa_export_priv_size
- _ccrsa_export_pub
- _ccrsa_export_pub_size
- _ccrsa_generate_fips186_key
- _ccrsa_import_pub
- _ccrsa_import_pub_n
- _ccrsa_verify_pkcs1v15
- _ccsha1_di
- _ccsha256_di
- _ccsrp_client_process_challenge
- _ccsrp_client_start_authentication
- _ccsrp_client_verify_session
- _ccsrp_ctx_init_option
- _ccsrp_generate_salt_and_verification
- _ccsrp_get_session_key_length
- _ccsrp_gp_rfc5054_2048
- _ccsrp_server_start_authentication
- _ccsrp_server_verify_session
- _ccsrp_sizeof_M_HAMK
- _dispatch_get_global_queue
- _getprogname
- _kCFAllocatorNull
- _kSecAttrKeyClass
- _kSecAttrKeyClassPrivate
- _kSecAttrKeyType
- _kSecAttrKeyTypeRSA
- _kSecMatchLimitAll
- _kSecPolicyAppleEscrowService
- _kSecPolicyAppleEscrowServiceIdKeySigning
- _kSecPolicyApplePCSEscrowService
- _kSecPolicyApplePCSEscrowServiceIdKeySigning
- _memmove
- _objc_getClass
- _objc_retain_x5
- _objc_retain_x7
- _pthread_main_np
- _strlen
- _vasprintf
CStrings:
+ "CSSRPClientRequest"
+ "authKitAccountWithAltDSID:error:"
+ "failed to look up authKitAccount: %!@(MISSING)"
+ "localStringFromDate:"
+ "secureBackupDateFromString:"
+ "v32@?0@\"EscrowSRPResponse\"8@\"CSSESWrapper\"16@\"NSError\"24"
- "\x06\t`\x86H\x01e\x03\x04\x02\x01"
- "\x11"
- "\x13\x16"
- " CloudServicesSignpostNameEnableWithRequest=%!{(MISSING)public,signpost.telemetry:number1,name=CloudServicesSignpostNameEnableWithRequest}d "
- "%!@(MISSING)"
- "%!@(MISSING): %!@(MISSING)"
- "%!d(MISSING)"
- "%!s(MISSING)"
- "+[SecureBackup daemonPasscodeRequestOpinion:]"
- "-[SecureBackup backupForRecoveryKeyWithInfo:]"
- "-[SecureBackup backupWithInfo:]"
- "-[SecureBackup beginHSA2PasscodeRequest:uuid:reason:error:]"
- "-[SecureBackup changeSMSTargetWithError:]"
- "-[SecureBackup disableWithError:]"
- "-[SecureBackup enableWithError:]"
- "-[SecureBackup getAccountInfoWithError:]"
- "-[SecureBackup isRecoveryKeySet:]"
- "-[SecureBackup prepareHSA2EscrowRecordContents:reply:]"
- "-[SecureBackup recoverSilentWithCDPContext:allRecords:error:]"
- "-[SecureBackup recoverWithCDPContext:escrowRecord:error:]"
- "-[SecureBackup recoverWithError:]"
- "-[SecureBackup removeRecoveryKeyFromBackup:]"
- "-[SecureBackup restoreKeychainAsyncWithPassword:keybagDigest:haveBottledPeer:viewsNotToBeRestored:error:]"
- "-[SecureBackup restoreKeychainWithBackupPassword:error:]"
- "-[SecureBackup startSMSChallengeWithError:]"
- "-[SecureBackup updateMetadataWithError:]"
- "-[SecureBackup verifyRecoveryKey:error:]"
- "/AppleInternal/Library/CloudServices/iCloudDevCert.der"
- "/AppleInternal/Library/CloudServices/iCloudDevCert150.der"
- "/AppleInternal/Library/CloudServices/iCloudDevCert152.der"
- "2.5.4.5"
- "731C3DF1-AB61-409D-9B4E-72CC478601CD"
- "<SBBPRR: %!@(MISSING) %!@(MISSING) %!@(MISSING) %!@(MISSING) %!@(MISSING)>"
- "?\x0f\b"
- "@\"SESWrapper\""
- "@\"SecureBackupTermsInfo\""
- "@24@0:8^{__SecCertificate=}16"
- "@28@0:8@16i24"
- "@28@0:8B16^@20"
- "@32@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16^@24"
- "@32@0:8q16@24"
- "@36@0:8B16@20^@28"
- "@36@0:8I16@20@28"
- "@40@0:8@16B24@28B36"
- "@40@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{ccrsa_full_ctx=QQ^{cczp_funcs}[1Q]}32"
- "@40@0:8@16q24@32"
- "@40@0:8I16@20@28B36"
- "@40@0:8q16@24@32"
- "@44@0:8B16@20@28^@36"
- "@48@0:8q16@24@32@40"
- "@60@0:8@16@24@32@40@48i56"
- "B80@0:8@16^^{__SecCertificate}24^^{__SecKey}32B40B44@48@56B64B68^@72"
- "BEGIN [%!l(MISSING)ld]: EnableWithRequest  enableTelemetry=YES "
- "BackupBagPassword"
- "CKPrettyError"
- "CKRecordID"
- "CKVR_SRP_SALT_LEN %!d(MISSING) != packet_salt_len %!z(MISSING)u"
- "CN"
- "CertOperations"
- "ClientMetadata"
- "CloudServicesAnalytics"
- "CloudServicesAnalytics"
- "CloudServicesAnalyticsDoubleCreateBlob"
- "CloudServicesAnalyticsDoubleEnrollment"
- "CloudServicesAnalyticsDoubleGetClubCert"
- "CloudServicesAnalyticsDoubleRecovery"
- "CloudServicesAnalyticsDoubleRecoveryDataMatch3"
- "CloudServicesAnalyticsDoubleRecoveryPCS"
- "CloudServicesAnalyticsDoubleRecoveryPCSDataMatch"
- "CloudServicesAnalyticsGestalt"
- "CloudServicesAnalyticsRecoverRequest"
- "CloudServicesAnalyticsRequestV1"
- "CloudServicesAnalyticsRequestV1Fallback"
- "CloudServicesAnalyticsRequestV1ToV0Fallback"
- "CloudServicesAnalyticsRequestV2"
- "CloudServicesAnalyticsRequestV2Fallback"
- "CloudServicesAnalyticsRequestV2ToV0Fallback"
- "CloudServicesAnalyticsRestoreKeychainWithBackupBag"
- "CloudServicesAnalyticsiCDPKeybag"
- "CloudServicesAnalyticsiCDPKeybagRecoveryKey"
- "CloudServicesBackupForViewName"
- "CloudServicesBackupWithChangesFull"
- "CloudServicesBackupWithChangesIncremental"
- "CloudServicesError"
- "CloudServicesErrorDomain"
- "CloudServicesLakituResponse"
- "CloudServicesRecoverEscrowWithRequest"
- "CloudServicesRestoreBackupName"
- "CloudServicesSOSRestoreMetrics"
- "CloudServicesSetConfirmedManifest"
- "CloudServicesiCloudIdentity"
- "Could not generate key"
- "Could not generate key: %!d(MISSING)"
- "Deserialized SecureBackup object: %!@(MISSING) %!@(MISSING)"
- "Desire password when available"
- "Dispatch doesn't have a state for us yet, opportunistically asking for the password"
- "DoubleEnrollment"
- "DoubleEnrollment attempted, but ForceCyrus is enabled"
- "END [%!l(MISSING)ld] %!f(MISSING)s: EnableWithRequest  CloudServicesSignpostNameEnableWithRequest=%!{(MISSING)public,signpost.telemetry:number1,name=CloudServicesSignpostNameEnableWithRequest}d "
- "Error copying escrow trust policy"
- "Error copying escrow trust policy"
- "Error copying root cert array"
- "Error copying root cert array"
- "Error creating SecCertificateRef"
- "Error decoding secret"
- "Error deserializing data: %!@(MISSING)"
- "Error extracting public key from certificate"
- "Escrow data too long"
- "Escrow data too long: %!l(MISSING)u"
- "Escrow error encrypting data"
- "Escrow error encrypting data"
- "Escrow error encrypting data (spare)"
- "Escrow error encrypting data (spare)"
- "EscrowServiceErrorDomain"
- "EscrowServiceEscrowData"
- "FEDERATION_MOVE"
- "Fail to parse certificate"
- "Fail to parse certificate"
- "Failed to store terms: %!@(MISSING)"
- "ForceCyrus"
- "I24@0:8^@16"
- "Issuer Name"
- "Local SRP verify failed"
- "Local SRP verify failed"
- "NSArray"
- "NSData"
- "NSDate"
- "NSDictionary"
- "NSError"
- "NSNull"
- "NSNumber"
- "NSOrderedSet"
- "NSSet"
- "NSString"
- "NSURL"
- "Need password on next unlock"
- "New SecureBackup object: %!@(MISSING) %!@(MISSING)"
- "No code for POSIX error: %!s(MISSING) (%!d(MISSING))"
- "No need for passcode"
- "OctagonEscrowMove"
- "POSIXDate"
- "PROD"
- "SBDate"
- "SESWrapper"
- "SRPClientRequest"
- "SRPInit"
- "SecKeyCopyPublicBytes failed"
- "SecTrustCreateWithCertificates failed: %!l(MISSING)d"
- "SecTrustEvaluate failed: %!@(MISSING)"
- "SecTrustEvaluateWithError() trust result = %!s(MISSING)"
- "SecTrustSetAnchorCertificates failed: %!l(MISSING)d"
- "SecureBackupAccountIsHighSecurity"
- "SecureBackupAlliCDPRecords"
- "SecureBackupAuthenticationAppleID"
- "SecureBackupAuthenticationAuthToken"
- "SecureBackupAuthenticationDSID"
- "SecureBackupAuthenticationEscrowProxyURL"
- "SecureBackupAuthenticationPassword"
- "SecureBackupAuthenticationiCloudEnvironment"
- "SecureBackupBackOffDate"
- "SecureBackupBeginPasscodeRequestResults"
- "SecureBackupContainsEMCSData"
- "SecureBackupContainsiCDPData"
- "SecureBackupContainsiCloudIdentity"
- "SecureBackupCountrySMSCodes"
- "SecureBackupDeleteDoubleOnly"
- "SecureBackupDeviceSessionIDKey"
- "SecureBackupDoubleEnrollmentRecordIDs"
- "SecureBackupEMCSIDMSDict"
- "SecureBackupEMCSManagedCredential"
- "SecureBackupEMCSOldManagedCredential"
- "SecureBackupEnabled"
- "SecureBackupErrorDomain"
- "SecureBackupEscrowDate"
- "SecureBackupEscrowDigest"
- "SecureBackupEscrowReason"
- "SecureBackupEscrowTimestamp"
- "SecureBackupExcludeiCDPRecords"
- "SecureBackupFMiPDataKey"
- "SecureBackupFMiPRecoveryKey"
- "SecureBackupFMiPUUIDKey"
- "SecureBackupFlowIDKey"
- "SecureBackupHSA2CachedPrerecordUUID"
- "SecureBackupIDMSData"
- "SecureBackupIDMSRecovery"
- "SecureBackupLastBackupDate"
- "SecureBackupLastBackupTimestamp"
- "SecureBackupMetadata"
- "SecureBackupNonViableRepairKey"
- "SecureBackupNumericPassphraseLength"
- "SecureBackupPassphrase"
- "SecureBackupRecoveryKey"
- "SecureBackupRecoveryRequiresVerificationToken"
- "SecureBackupRecoveryVerificationTokenLength"
- "SecureBackupSMSTarget"
- "SecureBackupSOSCompatibleEscrowSorting"
- "SecureBackupSilentDoubleRecovery"
- "SecureBackupSilentRecoveryAttempt"
- "SecureBackupSpecifiedFederation"
- "SecureBackupStingrayMetadata"
- "SecureBackupStingrayMetadataHash"
- "SecureBackupSuppressServerFiltering"
- "SecureBackupSynchronize"
- "SecureBackupTerms"
- "SecureBackupTermsInfo"
- "SecureBackupUseCachedPassphrase"
- "SecureBackupUsesComplexPassphrase"
- "SecureBackupUsesMultipleiCSCs"
- "SecureBackupUsesNumericPassphrase"
- "SecureBackupUsesRandomPassphrase"
- "SecureBackupUsesRecoveryKey"
- "SecureBackupVerifcationToken"
- "SecureBackupiCDPRecords"
- "SecureBackupiCloudDataProtectionDeleteAllRecords"
- "SecureBackupiCloudIdentityData"
- "Security"
- "Server Start Fails (ckvr_srp_server_start_authentication)"
- "StoredTermsInfo"
- "StringAsReason:"
- "Successfully stored terms"
- "T@\"NSData\",&,N,V_certData"
- "T@\"NSData\",&,N,V_iCloudIdentityData"
- "T@\"NSData\",&,N,V_idmsData"
- "T@\"NSData\",&,V_recoveryBlob"
- "T@\"NSData\",R,V_cert"
- "T@\"NSDate\",&,N,V_backOffDate"
- "T@\"NSDate\",C,N,V_escrowDate"
- "T@\"NSDictionary\",&,N,V_emcsDict"
- "T@\"NSDictionary\",&,N,V_escrowRecord"
- "T@\"NSDictionary\",&,N,V_metadataHash"
- "T@\"NSDictionary\",R,C,N,V_escrowRecord"
- "T@\"NSNumber\",C,N,V_specifiedFederation"
- "T@\"NSString\",&,N,V_altDSID"
- "T@\"NSString\",&,N,V_countryCode"
- "T@\"NSString\",&,N,V_deviceSessionID"
- "T@\"NSString\",&,N,V_expectedFederationID"
- "T@\"NSString\",&,N,V_flowID"
- "T@\"NSString\",&,N,V_icloudVersion"
- "T@\"NSString\",&,N,V_metadata"
- "T@\"NSString\",&,N,V_version"
- "T@\"NSString\",C,N,V_appleID"
- "T@\"NSString\",C,N,V_authToken"
- "T@\"NSString\",C,N,V_countryCode"
- "T@\"NSString\",C,N,V_countryDialCode"
- "T@\"NSString\",C,N,V_decodedLabel"
- "T@\"NSString\",C,N,V_dsid"
- "T@\"NSString\",C,N,V_emcsCred"
- "T@\"NSString\",C,N,V_escrowProxyURL"
- "T@\"NSString\",C,N,V_hsa2CachedPrerecordUUID"
- "T@\"NSString\",C,N,V_iCloudEnv"
- "T@\"NSString\",C,N,V_iCloudPassword"
- "T@\"NSString\",C,N,V_oldEMCSCred"
- "T@\"NSString\",C,N,V_passphrase"
- "T@\"NSString\",C,N,V_recordLabel"
- "T@\"NSString\",C,N,V_recoveryKey"
- "T@\"NSString\",C,N,V_recoveryPassphrase"
- "T@\"NSString\",C,N,V_smsTarget"
- "T@\"NSString\",C,N,V_verificationToken"
- "T@\"NSString\",R,C,N,V_label"
- "T@\"NSString\",R,V_dsid"
- "T@\"NSString\",R,V_escrowFederation"
- "T@\"NSString\",R,V_iCloudEnvironment"
- "T@\"NSString\",R,V_uuid"
- "T@\"NSUUID\",R,N,V_activityUUID"
- "T@\"SESWrapper\",&,N,V_ses"
- "T@\"SecureBackup\",R,&,N,V_sb"
- "T@\"SecureBackupTermsInfo\",&,N,V_termsInfo"
- "TB,N,V_deleteAll"
- "TB,N,V_deleteDoubleOnly"
- "TB,N,V_emcsMode"
- "TB,N,V_excludeiCDPRecords"
- "TB,N,V_fmipRecovery"
- "TB,N,V_icdp"
- "TB,N,V_idmsRecovery"
- "TB,N,V_nonViableRepair"
- "TB,N,V_recoveryPassphraseMutable"
- "TB,N,V_silent"
- "TB,N,V_silentDoubleRecovery"
- "TB,N,V_sosCompatibleEscrowSorting"
- "TB,N,V_stingray"
- "TB,N,V_suppressServerFiltering"
- "TB,N,V_synchronize"
- "TB,N,V_useCachedPassphrase"
- "TB,N,V_useRecoveryPET"
- "TB,N,V_usesMultipleiCSC"
- "TB,N,V_usesRandomPassphrase"
- "TB,N,V_usesRecoveryKey"
- "TQ,N,V_storageVersion"
- "T^{ckvr_srp_context=^{ccrng_state}^{ccdigest_info}^{ccmode_cbc}^{ccmode_cbc}^{ccmode_gcm}^{ccmode_gcm}^{ccsrp_ctx}},R,N,V_ckvr"
- "Ti,N,V_reason"
- "Ti,N,V_reqVersion"
- "Unable to create SecCertificateRef from response data: %!@(MISSING)"
- "Unable to extract public key"
- "Unable to find terms in keychain"
- "Username missing"
- "^{ckvr_srp_context=^{ccrng_state}^{ccdigest_info}^{ccmode_cbc}^{ccmode_cbc}^{ccmode_gcm}^{ccmode_gcm}^{ccsrp_ctx}}"
- "^{ckvr_srp_context=^{ccrng_state}^{ccdigest_info}^{ccmode_cbc}^{ccmode_cbc}^{ccmode_gcm}^{ccmode_gcm}^{ccsrp_ctx}}16@0:8"
- "_ClassCreateSecureBackupConcurrentConnection"
- "_CreateSecureBackupConnection"
- "_altDSID"
- "_backOffDate"
- "_cert"
- "_certData"
- "_ckvr"
- "_decodedLabel"
- "_deleteAll"
- "_deleteDoubleOnly"
- "_emcsCred"
- "_emcsDict"
- "_emcsMode"
- "_escrowDate"
- "_escrowFederation"
- "_escrowProxyURL"
- "_excludeiCDPRecords"
- "_expectedFederationID"
- "_getAcceptedTermsForAltDSID:withError:"
- "_hsa2CachedPrerecordUUID"
- "_iCloudIdentityData"
- "_icdp"
- "_icloudVersion"
- "_idmsData"
- "_idmsRecovery"
- "_label"
- "_metadataHash"
- "_oldEMCSCred"
- "_passphrase"
- "_reason"
- "_recordLabel"
- "_recoveryBlob"
- "_recoveryKey"
- "_recoveryPassphraseMutable"
- "_reqVersion"
- "_sb"
- "_ses"
- "_silent"
- "_smsTarget"
- "_sosCompatibleEscrowSorting"
- "_specifiedFederation"
- "_storageVersion"
- "_suppressServerFiltering"
- "_synchronize"
- "_termsInfo"
- "_useCachedPassphrase"
- "_usesMultipleiCSC"
- "_usesRandomPassphrase"
- "_usesRecoveryKey"
- "_uuid"
- "_verificationToken"
- "_version"
- "addBarrierBlock:"
- "adding extra cert"
- "asyncRequestEscrowRecordUpdate"
- "authKitAccountWithAltDSID:"
- "backOffDateWithCompletionBlock:"
- "backOffDateWithInfo:completionBlock:"
- "backOffDateWithRequest came back with %!@(MISSING)"
- "backOffDateWithRequest remote proxy error: %!l(MISSING)d"
- "backupForRecoveryKeyWithInfo remote proxy error: %!@(MISSING)"
- "backupForRecoveryKeyWithInfo:"
- "backupForRecoveryKeyWithInfoInDaemon came back with %!@(MISSING)"
- "backupWithInfo came back with %!@(MISSING)"
- "backupWithInfo remote proxy error: %!l(MISSING)d"
- "backupWithInfo:"
- "backupWithInfo:completionBlock:"
- "bad reqVersion (%!d(MISSING)) not in [0,2]"
- "beginHSA2PasscodeRequest came back with %!@(MISSING)"
- "beginHSA2PasscodeRequest remote proxy error: %!l(MISSING)d"
- "beginHSA2PasscodeRequest:error:"
- "beginHSA2PasscodeRequest:uuid:error:"
- "beginHSA2PasscodeRequest:uuid:reason:error:"
- "bottleValid"
- "build"
- "cStringUsingEncoding:"
- "cachePassphrase"
- "cachePassphraseWithCompletionBlock:"
- "cachePassphraseWithInfo:"
- "cachePassphraseWithInfo:completionBlock:"
- "cachePassphraseWithRequest remote proxy error: %!l(MISSING)d"
- "cacheRecoveryKeyWithCompletionBlock:"
- "cacheRecoveryKeyWithRequest remote proxy error: %!l(MISSING)d"
- "calling %!s(MISSING) from the main thread"
- "calling backOffDateWithRequest in daemon"
- "calling backupForRecoveryKeyWithInfoInDaemon in daemon"
- "calling backupWithInfo in daemon"
- "calling beginHSA2PasscodeRequest in daemon"
- "calling cachePassphraseWithRequest in daemon"
- "calling cachePassphraseWithRequestAsync in daemon"
- "calling cacheRecoveryKeyWithRequest in daemon"
- "calling changeSMSTargetWithRequest in daemon"
- "calling createICDPRecord in daemon"
- "calling daemonPasscodeRequestOpinion in daemon"
- "calling disableWithRequest in daemon"
- "calling enableWithRequest in daemon"
- "calling getAcceptedTermsForAltDSID in daemon"
- "calling getAccountInfoWithRequest in daemon"
- "calling getCertificatesWithRequest in daemon"
- "calling getCountrySMSCodesWithRequest in daemon"
- "calling isRecoveryKeySetInDaemon in daemon"
- "calling knownICDPFederations in daemon"
- "calling moveToFederationAllowed in daemon"
- "calling notificationInfo in daemon"
- "calling prepareHSA2EscrowRecordContents in daemon"
- "calling recoverRecordContents in daemon"
- "calling recoverSilentWithCDPContextInDaemon in daemon"
- "calling recoverWithCDPContextInDaemon in daemon"
- "calling recoverWithRequest in daemon"
- "calling removeRecoveryKeyFromBackup in daemon"
- "calling restoreKeychainAsyncWithPassword in daemon"
- "calling restoreKeychainWithBackupPassword in daemon"
- "calling saveTermsAcceptance in daemon"
- "calling setBackOffDateWithRequest in daemon"
- "calling startSMSChallengeWithRequest in daemon"
- "calling stashRecoveryDataWithRequest in daemon"
- "calling stateCapture in daemon"
- "calling uncachePassphraseWithRequest in daemon"
- "calling uncachePassphraseWithRequestAsync in daemon"
- "calling updateMetadata in daemon"
- "calling updateMetadataWithRequest in daemon"
- "calling verifyRecoveryKey in daemon"
- "can't process recovery blob with no username"
- "can't process recovery blob with no username"
- "cannot create key"
- "ccses->salt_len %!d(MISSING) != salt_len %!z(MISSING)d"
- "ccsrp_client_process_challenge failed: %!d(MISSING)"
- "cert URL = %!@(MISSING)"
- "changeSMSTargetWithCompletionBlock:"
- "changeSMSTargetWithError:"
- "changeSMSTargetWithInfo:"
- "changeSMSTargetWithInfo:completionBlock:"
- "changeSMSTargetWithRequest came back with %!@(MISSING)"
- "changeSMSTargetWithRequest remote proxy error: %!l(MISSING)d"
- "ckvr"
- "ckvr_cylon_process_blob failed"
- "ckvr_pack_srp_init_resp failed"
- "ckvr_srp_server_verify_session failed"
- "ckvr_unpack_clubh_recover_req_pkt failed"
- "codeForErrno:"
- "codeForNSError:"
- "com.apple.SecureBackupDaemon"
- "com.apple.SecureBackupDaemon.concurrent"
- "com.apple.sbd.passcode_request"
- "could not create local SRP recovery blob"
- "could not create local SRP recovery blob"
- "could not create priv key: %!@(MISSING)"
- "createICDPRecord came back with %!@(MISSING)"
- "createICDPRecord remote proxy error: %!l(MISSING)d"
- "createICDPRecordWithContents:reply:"
- "creating connection to sbd: uid %!d(MISSING), progname %!s(MISSING)"
- "daemon believes there's no need for a passcode"
- "daemon unable to determine passcode status due to keybag lock; relying on dispatch state"
- "daemonPasscodeRequestOpinion came back with %!@(MISSING)"
- "daemonPasscodeRequestOpinion remote proxy error: %!l(MISSING)d"
- "dataWithLength:"
- "databasePath"
- "dd-MM-yyyy HH:mm:ss"
- "dealloc"
- "decodeBoolForKey:"
- "decodePropertyListForKey:"
- "decodedEscrowRecordFromData: failed to convert"
- "decodedEscrowRecordFromData: failed to parse packet header"
- "defaultAnalyticsDatabasePath:"
- "disableWithCompletionBlock:"
- "disableWithError:"
- "disableWithInfo:"
- "disableWithInfo:completionBlock:"
- "disableWithRequest came back with %!@(MISSING)"
- "disableWithRequest remote proxy error: %!l(MISSING)d"
- "do initial state fetch in the background"
- "dropping extra cert, feature is disabled"
- "enableWithCompletionBlock:"
- "enableWithError:"
- "enableWithInfo:"
- "enableWithInfo:completionBlock:"
- "enableWithRequest came back with %!@(MISSING)"
- "enableWithRequest in daemon came back with %!@(MISSING)"
- "enableWithRequest remote proxy error: %!l(MISSING)d"
- "encodeBool:forKey:"
- "error serializing escrow data: %!@(MISSING)"
- "errorDomain"
- "errorForNSError:path:format:"
- "errorWithCode:URL:format:"
- "errorWithCode:error:URL:format:"
- "escrowFederation"
- "escrowFederation"
- "failed to convert srp init response"
- "failed to convert srp init response"
- "failed to create SecCertificate"
- "failed to create cert data"
- "failed to create data buffer"
- "failed to extra bytes of priv key"
- "failed to get terms for altDSID %!{(MISSING)private}@: %!@(MISSING)"
- "firstObject"
- "getAcceptedTermsForAltDSID came back with %!@(MISSING)"
- "getAcceptedTermsForAltDSID remote proxy error: %!l(MISSING)d"
- "getAcceptedTermsForAltDSID:withError:"
- "getAccountInfoWithError:"
- "getAccountInfoWithInfo:completionBlock:"
- "getAccountInfoWithInfo:completionBlockWithResults:"
- "getAccountInfoWithInfo:results:"
- "getAccountInfoWithRequest came back with %!@(MISSING)"
- "getAccountInfoWithRequest in daemon came back with %!@(MISSING)"
- "getAccountInfoWithRequest remote proxy error: %!l(MISSING)d"
- "getAccountInfoWithResults:"
- "getAllAcceptedTermsWithError:"
- "getCertificates:"
- "getCertificatesWithRequest remote proxy error: %!l(MISSING)d"
- "getCountrySMSCodesWithInfo:completionBlockWithResults:"
- "getCountrySMSCodesWithRequest came back with %!@(MISSING)"
- "getCountrySMSCodesWithRequest remote proxy error: %!l(MISSING)d"
- "getCountrySMSCodesWithResults:"
- "hasAltDSID"
- "hasCountryCode"
- "hasExpectedFederationID"
- "hasIcloudVersion"
- "hasMetadata"
- "hasReason"
- "hasStorageVersion"
- "hasTermsInfo"
- "hasVersion"
- "hsm_id_len %!z(MISSING)u not in (0,%!d(MISSING))"
- "icloudVersion"
- "icloudVersion"
- "initFileURLWithPath:isDirectory:"
- "initWithBytes:length:encoding:"
- "initWithDSID:escrowRecordContents:recoveryPassphrase:recordID:recordLabel:"
- "initWithFormat:arguments:"
- "initWithMachServiceName:options:"
- "initWithSecureBackup:"
- "initial state fetch completed with: %!d(MISSING) %!@(MISSING)"
- "invalid request: %!@(MISSING)"
- "invalidate"
- "invalidating connection"
- "isEqualToNumber:"
- "isRecoveryKeySet:"
- "isRecoveryKeySet: invoked"
- "isRecoveryKeySet: remote proxy error: %!l(MISSING)d"
- "isRecoveryKeySetInDaemon came back with %!@(MISSING)"
- "knownICDPFederations came back with %!@(MISSING)"
- "knownICDPFederations remote proxy error: %!l(MISSING)d"
- "label missing"
- "label missing for %!@(MISSING) (dsid %!@(MISSING))"
- "legacyDateFormatter"
- "localString"
- "localTimeZone"
- "logSuccessForEventNamed:"
- "moveToFederationAllowed came back with %!@(MISSING)"
- "moveToFederationAllowed remote proxy error: %!l(MISSING)d"
- "moveToFederationAllowed:altDSID:error:"
- "needPasscodeForHSA2EscrowRecordUpdate:"
- "no error"
- "notificationInfo came back with %!@(MISSING)"
- "notificationInfo:"
- "notificationInfoWithReply remote proxy error: %!l(MISSING)d"
- "numberWithUnsignedLong:"
- "osVersion"
- "pack_srp_recovery_rec failed"
- "peerInfo"
- "peerInfoSerialNumber"
- "pki_size %!z(MISSING)d < B_len %!z(MISSING)d"
- "pki_size %!z(MISSING)d > B_len %!z(MISSING)d"
- "prepareHSA2EscrowRecordContents came back with %!@(MISSING)"
- "prepareHSA2EscrowRecordContents remote proxy error: %!l(MISSING)d"
- "prepareHSA2EscrowRecordContents:reply:"
- "processInfo"
- "processName"
- "q24@0:8q16"
- "reasonAsString:"
- "recoverRecordContents came back with %!@(MISSING)"
- "recoverRecordContents:"
- "recoverRecordContentsWithRequest remote proxy error: %!l(MISSING)d"
- "recoverSilentWithCDPContext: invoked silent escrow recovery with records: %!@(MISSING)"
- "recoverSilentWithCDPContext:allRecords:error:"
- "recoverSilentWithCDPContextAndRecords: remote proxy error: %!l(MISSING)d"
- "recoverSilentWithCDPContextInDaemon came back with %!@(MISSING)"
- "recoverWithCDPContext: invoked escrow recovery with escrowRecord: %!@(MISSING)"
- "recoverWithCDPContext: remote proxy error: %!l(MISSING)d"
- "recoverWithCDPContext:escrowRecord:error:"
- "recoverWithCDPContextInDaemon came back with %!@(MISSING)"
- "recoverWithError:"
- "recoverWithInfo:completionBlock:"
- "recoverWithInfo:completionBlockWithResults:"
- "recoverWithInfo:results:"
- "recoverWithRequest came back with %!@(MISSING)"
- "recoverWithRequest remote proxy error: %!l(MISSING)d"
- "recoverWithResults:"
- "recoveryBlob"
- "recoveryPassphrase could not be converted to cstring"
- "recoveryPassphrase could not be converted to cstring"
- "recoveryPassphrase not provided"
- "recoveryPassphrase not provided"
- "recoveryPassphraseMutable"
- "recoveryResponseForBlob:"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "removeRecoveryKeyFromBackup came back with %!@(MISSING)"
- "removeRecoveryKeyFromBackup:"
- "removeRecoveryKeyFromBackup: invoked"
- "removeRecoveryKeyFromBackup: remote proxy error: %!l(MISSING)d"
- "reqVersion"
- "restoreKeychainAsyncWithPassword: invoked"
- "restoreKeychainAsyncWithPassword: remote proxy error: %!l(MISSING)d"
- "restoreKeychainAsyncWithPassword:keybagDigest:haveBottledPeer:viewsNotToBeRestored:error:"
- "restoreKeychainAsyncWithPasswordInDaemon came back with %!@(MISSING)"
- "restoreKeychainWithBackupPassword came back with %!@(MISSING)"
- "restoreKeychainWithBackupPassword: invoked"
- "restoreKeychainWithBackupPassword: remote proxy error: %!l(MISSING)d"
- "restoreKeychainWithBackupPassword:error:"
- "saveTermsAcceptance came back with %!@(MISSING)"
- "saveTermsAcceptance remote proxy error: %!l(MISSING)d"
- "sb"
- "sbd connection created"
- "scanUnsignedLongLong:"
- "secureBackupDate"
- "serial"
- "ses"
- "set"
- "setBackOffDate:"
- "setBackOffDateWithCompletionBlock:"
- "setBackOffDateWithInfo:completionBlock:"
- "setBackOffDateWithRequest came back with %!@(MISSING)"
- "setBackOffDateWithRequest remote proxy error: %!l(MISSING)d"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCountryCode:"
- "setCountryDialCode:"
- "setDecodedLabel:"
- "setDeleteAll:"
- "setDeleteDoubleOnly:"
- "setDeviceSessionID:"
- "setEmcsCred:"
- "setEmcsDict:"
- "setEmcsMode:"
- "setEscrowDate:"
- "setExcludeiCDPRecords:"
- "setExpectedFederationID:"
- "setFlowID:"
- "setFmipRecovery:"
- "setHasReason:"
- "setHasStorageVersion:"
- "setHsa2CachedPrerecordUUID:"
- "setICloudIdentityData:"
- "setIcloudVersion:"
- "setIdmsRecovery:"
- "setMetadataHash:"
- "setNonViableRepair:"
- "setOldEMCSCred:"
- "setReason:"
- "setRecordLabel:"
- "setRecoveryBlob:"
- "setRecoveryPassphrase:"
- "setRecoveryPassphraseMutable:"
- "setRemoteObjectInterface:"
- "setSes:"
- "setSilent:"
- "setSosCompatibleEscrowSorting:"
- "setStorageVersion:"
- "setSuppressServerFiltering:"
- "setSynchronize:"
- "setTermsInfo:"
- "setTimeZone:"
- "setUseCachedPassphrase:"
- "setUsesRandomPassphrase:"
- "setUsesRecoveryKey:"
- "setValuesForKeysWithDictionary:"
- "setVerificationToken:"
- "setVersion:"
- "setWithObject:"
- "setWithObjects:"
- "skipping extra cert because terms were not accepted"
- "srp recovery blob too large: %!l(MISSING)u bytes"
- "srp recovery blob too large: %!l(MISSING)u bytes"
- "srpInitNonce"
- "srpKeySize"
- "srpPublicKeySize"
- "srpRecoveryBlobFromSRPInitResponse:"
- "srpRecoveryBlobFromSRPInitResponse:error:"
- "srpRecoveryUpdateDSID:recoveryPassphrase:"
- "srpResponseForEscrowBlob:withKey:withFullCCKey:"
- "srp_challenge_process failed: %!d(MISSING), %!@(MISSING)"
- "startSMSChallengeWithError:"
- "startSMSChallengeWithInfo:completionBlock:"
- "startSMSChallengeWithInfo:completionBlockWithResults:"
- "startSMSChallengeWithInfo:results:"
- "startSMSChallengeWithRequest came back with %!@(MISSING)"
- "startSMSChallengeWithRequest remote proxy error: %!l(MISSING)d"
- "startSMSChallengeWithResults:"
- "stashRecoveryDataWithCompletionBlock:"
- "stashRecoveryDataWithInfo:completionBlock:"
- "stashRecoveryDataWithRequest came back with %!@(MISSING)"
- "stashRecoveryDataWithRequest remote proxy error: %!l(MISSING)d"
- "stateCapture came back with %!@(MISSING)"
- "stateCaptureWithCompletionBlock:"
- "stateCaptureWithReply remote proxy error: %!l(MISSING)d"
- "storageVersion"
- "storageVersion"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "terms requested with no altDSID"
- "termsInfo"
- "termsInfo"
- "timeZoneForSecondsFromGMT:"
- "unable to ask daemon for confirmation of passcode request: %!@(MISSING)"
- "unable to fetch passcode_request token"
- "unable to fetch state of passcode_request token (%!d(MISSING))"
- "uncachePassphrase"
- "uncachePassphraseWithCompletionBlock:"
- "uncachePassphraseWithInfo:"
- "uncachePassphraseWithInfo:completionBlock:"
- "uncachePassphraseWithRequest remote proxy error: %!l(MISSING)d"
- "uncacheRecoveryKeyWithCompletionBlock:"
- "uncacheRecoveryKeyWithRequest remote proxy error: %!l(MISSING)d"
- "unknown activity"
- "unknown error"
- "unknown passcode request state: %!l(MISSING)lu"
- "unknown reqVersion: %!d(MISSING)"
- "unpack_srp_init_resp_rec failed"
- "unsupported reqVersion: %!d(MISSING)"
- "updateMetadata came back with %!@(MISSING)"
- "updateMetadata remote proxy error: %!l(MISSING)d"
- "updateMetadataWithCompletionBlock:"
- "updateMetadataWithError:"
- "updateMetadataWithInfo:"
- "updateMetadataWithInfo:completionBlock:"
- "updateMetadataWithRequest came back with %!@(MISSING)"
- "updateMetadataWithRequest remote proxy error: %!l(MISSING)d"
- "username could not be converted to cstring"
- "username could not be converted to cstring"
- "username missing for %!@(MISSING) (dsid %!@(MISSING))"
- "v16@?0r*8"
- "v20@?0I8@\"NSError\"12"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v24@?0@\"SecureBackupBeginPasscodeRequestResults\"8@\"NSError\"16"
- "v32@?0@\"EscrowSRPResponse\"8@\"SESWrapper\"16@\"NSError\"24"
- "v40@?0@\"NSDictionary\"8@\"NSData\"16@\"NSData\"24@\"NSError\"32"
- "v52@0:8@16@24B32@36^@44"
- "verifyRecoveryKey came back with %!@(MISSING)"
- "verifyRecoveryKey: invoked"
- "verifyRecoveryKey: remote proxy error: %!l(MISSING)d"
- "verifycert failed: %!@(MISSING)"
- "yyyy-MM-dd HH:mm:ss"
- "yyyy-MM-dd HH:mm:ssZZZZZ"
- "{?=\"reason\"b1}"
- "{?=\"storageVersion\"b1}"

```
