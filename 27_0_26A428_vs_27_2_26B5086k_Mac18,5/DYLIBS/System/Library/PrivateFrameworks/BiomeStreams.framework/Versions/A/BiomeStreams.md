## BiomeStreams

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x3f1664
-  __TEXT.__objc_methlist: 0x14f1c
-  __TEXT.__const: 0xad134
-  __TEXT.__cstring: 0x313f3
-  __TEXT.__gcc_except_tab: 0x1264
-  __TEXT.__oslogstring: 0xc460
+255.0.2.0.0
+  __TEXT.__text: 0x3f2dc8
+  __TEXT.__objc_methlist: 0x1500c
+  __TEXT.__const: 0xad174
+  __TEXT.__cstring: 0x314e3
+  __TEXT.__gcc_except_tab: 0x12c4
+  __TEXT.__oslogstring: 0xc640
   __TEXT.__dlopen_cstrs: 0x632
-  __TEXT.__constg_swiftt: 0xb2b8
-  __TEXT.__swift5_typeref: 0x54f0
+  __TEXT.__constg_swiftt: 0xb338
+  __TEXT.__swift5_typeref: 0x54e6
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x6e31
-  __TEXT.__swift5_fieldmd: 0xbb70
-  __TEXT.__swift5_capture: 0x2a4
+  __TEXT.__swift5_reflstr: 0x6e41
+  __TEXT.__swift5_fieldmd: 0xbba8
   __TEXT.__swift5_assocty: 0xbf8
+  __TEXT.__swift5_capture: 0x254
   __TEXT.__swift5_proto: 0x1f68
-  __TEXT.__swift5_types: 0x844
+  __TEXT.__swift5_types: 0x84c
   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__unwind_info: 0x10fc8
-  __TEXT.__eh_frame: 0xd888
+  __TEXT.__unwind_info: 0x11018
+  __TEXT.__eh_frame: 0xd800
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x29e60
-  __DATA_CONST.__objc_classlist: 0xe88
+  __DATA_CONST.__objc_classlist: 0xe98
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60b8
+  __DATA_CONST.__objc_selrefs: 0x6178
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x978
-  __DATA_CONST.__objc_arraydata: 0x108
-  __DATA_CONST.__got: 0x1090
-  __AUTH_CONST.__const: 0x139f0
-  __AUTH_CONST.__cfstring: 0x95c0
-  __AUTH_CONST.__objc_const: 0x4d478
+  __DATA_CONST.__objc_arraydata: 0xf8
+  __DATA_CONST.__got: 0x10a0
+  __AUTH_CONST.__const: 0x139c0
+  __AUTH_CONST.__cfstring: 0x95e0
+  __AUTH_CONST.__objc_const: 0x4d5f0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1108
+  __AUTH_CONST.__auth_got: 0x1118
   __AUTH.__objc_data: 0x7b90
-  __AUTH.__data: 0x13490
+  __AUTH.__data: 0x135c0
   __AUTH.__thread_vars: 0x348
   __AUTH.__thread_data: 0xf4
   __AUTH.__thread_bss: 0x458
   __DATA.__objc_ivar: 0x1850
-  __DATA.__data: 0x9c58
+  __DATA.__data: 0x9cc8
   __DATA.__common: 0x1c10
   __DATA_DIRTY.__objc_data: 0x1670
-  __DATA_DIRTY.__data: 0x1e0
+  __DATA_DIRTY.__data: 0x1b0
   __DATA_DIRTY.__bss: 0x4e0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
+  - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 21999
-  Symbols:   48010
-  CStrings:  9209
+  Functions: 22022
+  Symbols:   48088
+  CStrings:  9220
 
