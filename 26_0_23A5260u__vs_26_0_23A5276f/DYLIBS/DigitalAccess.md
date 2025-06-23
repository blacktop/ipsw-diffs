## DigitalAccess

> `/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess`

```diff

-60.26.1.0.0
-  __TEXT.__text: 0x32e50
+60.28.0.0.0
+  __TEXT.__text: 0x330e8
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x252c
+  __TEXT.__objc_methlist: 0x2514
   __TEXT.__const: 0x6a8
   __TEXT.__cstring: 0x6e71
   __TEXT.__oslogstring: 0x1f02
   __TEXT.__gcc_except_tab: 0x1180
-  __TEXT.__unwind_info: 0xbe8
+  __TEXT.__unwind_info: 0xc00
   __TEXT.__objc_classname: 0x4f4
-  __TEXT.__objc_methname: 0x66c3
+  __TEXT.__objc_methname: 0x66ad
   __TEXT.__objc_methtype: 0x1a1a
-  __TEXT.__objc_stubs: 0x29c0
+  __TEXT.__objc_stubs: 0x29a0
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0xf90
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12e0
+  __DATA_CONST.__objc_selrefs: 0x12d8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__auth_got: 0x338
-  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x1be0
   __AUTH_CONST.__objc_const: 0x41a8
-  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x2d8
   __DATA.__data: 0x600
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSESShared.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 277C4867-249F-3D40-8BAF-9B0B1DA1A150
-  Functions: 918
-  Symbols:   3028
-  CStrings:  2172
+  UUID: A4A10EF2-C70F-3536-8C07-43C0E622599F
+  Functions: 915
+  Symbols:   3017
+  CStrings:  2171
 
Symbols:
+ ___102-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.48
+ ___102-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:fromMailboxIdentifier:completionHandler:]_block_invoke.30
+ ___105-[DAKeyManagementSession hasUpgradeAvailableForKeyWithIdentifier:versionType:versions:completionHandler:]_block_invoke.34
+ ___105-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.51
+ ___107-[DAKeySharingSession sendSharingInvitationForKeyIdentifier:toIdsIdentifier:auth:config:completionHandler:]_block_invoke.13
+ ___108-[DAKeyManagementSession upgradeKeyWithIdentifier:versionType:version:upgradeInformation:completionHandler:]_block_invoke.36
+ ___108-[DAKeySharingSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.49
+ ___108-[DAKeySharingSession setMailboxIdentifier:forOwnerKeyIdentifier:forInvitationIdentifier:completionHandler:]_block_invoke.28
+ ___109-[DAKeySharingSession sendSilentSharingInvitationWithKeyIdentifier:config:groupIdentifier:completionHandler:]_block_invoke.15
+ ___110-[DAKeySharingSession acceptSharingInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.22
+ ___111-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.52
+ ___113-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:]_block_invoke.39
+ ___116-[DAKeySharingSession acceptCrossPlatformInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.33
+ ___122-[DAKeyManagementSession revokeNodesWithGroupIdentifiers:treesWithGroupIdentifier:authorizedByKeyWithIdentifier:callback:]_block_invoke.33
+ ___133-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:ourBindingAttestation:config:completionHandler:]_block_invoke.25
+ ___23-[DASession endSession]_block_invoke.14
+ ___35-[DAKeyPairingSession startProbing]_block_invoke.16
+ ___35-[DAManager establishXpcConnection]_block_invoke.73
+ ___35-[DAManager establishXpcConnection]_block_invoke.73.cold.1
+ ___46-[DAKeyPairingSession preWarmForManufacturer:]_block_invoke.13
+ ___46-[DAManager createPairingSessionWithDelegate:]_block_invoke.76
+ ___46-[DAManager createSharingSessionWithDelegate:]_block_invoke.79
+ ___47-[DAKeySharingSession cancelSharingInvitation:]_block_invoke.18
+ ___49-[DAManager createManagementSessionWithDelegate:]_block_invoke.82
+ ___54-[DAKeyManagementSession deleteKey:completionHandler:]_block_invoke.15
+ ___59-[DAKeyManagementSession localDeleteKey:completionHandler:]_block_invoke.22
+ ___65-[DAKeySharingSession cancelSharingInvitation:completionHandler:]_block_invoke.21
+ ___65-[DAKeySharingSession requestInviteWithConfig:completionHandler:]_block_invoke.24
+ ___69-[DAKeyManagementSession listReceivedSharingInvitationsWithCallback:]_block_invoke.21
+ ___71-[DAKeySharingSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.47
+ ___72-[DAKeySharingSession retryPasscode:forKeyIdentifier:completionHandler:]_block_invoke.40
+ ___73-[DAKeyManagementSession cancelInvitationWithIdentifier:reason:callback:]_block_invoke.28
+ ___74-[DAKeyManagementSession cancelAllFriendInvitationsWithCompletionHandler:]_block_invoke.23
+ ___74-[DAKeyManagementSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.50
+ ___74-[DAKeyManagementSession listSharingInvitationsForKeyIdentifier:callback:]_block_invoke.19
+ ___74-[DAKeyManagementSession removeSharingInvitationWithId:completionHandler:]_block_invoke.24
+ ___74-[DAKeySharingSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.54
+ ___74-[DAKeySharingSession updateSharingAnalyticsWithConfig:completionHandler:]_block_invoke.41
+ ___75-[DAKeySharingSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.44
+ ___77-[DAKeyManagementSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.57
+ ___78-[DAKeyManagementSession countImmobilizerTokensForKeyWithIdentifier:callback:]_block_invoke.25
+ ___78-[DAKeyManagementSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.48
+ ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.21
+ ___79-[DAKeySharingSession retryPasscode:forInvitationIdentifier:completionHandler:]_block_invoke.39
+ ___80-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.51
+ ___80-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:]_block_invoke.29
+ ___80-[DAManager handleSharingMessage:forInvitationIdentifier:fromMailboxIdentifier:]_block_invoke.84
+ ___81-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.43
+ ___81-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:completionHandler:]_block_invoke.34
+ ___82-[DAKeySharingSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.42
+ ___83-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.54
+ ___83-[DAKeySharingSession authorizeSharingInvitationIdentifier:auth:completionHandler:]_block_invoke.17
+ ___83-[DAKeySharingSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.52
+ ___85-[DAKeyManagementSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.46
+ ___85-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:completionHandler:]_block_invoke.45
+ ___86-[DAKeyManagementSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.55
+ ___86-[DAKeySharingSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.53
+ ___87-[DAKeySharingSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.45
+ ___88-[DAKeySharingSession handleInitiatorMessage:forInvitationIdentifier:completionHandler:]_block_invoke.37
+ ___88-[DAKeySharingSession handleRecipientMessage:forInvitationIdentifier:completionHandler:]_block_invoke.35
+ ___89-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.56
+ ___90-[DAKeyManagementSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.49
+ ___90-[DAKeyManagementSession removeSharedKeysWithIdentifiers:ownerKeyWithIdentifier:callback:]_block_invoke.30
+ ___90-[DAKeySharingSession createSilentSharingInvitationWithGroupIdentifier:completionHandler:]_block_invoke.26
+ ___92-[DAKeyManagementSession revokeKeysWithIdentifiers:sharedByOwnerKeyWithIdentifier:callback:]_block_invoke.31
+ ___92-[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:]_block_invoke.14
+ ___96-[DAKeySharingSession acceptSharingInvitation:fromMailboxIdentifier:passcode:completionHandler:]_block_invoke.31
+ ___97-[DAKeyManagementSession cancelInvitationsWithIdentifiers:sentByOwnerKeyWithIdentifier:callback:]_block_invoke.27
+ ___98-[DAKeyManagementSession commitUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.37
+ ___98-[DAKeyManagementSession revertUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.38
+ ___block_literal_global.100
+ ___block_literal_global.102
+ ___block_literal_global.104
+ ___block_literal_global.28
+ ___block_literal_global.363
+ ___block_literal_global.431
+ _decodeWithData:error:.allowedClasses.361
+ _decodeWithData:error:.allowedClasses.429
+ _decodeWithData:error:.pred.360
+ _decodeWithData:error:.pred.428
- +[KmlSettingsManager sharedSettingsManager]
- +[KmlSettingsManager sharedSettingsManager].cold.1
- __OBJC_$_CLASS_METHODS_KmlSettingsManager
- ___102-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.42
- ___102-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:fromMailboxIdentifier:completionHandler:]_block_invoke.24
- ___105-[DAKeyManagementSession hasUpgradeAvailableForKeyWithIdentifier:versionType:versions:completionHandler:]_block_invoke.28
- ___105-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.45
- ___107-[DAKeySharingSession sendSharingInvitationForKeyIdentifier:toIdsIdentifier:auth:config:completionHandler:]_block_invoke.7
- ___108-[DAKeyManagementSession upgradeKeyWithIdentifier:versionType:version:upgradeInformation:completionHandler:]_block_invoke.30
- ___108-[DAKeySharingSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.43
- ___108-[DAKeySharingSession setMailboxIdentifier:forOwnerKeyIdentifier:forInvitationIdentifier:completionHandler:]_block_invoke.22
- ___109-[DAKeySharingSession sendSilentSharingInvitationWithKeyIdentifier:config:groupIdentifier:completionHandler:]_block_invoke.9
- ___110-[DAKeySharingSession acceptSharingInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.16
- ___111-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.46
- ___113-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:]_block_invoke.33
- ___116-[DAKeySharingSession acceptCrossPlatformInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.27
- ___122-[DAKeyManagementSession revokeNodesWithGroupIdentifiers:treesWithGroupIdentifier:authorizedByKeyWithIdentifier:callback:]_block_invoke.27
- ___133-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:ourBindingAttestation:config:completionHandler:]_block_invoke.19
- ___23-[DASession endSession]_block_invoke.8
- ___35-[DAKeyPairingSession startProbing]_block_invoke.10
- ___35-[DAManager establishXpcConnection]_block_invoke.67
- ___35-[DAManager establishXpcConnection]_block_invoke.67.cold.1
- ___43+[KmlSettingsManager sharedSettingsManager]_block_invoke
- ___46-[DAKeyPairingSession preWarmForManufacturer:]_block_invoke.7
- ___46-[DAManager createPairingSessionWithDelegate:]_block_invoke.70
- ___46-[DAManager createSharingSessionWithDelegate:]_block_invoke.73
- ___47-[DAKeySharingSession cancelSharingInvitation:]_block_invoke.12
- ___49-[DAManager createManagementSessionWithDelegate:]_block_invoke.76
- ___54-[DAKeyManagementSession deleteKey:completionHandler:]_block_invoke.9
- ___59-[DAKeyManagementSession localDeleteKey:completionHandler:]_block_invoke.16
- ___65-[DAKeySharingSession cancelSharingInvitation:completionHandler:]_block_invoke.15
- ___65-[DAKeySharingSession requestInviteWithConfig:completionHandler:]_block_invoke.18
- ___69-[DAKeyManagementSession listReceivedSharingInvitationsWithCallback:]_block_invoke.15
- ___71-[DAKeySharingSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.41
- ___72-[DAKeySharingSession retryPasscode:forKeyIdentifier:completionHandler:]_block_invoke.34
- ___73-[DAKeyManagementSession cancelInvitationWithIdentifier:reason:callback:]_block_invoke.22
- ___74-[DAKeyManagementSession cancelAllFriendInvitationsWithCompletionHandler:]_block_invoke.17
- ___74-[DAKeyManagementSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.44
- ___74-[DAKeyManagementSession listSharingInvitationsForKeyIdentifier:callback:]_block_invoke.13
- ___74-[DAKeyManagementSession removeSharingInvitationWithId:completionHandler:]_block_invoke.18
- ___74-[DAKeySharingSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.48
- ___74-[DAKeySharingSession updateSharingAnalyticsWithConfig:completionHandler:]_block_invoke.35
- ___75-[DAKeySharingSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.38
- ___77-[DAKeyManagementSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.51
- ___78-[DAKeyManagementSession countImmobilizerTokensForKeyWithIdentifier:callback:]_block_invoke.19
- ___78-[DAKeyManagementSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.42
- ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.15
- ___79-[DAKeySharingSession retryPasscode:forInvitationIdentifier:completionHandler:]_block_invoke.33
- ___80-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.45
- ___80-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:]_block_invoke.23
- ___80-[DAManager handleSharingMessage:forInvitationIdentifier:fromMailboxIdentifier:]_block_invoke.78
- ___81-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.37
- ___81-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:completionHandler:]_block_invoke.28
- ___82-[DAKeySharingSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.36
- ___83-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.48
- ___83-[DAKeySharingSession authorizeSharingInvitationIdentifier:auth:completionHandler:]_block_invoke.11
- ___83-[DAKeySharingSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.46
- ___85-[DAKeyManagementSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.40
- ___85-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:completionHandler:]_block_invoke.39
- ___86-[DAKeyManagementSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.49
- ___86-[DAKeySharingSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.47
- ___87-[DAKeySharingSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.39
- ___88-[DAKeySharingSession handleInitiatorMessage:forInvitationIdentifier:completionHandler:]_block_invoke.31
- ___88-[DAKeySharingSession handleRecipientMessage:forInvitationIdentifier:completionHandler:]_block_invoke.29
- ___89-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.50
- ___90-[DAKeyManagementSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.43
- ___90-[DAKeyManagementSession removeSharedKeysWithIdentifiers:ownerKeyWithIdentifier:callback:]_block_invoke.24
- ___90-[DAKeySharingSession createSilentSharingInvitationWithGroupIdentifier:completionHandler:]_block_invoke.20
- ___92-[DAKeyManagementSession revokeKeysWithIdentifiers:sharedByOwnerKeyWithIdentifier:callback:]_block_invoke.25
- ___92-[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:]_block_invoke.8
- ___96-[DAKeySharingSession acceptSharingInvitation:fromMailboxIdentifier:passcode:completionHandler:]_block_invoke.25
- ___97-[DAKeyManagementSession cancelInvitationsWithIdentifiers:sentByOwnerKeyWithIdentifier:callback:]_block_invoke.21
- ___98-[DAKeyManagementSession commitUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.31
- ___98-[DAKeyManagementSession revertUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.32
- ___block_literal_global.22
- ___block_literal_global.357
- ___block_literal_global.425
- ___block_literal_global.80
- ___block_literal_global.82
- ___block_literal_global.84
- _decodeWithData:error:.allowedClasses.355
- _decodeWithData:error:.allowedClasses.423
- _decodeWithData:error:.pred.354
- _decodeWithData:error:.pred.422
- _objc_msgSend$sharedSettingsManager
- _sharedSettingsManager._sharedInstance
- _sharedSettingsManager.onceToken
CStrings:
- "sharedSettingsManager"

```
