## TrustedPeers

> `/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers`

```diff

-61040.82.1.0.0
-  __TEXT.__text: 0x2a240
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x3148
+61123.100.169.0.0
+  __TEXT.__text: 0x2cc00
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x34a0
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__cstring: 0xc18
-  __TEXT.__oslogstring: 0x10e3
-  __TEXT.__unwind_info: 0x95c
-  __TEXT.__objc_classname: 0x45d
-  __TEXT.__objc_methname: 0x5d1b
-  __TEXT.__objc_methtype: 0xb06
-  __TEXT.__objc_stubs: 0x4040
+  __TEXT.__gcc_except_tab: 0x424
+  __TEXT.__cstring: 0xce7
+  __TEXT.__oslogstring: 0x1451
+  __TEXT.__unwind_info: 0xb1c
+  __TEXT.__objc_classname: 0x4f8
+  __TEXT.__objc_methname: 0x61f6
+  __TEXT.__objc_methtype: 0xc8d
+  __TEXT.__objc_stubs: 0x42c0
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x350
-  __DATA_CONST.__objc_classlist: 0x168
+  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3790
-  __DATA_CONST.__objc_selrefs: 0x1650
+  __DATA_CONST.__objc_const: 0x3b30
+  __DATA_CONST.__objc_selrefs: 0x1750
+  __DATA_CONST.__objc_classrefs: 0x208
+  __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x1800
-  __AUTH_CONST.__objc_const: 0x13d0
-  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x1538
+  __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_classrefs: 0x1f0
-  __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x2bc
-  __DATA.__data: 0x2b0
+  __AUTH_CONST.__auth_got: 0x310
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x2d8
+  __DATA.__data: 0x310
   __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E74DAFF5-EB50-36B6-B565-85983C862C5E
-  Functions: 1071
-  Symbols:   3369
-  CStrings:  1708
+  UUID: 39EAA7C9-060D-3560-9D20-9750C807C266
+  Functions: 1173
+  Symbols:   3666
+  CStrings:  1811
 
Symbols:
+ +[TPHashBuilder keyedHashWithAlgo:key:data:]
+ +[TPModel pickClock:]
+ +[TPPeer calculateHmacWithHmacKey:permanentInfo:stableInfo:dynamicInfo:]
+ +[TPPeer verifyHMACWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:]
+ +[TPPeerPermanentInfo permanentInfoWithMachineID:modelID:epoch:signingKeyPair:encryptionKeyPair:creationTime:peerIDHashAlgo:error:]
+ -[TPHashBuilder ctxHMAC]
+ -[TPHashBuilder finalKeyedHash]
+ -[TPHashBuilder initWithKeyedAlgo:key:]
+ -[TPHashBuilder keyed]
+ -[TPHashBuilder setCtxHMAC:]
+ -[TPHashBuilder setKeyed:]
+ -[TPModel _iterateOverPeersWithBlock:]
+ -[TPModel bestRecoveryKeyForStableInfo:vouchers:]
+ -[TPModel bestWalrusForStableInfo:walrusStableChanges:]
+ -[TPModel bestWebAccessForStableInfo:webAccessStableChanges:]
+ -[TPModel calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:sponsorPeerID:error:]
+ -[TPModel copyPeerWithNewDynamicInfo:forPeerWithID:error:]
+ -[TPModel copyPeerWithNewStableInfo:forPeerWithID:error:]
+ -[TPModel dbAdapter]
+ -[TPModel enumeratePeersUsingBlock:]
+ -[TPModel enumerateVouchersUsingBlock:]
+ -[TPModel filterPeerList:byMachineIDs:sponsorPeerID:dispositions:]
+ -[TPModel hasAnyPeers]
+ -[TPModel hasPotentiallyTrustedPeer]
+ -[TPModel initWithDecrypter:dbAdapter:]
+ -[TPModel peerCount]
+ -[TPModel possibleSponsorsForCustodianRecoveryKey:block:]
+ -[TPModel possibleSponsorsForRecoveryKey:block:]
+ -[TPModel setDbAdapter:]
+ -[TPModel trustedPeerIDs]
+ -[TPModel voucherCount]
+ -[TPModelInMemoryDb .cxx_destruct]
+ -[TPModelInMemoryDb allPeerIDs]
+ -[TPModelInMemoryDb deletePeerWithID:]
+ -[TPModelInMemoryDb enumeratePeersUsingBlock:]
+ -[TPModelInMemoryDb enumerateVouchersUsingBlock:]
+ -[TPModelInMemoryDb hasAnyPeers]
+ -[TPModelInMemoryDb init]
+ -[TPModelInMemoryDb peerWithID:]
+ -[TPModelInMemoryDb peersByID]
+ -[TPModelInMemoryDb registerPeerWithPermanentInfo:]
+ -[TPModelInMemoryDb registerVoucher:]
+ -[TPModelInMemoryDb setPeersByID:]
+ -[TPModelInMemoryDb setVouchers:]
+ -[TPModelInMemoryDb updatePeer:error:]
+ -[TPModelInMemoryDb voucherCount]
+ -[TPModelInMemoryDb vouchers]
+ -[TPPBDisposition evictedMachineID]
+ -[TPPBDisposition ghostedMachineID]
+ -[TPPBDisposition hasEvictedMachineID]
+ -[TPPBDisposition hasGhostedMachineID]
+ -[TPPBDisposition hasUnknownReasonRemovalMachineID]
+ -[TPPBDisposition setEvictedMachineID:]
+ -[TPPBDisposition setGhostedMachineID:]
+ -[TPPBDisposition setUnknownReasonRemovalMachineID:]
+ -[TPPBDisposition unknownReasonRemovalMachineID]
+ -[TPPBDispositionEvictedMachineID copyTo:]
+ -[TPPBDispositionEvictedMachineID copyWithZone:]
+ -[TPPBDispositionEvictedMachineID description]
+ -[TPPBDispositionEvictedMachineID dictionaryRepresentation]
+ -[TPPBDispositionEvictedMachineID hash]
+ -[TPPBDispositionEvictedMachineID isEqual:]
+ -[TPPBDispositionEvictedMachineID mergeFrom:]
+ -[TPPBDispositionEvictedMachineID readFrom:]
+ -[TPPBDispositionEvictedMachineID writeTo:]
+ -[TPPBDispositionGhostedMachineID copyTo:]
+ -[TPPBDispositionGhostedMachineID copyWithZone:]
+ -[TPPBDispositionGhostedMachineID description]
+ -[TPPBDispositionGhostedMachineID dictionaryRepresentation]
+ -[TPPBDispositionGhostedMachineID hash]
+ -[TPPBDispositionGhostedMachineID isEqual:]
+ -[TPPBDispositionGhostedMachineID mergeFrom:]
+ -[TPPBDispositionGhostedMachineID readFrom:]
+ -[TPPBDispositionGhostedMachineID writeTo:]
+ -[TPPBDispositionUnknownReasonRemovalMachineID copyTo:]
+ -[TPPBDispositionUnknownReasonRemovalMachineID copyWithZone:]
+ -[TPPBDispositionUnknownReasonRemovalMachineID description]
+ -[TPPBDispositionUnknownReasonRemovalMachineID dictionaryRepresentation]
+ -[TPPBDispositionUnknownReasonRemovalMachineID hash]
+ -[TPPBDispositionUnknownReasonRemovalMachineID isEqual:]
+ -[TPPBDispositionUnknownReasonRemovalMachineID mergeFrom:]
+ -[TPPBDispositionUnknownReasonRemovalMachineID readFrom:]
+ -[TPPBDispositionUnknownReasonRemovalMachineID writeTo:]
+ -[TPPBPeerPermanentInfo creationTime]
+ -[TPPBPeerPermanentInfo hasCreationTime]
+ -[TPPBPeerPermanentInfo setCreationTime:]
+ -[TPPBPeerPermanentInfo setHasCreationTime:]
+ -[TPPeer calculateHmacWithHmacKey:]
+ -[TPPeer initWithPermanentInfo:stableInfo:dynamicInfo:error:]
+ -[TPPeer initWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:error:]
+ -[TPPeerPermanentInfo creationTime]
+ -[TPPeerPermanentInfo initWithMachineID:modelID:epoch:signingPubKey:encryptionPubKey:creationTime:data:sig:peerID:]
+ -[TPVoucher hash]
+ GCC_except_table1111
+ GCC_except_table1119
+ GCC_except_table126
+ GCC_except_table139
+ GCC_except_table149
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table158
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table174
+ GCC_except_table179
+ GCC_except_table192
+ GCC_except_table200
+ GCC_except_table206
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table214
+ GCC_except_table216
+ GCC_except_table218
+ GCC_except_table222
+ GCC_except_table224
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table308
+ OBJC_IVAR_$_TPPBDisposition._evictedMachineID
+ OBJC_IVAR_$_TPPBDisposition._ghostedMachineID
+ OBJC_IVAR_$_TPPBDisposition._unknownReasonRemovalMachineID
+ OBJC_IVAR_$_TPPBPeerPermanentInfo._creationTime
+ _CCHmacFinal
+ _CCHmacInit
+ _CCHmacUpdate
+ _OBJC_CLASS_$_TPModelInMemoryDb
+ _OBJC_CLASS_$_TPPBDispositionEvictedMachineID
+ _OBJC_CLASS_$_TPPBDispositionGhostedMachineID
+ _OBJC_CLASS_$_TPPBDispositionUnknownReasonRemovalMachineID
+ _OBJC_IVAR_$_TPHashBuilder._ctxHMAC
+ _OBJC_IVAR_$_TPHashBuilder._keyed
+ _OBJC_IVAR_$_TPModel._dbAdapter
+ _OBJC_IVAR_$_TPModelInMemoryDb._peersByID
+ _OBJC_IVAR_$_TPModelInMemoryDb._vouchers
+ _OBJC_IVAR_$_TPPeerPermanentInfo._creationTime
+ _OBJC_METACLASS_$_TPModelInMemoryDb
+ _OBJC_METACLASS_$_TPPBDispositionEvictedMachineID
+ _OBJC_METACLASS_$_TPPBDispositionGhostedMachineID
+ _OBJC_METACLASS_$_TPPBDispositionUnknownReasonRemovalMachineID
+ _TPPBDispositionEvictedMachineIDReadFrom
+ _TPPBDispositionGhostedMachineIDReadFrom
+ _TPPBDispositionUnknownReasonRemovalMachineIDReadFrom
+ __OBJC_$_CLASS_METHODS_TPPeer
+ __OBJC_$_INSTANCE_METHODS_TPModelInMemoryDb
+ __OBJC_$_INSTANCE_METHODS_TPPBDispositionEvictedMachineID
+ __OBJC_$_INSTANCE_METHODS_TPPBDispositionGhostedMachineID
+ __OBJC_$_INSTANCE_METHODS_TPPBDispositionUnknownReasonRemovalMachineID
+ __OBJC_$_INSTANCE_VARIABLES_TPModelInMemoryDb
+ __OBJC_$_PROP_LIST_TPModelInMemoryDb
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TPModelDBAdapterProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TPModelDBAdapterProtocol
+ __OBJC_CLASS_PROTOCOLS_$_TPModelInMemoryDb
+ __OBJC_CLASS_PROTOCOLS_$_TPPBDispositionEvictedMachineID
+ __OBJC_CLASS_PROTOCOLS_$_TPPBDispositionGhostedMachineID
+ __OBJC_CLASS_PROTOCOLS_$_TPPBDispositionUnknownReasonRemovalMachineID
+ __OBJC_CLASS_RO_$_TPModelInMemoryDb
+ __OBJC_CLASS_RO_$_TPPBDispositionEvictedMachineID
+ __OBJC_CLASS_RO_$_TPPBDispositionGhostedMachineID
+ __OBJC_CLASS_RO_$_TPPBDispositionUnknownReasonRemovalMachineID
+ __OBJC_LABEL_PROTOCOL_$_TPModelDBAdapterProtocol
+ __OBJC_METACLASS_RO_$_TPModelInMemoryDb
+ __OBJC_METACLASS_RO_$_TPPBDispositionEvictedMachineID
+ __OBJC_METACLASS_RO_$_TPPBDispositionGhostedMachineID
+ __OBJC_METACLASS_RO_$_TPPBDispositionUnknownReasonRemovalMachineID
+ __OBJC_PROTOCOL_$_TPModelDBAdapterProtocol
+ ___137-[TPModel dynamicInfoForJoiningPeerID:peerPermanentInfo:peerStableInfo:sponsorID:preapprovedKeys:signingKeyPair:currentMachineIDs:error:]_block_invoke_2
+ ___141-[TPModel considerPreapprovalsSponsoredByPeer:toRecursivelyExpandIncludedPeerIDs:andExcludedPeerIDs:dispositions:currentMachineIDs:forEpoch:]_block_invoke
+ ___160-[TPModel considerVouchersSponsoredByPeerID:sponsorPermanentInfo:toRecursivelyExpandIncludedPeerIDs:andExcludedPeerIDs:dispositions:currentMachineIDs:forEpoch:]_block_invoke
+ ___198-[TPModel calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:sponsorPeerID:error:]_block_invoke
+ ___198-[TPModel calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:sponsorPeerID:error:]_block_invoke.150
+ ___21+[TPModel pickClock:]_block_invoke
+ ___24-[TPModel allMachineIDs]_block_invoke
+ ___25-[TPModel trustedPeerIDs]_block_invoke
+ ___28-[TPModel allPolicyVersions]_block_invoke
+ ___30-[TPModel peersWithMachineID:]_block_invoke
+ ___30-[TPModel statusOfPeerWithID:]_block_invoke
+ ___32-[TPModel peerCountsByMachineID]_block_invoke
+ ___33-[TPModel isRecoveryKeyExcluded:]_block_invoke
+ ___36-[TPModel enumeratePeersUsingBlock:]_block_invoke
+ ___36-[TPModel hasPotentiallyTrustedPeer]_block_invoke
+ ___36-[TPModel viablePeerCountsByModelID]_block_invoke
+ ___38-[TPModel _iterateOverPeersWithBlock:]_block_invoke
+ ___39-[TPModel bestWalrusAcrossTrustedPeers]_block_invoke
+ ___39-[TPModel enumerateVouchersUsingBlock:]_block_invoke
+ ___42-[TPModel bestWebAccessAcrossTrustedPeers]_block_invoke
+ ___42-[TPModel currentStatePossiblyMissingData]_block_invoke
+ ___42-[TPModel validateVoucherForPeer:sponsor:]_block_invoke
+ ___44-[TPModel anyTrustedPeerDistrustsOtherPeer:]_block_invoke
+ ___46-[TPModelInMemoryDb enumeratePeersUsingBlock:]_block_invoke
+ ___48-[TPModel allTrustedPeersWithCurrentRecoveryKey]_block_invoke
+ ___48-[TPModel possibleSponsorsForRecoveryKey:block:]_block_invoke
+ ___49-[TPModel bestRecoveryKeyForStableInfo:vouchers:]_block_invoke
+ ___49-[TPModelInMemoryDb enumerateVouchersUsingBlock:]_block_invoke
+ ___51-[TPModel hasPotentiallyTrustedPeerWithSigningKey:]_block_invoke
+ ___52-[TPModel doesOctagonContainsDistrustedRecoveryKeys]_block_invoke
+ ___52-[TPModel hasPotentiallyTrustedPeerPreapprovingKey:]_block_invoke
+ ___57-[TPModel possibleSponsorsForCustodianRecoveryKey:block:]_block_invoke
+ ___Block_byref_object_copy_.2927
+ ___Block_byref_object_dispose_.2928
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s_e20_v24?0"TPPeer"8^B16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_32_e16_B16?0"TPPeer"8l
+ ___block_descriptor_32_e16_v16?0"TPPeer"8l
+ ___block_descriptor_40_e8_32bs_e20_v24?0"TPPeer"8^B16ls32l8
+ ___block_descriptor_40_e8_32bs_e23_v24?0"TPVoucher"8^B16ls32l8
+ ___block_descriptor_40_e8_32bs_e33_v32?0"NSString"8"TPPeer"16^B24ls32l8
+ ___block_descriptor_40_e8_32r_e16_v16?0"TPPeer"8lr32l8
+ ___block_descriptor_40_e8_32r_e20_v24?0"TPPeer"8^B16lr32l8
+ ___block_descriptor_40_e8_32s_e20_v24?0"TPPeer"8^B16ls32l8
+ ___block_descriptor_48_e8_32s40r_e16_v16?0"TPPeer"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e20_v24?0"TPPeer"8^B16ls32l8r40l8
+ ___block_descriptor_56_e8_32bs40r48r_e20_v24?0"TPPeer"8^B16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e20_v24?0"TPPeer"8^B16lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e20_v24?0"TPPeer"8^B16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e16_B16?0"TPPeer"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e16_v16?0"TPPeer"8ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e20_v24?0"TPPeer"8^B16ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e23_v24?0"TPVoucher"8^B16ls32l8s40l8s48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s_e20_v24?0"TPPeer"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e16_v16?0"TPPeer"8ls32l8r56l8s40l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e16_v16?0"TPPeer"8ls32l8r56l8s40l8s48l8r64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s_e23_v24?0"TPVoucher"8^B16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.1164
+ ___block_literal_global.1359
+ ___block_literal_global.175
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.2936
+ __unnamed_array_storage.175
+ _failWithNoPeerWithIDError
+ _memcpy
+ _objc_msgSend$_iterateOverPeersWithBlock:
+ _objc_msgSend$anyObject
+ _objc_msgSend$bestWalrusAcrossTrustedPeers
+ _objc_msgSend$bestWebAccessAcrossTrustedPeers
+ _objc_msgSend$calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:sponsorPeerID:error:
+ _objc_msgSend$calculateHmacWithHmacKey:permanentInfo:stableInfo:dynamicInfo:
+ _objc_msgSend$creationTime
+ _objc_msgSend$dbAdapter
+ _objc_msgSend$enumeratePeersUsingBlock:
+ _objc_msgSend$enumerateVouchersUsingBlock:
+ _objc_msgSend$evictedMachineID
+ _objc_msgSend$filterPeerList:byMachineIDs:sponsorPeerID:dispositions:
+ _objc_msgSend$finalKeyedHash
+ _objc_msgSend$firstObject
+ _objc_msgSend$ghostedMachineID
+ _objc_msgSend$hasAnyPeers
+ _objc_msgSend$hasEvictedMachineID
+ _objc_msgSend$hasGhostedMachineID
+ _objc_msgSend$hasUnknownReasonRemovalMachineID
+ _objc_msgSend$initWithKeyedAlgo:key:
+ _objc_msgSend$initWithMachineID:modelID:epoch:signingPubKey:encryptionPubKey:creationTime:data:sig:peerID:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$keyedHashWithAlgo:key:data:
+ _objc_msgSend$pickClock:
+ _objc_msgSend$possibleSponsorsForCustodianRecoveryKey:block:
+ _objc_msgSend$possibleSponsorsForRecoveryKey:block:
+ _objc_msgSend$setCreationTime:
+ _objc_msgSend$setEvictedMachineID:
+ _objc_msgSend$setGhostedMachineID:
+ _objc_msgSend$setUnknownReasonRemovalMachineID:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$unknownReasonRemovalMachineID
+ _objc_msgSend$verifyHMACWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:
+ _objc_msgSend$voucherCount
+ _objc_retain_x4
- +[TPPeerPermanentInfo permanentInfoWithMachineID:modelID:epoch:signingKeyPair:encryptionKeyPair:peerIDHashAlgo:error:]
- -[TPModel allPeers]
- -[TPModel allVouchers]
- -[TPModel bestRecoveryKeyForStableInfo:dynamicInfo:vouchers:]
- -[TPModel bestWalrusForStableInfo:dynamicInfo:walrusStableChanges:]
- -[TPModel bestWebAccessForStableInfo:dynamicInfo:webAccessStableChanges:]
- -[TPModel calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:error:]
- -[TPModel checkVouchers]
- -[TPModel deletePeerWithID:]
- -[TPModel doesVoucherMatchRecoveryKeys:]
- -[TPModel filterPeerList:byMachineIDs:dispositions:]
- -[TPModel initWithDecrypter:]
- -[TPModel isRecoveryKeyDistrusted:]
- -[TPModel peersByID]
- -[TPModel registerPeerWithPermanentInfo:]
- -[TPModel registerVoucher:]
- -[TPModel setPeersByID:]
- -[TPModel setUncheckedVouchers:]
- -[TPModel setVouchers:]
- -[TPModel trustedPeers]
- -[TPModel uncheckedVouchers]
- -[TPModel untrustedPeerIDsFromTrustedPeers]
- -[TPModel updateDynamicInfo:forPeerWithID:error:]
- -[TPModel updateStableInfo:forPeerWithID:error:]
- -[TPModel vouchers]
- -[TPPeerPermanentInfo initWithMachineID:modelID:epoch:signingPubKey:encryptionPubKey:data:sig:peerID:]
- GCC_except_table1011
- GCC_except_table1019
- GCC_except_table110
- GCC_except_table113
- GCC_except_table115
- GCC_except_table119
- GCC_except_table121
- GCC_except_table124
- GCC_except_table166
- GCC_except_table255
- _OBJC_IVAR_$_TPModel._peersByID
- _OBJC_IVAR_$_TPModel._uncheckedVouchers
- _OBJC_IVAR_$_TPModel._vouchers
- ___184-[TPModel calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:error:]_block_invoke
- ___184-[TPModel calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:error:]_block_invoke.107
- ___43-[TPModel untrustedPeerIDsFromTrustedPeers]_block_invoke
- ___Block_byref_object_copy_.2771
- ___Block_byref_object_dispose_.2772
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s_e33_v32?0"NSString"8"TPPeer"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_40_e8_32r_e33_v32?0"NSString"8"TPPeer"16^B24lr32l8
- ___block_descriptor_40_e8_32s_e33_v32?0"NSString"8"TPPeer"16^B24ls32l8
- ___block_descriptor_56_e8_32s40s48r_e33_v32?0"NSString"8"TPPeer"16^B24ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48s_e33_v32?0"NSString"8"TPPeer"16^B24ls32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e33_v32?0"NSString"8"TPPeer"16^B24ls32l8s40l8s48l8s56l8s64l8r72l8
- ___block_literal_global.1294
- ___block_literal_global.2780
- __unnamed_array_storage.116
- _objc_msgSend$allPeers
- _objc_msgSend$anyTrustedPeerDistrustsOtherPeer:
- _objc_msgSend$calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:error:
- _objc_msgSend$checkVouchers
- _objc_msgSend$doesVoucherMatchRecoveryKeys:
- _objc_msgSend$filterPeerList:byMachineIDs:dispositions:
- _objc_msgSend$initWithMachineID:modelID:epoch:signingPubKey:encryptionPubKey:data:sig:peerID:
- _objc_msgSend$isRecoveryKeyDistrusted:
- _objc_msgSend$isRecoveryKeyEnrolled
- _objc_msgSend$objectForKey:
- _objc_msgSend$setUncheckedVouchers:
- _objc_msgSend$trustedPeers
- _objc_msgSend$uncheckedVouchers
- _objc_msgSend$untrustedPeerIDsFromTrustedPeers
CStrings:
+ "\x02\x12\x13"
+ "\b"
+ "$"
+ "@\"<TPModelDBAdapterProtocol>\""
+ "@\"NSArray\"16@0:8"
+ "@\"TPPBDispositionEvictedMachineID\""
+ "@\"TPPBDispositionGhostedMachineID\""
+ "@\"TPPBDispositionUnknownReasonRemovalMachineID\""
+ "@\"TPPeer\"24@0:8@\"NSString\"16"
+ "@112@0:8@16@24@32@40@48@56@64@72@80@88@96^@104"
+ "@24@0:8@?16"
+ "@32@0:8@16@?24"
+ "@40@0:8q16@24@32"
+ "@80@0:8@16@24Q32@40@48Q56q64^@72"
+ "@88@0:8@16@24Q32@40@48Q56@64@72@80"
+ "AppleTV"
+ "AudioAccessory"
+ "B16@?0@\"TPPeer\"8"
+ "B56@0:8@16@24@32@40@48"
+ "Ignoring TDL Disallowed Machine IDs"
+ "No peer for given peer id: %{public}@"
+ "Peer (%{public}@) has an evicted machine ID (%{public}@)"
+ "Peer (%{public}@) with machine ID (%{public}@) has been removed with an unknown reason"
+ "Peer (%{public}@) with machine ID (%{public}@) has ghosted the TDL"
+ "Skipping voucher for already known beneficiary: %{public}@"
+ "Skipping voucher for unknown sponsor: %{public}@"
+ "T@\"<TPModelDBAdapterProtocol>\",&,N,V_dbAdapter"
+ "T@\"NSString\",?,R,C"
+ "T@\"TPPBDispositionEvictedMachineID\",&,N,V_evictedMachineID"
+ "T@\"TPPBDispositionGhostedMachineID\",&,N,V_ghostedMachineID"
+ "T@\"TPPBDispositionUnknownReasonRemovalMachineID\",&,N,V_unknownReasonRemovalMachineID"
+ "TB,N,V_keyed"
+ "TPModelDBAdapterProtocol"
+ "TPModelInMemoryDb"
+ "TPPBDispositionEvictedMachineID"
+ "TPPBDispositionGhostedMachineID"
+ "TPPBDispositionUnknownReasonRemovalMachineID"
+ "TQ,N,V_creationTime"
+ "TQ,R,N,V_creationTime"
+ "T{?=[96I]},N,V_ctxHMAC"
+ "Unknown peers, distrusting by default: %{public}@"
+ "_creationTime"
+ "_ctxHMAC"
+ "_dbAdapter"
+ "_evictedMachineID"
+ "_ghostedMachineID"
+ "_iterateOverPeersWithBlock:"
+ "_keyed"
+ "_unknownReasonRemovalMachineID"
+ "anyObject"
+ "bestRecoveryKeyForStableInfo:vouchers:"
+ "bestWalrusForStableInfo:walrusStableChanges:"
+ "bestWebAccessForStableInfo:webAccessStableChanges:"
+ "calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:sponsorPeerID:error:"
+ "calculateHmacWithHmacKey:"
+ "calculateHmacWithHmacKey:permanentInfo:stableInfo:dynamicInfo:"
+ "can't update peerID %{public}@: peer does not exist"
+ "copyPeerWithNewDynamicInfo:forPeerWithID:error:"
+ "copyPeerWithNewStableInfo:forPeerWithID:error:"
+ "creationTime"
+ "creation_time"
+ "ctxHMAC"
+ "dbAdapter"
+ "enumeratePeersUsingBlock:"
+ "enumerateVouchersUsingBlock:"
+ "evicted"
+ "evictedMachineID"
+ "filterPeerList:byMachineIDs:sponsorPeerID:dispositions:"
+ "finalKeyedHash"
+ "firstObject"
+ "ghostedFromTDL"
+ "ghostedMachineID"
+ "hasAnyPeers"
+ "hasCreationTime"
+ "hasEvictedMachineID"
+ "hasGhostedMachineID"
+ "hasPotentiallyTrustedPeer"
+ "hasUnknownReasonRemovalMachineID"
+ "initWithDecrypter:dbAdapter:"
+ "initWithKeyedAlgo:key:"
+ "initWithMachineID:modelID:epoch:signingPubKey:encryptionPubKey:creationTime:data:sig:peerID:"
+ "initWithPermanentInfo:stableInfo:dynamicInfo:error:"
+ "initWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:error:"
+ "intersectSet:"
+ "keyed"
+ "keyedHashWithAlgo:key:data:"
+ "peerCount"
+ "permanentInfoWithMachineID:modelID:epoch:signingKeyPair:encryptionKeyPair:creationTime:peerIDHashAlgo:error:"
+ "pickClock:"
+ "possibleSponsorsForCustodianRecoveryKey: %{public}@/%{public}@"
+ "possibleSponsorsForCustodianRecoveryKey: CRK %{public}@/%{public}@ is not trusted"
+ "possibleSponsorsForCustodianRecoveryKey: CRK %{public}@/%{public}@ returning %@"
+ "possibleSponsorsForCustodianRecoveryKey: no sponsors, no distrust"
+ "possibleSponsorsForCustodianRecoveryKey:block:"
+ "possibleSponsorsForRecoveryKey: no sponsors, no distrust"
+ "possibleSponsorsForRecoveryKey: registered recovery key is not trusted"
+ "possibleSponsorsForRecoveryKey: returning %@"
+ "possibleSponsorsForRecoveryKey: sign %{public}@, enc %{public}@"
+ "possibleSponsorsForRecoveryKey:block:"
+ "q24@?0@8@16"
+ "setCreationTime:"
+ "setCtxHMAC:"
+ "setDbAdapter:"
+ "setEvictedMachineID:"
+ "setGhostedMachineID:"
+ "setHasCreationTime:"
+ "setKeyed:"
+ "setUnknownReasonRemovalMachineID:"
+ "sortUsingComparator:"
+ "unknownReason"
+ "unknownReasonRemovalMachineID"
+ "updatePeer:error:"
+ "v16@?0@\"TPPeer\"8"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"TPPeer\"^B>16"
+ "v24@0:8@?<v@?@\"TPVoucher\"^B>16"
+ "v24@?0@\"TPPeer\"8^B16"
+ "v24@?0@\"TPVoucher\"8^B16"
+ "v400@0:8{?=[96I]}16"
+ "verifyHMACWithPermanentInfo:stableInfo:dynamicInfo:hmacKey:hmacSig:"
+ "voucher: evicted machineID %{public}@ %{public}@"
+ "voucher: ghosted machineID %{public}@ %{public}@"
+ "voucher: unknown reason removed machineID %{public}@ %{public}@"
+ "voucherCount"
+ "{?=\"creationTime\"b1\"epoch\"b1}"
+ "{?=\"ctx\"[96I]}"
+ "{?=[96I]}16@0:8"
- "\x02\x15"
- "\x18"
- "@104@0:8@16@24@32@40@48@56@64@72@80@88^@96"
- "@72@0:8@16@24Q32@40@48q56^@64"
- "@80@0:8@16@24Q32@40@48@56@64@72"
- "B40@0:8@16@24^@32"
- "No peer for given peerID: %@"
- "No peer: %{public}@"
- "Peer (%{public}@) unknown, distrusting by default"
- "T@\"NSMutableSet\",&,N,V_uncheckedVouchers"
- "_uncheckedVouchers"
- "allPeers"
- "allVouchers"
- "bestRecoveryKeyForStableInfo:dynamicInfo:vouchers:"
- "bestWalrusForStableInfo:dynamicInfo:walrusStableChanges:"
- "bestWebAccessForStableInfo:dynamicInfo:webAccessStableChanges:"
- "calculateDynamicInfoFromModel:peer:peerPermanentInfo:peerStableInfo:startingDynamicInfo:addingPeerIDs:removingPeerIDs:preapprovedKeys:signingKeyPair:currentMachineIDs:error:"
- "checkVouchers"
- "doesVoucherMatchRecoveryKeys:"
- "filterPeerList:byMachineIDs:dispositions:"
- "initWithDecrypter:"
- "initWithMachineID:modelID:epoch:signingPubKey:encryptionPubKey:data:sig:peerID:"
- "isCustodianRecoveryKeyTrusted: returning %d"
- "isCustodianRecoveryKeyTrusted: size = %lu"
- "isRecoveryKeyDistrusted:"
- "isRecoveryKeyEnrolled: returning %d"
- "isRecoveryKeyEnrolled: sign %{public}@, enc %{public}@, count = %lu"
- "objectForKey:"
- "permanentInfoWithMachineID:modelID:epoch:signingKeyPair:encryptionKeyPair:peerIDHashAlgo:error:"
- "setUncheckedVouchers:"
- "status: peerID %{public}@ has no peer in model"
- "trustedPeers"
- "uncheckedVouchers"
- "untrustedPeerIDsFromTrustedPeers"
- "updateDynamicInfo:forPeerWithID:error:"
- "updateStableInfo:forPeerWithID:error:"
- "{?=\"epoch\"b1}"

```
