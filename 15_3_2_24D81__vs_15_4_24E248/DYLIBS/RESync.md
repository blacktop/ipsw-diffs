## RESync

> `/System/Library/PrivateFrameworks/RESync.framework/Versions/A/RESync`

```diff

-366.80.1.0.0
-  __TEXT.__text: 0x6bfac
+366.100.14.0.0
+  __TEXT.__text: 0x6b5dc
   __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x16c
-  __TEXT.__const: 0x1f8f
+  __TEXT.__objc_methlist: 0x2d4
+  __TEXT.__const: 0x1f9f
   __TEXT.__cstring: 0x540b
   __TEXT.__oslogstring: 0x454f
-  __TEXT.__unwind_info: 0x58
   __TEXT.__objc_classname: 0x6a
   __TEXT.__objc_methname: 0x8d8
   __TEXT.__objc_methtype: 0x883

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f0
+  __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x3068
   __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x878
+  __AUTH_CONST.__objc_const: 0x5e8
   __AUTH.__objc_data: 0x140
   __AUTH.__thread_vars: 0x30
-  __AUTH.__thread_bss: 0xc1
+  __AUTH.__thread_bss: 0xc8
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x108
-  __DATA.__common: 0x960
-  __DATA.__bss: 0xd8
+  __DATA.__common: 0x970
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++abi.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0EA8769-C0DD-39D5-B6C1-EBE2F1F0667A
-  Functions: 1980
-  Symbols:   3136
+  UUID: 20AD1FEC-5324-3929-A194-B22B7543ECEA
+  Functions: 1960
+  Symbols:   3129
   CStrings:  1013
 
Symbols:
+ _MergedGlobals.73
+ __ZGVZL14ArcObjectClassvE3cls
+ __ZNSt3__110unique_ptrIN2re20SharedAppSyncManager9PeerStateENS1_11SyncDeleterIS3_EEED2B8nn190102Ev
+ __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS7_EEENS3_ISB_EEE5resetB8nn190102EPSB_
+ __ZNSt3__114__thread_proxyB8nn190102INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS8_EEEEEPvSD_
+ __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEbT1_S9_T0_
+ __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEjT1_S9_S9_T0_
+ __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEvT1_S9_S9_S9_T0_
+ __ZNSt3__17__sort5B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEvT1_S9_S9_S9_S9_T0_
+ __ZSt28__throw_bad_array_new_lengthB8nn190102v
+ __ZZL14ArcObjectClassvE3cls
+ __ZZL14ArcObjectClassvENK3$_0clEv
- _MergedGlobals.71
- __ZN12_GLOBAL__N_116MCProtocolHandle11onHandshakeEP9MCSessionN2re5SliceIhEE
- __ZN2re17PacketStatsFilter28updateChannelBandwidthUsagesERKNS_6PacketE
- __ZN2re18NetworkSyncManager22removeDeferredSessionsEv
- __ZN2re9Transport26readPacketHeaderFromBufferEPKhjRNS0_12PacketHeaderE
- __ZN2re9Transport9hostStatsEv
- __ZNK2re16SharedAppUnicast13shouldForwardERKNS_9SharedPtrINS_10SyncObjectEEE
- __ZNK2re17SyncCommitBuilder13shouldForwardERKNS_9SharedPtrINS_10SyncObjectEEE
- __ZNSt3__110unique_ptrIN2re20SharedAppSyncManager9PeerStateENS1_11SyncDeleterIS3_EEED2B8nn180100Ev
- __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS7_EEENS3_ISB_EEE5resetB8nn180100EPSB_
- __ZNSt3__114__thread_proxyB8nn180100INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEMN2re33TransportCommandsThreadedProtocolEFvvEPS8_EEEEEPvSD_
- __ZNSt3__121__unwrap_and_dispatchB8nn180100INS_10__overloadINS_11__copy_loopINS_17_ClassicAlgPolicyEEENS_14__copy_trivialEEEPN2re20SyncOwnershipRequestES9_S9_Li0EEENS_4pairIT0_T2_EESB_T1_SC_
- __ZNSt3__121__unwrap_and_dispatchB8nn180100INS_10__overloadINS_11__copy_loopINS_17_ClassicAlgPolicyEEENS_14__copy_trivialEEEPN2re8internal17SyncSnapshotEntryESA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
- __ZNSt3__127__insertion_sort_incompleteB8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEbT1_S9_T0_
- __ZNSt3__17__sort3B8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEjT1_S9_S9_T0_
- __ZNSt3__17__sort4B8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEvT1_S9_S9_S9_T0_
- __ZNSt3__17__sort5B8nn180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPPN2re10SyncViewerEEEvT1_S9_S9_S9_S9_T0_
- __ZSt28__throw_bad_array_new_lengthB8nn180100v

```
