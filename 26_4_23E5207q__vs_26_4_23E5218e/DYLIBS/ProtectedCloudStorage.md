## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-1188.100.57.0.0
-  __TEXT.__text: 0x6b494
+1188.100.65.0.0
+  __TEXT.__text: 0x6d9ec
   __TEXT.__auth_stubs: 0x1930
-  __TEXT.__objc_methlist: 0x1fd8
+  __TEXT.__objc_methlist: 0x2020
   __TEXT.__const: 0x3a8
-  __TEXT.__cstring: 0xda5b
-  __TEXT.__oslogstring: 0x34ab
-  __TEXT.__gcc_except_tab: 0x33f8
+  __TEXT.__cstring: 0xdb81
+  __TEXT.__oslogstring: 0x3b10
+  __TEXT.__gcc_except_tab: 0x3700
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x1880
+  __TEXT.__unwind_info: 0x18b0
   __TEXT.__objc_classname: 0x326
-  __TEXT.__objc_methname: 0x531b
+  __TEXT.__objc_methname: 0x554a
   __TEXT.__objc_methtype: 0x15ef
-  __TEXT.__objc_stubs: 0x42e0
-  __DATA_CONST.__got: 0x618
-  __DATA_CONST.__const: 0x2c80
+  __TEXT.__objc_stubs: 0x4440
+  __DATA_CONST.__got: 0x658
+  __DATA_CONST.__const: 0x2d60
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15f8
+  __DATA_CONST.__objc_selrefs: 0x1650
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x41e8
   __AUTH_CONST.__auth_got: 0xca8
-  __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0x183c0
-  __AUTH_CONST.__objc_const: 0x3800
+  __AUTH_CONST.__const: 0x960
+  __AUTH_CONST.__cfstring: 0x184a0
+  __AUTH_CONST.__objc_const: 0x3890
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0x280
-  __AUTH.__data: 0x2d0
-  __DATA.__objc_ivar: 0x290
-  __DATA.__data: 0x900
+  __AUTH.__data: 0x2e0
+  __DATA.__objc_ivar: 0x29c
+  __DATA.__data: 0x908
   __DATA.__bss: 0x330
-  __DATA.__common: 0x30
+  __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x10b8
   __DATA_DIRTY.__bss: 0xf0

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7EE50F3D-9823-3B38-8860-0F07A75148F3
-  Functions: 2068
-  Symbols:   6297
-  CStrings:  8033
+  UUID: AC97C25B-5E9F-33F1-9EAB-CDACBD1E0873
+  Functions: 2103
+  Symbols:   6393
+  CStrings:  8089
 
