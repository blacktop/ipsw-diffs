## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-1188.40.8.0.1
-  __TEXT.__text: 0x6432c
+1188.40.16.0.0
+  __TEXT.__text: 0x60c48
   __TEXT.__auth_stubs: 0x1950
-  __TEXT.__objc_methlist: 0x1e0c
+  __TEXT.__objc_methlist: 0x1e1c
   __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0xd68d
-  __TEXT.__oslogstring: 0x382c
-  __TEXT.__gcc_except_tab: 0x2d1c
+  __TEXT.__cstring: 0xd33e
+  __TEXT.__oslogstring: 0x348f
+  __TEXT.__gcc_except_tab: 0x2a04
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x16d0
+  __TEXT.__unwind_info: 0x1690
   __TEXT.__objc_classname: 0x30c
-  __TEXT.__objc_methname: 0x4f9a
+  __TEXT.__objc_methname: 0x4faf
   __TEXT.__objc_methtype: 0x1595
   __TEXT.__objc_stubs: 0x4080
   __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x28c8
+  __DATA_CONST.__const: 0x27d8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1528
+  __DATA_CONST.__objc_selrefs: 0x1530
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x4130
   __AUTH_CONST.__auth_got: 0xcb8
   __AUTH_CONST.__const: 0x940
-  __AUTH_CONST.__cfstring: 0x18080
+  __AUTH_CONST.__cfstring: 0x17e60
   __AUTH_CONST.__objc_const: 0x3510
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x230
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x264
-  __DATA.__data: 0x8e0
-  __DATA.__bss: 0x348
+  __DATA.__data: 0x8d8
+  __DATA.__bss: 0x330
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x10b8
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0xf0
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C48577F0-53C4-3723-B5EC-7033AF30DA69
-  Functions: 1897
-  Symbols:   5876
-  CStrings:  7935
+  UUID: FF282FC7-F08F-3566-AC26-977A9DD8DE45
+  Functions: 1880
+  Symbols:   5826
+  CStrings:  7880
 
