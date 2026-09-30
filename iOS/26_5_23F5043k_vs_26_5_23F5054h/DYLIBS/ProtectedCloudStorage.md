## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-1188.120.23.0.0
-  __TEXT.__text: 0x6e60c
+1188.120.32.0.0
+  __TEXT.__text: 0x6f3cc
   __TEXT.__auth_stubs: 0x1940
-  __TEXT.__objc_methlist: 0x2008
-  __TEXT.__const: 0x3c0
-  __TEXT.__cstring: 0xddc9
-  __TEXT.__oslogstring: 0x3cf2
-  __TEXT.__gcc_except_tab: 0x379c
+  __TEXT.__objc_methlist: 0x2020
+  __TEXT.__const: 0x3c8
+  __TEXT.__cstring: 0xe080
+  __TEXT.__oslogstring: 0x3d93
+  __TEXT.__gcc_except_tab: 0x38d8
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x18c8
+  __TEXT.__unwind_info: 0x1908
   __TEXT.__objc_classname: 0x326
-  __TEXT.__objc_methname: 0x5555
-  __TEXT.__objc_methtype: 0x15e4
-  __TEXT.__objc_stubs: 0x4460
-  __DATA_CONST.__got: 0x660
-  __DATA_CONST.__const: 0x2d60
+  __TEXT.__objc_methname: 0x556e
+  __TEXT.__objc_methtype: 0x15ef
+  __TEXT.__objc_stubs: 0x4440
+  __DATA_CONST.__got: 0x678
+  __DATA_CONST.__const: 0x2e50
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1658
+  __DATA_CONST.__objc_selrefs: 0x1650
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x41e8
+  __DATA_CONST.__objc_arraydata: 0x4240
   __AUTH_CONST.__auth_got: 0xcb0
   __AUTH_CONST.__const: 0x960
-  __AUTH_CONST.__cfstring: 0x18680
-  __AUTH_CONST.__objc_const: 0x3860
+  __AUTH_CONST.__cfstring: 0x18920
+  __AUTH_CONST.__objc_const: 0x3890
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x2e0
-  __DATA.__objc_ivar: 0x298
+  __DATA.__objc_ivar: 0x29c
   __DATA.__data: 0x908
   __DATA.__bss: 0x330
-  __DATA.__common: 0x38
+  __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x870
-  __DATA_DIRTY.__data: 0x10d8
+  __DATA_DIRTY.__data: 0x10f8
   __DATA_DIRTY.__bss: 0xf0
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7A9C091F-8BCE-3ED3-AC31-975EB63A0140
-  Functions: 2101
-  Symbols:   6393
-  CStrings:  8125
+  UUID: 88E9A53A-5B02-3315-9048-379C0BB9235F
+  Functions: 2111
+  Symbols:   6427
+  CStrings:  8174
 
