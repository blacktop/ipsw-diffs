## DigitalAccess

> `/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess`

```diff

-65.3.1.0.0
-  __TEXT.__text: 0x36064
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x25f4
-  __TEXT.__const: 0x680
-  __TEXT.__cstring: 0x70b5
-  __TEXT.__oslogstring: 0x20da
-  __TEXT.__gcc_except_tab: 0x1248
-  __TEXT.__unwind_info: 0xcd0
-  __TEXT.__objc_classname: 0x50a
-  __TEXT.__objc_methname: 0x688f
-  __TEXT.__objc_methtype: 0x19fb
-  __TEXT.__objc_stubs: 0x2a40
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0xf90
-  __DATA_CONST.__objc_classlist: 0x128
+70.31.1.0.0
+  __TEXT.__text: 0x395d4
+  __TEXT.__objc_methlist: 0x2abc
+  __TEXT.__const: 0x700
+  __TEXT.__cstring: 0x8917
+  __TEXT.__oslogstring: 0x2334
+  __TEXT.__gcc_except_tab: 0x11cc
+  __TEXT.__unwind_info: 0xdb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1130
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1328
+  __DATA_CONST.__objc_selrefs: 0x1588
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x2f0
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x1f20
-  __AUTH_CONST.__objc_const: 0x43f0
-  __AUTH_CONST.__objc_intobj: 0x258
+  __DATA_CONST.__got: 0x240
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x2a60
+  __AUTH_CONST.__objc_const: 0x4b40
+  __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x2f8
-  __DATA.__data: 0x600
-  __DATA.__bss: 0x80
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x364
+  __DATA.__data: 0x6c0
+  __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x8c0
-  __DATA_DIRTY.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/SESShared.framework/SESShared

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4F30F11-6369-37EA-94DD-70AAB2328F3B
-  Functions: 956
-  Symbols:   3130
-  CStrings:  2258
+  UUID: 3254B140-B78C-3607-B223-BE317DEE4F55
+  Functions: 1065
+  Symbols:   3481
+  CStrings:  1312
 
Symbols:
+ +[DAManager(PendingPairing) createPendingPairingForManufacturer:brand:pairingPassword:supportedTransports:ppid:pti:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:]
+ +[DAManager(PendingPairing) createPendingPairingForOPURL:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:simulateBiomeEvent:]
+ +[DAManager(PendingPairing) createPendingPairingForOPURLString:]
+ +[DAManager(PendingPairing) forceMagicPairingEmailParsing]
+ +[DAManager(PendingPairing) listMagicPairingEligiblePendingPairingsForTransport:brand:completion:]
+ +[DAManager(PendingPairing) listNfcMagicPairingEligiblePendingPairingsWithBrand:completion:]
+ +[DAManager(PendingPairing) listPendingPairingObjectsWithCompletion:]
+ +[DAManager(PendingPairing) removePendingPairingWithIdentifier:]
+ +[DAManager(PendingPairing) setUserConsentForPendingPairingIdentifier:]
+ +[DAPPIDFetchRequestConfiguration supportsSecureCoding]
+ +[DAPendingPairingConfiguration supportsSecureCoding]
+ -[DAKeyPairingConfig brand]
+ -[DAKeyPairingConfig enableConnectionTimeout]
+ -[DAKeyPairingConfig initWithPassword:displayName:transport:bindingAttestation:brand:ppid:pendingPairingIdentifier:enableConnectionTimeout:additionalParameters:]
+ -[DAKeyPairingConfig initWithPassword:displayName:transport:bindingAttestation:ppid:pendingPairingIdentifier:enableConnectionTimeout:additionalParameters:]
+ -[DAKeyPairingConfig pendingPairingIdentifier]
+ -[DAKeyPairingSession createPPIDRequestForConfig:completionHandler:]
+ -[DAKeyPairingSession decryptPPIDResponse:completionHandler:]
+ -[DAKeyPairingSession handleProbingCompletionWithBrandCode:pendingPairingIdentifier:error:]
+ -[DAKeyPairingSession startProbingWithBrand:]
+ -[DAKeyPairingSession startProbingWithBrand:transport:]
+ -[DAManager(PendingPairing) createPendingPairingForManufacturer:brand:pairingPassword:supportedTransports:ppid:pti:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:]
+ -[DAManager(PendingPairing) createPendingPairingForOPURL:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:simulateBiomeEvent:]
+ -[DAManager(PendingPairing) forceMagicPairingEmailParsing]
+ -[DAManager(PendingPairing) listMagicPairingEligiblePendingPairingsForTransport:brand:completion:]
+ -[DAManager(PendingPairing) listNfcMagicPairingEligiblePendingPairingsWithBrand:completion:]
+ -[DAManager(PendingPairing) listPendingPairingObjectsWithCompletion:]
+ -[DAManager(PendingPairing) registerMagicPairingResumeProvisioningsHandler:]
+ -[DAManager(PendingPairing) registerPendingProvisioningCreationHandler:]
+ -[DAManager(PendingPairing) registerPendingProvisioningRemovalHandler:]
+ -[DAManager(PendingPairing) removePendingPairingWithIdentifier:]
+ -[DAManager(PendingPairing) setUserConsentForPendingPairingIdentifier:]
+ -[DAManager(PendingPairing) triggerMagicPairingDetection:]
+ -[DAManager(PendingPairing) unregisterOwnerPairingTestHandlers]
+ -[DAPPIDFetchRequestConfiguration .cxx_destruct]
+ -[DAPPIDFetchRequestConfiguration brand]
+ -[DAPPIDFetchRequestConfiguration copyWithZone:]
+ -[DAPPIDFetchRequestConfiguration description]
+ -[DAPPIDFetchRequestConfiguration encodeWithCoder:]
+ -[DAPPIDFetchRequestConfiguration initWithCoder:]
+ -[DAPPIDFetchRequestConfiguration initWithManufacturer:brand:vehicleIdentifier:ownerPairingToken:vehicleDiscriminator:region:]
+ -[DAPPIDFetchRequestConfiguration manufacturer]
+ -[DAPPIDFetchRequestConfiguration ownerPairingToken]
+ -[DAPPIDFetchRequestConfiguration region]
+ -[DAPPIDFetchRequestConfiguration vehicleDiscriminator]
+ -[DAPPIDFetchRequestConfiguration vehicleIdentifier]
+ -[DAPendingPairingConfiguration .cxx_destruct]
+ -[DAPendingPairingConfiguration bindingAttestation]
+ -[DAPendingPairingConfiguration brandCode]
+ -[DAPendingPairingConfiguration brand]
+ -[DAPendingPairingConfiguration copyWithZone:]
+ -[DAPendingPairingConfiguration creationDate]
+ -[DAPendingPairingConfiguration description]
+ -[DAPendingPairingConfiguration didReceiveUserConsent]
+ -[DAPendingPairingConfiguration displayName]
+ -[DAPendingPairingConfiguration encodeWithCoder:]
+ -[DAPendingPairingConfiguration expirationDate]
+ -[DAPendingPairingConfiguration initWithCoder:]
+ -[DAPendingPairingConfiguration initWithPendingPairingIdentifier:manufacturer:brand:brandCode:supportedTransports:ppid:pti:pairingState:didReceiveUserConsent:bindingAttestation:displayName:numMagicPairingAttempts:numPasswordAttempts:creationDate:expirationDate:vehicleName:userNotificationDate:]
+ -[DAPendingPairingConfiguration manufacturer]
+ -[DAPendingPairingConfiguration numMagicPairingAttempts]
+ -[DAPendingPairingConfiguration numPairingAttempts]
+ -[DAPendingPairingConfiguration numPasswordAttempts]
+ -[DAPendingPairingConfiguration pairingState]
+ -[DAPendingPairingConfiguration pendingPairingIdentifier]
+ -[DAPendingPairingConfiguration ppid]
+ -[DAPendingPairingConfiguration pti]
+ -[DAPendingPairingConfiguration supportedTransports]
+ -[DAPendingPairingConfiguration userNotificationDate]
+ -[DAPendingPairingConfiguration vehicleName]
+ -[KmlSettingsManager BluetoothProbingTimeLimit]
+ -[KmlSettingsManager BluetoothVehicleConnectionTimeLimit]
+ -[KmlSettingsManager BluetoothVehicleDetectionTimeLimit]
+ -[KmlSettingsManager NFCProbingTimeLimit]
+ -[KmlSettingsManager NFCVehicleConnectionTimeLimit]
+ -[KmlSettingsManager arrayValueForSetting:manufacturer:brand:uuid:error:]
+ -[KmlSettingsManager defaultIntValueForSetting:]
+ -[KmlSettingsManager ignoreGlobalPairingDataExtractionLanguageDenylist]
+ -[KmlSettingsManager ignorePendingPairingRateLimit]
+ -[KmlSettingsManager ignoreProcessedSpotlightIdCheck]
+ -[KmlSettingsManager intValueForSetting:manufacturer:brand:uuid:error:]
+ -[KmlSettingsManager magicPairingCooldownDurationSeconds]
+ -[KmlSettingsManager magicPairingMaxSourceAgeDays]
+ -[KmlSettingsManager magicPairingPostProvisioningCooldownDays]
+ -[KmlSettingsManager pairingDataExtractionLanguageDenyListWithError:]
+ -[KmlSettingsManager pendingPairingNotificationSchedulingStrategy]
+ -[KmlSettingsManager userInitiatedVehicleConnectionTimeLimit]
+ GCC_except_table20
+ GCC_except_table27
+ GCC_except_table32
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table51
+ GCC_except_table54
+ _DAKeyPairingConfigBrandCodeKey
+ _DAKeyPairingConfigUserInitiatedPairingKey
+ _OBJC_CLASS_$_DAPPIDFetchRequestConfiguration
+ _OBJC_CLASS_$_DAPendingPairingConfiguration
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_DAKeyPairingConfig._brand
+ _OBJC_IVAR_$_DAKeyPairingConfig._enableConnectionTimeout
+ _OBJC_IVAR_$_DAKeyPairingConfig._pendingPairingIdentifier
+ _OBJC_IVAR_$_DAPPIDFetchRequestConfiguration._brand
+ _OBJC_IVAR_$_DAPPIDFetchRequestConfiguration._manufacturer
+ _OBJC_IVAR_$_DAPPIDFetchRequestConfiguration._ownerPairingToken
+ _OBJC_IVAR_$_DAPPIDFetchRequestConfiguration._region
+ _OBJC_IVAR_$_DAPPIDFetchRequestConfiguration._vehicleDiscriminator
+ _OBJC_IVAR_$_DAPPIDFetchRequestConfiguration._vehicleIdentifier
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._bindingAttestation
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._brand
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._brandCode
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._creationDate
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._didReceiveUserConsent
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._displayName
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._expirationDate
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._manufacturer
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._numMagicPairingAttempts
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._numPasswordAttempts
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._pairingState
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._pendingPairingIdentifier
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._ppid
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._pti
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._supportedTransports
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._userNotificationDate
+ _OBJC_IVAR_$_DAPendingPairingConfiguration._vehicleName
+ _OBJC_IVAR_$_KmlSettingsManager._defaultSLGBoolValues
+ _OBJC_IVAR_$_KmlSettingsManager._defaultSLGIntValues
+ _OBJC_IVAR_$_KmlSettingsManager._slgBoolOverrideKeys
+ _OBJC_IVAR_$_KmlSettingsManager._slgIntOverrideKeys
+ _OBJC_METACLASS_$_DAPPIDFetchRequestConfiguration
+ _OBJC_METACLASS_$_DAPendingPairingConfiguration
+ __OBJC_$_CLASS_METHODS_DAManager(HydraKey|PendingPairing|AliroKey)
+ __OBJC_$_CLASS_METHODS_DAPPIDFetchRequestConfiguration
+ __OBJC_$_CLASS_METHODS_DAPendingPairingConfiguration
+ __OBJC_$_CLASS_PROP_LIST_DAPPIDFetchRequestConfiguration
+ __OBJC_$_CLASS_PROP_LIST_DAPendingPairingConfiguration
+ __OBJC_$_INSTANCE_METHODS_DAManager(HydraKey|PendingPairing|AliroKey)
+ __OBJC_$_INSTANCE_METHODS_DAPPIDFetchRequestConfiguration
+ __OBJC_$_INSTANCE_METHODS_DAPendingPairingConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_DAPPIDFetchRequestConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_DAPendingPairingConfiguration
+ __OBJC_$_PROP_LIST_DAPPIDFetchRequestConfiguration
+ __OBJC_$_PROP_LIST_DAPendingPairingConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_KmlPendingPairingProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_KmlPendingPairingProtocol
+ __OBJC_$_PROTOCOL_REFS_KmlPendingPairingProtocol
+ __OBJC_$_PROTOCOL_REFS_KmlXpcServiceProtocol
+ __OBJC_CLASS_PROTOCOLS_$_DAPPIDFetchRequestConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_DAPendingPairingConfiguration
+ __OBJC_CLASS_RO_$_DAPPIDFetchRequestConfiguration
+ __OBJC_CLASS_RO_$_DAPendingPairingConfiguration
+ __OBJC_LABEL_PROTOCOL_$_KmlPendingPairingProtocol
+ __OBJC_LABEL_PROTOCOL_$_KmlXpcServiceProtocol
+ __OBJC_METACLASS_RO_$_DAPPIDFetchRequestConfiguration
+ __OBJC_METACLASS_RO_$_DAPendingPairingConfiguration
+ __OBJC_PROTOCOL_$_KmlPendingPairingProtocol
+ __OBJC_PROTOCOL_$_KmlXpcServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_KmlXpcServiceProtocol
+ ___102-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.54
+ ___102-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:fromMailboxIdentifier:completionHandler:]_block_invoke.36
+ ___105-[DAKeyManagementSession hasUpgradeAvailableForKeyWithIdentifier:versionType:versions:completionHandler:]_block_invoke.40
+ ___105-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.57
+ ___107-[DAKeySharingSession sendSharingInvitationForKeyIdentifier:toIdsIdentifier:auth:config:completionHandler:]_block_invoke.19
+ ___108-[DAKeyManagementSession upgradeKeyWithIdentifier:versionType:version:upgradeInformation:completionHandler:]_block_invoke.42
+ ___108-[DAKeySharingSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.55
+ ___108-[DAKeySharingSession setMailboxIdentifier:forOwnerKeyIdentifier:forInvitationIdentifier:completionHandler:]_block_invoke.34
+ ___109-[DAKeySharingSession sendSilentSharingInvitationWithKeyIdentifier:config:groupIdentifier:completionHandler:]_block_invoke.21
+ ___110-[DAKeySharingSession acceptSharingInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.28
+ ___111-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.58
+ ___113-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:]_block_invoke.45
+ ___116-[DAKeySharingSession acceptCrossPlatformInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.39
+ ___122-[DAKeyManagementSession revokeNodesWithGroupIdentifiers:treesWithGroupIdentifier:authorizedByKeyWithIdentifier:callback:]_block_invoke.39
+ ___133-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:ourBindingAttestation:config:completionHandler:]_block_invoke.31
+ ___23-[DASession endSession]_block_invoke.20
+ ___239-[DAManager(PendingPairing) createPendingPairingForOPURL:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:simulateBiomeEvent:]_block_invoke
+ ___239-[DAManager(PendingPairing) createPendingPairingForOPURL:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:simulateBiomeEvent:]_block_invoke.11
+ ___278-[DAManager(PendingPairing) createPendingPairingForManufacturer:brand:pairingPassword:supportedTransports:ppid:pti:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:]_block_invoke
+ ___278-[DAManager(PendingPairing) createPendingPairingForManufacturer:brand:pairingPassword:supportedTransports:ppid:pti:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:]_block_invoke.2
+ ___35-[DAManager establishXpcConnection]_block_invoke.79
+ ___35-[DAManager establishXpcConnection]_block_invoke.79.cold.1
+ ___46-[DAKeyPairingSession preWarmForManufacturer:]_block_invoke.220
+ ___46-[DAManager createPairingSessionWithDelegate:]_block_invoke.82
+ ___46-[DAManager createSharingSessionWithDelegate:]_block_invoke.85
+ ___47-[DAKeySharingSession cancelSharingInvitation:]_block_invoke.24
+ ___49-[DAKeyPairingSession startKeyPairingWithConfig:]_block_invoke.225
+ ___49-[DAManager createManagementSessionWithDelegate:]_block_invoke.88
+ ___54-[DAKeyManagementSession deleteKey:completionHandler:]_block_invoke.21
+ ___55-[DAKeyPairingSession startProbingWithBrand:transport:]_block_invoke
+ ___55-[DAKeyPairingSession startProbingWithBrand:transport:]_block_invoke.227
+ ___58-[DAManager(PendingPairing) forceMagicPairingEmailParsing]_block_invoke
+ ___58-[DAManager(PendingPairing) forceMagicPairingEmailParsing]_block_invoke.25
+ ___58-[DAManager(PendingPairing) triggerMagicPairingDetection:]_block_invoke
+ ___58-[DAManager(PendingPairing) triggerMagicPairingDetection:]_block_invoke.24
+ ___59-[DAKeyManagementSession localDeleteKey:completionHandler:]_block_invoke.28
+ ___61-[DAKeyPairingSession decryptPPIDResponse:completionHandler:]_block_invoke
+ ___61-[DAKeyPairingSession decryptPPIDResponse:completionHandler:]_block_invoke.223
+ ___63-[DAManager(PendingPairing) unregisterOwnerPairingTestHandlers]_block_invoke
+ ___64-[DAManager(PendingPairing) removePendingPairingWithIdentifier:]_block_invoke
+ ___64-[DAManager(PendingPairing) removePendingPairingWithIdentifier:]_block_invoke.1
+ ___65-[DAKeySharingSession cancelSharingInvitation:completionHandler:]_block_invoke.27
+ ___65-[DAKeySharingSession requestInviteWithConfig:completionHandler:]_block_invoke.30
+ ___68-[DAKeyPairingSession createPPIDRequestForConfig:completionHandler:]_block_invoke
+ ___68-[DAKeyPairingSession createPPIDRequestForConfig:completionHandler:]_block_invoke.221
+ ___69+[DAManager(PendingPairing) listPendingPairingObjectsWithCompletion:]_block_invoke
+ ___69-[DAKeyManagementSession listReceivedSharingInvitationsWithCallback:]_block_invoke.27
+ ___69-[DAManager(PendingPairing) listPendingPairingObjectsWithCompletion:]_block_invoke
+ ___69-[DAManager(PendingPairing) listPendingPairingObjectsWithCompletion:]_block_invoke.16
+ ___71-[DAKeySharingSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.53
+ ___71-[DAManager(PendingPairing) registerPendingProvisioningRemovalHandler:]_block_invoke
+ ___71-[DAManager(PendingPairing) setUserConsentForPendingPairingIdentifier:]_block_invoke
+ ___71-[DAManager(PendingPairing) setUserConsentForPendingPairingIdentifier:]_block_invoke.17
+ ___72-[DAKeySharingSession retryPasscode:forKeyIdentifier:completionHandler:]_block_invoke.46
+ ___72-[DAManager(PendingPairing) registerPendingProvisioningCreationHandler:]_block_invoke
+ ___73-[DAKeyManagementSession cancelInvitationWithIdentifier:reason:callback:]_block_invoke.34
+ ___74-[DAKeyManagementSession cancelAllFriendInvitationsWithCompletionHandler:]_block_invoke.29
+ ___74-[DAKeyManagementSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.56
+ ___74-[DAKeyManagementSession listSharingInvitationsForKeyIdentifier:callback:]_block_invoke.25
+ ___74-[DAKeyManagementSession removeSharingInvitationWithId:completionHandler:]_block_invoke.30
+ ___74-[DAKeySharingSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.60
+ ___74-[DAKeySharingSession updateSharingAnalyticsWithConfig:completionHandler:]_block_invoke.47
+ ___75-[DAKeySharingSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.50
+ ___76-[DAManager(PendingPairing) registerMagicPairingResumeProvisioningsHandler:]_block_invoke
+ ___77-[DAKeyManagementSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.63
+ ___78-[DAKeyManagementSession countImmobilizerTokensForKeyWithIdentifier:callback:]_block_invoke.31
+ ___78-[DAKeyManagementSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.54
+ ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.232
+ ___79-[DAKeySharingSession retryPasscode:forInvitationIdentifier:completionHandler:]_block_invoke.45
+ ___80-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.57
+ ___80-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:]_block_invoke.35
+ ___80-[DAManager handleSharingMessage:forInvitationIdentifier:fromMailboxIdentifier:]_block_invoke.90
+ ___81-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.49
+ ___81-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:completionHandler:]_block_invoke.40
+ ___82-[DAKeySharingSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.48
+ ___83-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.60
+ ___83-[DAKeySharingSession authorizeSharingInvitationIdentifier:auth:completionHandler:]_block_invoke.23
+ ___83-[DAKeySharingSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.58
+ ___85-[DAKeyManagementSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.52
+ ___85-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:completionHandler:]_block_invoke.51
+ ___86-[DAKeyManagementSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.61
+ ___86-[DAKeySharingSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.59
+ ___87-[DAKeySharingSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.51
+ ___88-[DAKeySharingSession handleInitiatorMessage:forInvitationIdentifier:completionHandler:]_block_invoke.43
+ ___88-[DAKeySharingSession handleRecipientMessage:forInvitationIdentifier:completionHandler:]_block_invoke.41
+ ___89-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.62
+ ___90-[DAKeyManagementSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.55
+ ___90-[DAKeyManagementSession removeSharedKeysWithIdentifiers:ownerKeyWithIdentifier:callback:]_block_invoke.36
+ ___90-[DAKeySharingSession createSilentSharingInvitationWithGroupIdentifier:completionHandler:]_block_invoke.32
+ ___91-[DAKeyPairingSession handleProbingCompletionWithBrandCode:pendingPairingIdentifier:error:]_block_invoke
+ ___92+[DAManager(PendingPairing) listNfcMagicPairingEligiblePendingPairingsWithBrand:completion:]_block_invoke
+ ___92-[DAKeyManagementSession revokeKeysWithIdentifiers:sharedByOwnerKeyWithIdentifier:callback:]_block_invoke.37
+ ___92-[DAManager(PendingPairing) listNfcMagicPairingEligiblePendingPairingsWithBrand:completion:]_block_invoke
+ ___92-[DAManager(PendingPairing) listNfcMagicPairingEligiblePendingPairingsWithBrand:completion:]_block_invoke.14
+ ___96-[DAKeySharingSession acceptSharingInvitation:fromMailboxIdentifier:passcode:completionHandler:]_block_invoke.37
+ ___97-[DAKeyManagementSession cancelInvitationsWithIdentifiers:sentByOwnerKeyWithIdentifier:callback:]_block_invoke.33
+ ___98+[DAManager(PendingPairing) listMagicPairingEligiblePendingPairingsForTransport:brand:completion:]_block_invoke
+ ___98-[DAKeyManagementSession commitUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.43
+ ___98-[DAKeyManagementSession revertUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.44
+ ___98-[DAManager(PendingPairing) listMagicPairingEligiblePendingPairingsForTransport:brand:completion:]_block_invoke
+ ___98-[DAManager(PendingPairing) listMagicPairingEligiblePendingPairingsForTransport:brand:completion:]_block_invoke.15
+ ___block_descriptor_40_e8_32r_e18_v16?0"NSString"8lr32l8
+ ___block_descriptor_40_e8_32r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48lr32l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSError"8"NSArray"16lr32l8r40l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.10
+ ___block_literal_global.106
+ ___block_literal_global.108
+ ___block_literal_global.110
+ ___block_literal_global.19
+ ___block_literal_global.21
+ ___block_literal_global.23
+ ___block_literal_global.27
+ ___block_literal_global.29
+ ___block_literal_global.34
+ ___block_literal_global.363
+ ___block_literal_global.431
+ ___exp10
+ ___kmlUtilUserVisibleLen_block_invoke
+ _decodeWithData:error:.allowedClasses.361
+ _decodeWithData:error:.allowedClasses.429
+ _decodeWithData:error:.pred.360
+ _decodeWithData:error:.pred.428
+ _kmlUtilDecodeHTMLEntities
+ _kmlUtilFullyDecodeURL
+ _kmlUtilGeneratePairingSourceIdentifier
+ _kmlUtilRoundToSignificantDigit
+ _kmlUtilUserVisibleLen
+ _log10
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$arrayValueForSetting:manufacturer:brand:uuid:error:
+ _objc_msgSend$brandCode
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$connection
+ _objc_msgSend$createPPIDRequestForConfig:callback:
+ _objc_msgSend$createPendingPairingForManufacturer:brand:pairingPassword:supportedTransports:ppid:pti:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:
+ _objc_msgSend$createPendingPairingForManufacturer:brand:pairingPassword:supportedTransports:ppid:pti:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:callback:
+ _objc_msgSend$createPendingPairingForOPURL:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:simulateBiomeEvent:
+ _objc_msgSend$createPendingPairingForOPURL:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:simulateBiomeEvent:callback:
+ _objc_msgSend$creationDate
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$decryptPPIDResponse:callback:
+ _objc_msgSend$defaultIntValueForSetting:
+ _objc_msgSend$didFinishProbingWithBrandCode:pendingPairingIdentifier:error:
+ _objc_msgSend$didReceiveUserConsent
+ _objc_msgSend$distantPast
+ _objc_msgSend$establishXpcConnection
+ _objc_msgSend$expirationDate
+ _objc_msgSend$forceMagicPairingEmailParsing
+ _objc_msgSend$forceMagicPairingEmailParsingWithCallback:
+ _objc_msgSend$initWithManufacturer:brand:vehicleIdentifier:ownerPairingToken:vehicleDiscriminator:region:
+ _objc_msgSend$initWithPassword:displayName:transport:bindingAttestation:brand:ppid:pendingPairingIdentifier:enableConnectionTimeout:additionalParameters:
+ _objc_msgSend$initWithPendingPairingIdentifier:manufacturer:brand:brandCode:supportedTransports:ppid:pti:pairingState:didReceiveUserConsent:bindingAttestation:displayName:numMagicPairingAttempts:numPasswordAttempts:creationDate:expirationDate:vehicleName:userNotificationDate:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$intValueForSetting:manufacturer:brand:uuid:error:
+ _objc_msgSend$listMagicPairingEligiblePendingPairingsForTransport:brand:callback:
+ _objc_msgSend$listMagicPairingEligiblePendingPairingsForTransport:brand:completion:
+ _objc_msgSend$listNfcMagicPairingEligiblePendingPairingsWithBrand:callback:
+ _objc_msgSend$listNfcMagicPairingEligiblePendingPairingsWithBrand:completion:
+ _objc_msgSend$listPendingPairingObjectsWithCallback:
+ _objc_msgSend$listPendingPairingObjectsWithCompletion:
+ _objc_msgSend$now
+ _objc_msgSend$numMagicPairingAttempts
+ _objc_msgSend$numPasswordAttempts
+ _objc_msgSend$pairingState
+ _objc_msgSend$pendingPairingIdentifier
+ _objc_msgSend$ppid
+ _objc_msgSend$pti
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$registerMagicPairingResumeProvisioningHandler:
+ _objc_msgSend$registerPendingProvisioningCreationHandler:
+ _objc_msgSend$registerPendingProvisioningRemovalHandler:
+ _objc_msgSend$removePendingPairingWithIdentifier:
+ _objc_msgSend$removePendingPairingWithIdentifier:callback:
+ _objc_msgSend$ses_appendU16BE:
+ _objc_msgSend$setUserConsentForPendingPairingIdentifier:
+ _objc_msgSend$setUserConsentForPendingPairingIdentifier:callback:
+ _objc_msgSend$startProbingWithBrand:transport:
+ _objc_msgSend$startProbingWithBrand:transport:callback:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByRemovingPercentEncoding
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$triggerMagicPairingDetection:callback:
+ _objc_msgSend$unregisterOwnerPairingTestHandlers
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$userNotificationDate
+ _objc_msgSend$vehicleName
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x8
- -[DAKeyPairingConfig btAddress]
- -[DAKeyPairingConfig btIRK]
- -[DAKeyPairingConfig initWithPassword:displayName:transport:bindingAttestation:ppid:btAddress:btIRK:additionalParameters:]
- -[DAKeyPairingSession handleProbingCompletionWithBrandCode:error:]
- -[DAManager establishXpcConnection].cold.1
- -[KmlSettingsManager buildNonOSPPreShareTlvOverride]
- GCC_except_table103
- GCC_except_table108
- GCC_except_table63
- _NSLog
- _OBJC_IVAR_$_DAKeyPairingConfig._btAddress
- _OBJC_IVAR_$_DAKeyPairingConfig._btIRK
- _OBJC_IVAR_$_KmlSettingsManager._defaultSLGValues
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- __OBJC_$_CLASS_METHODS_DAManager(HydraKey|AliroKey)
- __OBJC_$_INSTANCE_METHODS_DAManager
- __OBJC_PROTOCOL_REFERENCE_$_KmlManagerProtocol
- ___102-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.48
- ___102-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:fromMailboxIdentifier:completionHandler:]_block_invoke.30
- ___105-[DAKeyManagementSession hasUpgradeAvailableForKeyWithIdentifier:versionType:versions:completionHandler:]_block_invoke.34
- ___105-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.51
- ___107-[DAKeySharingSession sendSharingInvitationForKeyIdentifier:toIdsIdentifier:auth:config:completionHandler:]_block_invoke.13
- ___108-[DAKeyManagementSession upgradeKeyWithIdentifier:versionType:version:upgradeInformation:completionHandler:]_block_invoke.36
- ___108-[DAKeySharingSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.49
- ___108-[DAKeySharingSession setMailboxIdentifier:forOwnerKeyIdentifier:forInvitationIdentifier:completionHandler:]_block_invoke.28
- ___109-[DAKeySharingSession sendSilentSharingInvitationWithKeyIdentifier:config:groupIdentifier:completionHandler:]_block_invoke.15
- ___110-[DAKeySharingSession acceptSharingInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.22
- ___111-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.52
- ___113-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:]_block_invoke.39
- ___116-[DAKeySharingSession acceptCrossPlatformInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.33
- ___122-[DAKeyManagementSession revokeNodesWithGroupIdentifiers:treesWithGroupIdentifier:authorizedByKeyWithIdentifier:callback:]_block_invoke.33
- ___133-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:ourBindingAttestation:config:completionHandler:]_block_invoke.25
- ___23-[DASession endSession]_block_invoke.14
- ___35-[DAKeyPairingSession startProbing]_block_invoke
- ___35-[DAKeyPairingSession startProbing]_block_invoke.129
- ___35-[DAManager establishXpcConnection]_block_invoke.73
- ___35-[DAManager establishXpcConnection]_block_invoke.73.cold.1
- ___46-[DAKeyPairingSession preWarmForManufacturer:]_block_invoke.126
- ___46-[DAManager createPairingSessionWithDelegate:]_block_invoke.76
- ___46-[DAManager createSharingSessionWithDelegate:]_block_invoke.79
- ___47-[DAKeySharingSession cancelSharingInvitation:]_block_invoke.18
- ___49-[DAKeyPairingSession startKeyPairingWithConfig:]_block_invoke.127
- ___49-[DAManager createManagementSessionWithDelegate:]_block_invoke.82
- ___54-[DAKeyManagementSession deleteKey:completionHandler:]_block_invoke.15
- ___59-[DAKeyManagementSession localDeleteKey:completionHandler:]_block_invoke.22
- ___65-[DAKeySharingSession cancelSharingInvitation:completionHandler:]_block_invoke.21
- ___65-[DAKeySharingSession requestInviteWithConfig:completionHandler:]_block_invoke.24
- ___66-[DAKeyPairingSession handleProbingCompletionWithBrandCode:error:]_block_invoke
- ___69-[DAKeyManagementSession listReceivedSharingInvitationsWithCallback:]_block_invoke.21
- ___71-[DAKeySharingSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.47
- ___72-[DAKeySharingSession retryPasscode:forKeyIdentifier:completionHandler:]_block_invoke.40
- ___73-[DAKeyManagementSession cancelInvitationWithIdentifier:reason:callback:]_block_invoke.28
- ___74-[DAKeyManagementSession cancelAllFriendInvitationsWithCompletionHandler:]_block_invoke.23
- ___74-[DAKeyManagementSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.50
- ___74-[DAKeyManagementSession listSharingInvitationsForKeyIdentifier:callback:]_block_invoke.19
- ___74-[DAKeyManagementSession removeSharingInvitationWithId:completionHandler:]_block_invoke.24
- ___74-[DAKeySharingSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.54
- ___74-[DAKeySharingSession updateSharingAnalyticsWithConfig:completionHandler:]_block_invoke.41
- ___75-[DAKeySharingSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.44
- ___77-[DAKeyManagementSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.57
- ___78-[DAKeyManagementSession countImmobilizerTokensForKeyWithIdentifier:callback:]_block_invoke.25
- ___78-[DAKeyManagementSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.48
- ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.134
- ___79-[DAKeySharingSession retryPasscode:forInvitationIdentifier:completionHandler:]_block_invoke.39
- ___80-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.51
- ___80-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:]_block_invoke.29
- ___80-[DAManager handleSharingMessage:forInvitationIdentifier:fromMailboxIdentifier:]_block_invoke.84
- ___81-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.43
- ___81-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:completionHandler:]_block_invoke.34
- ___82-[DAKeySharingSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.42
- ___83-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.54
- ___83-[DAKeySharingSession authorizeSharingInvitationIdentifier:auth:completionHandler:]_block_invoke.17
- ___83-[DAKeySharingSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.52
- ___85-[DAKeyManagementSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.46
- ___85-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:completionHandler:]_block_invoke.45
- ___86-[DAKeyManagementSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.55
- ___86-[DAKeySharingSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.53
- ___87-[DAKeySharingSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.45
- ___88-[DAKeySharingSession handleInitiatorMessage:forInvitationIdentifier:completionHandler:]_block_invoke.37
- ___88-[DAKeySharingSession handleRecipientMessage:forInvitationIdentifier:completionHandler:]_block_invoke.35
- ___89-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.56
- ___90-[DAKeyManagementSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.49
- ___90-[DAKeyManagementSession removeSharedKeysWithIdentifiers:ownerKeyWithIdentifier:callback:]_block_invoke.30
- ___90-[DAKeySharingSession createSilentSharingInvitationWithGroupIdentifier:completionHandler:]_block_invoke.26
- ___92-[DAKeyManagementSession revokeKeysWithIdentifiers:sharedByOwnerKeyWithIdentifier:callback:]_block_invoke.31
- ___96-[DAKeySharingSession acceptSharingInvitation:fromMailboxIdentifier:passcode:completionHandler:]_block_invoke.31
- ___97-[DAKeyManagementSession cancelInvitationsWithIdentifiers:sentByOwnerKeyWithIdentifier:callback:]_block_invoke.27
- ___98-[DAKeyManagementSession commitUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.37
- ___98-[DAKeyManagementSession revertUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.38
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.28
- ___block_literal_global.358
- ___block_literal_global.426
- ___block_literal_global.86
- ___block_literal_global.88
- ___block_literal_global.90
- _decodeWithData:error:.allowedClasses.356
- _decodeWithData:error:.allowedClasses.424
- _decodeWithData:error:.pred.355
- _decodeWithData:error:.pred.423
- _objc_msgSend$appendU16BE:
- _objc_msgSend$didFinishProbingWithBrandCode:error:
- _objc_msgSend$initWithPassword:displayName:transport:bindingAttestation:ppid:btAddress:btIRK:additionalParameters:
- _objc_msgSend$startProbingWithCallback:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "\""
+ "%@:%@"
+ "%s : %i : %{public}@"
+ "%s : %i : :%{public}@"
+ "%s : %i : Cancel invite with id : %{public}@"
+ "%s : %i : Config:\n%@"
+ "%s : %i : DAAlishaKeyEncryptedRequest decodeWithData error: %{public}@"
+ "%s : %i : Invalid OP URL string: %{public}@"
+ "%s : %i : Invitation Id %{public}@"
+ "%s : %i : Invitation Identifier : %{public}@"
+ "%s : %i : InvitationId : %{public}@"
+ "%s : %i : InvitationIdentifier - %{public}@"
+ "%s : %i : KmlVersionOverride = %{public}@"
+ "%s : %i : Manufacturer: %{public}@"
+ "%s : %i : Missing default value for key: %@, assuming default is 0"
+ "%s : %i : No Data to initialize Mailbox mapping, using defaults"
+ "%s : %i : Null arguments provided. Session : %{public}@, seid : %@"
+ "%s : %i : Original key name: %@, truncated key name: %@"
+ "%s : %i : OwnerKeyIdentifier - %@, InvitationIdentifier - %{public}@"
+ "%s : %i : Requested Versions = { %{public}@ }"
+ "%s : %i : Result of decrypting vehicleMobilizationData: %{public}@"
+ "%s : %i : Result: %{public}@"
+ "%s : %i : SLG OVERRIDE FROM UD: %{public}@ = %d (was %d)"
+ "%s : %i : SLG OVERRIDE FROM UD: %{public}@ = %ld (was %ld)"
+ "%s : %i : This function is deprecated, please use either [DAKeySharingSession handleRecipientMessage] or [DAKeySharingSession handleInitiatorMessage] instead"
+ "%s : %i : Transport = %{public}@, displayName: %@"
+ "%s : %i : Vehicle never provided a supported versions list"
+ "%s : %i : XPC Proxy error %{public}@"
+ "%s : %i : brand: %{public}@"
+ "%s : %i : endPointPrivacyDecryption: return error: %{public}@"
+ "%s : %i : invitationIdentifier: %{public}@"
+ "%s : %i : json serialization error : %{public}@"
+ "%s : %i : keyRoleToShareOverride: %{public}@"
+ "%s : %i : length of : longTermSecret:%u; seed:%u; desiredPasscodeLength:%u"
+ "%s : %i : proxyError: %{public}@"
+ "%s : %i : transport: %{public}@ brand: %{public}@"
+ "&"
+ "&amp;"
+ "&apos;"
+ "&gt;"
+ "&lt;"
+ "&nbsp;"
+ "&quot;"
+ "'"
+ "(none)"
+ "+[DAAlishaKeyInformation withEndpoint:]"
+ "+[DAManager(PendingPairing) createPendingPairingForOPURLString:]"
+ ", "
+ "-[DAKeyPairingSession createPPIDRequestForConfig:completionHandler:]"
+ "-[DAKeyPairingSession createPPIDRequestForConfig:completionHandler:]_block_invoke"
+ "-[DAKeyPairingSession decryptPPIDResponse:completionHandler:]"
+ "-[DAKeyPairingSession decryptPPIDResponse:completionHandler:]_block_invoke"
+ "-[DAKeyPairingSession startProbingWithBrand:transport:]_block_invoke"
+ "-[DAManager(PendingPairing) createPendingPairingForManufacturer:brand:pairingPassword:supportedTransports:ppid:pti:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:]"
+ "-[DAManager(PendingPairing) createPendingPairingForManufacturer:brand:pairingPassword:supportedTransports:ppid:pti:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:]_block_invoke"
+ "-[DAManager(PendingPairing) createPendingPairingForOPURL:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:simulateBiomeEvent:]"
+ "-[DAManager(PendingPairing) createPendingPairingForOPURL:pairingPasswordExpiration:vehicleName:userNotificationDate:spotlightDomain:spotlightUniqueId:spotlightBundle:sourceReceivedDate:sourceLanguage:alreadyProvisioned:simulateBiomeEvent:]_block_invoke"
+ "-[DAManager(PendingPairing) forceMagicPairingEmailParsing]"
+ "-[DAManager(PendingPairing) forceMagicPairingEmailParsing]_block_invoke"
+ "-[DAManager(PendingPairing) listMagicPairingEligiblePendingPairingsForTransport:brand:completion:]"
+ "-[DAManager(PendingPairing) listMagicPairingEligiblePendingPairingsForTransport:brand:completion:]_block_invoke"
+ "-[DAManager(PendingPairing) listNfcMagicPairingEligiblePendingPairingsWithBrand:completion:]"
+ "-[DAManager(PendingPairing) listNfcMagicPairingEligiblePendingPairingsWithBrand:completion:]_block_invoke"
+ "-[DAManager(PendingPairing) listPendingPairingObjectsWithCompletion:]"
+ "-[DAManager(PendingPairing) listPendingPairingObjectsWithCompletion:]_block_invoke"
+ "-[DAManager(PendingPairing) registerMagicPairingResumeProvisioningsHandler:]"
+ "-[DAManager(PendingPairing) registerMagicPairingResumeProvisioningsHandler:]_block_invoke"
+ "-[DAManager(PendingPairing) registerPendingProvisioningCreationHandler:]"
+ "-[DAManager(PendingPairing) registerPendingProvisioningCreationHandler:]_block_invoke"
+ "-[DAManager(PendingPairing) registerPendingProvisioningRemovalHandler:]"
+ "-[DAManager(PendingPairing) registerPendingProvisioningRemovalHandler:]_block_invoke"
+ "-[DAManager(PendingPairing) removePendingPairingWithIdentifier:]"
+ "-[DAManager(PendingPairing) removePendingPairingWithIdentifier:]_block_invoke"
+ "-[DAManager(PendingPairing) setUserConsentForPendingPairingIdentifier:]"
+ "-[DAManager(PendingPairing) setUserConsentForPendingPairingIdentifier:]_block_invoke"
+ "-[DAManager(PendingPairing) triggerMagicPairingDetection:]"
+ "-[DAManager(PendingPairing) triggerMagicPairingDetection:]_block_invoke"
+ "-[DAManager(PendingPairing) unregisterOwnerPairingTestHandlers]"
+ "-[DAManager(PendingPairing) unregisterOwnerPairingTestHandlers]_block_invoke"
+ "-[KmlSettingsManager boolValueForSetting:manufacturer:brand:uuid:error:]"
+ "-[KmlSettingsManager defaultIntValueForSetting:]"
+ "-[KmlSettingsManager intValueForSetting:manufacturer:brand:uuid:error:]"
+ "<"
+ ">"
+ "BT "
+ "Binding Attestation Length         : %d\n"
+ "Brand                              : %@\n"
+ "Brand                            : %@\n"
+ "Brand                       : %@\n"
+ "Brand Code                         : 0x%04lX\n"
+ "Brand code mismatch during pairing"
+ "Connected Timeout Requested : %@\n"
+ "Creation Date                      : %@\n"
+ "Display Name                       : %@\n"
+ "Expiration Date                    : %@\n"
+ "Failed to get preTrack data"
+ "Magic Pairing Attempts             : %ld\n"
+ "Manufacturer                       : %@\n"
+ "Manufacturer                     : %@\n"
+ "Max magic pairing attempts reached for pending pairing"
+ "NFC "
+ "Not eligible for magic pairing, but saved pending pairing info"
+ "OPProbingTimeout"
+ "OPUserInitiatedVehicleConnectionTimeout"
+ "OPVehicleConnectionTimeout"
+ "OPVehicleDetectionTimeout"
+ "Owner Pairing Token Length       : %d\n"
+ "PPID                               : %@\n"
+ "PTI                                : %@\n"
+ "Pairing config is for a different vehicle"
+ "PairingDataExtractionBlockedLanguages"
+ "Password Attempts                  : %ld\n"
+ "Pending Pairing Identifier         : %@\n"
+ "Pending Pairing Identifier  : %@\n"
+ "Pending Pairing is invalid"
+ "Preconditions Satisfied"
+ "Ready for Cleanup"
+ "Region                           : %@\n"
+ "Saved preconditions for magic pairing"
+ "State                              : %@\n"
+ "Supported Transports               : %@\n"
+ "Uninitialized"
+ "Unknown (%ld)"
+ "User Consent Received              : %@\n"
+ "User Notification Date             : %@\n"
+ "Vehicle Discriminator Length     : %d\n"
+ "Vehicle Identifier               : %@\n"
+ "Vehicle Name                       : %@"
+ "Waiting for Preconditions"
+ "Waiting for Right Time"
+ "brandCode"
+ "creationDate"
+ "debug.IgnoreGlobalPairingDataExtractionLanguageDenylist"
+ "debug.IgnorePendingPairingRateLimit"
+ "debug.IgnoreProcessedSpotlightIdCheck"
+ "debug.magicPairingCooldownDuration"
+ "debug.magicPairingMaxSourceAgeDays"
+ "debug.magicPairingPostProvisioningCooldownDays"
+ "debug.pendingPairingNotificationSchedulingStrategy"
+ "debug.slgOverride.BuildNonOSPPreShareTlv"
+ "debug.slgOverride.BuildOPPreTrackRequest"
+ "debug.slgOverride.DisableNFCOnlyDevice"
+ "debug.slgOverride.DowngradePairingVersion"
+ "debug.slgOverride.EnableSharingFromWatch"
+ "debug.slgOverride.IgnoreExtractedPairingData"
+ "debug.slgOverride.IgnoreMagicPairingPostProvisioningCooldown"
+ "debug.slgOverride.KeyUpgradeEnabledForFriendKey"
+ "debug.slgOverride.KeyUpgradeEnabledForOwnerKey"
+ "debug.slgOverride.MagicPairingBluetooth"
+ "debug.slgOverride.MagicPairingNFC"
+ "debug.slgOverride.Pairing"
+ "debug.slgOverride.RKE"
+ "debug.slgOverride.RSSIPairing"
+ "debug.slgOverride.SendDeviceDiscriminator"
+ "debug.slgOverride.UWB"
+ "didReceiveUserConsent"
+ "enableConnectionTimeout"
+ "expirationDate"
+ "i"
+ "isUserInitiated"
+ "numMagicPairingAttempts"
+ "numPasswordAttempts"
+ "ownerPairingToken"
+ "pairingState"
+ "pending:"
+ "pendingPairingIdentifier"
+ "pti"
+ "region"
+ "userNotificationDate"
+ "v16@?0@\"NSString\"8"
+ "v24@?0@\"NSError\"8@\"NSArray\"16"
+ "vehicleDiscriminator"
+ "vehicleIdentifier"
+ "vehicleName"
- "#16@0:8"
- "%s : %i : :%@"
- "%s : %i : Cancel invite with id : %@"
- "%s : %i : Invitation Id %@"
- "%s : %i : Invitation Identifier : %@"
- "%s : %i : InvitationId : %@"
- "%s : %i : InvitationIdentifier - %@"
- "%s : %i : KmlVersionOverride = %@"
- "%s : %i : Manufacturer: %@"
- "%s : %i : No Data to initalize Mailbox mapping, using defaults"
- "%s : %i : Null arguments provided. Session : %@, seid : %@"
- "%s : %i : Original key name: %@ ,  truncated key name: %@"
- "%s : %i : OwnerKeyIdentifier - %@, InvitationIdentifier - %@"
- "%s : %i : Requested Versions = { %@ }"
- "%s : %i : Result of decrypting vehicleMobilizationData: %@"
- "%s : %i : This function is deprecated, please use either [DAKeySharingSession handleRecipientMessage] or [DAKeySharingSession handleInititiatorMessage] instead"
- "%s : %i : Transport = %@, displayName: %@"
- "%s : %i : Vehicle never provided a supported versiosn list"
- "%s : %i : XPC Proxy error %@"
- "%s : %i : endPointPrivacyDecryption: return error: %@"
- "%s : %i : invitationIdentifier: %@"
- "%s : %i : json serialization error : %@"
- "%s : %i : keyRoleToShareOverride: %@"
- "%s : %i : length of : longTermSecret:%u; seed:%u; desiredPasscode:%u"
- "%s : %i : proxyError: %@"
- "-[DAKeyPairingSession startProbing]_block_invoke"
- ".cxx_destruct"
- "@"
- "@\"DAAlishaKeyEncryptedRequest\""
- "@\"DAAlishaKeyInformation\""
- "@\"DACarKeyAdditionalCrossPlatformSharingData\""
- "@\"DACarKeyGenericCrossPlatformSharingData\""
- "@\"DACarKeyPrivateCrossPlatformSharingData\""
- "@\"DACarKeySharingMessage\""
- "@\"DAHomeKeyInformation\""
- "@\"DAHydraKeyInformation\""
- "@\"DAKeyInformation\""
- "@\"DAKeySharingAnalyticsData\""
- "@\"DASessionInternal\""
- "@\"KmlTlv\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSError\"32@0:8@\"NSData\"16@\"NSString\"24"
- "@\"NSError\"40@0:8@\"NSData\"16@\"DAAlishaKeyEncryptedRequest\"24@\"NSString\"32"
- "@\"NSError\"40@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32"
- "@\"NSError\"56@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSString\"48"
- "@\"NSMutableArray\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<NSXPCProxyCreating>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSUserDefaults\""
- "@\"NSXPCConnection\""
- "@\"SEEndPoint\""
- "@\"SESConfigDCK\""
- "@16@0:8"
- "@20@0:8C16"
- "@20@0:8I16"
- "@20@0:8S16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8S16C20"
- "@24@0:8S16I20"
- "@24@0:8S16S20"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8@16S24"
- "@28@0:8S16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24q32"
- "@44@0:8@16@24B32@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16@24q32@40"
- "@48@0:8Q16@24@32q40"
- "@48@0:8{_DAVersionUpgrade=QBQQ}16"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@40^@48"
- "@64@0:8@16@24@32@40@48^@56"
- "@64@0:8@16@24@32C40@44C52@56"
- "@64@0:8@16@24@32q40q48@56"
- "@76@0:8Q16@24@32q40B48Q52@60@68"
- "@80@0:8@16@24q32@40@48@56@64@72"
- "AliroKey"
- "B"
- "B16@0:8"
- "B20@0:8C16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8S16S20"
- "B28@0:8S16q20"
- "B32@0:8@16^@24"
- "B48@0:8@16@24@32^@40"
- "B56@0:8@16@24@32@40^@48"
- "B56@0:8Q16@24@32@40^@48"
- "BT Address                  : %@\n"
- "BT IRK Length               : %lu\n"
- "BluetoothHceSessionTimeLimit"
- "BluetoothLoyaltyAndPaymentSessionTimeLimit"
- "C16@0:8"
- "DAAdditionalConfigurationData"
- "DAAlishaKeyEncryptedRequest"
- "DAAlishaKeyEncryptedRequest decodeWithData error: %@"
- "DAAlishaKeyInformation"
- "DAAvailableVersionUpgrade"
- "DACarKeyAdditionalCrossPlatformSharingData"
- "DACarKeyGenericCrossPlatformSharingData"
- "DACarKeyPrivateCrossPlatformSharingData"
- "DACarKeySharingMessage"
- "DAHomeKeyInformation"
- "DAHydraKeyInformation"
- "DAKeyBindingAttestationRequestData"
- "DAKeyInformation"
- "DAKeyInvitationRequestConfig"
- "DAKeyManagementSession"
- "DAKeyPairingConfig"
- "DAKeyPairingSession"
- "DAKeyPreTrackDataUpdate"
- "DAKeySharing2FAConfiguration"
- "DAKeySharingAnalyticsData"
- "DAKeySharingConfiguration"
- "DAKeySharingInvitationData"
- "DAKeySharingSession"
- "DAKeyTrackingUpdate"
- "DAManager"
- "DASession"
- "DASessionInternal"
- "DAShareInitiatorResult"
- "DAShareRecipientResult"
- "DASharingAnalyticsUpdateConfig"
- "DASharingSecondFactorRequestConfiguration"
- "DAUtils"
- "HydraKey"
- "I"
- "I16@0:8"
- "JSONObjectWithData:options:error:"
- "KmlCancelMessage"
- "KmlDeviceConfigurationData"
- "KmlKeyManagementInterface"
- "KmlKeyManagementProtocol"
- "KmlKeySharingProtocol"
- "KmlKeyTrackingReceiptUpdateProtocol"
- "KmlMailboxMappingData"
- "KmlManagerCallbacks"
- "KmlManagerInterface"
- "KmlManagerProtocol"
- "KmlOwnerPairingCallbacks"
- "KmlOwnerPairingProtocol"
- "KmlPreTrackDataUpdateProtocol"
- "KmlSessionCallbacks"
- "KmlSessionProtocol"
- "KmlSettingsManager"
- "KmlTlv"
- "KmlVersionOverride"
- "KmlVersions"
- "NFCHceSessionTimeLimit"
- "NFCLoyaltyAndPaymentSessionTimeLimit"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "S16@0:8"
- "T#,R"
- "T@\"DAAlishaKeyEncryptedRequest\",R,N,V_trackingRequest"
- "T@\"DAAlishaKeyInformation\",R,N,V_alishaKeyInformation"
- "T@\"DACarKeyAdditionalCrossPlatformSharingData\",R,N,V_additionalData"
- "T@\"DACarKeyGenericCrossPlatformSharingData\",R,N,V_genericData"
- "T@\"DACarKeyPrivateCrossPlatformSharingData\",R,N,V_privateData"
- "T@\"DACarKeySharingMessage\",R,N,V_response"
- "T@\"DAHomeKeyInformation\",R,N,V_homeKeyInformation"
- "T@\"DAHydraKeyInformation\",R,N,V_hydraKeyInformation"
- "T@\"DAKeyInformation\",R,N,V_keyInformation"
- "T@\"DAKeySharingAnalyticsData\",R,N,V_analyticsData"
- "T@\"KmlTlv\",R,N"
- "T@\"NSArray\",R,N,V_invitationIdentifiers"
- "T@\"NSArray\",R,N,V_secondFactorList"
- "T@\"NSArray\",R,N,V_supportedTransports"
- "T@\"NSArray\",R,V_certificateChain"
- "T@\"NSData\",&,N,V_additionalMailboxSettingAsData"
- "T@\"NSData\",&,N,V_bindingAttestation"
- "T@\"NSData\",&,N,V_confMailboxSettingAsData"
- "T@\"NSData\",&,N,V_deviceBtIntroKey"
- "T@\"NSData\",&,N,V_deviceBtOOBKey"
- "T@\"NSData\",&,N,V_initiatorSupportedFrameworkVersionsData"
- "T@\"NSData\",&,N,V_metaData"
- "T@\"NSData\",&,N,V_mfiPPID"
- "T@\"NSData\",&,N,V_oemSpecificContentAsData"
- "T@\"NSData\",&,N,V_onlineBleOOBMasterKeyOverride"
- "T@\"NSData\",&,N,V_privateMailboxSettingAsData"
- "T@\"NSData\",&,N,V_readerBtIRK"
- "T@\"NSData\",&,N,V_readerBtIdAddress"
- "T@\"NSData\",&,N,V_sharingPasswordLengthAsData"
- "T@\"NSData\",&,N,V_supportedKeyProfiles"
- "T@\"NSData\",&,N,V_v3ConfMailboxSettingAsData"
- "T@\"NSData\",&,N,V_v3PrivateMailboxSettingAsData"
- "T@\"NSData\",&,N,V_vehicleSupportedFrameworkVersionsData"
- "T@\"NSData\",R,N"
- "T@\"NSData\",R,N,V_bindingAttestation"
- "T@\"NSData\",R,N,V_casd"
- "T@\"NSData\",R,N,V_encryptedRequest"
- "T@\"NSData\",R,N,V_ephemeralPublicKey"
- "T@\"NSData\",R,N,V_message"
- "T@\"NSData\",R,N,V_publicKeyHash"
- "T@\"NSData\",R,N,V_revocationAttestation"
- "T@\"NSData\",R,N,V_rsaCertData"
- "T@\"NSData\",R,N,V_subCaAttestation"
- "T@\"NSData\",R,N,V_trackingReceipt"
- "T@\"NSData\",R,V_appletIdentifier"
- "T@\"NSData\",R,V_publicKey"
- "T@\"NSData\",R,V_readerIdentifier"
- "T@\"NSDictionary\",R,N,V_additionalParameters"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSNumber\",R,N,V_keyRole"
- "T@\"NSString\",&,N,V_deviceEnteredPasscode"
- "T@\"NSString\",&,N,V_displayName"
- "T@\"NSString\",&,N,V_proprietaryEntitlements"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_btAddress"
- "T@\"NSString\",R,N,V_btIRK"
- "T@\"NSString\",R,N,V_credentialIdentifier"
- "T@\"NSString\",R,N,V_displayName"
- "T@\"NSString\",R,N,V_friendKeyIdentifier"
- "T@\"NSString\",R,N,V_initiatorIdsPseudonym"
- "T@\"NSString\",R,N,V_invitationIdentifier"
- "T@\"NSString\",R,N,V_keyIdentifier"
- "T@\"NSString\",R,N,V_localIdentifier"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_ownerIDSIdentifier"
- "T@\"NSString\",R,N,V_ownerIdsIdentifier"
- "T@\"NSString\",R,N,V_pairedEntityIdentifier"
- "T@\"NSString\",R,N,V_passcode"
- "T@\"NSString\",R,N,V_password"
- "T@\"NSString\",R,N,V_ppid"
- "T@\"NSString\",R,N,V_publicKeyIdentifier"
- "T@\"NSString\",R,N,V_sharingIdentifier"
- "T@\"NSString\",R,N,V_vehicleEnteredPasscode"
- "T@\"NSString\",R,N,V_vehicleSupportedFrameworkVersionsForCA"
- "T@\"NSString\",R,N,V_version"
- "T@\"NSUUID\",R,N,V_sharingSessionIdentifier"
- "T@\"NSUUID\",R,N,V_sharingSessionUUID"
- "T@,&,SsetProxy:"
- "T@,R,W,V_delegate"
- "TB,N,V_carSupportsUpdateAttestation"
- "TB,N,V_didParseDataSuccessfully"
- "TB,N,V_enableVehicleEnteredPasscode"
- "TB,N,V_keyTrackingReceiptRequired"
- "TB,N,V_mockRefreshInstanceCA"
- "TB,N,V_onlineAttestationDeliverySupported"
- "TB,N,V_readerSupportsLELR"
- "TB,N,V_readerSupportsNfc"
- "TB,N,V_readerSupportsUwb"
- "TB,N,V_sharingPasswordRequired"
- "TB,N,V_uwbDisabledLocally"
- "TB,R"
- "TB,R,N,V_fleetVehicle"
- "TB,R,N,V_onlineImmobilizerToken"
- "TB,R,N,V_recipientFlow"
- "TB,R,N,V_serverIssued"
- "TB,R,N,V_vehicleSupportsSharingPassword"
- "TB,V_isFirstInQueue"
- "TC,N,V_cccCode"
- "TC,N,V_immoTokenConfig"
- "TC,N,V_maxOfflineAttestationCount"
- "TC,N,V_sharingPasswordLength"
- "TC,R,N,V_immoTokenLength"
- "TC,R,N,V_mailboxVersion"
- "TC,R,N,V_slotIdentifierLength"
- "TI,N,V_kmlCode"
- "TLVWithJustTag:"
- "TLVWithTag:unsignedChar:"
- "TLVWithTag:unsignedLongValue:"
- "TLVWithTag:unsignedShort:"
- "TLVWithTag:value:"
- "TLVsWithData:"
- "TQ,N,V_keyRole"
- "TQ,N,V_maxRetriesForDeviceEnteredPasscode"
- "TQ,N,V_profile"
- "TQ,R"
- "TQ,R,N,V_agreedAppletVersion"
- "TQ,R,N,V_agreedFrameworkVersion"
- "TQ,R,N,V_agreedVehicleServerVersion"
- "TQ,R,N,V_longTermSharedSecretLength"
- "TQ,R,N,V_maxRetriesAllowed"
- "TQ,R,N,V_retryCount"
- "TQ,R,N,V_type"
- "TS,N,V_keyRoleToShare"
- "TS,N,V_kmlOverrideVersion"
- "TS,R,N"
- "TS,R,N,V_agreedKmlSharingVersion"
- "TS,R,N,V_attestationPackageLength"
- "TS,R,N,V_keyAttestationStartOffset"
- "TS,R,N,V_keyRoleToShare"
- "TS,R,N,V_mailboxEndOffset"
- "TS,R,N,V_ourPreferredKmlVersion"
- "TS,R,N,V_ourPreferredVehicleServerVersion"
- "TS,R,N,V_signalingBitmapOffset"
- "TS,R,N,V_signerSlotIdListOffset"
- "TS,R,N,V_slotIdBitmapOffset"
- "TS,R,N,V_slotIdListOffset"
- "TS,R,N,V_vehicleProprietaryDataOffset"
- "Tq,N,V_targetDeviceType"
- "Tq,R,N,V_invitationState"
- "Tq,R,N,V_keyType"
- "Tq,R,N,V_messageType"
- "Tq,R,N,V_sharingFlow"
- "Tq,R,N,V_sharingTargetType"
- "Tq,R,N,V_targetDeviceType"
- "Tq,R,N,V_transport"
- "T{_DAVersionUpgrade=QBQQ},R"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?@\"DAKeyInformation\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSData\"@\"NSString\">16"
- "Vv24@0:8@?<v@?@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSString\"@\"NSUUID\"@\"NSData\">16"
- "Vv24@0:8@?<v@?@\"NSString\"Q>16"
- "Vv24@0:8@?<v@?@\"NSUUID\"@\"NSString\"@\"NSString\">16"
- "Vv24@0:8@?<v@?B>16"
- "Vv32@0:8@\"DACarKeySharingMessage\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"DAKeyInvitationRequestConfig\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"DAKeyPairingConfig\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"DASharingAnalyticsUpdateConfig\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "Vv32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\">24"
- "Vv32@0:8@\"NSData\"16@\"NSString\"24"
- "Vv32@0:8@\"NSObject<KmlOwnerPairingCallbacks>\"16@?<v@?@\"NSObject<KmlOwnerPairingProtocol>\"B@\"NSError\">24"
- "Vv32@0:8@\"NSObject<KmlSessionCallbacks>\"16@?<v@?@\"NSObject<KmlKeyManagementProtocol>\"B@\"NSError\">24"
- "Vv32@0:8@\"NSObject<KmlSessionCallbacks>\"16@?<v@?@\"NSObject<KmlKeySharingProtocol>\"B@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"DAAlishaKeyEncryptedRequest\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"DAKeyBindingAttestationRequestData\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"DAShareRecipientResult\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?QQ>24"
- "Vv32@0:8@\"NSUUID\"16@?<v@?@\"DACarKeySharingMessage\"@\"NSError\">24"
- "Vv32@0:8@16@24"
- "Vv32@0:8@16@?24"
- "Vv40@0:8@\"DAAlishaKeyEncryptedRequest\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"DACarKeySharingMessage\"16@\"NSString\"24@?<v@?@\"DAShareInitiatorResult\">32"
- "Vv40@0:8@\"DACarKeySharingMessage\"16@\"NSString\"24@?<v@?@\"DAShareRecipientResult\">32"
- "Vv40@0:8@\"DACarKeySharingMessage\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"DAAlishaKeyEncryptedRequest\"@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"DACarKeySharingMessage\"@\"DAKeyInformation\"@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16Q24@?<v@?@\"DACarKeySharingMessage\"@\"NSError\">32"
- "Vv40@0:8@16@24@?32"
- "Vv40@0:8@16Q24@?32"
- "Vv48@0:8@\"DACarKeySharingMessage\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"NSData\"16@\"NSString\"24@\"DAAdditionalConfigurationData\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16@\"DAKeySharingConfiguration\"24@\"NSUUID\"32@?<v@?@\"DAKeySharingInvitationData\"@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"DAAlishaKeyEncryptedRequest\"32@?<v@?@\"DAKeyInformation\"@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16Q24@\"NSArray\"32@?<v@?@\"NSValue\"@\"NSError\">40"
- "Vv48@0:8@16@24@32@?40"
- "Vv48@0:8@16Q24@32@?40"
- "Vv52@0:8@\"NSString\"16Q24Q32B40@?<v@?@\"NSError\">44"
- "Vv52@0:8@16Q24Q32B40@?44"
- "Vv56@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@\"NSString\"40@?<v@?@\"DAAlishaKeyEncryptedRequest\"@\"NSError\">48"
- "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@\"NSArray\"40@?<v@?@\"NSArray\"@\"NSError\">48"
- "Vv56@0:8@\"NSString\"16Q24Q32@\"NSData\"40@?<v@?@\"NSError\">48"
- "Vv56@0:8@16@24@32@40@?48"
- "Vv56@0:8@16Q24Q32@40@?48"
- "Vv64@0:8@\"DACarKeySharingMessage\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"DAAlishaKeyEncryptedRequest\"48@?<v@?@\"DACarKeySharingMessage\"@\"DAKeyInformation\"@\"NSError\">56"
- "Vv64@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@\"NSData\"40@\"NSArray\"48@?<v@?@\"NSArray\"@\"NSError\">56"
- "Vv64@0:8@16@24@32@40@48@?56"
- "^{_NSZone=}16@0:8"
- "_activeSessions"
- "_additionalData"
- "_additionalMailboxSettingAsData"
- "_additionalParameters"
- "_agreedAppletVehicleVersion"
- "_agreedAppletVersion"
- "_agreedFrameworkVersion"
- "_agreedKmlBluetoothVersion"
- "_agreedKmlSharingVersion"
- "_agreedKmlVehicleServerVersion"
- "_agreedKmlVehicleVersion"
- "_agreedVehicleServerVersion"
- "_alishaKeyInformation"
- "_allMailboxMappingTlvs"
- "_analyticsData"
- "_appletIdentifier"
- "_appletSupportedVersionsList"
- "_appletSupportedVersionsTlvForPairing"
- "_attestationPackageLength"
- "_bindingAttestation"
- "_btAddress"
- "_btIRK"
- "_callbackQueue"
- "_carSupportsUpdateAttestation"
- "_casd"
- "_cccCode"
- "_certificateChain"
- "_clientConnection"
- "_confMailboxSettingAsData"
- "_credentialIdentifier"
- "_dckConfig"
- "_defaultSLGValues"
- "_delegate"
- "_deviceBtIntroKey"
- "_deviceBtOOBKey"
- "_deviceEnteredPasscode"
- "_didParseDataSuccessfully"
- "_displayName"
- "_downgradeFrameworkVersion"
- "_enableVehicleEnteredPasscode"
- "_encryptedRequest"
- "_endpoint"
- "_ephemeralPublicKey"
- "_error"
- "_fleetVehicle"
- "_friendKeyIdentifier"
- "_genericData"
- "_hasEnded"
- "_homeKeyInformation"
- "_hydraKeyInformation"
- "_immoTokenConfig"
- "_immoTokenLength"
- "_initiatorIdsPseudonym"
- "_initiatorSupportedFrameworkVersionsData"
- "_internal"
- "_invitationIdentifier"
- "_invitationIdentifiers"
- "_invitationState"
- "_isCallbackQueueSuspended"
- "_isFirstInQueue"
- "_keyAttestationListStartOffset"
- "_keyAttestationStartOffset"
- "_keyIdentifier"
- "_keyInformation"
- "_keyRole"
- "_keyRoleToShare"
- "_keyTrackingReceiptRequired"
- "_keyType"
- "_kmlCode"
- "_kmlOverrideVersion"
- "_kmlSupportedVehicleServerVersionsList"
- "_kmlSupportedVersionsList"
- "_kmlSupportedVersionsTlvForPairing"
- "_kmlSupportedVersionsTlvForShareInitiator"
- "_kmlUpgradeReadyVersionsList"
- "_localIdentifier"
- "_longTermSharedSecretLength"
- "_mailboxEndOffset"
- "_mailboxVersion"
- "_maxOfflineAttestationCount"
- "_maxRetriesAllowed"
- "_maxRetriesForDeviceEnteredPasscode"
- "_message"
- "_messageType"
- "_metaData"
- "_mfiPPID"
- "_mockRefreshInstanceCA"
- "_name"
- "_oemSpecificContentAsData"
- "_onlineAttestationDeliverySupported"
- "_onlineBleOOBMasterKeyOverride"
- "_onlineImmobilizerToken"
- "_ourPreferredKmlVersion"
- "_ourPreferredVehicleServerVersion"
- "_ownerIDSIdentifier"
- "_ownerIdsIdentifier"
- "_pairedEntityIdentifier"
- "_passcode"
- "_password"
- "_ppid"
- "_preferredVersion"
- "_preferredVersionTlvs"
- "_privateData"
- "_privateMailboxSettingAsData"
- "_profile"
- "_proprietaryEntitlements"
- "_proxy"
- "_publicKey"
- "_publicKeyHash"
- "_publicKeyIdentifier"
- "_readerBtIRK"
- "_readerBtIdAddress"
- "_readerIdentifier"
- "_readerSupportsLELR"
- "_readerSupportsNfc"
- "_readerSupportsUwb"
- "_recipientFlow"
- "_remainingTlvs"
- "_response"
- "_retryCount"
- "_revocationAttestation"
- "_rsaCertData"
- "_secondFactorList"
- "_serverIssued"
- "_serviceName"
- "_sharingConfigTagParsed"
- "_sharingFlow"
- "_sharingIdentifier"
- "_sharingPasswordLength"
- "_sharingPasswordLengthAsData"
- "_sharingPasswordRequired"
- "_sharingSessionIdentifier"
- "_sharingSessionUUID"
- "_sharingTargetType"
- "_signalingBitmapOffset"
- "_signerSlotIdListOffset"
- "_slotIdBitmapOffset"
- "_slotIdListOffset"
- "_slotIdentifierLength"
- "_stockholmUserDefaults"
- "_subCaAttestation"
- "_supportedKeyProfiles"
- "_supportedRadioTagParsed"
- "_supportedTransports"
- "_tag"
- "_targetDeviceType"
- "_trackingReceipt"
- "_trackingRequest"
- "_transport"
- "_type"
- "_upgradeEnabledForFriendKey"
- "_upgradeEnabledForOwnerKey"
- "_useOldSignalingBitmap"
- "_userDefaults"
- "_uwbDisabledLocally"
- "_v3ConfMailboxSettingAsData"
- "_v3PrivateMailboxSettingAsData"
- "_value"
- "_vehicleEnteredPasscode"
- "_vehicleProprietaryDataOffset"
- "_vehicleProprietaryDataOffset_v3"
- "_vehicleServerVersionsUpgradeReadyList"
- "_vehicleSupportedAppletVersionsTlvAsData"
- "_vehicleSupportedBluetoothVersionsTlvAsData"
- "_vehicleSupportedFrameworkVersionsData"
- "_vehicleSupportedFrameworkVersionsForCA"
- "_vehicleSupportedFrameworkVersionsTlvAsData"
- "_vehicleSupportsSharingPassword"
- "_version"
- "acceptCrossPlatformInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:"
- "acceptInvitationWithIdentifier:passcode:completionHandler:"
- "acceptSharingInvitation:fromMailboxIdentifier:completionHandler:"
- "acceptSharingInvitation:fromMailboxIdentifier:passcode:completionHandler:"
- "acceptSharingInvitation:withIdentifier:fromMailboxIdentifier:passcode:productPlanIdentifier:completionHandler:"
- "acceptSharingInvitationWithIdentifier:completionHandler:"
- "acceptSharingInvitationWithIdentifier:passcode:completionHandler:"
- "acceptSharingInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:"
- "addObject:"
- "addObjectsFromArray:"
- "additionalMailboxSettingAsData"
- "agreedAppletVehicleVersion"
- "agreedKmlBluetoothVersion"
- "agreedKmlSharingVersion"
- "agreedKmlVehicleServerVersion"
- "agreedKmlVehicleVersion"
- "alishaKeyWithPublicKeyIdentifier:alishaKeyInformation:"
- "allKeys"
- "allocWithZone:"
- "allowFleetOwnerPairing"
- "allowRadioMismatchForTest"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "appendU16BE:"
- "appletSupportedVersionsTlvForPairing"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "asData"
- "asDictionary"
- "attestationPackageLength"
- "authorizeSharingInvitationIdentifier:auth:completionHandler:"
- "autorelease"
- "availableVersionUpgradeValue"
- "boolValue"
- "boolValueForSetting:manufacturer:brand:uuid:error:"
- "boolValueForUserDefault:"
- "btAddress"
- "btIRK"
- "buildNonOSPPreShareTlvOverride"
- "bypassAccountInfoHash"
- "bytes"
- "cancelAllFriendInvitationsWithCompletionHandler:"
- "cancelInvitationWithIdentifier:reason:callback:"
- "cancelInvitationsWithIdentifiers:sentByOwnerKeyWithIdentifier:callback:"
- "cancelSharingInvitation:"
- "cancelSharingInvitation:completionHandler:"
- "carSupportsUpdateAttestation"
- "casdECDSACertificate"
- "casdRSACertificate"
- "cccCode"
- "certificates"
- "characterAtIndex:"
- "class"
- "closeProxy"
- "code"
- "commitUpgradeForKeyWithIdentifier:versionType:version:completionHandler:"
- "confMailboxSettingAsData"
- "configuration"
- "conformsToProtocol:"
- "connection"
- "consumeTrackingReceipt:otherJSONData:forKeyWithIdentifier:callback:"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countImmobilizerTokensForKeyWithIdentifier:callback:"
- "createAliroHomeKey:seid:readerIdentifier:readerPublicKey:homeUUID:outError:"
- "createAliroHydraKey:seid:serverParameters:outError:"
- "createHomeKey:seid:readerIdentifier:readerPublicKey:outError:"
- "createHydraKey:seid:serverParameters:outError:"
- "createManagementSessionWithDelegate:"
- "createPairingSessionWithDelegate:"
- "createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:config:completionHandler:"
- "createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:ourBindingAttestation:config:completionHandler:"
- "createSharingSessionWithDelegate:"
- "createSilentSharingInvitationWithGroupIdentifier:completionHandler:"
- "d16@0:8"
- "d48@0:8@16d24d32d40"
- "daSession:didBecomeActive:"
- "daSession:didEnd:"
- "data"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithCapacity:"
- "dataWithLength:"
- "date"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "debug.BuildNonOSPPreShareTlvOverride"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodeWithData:error:"
- "decryptVehicleMobilizationData:forKeyWithIdentifier:"
- "defaultBoolValueForSetting:"
- "delegate"
- "deleteKey:callback:"
- "deleteKey:completionHandler:"
- "description"
- "deviceBtIntroKey"
- "deviceBtOOBKey"
- "deviceConfiguration"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "didEnd:"
- "didFinishFirstTransactionForSession:error:"
- "didFinishPreWarmWithResult:"
- "didFinishProbingWithBrandCode:error:"
- "didParseDataSuccessfully"
- "didStart:"
- "didStartPairing"
- "disableFleetKeyStrictShareInitCertChainValidation"
- "disablePrivateKeyStrictShareInitCertChainValidation"
- "dispatchBlockOnCallback:"
- "dispatchOnCallbackQueue:"
- "doesAgreedVersionSupportOnlineBleKeys"
- "doesVersion:support:"
- "domain"
- "doubleForKey:"
- "downgradePreferredVersion"
- "emulateNFCOnlyDevice"
- "encodeBool:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodeWithError:"
- "endPointPrivacyDecryption:encryptedData:publicKey:callback:"
- "endPointType"
- "endSession"
- "endSessionWithCompletion:"
- "enumerateObjectsUsingBlock:"
- "enumerateSubstringsInRange:options:usingBlock:"
- "errorWithDomain:code:userInfo:"
- "finalizeUpgradeForKeyWithIdentifier:versionType:version:revert:completionHandler:"
- "firstObject"
- "fleetManufacturerAllowListWithError:"
- "fleetServiceProviderAllowListWithError:"
- "fleetVehicle"
- "friendlyName"
- "getAgreedBluetoothVersionsTlv"
- "getAliroSupportedProtocolVersions:"
- "getDelegate"
- "getHydraEncryptionCert:session:seid:outError:"
- "getKmlSupportedVersionsTlvAsShareRecipient"
- "getMaskToIndicateKeyAttestationConsumed"
- "getMaskToIndicateKeyAttestationSaved"
- "getMaskToIndicateOemPropDataConsumed"
- "getMaskToIndicateOemPropDataSaved"
- "getMaskToIndicateSlotIdListConsumed"
- "getMaskToIndicateSlotIdListSaved"
- "getPreTrackRequestForInvitationWithIdentifier:completionHandler:"
- "getPreTrackRequestForKeyWithIdentifier:callback:"
- "getRemoteProxy:"
- "getRootCertificateFor:keyID:error:"
- "getRootCertificateFor:keyId:"
- "getSecondFactorRequestForConfigs:completionHandler:"
- "getSettingForKey:error:"
- "getUUIDBytes:"
- "getValue:size:"
- "getVehicleSupportedVersionsData"
- "handleActivationForKeyWithIdentifier:callback:"
- "handleFirstTransactionCompletionResult:"
- "handleInitiatorMessage:forInvitationIdentifier:completionHandler:"
- "handleKeyPairingCompletionResult:keyInformation:trackingRequest:"
- "handlePairingDidStart"
- "handlePreWarmCompletionResult:"
- "handleProbingCompletionWithBrandCode:error:"
- "handleRecipientMessage:forInvitationIdentifier:completionHandler:"
- "handleSharingMessage:forInvitationIdentifier:fromMailboxIdentifier:completionHandler:"
- "hasUpgradeAvailableForKeyWithIdentifier:versionType:versions:completionHandler:"
- "hasUpgradeForVersionType:versions:isOwnerPairedKey:"
- "hash"
- "ignoreInvalidAttestationPackageSignature"
- "immoTokenConfig"
- "immoTokenLength"
- "init"
- "initCredentialProvisionedResultWithCredentialIdentifier:keyInformation:"
- "initDataRequiredResultWithCredentialIdentifier:response:keyInformation:"
- "initDataRequiredResultWithResponse:"
- "initFailureResultWithCredentialIdentifier:error:"
- "initFailureResultWithResponse:error:"
- "initForBringOtherKey"
- "initForDeviceVerifiedPasscode:maxRetries:"
- "initForSecondFactorNone"
- "initForServerVerifiedPasscode:"
- "initForVehicleVerifiedPasscode"
- "initInviteAcceptedResultWithResponse:"
- "initPasscodeFailureResultWithCredentialIdentifier:retryCount:"
- "initSharingCancelledResultWithResponse:error:"
- "initWithArray:copyItems:"
- "initWithCCCErrorCode:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithData:outerTag:"
- "initWithData:preferredVersion:"
- "initWithDelegate:"
- "initWithDictionary:"
- "initWithEndpoint:"
- "initWithEndpoint:downgradeFrameworkSetting:"
- "initWithGenericCrossPlatformSharingData:additionalData:privateData:"
- "initWithGenericDataDictionary:additionalDataDictionary:"
- "initWithInvitationIdentifier:keyIdentifier:recipientFlow:secondFactorList:"
- "initWithInvitationIdentifiers:keyIdentifier:recipientFlow:analyticsData:"
- "initWithKeyRole:"
- "initWithKmlErrorCode:"
- "initWithMachServiceName:options:"
- "initWithPassword:displayName:transport:bindingAttestation:ppid:btAddress:btIRK:additionalParameters:"
- "initWithProfile:displayName:metaData:targetDeviceType:"
- "initWithProfile:displayName:metaData:targetDeviceType:enableVehiclePasscode:maxRetriesForDevicePasscode:deviceEnteredPasscode:proprietaryEntitlements:"
- "initWithReaderInformation:"
- "initWithSessionUUID:invitationIdentifier:friendKeyIdentifier:sharingTarget:state:vehicleEnteredPasscode:"
- "initWithSharingFlow:"
- "initWithSharingIdentifier:friendKeyIdentifier:sharingMessageType:message:"
- "initWithSharingSessionIdentifier:ownerIdsIdentifier:"
- "initWithSharingSessionIdentifier:subCaAttestation:casd:rsaCertData:"
- "initWithSharingSessionUUID:bindingAttestation:targetDeviceType:initiatorIdsPseudonym:"
- "initWithSuiteName:"
- "initWithUTF8String:"
- "initWithUUIDString:"
- "initWithVehicleEnteredPasscode:pairedEntityIdentifier:"
- "initWithVersion:ephemeralPublicKey:publicKeyHash:encryptedRequest:"
- "initiatorSupportedFrameworkVersionsData"
- "integerValue"
- "interface"
- "interfaceWithProtocol:"
- "invalidate"
- "isCarKeySupportedForManufacturer:brand:ppid:error:"
- "isDCKConfigurationAvailableFor:error:"
- "isEqual:"
- "isEqualToData:"
- "isEqualToString:"
- "isFirstInQueue"
- "isFriendImmoTokenOrSlotOnline"
- "isImmoTokenNeeded"
- "isKeyAttestationSetByCarInSignalingBitmap:"
- "isKeyAttestationSetByDeviceInSignalingBitmap:"
- "isKindOfClass:"
- "isManufacturerSupported:error:"
- "isMemberOfClass:"
- "isOemPropDataSetByCarInSignalingBitmap:"
- "isOemPropDataSetByDeviceInSignalingBitmap:"
- "isOwnerImmoTokenOrSlotOnline"
- "isProxy"
- "isSharingEnabledForManufacturer:brand:ppid:error:"
- "isSlotIdListSetByCarInSignalingBitmap:"
- "isSlotIdListSetByDeviceInSignalingBitmap:"
- "isSubsetOfSet:"
- "isSupported"
- "isValid"
- "isValidForKmlVersion:transport:"
- "keyAttestationStartOffset"
- "keyPairingSession:didFinishPairingWithKey:trackingRequest:error:"
- "keyRoleToShare"
- "keyRoleToShareOverride"
- "keyTrackingReceiptRequired"
- "kmlCode"
- "kmlOverrideVersion"
- "kmlSupportedVersionsTlvForPairing"
- "kmlSupportedVersionsTlvForShareInitiator"
- "kmlVersionOverride"
- "length"
- "lengthOfBytesUsingEncoding:"
- "listKeysWithHandler:"
- "listKeysWithSession:seid:callback:"
- "listReceivedSharingInvitationsWithCallback:"
- "listSharingInvitationsForKeyIdentifier:callback:"
- "localDeleteKey:callback:"
- "localDeleteKey:completionHandler:"
- "localeWithLocaleIdentifier:"
- "localizedFailureReason"
- "longTermSharedSecret"
- "longValue"
- "mailboxEndOffset"
- "mailboxVersion"
- "maxOfflineAttestationCount"
- "message"
- "messageType"
- "mfiPPID"
- "mockFleetEndpointCert"
- "mockFleetExtCaCert"
- "mockFleetIntermediateCert"
- "mutableBytes"
- "numberFromString:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "oemSpecificContentAsData"
- "onlineAttestationDeliverySupported"
- "onlineBleOOBMasterKeyOverride"
- "opt2"
- "opt2AuthDeletionAlarmDurationSeconds"
- "ourPreferredKmlVersion"
- "ourPreferredVehicleServerVersion"
- "ourSupportedFrameworkVersionsAsCAString"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "ppidRequestForInvitationWithIdentifier:completionHandler:"
- "ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:"
- "preWarmForManufacturer:"
- "preWarmForManufacturer:callback:"
- "pretendBindingAttestationUsed"
- "privateMailboxSettingAsData"
- "proxy"
- "q"
- "q16@0:8"
- "queueCrossPlatformSharingMessage:forInvitationIdentifier:fromMailboxIdentifier:callback:"
- "queueManagementSession:callback:"
- "queueOwnerPairingSession:callback:"
- "queueSharingSession:callback:"
- "readerBtIRK"
- "readerBtIdAddress"
- "readerConfigID"
- "readerInfo"
- "readerInformationForInvitationWithIdentifier:completionHandler:"
- "readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:"
- "readerSupportedTransports"
- "readerSupportsLELR"
- "readerSupportsNfc"
- "readerSupportsUwb"
- "registerCrossPlatformTestMessageOverIDSHandler:"
- "registerCrossPlatformTestMessageSendHandler:"
- "registerFriendSideInvitationUnusableHandler:"
- "registerFriendSidePasscodeRetryRequestHandler:"
- "registerFriendSidePasscodeRetryRequestTestHandler:"
- "registerFriendSideSharingTestCompletion:"
- "registerFriendSideSharingTestInvitationUUIDHandler:"
- "registerOwnerSideInvitationRequestHandler:"
- "registerOwnerSideSharingTestInvitations:callback:"
- "registerSession:"
- "rejectSharingInvitation:completionHandler:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "remoteTerminateKeys:nodeGroupIdentifiers:treeGroupIdentifiers:adminKey:callback:"
- "removeAllObjects"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeSharedKeysWithIdentifiers:ownerKeyWithIdentifier:callback:"
- "removeSharingInvitationWithId:completionHandler:"
- "removeUwbSupportLocally"
- "replaceBytesInRange:withBytes:"
- "requestBindingAttestationDataForKeyWithIdentifier:callback:"
- "requestBindingAttestationDataForManufacturer:callback:"
- "requestInviteWithConfig:completionHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "retryPasscode:forInvitationIdentifier:completionHandler:"
- "retryPasscode:forKeyIdentifier:completionHandler:"
- "revertUpgradeForKeyWithIdentifier:versionType:version:completionHandler:"
- "revokeKeysWithIdentifiers:sharedByOwnerKeyWithIdentifier:callback:"
- "revokeNodesWithGroupIdentifiers:treesWithGroupIdentifier:authorizedByKeyWithIdentifier:callback:"
- "self"
- "sendCrossPlatformTestData:toIdsIdentifier:"
- "sendSharingInvitationForKeyIdentifier:toIdsIdentifier:auth:config:completionHandler:"
- "sendSharingInviteForKeyIdentifier:toIdsIdentifier:auth:config:completionHandler:"
- "sendSilentSharingInvitationWithKeyIdentifier:config:groupIdentifier:completionHandler:"
- "sendSilentSharingInviteForKeyIdentifier:config:groupIdentifier:completionHandler:"
- "serverIssued"
- "setAdditionalMailboxSettingAsData:"
- "setBindingAttestation:"
- "setBindingAttestation:forKeyWithIdentifier:callback:"
- "setCarSupportsUpdateAttestation:"
- "setCccCode:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConfMailboxSettingAsData:"
- "setDateFormat:"
- "setDeviceBtIntroKey:"
- "setDeviceBtOOBKey:"
- "setDeviceEnteredPasscode:"
- "setDidParseDataSuccessfully:"
- "setDisplayName:"
- "setEnableVehicleEnteredPasscode:"
- "setExportedInterface:"
- "setExportedObject:"
- "setImmoTokenConfig:"
- "setInitiatorSupportedFrameworkVersionsData:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsFirstInQueue:"
- "setKeyRole:"
- "setKeyRoleToShare:"
- "setKeyTrackingReceiptRequired:"
- "setKmlCode:"
- "setKmlOverrideVersion:"
- "setLocale:"
- "setMailboxIdentifier:forOwnerKeyIdentifier:forInvitationIdentifier:completionHandler:"
- "setMaxOfflineAttestationCount:"
- "setMaxRetriesForDeviceEnteredPasscode:"
- "setMetaData:"
- "setMfiPPID:"
- "setMockRefreshInstanceCA:"
- "setObject:forKeyedSubscript:"
- "setOemSpecificContentAsData:"
- "setOnlineAttestationDeliverySupported:"
- "setOnlineBleOOBMasterKeyOverride:"
- "setPrivateMailboxSettingAsData:"
- "setProductPlanIdentifier:forInvitationIdentifier:completion:"
- "setProfile:"
- "setProprietaryEntitlements:"
- "setProxy:"
- "setReaderBtIRK:"
- "setReaderBtIdAddress:"
- "setReaderSupportsLELR:"
- "setReaderSupportsNfc:"
- "setReaderSupportsUwb:"
- "setRemoteObjectInterface:"
- "setSharingPasswordLength:"
- "setSharingPasswordLengthAsData:"
- "setSharingPasswordRequired:"
- "setSupportedKeyProfiles:"
- "setTargetDeviceType:"
- "setTimeZone:"
- "setTrackingReceipt:decryptedDeviceData:forKeyWithIdentifier:"
- "setTrackingReceipt:forKeyWithIdentifier:"
- "setTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:forKeyWithIdentifier:"
- "setTrackingReceipt:vehicleMobilizationData:forKeyWithIdentifier:"
- "setUwbDisabledLocally:"
- "setV3ConfMailboxSettingAsData:"
- "setV3PrivateMailboxSettingAsData:"
- "setVehicleSupportedFrameworkVersionsData:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "sharedManager"
- "sharedVersionsOverrides"
- "sharingConfigForFriendAsData"
- "sharingIdentifier"
- "sharingPasswordLength"
- "sharingPasswordLengthAsData"
- "sharingPasswordRequired"
- "shortValue"
- "signAppData:appBundleIdentifier:nonce:auth:keyIdentifier:callback:"
- "signalingBitmapOffset"
- "signerSlotIdListOffset"
- "simulateCrossPlatformSharingInitiator"
- "skipWaitingForBindingAttestation"
- "slotIdBitmapOffset"
- "slotIdListOffset"
- "slotIdentifierLength"
- "startKeyPairingWithConfig:"
- "startKeyPairingWithConfig:callback:"
- "startKeyPairingWithPassword:displayName:"
- "startKeyPairingWithPassword:displayName:transport:"
- "startKeyPairingWithPassword:displayName:transport:bindingAttestation:"
- "startProbing"
- "startProbingWithCallback:"
- "startShareAcceptanceFlowWithInvitation:completionHandler:"
- "startShareAcceptanceFlowWithInvitation:fromMailboxIdentifier:completionHandler:"
- "string"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForKey:"
- "stringFromDate:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subCAAttestation"
- "subdataWithRange:"
- "subjectIdentifier"
- "substringWithRange:"
- "superclass"
- "supportedKeyProfiles"
- "supportedRadiosAsDataForTarget:"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "tag"
- "timeIntervalForUserDefault:minTimeInterval:maxTimeInterval:defaultTimeInterval:"
- "timeIntervalSince1970"
- "timeZoneWithName:"
- "unarchivedObjectOfClasses:fromData:error:"
- "underlyingErrors"
- "unregisterSession:"
- "unregisterSharingTestHandlers"
- "unsignedShortValue"
- "updateAliroCredentialDocumentStatus:seid:keyIdentifier:accessDocumentPresent:accessDocumentSignedTimestamp:revocationDocumentPresent:revocationDocumentSignedTimestamp:"
- "updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:"
- "updateConfiguration:forKeyWithIdentifier:completionHandler:"
- "updateHydraKey:session:seid:encryptedSEData:outError:"
- "updatePPIDWithConfigValue:"
- "updatePPIDWithServerProvidedData:"
- "updateSharingAnalyticsWithConfig:completionHandler:"
- "updateSharingConfigWithData:"
- "updateSupportedFrameworkVersionsForSharing:"
- "updateSupportedRadiosWithData:"
- "updateVehicleServerSupportedVersions:"
- "updateVehicleSupportedAppletVersions:"
- "updateVehicleSupportedBluetoothVersions:"
- "updateVehicleSupportedFrameworkVersions:"
- "upgradeForVersionType:version:"
- "upgradeKeyWithIdentifier:versionType:version:upgradeInformation:completionHandler:"
- "useAppletVersionsForCertificationTesting"
- "useBasicSecurityPolicy"
- "useOldKeyConfigTag"
- "useOldKeyTrackingTag"
- "useOldSignalingBitmap"
- "userInfo"
- "uwbDisabledLocally"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"DAAlishaKeyEncryptedRequest\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"DAKeyBindingAttestationRequestData\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@\"NSError\"24"
- "v32@0:8Q16@24"
- "v32@0:8Q16Q24"
- "v3ConfMailboxSettingAsData"
- "v3PrivateMailboxSettingAsData"
- "v40@0:8@\"DAAlishaKeyEncryptedRequest\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSError\"16@\"DAKeyInformation\"24@\"DAAlishaKeyEncryptedRequest\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"DAAlishaKeyEncryptedRequest\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8@16Q24Q32@?40"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16Q24Q32@40@?48"
- "v64@0:8@16@24@32@40@48@?56"
- "value"
- "valueAsUnsignedChar"
- "valueAsUnsignedLong"
- "valueAsUnsignedShort"
- "valueWithBytes:objCType:"
- "valueWithDAAvailableVersionUpgrade:"
- "vehicleProprietaryDataOffset"
- "vehicleSupportedAppletVersionsTlvAsData"
- "vehicleSupportedBluetoothVersionsTlvAsData"
- "vehicleSupportedFrameworkVersionsData"
- "vehicleSupportedFrameworkVersionsForCA"
- "vehicleSupportedFrameworkVersionsTlvAsData"
- "vehicleSupportedVersionsData"
- "withEndpoint:"
- "zone"
- "{_DAVersionUpgrade=QBQQ}16@0:8"
- "{_DAVersionUpgrade=QBQQ}36@0:8Q16@24B32"

```