Symbols:
+ -[PCSMigrationState fallbackSerializedEscrowRecord]
+ -[PCSMigrationState lrcFedSerializedEscrowRecord]
+ -[PCSMigrationState lrcSerializedEscrowRecord]
+ -[PCSMigrationState primarySerializedEscrowRecord]
+ -[PCSMigrationState setFallbackSerializedEscrowRecord:]
+ -[PCSMigrationState setLrcFedSerializedEscrowRecord:]
+ -[PCSMigrationState setLrcSerializedEscrowRecord:]
+ -[PCSMigrationState setPrimarySerializedEscrowRecord:]
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table174
+ GCC_except_table189
+ GCC_except_table211
+ GCC_except_table215
+ GCC_except_table226
+ GCC_except_table230
+ GCC_except_table242
+ GCC_except_table247
+ GCC_except_table252
+ GCC_except_table256
+ GCC_except_table285
+ _CreateFallbackUpdateDict
+ _CreateLRCFedUpdateDict
+ _CreateLRCUpdateDict
+ _CreateSHA256Hash
+ _NowAsString
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_IVAR_$_PCSMigrationState._fallbackSerializedEscrowRecord
+ _OBJC_IVAR_$_PCSMigrationState._lrcFedSerializedEscrowRecord
+ _OBJC_IVAR_$_PCSMigrationState._lrcSerializedEscrowRecord
+ _OBJC_IVAR_$_PCSMigrationState._primarySerializedEscrowRecord
+ _PCSEngineStoreLRCHSM
+ _PCSEngineStoreLRCHSM.cold.1
+ _PCSEngineStoreLRCHSM.cold.2
+ _PCSEngineStoreLRCHSM.cold.3
+ _PCSEngineStoreLRCHSM.cold.4
+ _PCSEngineStoreLRCHSM.cold.5
+ _PCSEngineStoreLRCHSM.cold.6
+ _PCSEngineStoreLRCHSM.cold.7
+ _SecureBackupWrapDataToFedKey
+ __PCSSecureBackupWrapDataToFedKey
+ ___CreateLRCFedUpdateDict_block_invoke
+ ___EnsureLRCKeysExist_block_invoke
+ ___EnsureLRCKeysExist_block_invoke.908
+ ___PCSDBRValidateIdentities_block_invoke.362
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.958
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.959
+ ___PCSEngineExtractKeys_block_invoke.685
+ ___PCSEngineExtractKeys_block_invoke.696
+ ___PCSEngineStoreHSM_block_invoke.835
+ ___PCSEngineStoreHSM_block_invoke.836
+ ___PCSEngineStoreHSM_block_invoke.840
+ ___PCSEngineStoreLRCHSM_block_invoke
+ ___PCSEngineStoreLRCHSM_block_invoke.906
+ ___PCSEngineStoreLRCHSM_block_invoke.907
+ ___PCSIdentityOptionsToMetaMapping
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.639
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.639.cold.1
+ ___block_descriptor_48_e8_32s40r_e61_v48?0"NSData"8"NSData"16"NSData"24"NSData"32"NSError"40ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e28_v24?0"NSData"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e34_v24?0^{__CFData=}8^{__CFError=}16ls32l8r48l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e40_v24?0^{__CFDictionary=}8^{__CFError=}16ls32l8s40l8r56l8s48l8
+ ___block_literal_global.1187
+ ___block_literal_global.389
+ ___block_literal_global.441
+ ___block_literal_global.444
+ ___block_literal_global.886
+ ___connectionPCSKeySyncing_block_invoke.439
+ ___connectionPCSKeySyncing_block_invoke.442
+ _kPCSEscrowServiceLRCNotAvailable
+ _kSecureBackupFallBackSRKey
+ _kSecureBackupKeybagLRCFedRecordKey
+ _kSecureBackupKeybagLRCFedSHA256Key
+ _kSecureBackupLRCFedKey
+ _kSecureBackupLRCKey
+ _kSecureBackupTimestampKey
+ _objc_msgSend$fallbackSerializedEscrowRecord
+ _objc_msgSend$label
+ _objc_msgSend$lrcFedSerializedEscrowRecord
+ _objc_msgSend$lrcSerializedEscrowRecord
+ _objc_msgSend$now
+ _objc_msgSend$primarySerializedEscrowRecord
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setFallbackSerializedEscrowRecord:
+ _objc_msgSend$setIsGuitarfish:
+ _objc_msgSend$setLrcFedSerializedEscrowRecord:
+ _objc_msgSend$setLrcSerializedEscrowRecord:
+ _objc_msgSend$setPrimarySerializedEscrowRecord:
+ _objc_msgSend$stringFromDate:
- -[PCSMigrationState serializedEscrowRecord]
- -[PCSMigrationState setSerializedEscrowRecord:]
- GCC_except_table149
- GCC_except_table157
- GCC_except_table167
- GCC_except_table181
- GCC_except_table203
- GCC_except_table208
- GCC_except_table212
- GCC_except_table224
- GCC_except_table228
- GCC_except_table233
- GCC_except_table237
- GCC_except_table266
- _OBJC_IVAR_$_PCSMigrationState._serializedEscrowRecord
- ___PCSDBRValidateIdentities_block_invoke.364
- ___PCSEngineAddMissingCurrentPointers_block_invoke.933
- ___PCSEngineAddMissingCurrentPointers_block_invoke.936
- ___PCSEngineExtractKeys_block_invoke.670
- ___PCSEngineExtractKeys_block_invoke.681
- ___PCSEngineStoreHSM_block_invoke.817
- ___PCSEngineStoreHSM_block_invoke.818
- ___PCSEngineStoreHSM_block_invoke.822
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.624
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.624.cold.1
- ___block_literal_global.1147
- ___block_literal_global.363
- ___block_literal_global.391
- ___block_literal_global.443
- ___block_literal_global.446
- ___block_literal_global.868
- ___connectionPCSKeySyncing_block_invoke.441
- ___connectionPCSKeySyncing_block_invoke.444
- _objc_msgSend$serializedEscrowRecord
- _objc_msgSend$setSerializedEscrowRecord:
CStrings:
+ "DBR_TWO Feature flag off, exiting storeHSM"
+ "Failed to get serialized plist escrow record from CloudServices"
+ "Pre-records to be passed in for ADP disablement: %@"
+ "StoreLRCHSM"
+ "T@\"OTSerializedPlistEscrowRecord\",&,V_fallbackSerializedEscrowRecord"
+ "T@\"OTSerializedPlistEscrowRecord\",&,V_lrcFedSerializedEscrowRecord"
+ "T@\"OTSerializedPlistEscrowRecord\",&,V_lrcSerializedEscrowRecord"
+ "T@\"OTSerializedPlistEscrowRecord\",&,V_primarySerializedEscrowRecord"
+ "_PCSSecureBackupWrapDataToFedKey: %@"
+ "_fallbackSerializedEscrowRecord"
+ "_lrcFedSerializedEscrowRecord"
+ "_lrcSerializedEscrowRecord"
+ "_primarySerializedEscrowRecord"
+ "fallbackSerializedEscrowRecord"
+ "incomplete password metadata"
+ "lrcFedSerializedEscrowRecord"
+ "lrcSerializedEscrowRecord"
+ "primarySerializedEscrowRecord"
+ "setDateFormat:"
+ "setFallbackSerializedEscrowRecord:"
+ "setIsGuitarfish:"
+ "setLrcFedSerializedEscrowRecord:"
+ "setLrcSerializedEscrowRecord:"
+ "setPrimarySerializedEscrowRecord:"
+ "storeLRCHSM: Attempting to write LRC Record"
+ "storeLRCHSM: DBR FF is off, skipping storeLRCHSM"
+ "storeLRCHSM: DBR Record does not contain LRC hashes, in need of repair"
+ "storeLRCHSM: Didn't get a serialized escrow record for Fallback Stingray Record, quitting"
+ "storeLRCHSM: Didn't get a serialized escrow record for LRC Fed Record, quitting"
+ "storeLRCHSM: Didn't get a serialized escrow record for LRC Record"
+ "storeLRCHSM: Failed to enroll Fallback Stingray Record: %@"
+ "storeLRCHSM: Failed to enroll LRC Fed Record, quitting: %@"
+ "storeLRCHSM: Failed to enroll LRC Record, quitting: %@"
+ "storeLRCHSM: LRC Record(s) need recreation, ensuring that we have LRC keys in memory..."
+ "storeLRCHSM: LRC key hash in existing LRC record matches our DBR Record, nothing to be done."
+ "storeLRCHSM: LRC record enrollment attempt got error indicating LRC club is not available, checking state of Fallback Stingray & LRC Fed Record: %@"
+ "storeLRCHSM: Not an active DBR account, skipping storeLRCHSM"
+ "storeLRCHSM: Nothing needed to be done, both LRC key and Fallback key hashes in existing records match our DBR Record!"
+ "storeLRCHSM: Re-creating Fallback Stingray Record"
+ "storeLRCHSM: Re-creating LRC Fed Record"
+ "storeLRCHSM: Recovered wrapping key from keychain"
+ "storeLRCHSM: Successfully enrolled Fallback Stingray Record"
+ "storeLRCHSM: Successfully enrolled LRC Fed Record"
+ "storeLRCHSM: Successfully enrolled LRC Record"
+ "storeLRCHSM: could not recover existing DBR record with wrapping key: %@"
+ "storeLRCHSM: couldn't get LRC keys in memory, quitting: %@"
+ "storeLRCHSM: no DBR record, in need of repair"
+ "storeLRCHSM: recovered keys from existing record"
+ "storeLRCHSM: unable to recover wrapping key from keychain: %@"
+ "stringFromDate:"
+ "yyyy-MM-dd'T'HH:mm:ss.SSSZ"
+ "\xf0i"
- "T@\"OTSerializedPlistEscrowRecord\",&,V_serializedEscrowRecord"
- "_serializedEscrowRecord"
- "serializedEscrowRecord"
- "setSerializedEscrowRecord:"
- "\xf0f"

```
