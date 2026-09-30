## AudioCaptureServer

> `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioCaptureServer.framework/AudioCaptureServer`

```diff

-122.104.0.0.0
-  __TEXT.__text: 0x10c58
+139.0.0.0.0
+  __TEXT.__text: 0x113cc
   __TEXT.__auth_stubs: 0x500
-  __TEXT.__const: 0xbe8
-  __TEXT.__gcc_except_tab: 0x8a0
-  __TEXT.__cstring: 0x1c53
+  __TEXT.__const: 0xbd0
+  __TEXT.__gcc_except_tab: 0x8fc
+  __TEXT.__cstring: 0x1bc3
   __TEXT.__oslogstring: 0x97f
-  __TEXT.__unwind_info: 0x688
+  __TEXT.__unwind_info: 0x6c8
   __DATA.__auth_got: 0x288
   __DATA.__got: 0x78
-  __DATA.__const: 0xb28
+  __DATA.__const: 0xb58
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0xe0
   - /System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation
   - /System/ExclaveKit/System/Library/Frameworks/SharedMemory.framework/SharedMemory
   - /System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libc++.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
-  Functions: 310
-  Symbols:   643
+  Functions: 315
+  Symbols:   652
   CStrings:  166
 
Symbols:
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table4
+ GCC_except_table44
+ GCC_except_table48
+ __ZN2ad12checked_spanIK11AudioBufferEC2IPS2_EET_m
+ __ZN2ad12checked_spanIcEC2IPcEET_m
+ __ZN3shm15GetSegMaxOffsetEP24sharedmemory_segaccess_s
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8fe180100IONS1_9__variant15__value_visitorI10overloadedIJZNK3shm16SharedMemoryImpl10MakeReaderERKNS_8optionalINS9_11MemoryRangeEEEE3$_0ZNKSA_10MakeReaderESF_E3$_1EEEEJRNS0_6__baseILNS0_6_TraitE0EJP13sharedmem_mapP16sharedmem_segmapEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8fe180100IONS1_9__variant15__value_visitorI10overloadedIJZNK3shm16SharedMemoryImpl10MakeWriterERKNS_8optionalINS9_11MemoryRangeEEEE3$_0ZNKSA_10MakeWriterESF_E3$_1EEEEJRNS0_6__baseILNS0_6_TraitE0EJP13sharedmem_mapP16sharedmem_segmapEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8fe180100IONS1_9__variant15__value_visitorIZZN3shm16SharedMemoryImpl4ImplD1EvENK3$_0clEvEUlOT_E_EEJRNS0_6__baseILNS0_6_TraitE0EJP13sharedmem_mapP16sharedmem_segmapEEEEEEDcSC_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8fe180100IONS1_9__variant15__value_visitorI10overloadedIJZNK3shm16SharedMemoryImpl10MakeReaderERKNS_8optionalINS9_11MemoryRangeEEEE3$_0ZNKSA_10MakeReaderESF_E3$_1EEEEJRNS0_6__baseILNS0_6_TraitE0EJP13sharedmem_mapP16sharedmem_segmapEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8fe180100IONS1_9__variant15__value_visitorI10overloadedIJZNK3shm16SharedMemoryImpl10MakeWriterERKNS_8optionalINS9_11MemoryRangeEEEE3$_0ZNKSA_10MakeWriterESF_E3$_1EEEEJRNS0_6__baseILNS0_6_TraitE0EJP13sharedmem_mapP16sharedmem_segmapEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8fe180100IONS1_9__variant15__value_visitorIZZN3shm16SharedMemoryImpl4ImplD1EvENK3$_0clEvEUlOT_E_EEJRNS0_6__baseILNS0_6_TraitE0EJP13sharedmem_mapP16sharedmem_segmapEEEEEEDcSC_DpT0_
+ __ZNSt3__16vectorI31captureaudiotypes_audiobuffer_sNS_9allocatorIS1_EEE7reserveEm
+ __ZdaPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
+ _sharedmem_segaccess_parameters
+ _sharedmem_segparameters_getMaxOffset
+ _tb_message_configure_received
- GCC_except_table27
- __ZN12_GLOBAL__N_114kMemoryRangeV2E
- __ZNSt3__16vectorI31captureaudiotypes_audiobuffer_sNS_9allocatorIS1_EEE11__vallocateB8fe180100Em
- __ZNSt3__16vectorI31captureaudiotypes_audiobuffer_sNS_9allocatorIS1_EEEC2Em
- ___memcpy_chk
- _bzero
- _malloc_type_malloc
- _memcpy
- _tb_message_configure_recieved
CStrings:
+ "PRECONDITION FAILURE: [audioBuffer.mData != nullptr] is false"
+ "PRECONDITION FAILURE: [audioBuffer.mDataByteSize > 0] is false"
+ "PRECONDITION FAILURE: [audioBuffer.mNumberChannels > 0] is false"
+ "PRECONDITION FAILURE: [mImpl->mProxy->getPermissions(map) == SHAREDMEMORY_PERMISSIONS_READONLY] is false"
+ "PRECONDITION FAILURE: [mImpl->mProxy->getPermissions(map) == SHAREDMEMORY_PERMISSIONS_READWRITE] is false"
+ "PRECONDITION FAILURE: [mImpl->mProxy->getPermissions(map) == SHAREDMEM_PERMISSIONS_READONLY] is false"
+ "PRECONDITION FAILURE: [mImpl->mProxy->getPermissions(map) == SHAREDMEM_PERMISSIONS_READWRITE] is false"
- "PRECONDITION FAILURE: [abl.mBuffers[i].mData != nullptr] is false"
- "PRECONDITION FAILURE: [abl.mBuffers[i].mDataByteSize > 0] is false"
- "PRECONDITION FAILURE: [abl.mBuffers[i].mNumberChannels > 0] is false"
- "PRECONDITION FAILURE: [mImpl->mProxy->getPermissions(std::get<shm::v1::map*>(mImpl->mMap)) == SHAREDMEMORY_PERMISSIONS_READONLY] is false"
- "PRECONDITION FAILURE: [mImpl->mProxy->getPermissions(std::get<shm::v1::map*>(mImpl->mMap)) == SHAREDMEMORY_PERMISSIONS_READWRITE] is false"
- "PRECONDITION FAILURE: [mImpl->mProxy->getPermissions(std::get<shm::v2::map*>(mImpl->mMap)) == SHAREDMEM_PERMISSIONS_READONLY] is false"
- "PRECONDITION FAILURE: [mImpl->mProxy->getPermissions(std::get<shm::v2::map*>(mImpl->mMap)) == SHAREDMEM_PERMISSIONS_READWRITE] is false"

```