Symbols:
+ +[BMStreamBase(PeriodicMaintenance_Private) _atLeastOneSegmentFileInDirectory:fileManager:]
+ -[BMComputeSourceClient sendEvent:account:remoteName:timestamp:signpostID:sendFullEvent:completion:]
+ -[BMComputeSourceServer _sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:acknowledgement:]
+ -[BMComputeSourceServer sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:acknowledgement:]
+ -[BMComputeSubscriptionSubstreamManager _repopulateSubscriptionSubstreamForStream:]
+ -[BMComputeSubscriptionSubstreamManager _resetSubscriptionSubstreamOnUnrealisticFutureFrameForStream:]
+ -[BMComputeSubscriptionSubstreamManager resetSubscriptionSubstreamsOnUnrealisticFutureFrame]
+ -[BMPruner resetStream]
+ -[BMSource sendEvent:timestamp:completion:]
+ -[BMStoreSource _writeEvent:timestamp:signpostID:notifyCompute:completion:]
+ -[BMStoreSource sendEvent:timestamp:completion:]
+ -[BMStoreStream _resetStreamWithConfig:eventDataClass:]
+ -[BMStoreStream resetStream]
+ -[BMStreamBase(PeriodicMaintenance_Private) _executePruningPolicyOnSubscriptionSubstream]
+ -[BMStreamBase(PeriodicMaintenance_Private) _pruneDisabledSubstreams]
+ -[BMStreamBase(PeriodicMaintenance_Private) _pruneEmptyRemotesNotRecentlyModified]
+ -[BMStreamBase(PeriodicMaintenance_Private) _resetMainUnitOnUnrealisticFutureFrame]
+ -[BMStreamBase(PeriodicMaintenance_Private) _resetTombstoneSubstoreOnUnrealisticFutureFrameWithConfig:]
+ -[BMStreamBase(PeriodicMaintenance_Private) _resetTombstoneSubstoresOnUnrealisticFutureFrame]
+ -[BMStreamBase(PeriodicMaintenance_Private) executePruningPolicyForAccount:includeStorageCleanup:]
+ -[BMStreamVirtualTable initWithStream:useCase:schema:publisherBlockWithOptions:acceptPublisherOptions:]
+ -[BPSBiomeStorePublisher _invalidBookmarkError:]
+ -[BPSBiomeStorePublisher validateBookmarkValue:]
+ GCC_except_table8
+ _$s12BiomeStreams11LibraryBaseP33expeditedPruningStreamIdentifiersST_pSS7ElementRts_XPvgZ
+ _$s12BiomeStreams11LibraryBaseP33expeditedPruningStreamIdentifiersST_pSS7ElementRts_XPvgZTj
+ _$s12BiomeStreams11LibraryBaseP33expeditedPruningStreamIdentifiersST_pSS7ElementRts_XPvgZTq
+ _$s12BiomeStreams11LibraryBasePAAE11streamBasesST_pSo08BMStreamD0C7ElementRts_XPvgZTm
+ _$s12BiomeStreams11LibraryBasePAAE33expeditedPruningStreamIdentifiersST_pSS7ElementRts_XPvgZ
+ _$s12BiomeStreams11LibraryBasePAAE33expeditedPruningStreamIdentifiersST_pSS7ElementRts_XPvpZMV
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO02bmD11StreamBasesAF0kL6LookupCSgvsZTm
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO15lockedLibraries_WZTm
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupC6lookupySo08BMStreamK0CSo0N10IdentifieraKcvpWvd
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupCMF
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupCMa
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupCMf
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupCMm
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupCMn
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupCN
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupCfD
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupC6lookupST_pSo12BMStreamBaseC7ElementSTRts_XPycvpWvd
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupCMF
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupCMa
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupCMf
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupCMm
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupCMn
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupCN
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupCfD
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO25lockedBMLibraryStreamBase2os21OSAllocatedUnfairLockVyAF0lM6LookupCSgGvpZ
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO25lockedBMLibraryStreamBase_WZ
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO25lockedBMLibraryStreamBase_Wz
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO26lockedBMLibraryStreamBases2os21OSAllocatedUnfairLockVyAF0lM6LookupCSgGvpZ
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO26lockedBMLibraryStreamBases_WZ
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO26lockedBMLibraryStreamBases_Wz
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO33expeditedPruningStreamIdentifiersST_pSS7ElementSTRts_XPvgZSaySSGAA0D4Base_pXpcfU_
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO33expeditedPruningStreamIdentifiersST_pSS7ElementSTRts_XPvgZTm
+ _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLOAA0D4BaseA2aGP33expeditedPruningStreamIdentifiersST_pSS7ElementRts_XPvgZTW
+ _$sSaySSGSayxGSTsWL
+ _$sSo18BMStreamIdentifieraABSYSCWlTm
+ _$ss12LazySequenceVys07FlattenB0Vys0a3MapB0VySay12BiomeStreams11LibraryBase_pXpGSaySSGGGGAByxGSTsWL
+ _$ss12LazySequenceVys07FlattenB0Vys0a3MapB0VySay12BiomeStreams11LibraryBase_pXpGSaySSGGGGMR
+ _$ss12LazySequenceVys07FlattenB0Vys0a3MapB0VySay12BiomeStreams11LibraryBase_pXpGSaySSGGGGMd
+ _$ss13ManagedBufferCy12BiomeStreams14UnifiedLibraryO0F033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupCSgSo16os_unfair_lock_sVGMR
+ _$ss13ManagedBufferCy12BiomeStreams14UnifiedLibraryO0F033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupCSgSo16os_unfair_lock_sVGMd
+ _$ss13ManagedBufferCy12BiomeStreams14UnifiedLibraryO0F033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupCSgSo16os_unfair_lock_sVGMR
+ _$ss13ManagedBufferCy12BiomeStreams14UnifiedLibraryO0F033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupCSgSo16os_unfair_lock_sVGMd
+ _OBJC_CLASS_$_BMFrameStore
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ __100-[BMComputeSourceClient sendEvent:account:remoteName:timestamp:signpostID:sendFullEvent:completion:]_block_invoke
+ __89-[BMStreamBase(PeriodicMaintenance_Private) _executePruningPolicyOnSubscriptionSubstream]_block_invoke
+ __89-[BMStreamBase(PeriodicMaintenance_Private) _executePruningPolicyOnSubscriptionSubstream]_block_invoke_3
+ __98-[BMStreamBase(PeriodicMaintenance_Private) executePruningPolicyForAccount:includeStorageCleanup:]_block_invoke
+ __Block_byref_object_copy_
+ __Block_byref_object_dispose_
+ __DATA__TtCOO12BiomeStreams14UnifiedLibraryP33_850BEB6472663B017EAF49437FB662E47Library16StreamBaseLookup
+ __DATA__TtCOO12BiomeStreams14UnifiedLibraryP33_850BEB6472663B017EAF49437FB662E47Library17StreamBasesLookup
+ __IVARS__TtCOO12BiomeStreams14UnifiedLibraryP33_850BEB6472663B017EAF49437FB662E47Library16StreamBaseLookup
+ __IVARS__TtCOO12BiomeStreams14UnifiedLibraryP33_850BEB6472663B017EAF49437FB662E47Library17StreamBasesLookup
+ __METACLASS_DATA__TtCOO12BiomeStreams14UnifiedLibraryP33_850BEB6472663B017EAF49437FB662E47Library16StreamBaseLookup
+ __METACLASS_DATA__TtCOO12BiomeStreams14UnifiedLibraryP33_850BEB6472663B017EAF49437FB662E47Library17StreamBasesLookup
+ __OBJC_$_CLASS_METHODS_BMStreamBase(Tombstones_Project|Tombstones|PeriodicMaintenance|PeriodicMaintenance_Private|Subscriptions_Project|Subscriptions)
+ __OBJC_$_INSTANCE_METHODS_BMStreamBase(Tombstones_Project|Tombstones|PeriodicMaintenance|PeriodicMaintenance_Private|Subscriptions_Project|Subscriptions)
+ ___100-[BMComputeSourceClient sendEvent:account:remoteName:timestamp:signpostID:sendFullEvent:completion:]_block_invoke
+ ___139-[BMComputeSourceServer _sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:acknowledgement:]_block_invoke
+ ___48-[BMStoreSource sendEvent:timestamp:completion:]_block_invoke
+ ___48-[BMStoreSource sendEvent:timestamp:completion:]_block_invoke_2
+ ___89-[BMStreamBase(PeriodicMaintenance_Private) _executePruningPolicyOnSubscriptionSubstream]_block_invoke
+ ___89-[BMStreamBase(PeriodicMaintenance_Private) _executePruningPolicyOnSubscriptionSubstream]_block_invoke_2
+ ___89-[BMStreamBase(PeriodicMaintenance_Private) _executePruningPolicyOnSubscriptionSubstream]_block_invoke_3
+ ___98-[BMStreamBase(PeriodicMaintenance_Private) executePruningPolicyForAccount:includeStorageCleanup:]_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0l
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0l
+ __os_feature_enabled_impl
+ _kTCCServiceSiriAccess
+ _objc_msgSend$_invalidBookmarkError:
+ _objc_msgSend$_repopulateSubscriptionSubstreamForStream:
+ _objc_msgSend$_resetMainUnitOnUnrealisticFutureFrame
+ _objc_msgSend$_resetStreamWithConfig:eventDataClass:
+ _objc_msgSend$_resetSubscriptionSubstreamOnUnrealisticFutureFrameForStream:
+ _objc_msgSend$_resetTombstoneSubstoreOnUnrealisticFutureFrameWithConfig:
+ _objc_msgSend$_resetTombstoneSubstoresOnUnrealisticFutureFrame
+ _objc_msgSend$_sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:acknowledgement:
+ _objc_msgSend$_writeEvent:timestamp:signpostID:notifyCompute:completion:
+ _objc_msgSend$executePruningPolicyForAccount:includeStorageCleanup:
+ _objc_msgSend$initWithStream:permission:config:
+ _objc_msgSend$initWithStream:useCase:schema:publisherBlockWithOptions:acceptPublisherOptions:
+ _objc_msgSend$isTimeTravelStreamResetEnabled
+ _objc_msgSend$isTimeTravelStreamResetEnabledForConfig:
+ _objc_msgSend$resetOnUnrealisticFutureFrame
+ _objc_msgSend$resetStream
+ _objc_msgSend$resetStreamWithReason:
+ _objc_msgSend$resetSubscriptionSubstreamsOnUnrealisticFutureFrame
+ _objc_msgSend$resetSubstoreOnUnrealisticFutureFrame
+ _objc_msgSend$sendEvent:account:remoteName:timestamp:signpostID:sendFullEvent:completion:
+ _objc_msgSend$sendEvent:timestamp:completion:
+ _objc_msgSend$sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:acknowledgement:
+ _objc_msgSend$timestampIsUnreachablyInTheFuture:
+ _symbolic So12BMStreamBaseC_____Kc So18BMStreamIdentifiera
+ _symbolic _____ 12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupC
+ _symbolic _____ 12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupC
+ _symbolic _____So12BMStreamBaseCXjyc lST_px7ElementRts_XPXGMq
+ _symbolic _____y_____Sg_____G s13ManagedBufferCsRi__rlE 12BiomeStreams14UnifiedLibraryO0F033_850BEB6472663B017EAF49437FB662E4LLO16StreamBaseLookupC So16os_unfair_lock_sV
+ _symbolic _____y_____Sg_____G s13ManagedBufferCsRi__rlE 12BiomeStreams14UnifiedLibraryO0F033_850BEB6472663B017EAF49437FB662E4LLO17StreamBasesLookupC So16os_unfair_lock_sV
+ _symbolic _____y_____y_____ySay______pXpGSaySSGGGG s12LazySequenceV s07FlattenB0V s0a3MapB0V 12BiomeStreams11LibraryBaseP
+ executePruningPolicyForAccount:includeStorageCleanup:.onceToken
- $sSo18BMStreamIdentifieraSo0A4BaseCs5Error_pIeggozo_AbDsAE_pIegnrzo_TRTA
- $sSo18BMStreamIdentifieraSo0A4BaseCs5Error_pIegnrzo_AbDsAE_pIeggozo_TRTA
- +[BMStreamBase(PeriodicMaintenance) _atLeastOneSegmentFileInDirectory:fileManager:]
- -[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]
- -[BMStreamBase(PeriodicMaintenance) _pruneDisabledSubstreams]
- -[BMStreamBase(PeriodicMaintenance) _pruneEmptyRemotesNotRecentlyModified]
- -[BPSBiomeStorePublisher validateBookmark:]
- _$s12BiomeStreams13StorableValueOACSQAAWlTm
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO02bmD14StreamBaseFuncSo08BMStreamL0CSo0N10IdentifieraKcSgvgZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO02bmD14StreamBaseFuncSo08BMStreamL0CSo0N10IdentifieraKcSgvsZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO02bmD14StreamBaseFuncSo08BMStreamL0CSo0N10IdentifieraKcSgvsZyALzYbXEfU_
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO02bmD15StreamBasesFuncST_pSo12BMStreamBaseC7ElementSTRts_XPycSgvgZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO02bmD15StreamBasesFuncST_pSo12BMStreamBaseC7ElementSTRts_XPycSgvsZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO02bmD15StreamBasesFuncST_pSo12BMStreamBaseC7ElementSTRts_XPycSgvsZyALzYbXEfU_
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO13dataArtifactsST_pAA0D8ArtifactO04DataL0_pXp7ElementSTRts_XPvgZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO29lockedBMLibraryStreamBaseFunc2os21OSAllocatedUnfairLockVySo08BMStreamM0CSo0S10IdentifieraKcSgGvpZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO29lockedBMLibraryStreamBaseFunc_WZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO29lockedBMLibraryStreamBaseFunc_Wz
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO30lockedBMLibraryStreamBasesFunc2os21OSAllocatedUnfairLockVyST_pSo12BMStreamBaseC7ElementSTRts_XPycSgGvpZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO30lockedBMLibraryStreamBasesFunc_WZ
- _$s12BiomeStreams14UnifiedLibraryO0D033_850BEB6472663B017EAF49437FB662E4LLO30lockedBMLibraryStreamBasesFunc_Wz
- _$sSo18BMStreamIdentifieraSo0A4BaseCs5Error_pIeggozo_AbDsAE_pIegnrzo_TRTA
- _$sSo18BMStreamIdentifieraSo0A4BaseCs5Error_pIeggozo_AbDsAE_pIegnrzo_TRTATm
- _$sSo18BMStreamIdentifieraSo0A4BaseCs5Error_pIegnrzo_AbDsAE_pIeggozo_TR
- _$sSo18BMStreamIdentifieraSo0A4BaseCs5Error_pIegnrzo_AbDsAE_pIeggozo_TRTA
- _$ss13ManagedBufferCyST_pSo12BMStreamBaseC7ElementSTRts_XPycSgSo16os_unfair_lock_sVGMR
- _$ss13ManagedBufferCyST_pSo12BMStreamBaseC7ElementSTRts_XPycSgSo16os_unfair_lock_sVGMd
- _$ss13ManagedBufferCySo12BMStreamBaseCSo0C10IdentifieraKcSgSo16os_unfair_lock_sVGMR
- _$ss13ManagedBufferCySo12BMStreamBaseCSo0C10IdentifieraKcSgSo16os_unfair_lock_sVGMd
- __68-[BMStreamBase(PeriodicMaintenance) executePruningPolicyForAccount:]_block_invoke
- __81-[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]_block_invoke
- __81-[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]_block_invoke_3
- __89-[BMComputeSourceClient sendEvent:account:remoteName:timestamp:signpostID:sendFullEvent:]_block_invoke
- __OBJC_$_CLASS_METHODS_BMStreamBase(Tombstones_Project|Tombstones|PeriodicMaintenance|Subscriptions_Project|Subscriptions)
- __OBJC_$_INSTANCE_METHODS_BMStreamBase(Tombstones_Project|Tombstones|PeriodicMaintenance|Subscriptions_Project|Subscriptions)
- ___122-[BMComputeSourceServer sendEventWithStreamIdentifier:timestamp:signpostID:eventData:eventDataVersion:account:remoteName:]_block_invoke
- ___37-[BMStoreSource sendEvent:timestamp:]_block_invoke
- ___37-[BMStoreSource sendEvent:timestamp:]_block_invoke_2
- ___68-[BMStreamBase(PeriodicMaintenance) executePruningPolicyForAccount:]_block_invoke
- ___81-[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]_block_invoke
- ___81-[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]_block_invoke_2
- ___81-[BMStreamBase(PeriodicMaintenance) _executePruningPolicyOnSubscriptionSubstream]_block_invoke_3
- ___89-[BMComputeSourceClient sendEvent:account:remoteName:timestamp:signpostID:sendFullEvent:]_block_invoke
- _symbolic _____So12BMStreamBaseC______pIeggozo_ So18BMStreamIdentifiera s5ErrorP
- _symbolic _____So12BMStreamBaseC______pIegnrzo_ So18BMStreamIdentifiera s5ErrorP
- _symbolic _____ySo12BMStreamBaseC_____KcSg_____G s13ManagedBufferCsRi__rlE So18BMStreamIdentifiera So16os_unfair_lock_sV
- _symbolic _____y_____So12BMStreamBaseCXjycSg_____G s13ManagedBufferCsRi__rlE lST_px7ElementRts_XPXGMq So16os_unfair_lock_sV
- executePruningPolicyForAccount:.onceToken
CStrings:
+ "%@ %@ for %@, so any state derived from it has to be rebuilt"
+ "-resetStream is not supported on a device-specific pruner for '%@'"
+ "AppExclusions"
+ "BMBiomeScheduler for %@ is discarding a latest event time of %@ that is unreachably in the future, and resuming from event time %@"
+ "Device.Wireless.BluetoothPowerEnabled"
+ "IntelligenceFlow"
+ "Unable to enumerate remotes of %{public}@ to check their tombstones: %@"
+ "[_useCase isEqual:BMUseCasePruner]"
+ "cannot be resolved"
+ "com.apple.TCC.kTCCServiceSiriAccess.authorization.changed"
+ "com.apple.biome.compute-source-delivery"
+ "com.apple.biome.reset-stream"
+ "no subscription source for %{public}@; its %lu subscriptions are not registered on disk until they are donated again"
+ "repopulating %lu subscriptions into %{public}@:subscriptions after resetting it"
- "CarPlay.Connected"
- "Device.Wireless.CellularQualityStatus"
- "Siri.Remembers.Intent"
```
