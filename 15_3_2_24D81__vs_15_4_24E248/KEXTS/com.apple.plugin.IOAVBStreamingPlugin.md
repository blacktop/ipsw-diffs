## com.apple.plugin.IOAVBStreamingPlugin

> `com.apple.plugin.IOAVBStreamingPlugin`

```diff

   __TEXT.__cstring: 0x1dac
   __TEXT.__os_log: 0x53ba
   __TEXT.__const: 0x10
-  __TEXT_EXEC.__text: 0x152d8
+  __TEXT_EXEC.__text: 0x15ed4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x240

   __DATA_CONST.__const: 0x7820
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: D85452EF-BB12-3B3C-81F3-81B785DFB7B5
-  Functions: 416
-  Symbols:   1312
+  UUID: 0B4BB30B-44BF-3908-8CCE-BFA9ABE21783
+  Functions: 470
+  Symbols:   1368
   CStrings:  358
 
Symbols:
+ _ZN16IOAVBInputStream17setDestinationMACEPKh.cold.1
+ _ZN16IOAVBInputStream17setDestinationMACEPKh.cold.2
+ _ZN16IOAVBInputStream4initEyPKhmmmi.cold.1
+ _ZN16IOAVBInputStream5startEP9IOService.cold.1
+ _ZN17IOAVBOutputStream12outputPacketEm.cold.1
+ _ZN17IOAVBOutputStream12outputPacketEm.cold.2
+ _ZN17IOAVBOutputStream19clientMemoryForTypeEjPjPP18IOMemoryDescriptor.cold.1
+ _ZN17IOAVBOutputStream5startEP9IOService.cold.1
+ _ZN17IOAVBOutputStream5startEP9IOService.cold.2
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.1
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.10
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.2
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.3
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.4
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.5
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.6
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.7
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.8
+ _ZN25IOAVBContiguousPacketPool12updatePacketEtybmmmm.cold.9
+ _ZN25IOAVBContiguousPacketPool13packetAtIndexEt.cold.1
+ _ZN25IOAVBContiguousPacketPool14completePacketEPN20IOEthernetController19IOEthernetAVBPacketE.cold.2
+ _ZN25IOAVBContiguousPacketPool4initEthPmP8IOMapperyj.cold.1
+ _ZN25IOAVBContiguousPacketPool4initEthPmP8IOMapperyj.cold.2
+ _ZN25IOAVBContiguousPacketPool4initEthPmP8IOMapperyj.cold.3
+ _ZN25IOAVBContiguousPacketPool4initEthPmP8IOMapperyj.cold.4
+ _ZN25IOAVBContiguousPacketPool4initEthPmP8IOMapperyj.cold.5
+ _ZN25IOAVBContiguousPacketPool4initEthPmP8IOMapperyj.cold.6
+ _ZN25IOAVBContiguousPacketPool4initEthPmP8IOMapperyj.cold.7
+ _ZN25IOAVBContiguousPacketPool4initEthPmP8IOMapperyj.cold.8
+ _ZN25IOAVBContiguousPacketPool4initEthPmP8IOMapperyj.cold.9
+ _ZN25IOAVBRealtimeReceiveQueue20changeDestinationMACEPKhS1_.cold.1
+ _ZN25IOAVBRealtimeReceiveQueue5startEP9IOService.cold.1
+ _ZN26IOAVBOutputUserSpaceStream21updatePacketsFromInfoEmm.cold.1
+ _ZN26IOAVBOutputUserSpaceStream21updatePacketsFromInfoEmm.cold.2
+ _ZN26IOAVBOutputUserSpaceStream21updatePacketsFromInfoEmm.cold.3
+ _ZN26IOAVBOutputUserSpaceStream21updatePacketsFromInfoEmm.cold.4
+ _ZN26IOAVBOutputUserSpaceStream21updatePacketsFromInfoEmm.cold.5
+ _ZN26IOAVBRealtimeTransmitQueue4initEjP12OSDictionary.cold.1
+ _ZN26IOAVBRealtimeTransmitQueue5startEP9IOService.cold.1
+ _ZN27IOAVBInterfaceStreamManager17allocateBandwidthEyy.cold.1
+ _ZN27IOAVBInterfaceStreamManager17allocateBandwidthEyy.cold.2
+ _ZN27IOAVBInterfaceStreamManager5startEP9IOService.cold.1
+ _ZN35IOAVBInputUserSpaceStreamUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv.cold.1
+ _ZN35IOAVBRealtimeReceiveQueueUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN35IOAVBRealtimeReceiveQueueUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.2
+ _ZN35IOAVBRealtimeReceiveQueueUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.3
+ _ZN35IOAVBRealtimeReceiveQueueUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.4
+ _ZN35IOAVBRealtimeReceiveQueueUserClient16setAsyncCallbackEPy.cold.1
+ _ZN35IOAVBRealtimeReceiveQueueUserClient20releaseAsyncCallbackEv.cold.1
+ _ZN35IOAVBRealtimeReceiveQueueUserClient20streamReceivedPacketEPN20IOEthernetController19IOEthernetAVBPacketE.cold.1
+ _ZN35IOAVBRealtimeReceiveQueueUserClient20streamReceivedPacketEPN20IOEthernetController19IOEthernetAVBPacketE.cold.2
+ _ZN35IOAVBRealtimeReceiveQueueUserClient20streamReceivedPacketEPN20IOEthernetController19IOEthernetAVBPacketE.cold.3
+ _ZN35IOAVBRealtimeReceiveQueueUserClient5startEP9IOService.cold.1
+ _ZN35IOAVBRealtimeReceiveQueueUserClient5startEP9IOService.cold.2
+ _ZN35IOAVBRealtimeReceiveQueueUserClient5startEP9IOService.cold.3
+ _ZNK25IOAVBContiguousPacketPool26memoryDescriptorForSegmentEh.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBContiguousPacketPool.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputStream.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputUserSpaceStream.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputUserSpaceStreamUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInterfaceStreamManager.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInterfaceStreamManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputStream.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputUserSpaceStream.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputUserSpaceStreamUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeReceiveQueue.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeReceiveQueueUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeTransmitQueue.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBContiguousPacketPool.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputStream.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputUserSpaceStream.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInputUserSpaceStreamUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInterfaceStreamManager.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBInterfaceStreamManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputStream.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputUserSpaceStream.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBOutputUserSpaceStreamUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeReceiveQueue.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeReceiveQueueUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBStreamingPlugin/IOAVBRealtimeTransmitQueue.cpp"

```