Symbols:
+ -[PCSMigrationState fdeSet]
+ -[PCSMigrationState setFdeSet:]
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table166
+ GCC_except_table171
+ GCC_except_table181
+ GCC_except_table196
+ GCC_except_table220
+ GCC_except_table231
+ GCC_except_table243
+ GCC_except_table249
+ GCC_except_table258
+ GCC_except_table266
+ GCC_except_table289
+ _OBJC_IVAR_$_PCSMigrationState._fdeSet
+ _PCSDBRValidateIdentities.cold.1
+ _PCSEngineExtractFDE
+ _SecureBackupGetFedCert
+ _SetExtraMetadataForDBRRecord
+ _SetExtraMetadataForDBRRecord.cold.1
+ _SetExtraMetadataForDBRRecord.cold.2
+ __PCSDBRGetWrappingKey
+ __PCSDBRGetWrappingKey.cold.1
+ ___EnsureLRCKeysExist_block_invoke.968
+ ___FDECreateIdentitySetFromWrappedKeys_block_invoke
+ ___PCSCopyHSMData.cold.3
+ ___PCSDBRRepairIdentities_block_invoke.349
+ ___PCSDBRSetupIdentities_block_invoke.354
+ ___PCSDBRValidateIdentities_block_invoke.363
+ ___PCSDBRValidateIdentities_block_invoke.364
+ ___PCSDBRValidateIdentities_block_invoke.365
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.1022
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.1023
+ ___PCSEngineExtractFDE_block_invoke
+ ___PCSEngineExtractKeys_block_invoke.718
+ ___PCSEngineExtractKeys_block_invoke.729
+ ___PCSEngineStoreHSM_block_invoke.890
+ ___PCSEngineStoreHSM_block_invoke.891
+ ___PCSEngineStoreHSM_block_invoke.892
+ ___PCSEngineStoreHSM_block_invoke.896
+ ___PCSEngineStoreHSM_block_invoke.912
+ ___PCSEngineStoreHSM_block_invoke_2.cold.1
+ ___PCSGetFedCert
+ ___PCSIdentityRecoverFDE_block_invoke
+ ____PCSDBRGetWrappingKey_block_invoke
+ ____PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke
+ ____PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.201
+ ____PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.203
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.672
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.672.cold.1
+ _____PCSDeleteGuitarfishTokenRecord_block_invoke.54
+ _____PCSGetFedCert_block_invoke
+ ___block_descriptor_48_e8_32r40r_e27_v24?0"NSData"8"NSData"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e34_v40?0"NSData"8q16q24"NSError"32lr40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e28_v24?0"NSData"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48r_e17_v16?0"NSError"8lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32r40r48r_e34_v40?0"NSData"8q16q24"NSError"32lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e34_v40?0"NSData"8q16q24"NSError"32lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e34_v40?0"NSData"8q16q24"NSError"32ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40r48r56r_e34_v40?0"NSData"8q16q24"NSError"32lr40l8r48l8r56l8s32l8
+ ___block_descriptor_64_e8_32s40r_e34_v24?0^{__CFData=}8^{__CFError=}16lr40l8s32l8
+ ___block_literal_global.1230
+ ___block_literal_global.356
+ ___block_literal_global.395
+ ___block_literal_global.450
+ ___block_literal_global.944
+ ___connectionPCSKeySyncing_block_invoke.448
+ _kSecureBackupContainsFDEiCloudIdentityKey
+ _kSecureBackupFDEMetadataKey
+ _kSecureBackupKeybagFDESHA256Key
+ _kSecureBackupLRCRecordFedHashKey
+ _objc_msgSend$fdeSet
+ _objc_msgSend$setFdeSet:
- GCC_except_table154
- GCC_except_table155
- GCC_except_table162
- GCC_except_table167
- GCC_except_table177
- GCC_except_table192
- GCC_except_table215
- GCC_except_table227
- GCC_except_table239
- GCC_except_table245
- GCC_except_table250
- GCC_except_table283
- GCC_except_table9
- _NowAsString
- _OBJC_CLASS_$_NSDateFormatter
- _PCSDBRRepairWrappingKeyFromEscrowIdentity
- _PCSEngineStoreLRCHSM.cold.10
- __PCSDBRGetKeychainItem
- __PCSDBRGetKeychainItem.cold.1
- ___EnsureLRCKeysExist_block_invoke.950
- ___PCSDBRRepairIdentities_block_invoke.346
- ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke
- ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.100
- ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.105
- ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.107
- ___PCSDBRSetupIdentities_block_invoke.353
- ___PCSDBRValidateIdentities_block_invoke.359
- ___PCSDBRValidateIdentities_block_invoke.360
- ___PCSDBRValidateIdentities_block_invoke.361
- ___PCSDBRValidateIdentities_block_invoke.362
- ___PCSEngineAddMissingCurrentPointers_block_invoke.1003
- ___PCSEngineAddMissingCurrentPointers_block_invoke.1004
- ___PCSEngineExtractKeys_block_invoke.705
- ___PCSEngineExtractKeys_block_invoke.716
- ___PCSEngineStoreHSM_block_invoke.877
- ___PCSEngineStoreHSM_block_invoke.878
- ___PCSEngineStoreHSM_block_invoke.879
- ___PCSEngineStoreHSM_block_invoke.883
- ___PCSEngineStoreHSM_block_invoke_3
- ___PCSEngineStoreHSM_block_invoke_3.cold.1
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.659
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.659.cold.1
- _____PCSDeleteGuitarfishTokenRecord_block_invoke.53
- ___block_descriptor_48_e8_32s40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e23_v32?0q8q16"NSError"24lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e28_v24?0"NSData"8"NSError"16ls32l8r48l8s40l8
- ___block_literal_global.1224
- ___block_literal_global.355
- ___block_literal_global.392
- ___block_literal_global.444
- ___block_literal_global.929
- ___connectionPCSKeySyncing_block_invoke.442
- _kSecureBackupTimestampKey
- _objc_msgSend$now
- _objc_msgSend$setDateFormat:
- _objc_msgSend$stringFromDate:
CStrings:
+ "1<<18"
+ "1<<19"
+ "1<<20"
+ "1<<21"
+ "1<<22"
+ "1<<23"
+ "1<<24"
+ "1<<25"
+ "Adding additional metadata key hashes to DBR record"
+ "Cannot generate a PDP password change blob when walrus is on"
+ "Couldn't generate a PDP blob for password change"
+ "CreateLRCFedUpdateDict: Errored on obtaining fed cert hash: %@"
+ "Current DBR State: %lu"
+ "ExtractFDE"
+ "FDECreateIdentitySetFromWrappedKeys: %@"
+ "Failed to get federation cert on device: %@"
+ "Failed to store FDE record in keychain: %@"
+ "FlagFallbackRecordExistsWithWalrusOn"
+ "FlagLRCFedRecordExistsWithWalrusOn"
+ "FlagLRCRecordExistsWithWalrusOn"
+ "GetFedCertHash: fedCertHash: %@"
+ "Hash mismatch for keychain copy of FDE record"
+ "In modified path + walrus, not setting IDMS password metadata"
+ "In new identity path + walrus, not setting IDMS password metadata"
+ "LRC records exist in account even though Walrus is on"
+ "Not an DBR account (%lu)"
+ "PCSDBRValidateIdentities: Not an DBR account (%lu)"
+ "PCSDBRValidateIdentities: state %lu - (fallbackStingray, lrcFed, lrc) = (%{BOOL}d, %{BOOL}d, %{BOOL}d)"
+ "Q24@0:8@16"
+ "Stingray recovery failed, but FDE recovery succeeded."
+ "T^{_PCSIdentitySetData=},V_fdeSet"
+ "_fdeSet"
+ "fdeSet"
+ "setFdeSet:"
+ "storeLRCHSM: Not an active DBR account (%lu), skipping storeLRCHSM"
+ "storeLRCHSM: state %lu - (fallbackStingray, lrcFed, lrc) = (%{BOOL}d, %{BOOL}d, %{BOOL}d)"
+ "unrecognized AKPDPState value: %lu"
+ "v24@?0@\"NSData\"8@\"NSData\"16"
+ "v40@?0@\"NSData\"8q16q24@\"NSError\"32"
+ "\xf0x"
- "Current DBR State: %d"
- "Not an DBR account (%d)"
- "PCSDBRValidateIdentities: Not an DBR account (%d)"
- "PCSDBRValidateIdentities: state %d - (fallbackStingray, lrcFed, lrc) = (%{BOOL}d, %{BOOL}d, %{BOOL}d)"
- "setDateFormat:"
- "storeLRCHSM: DBR Record does not contain LRC hashes, in need of repair"
- "storeLRCHSM: Not an active DBR account (%d), skipping storeLRCHSM"
- "storeLRCHSM: state %d - (fallbackStingray, lrcFed, lrc) = (%{BOOL}d, %{BOOL}d, %{BOOL}d)"
- "stringFromDate:"
- "unrecognized PDPState value: %lu"
- "yyyy-MM-dd'T'HH:mm:ss.SSSZ"
- "\xf0h"

```
