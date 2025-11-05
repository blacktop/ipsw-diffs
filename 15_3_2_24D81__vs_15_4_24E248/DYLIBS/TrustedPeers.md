## TrustedPeers

> `/System/Library/PrivateFrameworks/TrustedPeers.framework/Versions/A/TrustedPeers`

```diff

-61439.81.1.0.0
-  __TEXT.__text: 0x32d44
+61439.101.1.0.0
+  __TEXT.__text: 0x336ec
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0x34bc
+  __TEXT.__objc_methlist: 0x36ac
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0xa18
+  __TEXT.__gcc_except_tab: 0xa0c
   __TEXT.__cstring: 0xcc7
-  __TEXT.__oslogstring: 0x18f2
-  __TEXT.__unwind_info: 0xb90
+  __TEXT.__oslogstring: 0x18f1
+  __TEXT.__unwind_info: 0xb70
   __TEXT.__objc_classname: 0x4f8
-  __TEXT.__objc_methname: 0x6448
+  __TEXT.__objc_methname: 0x64c6
   __TEXT.__objc_methtype: 0xcfd
-  __TEXT.__objc_stubs: 0x4300
+  __TEXT.__objc_stubs: 0x4360
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1748
+  __DATA_CONST.__objc_selrefs: 0x17f8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x228
-  __AUTH_CONST.__const: 0x690
+  __AUTH_CONST.__const: 0x6c0
   __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x4fe0
+  __AUTH_CONST.__objc_const: 0x4ce8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf50
   __DATA.__objc_ivar: 0x2d8
-  __DATA.__data: 0x2b8
+  __DATA.__data: 0x2c0
   __DATA.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/SecurityFoundation.framework/Versions/A/SecurityFoundation
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77091A53-40A9-3F83-9D7C-E329D81E0DCE
-  Functions: 1204
-  Symbols:   2546
-  CStrings:  1817
+  UUID: F8A11F55-18B2-3960-B1EE-0FFC538100B0
+  Functions: 1207
+  Symbols:   2568
+  CStrings:  1823
 
Symbols:
+ -[TPCustodianRecoveryKey hash]
+ -[TPCustodianRecoveryKey isEqual:]
+ -[TPModel countOfDistrustedRecoveryKeys]
+ -[TPModel countTotalNumberOfRecoveryKeys]
+ -[TPModel countTotalTrustedCustodians]
+ GCC_except_table1158
+ GCC_except_table1166
+ GCC_except_table169
+ GCC_except_table176
+ GCC_except_table181
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table209
+ GCC_except_table215
+ GCC_except_table219
+ GCC_except_table221
+ GCC_except_table223
+ GCC_except_table230
+ GCC_except_table234
+ GCC_except_table236
+ GCC_except_table245
+ GCC_except_table248
+ GCC_except_table250
+ GCC_except_table321
+ _TPCheckHMACCount
+ _TPCheckSigCount
+ _TPCheckSignatureGenerationCount
+ _TPStartTrackingCheckSigCount
+ _TPStartTrackingHMACCount
+ _TPStartTrackingSignatureGenerationCount
+ _TPStopTrackingCheckSigCount
+ _TPStopTrackingHMACCount
+ _TPStopTrackingSignatureGenerationCount
+ __137-[TPModel dynamicInfoForJoiningPeerID:peerPermanentInfo:peerStableInfo:sponsorID:preapprovedKeys:signingKeyPair:currentMachineIDs:error:]_block_invoke.127
+ __198-[TPModel calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:sponsorPeerID:error:]_block_invoke.117
+ __Block_byref_object_copy_.2997
+ __Block_byref_object_dispose_.2998
+ ___40-[TPModel countOfDistrustedRecoveryKeys]_block_invoke
+ ___41-[TPModel countTotalNumberOfRecoveryKeys]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56s_e16_v16?0"TPPeer"8l
+ ___copy_helper_block_e8_32s40s48s56s
+ ___destroy_helper_block_e8_32s40s48s56s
+ __block_literal_global.1220
+ __block_literal_global.1412
+ __block_literal_global.145
+ __block_literal_global.152
+ __block_literal_global.154
+ __block_literal_global.3008
+ _gHMACCount
+ _gSigCreationCount
+ _objc_msgSend$allCustodianRecoveryKeys
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$intValue
+ _objc_msgSend$isCustodianRecoveryKeyTrusted:error:
+ _objc_msgSend$numberWithInt:
- GCC_except_table1142
- GCC_except_table1150
- GCC_except_table167
- GCC_except_table174
- GCC_except_table179
- GCC_except_table191
- GCC_except_table194
- GCC_except_table204
- GCC_except_table210
- GCC_except_table214
- GCC_except_table216
- GCC_except_table218
- GCC_except_table220
- GCC_except_table222
- GCC_except_table226
- GCC_except_table237
- GCC_except_table240
- GCC_except_table242
- GCC_except_table313
- __137-[TPModel dynamicInfoForJoiningPeerID:peerPermanentInfo:peerStableInfo:sponsorID:preapprovedKeys:signingKeyPair:currentMachineIDs:error:]_block_invoke.126
- __Block_byref_object_copy_.2984
- __Block_byref_object_dispose_.2985
- __block_literal_global.1208
- __block_literal_global.1400
- __block_literal_global.144
- __block_literal_global.151
- __block_literal_global.153
- __block_literal_global.2995
- _checkSigCount
- _objc_msgSend$allTrustedPeersWithCurrentRecoveryKeyWithError:
- _objc_msgSend$isRecoveryKeyExcluded:error:
- _startTrackingCheckSigCount
- _stopTrackingCheckSigCount
CStrings:
+ "Excluding not-trusted RKs: %{public}@"
+ "Failed to iterate peers to check recovery keys, not changing RK trust: %{public}@"
+ "countOfDistrustedRecoveryKeys"
+ "countTotalNumberOfRecoveryKeys"
+ "countTotalTrustedCustodians"
+ "initWithInt:"
+ "intValue"
+ "numberWithInt:"
- "Error determining whether recovery key is excluded: %{public}@"
- "Error finding peers with current recovery key: %{public}@"

```
