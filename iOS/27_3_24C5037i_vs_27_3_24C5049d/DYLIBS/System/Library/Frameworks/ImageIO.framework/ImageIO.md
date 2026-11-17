## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-2851.2.2.0.0
-  __TEXT.__text: 0x4fc64c
+2851.2.5.0.0
+  __TEXT.__text: 0x4fd4c0
   __TEXT.__objc_methlist: 0xd68
   __TEXT.__const: 0x4a070
-  __TEXT.__gcc_except_tab: 0x22bf8
+  __TEXT.__gcc_except_tab: 0x22c60
   __TEXT.__cstring: 0xa7b1d
   __TEXT.__oslogstring: 0x17
   __TEXT.__constg_swiftt: 0x26a4

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x18380
+  __TEXT.__unwind_info: 0x183c8
   __TEXT.__eh_frame: 0x9324
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
-  Functions: 23245
-  Symbols:   24506
+  Functions: 23266
+  Symbols:   24528
   CStrings:  18354
 
Symbols:
+ __ZL21sourceAuxGainMapTypesP14IIOImageSourcemPbS1_
+ __ZN12OFDContainer20adoptNestedContainerEPS_
+ __ZN12OFDContainerC1EPK8__CFData
+ __ZN12OFDContainerC2EPK8__CFData
+ __ZN13GlobalPNGInfo10fcTLResizeEm
+ __ZN13GlobalPNGInfo15fcTLBeginUpdateEm
+ __ZN13GlobalPNGInfo7getPrivEM13GlobalPNGDataj
+ __ZN13GlobalPNGInfo7setPrivEM13GlobalPNGDatajj
+ __ZN13GlobalPNGInfo9fcTLSetAtEmRK10fcTL_CHUNK
+ __ZN17IIO_ReaderHandler22preferredTypeForUTTypeEPK10__CFStringj
+ __ZN6_APP13C2EPhm
+ __ZN9_JPEGFile19preserveAIMarkerBoxEv
+ __ZNK13GlobalPNGInfo12fcTLSnapshotEv
+ __ZNK13GlobalPNGInfo6fcTLAtEmR10fcTL_CHUNK
+ __ZNK13GlobalPNGInfo9fcTLCountEv
+ __ZNSt3__16__treeINS_12__value_typeItZN9_JPEGFile19preserveAIMarkerBoxEvE3BoxEENS_19__map_value_compareItNS_4pairIKtS3_EENS_4lessItEEEENS_9allocatorIS8_EEE14__tree_deleterclB9fqe220106EPNS_11__tree_nodeIS4_PvEE
+ __ZNSt3__16vectorI10fcTL_CHUNKNS_9allocatorIS1_EEE11__vallocateB9fqe220106Em
+ __ZNSt3__16vectorI10fcTL_CHUNKNS_9allocatorIS1_EEE16__init_with_sizeB9fqe220106IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI10fcTL_CHUNKNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorIP12OFDContainerNS_9allocatorIS2_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorIP12OFDContainerNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIZN9_JPEGFile19preserveAIMarkerBoxEvE7SegmentNS_9allocatorIS2_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__19allocatorIP12OFDContainerE17allocate_at_leastB9fqe220106Em
+ __ZZNSt3__16vectorIZN9_JPEGFile19preserveAIMarkerBoxEvE7SegmentNS_9allocatorIS2_EEE12emplace_backIJS2_EEERS2_DpOT_ENKUlvE0_clEv
- __ZN12OFDContainerC1EPhj
- __ZN12OFDContainerC2EPhj
CStrings:
+ "*** Can't access image data [%llu/%llu] (%dx%d)\n"
- "*** Can't access image data [%ld/%ld] (%dx%d)\n"
```
