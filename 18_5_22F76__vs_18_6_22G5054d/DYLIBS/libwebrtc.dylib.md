## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-621.2.5.10.10
-  __TEXT.__text: 0xa6b2c8
+621.3.6.10.1
+  __TEXT.__text: 0xa6b520
   __TEXT.__auth_stubs: 0x1560
   __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0xb3a98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 703F2AFD-9677-36D6-9D2D-3349AE8AEAE1
-  Functions: 18023
-  Symbols:   43549
+  UUID: 0DAA7DC8-49C4-31A9-8B60-09F34B07F592
+  Functions: 18026
+  Symbols:   43555
   CStrings:  9558
 
Symbols:
+ __ZN6dcsctp15OutstandingData23ExpireOutstandingChunksEN6webrtc9TimestampE
+ __ZNSt3__15dequeIN6dcsctp15OutstandingData4ItemENS_9allocatorIS3_EEE12emplace_backIJN6webrtc11StrongAliasINS1_20OutgoingMessageIdTagEjEENS1_4DataENS8_9TimestampENS1_14MaxRetransmitsESD_NS1_11LifecycleIdEEEERS3_DpOT_
+ __ZNSt3__15dequeIN6dcsctp15OutstandingData4ItemENS_9allocatorIS3_EEED2B8sn190102Ev
Functions:
~ __ZN6dcsctp15OutstandingData13AbandonAllForERKNS0_4ItemE : 1032 -> 832
+ __ZNSt3__15dequeIN6dcsctp15OutstandingData4ItemENS_9allocatorIS3_EEE12emplace_backIJN6webrtc11StrongAliasINS1_20OutgoingMessageIdTagEjEENS1_4DataENS8_9TimestampENS1_14MaxRetransmitsESD_NS1_11LifecycleIdEEEERS3_DpOT_
+ __ZN6dcsctp15OutstandingData23ExpireOutstandingChunksEN6webrtc9TimestampE
+ __ZNSt3__16__treeIN6dcsctp23UnwrappedSequenceNumberIN6webrtc11StrongAliasINS1_6TSNTagEjEEEENS_4lessIS7_EENS_9allocatorIS7_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEENS_21__tree_const_iteratorIS7_PNS_11__tree_nodeIS7_SF_EElEERPNS_15__tree_end_nodeISH_EESI_RKT_
~ __ZN6dcsctp24TransmissionControlBlock19SendBufferedPacketsERNS_10SctpPacket7BuilderEN6webrtc9TimestampE : 1608 -> 1416
~ __ZN6dcsctp24TransmissionControlBlockD2Ev : 1420 -> 1024
~ _vp8e_init : 528 -> 540

```
