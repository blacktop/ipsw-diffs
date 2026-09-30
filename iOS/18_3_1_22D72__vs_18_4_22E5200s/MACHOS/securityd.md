## securityd

> `/usr/libexec/securityd`

```diff

-61439.82.1.0.0
-  __TEXT.__text: 0x2308dc
-  __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1a4c0
-  __TEXT.__objc_methlist: 0x128e4
-  __TEXT.__const: 0x8cd
-  __TEXT.__cstring: 0x1f929
-  __TEXT.__oslogstring: 0x29062
-  __TEXT.__gcc_except_tab: 0xacb0
-  __TEXT.__objc_classname: 0x2284
-  __TEXT.__objc_methname: 0x292e2
-  __TEXT.__objc_methtype: 0x9a89
+61439.100.285.0.1
+  __TEXT.__text: 0x233b10
+  __TEXT.__auth_stubs: 0x3980
+  __TEXT.__objc_stubs: 0x1ade0
+  __TEXT.__objc_methlist: 0x14694
+  __TEXT.__const: 0x3e5
+  __TEXT.__cstring: 0x1f90f
+  __TEXT.__oslogstring: 0x29496
   __TEXT.__dlopen_cstrs: 0x1c8
+  __TEXT.__gcc_except_tab: 0xad08
+  __TEXT.__objc_classname: 0x2289
+  __TEXT.__objc_methname: 0x2a0cb
+  __TEXT.__objc_methtype: 0x9d71
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6220
-  __DATA_CONST.__auth_got: 0x1c70
-  __DATA_CONST.__got: 0x1048
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x13058
-  __DATA_CONST.__cfstring: 0x1a560
+  __TEXT.__unwind_info: 0x6098
+  __DATA_CONST.__auth_got: 0x1cd0
+  __DATA_CONST.__got: 0x1080
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x13770
+  __DATA_CONST.__cfstring: 0x1a8a0
   __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x210

   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x7d8
   __DATA_CONST.__objc_intobj: 0x12d8
-  __DATA_CONST.__objc_arraydata: 0x3d8
+  __DATA_CONST.__objc_arraydata: 0x3e8
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x23518
-  __DATA.__objc_selrefs: 0x8758
-  __DATA.__objc_ivar: 0x185c
+  __DATA.__objc_const: 0x21900
+  __DATA.__objc_selrefs: 0x8bd8
+  __DATA.__objc_ivar: 0x1954
   __DATA.__objc_data: 0x5460
-  __DATA.__data: 0x20b8
-  __DATA.__thread_vars: 0xd8
-  __DATA.__thread_bss: 0x1e
-  __DATA.__bss: 0x9d0
-  __DATA.__common: 0x10
+  __DATA.__data: 0x1ee8
+  __DATA.__thread_vars: 0xc0
+  __DATA.__thread_bss: 0x28
+  __DATA.__bss: 0x9b8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9067
-  Symbols:   1452
-  CStrings:  15148
+  Functions: 9130
+  Symbols:   1473
+  CStrings:  15369
 
Symbols:
+ _aks_assert_drop
+ _aks_assert_hold
+ _aks_dealloc
+ _aks_generation
+ _aks_get_bag_uuid
+ _aks_get_device_state
+ _aks_get_lock_state
+ _aks_get_system
+ _aks_kc_backup_get_uuid
+ _aks_kc_backup_open_keybag
+ _aks_kc_backup_unwrap_key
+ _aks_kc_backup_wrap_key
+ _aks_load_bag
+ _aks_operation_optional_params
+ _aks_params_create
+ _aks_params_free
+ _aks_params_get_der
+ _aks_params_set_data
+ _aks_ref_key_create
+ _aks_ref_key_create_with_blob
+ _aks_ref_key_decrypt
+ _aks_ref_key_delete
+ _aks_ref_key_encrypt
+ _aks_ref_key_free
+ _aks_ref_key_get_blob
+ _aks_ref_key_get_external_data
+ _aks_ref_key_get_public_key
+ _aks_ref_key_unwrap
+ _aks_ref_key_wrap
+ _aks_unload_bag
+ _aks_unlock_bag
+ _aks_unwrap_key
+ _aks_wrap_key
+ _kSecAttrAlias
+ _kSecAttrEndDate
+ _kSecAttrHasCustomIcon
+ _kSecAttrIsNegative
+ _kSecAttrKeyCreator
+ _kSecAttrScriptCode
+ _kSecAttrStartDate
+ _kSecurityRTCEventNameEstablishOperation
+ _kSecurityRTCEventNameJoinWithVoucherOperation
+ _kSecurityRTCEventNameVouchWithBottle
- _IOConnectCallMethod
- _IOServiceClose
- ___stdoutp
- _calloc
- _ccaes_cbc_decrypt_mode
- _cccbc_clear_iv
- _cccbc_init
- _cccbc_update
- _cccurve25519_make_pub
- _ccder_blob_decode_len
- _ccder_blob_decode_range
- _ccder_blob_decode_sequence_tl
- _ccder_blob_decode_tag
- _ccder_blob_decode_tl
- _ccder_blob_encode_body
- _ccder_blob_encode_tl
- _ccec_compact_import_pub
- _ccec_cp_384
- _ccec_export_pub
- _fmod
- _fprintf
- _uuid_compare
CStrings:
+ "\x01t\x83"
+ "\x01\x8f\x01\x14"
+ "\x02\x14#\x13"
+ "\x0f\x01\"F"
+ "-[CuttlefishXPCWrapper attemptPreapprovedJoinWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper establishWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper fetchRecoverableTLKSharesWithSpecificUser:peerID:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper preflightVouchWithBottleWithSpecificUser:bottleID:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper vouchWithBottleWithSpecificUser:bottleID:entropy:bottleSalt:tlkShares:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "<CKKSZoneStateEntry[%@](%@): created:%@ subscribed:%@ moreRecords:%@ fetchNewestChangesFirst:%@ initialSyncFinished:%@>"
+ "@92@0:8@16@24B32B36@40B48@52@60Q68@76B84B88"
+ "Doesn't have canDecrypt, setting with %ld"
+ "Doesn't have canDerive, setting with %ld"
+ "Doesn't have canEncrypt, setting with %ld"
+ "Doesn't have canSignRecover, setting with %ld"
+ "Doesn't have canUnwrap, setting with %ld"
+ "Doesn't have canVerify, setting with %ld"
+ "Doesn't have canVerifyRecover, setting with %ld"
+ "Doesn't have canWrap, setting with %ld"
+ "Doesn't have isExtractable, setting with %ld"
+ "Doesn't have isModifiable, setting with %ld"
+ "Doesn't have isPermanent, setting with %ld"
+ "Doesn't have isPrivate, setting with %ld"
+ "Doesn't have isSensitive, setting with %ld"
+ "Doesn't have key class, setting with %ld"
+ "Doesn't have wasAlwaysSensitive, setting with %ld"
+ "Doesn't have wasNeverExtractable, setting with %ld"
+ "Doesn't havec canSign, setting with %ld"
+ "Have canDecrypt"
+ "Have canDerive"
+ "Have canEncrypt"
+ "Have canSign"
+ "Have canSignRecover"
+ "Have canUnwrap"
+ "Have canVerify"
+ "Have canVerifyRecover"
+ "Have canWrap"
+ "Have isExtractable"
+ "Have isModifiable"
+ "Have isPermanent"
+ "Have isPrivate"
+ "Have isSensitive"
+ "Have key class"
+ "Have wasAlwaysSensitive"
+ "Have wasNeverExtractable"
+ "Issuing deletion of olditem: %{private}@"
+ "KCSharingInternetPasswordCredential(sharingGroup:%@ accessGroup:%@ account:%@ protocol:%@ server:%@ port:%@ path:%@ authenticationType:%@ type:%ld creator:%ld description:%@ alias:%@ visibility:%ld negative:%ld icon:%ld scriptCode:%ld creationDate:%@ modificationDate:%@ comment:%@ label:%@ accessibility:%@ viewHint:%@ securityDomain:%@)"
+ "KCSharingPrivateKeyCredential(sharingGroup:%@, accessGroup:%@, keyType:%ld, applicationTag:%@, label:%@, applicationLabel:%@, alias:%@, startDate:%@, endDate:%@, viewHint:%@, keyClass:%ld, isPermanent:%ld, isPrivate:%ld, isModifiable:%ld, isSensitive:%ld, wasAlwaysSensitive:%ld, isExtractable:%ld, wasNeverExtractable:%ld ,canEncrypt:%ld, canDecrypt:%ld, canDerive:%ld, canSign:%ld, canVerify:%ld, canSignRecover:%ld, canVerifyRecover:%ld, canWrap:%ld, canUnwrap:%ld, creator:%ld, keySizeInBits:%ld, effectiveKeySize:%ld, creationDate:%@, modificationDate:%@)"
+ "Primary key conflict; deleting incoming CK item (%@)%{private}@ in favor of old item (%@)%{private}@"
+ "Rejecting (%@) outgoing queue entry creation for tombstone item: %{private}@"
+ "T@\"NSData\",&,N,V_alias"
+ "T@\"NSData\",R,N,V_alias"
+ "T@\"NSDate\",R,N,V_endDate"
+ "T@\"NSDate\",R,N,V_startDate"
+ "T@\"NSString\",&,N,V_itemDescription"
+ "T@\"NSString\",R,N,V_itemDescription"
+ "TB,V_fetchNewestChangesFirst"
+ "TB,V_initialSyncFinished"
+ "Td,N,V_endDate"
+ "Td,N,V_startDate"
+ "Ti,N,V_canDecrypt"
+ "Ti,N,V_canDerive"
+ "Ti,N,V_canEncrypt"
+ "Ti,N,V_canSign"
+ "Ti,N,V_canSignRecover"
+ "Ti,N,V_canUnwrap"
+ "Ti,N,V_canVerify"
+ "Ti,N,V_canVerifyRecover"
+ "Ti,N,V_canWrap"
+ "Ti,N,V_creator"
+ "Ti,N,V_isExtractable"
+ "Ti,N,V_isModifiable"
+ "Ti,N,V_isPermanent"
+ "Ti,N,V_isPrivate"
+ "Ti,N,V_isSensitive"
+ "Ti,N,V_keyClass"
+ "Ti,N,V_wasAlwaysSensitive"
+ "Ti,N,V_wasNeverExtractable"
+ "Tombstone modification not allowed"
+ "Tq,N,V_creator"
+ "Tq,N,V_customIcon"
+ "Tq,N,V_isInvisible"
+ "Tq,N,V_isNegative"
+ "Tq,N,V_scriptCode"
+ "Tq,N,V_type"
+ "Tq,R,N,V_canDecrypt"
+ "Tq,R,N,V_canDerive"
+ "Tq,R,N,V_canEncrypt"
+ "Tq,R,N,V_canSign"
+ "Tq,R,N,V_canSignRecover"
+ "Tq,R,N,V_canUnwrap"
+ "Tq,R,N,V_canVerify"
+ "Tq,R,N,V_canVerifyRecover"
+ "Tq,R,N,V_canWrap"
+ "Tq,R,N,V_creator"
+ "Tq,R,N,V_customIcon"
+ "Tq,R,N,V_isExtractable"
+ "Tq,R,N,V_isInvisible"
+ "Tq,R,N,V_isModifiable"
+ "Tq,R,N,V_isNegative"
+ "Tq,R,N,V_isPermanent"
+ "Tq,R,N,V_isPrivate"
+ "Tq,R,N,V_isSensitive"
+ "Tq,R,N,V_keyClass"
+ "Tq,R,N,V_scriptCode"
+ "Tq,R,N,V_wasAlwaysSensitive"
+ "Tq,R,N,V_wasNeverExtractable"
+ "UUID of olditem (%@) is higher than UUID of incoming item (%@)"
+ "_SecItemAdd returned bad data type"
+ "_alias"
+ "_canDecrypt"
+ "_canDerive"
+ "_canEncrypt"
+ "_canSign"
+ "_canSignRecover"
+ "_canUnwrap"
+ "_canVerify"
+ "_canVerifyRecover"
+ "_canWrap"
+ "_creator"
+ "_customIcon"
+ "_endDate"
+ "_fetchNewestChangesFirst"
+ "_initialSyncFinished"
+ "_isExtractable"
+ "_isInvisible"
+ "_isModifiable"
+ "_isNegative"
+ "_isPermanent"
+ "_isPrivate"
+ "_isSensitive"
+ "_itemDescription"
+ "_keyClass"
+ "_scriptCode"
+ "_startDate"
+ "_wasAlwaysSensitive"
+ "_wasNeverExtractable"
+ "alias"
+ "attemptPreapprovedJoinWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "canDecrypt"
+ "canDerive"
+ "canEncrypt"
+ "canSign"
+ "canSignRecover"
+ "canUnwrap"
+ "canVerify"
+ "canVerifyRecover"
+ "canWrap"
+ "creation-date-missing"
+ "creator"
+ "customIcon"
+ "endDate"
+ "establishWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "fetchNewestChangesFirst"
+ "fetchRecoverableTLKShares:peerID:contextID:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "fetchRecoverableTLKSharesWithSpecificUser:peerID:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "hasAlias"
+ "hasCanDecrypt"
+ "hasCanDerive"
+ "hasCanEncrypt"
+ "hasCanSign"
+ "hasCanSignRecover"
+ "hasCanUnwrap"
+ "hasCanVerify"
+ "hasCanVerifyRecover"
+ "hasCanWrap"
+ "hasCreator"
+ "hasCustomIcon"
+ "hasEndDate"
+ "hasIsExtractable"
+ "hasIsInvisible"
+ "hasIsModifiable"
+ "hasIsNegative"
+ "hasIsPermanent"
+ "hasIsPrivate"
+ "hasIsSensitive"
+ "hasItemDescription"
+ "hasKeyClass"
+ "hasScriptCode"
+ "hasStartDate"
+ "hasWasAlwaysSensitive"
+ "hasWasNeverExtractable"
+ "initWithContextID:zoneName:zoneCreated:zoneSubscribed:changeToken:moreRecordsInCloudKit:lastFetch:lastScan:lastFixup:encodedRateLimiter:fetchNewestChangesFirst:initialSyncFinished:"
+ "initialSyncFinished"
+ "initialSyncStatus:reply:"
+ "isExtractable"
+ "isInvisible"
+ "isModifiable"
+ "isNegative"
+ "isPermanent"
+ "isPrivate"
+ "isSensitive"
+ "itemDescription"
+ "keyClass"
+ "preflightVouchWithBottleWithSpecificUser:bottleID:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "proceedWithFilteredTLKShares:vouchWithBottleEvent:"
+ "proceedWithPeerID:refetchWasNeeded:vouchWithBottleEvent:"
+ "proceedWithPendingTLKShares:event:"
+ "scriptCode"
+ "setAlias:"
+ "setCanDecrypt:"
+ "setCanDerive:"
+ "setCanEncrypt:"
+ "setCanSign:"
+ "setCanSignRecover:"
+ "setCanUnwrap:"
+ "setCanVerify:"
+ "setCanVerifyRecover:"
+ "setCanWrap:"
+ "setCreator:"
+ "setCustomIcon:"
+ "setEndDate:"
+ "setFetchNewestChangesFirst:"
+ "setHasCanDecrypt:"
+ "setHasCanDerive:"
+ "setHasCanEncrypt:"
+ "setHasCanSign:"
+ "setHasCanSignRecover:"
+ "setHasCanUnwrap:"
+ "setHasCanVerify:"
+ "setHasCanVerifyRecover:"
+ "setHasCanWrap:"
+ "setHasCreator:"
+ "setHasCustomIcon:"
+ "setHasEndDate:"
+ "setHasIsExtractable:"
+ "setHasIsInvisible:"
+ "setHasIsModifiable:"
+ "setHasIsNegative:"
+ "setHasIsPermanent:"
+ "setHasIsPrivate:"
+ "setHasIsSensitive:"
+ "setHasKeyClass:"
+ "setHasScriptCode:"
+ "setHasStartDate:"
+ "setHasWasAlwaysSensitive:"
+ "setHasWasNeverExtractable:"
+ "setInitialSyncFinished:"
+ "setIsExtractable:"
+ "setIsInvisible:"
+ "setIsModifiable:"
+ "setIsNegative:"
+ "setIsPermanent:"
+ "setIsPrivate:"
+ "setIsSensitive:"
+ "setItemDescription:"
+ "setKeyClass:"
+ "setScriptCode:"
+ "setStartDate:"
+ "setWasAlwaysSensitive:"
+ "setWasNeverExtractable:"
+ "startDate"
+ "uuid disappeared"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v36@0:8@16B24@28"
+ "v68@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48B56@?<v@?@\"NSArray\"@\"NSError\">60"
+ "v68@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48B56@?<v@?@\"NSString\"@\"TPSyncingPolicy\"B@\"NSError\">60"
+ "v68@0:8@16@24@32@40@48B56@?60"
+ "v76@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56B64@?<v@?@\"NSArray\"@\"NSError\">68"
+ "v76@0:8@16@24@32@40@48@56B64@?68"
+ "v84@0:8@\"TPSpecificUser\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64B72@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">76"
+ "v84@0:8@16@24@32@40@48@56@64B72@?76"
+ "v92@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40@\"NSArray\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72B80@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">84"
+ "vouchWithBottleWithSpecificUser:bottleID:entropy:bottleSalt:tlkShares:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "wasAlwaysSensitive"
+ "wasNeverExtractable"
+ "{?=\"creationDate\"b1\"creator\"b1\"customIcon\"b1\"isInvisible\"b1\"isNegative\"b1\"modificationDate\"b1\"scriptCode\"b1\"type\"b1\"port\"b1}"
+ "{?=\"creationDate\"b1\"effectiveKeySize\"b1\"endDate\"b1\"keySizeInBits\"b1\"keyType\"b1\"modificationDate\"b1\"startDate\"b1\"canDecrypt\"b1\"canDerive\"b1\"canEncrypt\"b1\"canSign\"b1\"canSignRecover\"b1\"canUnwrap\"b1\"canVerify\"b1\"canVerifyRecover\"b1\"canWrap\"b1\"creator\"b1\"isExtractable\"b1\"isModifiable\"b1\"isPermanent\"b1\"isPrivate\"b1\"isSensitive\"b1\"keyClass\"b1\"wasAlwaysSensitive\"b1\"wasNeverExtractable\"b1}"
- "\x01.\x14"
- "\x01U"
- "\x02\x14\""
- "\x0f\a"
- "%@ engine unknown coder state: %d"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Unwrapped DER backup bag%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
- "-[CuttlefishXPCWrapper attemptPreapprovedJoinWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper establishWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper fetchRecoverableTLKSharesWithSpecificUser:peerID:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper preflightVouchWithBottleWithSpecificUser:bottleID:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper vouchWithBottleWithSpecificUser:bottleID:entropy:bottleSalt:tlkShares:reply:]_block_invoke"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "<CKKSZoneStateEntry[%@](%@): created:%@ subscribed:%@ moreRecords:%@>"
- "@84@0:8@16@24B32B36@40B48@52@60Q68@76"
- "AppleKeyStore"
- "IOService:/IOResources/AppleKeyStore"
- "KCSharingInternetPasswordCredential(sharingGroup:%@ accessGroup:%@ account:%@ protocol:%@ server:%@ port:%@ path:%@ authenticationType:%@ creationDate:%@ modificationDate:%@ comment:%@ label:%@ accessibility:%@ viewHint:%@ securityDomain:%@)"
- "KCSharingPrivateKeyCredential(sharingGroup:%@ accessGroup:%@ keyType:%ld applicationTag:%@ label:%@ applicationLabel:%@ keySizeInBits:%ld effectiveKeySize:%ld creationDate:%@ modificationDate:%@)"
- "Primary key conflict; deleting incoming CK item (%@)%{private}@in favor of old item (%@)%{private}@"
- "REQUIRE_func"
- "UUID of olditem (%@) is higher than UUID of incoming item (%@), issuing deletion of olditem: %{private}@"
- "_aks_operation"
- "_get_device_state"
- "_get_prederived_configuration"
- "_merge_dict_cb"
- "account state unknown"
- "aks-client-queue"
- "aks_assert_drop"
- "aks_assert_hold"
- "aks_generation"
- "aks_get_bag_uuid"
- "aks_get_lock_state"
- "aks_get_system"
- "aks_kc_backup_get_uuid"
- "aks_kc_backup_open_keybag"
- "aks_kc_backup_unwrap_key"
- "aks_kc_backup_wrap_key"
- "aks_load_bag"
- "aks_unload_bag"
- "aks_unlock_bag"
- "aks_unwrap_key"
- "aks_wrap_key"
- "attemptPreapprovedJoinWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:reply:"
- "could not determine"
- "der_key_validate"
- "establishWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:reply:"
- "failed to open connection to %s\n"
- "fetchRecoverableTLKShares:peerID:contextID:reply:"
- "fetchRecoverableTLKSharesWithSpecificUser:peerID:reply:"
- "initWithContextID:zoneName:zoneCreated:zoneSubscribed:changeToken:moreRecordsInCloudKit:lastFetch:lastScan:lastFixup:encodedRateLimiter:"
- "invalid transaction type %d"
- "ks_decrypt_data: invalid version %d"
- "logged in"
- "logged out"
- "preflightVouchWithBottleWithSpecificUser:bottleID:reply:"
- "proceedWithPeerID:refetchWasNeeded:"
- "proceedWithPendingTLKShares:"
- "restricted"
- "stringFromAccountStatus:"
- "v40@0:8@\"TPSpecificUser\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"TPSpecificUser\"16@\"NSString\"24@?<v@?@\"NSString\"@\"TPSyncingPolicy\"B@\"NSError\">32"
- "v48@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v56@0:8@\"TPSpecificUser\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">48"
- "v64@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40@\"NSArray\"48@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">56"
- "vouchWithBottleWithSpecificUser:bottleID:entropy:bottleSalt:tlkShares:reply:"
- "{?=\"creationDate\"b1\"effectiveKeySize\"b1\"keySizeInBits\"b1\"keyType\"b1\"modificationDate\"b1}"
- "{?=\"creationDate\"b1\"modificationDate\"b1\"port\"b1}"

```