Symbols:
+ -[PCSMigrationState recordTypeForReading]
+ GCC_except_table136
+ GCC_except_table154
+ GCC_except_table172
+ GCC_except_table177
+ GCC_except_table181
+ GCC_except_table193
+ GCC_except_table197
+ _PCSEngineEnsureClassicContent.cold.7
+ _PCSEngineStoreLocal.cold.2
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.844
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.847
+ ___PCSEngineExtractKeys_block_invoke.571
+ ___PCSEngineExtractKeys_block_invoke.582
+ ___PCSEngineStoreHSM_block_invoke.736
+ ___block_literal_global.1045
+ ___block_literal_global.780
+ _checkData.cold.1
+ _checkData.cold.2
+ _checkData.cold.3
+ _objc_msgSend$recordTypeForReading
- GCC_except_table119
- GCC_except_table127
- GCC_except_table137
- GCC_except_table147
- GCC_except_table161
- GCC_except_table183
- GCC_except_table190
- GCC_except_table194
- GCC_except_table206
- GCC_except_table210
- _OUTLINED_FUNCTION_16
- _PCSEngineExtractKeys.cold.7
- _PCSEngineExtractKeys.cold.8
- _PCSEngineStoreHSM.cold.4
- _PCSEngineStoreRTHSM.cold.1
- _PCSEngineStoreRTHSM.cold.2
- _PCSEngineStoreRTHSM.cold.3
- __PCSIdentityGuitarfishOptionsToMetadata
- __PCSMigrationRecoverPPasswordFromStashedKey
- __PCSMigrationStateIsGuitarfish
- ___PCSEngineAddMissingCurrentPointers_block_invoke.859
- ___PCSEngineAddMissingCurrentPointers_block_invoke.862
- ___PCSEngineExtractKeys_block_invoke.583
- ___PCSEngineExtractKeys_block_invoke.588
- ___PCSEngineExtractKeys_block_invoke.599
- ___PCSEngineStoreHSM_block_invoke
- ___PCSEngineStoreHSM_block_invoke.735
- ___PCSEngineStoreHSM_block_invoke.735.cold.1
- ___PCSEngineStoreHSM_block_invoke.742
- ___PCSEngineStoreHSM_block_invoke.750
- ___PCSEngineStoreHSM_block_invoke.786
- ___PCSEngineStoreHSM_block_invoke.786.cold.1
- ___PCSEngineStoreHSM_block_invoke_3
- ___PCSEngineStoreRTHSM_block_invoke
- ___PCSEngineStoreRTHSM_block_invoke.814
- ___PCSEngineStoreRTHSM_block_invoke.cold.1
- ___PCSIdentityOptionsToMetaMapping
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.547
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.547.cold.1
- ___block_descriptor_48_e8_32r_e39_v32?0"NSData"8"NSData"16"NSError"24lr32l8
- ___block_descriptor_48_e8_32s40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
- ___block_descriptor_56_e8_32r40r_e62_v48?0"NSData"8"NSArray"16"NSData"24"NSData"32"NSError"40lr32l8r40l8
- ___block_descriptor_56_e8_32s40s48s_e20_v16?0^{__CFError=}8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32r40r48r_e62_v48?0"NSData"8"NSArray"16"NSData"24"NSData"32"NSError"40lr32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40s48r56r_e61_v48?0"NSData"8"NSData"16"NSData"24"NSData"32"NSError"40lr48l8s32l8r56l8s40l8
- ___block_literal_global.1060
- ___block_literal_global.794
- _applyOptions.cold.1
- _kPCSServiceGuitarfishName
- _objc_msgSend$boolOption:
CStrings:
+ "PCSDBR"
+ "recordTypeForReading"
- "Creating RT Record: re-enroll: %d"
- "Error during PCSGuitarfishUnwrapKeys: %@"
- "Error unwrapping keys: %@"
- "Escrow identity not in escrowed set (in modified path)"
- "Failed to delete Guitarfish token record: %@"
- "No existing data, create one from the options stub"
- "Not guitarfish state, not unwrapping"
- "Primary Record PID: %@"
- "ProtectedCloudStorageGuitarfish"
- "RT Record Existing Federation: %@, Expected Federation: %@"
- "RT Record Federation Migration Needed"
- "RT Record PID does not match primary! deleting it so it can be recreated"
- "RT Record PID matches Primary Record PID"
- "RT Record PID: %@"
- "RT Record already exists"
- "RT Record is terminal, re-enroll needed"
- "Recovered p_password via stashed keychain wrappingKey by inner unwrap of record"
- "Setting new HSM content since it does not exist or is incorrect"
- "_PCSSecureBackupEnableWithInfo (Guitarfish recovery token): %@"
- "__PCSCopyHSMData failed"
- "copy of escrow data found in keychain"
- "error deriving p_token from p_recovery and mnemonic: %@"
- "escrow identity is %@"
- "including previous classicContent for force-enroll"
- "local escrow data invalid, replacing with contents from escrow: %@"
- "no template to create record from, must create record first through PCSGuitarfishSetupIdentities"
- "outer ASN contains mnemonic"
- "outer ASN contains p_recovery"
- "previous metadata blob does not exist, so creating a new one from the template"
- "recovered wrapping key from keychain"
- "sync: unable to get existing outerblob from metadata"
- "sync: unable to get wrappingKey from Keychain"
- "sync: unable to recover mnemonicArr from wrappingKey"
- "sync: unable to recover p_recovery from wrappingKey"
- "unable to derive pid"
- "unable to get wrappingKey from Keychain"
- "unable to unwrap inner unwrap: %@"
- "unsetting previous state.newHSMContent"
- "unwrapped PCSKeys in ExtractKeys successfully"
- "unwrappedKeys are %@"

```
