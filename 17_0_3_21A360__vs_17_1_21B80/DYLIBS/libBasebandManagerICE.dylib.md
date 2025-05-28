## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

```diff

-977.0.0.0.0
-  __TEXT.__text: 0x1d5524
-  __TEXT.__auth_stubs: 0x2fc0
-  __TEXT.__init_offsets: 0x100
+986.0.0.0.0
+  __TEXT.__text: 0x1d621c
+  __TEXT.__auth_stubs: 0x2ff0
+  __TEXT.__init_offsets: 0x104
   __TEXT.__objc_methlist: 0x1a8
-  __TEXT.__const: 0xbcb9
-  __TEXT.__gcc_except_tab: 0x2d458
-  __TEXT.__oslogstring: 0x989a
-  __TEXT.__cstring: 0x64e8
-  __TEXT.__unwind_info: 0x8e84
+  __TEXT.__const: 0xbcf9
+  __TEXT.__gcc_except_tab: 0x2d5d0
+  __TEXT.__oslogstring: 0x9ac5
+  __TEXT.__cstring: 0x64fa
+  __TEXT.__unwind_info: 0x8eb0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methname: 0xdd6
   __TEXT.__objc_methtype: 0xa42
   __TEXT.__objc_stubs: 0xc00
-  __DATA_CONST.__got: 0x1c50
+  __DATA_CONST.__got: 0x1c58
   __DATA_CONST.__const: 0x1990
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18

   __AUTH_CONST.__cfstring: 0x5e0
   __AUTH_CONST.__objc_const: 0x168
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x17f0
+  __AUTH_CONST.__auth_got: 0x1808
   __AUTH.__const_weak: 0xc50
   __AUTH.__objc_data: 0xa0
   __DATA.__got_weak: 0x7b0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper
+  - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager
   - /System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater
   - /System/Library/PrivateFrameworks/ApplePDPHelper.framework/ApplePDPHelper

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5631
-  Symbols:   15985
-  CStrings:  2169
+  Functions: 5638
+  Symbols:   16003
+  CStrings:  2186
 
Symbols:
+ GCC_except_table167
+ GCC_except_table177
+ GCC_except_table184
+ GCC_except_table187
+ GCC_except_table189
+ GCC_except_table194
+ _APFSVolumeNeedsCryptoMigration
+ _APFSVolumeRole
+ __ZN3abm8kUnknownE
+ __ZN4util4apfs24is_transcription_pendingEv
+ __ZNK3ctu14SharedLockableI10SharedDataE12execute_syncIZNS1_13setPreferenceIPK14__CFDictionaryEEbRKNSt3__112basic_stringIcNS8_11char_traitsIcEENS8_9allocatorIcEEEET_EUlvE_EENS8_5decayIDTclfp_EEE4typeEOSH_
+ __ZNK3ctu14SharedLockableI10SharedDataE12execute_syncIZNS1_13setPreferenceIiEEbRKNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEET_EUlvE_EENS5_5decayIDTclfp_EEE4typeEOSE_
+ __ZNSt3__110shared_ptrI10SharedDataEC2IS1_vEEPT_
+ __ZNSt3__110unique_ptrI10SharedDataNS_14default_deleteIS1_EEED1B7v160006Ev
+ ____ZN11RadioModule10initializeEN8dispatch13group_sessionE_block_invoke.27
+ ____ZN11RadioModule10initializeEN8dispatch13group_sessionE_block_invoke_2.26
+ ___block_descriptor_tmp.220
+ ___block_descriptor_tmp.224
+ ___block_descriptor_tmp.227
+ ___block_descriptor_tmp.230
+ ___block_descriptor_tmp.233
+ ___block_descriptor_tmp.236
+ ___block_descriptor_tmp.239
+ ___block_descriptor_tmp.248
+ ___block_descriptor_tmp.251
+ ___block_descriptor_tmp.254
+ ___block_descriptor_tmp.259
+ ___block_descriptor_tmp.272
+ ___block_descriptor_tmp.284
+ ___block_descriptor_tmp.285
+ ___block_literal_global.287
+ ___cxx_global_var_init.198
+ _statfs
- GCC_except_table165
- GCC_except_table176
- GCC_except_table182
- GCC_except_table188
- ____ZN11RadioModule10initializeEN8dispatch13group_sessionE_block_invoke.23
- ____ZN11RadioModule10initializeEN8dispatch13group_sessionE_block_invoke_2.24
- ___block_descriptor_tmp.219
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.231
- ___block_descriptor_tmp.237
- ___block_descriptor_tmp.240
- ___block_descriptor_tmp.243
- ___block_descriptor_tmp.246
- ___block_descriptor_tmp.249
- ___block_descriptor_tmp.252
- ___block_descriptor_tmp.255
- ___block_descriptor_tmp.270
- ___block_descriptor_tmp.283
- ___block_literal_global.285
CStrings:
+ "#D CoreMotion On Body Handler is empty"
+ "#D OBD manager is empty"
+ "#D hand detection manager is empty"
+ "#I APFS transcription is pending"
+ "#I Downgrading Baseband Reset MTBF metric because APFS transcription is pending"
+ "#I Set CoreMotion On Body Handler's motion parameter!"
+ "#I Setting OBD manager's motion parameter!"
+ "#I Setting hand detection manager's motion parameter!"
+ "/private/var"
+ "APFS needs crypto migration: %d"
+ "APFS volume role does not match"
+ "APFS volume role error: %d"
+ "AppleBasebandManager-AppleBasebandServices_Manager-986"
+ "AppleBasebandServices_Manager-986"
+ "Checking if disk requires APFS transcription"
+ "Failed to get ABM Shared Data"
+ "Failed to get mount point: %s"
+ "Failed to parse bitmask (current: 0x%x, received: 0x%x)"
+ "Failed to statfs: %s"
+ "Motion parameter is set!"
+ "Query APFS crypto migration error: %d"
+ "Query APFS crypto migration for volume: %s, %s"
+ "apfs"
- "#D SAR Helpers are already initialized"
- "#D Set CoreMotion On Body Handler's motion parameter!"
- "#D Setting OBD manager's motion parameter!"
- "#D Setting hand detection manager's motion parameter!"
- "AppleBasebandManager-AppleBasebandServices_Manager-977"
- "AppleBasebandServices_Manager-977"

```
