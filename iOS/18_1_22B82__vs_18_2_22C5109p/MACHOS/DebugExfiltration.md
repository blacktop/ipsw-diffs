## DebugExfiltration

> `/System/ExclaveKit/System/Library/PrivateFrameworks/DebugExfiltration.framework/DebugExfiltration`

```diff

-51.0.1.0.0
-  __TEXT.__text: 0x1494
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x1f8
-  __TEXT.__constg_swiftt: 0x134
-  __TEXT.__swift5_typeref: 0x77
-  __TEXT.__swift5_reflstr: 0x17
-  __TEXT.__swift5_fieldmd: 0x80
-  __TEXT.__swift5_types: 0x10
+53.60.18.0.0
+  __TEXT.__text: 0x4184
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__const: 0x28a
+  __TEXT.__cstring: 0x478
+  __TEXT.__constg_swiftt: 0x24c
+  __TEXT.__swift5_typeref: 0xce
+  __TEXT.__swift5_reflstr: 0x4c
+  __TEXT.__swift5_fieldmd: 0x10c
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0xd0
-  __TEXT.__eh_frame: 0xa8
-  __DATA.__auth_got: 0xe8
-  __DATA.__got: 0x30
-  __DATA.__auth_ptr: 0x68
-  __DATA.__const: 0x8
-  __DATA.__objc_classlist: 0x20
+  __TEXT.__unwind_info: 0x138
+  __TEXT.__eh_frame: 0x118
+  __DATA.__auth_got: 0x238
+  __DATA.__got: 0x70
+  __DATA.__auth_ptr: 0xa0
+  __DATA.__const: 0xc0
+  __DATA.__objc_classlist: 0x28
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x2d8
-  __DATA.__data: 0x298
+  __DATA.__objc_const: 0x450
+  __DATA.__data: 0x400
+  __DATA.__common: 0x8
   __DATA.__bss: 0x180
+  - /System/ExclaveKit/System/Library/Frameworks/SharedMemory.framework/SharedMemory
   - /System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
+  - /System/ExclaveKit/usr/lib/swift/libswiftC.dylib
   - /System/ExclaveKit/usr/lib/swift/libswiftCore.dylib
+  - /System/ExclaveKit/usr/lib/swift/libswift_errno.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_stdio.dylib
+  - /System/ExclaveKit/usr/lib/swift/libswift_time.dylib
   - /System/ExclaveKit/usr/lib/system/liblibc.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_malloc.dylib
-  Functions: 37
-  Symbols:   162
-  CStrings:  12
+  Functions: 74
+  Symbols:   315
+  CStrings:  31
 
Symbols:
+ _$s12SharedMemory13SegmentAccessCMn
+ _$s17DebugExfiltration0aB14ServiceHandlerP14ReadCompletion10channel_id02rbE6Offsetys6UInt64V_AHtFTj
+ _$s17DebugExfiltration0aB14ServiceHandlerP14ReadCompletion10channel_id02rbE6Offsetys6UInt64V_AHtFTq
+ _$s17DebugExfiltration0aB14ServiceHandlerP15ReadNonBlocking10channel_id6lengthAA0B15RingBufferStateVs6UInt64V_s6UInt32VtFTj
+ _$s17DebugExfiltration0aB14ServiceHandlerP15ReadNonBlocking10channel_id6lengthAA0B15RingBufferStateVs6UInt64V_s6UInt32VtFTq
+ _$s17DebugExfiltration0aB14ServiceHandlerP21NewChannelWithShmemId4name11callback_ep0K5_data8shmem_ids6UInt64VSays5UInt8VG_SuA2JtFTj
+ _$s17DebugExfiltration0aB14ServiceHandlerP21NewChannelWithShmemId4name11callback_ep0K5_data8shmem_ids6UInt64VSays5UInt8VG_SuA2JtFTq
+ _$s17DebugExfiltration0aB14ServiceHandlerP30NewChannelWriteOnlyWithShmemId4name8shmem_ids6UInt64VSays5UInt8VG_AHtFTj
+ _$s17DebugExfiltration0aB14ServiceHandlerP30NewChannelWriteOnlyWithShmemId4name8shmem_ids6UInt64VSays5UInt8VG_AHtFTq
+ _$s17DebugExfiltration0aB14ServiceHandlerP4Read10channel_id6lengthAA0B15RingBufferStateVs6UInt64V_s6UInt32VtFTj
+ _$s17DebugExfiltration0aB14ServiceHandlerP4Read10channel_id6lengthAA0B15RingBufferStateVs6UInt64V_s6UInt32VtFTq
+ _$s17DebugExfiltration0aB14ServiceWrapperC0B10ReadCommon2id6buffer6length8blockings6UInt64VAJ_Spys5UInt8VGs6UInt32VSbtF
+ _$s17DebugExfiltration0aB14ServiceWrapperC0B15ReadNonBlocking2id6buffer6lengths6UInt64VAI_Spys5UInt8VGs6UInt32VtF
+ _$s17DebugExfiltration0aB14ServiceWrapperC0B4Data2id6buffer6lengths6UInt64VAI_SPys5UInt8VGs6UInt32VtF
+ _$s17DebugExfiltration0aB14ServiceWrapperC0B4Read2id6buffer6lengths6UInt64VAI_Spys5UInt8VGs6UInt32VtF
+ _$s17DebugExfiltration0aB14ServiceWrapperC21NewChannelWithSegment4name05shmemH0s6UInt64VSS_12SharedMemory0H6AccessCtF
+ _$s17DebugExfiltration0aB14ServiceWrapperC3desAA0abC0C0C0CvpWvd
+ _$s17DebugExfiltration0aB14ServiceWrapperC9idToShmemSDys6UInt64VAA012ExfilExclaveG0CGvpZ
+ _$s17DebugExfiltration0aB14ServiceWrapperC9idToShmem_WZ
+ _$s17DebugExfiltration0aB14ServiceWrapperC9idToShmem_Wz
+ _$s17DebugExfiltration0aB7ServiceC0C0C10connectionAE9Tightbeam16ClientConnectionC_tcfCTq
+ _$s17DebugExfiltration0aB7ServiceC0C0C30NewChannelWriteOnlyWithShmemId4name8shmem_ids6UInt64VSays5UInt8VG_AJtKF
+ _$s17DebugExfiltration0aB7ServiceC0C0C4Data10channel_id6lengths6UInt64VAJ_s6UInt32VtKF
+ _$s17DebugExfiltration0aB7ServiceC8Selector33_4C69F2FE8FCF28DE7CF9FF9E93E820ECLLO8rawValueAFSgs6UInt64V_tcfCTf4nd_n
+ _$s17DebugExfiltration17ExfilExclaveShmemC11fromSegment6callerAC12SharedMemory0G6AccessC_SStcfCTq
+ _$s17DebugExfiltration17ExfilExclaveShmemC11fromSegment6callerAC12SharedMemory0G6AccessC_SStcfc
+ _$s17DebugExfiltration17ExfilExclaveShmemC11segmentSizes6UInt64VvgTq
+ _$s17DebugExfiltration17ExfilExclaveShmemC11unmapBufferyyFTq
+ _$s17DebugExfiltration17ExfilExclaveShmemC13shmemdebugmsg33_3AE4312FD03FBD43D9D5BBEEC4E5A7A3LL_8function4lineySS_SSSitFTf4nddn_nTm
+ _$s17DebugExfiltration17ExfilExclaveShmemC2id33_3AE4312FD03FBD43D9D5BBEEC4E5A7A3LLs6UInt64VvpWvd
+ _$s17DebugExfiltration17ExfilExclaveShmemC3map33_3AE4312FD03FBD43D9D5BBEEC4E5A7A3LLs13OpaquePointerVSgvpWvd
+ _$s17DebugExfiltration17ExfilExclaveShmemC3seg33_3AE4312FD03FBD43D9D5BBEEC4E5A7A3LL12SharedMemory13SegmentAccessCvpWvd
+ _$s17DebugExfiltration17ExfilExclaveShmemC5getIDs6UInt64VyFTq
+ _$s17DebugExfiltration17ExfilExclaveShmemC6buffer33_3AE4312FD03FBD43D9D5BBEEC4E5A7A3LLSo19sharedmem_mapregionVSgvpWvd
+ _$s17DebugExfiltration17ExfilExclaveShmemC6caller33_3AE4312FD03FBD43D9D5BBEEC4E5A7A3LLSSvpWvd
+ _$s17DebugExfiltration17ExfilExclaveShmemC7segSize33_3AE4312FD03FBD43D9D5BBEEC4E5A7A3LLs6UInt64VvpWvd
+ _$s17DebugExfiltration17ExfilExclaveShmemC9mapBuffer6lengthSvSgs6UInt64V_tF
+ _$s17DebugExfiltration17ExfilExclaveShmemC9mapBuffer6lengthSvSgs6UInt64V_tFTq
+ _$s17DebugExfiltration17ExfilExclaveShmemCMF
+ _$s17DebugExfiltration17ExfilExclaveShmemCMa
+ _$s17DebugExfiltration17ExfilExclaveShmemCMf
+ _$s17DebugExfiltration17ExfilExclaveShmemCMm
+ _$s17DebugExfiltration17ExfilExclaveShmemCMn
+ _$s17DebugExfiltration17ExfilExclaveShmemCN
+ _$s17DebugExfiltration17ExfilExclaveShmemCfD
+ _$s9Tightbeam0A7DecoderV6decode2asS2bm_tF
+ _$s9Tightbeam0A7DecoderV7messageAcA0A7MessageC_tcfC
+ _$s9Tightbeam0A7EncoderV6encodeyySbF
+ _$s9Tightbeam0A7EncoderV6encodeyys5UInt8VF
+ _$s9Tightbeam0A7EncoderV6encodeyys6UInt32VF
+ _$s9Tightbeam0A7MessageC7encoderAA0A7EncoderVyFTj
+ _$s9Tightbeam16ClientConnectionC15allocateMessage4size12capabilitiesAA0aE0CSi_SitKF
+ _$s9Tightbeam16ClientConnectionC4send7messageAA0A7MessageCAG_tKF
+ _$sBi8_WV
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCs6UInt64V_17DebugExfiltration17ExfilExclaveShmemCTgm5Tf4g_n
+ _$sSD8_VariantV8setValue_6forKeyyq_n_xtFs6UInt64V_17DebugExfiltration17ExfilExclaveShmemCTg5
+ _$sSS7cStringSSSPys4Int8VG_tcfC
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSSN
+ _$sSS_5radix9uppercaseSSx_SiSbtcSzRzlufC
+ _$sSa28_allocateBufferUninitialized15minimumCapacitys06_ArrayB0VyxGSi_tFZs5UInt8V_Tgm5
+ _$sSiN
+ _$sSis23CustomStringConvertiblesWP
+ _$sSo17sharedmem_failureV12SharedMemoryEABycfC
+ _$sSo19sharedmem_mapregionVMB
+ _$sSo19sharedmem_mapregionVMF
+ _$sSo19sharedmem_mapregionVML
+ _$sSo19sharedmem_mapregionVMa
+ _$sSo19sharedmem_mapregionVMaTm
+ _$sSo19sharedmem_mapregionVMf
+ _$sSo19sharedmem_mapregionVMn
+ _$sSo19sharedmem_mapregionVWV
+ _$sSo19sharedmem_mapregionVwet
+ _$sSo19sharedmem_mapregionVwst
+ _$sSo27sharedmem_backingmodel_ttagVMB
+ _$sSo27sharedmem_backingmodel_ttagVML
+ _$sSo27sharedmem_backingmodel_ttagVMa
+ _$sSo27sharedmem_backingmodel_ttagVMf
+ _$sSo27sharedmem_backingmodel_ttagVMn
+ _$sSoMXM
+ _$sSvN
+ _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss13OpaquePointerVMn
+ _$ss17_NativeDictionaryV12mutatingFind_8isUniques10_HashTableV6BucketV6bucket_Sb5foundtx_SbtFs6UInt64V_17DebugExfiltration17ExfilExclaveShmemCTg5
+ _$ss17_NativeDictionaryV20_copyOrMoveAndResize8capacity12moveElementsySi_SbtFs6UInt64V_17DebugExfiltration17ExfilExclaveShmemCTg5
+ _$ss17_NativeDictionaryV4copyyyFs6UInt64V_17DebugExfiltration17ExfilExclaveShmemCTg5
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _$ss18_DictionaryStorageC6resize8original8capacity4moveAByxq_Gs05__RawaB0C_SiSbtFZ
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss18_DictionaryStorageCys6UInt64V17DebugExfiltration17ExfilExclaveShmemCGMD
+ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tgmq5
+ _$ss22__RawDictionaryStorageC4find_9hashValues10_HashTableV6BucketV6bucket_Sb5foundtx_SitSHRzlFs6UInt64V_Tg5
+ _$ss22__RawDictionaryStorageC4findys10_HashTableV6BucketV6bucket_Sb5foundtxSHRzlFs6UInt64V_Tg5
+ _$ss23_ContiguousArrayStorageCyypGMD
+ _$ss32_copyCollectionToContiguousArrayys0dE0Vy7ElementQzGxSlRzlFSS8UTF8ViewV_Tgq5
+ _$ss53KEY_TYPE_OF_DICTIONARY_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _$ss5print_9separator10terminatoryypd_S2StF
+ _$ss6HasherV5_hash4seed_S2i_s6UInt64VtFZ
+ _$ss6UInt64VABSzsWL
+ _$ss6UInt64VABSzsWl
+ _$ss6UInt64VMn
+ _$ss6UInt64VSzsMc
+ _$sypN
+ __DATA__TtC17DebugExfiltration17ExfilExclaveShmem
+ __IVARS__TtC17DebugExfiltration17ExfilExclaveShmem
+ __METACLASS_DATA__TtC17DebugExfiltration17ExfilExclaveShmem
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_memcpy16_8
+ ___swift_noop_void_return
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftC
+ __swift_FORCE_LOAD_$_swiftC_$_DebugExfiltration
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_DebugExfiltration
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_DebugExfiltration
+ _bzero
+ _sharedmem_result_success
+ _sharedmem_result_toString
+ _sharedmem_segaccess_parameters
+ _sharedmem_segmap_createLocalSegAccess
+ _sharedmem_segmap_getMappedRegion
+ _sharedmem_segmap_mapRange
+ _sharedmem_segmap_unmapRange
+ _sharedmem_segparameters_getBackingModel
+ _sharedmem_segparameters_getMaxOffset
+ _sharedmem_segparameters_getShmemID
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRetain
+ _swift_endAccess
+ _swift_getForeignTypeMetadata
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_retain
+ _swift_setDeallocating
+ _swift_unexpectedError
+ _symbolic SS
+ _symbolic Si
+ _symbolic Sv
+ _symbolic _____ 12SharedMemory13SegmentAccessC
+ _symbolic _____ 17DebugExfiltration17ExfilExclaveShmemC
+ _symbolic _____ So19sharedmem_mapregionV
+ _symbolic _____ So27sharedmem_backingmodel_ttagV
+ _symbolic _____ s6UInt64V
+ _symbolic _____Sg So19sharedmem_mapregionV
+ _symbolic _____Sg s13OpaquePointerV
+ _symbolic _____y__________G s18_DictionaryStorageC s6UInt64V 17DebugExfiltration17ExfilExclaveShmemC
+ _symbolic _____yypG s23_ContiguousArrayStorageC
CStrings:
+ " bytes from segment "
+ " bytes in shared memory segment "
+ " bytes is available at "
+ " mapped, caller requested "
+ "/Library/Caches/com.apple.xbs/Sources/DebugExclave_exclavekit/debug/DebugExfiltration/ExfiltrationServiceEK.swift"
+ ": incorrect fixed-sized array length, expected 16, got "
+ "Cannot create mapper for segment "
+ "DebugExfiltration/ExfiltrationServiceEK.swift"
+ "NewChannelWriteOnlyWithShmemId(name:shmem_id:)"
+ "Region is not mapped"
+ "_TtC17DebugExfiltration17ExfilExclaveShmem"
+ "buffer"
+ "caller"
+ "des"
+ "id"
+ "map"
+ "seg"
+ "segSize"
+ "unmap range for "

```
