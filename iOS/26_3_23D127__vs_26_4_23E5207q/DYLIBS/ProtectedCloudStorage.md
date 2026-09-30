## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-1188.80.10.0.0
-  __TEXT.__text: 0x65818
-  __TEXT.__auth_stubs: 0x1950
-  __TEXT.__objc_methlist: 0x1e48
-  __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0xd673
-  __TEXT.__oslogstring: 0x3209
-  __TEXT.__gcc_except_tab: 0x3038
+1188.100.57.0.0
+  __TEXT.__text: 0x6b494
+  __TEXT.__auth_stubs: 0x1930
+  __TEXT.__objc_methlist: 0x1fd8
+  __TEXT.__const: 0x3a8
+  __TEXT.__cstring: 0xda5b
+  __TEXT.__oslogstring: 0x34ab
+  __TEXT.__gcc_except_tab: 0x33f8
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x1770
-  __TEXT.__objc_classname: 0x30c
-  __TEXT.__objc_methname: 0x4f8a
-  __TEXT.__objc_methtype: 0x15ce
-  __TEXT.__objc_stubs: 0x4020
-  __DATA_CONST.__got: 0x5d8
-  __DATA_CONST.__const: 0x2b88
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__unwind_info: 0x1880
+  __TEXT.__objc_classname: 0x326
+  __TEXT.__objc_methname: 0x531b
+  __TEXT.__objc_methtype: 0x15ef
+  __TEXT.__objc_stubs: 0x42e0
+  __DATA_CONST.__got: 0x618
+  __DATA_CONST.__const: 0x2c80
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1528
+  __DATA_CONST.__objc_selrefs: 0x15f8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0x41c0
-  __AUTH_CONST.__auth_got: 0xcb8
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x41e8
+  __AUTH_CONST.__auth_got: 0xca8
   __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0x18060
-  __AUTH_CONST.__objc_const: 0x3548
+  __AUTH_CONST.__cfstring: 0x183c0
+  __AUTH_CONST.__objc_const: 0x3800
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x230
-  __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x268
-  __DATA.__data: 0x8f0
+  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH.__objc_data: 0x280
+  __AUTH.__data: 0x2d0
+  __DATA.__objc_ivar: 0x290
+  __DATA.__data: 0x900
   __DATA.__bss: 0x330
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x870

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D8F6C5A8-B3B7-353D-BD65-0974A84511F0
-  Functions: 1931
-  Symbols:   5962
-  CStrings:  7908
+  UUID: 7EE50F3D-9823-3B38-8860-0F07A75148F3
+  Functions: 2068
+  Symbols:   6297
+  CStrings:  8033
 
