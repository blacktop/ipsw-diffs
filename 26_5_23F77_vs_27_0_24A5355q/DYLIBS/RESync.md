## RESync

> `/System/Library/PrivateFrameworks/RESync.framework/RESync`

```diff

-403.120.1.0.0
-  __TEXT.__text: 0x7bd44
-  __TEXT.__auth_stubs: 0xef0
+453.0.0.0.11
+  __TEXT.__text: 0x783cc
   __TEXT.__objc_methlist: 0x2d4
-  __TEXT.__const: 0x211f
-  __TEXT.__cstring: 0x722a
-  __TEXT.__oslogstring: 0x4633
-  __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methname: 0x8d8
-  __TEXT.__objc_methtype: 0x883
-  __TEXT.__objc_stubs: 0x6a0
-  __DATA_CONST.__got: 0x70
+  __TEXT.__const: 0x1fe8
+  __TEXT.__cstring: 0x6dee
+  __TEXT.__oslogstring: 0x455e
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x470
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x780
-  __AUTH_CONST.__const: 0x3960
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x3858
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x5e8
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__weak_auth_got: 0x20
+  __AUTH_CONST.__auth_got: 0x790
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0x18
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x108
-  __DATA.__common: 0x11f8
+  __DATA.__common: 0x1148
   __DATA.__bss: 0x128
+  __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__common: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/Network.framework/Network
-  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libc++abi.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F6DBAAA-6326-30F2-A5AB-2576582A2484
-  Functions: 2364
-  Symbols:   5961
-  CStrings:  1167
+  UUID: 168DD46B-DC85-3846-95CD-AAB70C85F947
+  Functions: 2332
+  Symbols:   5836
+  CStrings:  996
 
Symbols:
+ _.str.108
+ _.str.109
+ _.str.110
+ _.str.167
+ _.str.168
+ _.str.30
+ _.str.31
+ _.str.46
+ _.str.48
+ _.str.49
+ _.str.50
+ _RESyncProtocolLayerObserverOnReleaseFromSync
+ _RESyncProtocolLayerObserverOnTakeForSync
+ _RESyncSessionReleasePeer
+ _RESyncSessionRelievePressure
+ _RESyncSessionTakePeer
+ _RESyncSyncableTypeInfoSetSyncToSharedSimulation
+ _RESyncSyncableTypeInfoSyncToSharedSimulation
+ __ZGVZN2re22introspectionAllocatorEvE9allocator
+ __ZN12_GLOBAL__N_123SyncCustomProtocolLayer11takeForSyncEPKN2re14ProtocolHandleE
+ __ZN12_GLOBAL__N_123SyncCustomProtocolLayer15releaseFromSyncEPKN2re14ProtocolHandleE
+ __ZN2re10PacketPool15relievePressureEm
+ __ZN2re11SyncSession15relievePressureEm
+ __ZN2re15MallocAllocator11alloc_typedEmmy
+ __ZN2re15NWProtocolLayer11takeForSyncEPKNS_14ProtocolHandleE
+ __ZN2re15NWProtocolLayer15releaseFromSyncEPKNS_14ProtocolHandleE
+ __ZN2re16AlignedAllocator11alloc_typedEmmy
+ __ZN2re16TcpProtocolLayer11takeForSyncEPKNS_14ProtocolHandleE
+ __ZN2re16TcpProtocolLayer15releaseFromSyncEPKNS_14ProtocolHandleE
+ __ZN2re17IntrospectionBase7prepareEv
+ __ZN2re17SyncObjectManager11takeForSyncEy
+ __ZN2re17SyncObjectManager15releaseFromSyncEy
+ __ZN2re18DebugProtocolLayer11takeForSyncEPKNS_14ProtocolHandleE
+ __ZN2re18DebugProtocolLayer15releaseFromSyncEPKNS_14ProtocolHandleE
+ __ZN2re19MallocZoneAllocator11alloc_typedEmmy
+ __ZN2re20SharedAppSyncManager11takeForSyncEy
+ __ZN2re20SharedAppSyncManager15releaseFromSyncEy
+ __ZN2re21StackScratchAllocator11alloc_typedEmmy
+ __ZN2re22MultipeerProtocolLayer11takeForSyncEPKNS_14ProtocolHandleE
+ __ZN2re22MultipeerProtocolLayer15releaseFromSyncEPKNS_14ProtocolHandleE
+ __ZN2re8snapshot12EncoderOPACK27serializePolymorphicPointerEPKvyNS_11StringSliceERKNS_17FunctionForwarderIFvRNS0_7EncoderES3_EEE
+ __ZN2re9Transport11takeForSyncEy
+ __ZN2re9Transport15releaseFromSyncEy
+ __ZNK2re22IntrospectionStructure14ensurePreparedEv
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIiPN2re18DebugProtocolLayerEEENS_22__unordered_map_hasherIiNS_4pairIKiS4_EENS_4hashIiEENS_8equal_toIiEEEENS_21__unordered_map_equalIiS9_SD_SB_EENS_9allocatorIS9_EEE4findIiEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__110__function12__value_funcIFbPKvPvEED2B9fqn220100Ev
+ __ZNSt3__110__function12__value_funcIFvPvEE4swapB9fqn220100ERS4_
+ __ZNSt3__110__function12__value_funcIFvPvEED2B9fqn220100Ev
+ __ZNSt3__110unique_ptrIN2re20SharedAppSyncManager9PeerStateENS1_11SyncDeleterIS3_EEE5resetB9fqn220100EPS3_
+ __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEED1B9fqn220100Ev
+ __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS7_EEENS3_ISB_EEED1B9fqn220100Ev
+ __ZNSt3__114__thread_proxyB9fqn220100INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS8_EEEEEPvSD_
+ __ZNSt3__125__throw_bad_function_callB9fqn220100Ev
+ __ZNSt3__127__insertion_sort_incompleteB9fqn220100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEbT1_S9_T0_
+ __ZSt28__throw_bad_array_new_lengthB9fqn220100v
+ __ZZN2re22introspectionAllocatorEvE9allocator
+ _mach_task_self_
+ _malloc_type_aligned_alloc
+ _malloc_zone_pressure_relief
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x8
+ _semaphore_create
+ _semaphore_destroy
+ _semaphore_signal
+ _semaphore_timedwait
- _.str.133
- _.str.134
- _.str.135
- _.str.192
- _.str.193
- _.str.194
- _.str.32
- _.str.37
- _.str.60
- _.str.61
- _.str.62
- _.str.64
- _.str.65
- _.str.66
- _RESyncCustomProtocolLayerOnResponsive
- _RESyncCustomProtocolLayerOnUnresponsive
- _RESyncSessionPausePeer
- _RESyncSessionResumePeer
- __ZGVZN2re22introspectionAllocatorEvE13baseAllocator
- __ZGVZN2re22introspectionAllocatorEvE17autoFreeAllocator
- __ZN12_GLOBAL__N_120SessionObserverProxy12peerDidPauseEPN2re7SessionEy
- __ZN12_GLOBAL__N_120SessionObserverProxy13peerDidResumeEPN2re7SessionEy
- __ZN2re11HashSetBaseINS_13DynamicStringES1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE11setCapacityEj
- __ZN2re11HashSetBaseINS_13DynamicStringES1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE4initEPNS_9AllocatorEj
- __ZN2re11HashSetBaseINS_13DynamicStringES1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE6deinitEv
- __ZN2re11HashSetBaseINS_13DynamicStringES1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE9addAsCopyEjmRKS1_SB_
- __ZN2re11HashSetBaseINS_13DynamicStringES1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE9addAsMoveEjmRKS1_OS1_
- __ZN2re11HashSetBaseIPvS1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE11setCapacityEj
- __ZN2re11HashSetBaseIPvS1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE3addERKS1_
- __ZN2re11HashSetBaseIPvS1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE4initEPNS_9AllocatorEj
- __ZN2re11HashSetBaseIPvS1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE5clearEv
- __ZN2re11HashSetBaseIPvS1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE6deinitEv
- __ZN2re11HashSetBaseIPvS1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE6removeERKS1_
- __ZN2re12DynamicArrayINS_15DataArrayHandleINS_8internal13TypeInfoIndexEEEE11setCapacityEm
- __ZN2re12DynamicArrayINS_15DataArrayHandleINS_8internal13TypeInfoIndexEEEE6deinitEv
- __ZN2re12DynamicArrayINS_4PairIbNS_5EventINS_7SessionEJyEE12SubscriptionELb1EEEE12growCapacityEm
- __ZN2re12DynamicArrayINS_8internal13UnionTypeInfoEE11setCapacityEm
- __ZN2re12DynamicArrayINS_8internal13UnionTypeInfoEE6deinitEv
- __ZN2re15MallocAllocator5allocEmm
- __ZN2re16AlignedAllocator5allocEmm
- __ZN2re17SyncObjectManager10resumePeerEy
- __ZN2re17SyncObjectManager12onPeerPausedEPNS_7SessionEy
- __ZN2re17SyncObjectManager13onPeerResumedEPNS_7SessionEy
- __ZN2re17SyncObjectManager9pausePeerEy
- __ZN2re19MallocZoneAllocator5allocEmm
- __ZN2re20SharedAppSyncManager10resumePeerEy
- __ZN2re20SharedAppSyncManager12onPeerPausedEPNS_7SessionEy
- __ZN2re20SharedAppSyncManager13onPeerResumedEPNS_7SessionEy
- __ZN2re20SharedAppSyncManager9pausePeerEy
- __ZN2re21StackScratchAllocator5allocEmm
- __ZN2re26SyncReliableOrderedUnicast5pauseEv
- __ZN2re26SyncReliableOrderedUnicast6resumeEv
- __ZN2re26SyncReliableOrderedUnicastD2Ev
- __ZN2re27ThreadSafeAutoFreeAllocator4freeEPv
- __ZN2re27ThreadSafeAutoFreeAllocator5allocEmm
- __ZN2re27ThreadSafeAutoFreeAllocatorC1EPKcRNS_9AllocatorE
- __ZN2re27ThreadSafeAutoFreeAllocatorD0Ev
- __ZN2re27ThreadSafeAutoFreeAllocatorD1Ev
- __ZN2re27ThreadSafeAutoFreeAllocatorD2Ev
- __ZN2re5EventINS_7SessionEJyEE11unsubscribeINS_17SyncObjectManagerEEEvPT_
- __ZN2re5EventINS_7SessionEJyEE11unsubscribeINS_20SharedAppSyncManagerEEEvPT_
- __ZN2re7Session18onConnectionPausedEy
- __ZN2re7Session19onConnectionResumedEy
- __ZN2re8SyncCast5pauseEv
- __ZN2re8SyncCast6resumeEv
- __ZN2re8internal8CallableIZNS_9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEE8moveIntoEPv
- __ZN2re8internal8CallableIZNS_9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEED0Ev
- __ZN2re8internal8CallableIZNS_9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEED1Ev
- __ZN2re8internal8CallableIZNS_9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEE8moveIntoEPv
- __ZN2re8internal8CallableIZNS_9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEED0Ev
- __ZN2re8internal8CallableIZNS_9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEED1Ev
- __ZN2re8snapshot12EncoderOPACK27serializePolymorphicPointerEPKvyRKNS_17FunctionForwarderIFvRNS0_7EncoderES3_EEE
- __ZN2re8snapshot13BufferDecoder7readRawEPvm
- __ZN2re9DataArrayINS_10ConnectionEE10allocBlockEv
- __ZN2re9DataArrayINS_12TypeRegistry18TypeNameAndVersionEE10allocBlockEv
- __ZN2re9DataArrayINS_21PerFrameAllocatorImplEE10allocBlockEv
- __ZN2re9DataArrayINS_8internal13TypeInfoIndexEE10allocBlockEv
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE10allocEntryEjm
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE11addInternalIRKS3_JRKS5_EEERS5_RKNSA_10FindResultEOT_DpOT0_
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE11setCapacityEj
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE12addOrReplaceERKS3_RKS5_
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE14removeInternalENSA_10FindResultE
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE3addERKS3_RKS5_
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE4initEPNS_9AllocatorEj
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE4moveEOSA_
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE5clearEv
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE6deinitEv
- __ZN2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE6removeERKS3_
- __ZN2re9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleE
- __ZN2re9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleE
- __ZNK2re27ThreadSafeAutoFreeAllocator10statisticsEv
- __ZNK2re27ThreadSafeAutoFreeAllocator6parentEv
- __ZNK2re8internal8CallableIZNS_9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEE4sizeEv
- __ZNK2re8internal8CallableIZNS_9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEE9cloneIntoEPv
- __ZNK2re8internal8CallableIZNS_9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEEclEv
- __ZNK2re8internal8CallableIZNS_9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEE4sizeEv
- __ZNK2re8internal8CallableIZNS_9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEE9cloneIntoEPv
- __ZNK2re8internal8CallableIZNS_9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEEclEv
- __ZNK2re9HashTableINS_9SharedPtrINS_10SyncObjectEEENS_8internal18SyncSnapshotEventsENS_4HashIS3_EENS_7EqualToIS3_EELb1ELb0EE9findEntryIS3_EENSA_10FindResultERKT_m
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeIiPN2re18DebugProtocolLayerEEENS_22__unordered_map_hasherIiNS_4pairIKiS4_EENS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findIiEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
- __ZNSt3__110__function12__value_funcIFbPKvPvEED2B9nqn210106Ev
- __ZNSt3__110__function12__value_funcIFvPvEE4swapB9nqn210106ERS4_
- __ZNSt3__110__function12__value_funcIFvPvEED2B9nqn210106Ev
- __ZNSt3__110unique_ptrIN2re20SharedAppSyncManager9PeerStateENS1_11SyncDeleterIS3_EEE5resetB9nqn210106EPS3_
- __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEED1B9nqn210106Ev
- __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS7_EEENS3_ISB_EEED1B9nqn210106Ev
- __ZNSt3__114__thread_proxyB9nqn210106INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS8_EEEEEPvSD_
- __ZNSt3__125__throw_bad_function_callB9nqn210106Ev
- __ZNSt3__127__insertion_sort_incompleteB9nqn210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEbT1_S9_T0_
- __ZNSt3__15alignEmmRPvRm
- __ZSt28__throw_bad_array_new_lengthB9nqn210106v
- __ZTIN2re27ThreadSafeAutoFreeAllocatorE
- __ZTIN2re8internal8CallableIZNS_9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEEE
- __ZTIN2re8internal8CallableIZNS_9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEEE
- __ZTSN2re27ThreadSafeAutoFreeAllocatorE
- __ZTSN2re8internal8CallableIZNS_9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEEE
- __ZTSN2re8internal8CallableIZNS_9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEEE
- __ZTVN2re27ThreadSafeAutoFreeAllocatorE
- __ZTVN2re8internal8CallableIZNS_9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEEE
- __ZTVN2re8internal8CallableIZNS_9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleEE3$_0FvvEJEEE
- __ZThn24_N2re7Session18onConnectionPausedEy
- __ZThn24_N2re7Session19onConnectionResumedEy
- __ZThn24_N2re9Transport12onResponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleE
- __ZThn24_N2re9Transport14onUnresponsiveEPNS_13ProtocolLayerEPNS_14ProtocolHandleE
- __ZZN2re22introspectionAllocatorEvE13baseAllocator
- __ZZN2re22introspectionAllocatorEvE17autoFreeAllocator
- __ZZN2re5EventINS_7SessionEJyEE18createSubscriptionINS_17SyncObjectManagerEEENS2_12SubscriptionEPT_MS6_F20REEventHandlerResultPS1_yEENUlS9_RKS5_OyE_8__invokeES9_SD_SE_
- __ZZN2re5EventINS_7SessionEJyEE18createSubscriptionINS_20SharedAppSyncManagerEEENS2_12SubscriptionEPT_MS6_F20REEventHandlerResultPS1_yEENUlS9_RKS5_OyE_8__invokeES9_SD_SE_
- ___func__._ZN2re11HashSetBaseIPvS1_NS_8internal10ValueAsKeyIS1_EENS_4HashIS1_EENS_7EqualToIS1_EELb1ELb0EE4initEPNS_9AllocatorEj
- _malloc_type_posix_memalign
- _objc_retain_x27
CStrings:
+ "RESyncProtocolLayerObserverOnReleaseFromSync"
+ "RESyncProtocolLayerObserverOnTakeForSync"
+ "RESyncSessionReleasePeer"
+ "RESyncSessionTakePeer"
+ "alloc_typed"
+ "allocation failure: C string of %zu bytes"
+ "assertion failure: (flags_ & kPrepared) "
+ "ensurePrepared"
+ "flags_ & kPrepared"
+ "release != __null"
+ "take != __null"
- " "
- "!isInitialized() || m_allocator == other.m_allocator"
- "!sharedTypeInfo().constructor"
- "!sharedTypeInfo().destructor"
- "#16@0:8"
- ".cxx_construct"
- ".cxx_destruct"
- "@\"<MCSessionPrivateDelegate>\""
- "@\"MCSession\""
- "@\"NSLock\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_nw_listener>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8^v16"
- "@32@0:8:16@24"
- "@32@0:8@16^{MultipeerProtocolLayer=^^?{ArcRefCount=(isa_t=^v)}^{Allocator}^{ProtocolLayerListener}{ObjCObject=@}{ObjCObject=@}{Address={DynamicString=^{Allocator}(?={?=(?={?=b1b63}Q)*Q}{?=b1b7[23c]})}}}24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "C String of %zu bytes"
- "MCSessionHandler"
- "MCSessionPrivateDelegate"
- "NSObject"
- "NWListener"
- "NWProtocolDelegate"
- "Pausing peerID %llu."
- "Q16@0:8"
- "REMultipeerHelper"
- "RESyncCustomProtocolLayerOnResponsive"
- "RESyncCustomProtocolLayerOnUnresponsive"
- "Resuming peerID %llu"
- "Sending data on paused connection '%s', channel %d"
- "Sending sync data on paused connection to %llx ('%s'): %s"
- "T#,R"
- "T@\"<MCSessionPrivateDelegate>\",W,N,V_nextDelegate"
- "T@\"MCSession\",&,N,V_session"
- "T@\"NSLock\",&,N,V_handlesLock"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "T^{MultipeerProtocolLayer=^^?{ArcRefCount=(isa_t=^v)}^{Allocator}^{ProtocolLayerListener}{ObjCObject=@}{ObjCObject=@}{Address={DynamicString=^{Allocator}(?={?=(?={?=b1b63}Q)*Q}{?=b1b7[23c]})}}},N,V_protocolLayer"
- "T^{ProtocolLayerListener=^^?},N,V_listener"
- "T{DynamicArray<re::SharedPtr<(anonymous namespace)::MCProtocolHandle>>=^{Allocator}QQI^v},N,V_handles"
- "UTF8String"
- "Vv16@0:8"
- "^v"
- "^{MultipeerProtocolLayer=^^?{ArcRefCount=(isa_t=^v)}^{Allocator}^{ProtocolLayerListener}{ObjCObject=@}{ObjCObject=@}{Address={DynamicString=^{Allocator}(?={?=(?={?=b1b63}Q)*Q}{?=b1b7[23c]})}}}"
- "^{MultipeerProtocolLayer=^^?{ArcRefCount=(isa_t=^v)}^{Allocator}^{ProtocolLayerListener}{ObjCObject=@}{ObjCObject=@}{Address={DynamicString=^{Allocator}(?={?=(?={?=b1b63}Q)*Q}{?=b1b7[23c]})}}}16@0:8"
- "^{ProtocolLayerListener=^^?}"
- "^{ProtocolLayerListener=^^?}16@0:8"
- "^{_NSZone=}16@0:8"
- "_handles"
- "_handlesLock"
- "_listener"
- "_nextDelegate"
- "_protocolLayer"
- "_session"
- "addObserver:forKeyPath:options:context:"
- "alloc"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithObjects:count:"
- "assertion failure: '%s' (%s:line %i) Tagged unions can't be created directly. They need to be embedded in a class/struct."
- "assertion failure: '%s' (%s:line %i) Tagged unions don't support custom constructors."
- "assertion failure: '%s' (%s:line %i) Tagged unions don't support custom destructors."
- "assertion failure: '%s' (%s:line %i) Union tag type must be an enum type."
- "assertion failure: '%s' (%s:line %i) Union tag type must be registered before the union type."
- "assertion failure: (!\"Unreachable code\") Tagged unions can't be created directly. They need to be embedded in a class/struct."
- "assertion failure: (!isInitialized() || m_allocator == other.m_allocator) "
- "assertion failure: (!sharedTypeInfo().constructor) Tagged unions don't support custom constructors."
- "assertion failure: (!sharedTypeInfo().destructor) Tagged unions don't support custom destructors."
- "assertion failure: (tagType) Union tag type must be registered before the union type."
- "assertion failure: (tagType.value().isEnum()) Union tag type must be an enum type."
- "autorelease"
- "base64EncodedStringWithOptions:"
- "boolValue"
- "bytes"
- "class"
- "conformsToProtocol:"
- "connectedPeers"
- "countByEnumeratingWithState:objects:count:"
- "dataWithBytesNoCopy:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryForKey:"
- "displayName"
- "handles"
- "handlesLock"
- "hash"
- "i"
- "initWithLayer:"
- "initWithSession:protocolLayer:"
- "intValue"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "layer"
- "length"
- "listener"
- "listenerQueue"
- "listenerState"
- "lock"
- "makeAddressFromPeerID:"
- "myPeerID"
- "nextDelegate"
- "objectForKey:"
- "observeValueForKeyPath:ofObject:change:context:"
- "onResponsive: Invalid handle!"
- "onUnresponsive: Invalid handle!"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "protocolLayer"
- "rangeOfString:options:"
- "readySemaphore"
- "release"
- "removeObserver:forKeyPath:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendData:toPeers:withMode:error:"
- "session"
- "session:didFinishReceivingResourceWithName:fromPeer:atURL:withError:propagate:"
- "session:didReceiveCertificate:fromPeer:certificateHandler:propagate:"
- "session:didReceiveData:fromPeer:propagate:"
- "session:didReceiveStream:withName:fromPeer:propagate:"
- "session:didStartReceivingResourceWithName:fromPeer:withProgress:propagate:"
- "session:peer:didChangeState:propagate:"
- "setHandles:"
- "setHandlesLock:"
- "setListener:"
- "setNextDelegate:"
- "setPrivateDelegate:"
- "setProtocolLayer:"
- "setSession:"
- "standardUserDefaults"
- "stopListening"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringToIndex:"
- "superclass"
- "tagType"
- "tagType.value().isEnum()"
- "transportQueue"
- "unlock"
- "unsignedIntValue"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8^{MultipeerProtocolLayer=^^?{ArcRefCount=(isa_t=^v)}^{Allocator}^{ProtocolLayerListener}{ObjCObject=@}{ObjCObject=@}{Address={DynamicString=^{Allocator}(?={?=(?={?=b1b63}Q)*Q}{?=b1b7[23c]})}}}16"
- "v24@0:8^{ProtocolLayerListener=^^?}16"
- "v48@0:8@\"MCSession\"16@\"MCPeerID\"24q32^B40"
- "v48@0:8@\"MCSession\"16@\"NSData\"24@\"MCPeerID\"32^B40"
- "v48@0:8@16@24@32^B40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16@24q32^B40"
- "v56@0:8@\"MCSession\"16@\"NSArray\"24@\"MCPeerID\"32@?<v@?B>40^B48"
- "v56@0:8@\"MCSession\"16@\"NSInputStream\"24@\"NSString\"32@\"MCPeerID\"40^B48"
- "v56@0:8@\"MCSession\"16@\"NSString\"24@\"MCPeerID\"32@\"NSProgress\"40^B48"
- "v56@0:8@16@24@32@40^B48"
- "v56@0:8@16@24@32@?40^B48"
- "v56@0:8{DynamicArray<re::SharedPtr<(anonymous namespace)::MCProtocolHandle>>=^{Allocator}QQI^v}16"
- "v64@0:8@\"MCSession\"16@\"NSString\"24@\"MCPeerID\"32@\"NSURL\"40@\"NSError\"48^B56"
- "v64@0:8@16@24@32@40@48^B56"
- "waitForReady"
- "zone"
- "{Address={DynamicString=^{Allocator}(?={?=(?={?=b1b63}Q)*Q}{?=b1b7[23c]})}}24@0:8@16"
- "{DynamicArray<re::SharedPtr<(anonymous namespace)::MCProtocolHandle>>=\"m_allocator\"^{Allocator}\"m_capacity\"Q\"m_size\"Q\"m_version\"I\"m_data\"^v}"
- "{DynamicArray<re::SharedPtr<(anonymous namespace)::MCProtocolHandle>>=^{Allocator}QQI^v}16@0:8"

```
