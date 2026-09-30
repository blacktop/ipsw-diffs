## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-622.1.19.10.4
-  __TEXT.__text: 0xabcf4c
+622.1.21.10.3
+  __TEXT.__text: 0xabd2e4
   __TEXT.__auth_stubs: 0x1560
   __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0xb3d98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B5DA70D-48AF-3C4D-AC26-850298782006
-  Functions: 18385
-  Symbols:   45094
+  UUID: 78C6B909-2538-3CE1-B3D6-38E7D0287795
+  Functions: 18387
+  Symbols:   45098
   CStrings:  9790
 
Symbols:
+ __ZN6dcsctp15OutstandingData23ExpireOutstandingChunksEN6webrtc9TimestampE
+ __ZNSt3__15dequeIN6dcsctp15OutstandingData4ItemENS_9allocatorIS3_EEE12emplace_backIJN6webrtc11StrongAliasINS1_20OutgoingMessageIdTagEjEENS1_4DataENS8_9TimestampENS1_14MaxRetransmitsESD_NS1_11LifecycleIdEEEERS3_DpOT_
Functions:
~ __ZN6dcsctp15OutstandingData13AbandonAllForERKNS0_4ItemE : 1032 -> 832
+ __ZNSt3__15dequeIN6dcsctp15OutstandingData4ItemENS_9allocatorIS3_EEE12emplace_backIJN6webrtc11StrongAliasINS1_20OutgoingMessageIdTagEjEENS1_4DataENS8_9TimestampENS1_14MaxRetransmitsESD_NS1_11LifecycleIdEEEERS3_DpOT_
+ __ZN6dcsctp15OutstandingData23ExpireOutstandingChunksEN6webrtc9TimestampE
~ __ZN6dcsctp24TransmissionControlBlock19SendBufferedPacketsERNS_10SctpPacket7BuilderEN6webrtc9TimestampE : 1640 -> 1448
~ _encode_frame_internal : 4824 -> 4828
~ _vp9_create_compressor : 9144 -> 9148

```