Symbols:
+ -[PCSDBRRecordChangeBlob .cxx_destruct]
+ -[PCSDBRRecordChangeBlob copyTo:]
+ -[PCSDBRRecordChangeBlob copyWithZone:]
+ -[PCSDBRRecordChangeBlob currentMetadata]
+ -[PCSDBRRecordChangeBlob description]
+ -[PCSDBRRecordChangeBlob dictionaryRepresentation]
+ -[PCSDBRRecordChangeBlob hasCurrentMetadata]
+ -[PCSDBRRecordChangeBlob hasHsmBlob]
+ -[PCSDBRRecordChangeBlob hasOldMetadata]
+ -[PCSDBRRecordChangeBlob hash]
+ -[PCSDBRRecordChangeBlob hsmBlob]
+ -[PCSDBRRecordChangeBlob isEqual:]
+ -[PCSDBRRecordChangeBlob mergeFrom:]
+ -[PCSDBRRecordChangeBlob oldMetadata]
+ -[PCSDBRRecordChangeBlob readFrom:]
+ -[PCSDBRRecordChangeBlob setCurrentMetadata:]
+ -[PCSDBRRecordChangeBlob setHsmBlob:]
+ -[PCSDBRRecordChangeBlob setOldMetadata:]
+ -[PCSDBRRecordChangeBlob writeTo:]
+ -[PCSMigrationState .cxx_destruct]
+ -[PCSMigrationState dbrAESKey]
+ -[PCSMigrationState dbrWrappingKey]
+ -[PCSMigrationState escrowStoreAllowed]
+ -[PCSMigrationState existingEncodedMetadata]
+ -[PCSMigrationState fallbackAESKey]
+ -[PCSMigrationState lrcAESKey]
+ -[PCSMigrationState serializedEscrowRecord]
+ -[PCSMigrationState setDbrAESKey:]
+ -[PCSMigrationState setDbrWrappingKey:]
+ -[PCSMigrationState setEscrowStoreAllowed:]
+ -[PCSMigrationState setExistingEncodedMetadata:]
+ -[PCSMigrationState setFallbackAESKey:]
+ -[PCSMigrationState setLrcAESKey:]
+ -[PCSMigrationState setSerializedEscrowRecord:]
+ GCC_except_table103
+ GCC_except_table107
+ GCC_except_table113
+ GCC_except_table124
+ GCC_except_table143
+ GCC_except_table157
+ GCC_except_table167
+ GCC_except_table181
+ GCC_except_table203
+ GCC_except_table208
+ GCC_except_table212
+ GCC_except_table224
+ GCC_except_table228
+ GCC_except_table233
+ GCC_except_table237
+ GCC_except_table266
+ GCC_except_table40
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table62
+ GCC_except_table80
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table9
+ GCC_except_table95
+ GCC_except_table97
+ _GetEncodedMetadataFromSecureBackupInfo
+ _OBJC_CLASS_$_PCSDBRRecordChangeBlob
+ _OBJC_IVAR_$_PCSDBRRecordChangeBlob._currentMetadata
+ _OBJC_IVAR_$_PCSDBRRecordChangeBlob._hsmBlob
+ _OBJC_IVAR_$_PCSDBRRecordChangeBlob._oldMetadata
+ _OBJC_IVAR_$_PCSMigrationState._dbrAESKey
+ _OBJC_IVAR_$_PCSMigrationState._dbrWrappingKey
+ _OBJC_IVAR_$_PCSMigrationState._escrowStoreAllowed
+ _OBJC_IVAR_$_PCSMigrationState._existingEncodedMetadata
+ _OBJC_IVAR_$_PCSMigrationState._fallbackAESKey
+ _OBJC_IVAR_$_PCSMigrationState._lrcAESKey
+ _OBJC_IVAR_$_PCSMigrationState._serializedEscrowRecord
+ _OBJC_METACLASS_$_PCSDBRRecordChangeBlob
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _PCSAccountDisableWalrusDBR
+ _PCSAccountEnableWalrusDBR
+ _PCSAccountHealWalrusState
+ _PCSDBRCreateSetupParameters
+ _PCSDBRRecordChangeBlobReadFrom
+ _PCSEngineEvaluateOctagon.cold.1
+ _PCSEngineOTDisableWalrus
+ _PCSEngineOTEnableWalrus
+ _PCSEngineStoreHSM.cold.4
+ _PCSEngineStoreiCDPStatusNoWalrus
+ _PCSFPGetChainingSet
+ _PCSGenerateDBRBlob
+ _PCSIdentityGenerateBlobForPasswordChange
+ _SecureBackupEnableWithResults
+ _SecureBackupIsDBRTwoEnabled
+ __OBJC_$_INSTANCE_METHODS_PCSDBRRecordChangeBlob
+ __OBJC_$_INSTANCE_VARIABLES_PCSDBRRecordChangeBlob
+ __OBJC_$_PROP_LIST_PCSDBRRecordChangeBlob
+ __OBJC_CLASS_PROTOCOLS_$_PCSDBRRecordChangeBlob
+ __OBJC_CLASS_RO_$_PCSDBRRecordChangeBlob
+ __OBJC_METACLASS_RO_$_PCSDBRRecordChangeBlob
+ __OTCliqueForState
+ __PCSBackupDBREncodeInnerRecord
+ __PCSBackupDBREncodeOuterRecord
+ __PCSDBRWrapDataWithAESKey
+ __PCSDBRWrapKeyWithAESKey
+ __PCSIdentityDBROptionsToMetadata
+ __PCSIdentityMigrateDisableWalrusDBR
+ __PCSIdentityMigrateEnableWalrusDBR
+ __PCSSecureBackupEnableWithResults
+ ___PCSDBRRepairIdentities_block_invoke.344
+ ___PCSDBRRepairIdentities_block_invoke.345
+ ___PCSDBRRepairIdentities_block_invoke.346
+ ___PCSDBRRepairIdentities_block_invoke.347
+ ___PCSDBRRepairIdentities_block_invoke.348
+ ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.82
+ ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.87
+ ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.89
+ ___PCSDBRSetupIdentities_block_invoke.353
+ ___PCSDBRValidateIdentities_block_invoke.359
+ ___PCSDBRValidateIdentities_block_invoke.360
+ ___PCSDBRValidateIdentities_block_invoke.361
+ ___PCSDBRValidateIdentities_block_invoke.364
+ ___PCSDeleteDBRRecord
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.933
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.936
+ ___PCSEngineExtractKeys_block_invoke.670
+ ___PCSEngineExtractKeys_block_invoke.681
+ ___PCSEngineOTDisableWalrus_block_invoke
+ ___PCSEngineOTEnableWalrus_block_invoke
+ ___PCSEngineStoreHSM_block_invoke
+ ___PCSEngineStoreHSM_block_invoke.817
+ ___PCSEngineStoreHSM_block_invoke.818
+ ___PCSEngineStoreHSM_block_invoke.822
+ ___PCSEngineStoreHSM_block_invoke_3
+ ___PCSEngineStoreHSM_block_invoke_3.cold.1
+ ___PCSGuitarfishCreateSetupParameters_block_invoke.272
+ ___PCSGuitarfishRepairIdentities_block_invoke.235
+ ___PCSGuitarfishRepairIdentities_block_invoke.237
+ ___PCSGuitarfishRepairIdentities_block_invoke.247
+ ___PCSGuitarfishRepairIdentities_block_invoke.248
+ ___PCSGuitarfishRepairIdentities_block_invoke.249
+ ___PCSGuitarfishRepairIdentities_block_invoke.250
+ ___PCSGuitarfishSetupIdentities_block_invoke.288
+ ___PCSGuitarfishValidateIdentities_block_invoke.295
+ ___PCSGuitarfishValidateIdentities_block_invoke.296
+ ___PCSGuitarfishValidateIdentities_block_invoke.303
+ ___PCSGuitarfishValidateIdentities_block_invoke.307
+ ___PCSGuitarfishValidateIdentities_block_invoke.308
+ ___PCSGuitarfishValidateIdentities_block_invoke.315
+ ___PCSGuitarfishValidateIdentities_block_invoke.316
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.624
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.624.cold.1
+ _____PCSDeleteDBRRecord_block_invoke
+ _____PCSDeleteDBRRecord_block_invoke.33
+ _____PCSDeleteGuitarfishTokenRecord_block_invoke.35
+ ___block_descriptor_56_e8_32s40bs_e40_v24?0^{__CFDictionary=}8^{__CFError=}16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e40_v40?0q8q16"NSDictionary"24"NSError"32lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e61_v48?0"NSData"8"NSData"16"NSData"24"NSData"32"NSError"40ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e50_B48?0"NSString"8"NSString"16q24q32"NSString"40ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48r_e40_v24?0^{__CFDictionary=}8^{__CFError=}16ls32l8r48l8s40l8
+ ___block_descriptor_tmp.181
+ ___block_literal_global.1147
+ ___block_literal_global.183
+ ___block_literal_global.199
+ ___block_literal_global.214
+ ___block_literal_global.252
+ ___block_literal_global.290
+ ___block_literal_global.355
+ ___block_literal_global.363
+ ___block_literal_global.391
+ ___block_literal_global.443
+ ___block_literal_global.446
+ ___block_literal_global.868
+ ___connectionPCSKeySyncing_block_invoke.441
+ ___connectionPCSKeySyncing_block_invoke.444
+ _encode_PCSBackupDBRv2Escrow
+ _encode_PCSBackupDBRv2EscrowContents
+ _kPCSDBRTelemetryFallbackAttemptsRemaining
+ _kPCSDBRTelemetryLRCAttemptsRemaining
+ _kPCSDBRTelemetryLRCFedAttemptsRemaining
+ _kPCSSetupDBRPasswordChange
+ _kPCSSetupWalrusDBR
+ _kSecureBackupEncodedMetadataKey
+ _kSecureBackupFallbackStingrayMetadataKey
+ _kSecureBackupKeybagFallbackSHA256Key
+ _kSecureBackupKeybagLRCSHA256Key
+ _kSecureBackupLRCFedMetadataKey
+ _kSecureBackupLRCMetadataKey
+ _kSecureBackupReturnSerializedEscrowRecordKey
+ _kSecureBackupSerializedEscrowRecordKey
+ _length_PCSBackupDBRv2Escrow
+ _length_PCSBackupDBRv2EscrowContents
+ _migrateDisableWalrusDBR
+ _migrateEnableWalrusDBR
+ _objc_msgSend$blob
+ _objc_msgSend$ctx
+ _objc_msgSend$dbrAESKey
+ _objc_msgSend$dbrWrappingKey
+ _objc_msgSend$disableWalrus:preRecords:reply:
+ _objc_msgSend$enableWalrus:preRecords:reply:
+ _objc_msgSend$escrowStoreAllowed
+ _objc_msgSend$existingEncodedMetadata
+ _objc_msgSend$fallbackAESKey
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$lrcAESKey
+ _objc_msgSend$serializedEscrowRecord
+ _objc_msgSend$setCurrentMetadata:
+ _objc_msgSend$setDbrAESKey:
+ _objc_msgSend$setDbrWrappingKey:
+ _objc_msgSend$setEscrowStoreAllowed:
+ _objc_msgSend$setExistingEncodedMetadata:
+ _objc_msgSend$setFallbackAESKey:
+ _objc_msgSend$setHsmBlob:
+ _objc_msgSend$setLrcAESKey:
+ _objc_msgSend$setOldMetadata:
+ _objc_msgSend$setSerializedEscrowRecord:
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table102
- GCC_except_table106
- GCC_except_table119
- GCC_except_table125
- GCC_except_table129
- GCC_except_table131
- GCC_except_table139
- GCC_except_table142
- GCC_except_table163
- GCC_except_table179
- GCC_except_table184
- GCC_except_table188
- GCC_except_table200
- GCC_except_table204
- GCC_except_table56
- GCC_except_table57
- GCC_except_table60
- GCC_except_table75
- GCC_except_table78
- GCC_except_table81
- GCC_except_table84
- GCC_except_table90
- GCC_except_table92
- _PCSEngineExtractKeys.cold.8
- _SecureBackupEnableWithInfo
- __PCSSecureBackupEnableWithInfo
- ___PCSDBRRepairIdentities_block_invoke.317
- ___PCSDBRRepairIdentities_block_invoke.318
- ___PCSDBRRepairIdentities_block_invoke.319
- ___PCSDBRRepairIdentities_block_invoke.320
- ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.67
- ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.72
- ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.74
- ___PCSDBRSetupIdentities_block_invoke.322
- ___PCSDBRValidateIdentities_block_invoke.328
- ___PCSDBRValidateIdentities_block_invoke.329
- ___PCSDBRValidateIdentities_block_invoke.330
- ___PCSEngineAddMissingCurrentPointers_block_invoke.894
- ___PCSEngineAddMissingCurrentPointers_block_invoke.897
- ___PCSEngineExtractKeys_block_invoke.620
- ___PCSEngineExtractKeys_block_invoke.631
- ___PCSEngineStoreHSM_block_invoke.786
- ___PCSGuitarfishCreateSetupParameters_block_invoke.256
- ___PCSGuitarfishRepairIdentities_block_invoke.216
- ___PCSGuitarfishRepairIdentities_block_invoke.217
- ___PCSGuitarfishRepairIdentities_block_invoke.219
- ___PCSGuitarfishRepairIdentities_block_invoke.221
- ___PCSGuitarfishRepairIdentities_block_invoke.231
- ___PCSGuitarfishRepairIdentities_block_invoke.234
- ___PCSGuitarfishSetupIdentities_block_invoke.272
- ___PCSGuitarfishValidateIdentities_block_invoke.279
- ___PCSGuitarfishValidateIdentities_block_invoke.280
- ___PCSGuitarfishValidateIdentities_block_invoke.287
- ___PCSGuitarfishValidateIdentities_block_invoke.291
- ___PCSGuitarfishValidateIdentities_block_invoke.292
- ___PCSGuitarfishValidateIdentities_block_invoke.299
- ___PCSGuitarfishValidateIdentities_block_invoke.300
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.574
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.574.cold.1
- _____PCSDeleteGuitarfishTokenRecord_block_invoke.33
- ___block_descriptor_tmp.170
- ___block_literal_global.1095
- ___block_literal_global.172
- ___block_literal_global.185
- ___block_literal_global.198
- ___block_literal_global.236
- ___block_literal_global.274
- ___block_literal_global.324
- ___block_literal_global.332
- ___block_literal_global.337
- ___block_literal_global.389
- ___block_literal_global.392
- ___block_literal_global.830
- ___connectionPCSKeySyncing_block_invoke.387
- ___connectionPCSKeySyncing_block_invoke.390
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x6
CStrings:
+ "@\"OTSerializedPlistEscrowRecord\""
+ "B48@?0@\"NSString\"8@\"NSString\"16q24q32@\"NSString\"40"
+ "Couldn't generate new password change blob + metadata: %@"
+ "Error encoding outer record"
+ "Escrow identity not in escrowed set (in modified path)"
+ "Failed at encoding inner blob, error: %@"
+ "Failed at encoding outer blob, error: %@"
+ "Failed to delete DBR wrapping key from keychain: %@"
+ "Fallback record hash mismatch"
+ "Fallback stingray record is terminal, needs repair"
+ "FlagBadLRCRecord"
+ "GenerateBlob"
+ "LRC federation record hash mismatch"
+ "LRC federation record is terminal, needs repair"
+ "LRC record hash mismatch"
+ "LRC record is terminal, needs repair"
+ "MigrateDisableWalrusDBR"
+ "MigrateEnableWalrusDBR"
+ "OTDisableWalrus"
+ "OTEnableWalrus"
+ "PCSDBRRecordChangeBlob"
+ "Skipping StoreHSM in Silent DBR mode."
+ "StoreiCDPStatus"
+ "T@\"NSData\",&,N,V_currentMetadata"
+ "T@\"NSData\",&,N,V_hsmBlob"
+ "T@\"NSData\",&,N,V_oldMetadata"
+ "T@\"NSData\",&,V_dbrAESKey"
+ "T@\"NSData\",&,V_dbrWrappingKey"
+ "T@\"NSData\",&,V_existingEncodedMetadata"
+ "T@\"NSData\",&,V_fallbackAESKey"
+ "T@\"NSData\",&,V_lrcAESKey"
+ "T@\"OTSerializedPlistEscrowRecord\",&,V_serializedEscrowRecord"
+ "TB,V_escrowStoreAllowed"
+ "WalrusDBR"
+ "Writing inner blob"
+ "Writing new DBR Record"
+ "Writing outer blob"
+ "_PCSSecureBackupDisableWithInfo (DBR Record): %@"
+ "_PCSSecureBackupEnableWithResults: %@"
+ "__PCSDeleteDBRRecord"
+ "_currentMetadata"
+ "_dbrAESKey"
+ "_dbrWrappingKey"
+ "_escrowStoreAllowed"
+ "_existingEncodedMetadata"
+ "_fallbackAESKey"
+ "_hsmBlob"
+ "_lrcAESKey"
+ "_oldMetadata"
+ "_serializedEscrowRecord"
+ "blob"
+ "ctx"
+ "currentMetadata"
+ "dbrAESKey"
+ "dbrWrappingKey"
+ "disableWalrus:preRecords:reply:"
+ "enableWalrus:preRecords:reply:"
+ "encode PCSBackupDBREscrow"
+ "encode PCSBackupDBRv2EscrowContents"
+ "escrowStoreAllowed"
+ "existingEncodedMetadata"
+ "fallbackAESKey"
+ "fallbackRecordAttemptsRemaining"
+ "hasCurrentMetadata"
+ "hasHsmBlob"
+ "hasOldMetadata"
+ "hsmBlob"
+ "including previous classicContent for force-enroll"
+ "initWithBase64EncodedString:options:"
+ "kPCSSetupDBRPasswordChange"
+ "kPCSSetupWalrusDBR"
+ "lrcAESKey"
+ "lrcFedRecordAttemptsRemaining"
+ "lrcRecordAttemptsRemaining"
+ "oldMetadata"
+ "serializedEscrowRecord"
+ "setCurrentMetadata:"
+ "setDbrAESKey:"
+ "setDbrWrappingKey:"
+ "setEscrowStoreAllowed:"
+ "setExistingEncodedMetadata:"
+ "setFallbackAESKey:"
+ "setHsmBlob:"
+ "setLrcAESKey:"
+ "setOldMetadata:"
+ "setSerializedEscrowRecord:"
+ "storeHSM: Recovered wrapping key from keychain"
+ "storeHSM: could not recover existing DBR record with wrapping key, quitting to avoid data loss: %@"
+ "storeHSM: stashed wrapping key matches existing record"
+ "storeHSM: unable to recover wrapping key from keychain: %@"
+ "unable to create clique"
+ "unable to wrap DBRWrappingKey with DBRAESKey"
+ "unable to wrap DBRWrappingKey with Fallback Stingray Key"
+ "unable to wrap DBRWrappingKey with LRC AES Key"
+ "v40@?0q8q16@\"NSDictionary\"24@\"NSError\"32"
+ "\xf0f"
- "1<<2"
- "Skipping StoreHSM in DBR mode."
- "_PCSSecureBackupEnableWithInfo: %@"
- "manager:didFailVerificationWithError:"
- "managerDidFinishVerification:"

```
