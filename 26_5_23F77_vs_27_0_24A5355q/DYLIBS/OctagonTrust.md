## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`

```diff

-61901.120.67.0.0
-  __TEXT.__text: 0x20960
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__delay_helper: 0x99c
-  __TEXT.__objc_methlist: 0x1994
+62426.0.0.0.4
+  __TEXT.__text: 0x23888
+  __TEXT.__lazy_helpers: 0xe1c
+  __TEXT.__objc_methlist: 0x19fc
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x814
-  __TEXT.__cstring: 0x1420
-  __TEXT.__oslogstring: 0x293e
-  __TEXT.__unwind_info: 0x690
-  __TEXT.__objc_classname: 0x202
-  __TEXT.__objc_methname: 0x3ffd
-  __TEXT.__objc_methtype: 0x5b3
-  __TEXT.__objc_stubs: 0x2920
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x260
+  __TEXT.__gcc_except_tab: 0x92c
+  __TEXT.__cstring: 0x1591
+  __TEXT.__oslogstring: 0x3473
+  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf68
+  __DATA_CONST.__objc_selrefs: 0xff8
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH_CONST.__cfstring: 0x1740
+  __DATA_CONST.__got: 0x268
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__cfstring: 0x1820
   __AUTH_CONST.__objc_const: 0x24a8
+  __AUTH_CONST.__lazy_load_got: 0x150
+  __AUTH_CONST.__auth_got: 0x360
   __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x140
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7EF71B82-6D97-3960-B007-0F778FA0A053
-  Functions: 561
-  Symbols:   1984
-  CStrings:  1348
+  UUID: E1DA59CF-15BF-3B70-8C4D-3FF6190DA3CA
+  Functions: 578
+  Symbols:   2104
+  CStrings:  655
 
Symbols:
+ +[OTClique(Framework) clearCliqueFromAccount:error:]
+ +[OTClique(Framework) newFriendsWithContextData:error:]
+ +[OTClique(Framework) newFriendsWithContextData:resetReason:error:]
+ +[OTClique(Framework) performCKServerUnreadableDataRemoval:error:]
+ +[OTClique(Framework) performEscrowRecoveryWithContextData:escrowArguments:error:]
+ +[OTClique(Framework) resetProtectedData:error:]
+ +[OTClique(Framework) resetProtectedData:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:error:]
+ +[OTClique(Framework_Private) fetchTrustedDeviceList:reply:]
+ +[OTClique(Framework_Private) isCloudServicesAvailable]
+ GCC_except_table336
+ GCC_except_table342
+ GCC_except_table344
+ GCC_except_table347
+ GCC_except_table349
+ GCC_except_table351
+ GCC_except_table357
+ GCC_except_table362
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table372
+ GCC_except_table380
+ GCC_except_table382
+ GCC_except_table387
+ GCC_except_table396
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$_SecureBackup$lazyGOT
+ _OBJC_CLASS_$_SecureBackup$lazyGOT$loadHelper_x8
+ _SOSCCIsSOSTrustAndSyncingEnabledCachedValue
+ _SOSCCResetToOffering
+ __NSConcreteGlobalBlock
+ __OBJC_$_CLASS_METHODS_OTClique(Framework|Framework_Private)
+ ___100+[OTClique(Framework) resetProtectedData:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:error:]_block_invoke
+ ___52+[OTClique(Framework) clearCliqueFromAccount:error:]_block_invoke
+ ___55+[OTClique(Framework_Private) isCloudServicesAvailable]_block_invoke
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.146
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.153
+ ___66+[OTClique(Framework) performCKServerUnreadableDataRemoval:error:]_block_invoke
+ ___66+[OTClique(Framework) performCKServerUnreadableDataRemoval:error:]_block_invoke.209
+ ___67+[OTClique(Framework) newFriendsWithContextData:resetReason:error:]_block_invoke
+ ___72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.99
+ ___82+[OTClique(Framework) performEscrowRecoveryWithContextData:escrowArguments:error:]_block_invoke
+ ___82+[OTClique(Framework) performEscrowRecoveryWithContextData:escrowArguments:error:]_block_invoke.187
+ ___99+[OTClique(Framework) handleRecoveryResults:recoveredInformation:record:performedSilentBurn:error:]_block_invoke.40
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e39_v24?0"OTAccountSettings"8"NSError"16lr32l8
+ ___block_literal_global
+ __dyld_lazy_load
+ _dispatch_once
+ _isCloudServicesAvailable.onceToken
+ _kEscrowServiceRecordDataKey$lazyGOT
+ _kEscrowServiceRecordDataKey$lazyGOT$loadHelper_x8
+ _kSecureBackupAuthenticationAppleID$lazyGOT
+ _kSecureBackupAuthenticationAppleID$lazyGOT$loadHelper_x8
+ _kSecureBackupAuthenticationAuthToken$lazyGOT
+ _kSecureBackupAuthenticationAuthToken$lazyGOT$loadHelper_x8
+ _kSecureBackupAuthenticationDSID$lazyGOT
+ _kSecureBackupAuthenticationDSID$lazyGOT$loadHelper_x8
+ _kSecureBackupAuthenticationEscrowProxyURL$lazyGOT
+ _kSecureBackupAuthenticationEscrowProxyURL$lazyGOT$loadHelper_x8
+ _kSecureBackupAuthenticationPassword$lazyGOT
+ _kSecureBackupAuthenticationPassword$lazyGOT$loadHelper_x8
+ _kSecureBackupAuthenticationiCloudEnvironment$lazyGOT
+ _kSecureBackupAuthenticationiCloudEnvironment$lazyGOT$loadHelper_x8
+ _kSecureBackupBagPasswordKey$lazyGOT
+ _kSecureBackupBagPasswordKey$lazyGOT$loadHelper_x8
+ _kSecureBackupBottleIDKey$lazyGOT
+ _kSecureBackupBottleIDKey$lazyGOT$loadHelper_x8
+ _kSecureBackupBuildVersionKey$lazyGOT
+ _kSecureBackupBuildVersionKey$lazyGOT$loadHelper_x8
+ _kSecureBackupClientMetadataKey$lazyGOT
+ _kSecureBackupClientMetadataKey$lazyGOT$loadHelper_x8
+ _kSecureBackupContainsiCDPDataKey$lazyGOT
+ _kSecureBackupContainsiCDPDataKey$lazyGOT$loadHelper_x8
+ _kSecureBackupContainsiCDPDataKey$lazyGOT$loadHelper_x9
+ _kSecureBackupCoolOffEndKey$lazyGOT
+ _kSecureBackupCoolOffEndKey$lazyGOT$loadHelper_x8
+ _kSecureBackupErrorDomain$lazyGOT
+ _kSecureBackupErrorDomain$lazyGOT$loadHelper_x10
+ _kSecureBackupEscrowDateKey$lazyGOT
+ _kSecureBackupEscrowDateKey$lazyGOT$loadHelper_x8
+ _kSecureBackupEscrowedSPKIKey$lazyGOT
+ _kSecureBackupEscrowedSPKIKey$lazyGOT$loadHelper_x8
+ _kSecureBackupFMiPRecoveryKey$lazyGOT
+ _kSecureBackupFMiPRecoveryKey$lazyGOT$loadHelper_x8
+ _kSecureBackupFMiPUUIDKey$lazyGOT
+ _kSecureBackupFMiPUUIDKey$lazyGOT$loadHelper_x8
+ _kSecureBackupIDMSRecoveryKey$lazyGOT
+ _kSecureBackupIDMSRecoveryKey$lazyGOT$loadHelper_x8
+ _kSecureBackupKeybagDigestKey$lazyGOT
+ _kSecureBackupKeybagDigestKey$lazyGOT$loadHelper_x8
+ _kSecureBackupMetadataKey$lazyGOT
+ _kSecureBackupMetadataKey$lazyGOT$loadHelper_x8
+ _kSecureBackupNonViableRepairKey$lazyGOT
+ _kSecureBackupNonViableRepairKey$lazyGOT$loadHelper_x8
+ _kSecureBackupNumericPassphraseLengthKey$lazyGOT
+ _kSecureBackupNumericPassphraseLengthKey$lazyGOT$loadHelper_x8
+ _kSecureBackupPasscodeGenerationKey$lazyGOT
+ _kSecureBackupPasscodeGenerationKey$lazyGOT$loadHelper_x8
+ _kSecureBackupPassphraseKey$lazyGOT
+ _kSecureBackupPassphraseKey$lazyGOT$loadHelper_x8
+ _kSecureBackupPeerInfoDataKey$lazyGOT
+ _kSecureBackupPeerInfoDataKey$lazyGOT$loadHelper_x8
+ _kSecureBackupPeerInfoSerialNumberKey$lazyGOT
+ _kSecureBackupPeerInfoSerialNumberKey$lazyGOT$loadHelper_x8
+ _kSecureBackupRecordIDKey$lazyGOT
+ _kSecureBackupRecordIDKey$lazyGOT$loadHelper_x8
+ _kSecureBackupRecordLabelKey$lazyGOT
+ _kSecureBackupRecordLabelKey$lazyGOT$loadHelper_x8
+ _kSecureBackupRecordStatusKey$lazyGOT
+ _kSecureBackupRecordStatusKey$lazyGOT$loadHelper_x8
+ _kSecureBackupRecoveryKeyKey$lazyGOT
+ _kSecureBackupRecoveryKeyKey$lazyGOT$loadHelper_x8
+ _kSecureBackupRecoveryStatusKey$lazyGOT
+ _kSecureBackupRecoveryStatusKey$lazyGOT$loadHelper_x8
+ _kSecureBackupRemainingAttemptsKey$lazyGOT
+ _kSecureBackupRemainingAttemptsKey$lazyGOT$loadHelper_x8
+ _kSecureBackupSerialNumberKey$lazyGOT
+ _kSecureBackupSerialNumberKey$lazyGOT$loadHelper_x8
+ _kSecureBackupSilentRecoveryAttemptKey$lazyGOT
+ _kSecureBackupSilentRecoveryAttemptKey$lazyGOT$loadHelper_x8
+ _kSecureBackupUseCachedPassphraseKey$lazyGOT
+ _kSecureBackupUseCachedPassphraseKey$lazyGOT$loadHelper_x8
+ _kSecureBackupUsesComplexPassphraseKey$lazyGOT
+ _kSecureBackupUsesComplexPassphraseKey$lazyGOT$loadHelper_x8
+ _kSecureBackupUsesMultipleiCSCKey$lazyGOT
+ _kSecureBackupUsesMultipleiCSCKey$lazyGOT$loadHelper_x8
+ _kSecureBackupUsesNumericPassphraseKey$lazyGOT
+ _kSecureBackupUsesNumericPassphraseKey$lazyGOT$loadHelper_x8
+ _kSecureBackupUsesRecoveryKeyKey$lazyGOT
+ _kSecureBackupUsesRecoveryKeyKey$lazyGOT$loadHelper_x8
+ _kSecureBackupiCloudDataProtectionDeleteAllRecordsKey
+ _kSecureBackupiCloudDataProtectionDeleteAllRecordsKey$lazyGOT
+ _kSecureBackupiCloudDataProtectionDeleteAllRecordsKey$lazyGOT$loadHelper_x8
+ _kSecurityRTCErrorDomain
+ _kSecurityRTCEventNameClearCliqueFromAccount
+ _kSecurityRTCEventNameOctagonTrustLost
+ _kSecurityRTCEventNamePerformCKServerUnreadableDataRemoval
+ _kSecurityRTCEventNameRPDDeleteAllRecords
+ _kSecurityRTCEventNameResetProtectedData
+ _kSecurityRTCEventNameResetSOS
+ _kSecurityRTCFieldAccountIsDBR
+ _kSecurityRTCFieldAccountIsG
+ _kSecurityRTCFieldAccountIsW
+ _lazyLoadFlag$CloudServices
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$authenticationAppleID
+ _objc_msgSend$clearCliqueFromAccount:resetReason:isDBRv2:reply:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$disableWithInfo:
+ _objc_msgSend$fetchCliqueStatus:
+ _objc_msgSend$fetchTrustedDeviceList:reply:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$newFriendsWithContextData:resetReason:error:
+ _objc_msgSend$passwordEquivalentToken
+ _objc_msgSend$performCKServerUnreadableDataRemoval:isDBRv2:accountIsW:altDSID:reply:
+ _objc_msgSend$postNotificationName:object:userInfo:deliverImmediately:
+ _objc_msgSend$resetProtectedData:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:error:
+ _objc_msgSend$testsEnabled
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- GCC_except_table333
- GCC_except_table335
- GCC_except_table337
- GCC_except_table341
- GCC_except_table343
- GCC_except_table348
- GCC_except_table358
- GCC_except_table366
- GCC_except_table368
- GCC_except_table373
- __OBJC_$_CATEGORY_CLASS_METHODS_OTClique_$_Framework
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.144
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.151
- ___72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.97
- ___99+[OTClique(Framework) handleRecoveryResults:recoveredInformation:record:performedSilentBurn:error:]_block_invoke.37
- _dlopen
- _dlopenHelper$CloudServices
- _dlopenHelperFlag$CloudServices
- _gotLoadHelper_x10$_kSecureBackupErrorDomain
- _gotLoadHelper_x8$_OBJC_CLASS_$_SecureBackup
- _gotLoadHelper_x8$_kEscrowServiceRecordDataKey
- _gotLoadHelper_x8$_kSecureBackupAuthenticationAppleID
- _gotLoadHelper_x8$_kSecureBackupAuthenticationAuthToken
- _gotLoadHelper_x8$_kSecureBackupAuthenticationDSID
- _gotLoadHelper_x8$_kSecureBackupAuthenticationEscrowProxyURL
- _gotLoadHelper_x8$_kSecureBackupAuthenticationPassword
- _gotLoadHelper_x8$_kSecureBackupAuthenticationiCloudEnvironment
- _gotLoadHelper_x8$_kSecureBackupBagPasswordKey
- _gotLoadHelper_x8$_kSecureBackupBottleIDKey
- _gotLoadHelper_x8$_kSecureBackupBuildVersionKey
- _gotLoadHelper_x8$_kSecureBackupClientMetadataKey
- _gotLoadHelper_x8$_kSecureBackupContainsiCDPDataKey
- _gotLoadHelper_x8$_kSecureBackupCoolOffEndKey
- _gotLoadHelper_x8$_kSecureBackupEscrowDateKey
- _gotLoadHelper_x8$_kSecureBackupEscrowedSPKIKey
- _gotLoadHelper_x8$_kSecureBackupFMiPRecoveryKey
- _gotLoadHelper_x8$_kSecureBackupFMiPUUIDKey
- _gotLoadHelper_x8$_kSecureBackupIDMSRecoveryKey
- _gotLoadHelper_x8$_kSecureBackupKeybagDigestKey
- _gotLoadHelper_x8$_kSecureBackupMetadataKey
- _gotLoadHelper_x8$_kSecureBackupNonViableRepairKey
- _gotLoadHelper_x8$_kSecureBackupNumericPassphraseLengthKey
- _gotLoadHelper_x8$_kSecureBackupPasscodeGenerationKey
- _gotLoadHelper_x8$_kSecureBackupPassphraseKey
- _gotLoadHelper_x8$_kSecureBackupPeerInfoDataKey
- _gotLoadHelper_x8$_kSecureBackupPeerInfoSerialNumberKey
- _gotLoadHelper_x8$_kSecureBackupRecordIDKey
- _gotLoadHelper_x8$_kSecureBackupRecordLabelKey
- _gotLoadHelper_x8$_kSecureBackupRecordStatusKey
- _gotLoadHelper_x8$_kSecureBackupRecoveryKeyKey
- _gotLoadHelper_x8$_kSecureBackupRecoveryStatusKey
- _gotLoadHelper_x8$_kSecureBackupRemainingAttemptsKey
- _gotLoadHelper_x8$_kSecureBackupSerialNumberKey
- _gotLoadHelper_x8$_kSecureBackupSilentRecoveryAttemptKey
- _gotLoadHelper_x8$_kSecureBackupUseCachedPassphraseKey
- _gotLoadHelper_x8$_kSecureBackupUsesComplexPassphraseKey
- _gotLoadHelper_x8$_kSecureBackupUsesMultipleiCSCKey
- _gotLoadHelper_x8$_kSecureBackupUsesNumericPassphraseKey
- _gotLoadHelper_x8$_kSecureBackupUsesRecoveryKeyKey
CStrings:
+ " OctagonSignpostNameMakeNewFriends=%{public,signpost.telemetry:number1,name=OctagonSignpostNameMakeNewFriends}d "
+ " OctagonSignpostNamePerformOctagonJoin=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePerformOctagonJoin}d "
+ " OctagonSignpostNamePerformResetAndEstablishAfterFailedBottle=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePerformResetAndEstablishAfterFailedBottle}d "
+ "BEGIN [%lld]: MakeNewFriends  enableTelemetry=YES "
+ "BEGIN [%lld]: PerformOctagonJoin  enableTelemetry=YES "
+ "BEGIN [%lld]: PerformResetAndEstablishAfterFailedBottle  enableTelemetry=YES "
+ "CloudServices is unavailable on this platform"
+ "END [%lld] %fs: MakeNewFriends  OctagonSignpostNameMakeNewFriends=%{public,signpost.telemetry:number1,name=OctagonSignpostNameMakeNewFriends}d "
+ "END [%lld] %fs: PerformOctagonJoin  OctagonSignpostNamePerformOctagonJoin=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePerformOctagonJoin}d "
+ "END [%lld] %fs: PerformResetAndEstablishAfterFailedBottle  OctagonSignpostNamePerformResetAndEstablishAfterFailedBottle=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePerformResetAndEstablishAfterFailedBottle}d "
+ "MakeNewFriends"
+ "Octagon account reset succeeded"
+ "PerformOctagonJoin"
+ "PerformResetAndEstablishAfterFailedBottle"
+ "User initiated an RPD flow"
+ "account reset failed: %@"
+ "attempting an escrow recovery for context:%@, altdsid:%@"
+ "authenticationAppleID missing from configuration context"
+ "clique-clear-from-account"
+ "clique-inheritancekey"
+ "clique-newfriends"
+ "clique-perform-ckserver-unreadable-data-removal"
+ "clique-perform-ckserver-unreadable-data-removal: failed to remove data from ckserver: %@"
+ "clique-perform-ckserver-unreadable-data-removal: unable to create otcontrol: %@"
+ "clique-recovery"
+ "clique-reset-account-data"
+ "clique-reset-account-data: account reset failed: %@"
+ "clique-reset-account-data: authenticationAppleID not set on configuration context"
+ "clique-reset-account-data: failed to reset: %@"
+ "clique-reset-account-data: passwordEquivalentToken not set on configuration context"
+ "clique-reset-account-data: secure backup escrow record deletion failed: %@"
+ "clique-reset-account-data: unable to create otcontrol: %@"
+ "clique-reset-protected-data"
+ "clique-reset-protected-data: account reset failed: %@"
+ "clique-reset-protected-data: authenticationAppleID not set on configuration context"
+ "clique-reset-protected-data: failed to fetch account settings: %@"
+ "clique-reset-protected-data: passwordEquivalentToken not set on configuration context"
+ "clique-reset-protected-data: secure backup escrow record deletion failed: %@"
+ "clique-reset-protected-data: sos reset failed: %@, ignoring error and continuing with reset"
+ "clique-reset-protected-data: unable to create otcontrol: %@"
+ "com.apple.security.resetprotecteddata.complete"
+ "failed to reset octagon: %@"
+ "fetchTrustedDeviceList invoked for context:%@"
+ "fetched account settings: %@"
+ "makeNewFriends complete"
+ "makeNewFriends invoked using context: %@, altdsid: %@"
+ "octagon"
+ "octagon-fetch-trusted-device-list"
+ "passwordEquivalentToken missing from configuration context"
+ "platform does not support sos"
+ "recovery complete: %@"
+ "recovery key used during secure backup recovery, skipping bottle check"
+ "removed unreadable data from ckserver"
+ "reset octagon"
+ "sbd disableWithInfo succeeded"
+ "sbd escrow recovery failed: %@"
+ "sos reset succeeded"
+ "v8@?0"
- "#16@0:8"
- ".cxx_destruct"
- "/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices"
- "@\"NSData\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@\"OTCDPRecoveryInformation\""
- "@\"OTEscrowAuthenticationInformation\""
- "@\"OTEscrowMoveRequestContext\""
- "@\"OTEscrowRecordMetadata\""
- "@\"OTEscrowRecordMetadataClientMetadata\""
- "@\"OTEscrowRecordMetadataPasscodeGeneration\""
- "@\"OTSecureElementPeerIdentity\""
- "@\"OTWalrus\""
- "@\"OTWebAccess\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8r*16Q24"
- "@36@0:8@16B24^@28"
- "@36@0:8B16@20^@28"
- "@40@0:8@16@24^@32"
- "@40@0:8@16Q24^@32"
- "@40@0:8@16q24@32"
- "@40@0:8B16B20@24^@32"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16q24@32@40"
- "@52@0:8@16@24@32B40^@44"
- "@56@0:8@16@24@32@40^@48"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "CDPRecordContextToDictionary:"
- "Framework"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "OTAccountSettings"
- "OTCDPRecoveryInformation"
- "OTCurrentSecureElementIdentities"
- "OTCustodianRecoveryKey"
- "OTEscrowAuthenticationInformation"
- "OTEscrowCheckCallResult"
- "OTEscrowMoveRequestContext"
- "OTEscrowRecord"
- "OTEscrowRecordMetadata"
- "OTEscrowRecordMetadataClientMetadata"
- "OTEscrowRecordMetadataPasscodeGeneration"
- "OTEscrowTranslation"
- "OTICDPRecordContext"
- "OTICDPRecordSilentContext"
- "OTInheritanceKey"
- "OTSecureElementPeerIdentity"
- "OTWalrus"
- "OTWebAccess"
- "Q"
- "Q16@0:8"
- "StringAsRecordStatus:"
- "StringAsRecordViability:"
- "StringAsRecoveryStatus:"
- "StringAsViabilityStatus:"
- "T@\"NSData\",&,N,V_backupKeybagDigest"
- "T@\"NSData\",&,N,V_escrowedSpki"
- "T@\"NSData\",&,N,V_peerData"
- "T@\"NSData\",&,N,V_peerIdentifier"
- "T@\"NSData\",&,N,V_peerInfo"
- "T@\"NSData\",R,N,V_claimTokenData"
- "T@\"NSData\",R,N,V_recoveryKeyData"
- "T@\"NSData\",R,N,V_wrappedKey"
- "T@\"NSData\",R,N,V_wrappedKeyData"
- "T@\"NSData\",R,N,V_wrappingKey"
- "T@\"NSData\",R,N,V_wrappingKeyData"
- "T@\"NSMutableArray\",&,N,V_trustedPeerSecureElementIdentities"
- "T@\"NSString\",&,N,V_authenticationAppleid"
- "T@\"NSString\",&,N,V_authenticationAuthToken"
- "T@\"NSString\",&,N,V_authenticationDsid"
- "T@\"NSString\",&,N,V_authenticationEscrowproxyUrl"
- "T@\"NSString\",&,N,V_authenticationIcloudEnvironment"
- "T@\"NSString\",&,N,V_authenticationPassword"
- "T@\"NSString\",&,N,V_bottleId"
- "T@\"NSString\",&,N,V_bottleValidity"
- "T@\"NSString\",&,N,V_build"
- "T@\"NSString\",&,N,V_currentFederation"
- "T@\"NSString\",&,N,V_deviceColor"
- "T@\"NSString\",&,N,V_deviceEnclosureColor"
- "T@\"NSString\",&,N,V_deviceMid"
- "T@\"NSString\",&,N,V_deviceModel"
- "T@\"NSString\",&,N,V_deviceModelClass"
- "T@\"NSString\",&,N,V_deviceModelVersion"
- "T@\"NSString\",&,N,V_deviceName"
- "T@\"NSString\",&,N,V_escrowRecordLabel"
- "T@\"NSString\",&,N,V_expectedFederationId"
- "T@\"NSString\",&,N,V_federationId"
- "T@\"NSString\",&,N,V_fmipUuid"
- "T@\"NSString\",&,N,V_intendedFederation"
- "T@\"NSString\",&,N,V_label"
- "T@\"NSString\",&,N,V_recordId"
- "T@\"NSString\",&,N,V_recoveryKey"
- "T@\"NSString\",&,N,V_recoverySecret"
- "T@\"NSString\",&,N,V_serial"
- "T@\"NSString\",&,N,V_serialNumber"
- "T@\"NSString\",R,N,V_claimTokenString"
- "T@\"NSString\",R,N,V_recoveryString"
- "T@\"NSString\",R,N,V_wrappedKeyString"
- "T@\"NSString\",R,N,V_wrappingKeyString"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"OTCDPRecoveryInformation\",&,N,V_cdpInfo"
- "T@\"OTEscrowAuthenticationInformation\",&,N,V_authInfo"
- "T@\"OTEscrowAuthenticationInformation\",C,D,N"
- "T@\"OTEscrowMoveRequestContext\",&,V_moveRequest"
- "T@\"OTEscrowRecordMetadata\",&,N,V_escrowInformationMetadata"
- "T@\"OTEscrowRecordMetadataClientMetadata\",&,N,V_clientMetadata"
- "T@\"OTEscrowRecordMetadataPasscodeGeneration\",&,N,V_passcodeGeneration"
- "T@\"OTSecureElementPeerIdentity\",&,N,V_localPeerIdentity"
- "T@\"OTSecureElementPeerIdentity\",&,N,V_pendingLocalPeerIdentity"
- "T@\"OTWalrus\",&,N,V_walrus"
- "T@\"OTWebAccess\",&,N,V_webAccess"
- "TB,N"
- "TB,N,V_containsIcdpData"
- "TB,N,V_enabled"
- "TB,N,V_fmipRecovery"
- "TB,N,V_idmsRecovery"
- "TB,N,V_nonViableRepair"
- "TB,N,V_silentRecoveryAttempt"
- "TB,N,V_useCachedSecret"
- "TB,N,V_usePreviouslyCachedRecoveryKey"
- "TB,N,V_usesMultipleIcsc"
- "TB,R"
- "TB,R,N"
- "TB,V_needsReenroll"
- "TB,V_repairDisabled"
- "TB,V_secureTermsNeeded"
- "TQ,N,V_coolOffEnd"
- "TQ,N,V_creationDate"
- "TQ,N,V_devicePlatform"
- "TQ,N,V_remainingAttempts"
- "TQ,N,V_secureBackupMetadataTimestamp"
- "TQ,N,V_secureBackupNumericPassphraseLength"
- "TQ,N,V_secureBackupTimestamp"
- "TQ,N,V_secureBackupUsesComplexPassphrase"
- "TQ,N,V_secureBackupUsesMultipleIcscs"
- "TQ,N,V_secureBackupUsesNumericPassphrase"
- "TQ,N,V_silentAttemptAllowed"
- "TQ,N,V_value"
- "Ti,N,V_recordStatus"
- "Ti,N,V_recordViability"
- "Ti,N,V_recoveryStatus"
- "Ti,N,V_viabilityStatus"
- "Tq,V_daysLeftOnRateLimit"
- "Tq,V_octagonTrusted"
- "Tq,V_rateLimitState"
- "Tq,V_repairReason"
- "UTF8String"
- "UsefulConstructors"
- "_authInfo"
- "_authenticationAppleid"
- "_authenticationAuthToken"
- "_authenticationDsid"
- "_authenticationEscrowproxyUrl"
- "_authenticationIcloudEnvironment"
- "_authenticationPassword"
- "_backupKeybagDigest"
- "_bottleId"
- "_bottleValidity"
- "_build"
- "_cdpInfo"
- "_claimTokenData"
- "_claimTokenString"
- "_clientMetadata"
- "_containsIcdpData"
- "_coolOffEnd"
- "_creationDate"
- "_currentFederation"
- "_dateWithSecureBackupDateString:"
- "_daysLeftOnRateLimit"
- "_deviceColor"
- "_deviceEnclosureColor"
- "_deviceMid"
- "_deviceModel"
- "_deviceModelClass"
- "_deviceModelVersion"
- "_deviceName"
- "_devicePlatform"
- "_enabled"
- "_escrowInformationMetadata"
- "_escrowRecordLabel"
- "_escrowedSpki"
- "_expectedFederationId"
- "_federationId"
- "_fetchAccountWideSettingsDefaultWithForceFetch:useDefault:configuration:error:"
- "_fmipRecovery"
- "_fmipUuid"
- "_has"
- "_idmsRecovery"
- "_intendedFederation"
- "_label"
- "_localPeerIdentity"
- "_moveRequest"
- "_needsReenroll"
- "_nonViableRepair"
- "_octagonTrusted"
- "_passcodeGeneration"
- "_peerData"
- "_peerIdentifier"
- "_peerInfo"
- "_pendingLocalPeerIdentity"
- "_rateLimitState"
- "_recordId"
- "_recordStatus"
- "_recordViability"
- "_recoveryKey"
- "_recoveryKeyData"
- "_recoverySecret"
- "_recoveryStatus"
- "_recoveryString"
- "_remainingAttempts"
- "_repairDisabled"
- "_repairReason"
- "_secureBackupMetadataTimestamp"
- "_secureBackupNumericPassphraseLength"
- "_secureBackupTimestamp"
- "_secureBackupUsesComplexPassphrase"
- "_secureBackupUsesMultipleIcscs"
- "_secureBackupUsesNumericPassphrase"
- "_secureTermsNeeded"
- "_serial"
- "_serialNumber"
- "_setError"
- "_silentAttemptAllowed"
- "_silentRecoveryAttempt"
- "_stringWithSecureBackupDate:"
- "_trustedPeerSecureElementIdentities"
- "_useCachedSecret"
- "_usePreviouslyCachedRecoveryKey"
- "_usesMultipleIcsc"
- "_uuid"
- "_value"
- "_viabilityStatus"
- "_walrus"
- "_webAccess"
- "_wrappedKey"
- "_wrappedKeyData"
- "_wrappedKeyString"
- "_wrappingKey"
- "_wrappingKeyData"
- "_wrappingKeyString"
- "addEntriesFromDictionary:"
- "addMetrics:"
- "addObject:"
- "addObjectsFromArray:"
- "addTrustedPeerSecureElementIdentities:"
- "allocWithZone:"
- "altDSID"
- "appendData:"
- "appendString:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "areRecoveryKeysDistrusted:error:"
- "areRecoveryKeysDistrusted:reply:"
- "array"
- "authenticationAppleid"
- "authenticationAuthToken"
- "authenticationDsid"
- "authenticationEscrowproxyUrl"
- "authenticationIcloudEnvironment"
- "authenticationPassword"
- "backupForRecoveryKeyWithInfo:"
- "backupKeybagDigest"
- "base32:len:"
- "base64EncodedStringWithOptions:"
- "boolValue"
- "bottleId"
- "bottleValidity"
- "bytes"
- "cdpRecoveryInformationToDictionary:"
- "clearTrustedPeerSecureElementIdentities"
- "clientMetadata"
- "code"
- "componentsJoinedByString:"
- "containsIcdpData"
- "context"
- "coolOffEnd"
- "copyTo:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAndSetRecoveryKeyWithContext:error:"
- "createRecoveryKey:recoveryKey:reply:"
- "creationDate"
- "ctx"
- "data"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithCapacity:"
- "dataWithLength:"
- "dateFromString:"
- "dateWithTimeIntervalSince1970:"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decrypt:withKey:error:"
- "deliverAKDeviceListDelta:error:"
- "description"
- "deviceColor"
- "deviceEnclosureColor"
- "deviceMid"
- "deviceModel"
- "deviceModelClass"
- "deviceModelVersion"
- "deviceName"
- "devicePlatform"
- "deviceSessionID"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryToCDPRecordContext:"
- "dictionaryToCDPRecoveryInformation:"
- "dictionaryToEscrowAuthenticationInfo:"
- "dictionaryToEscrowRecord:"
- "dictionaryToMetadata:"
- "dictionaryWithObjects:forKeys:count:"
- "doesRecoveryKeyExistInOctagonAndIsCorrect:recoveryKey:error:"
- "doesRecoveryKeyExistInSOSAndIsCorrect:recoveryKey:error:"
- "domain"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encrypt:withKey:additionalAuthenticatedData:error:"
- "ensureBackupKeyExistsinSOS:"
- "errorWithDomain:code:description:"
- "errorWithDomain:code:description:underlying:"
- "errorWithDomain:code:userInfo:"
- "escrowAuth"
- "escrowAuthenticationInfoToDictionary:"
- "escrowCheck:isBackgroundCheck:error:"
- "escrowCheck:isBackgroundCheck:reply:"
- "escrowFetchSource"
- "escrowInformationMetadata"
- "escrowRecordToDictionary:"
- "escrowedSpki"
- "expectedFederationId"
- "federationId"
- "fetchAccountSettings:"
- "fetchAccountSettings:reply:"
- "fetchAccountWideSettings:error:"
- "fetchAccountWideSettingsDefaultWithForceFetch:configuration:error:"
- "fetchAccountWideSettingsWithForceFetch:arguments:reply:"
- "fetchAccountWideSettingsWithForceFetch:configuration:error:"
- "fetchAllEscrowRecords:error:"
- "fetchAndHandleEscrowRecords:shouldFilter:error:"
- "fetchEscrowRecords:error:"
- "fetchEscrowRecordsInternal:error:"
- "fetchTrustedSecureElementIdentities:"
- "fetchTrustedSecureElementIdentities:reply:"
- "filterRecords:"
- "filterViableSOSRecords:"
- "flowID"
- "fmipRecovery"
- "fmipUuid"
- "formatAsNestedJSON"
- "generateWrappingWithError:"
- "getBytes:range:"
- "handleRecoveryResults:recoveredInformation:record:performedSilentBurn:error:"
- "hasAuthInfo"
- "hasAuthenticationAppleid"
- "hasAuthenticationAuthToken"
- "hasAuthenticationDsid"
- "hasAuthenticationEscrowproxyUrl"
- "hasAuthenticationIcloudEnvironment"
- "hasAuthenticationPassword"
- "hasBackupKeybagDigest"
- "hasBottleId"
- "hasBottleValidity"
- "hasBuild"
- "hasCdpInfo"
- "hasClientMetadata"
- "hasContainsIcdpData"
- "hasCoolOffEnd"
- "hasCreationDate"
- "hasCurrentFederation"
- "hasDeviceColor"
- "hasDeviceEnclosureColor"
- "hasDeviceMid"
- "hasDeviceModel"
- "hasDeviceModelClass"
- "hasDeviceModelVersion"
- "hasDeviceName"
- "hasDevicePlatform"
- "hasEnabled"
- "hasError"
- "hasEscrowInformationMetadata"
- "hasEscrowRecordLabel"
- "hasEscrowedSpki"
- "hasExpectedFederationId"
- "hasFederationId"
- "hasFmipRecovery"
- "hasFmipUuid"
- "hasIdmsRecovery"
- "hasIntendedFederation"
- "hasLabel"
- "hasLocalPeerIdentity"
- "hasNonViableRepair"
- "hasPasscodeGeneration"
- "hasPeerData"
- "hasPeerIdentifier"
- "hasPeerInfo"
- "hasPendingLocalPeerIdentity"
- "hasRecordId"
- "hasRecordStatus"
- "hasRecordViability"
- "hasRecoveryKey"
- "hasRecoverySecret"
- "hasRecoveryStatus"
- "hasRemainingAttempts"
- "hasSecureBackupMetadataTimestamp"
- "hasSecureBackupNumericPassphraseLength"
- "hasSecureBackupTimestamp"
- "hasSecureBackupUsesComplexPassphrase"
- "hasSecureBackupUsesMultipleIcscs"
- "hasSecureBackupUsesNumericPassphrase"
- "hasSerial"
- "hasSerialNumber"
- "hasSilentAttemptAllowed"
- "hasSilentRecoveryAttempt"
- "hasUseCachedSecret"
- "hasUsePreviouslyCachedRecoveryKey"
- "hasUsesMultipleIcsc"
- "hasValue"
- "hasViabilityStatus"
- "hasWalrus"
- "hasWebAccess"
- "hash"
- "i"
- "i16@0:8"
- "i24@0:8@16"
- "idmsRecovery"
- "init"
- "initRandomKeyWithSpecifier:error:"
- "initWithBitSize:"
- "initWithBytes:length:encoding:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithConfiguration:"
- "initWithContextData:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithData:specifier:error:"
- "initWithKeySpecifier:"
- "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
- "initWithUUID:claimTokenData:wrappingKeyData:error:"
- "initWithUUID:error:"
- "initWithUUID:oldIK:error:"
- "initWithUUID:recoveryString:error:"
- "initWithUnsignedLongLong:"
- "initWithUserActivityLabel:"
- "initWithWrappedKey:wrappingKey:uuid:error:"
- "initWithWrappedKeyData:wrappingKeyData:claimTokenData:uuid:error:"
- "initWithWrappedKeyData:wrappingKeyData:uuid:error:"
- "initWithWrappedKeyData:wrappingKeyString:uuid:error:"
- "initWithWrappedKeyString:wrappingKeyData:uuid:error:"
- "intValue"
- "invalidateEscrowCache:error:"
- "invalidateEscrowCache:reply:"
- "isCloudServicesAvailable"
- "isEqual:"
- "isEqualToCustodianRecoveryKey:"
- "isEqualToData:"
- "isEqualToOTInheritanceKey:"
- "isEqualToString:"
- "isGuitarfish"
- "isKeyEquals:"
- "isMemberOfClass:"
- "isRecoveryKeyEqual:"
- "isRecoveryKeySet:"
- "isRecoveryKeySet:error:"
- "isRecoveryKeySet:reply:"
- "isRecoveryKeySetInOctagon:error:"
- "isRecoveryKeySetInSOS:error:"
- "keyData"
- "length"
- "longLongValue"
- "makeOTControl:"
- "mergeFrom:"
- "metadataToDictionary:"
- "mutableBytes"
- "mutableCopy"
- "nonViableRepair"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "octagonCapableRecordsExist"
- "otControl"
- "overrideForJoinAfterRestore"
- "parseBase32:checksumSize:error:"
- "peerInfo"
- "performEscrowRecovery:cdpContext:escrowRecord:error:"
- "performSilentEscrowRecovery:cdpContext:allRecords:error:"
- "position"
- "preflightRecoverOctagonUsingRecoveryKey:recoveryKey:error:"
- "preflightRecoverOctagonUsingRecoveryKey:recoveryKey:reply:"
- "printableWithData:checksumSize:error:"
- "q"
- "q16@0:8"
- "q40@0:8@16@24^@32"
- "readFrom:"
- "recordId"
- "recordMatchingLabel:allRecords:"
- "recordStatus"
- "recordStatusAsString:"
- "recordViability"
- "recordViabilityAsString:"
- "recoverSilentWithCDPContext:allRecords:altDSID:flowID:deviceSessionID:error:"
- "recoverWithCDPContext:escrowRecord:altDSID:flowID:deviceSessionID:error:"
- "recoverWithInfo:results:"
- "recoverWithRecoveryKey:recoveryKey:error:"
- "recoverWithRecoveryKey:recoveryKey:reply:"
- "recoveryKey"
- "recoverySecret"
- "recoveryStatus"
- "recoveryStatusAsString:"
- "registerRecoveryKeyInSOSAndBackup:recoveryKey:error:"
- "registerRecoveryKeyWithContext:recoveryKey:error:"
- "remainingAttempts"
- "removeAllObjects"
- "removeLocalSecureElementIdentityPeerID:error:"
- "removeLocalSecureElementIdentityPeerID:secureElementIdentityPeerID:reply:"
- "removeRecoveryKey:error:"
- "removeRecoveryKey:reply:"
- "removeRecoveryKeyFromBackup:"
- "removeRecoveryKeyFromSOSWhenInCircle:error:"
- "removeRecoveryKeyFromSOSWhenNOTInCircle:error:"
- "resetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:altDSID:flowID:deviceSessionID:canSendMetrics:error:"
- "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:"
- "restoreFromBottle:entropy:bottleID:reply:"
- "restoreKeychainAsyncWithPassword:keybagDigest:haveBottledPeer:viewsNotToBeRestored:error:"
- "restoreKeychainWithBackupPassword:error:"
- "sbd"
- "secureBackupMetadataTimestamp"
- "secureBackupNumericPassphraseLength"
- "secureBackupTimestamp"
- "secureBackupUsesComplexPassphrase"
- "secureBackupUsesMultipleIcscs"
- "secureBackupUsesNumericPassphrase"
- "sendMetricWithResult:error:"
- "serialNumber"
- "set"
- "setAccountSetting:error:"
- "setAccountSetting:setting:reply:"
- "setAuthInfo:"
- "setAuthenticationAppleid:"
- "setAuthenticationAuthToken:"
- "setAuthenticationDsid:"
- "setAuthenticationEscrowproxyUrl:"
- "setAuthenticationIcloudEnvironment:"
- "setAuthenticationPassword:"
- "setBackupKeybagDigest:"
- "setBottleId:"
- "setBottleValidity:"
- "setBuild:"
- "setCdpInfo:"
- "setClientMetadata:"
- "setContainsIcdpData:"
- "setCoolOffEnd:"
- "setCreationDate:"
- "setCurrentFederation:"
- "setDateFormat:"
- "setDaysLeftOnRateLimit:"
- "setDeviceColor:"
- "setDeviceEnclosureColor:"
- "setDeviceMid:"
- "setDeviceModel:"
- "setDeviceModelClass:"
- "setDeviceModelVersion:"
- "setDeviceName:"
- "setDevicePlatform:"
- "setEnabled:"
- "setEscrowAuth:"
- "setEscrowInformationMetadata:"
- "setEscrowRecordLabel:"
- "setEscrowedSpki:"
- "setExpectedFederationId:"
- "setFederationId:"
- "setFmipRecovery:"
- "setFmipUuid:"
- "setHasContainsIcdpData:"
- "setHasCoolOffEnd:"
- "setHasCreationDate:"
- "setHasDevicePlatform:"
- "setHasEnabled:"
- "setHasFmipRecovery:"
- "setHasIdmsRecovery:"
- "setHasNonViableRepair:"
- "setHasRecordStatus:"
- "setHasRecordViability:"
- "setHasRecoveryStatus:"
- "setHasRemainingAttempts:"
- "setHasSecureBackupMetadataTimestamp:"
- "setHasSecureBackupNumericPassphraseLength:"
- "setHasSecureBackupTimestamp:"
- "setHasSecureBackupUsesComplexPassphrase:"
- "setHasSecureBackupUsesMultipleIcscs:"
- "setHasSecureBackupUsesNumericPassphrase:"
- "setHasSilentAttemptAllowed:"
- "setHasSilentRecoveryAttempt:"
- "setHasUseCachedSecret:"
- "setHasUsePreviouslyCachedRecoveryKey:"
- "setHasUsesMultipleIcsc:"
- "setHasValue:"
- "setHasViabilityStatus:"
- "setIdmsRecovery:"
- "setIntendedFederation:"
- "setLabel:"
- "setLocalPeerIdentity:"
- "setLocalSecureElementIdentity:error:"
- "setLocalSecureElementIdentity:secureElementIdentity:reply:"
- "setMoveRequest:"
- "setNeedsReenroll:"
- "setNonViableRepair:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOctagonTrusted:"
- "setPasscodeGeneration:"
- "setPeerData:"
- "setPeerIdentifier:"
- "setPeerInfo:"
- "setPendingLocalPeerIdentity:"
- "setPosition:"
- "setRateLimitState:"
- "setRecordId:"
- "setRecordStatus:"
- "setRecordViability:"
- "setRecoveryKey:"
- "setRecoveryKeyWithContext:recoveryKey:error:"
- "setRecoverySecret:"
- "setRecoveryStatus:"
- "setRemainingAttempts:"
- "setRepairDisabled:"
- "setRepairReason:"
- "setSecureBackupMetadataTimestamp:"
- "setSecureBackupNumericPassphraseLength:"
- "setSecureBackupTimestamp:"
- "setSecureBackupUsesComplexPassphrase:"
- "setSecureBackupUsesMultipleIcscs:"
- "setSecureBackupUsesNumericPassphrase:"
- "setSecureTermsNeeded:"
- "setSerial:"
- "setSerialNumber:"
- "setSilentAttemptAllowed:"
- "setSilentRecoveryAttempt:"
- "setTimeZone:"
- "setTrustedPeerSecureElementIdentities:"
- "setUseCachedSecret:"
- "setUsePreviouslyCachedRecoveryKey:"
- "setUsesMultipleIcsc:"
- "setValue:"
- "setViabilityStatus:"
- "setWalrus:"
- "setWebAccess:"
- "silentRecoveryAttempt"
- "sortListPrioritizingiOSRecords:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromDate:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "substringFromIndex:"
- "substringToIndex:"
- "supportedRestorePath:"
- "supportsSecureCoding"
- "timeIntervalSince1970"
- "timeZoneForSecondsFromGMT:"
- "tlkRecoverabilityForEscrowRecord:error:"
- "tlkRecoverabilityForEscrowRecordData:recordData:source:reply:"
- "totalTrustedPeers:error:"
- "totalTrustedPeers:reply:"
- "trustedFullPeers:error:"
- "trustedFullPeers:reply:"
- "trustedPeerSecureElementIdentitiesAtIndex:"
- "trustedPeerSecureElementIdentitiesCount"
- "trustedPeerSecureElementIdentitiesType"
- "unarchivedObjectOfClass:fromData:error:"
- "unbase32:len:"
- "unwrapWithError:"
- "useCachedSecret"
- "usePreviouslyCachedRecoveryKey"
- "userInfo"
- "usesMultipleIcsc"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "verifyRecoveryKey:error:"
- "viabilityStatus"
- "viabilityStatusAsString:"
- "waitForPriorityViewKeychainDataRecovery:"
- "waitForPriorityViewKeychainDataRecovery:reply:"
- "wrapWithWrappingKey:error:"
- "writeTo:"
- "{?=\"containsIcdpData\"b1\"nonViableRepair\"b1\"silentRecoveryAttempt\"b1\"useCachedSecret\"b1\"usePreviouslyCachedRecoveryKey\"b1\"usesMultipleIcsc\"b1}"
- "{?=\"coolOffEnd\"b1\"creationDate\"b1\"remainingAttempts\"b1\"silentAttemptAllowed\"b1\"recordStatus\"b1\"recordViability\"b1\"recoveryStatus\"b1\"viabilityStatus\"b1}"
- "{?=\"devicePlatform\"b1\"secureBackupMetadataTimestamp\"b1\"secureBackupNumericPassphraseLength\"b1\"secureBackupUsesComplexPassphrase\"b1\"secureBackupUsesNumericPassphrase\"b1}"
- "{?=\"enabled\"b1}"
- "{?=\"fmipRecovery\"b1\"idmsRecovery\"b1}"
- "{?=\"secureBackupTimestamp\"b1\"secureBackupUsesMultipleIcscs\"b1}"
- "{?=\"value\"b1}"

```
