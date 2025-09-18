## TrustedPeers

> `/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers`

```diff

-61123.100.169.0.0
-  __TEXT.__text: 0x2cc00
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0x34a0
+61123.120.34.0.0
+  __TEXT.__text: 0x2e968
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_methlist: 0x34a8
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x424
+  __TEXT.__gcc_except_tab: 0x530
   __TEXT.__cstring: 0xce7
-  __TEXT.__oslogstring: 0x1451
-  __TEXT.__unwind_info: 0xb1c
+  __TEXT.__oslogstring: 0x1829
+  __TEXT.__unwind_info: 0xb30
   __TEXT.__objc_classname: 0x4f8
-  __TEXT.__objc_methname: 0x61f6
-  __TEXT.__objc_methtype: 0xc8d
-  __TEXT.__objc_stubs: 0x42c0
+  __TEXT.__objc_methname: 0x63e8
+  __TEXT.__objc_methtype: 0xd26
+  __TEXT.__objc_stubs: 0x4300
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__const: 0x638
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3b30
-  __DATA_CONST.__objc_selrefs: 0x1750
+  __DATA_CONST.__objc_selrefs: 0x1768
   __DATA_CONST.__objc_classrefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x48

   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH.__objc_data: 0x320
+  __AUTH_CONST.__auth_got: 0x318
+  __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x2d8
   __DATA.__data: 0x310
   __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0xc30
+  __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84F92BE2-C270-3059-B133-D764C45FE33C
+  UUID: 20B16022-1C8B-39EB-AABF-559E03BA301A
   Functions: 1173
-  Symbols:   3666
-  CStrings:  1811
+  Symbols:   3672
+  CStrings:  1842
 
Symbols:
+ +[TPPeer calculateHmacWithHmacKey:permanentInfoData:permanentInfoSig:stableInfoData:stableInfoSig:dynamicInfoData:dynamicInfoSig:]
+ +[TPPeer verifyHMACWithPermanentInfoData:permanentInfoSig:stableInfoData:stableInfoSig:dynamicInfoData:dynamicInfoSig:hmacKey:hmacSig:]
+ +[TPPeerPermanentInfo permanentInfoWithPeerID:data:sig:keyFactory:checkSig:]
+ -[TPModel _iterateOverPeersWithBlock:error:]
+ -[TPModel allMachineIDsWithError:]
+ -[TPModel allPolicyVersionsWithError:]
+ -[TPModel allTrustedPeersWithCurrentRecoveryKeyWithError:]
+ -[TPModel anyTrustedPeerDistrustsOtherPeer:error:]
+ -[TPModel bestRecoveryKeyForStableInfo:vouchers:error:]
+ -[TPModel bestWalrusAcrossTrustedPeersWithError:]
+ -[TPModel bestWalrusForStableInfo:walrusStableChanges:error:]
+ -[TPModel bestWebAccessAcrossTrustedPeersWithError:]
+ -[TPModel bestWebAccessForStableInfo:webAccessStableChanges:error:]
+ -[TPModel currentStatePossiblyMissingDataWithError:]
+ -[TPModel doesOctagonContainDistrustedRecoveryKeysWithError:]
+ -[TPModel enumeratePeersUsingBlock:error:]
+ -[TPModel enumerateVouchersUsingBlock:error:]
+ -[TPModel getDynamicInfoForPeerWithID:error:]
+ -[TPModel getStableInfoForPeerWithID:error:]
+ -[TPModel hasAnyPeersWithError:]
+ -[TPModel hasPeerWithID:error:]
+ -[TPModel hasPotentiallyTrustedPeerPreapprovingKey:error:]
+ -[TPModel hasPotentiallyTrustedPeerTestingOnlyWithError:]
+ -[TPModel hasPotentiallyTrustedPeerWithSigningKey:error:]
+ -[TPModel isCustodianRecoveryKeyTrusted:error:]
+ -[TPModel isRecoveryKeyEnrolledWithError:]
+ -[TPModel isRecoveryKeyExcluded:error:]
+ -[TPModel latestEpochAmongPeerIDs:error:]
+ -[TPModel maxClockWithError:]
+ -[TPModel peerCountWithError:]
+ -[TPModel peerCountsByMachineIDWithError:]
+ -[TPModel peerIDThatTrustsCustodianRecoveryKeys:canIntroducePeer:stableInfo:error:]
+ -[TPModel peerIDThatTrustsRecoveryKeys:canIntroducePeer:stableInfo:error:]
+ -[TPModel peerWithID:error:]
+ -[TPModel peersWithMachineID:error:]
+ -[TPModel possibleSponsorsForCustodianRecoveryKey:block:error:]
+ -[TPModel possibleSponsorsForRecoveryKey:block:error:]
+ -[TPModel statusOfPeerWithID:error:]
+ -[TPModel trustedPeerCountWithError:]
+ -[TPModel untrustedPeerIDsWithError:]
+ -[TPModel vectorClockWithError:]
+ -[TPModel viablePeerCountsByModelIDWithError:]
+ -[TPModel voucherCountWithError:]
+ -[TPModelInMemoryDb allPeerIDs:]
+ -[TPModelInMemoryDb enumeratePeersUsingBlock:error:]
+ -[TPModelInMemoryDb enumerateVouchersUsingBlock:error:]
+ -[TPModelInMemoryDb peerCount:]
+ -[TPModelInMemoryDb peerWithID:error:]
+ -[TPModelInMemoryDb voucherCount:]
+ -[TPPeer initWithPermanentInfo:stableInfo:dynamicInfo:checkSig:error:]
+ GCC_except_table151
+ GCC_except_table154
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table173
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table199
+ GCC_except_table205
+ GCC_except_table209
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table221
+ GCC_except_table223
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table307
+ ___29-[TPModel maxClockWithError:]_block_invoke
+ ___32-[TPModel vectorClockWithError:]_block_invoke
+ ___34-[TPModel allMachineIDsWithError:]_block_invoke
+ ___36-[TPModel peersWithMachineID:error:]_block_invoke
+ ___36-[TPModel statusOfPeerWithID:error:]_block_invoke
+ ___37-[TPModel trustedPeerCountWithError:]_block_invoke
+ ___37-[TPModel untrustedPeerIDsWithError:]_block_invoke
+ ___38-[TPModel allPolicyVersionsWithError:]_block_invoke
+ ___39-[TPModel isRecoveryKeyExcluded:error:]_block_invoke
+ ___42-[TPModel enumeratePeersUsingBlock:error:]_block_invoke
+ ___42-[TPModel isRecoveryKeyEnrolledWithError:]_block_invoke
+ ___42-[TPModel peerCountsByMachineIDWithError:]_block_invoke
+ ___44-[TPModel _iterateOverPeersWithBlock:error:]_block_invoke
+ ___45-[TPModel enumerateVouchersUsingBlock:error:]_block_invoke
+ ___46-[TPModel viablePeerCountsByModelIDWithError:]_block_invoke
+ ___47-[TPModel isCustodianRecoveryKeyTrusted:error:]_block_invoke
+ ___49-[TPModel bestWalrusAcrossTrustedPeersWithError:]_block_invoke
+ ___50-[TPModel anyTrustedPeerDistrustsOtherPeer:error:]_block_invoke
+ ___52-[TPModel bestWebAccessAcrossTrustedPeersWithError:]_block_invoke
+ ___52-[TPModel currentStatePossiblyMissingDataWithError:]_block_invoke
+ ___52-[TPModelInMemoryDb enumeratePeersUsingBlock:error:]_block_invoke
+ ___54-[TPModel possibleSponsorsForRecoveryKey:block:error:]_block_invoke
+ ___55-[TPModel bestRecoveryKeyForStableInfo:vouchers:error:]_block_invoke
+ ___55-[TPModelInMemoryDb enumerateVouchersUsingBlock:error:]_block_invoke
+ ___57-[TPModel hasPotentiallyTrustedPeerTestingOnlyWithError:]_block_invoke
+ ___57-[TPModel hasPotentiallyTrustedPeerWithSigningKey:error:]_block_invoke
+ ___58-[TPModel allTrustedPeersWithCurrentRecoveryKeyWithError:]_block_invoke
+ ___58-[TPModel hasPotentiallyTrustedPeerPreapprovingKey:error:]_block_invoke
+ ___61-[TPModel doesOctagonContainDistrustedRecoveryKeysWithError:]_block_invoke
+ ___63-[TPModel possibleSponsorsForCustodianRecoveryKey:block:error:]_block_invoke
+ ___74-[TPModel peerIDThatTrustsRecoveryKeys:canIntroducePeer:stableInfo:error:]_block_invoke
+ ___83-[TPModel peerIDThatTrustsCustodianRecoveryKeys:canIntroducePeer:stableInfo:error:]_block_invoke
+ ___Block_byref_object_copy_.2918
+ ___Block_byref_object_dispose_.2919
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88r_e23_v24?0"TPVoucher"8^B16ls32l8s40l8s48l8r88l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88r_e20_v24?0"TPPeer"8^B16ls32l8s40l8s48l8r88l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.1152
+ ___block_literal_global.1345
+ ___block_literal_global.174
+ ___block_literal_global.2927
+ __os_log_error_impl
+ _objc_msgSend$_iterateOverPeersWithBlock:error:
+ _objc_msgSend$allPeerIDs:
+ _objc_msgSend$allPolicyVersionsWithError:
+ _objc_msgSend$allTrustedPeersWithCurrentRecoveryKeyWithError:
+ _objc_msgSend$bestWalrusAcrossTrustedPeersWithError:
+ _objc_msgSend$bestWebAccessAcrossTrustedPeersWithError:
+ _objc_msgSend$calculateHmacWithHmacKey:permanentInfoData:permanentInfoSig:stableInfoData:stableInfoSig:dynamicInfoData:dynamicInfoSig:
+ _objc_msgSend$enumeratePeersUsingBlock:error:
+ _objc_msgSend$enumerateVouchersUsingBlock:error:
+ _objc_msgSend$hasPeerWithID:error:
+ _objc_msgSend$initWithPermanentInfo:stableInfo:dynamicInfo:checkSig:error:
+ _objc_msgSend$isRecoveryKeyExcluded:error:
+ _objc_msgSend$maxClockWithError:
+ _objc_msgSend$peerCount:
+ _objc_msgSend$peerCountWithError:
+ _objc_msgSend$peerWithID:error:
+ _objc_msgSend$peersWithMachineID:error:
+ _objc_msgSend$permanentInfoWithPeerID:data:sig:keyFactory:checkSig:
+ _objc_msgSend$possibleSponsorsForCustodianRecoveryKey:block:error:
+ _objc_msgSend$possibleSponsorsForRecoveryKey:block:error:
+ _objc_msgSend$untrustedPeerIDsWithError:
+ _objc_msgSend$voucherCount:
- +[TPPeer calculateHmacWithHmacKey:permanentInfo:stableInfo:dynamicInfo:]
- +[TPPeer verifyHMACWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:]
- -[TPModel _iterateOverPeersWithBlock:]
- -[TPModel allMachineIDs]
- -[TPModel allPolicyVersions]
- -[TPModel allTrustedPeersWithCurrentRecoveryKey]
- -[TPModel anyTrustedPeerDistrustsOtherPeer:]
- -[TPModel bestRecoveryKeyForStableInfo:vouchers:]
- -[TPModel bestWalrusAcrossTrustedPeers]
- -[TPModel bestWalrusForStableInfo:walrusStableChanges:]
- -[TPModel bestWebAccessAcrossTrustedPeers]
- -[TPModel bestWebAccessForStableInfo:webAccessStableChanges:]
- -[TPModel countOfTrustedPeers]
- -[TPModel currentStatePossiblyMissingData]
- -[TPModel doesOctagonContainsDistrustedRecoveryKeys]
- -[TPModel enumeratePeersUsingBlock:]
- -[TPModel enumerateVouchersUsingBlock:]
- -[TPModel getDynamicInfoForPeerWithID:]
- -[TPModel getStableInfoForPeerWithID:]
- -[TPModel hasAnyPeers]
- -[TPModel hasPeerWithID:]
- -[TPModel hasPotentiallyTrustedPeerPreapprovingKey:]
- -[TPModel hasPotentiallyTrustedPeerWithSigningKey:]
- -[TPModel hasPotentiallyTrustedPeer]
- -[TPModel isCustodianRecoveryKeyTrusted:]
- -[TPModel isRecoveryKeyEnrolled]
- -[TPModel isRecoveryKeyExcluded:]
- -[TPModel latestEpochAmongPeerIDs:]
- -[TPModel maxClock]
- -[TPModel peerCount]
- -[TPModel peerCountsByMachineID]
- -[TPModel peerIDThatTrustsCustodianRecoveryKeys:canIntroducePeer:stableInfo:]
- -[TPModel peerIDThatTrustsRecoveryKeys:canIntroducePeer:stableInfo:]
- -[TPModel peerWithID:]
- -[TPModel peersWithMachineID:]
- -[TPModel possibleSponsorsForCustodianRecoveryKey:block:]
- -[TPModel possibleSponsorsForRecoveryKey:block:]
- -[TPModel statusOfPeerWithID:]
- -[TPModel trustedPeerIDs]
- -[TPModel untrustedPeerIDs]
- -[TPModel vectorClock]
- -[TPModel viablePeerCountsByModelID]
- -[TPModel voucherCount]
- -[TPModelInMemoryDb allPeerIDs]
- -[TPModelInMemoryDb enumeratePeersUsingBlock:]
- -[TPModelInMemoryDb enumerateVouchersUsingBlock:]
- -[TPModelInMemoryDb hasAnyPeers]
- -[TPModelInMemoryDb peerWithID:]
- -[TPModelInMemoryDb voucherCount]
- -[TPPeer initWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:error:]
- GCC_except_table153
- GCC_except_table158
- GCC_except_table162
- GCC_except_table164
- GCC_except_table174
- GCC_except_table179
- GCC_except_table192
- GCC_except_table200
- GCC_except_table206
- GCC_except_table210
- GCC_except_table212
- GCC_except_table214
- GCC_except_table216
- GCC_except_table218
- GCC_except_table222
- GCC_except_table224
- GCC_except_table233
- GCC_except_table236
- GCC_except_table238
- GCC_except_table308
- ___19-[TPModel maxClock]_block_invoke
- ___22-[TPModel vectorClock]_block_invoke
- ___24-[TPModel allMachineIDs]_block_invoke
- ___25-[TPModel trustedPeerIDs]_block_invoke
- ___27-[TPModel untrustedPeerIDs]_block_invoke
- ___28-[TPModel allPolicyVersions]_block_invoke
- ___30-[TPModel peersWithMachineID:]_block_invoke
- ___30-[TPModel statusOfPeerWithID:]_block_invoke
- ___32-[TPModel isRecoveryKeyEnrolled]_block_invoke
- ___32-[TPModel peerCountsByMachineID]_block_invoke
- ___33-[TPModel isRecoveryKeyExcluded:]_block_invoke
- ___36-[TPModel enumeratePeersUsingBlock:]_block_invoke
- ___36-[TPModel hasPotentiallyTrustedPeer]_block_invoke
- ___36-[TPModel viablePeerCountsByModelID]_block_invoke
- ___38-[TPModel _iterateOverPeersWithBlock:]_block_invoke
- ___39-[TPModel bestWalrusAcrossTrustedPeers]_block_invoke
- ___39-[TPModel enumerateVouchersUsingBlock:]_block_invoke
- ___41-[TPModel isCustodianRecoveryKeyTrusted:]_block_invoke
- ___42-[TPModel bestWebAccessAcrossTrustedPeers]_block_invoke
- ___42-[TPModel currentStatePossiblyMissingData]_block_invoke
- ___44-[TPModel anyTrustedPeerDistrustsOtherPeer:]_block_invoke
- ___46-[TPModelInMemoryDb enumeratePeersUsingBlock:]_block_invoke
- ___48-[TPModel allTrustedPeersWithCurrentRecoveryKey]_block_invoke
- ___48-[TPModel possibleSponsorsForRecoveryKey:block:]_block_invoke
- ___49-[TPModel bestRecoveryKeyForStableInfo:vouchers:]_block_invoke
- ___49-[TPModelInMemoryDb enumerateVouchersUsingBlock:]_block_invoke
- ___51-[TPModel hasPotentiallyTrustedPeerWithSigningKey:]_block_invoke
- ___52-[TPModel doesOctagonContainsDistrustedRecoveryKeys]_block_invoke
- ___52-[TPModel hasPotentiallyTrustedPeerPreapprovingKey:]_block_invoke
- ___57-[TPModel possibleSponsorsForCustodianRecoveryKey:block:]_block_invoke
- ___68-[TPModel peerIDThatTrustsRecoveryKeys:canIntroducePeer:stableInfo:]_block_invoke
- ___77-[TPModel peerIDThatTrustsCustodianRecoveryKeys:canIntroducePeer:stableInfo:]_block_invoke
- ___Block_byref_object_copy_.2927
- ___Block_byref_object_dispose_.2928
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s_e23_v24?0"TPVoucher"8^B16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.1164
- ___block_literal_global.1359
- ___block_literal_global.175
- ___block_literal_global.2936
- _objc_msgSend$_iterateOverPeersWithBlock:
- _objc_msgSend$allPolicyVersions
- _objc_msgSend$allTrustedPeersWithCurrentRecoveryKey
- _objc_msgSend$bestWalrusAcrossTrustedPeers
- _objc_msgSend$bestWebAccessAcrossTrustedPeers
- _objc_msgSend$calculateHmacWithHmacKey:permanentInfo:stableInfo:dynamicInfo:
- _objc_msgSend$enumeratePeersUsingBlock:
- _objc_msgSend$enumerateVouchersUsingBlock:
- _objc_msgSend$hasAnyPeers
- _objc_msgSend$hasPeerWithID:
- _objc_msgSend$isRecoveryKeyExcluded:
- _objc_msgSend$maxClock
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$peerWithID:
- _objc_msgSend$peersWithMachineID:
- _objc_msgSend$possibleSponsorsForCustodianRecoveryKey:block:
- _objc_msgSend$possibleSponsorsForRecoveryKey:block:
- _objc_msgSend$untrustedPeerIDs
- _objc_msgSend$verifyHMACWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:
- _objc_msgSend$voucherCount
CStrings:
+ "@\"NSArray\"24@0:8^@16"
+ "@\"TPPeer\"32@0:8@\"NSString\"16^@24"
+ "@24@0:8^@16"
+ "@32@0:8@?16^@24"
+ "@40@0:8@16@?24^@32"
+ "@52@0:8@16@24@32@40B48"
+ "@52@0:8@16@24@32B40^@44"
+ "@64@0:8@16@24@32@40@48Q56"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "B24@0:8^@16"
+ "B32@0:8@?16^@24"
+ "B32@0:8@?<v@?@\"TPPeer\"^B>16^@24"
+ "B32@0:8@?<v@?@\"TPVoucher\"^B>16^@24"
+ "B80@0:8@16@24@32@40@48@56@64@72"
+ "Can't find peer %{public}@: %{public}@"
+ "Could not find peer %{public}@: %{public}@"
+ "DB error for sponsor %{public}@: %{public}@"
+ "Error determining possible sponsors: %{public}@"
+ "Error determining whether recovery key is excluded: %{public}@"
+ "Error enumerating peers: %{public}@"
+ "Error filtering preapprovals: %{public}@"
+ "Error finding excluded peer %{public}@: %{public}@"
+ "Error finding peer %@ in model, removing: %{public}@"
+ "Error finding peer %@: %{public}@"
+ "Error finding peer %{public}@: %{public}@"
+ "Error finding peers with current recovery key: %{public}@"
+ "Error recursively expanding peers: %{public}@"
+ "Error sponsor checking: %{public}@"
+ "Peer not in DB %{public}@"
+ "Peer not in DB %{public}@: %{public}@"
+ "Q24@0:8^@16"
+ "Q32@0:8@16^@24"
+ "_iterateOverPeersWithBlock:error:"
+ "allMachineIDsWithError:"
+ "allPeerIDs:"
+ "allPolicyVersionsWithError:"
+ "allTrustedPeersWithCurrentRecoveryKeyWithError:"
+ "anyTrustedPeerDistrustsOtherPeer:error:"
+ "bestRecoveryKeyForStableInfo:vouchers:error:"
+ "bestWalrusAcrossTrustedPeersWithError:"
+ "bestWalrusForStableInfo:walrusStableChanges:error:"
+ "bestWebAccessAcrossTrustedPeersWithError:"
+ "bestWebAccessForStableInfo:webAccessStableChanges:error:"
+ "calculateHmacWithHmacKey:permanentInfoData:permanentInfoSig:stableInfoData:stableInfoSig:dynamicInfoData:dynamicInfoSig:"
+ "can't find peer for status %{public}@: %{public}@"
+ "can't update dynamic info for peerID %{public}@: %{public}@"
+ "can't update stable info for peerID %{public}@: %{public}@"
+ "currentStatePossiblyMissingDataWithError:"
+ "doesOctagonContainDistrustedRecoveryKeysWithError:"
+ "enumeratePeersUsingBlock:error:"
+ "enumerateVouchersUsingBlock:error:"
+ "error determining epoch of peerID %{public}@: %{public}@"
+ "getDynamicInfoForPeerWithID:error:"
+ "getStableInfoForPeerWithID:error:"
+ "hasAnyPeersWithError:"
+ "hasPeerWithID:error:"
+ "hasPotentiallyTrustedPeer error: %{public}@"
+ "hasPotentiallyTrustedPeerPreapprovingKey:error:"
+ "hasPotentiallyTrustedPeerTestingOnlyWithError:"
+ "hasPotentiallyTrustedPeerWithSigningKey:error:"
+ "ignoring error getting policy for peerIDs %{public}@"
+ "initWithPermanentInfo:stableInfo:dynamicInfo:checkSig:error:"
+ "isCustodianRecoveryKeyTrusted:error:"
+ "isRecoveryKeyEnrolledWithError:"
+ "isRecoveryKeyExcluded:error:"
+ "latestEpochAmongPeerIDs:error:"
+ "maxClock error enumerating peers: %{public}@"
+ "maxClockWithError:"
+ "peerCount:"
+ "peerCountWithError:"
+ "peerCountsByMachineIDWithError:"
+ "peerIDThatTrustsCustodianRecoveryKeys:canIntroducePeer:stableInfo:error:"
+ "peerIDThatTrustsRecoveryKeys:canIntroducePeer:stableInfo:error:"
+ "peerWithID:error:"
+ "peersWithMachineID:error:"
+ "permanentInfoWithPeerID:data:sig:keyFactory:checkSig:"
+ "possibleSponsorsForCustodianRecoveryKey:block:error:"
+ "possibleSponsorsForRecoveryKey:block:error:"
+ "status: error enumerating peers: %{public}@"
+ "statusOfPeerWithID:error:"
+ "trustedPeerCountWithError:"
+ "untrustedPeerIDsWithError:"
+ "vectorClockWithError:"
+ "verifyHMACWithPermanentInfoData:permanentInfoSig:stableInfoData:stableInfoSig:dynamicInfoData:dynamicInfoSig:hmacKey:hmacSig:"
+ "viablePeerCountsByModelIDWithError:"
+ "voucher: no peer for id %{public}@: %{public}@"
+ "voucherCount:"
+ "voucherCountWithError:"
- "@\"NSArray\"16@0:8"
- "@\"TPPeer\"24@0:8@\"NSString\"16"
- "@24@0:8@?16"
- "@32@0:8@16@?24"
- "B56@0:8@16@24@32@40@48"
- "Q24@0:8@16"
- "_iterateOverPeersWithBlock:"
- "allMachineIDs"
- "allPolicyVersions"
- "allTrustedPeersWithCurrentRecoveryKey"
- "anyTrustedPeerDistrustsOtherPeer:"
- "bestRecoveryKeyForStableInfo:vouchers:"
- "bestWalrusAcrossTrustedPeers"
- "bestWalrusForStableInfo:walrusStableChanges:"
- "bestWebAccessAcrossTrustedPeers"
- "bestWebAccessForStableInfo:webAccessStableChanges:"
- "calculateHmacWithHmacKey:permanentInfo:stableInfo:dynamicInfo:"
- "can't update dynamic info for peerID %{public}@: peer does not exist"
- "can't update stable info for peerID %{public}@: peer does not exist"
- "countOfTrustedPeers"
- "currentStatePossiblyMissingData"
- "doesOctagonContainsDistrustedRecoveryKeys"
- "enumeratePeersUsingBlock:"
- "enumerateVouchersUsingBlock:"
- "getDynamicInfoForPeerWithID:"
- "getStableInfoForPeerWithID:"
- "hasAnyPeers"
- "hasPeerWithID:"
- "hasPotentiallyTrustedPeer"
- "hasPotentiallyTrustedPeerPreapprovingKey:"
- "hasPotentiallyTrustedPeerWithSigningKey:"
- "initWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:error:"
- "isCustodianRecoveryKeyTrusted:"
- "isRecoveryKeyEnrolled"
- "isRecoveryKeyExcluded:"
- "latestEpochAmongPeerIDs:"
- "maxClock"
- "numberWithInteger:"
- "peerCount"
- "peerCountsByMachineID"
- "peerIDThatTrustsCustodianRecoveryKeys:canIntroducePeer:stableInfo:"
- "peerIDThatTrustsRecoveryKeys:canIntroducePeer:stableInfo:"
- "peerWithID:"
- "peersWithMachineID:"
- "possibleSponsorsForCustodianRecoveryKey:block:"
- "possibleSponsorsForRecoveryKey:block:"
- "statusOfPeerWithID:"
- "untrustedPeerIDs"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"TPPeer\"^B>16"
- "v24@0:8@?<v@?@\"TPVoucher\"^B>16"
- "v64@0:8@16@24@32@40@48Q56"
- "vectorClock"
- "verifyHMACWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:"
- "viablePeerCountsByModelID"
- "voucher: no peer for id %{public}@"
- "voucherCount"

```
