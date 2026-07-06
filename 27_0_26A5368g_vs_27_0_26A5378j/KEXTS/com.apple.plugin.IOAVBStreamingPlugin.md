## com.apple.plugin.IOAVBStreamingPlugin

> `com.apple.plugin.IOAVBStreamingPlugin`

```diff

   __TEXT.__cstring: 0x1f20
   __TEXT.__os_log: 0x53ba
   __TEXT.__const: 0x10
-  __TEXT_EXEC.__text: 0x14bfc
+  __TEXT_EXEC.__text: 0x14bcc
   __TEXT_EXEC.__auth_stubs: 0x480
   __DATA.__data: 0xc8
   __DATA.__common: 0x240
Sections:
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ __ZN25IOAVBRealtimeReceiveQueue21processReceivedPacketEPN20IOEthernetController19IOEthernetAVBPacketE : 496 -> 484
~ __ZN25IOAVBRealtimeReceiveQueue21findStreamForStreamIDEy : 88 -> 76
~ __ZN25IOAVBRealtimeReceiveQueue9addStreamEythPhP16IOAVBInputStream : 440 -> 428
~ __ZN25IOAVBRealtimeReceiveQueue12removeStreamEy : 280 -> 268
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBContiguousPacketPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputUserSpaceStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputUserSpaceStreamUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInterfaceStreamManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInterfaceStreamManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputUserSpaceStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputUserSpaceStreamUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeReceiveQueue.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeReceiveQueueUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9HS6xG/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeTransmitQueue.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBContiguousPacketPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputUserSpaceStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputUserSpaceStreamUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInterfaceStreamManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInterfaceStreamManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputUserSpaceStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputUserSpaceStreamUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeReceiveQueue.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeReceiveQueueUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zAQ0Vt/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeTransmitQueue.cpp"

```
