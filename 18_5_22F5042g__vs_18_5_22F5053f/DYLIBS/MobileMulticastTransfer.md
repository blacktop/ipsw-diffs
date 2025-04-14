## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-63.120.18.0.0
-  __TEXT.__text: 0x290f0
+63.120.33.0.0
+  __TEXT.__text: 0x29dac
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0x13b0
+  __TEXT.__objc_methlist: 0x1420
   __TEXT.__const: 0x48f8
-  __TEXT.__cstring: 0xbef
-  __TEXT.__oslogstring: 0x2f91
-  __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__cstring: 0xd41
+  __TEXT.__oslogstring: 0x30f5
+  __TEXT.__gcc_except_tab: 0x618
+  __TEXT.__unwind_info: 0xbc8
   __TEXT.__objc_classname: 0x2fb
-  __TEXT.__objc_methname: 0x2fe9
-  __TEXT.__objc_methtype: 0x12cc
-  __TEXT.__objc_stubs: 0x23a0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x738
+  __TEXT.__objc_methname: 0x326b
+  __TEXT.__objc_methtype: 0x131b
+  __TEXT.__objc_stubs: 0x25a0
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x798
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb78
+  __DATA_CONST.__objc_selrefs: 0xbf8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x1ea0
-  __AUTH_CONST.__cfstring: 0x700
-  __AUTH_CONST.__objc_const: 0x45b8
+  __AUTH_CONST.__const: 0x1f40
+  __AUTH_CONST.__cfstring: 0x8c0
+  __AUTH_CONST.__objc_const: 0x4730
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x234
+  __DATA.__objc_ivar: 0x248
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x30
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1145
-  Symbols:   1712
-  CStrings:  1097
+  Functions: 1165
+  Symbols:   1746
+  CStrings:  1146
 
Symbols:
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_WiFiAwareMulticastConfiguration
+ _kMIBUClientControllerEventNanDataPathEnd
+ _kMIBUClientControllerEventNanDataPathInit
+ _kMIBUClientControllerEventNanDataPathStart
+ _kMIBUClientControllerEventNanMulticastEnd
+ _kMIBUClientControllerEventNanMulticastError
+ _kMIBUClientControllerEventNanMulticastInit
+ _kMIBUClientControllerEventNanMulticastStart
CStrings:
+ "\n("
+ "%"
+ "%{public}@: Failed to create WiFiAwareMulticastConfiguration"
+ "%{public}@: Failed to create WiFiAwareMulticastConfiguration, skipping enabling Rate Adapter..."
+ "%{public}@: Stopping using multicast..."
+ "%{public}@: device became ready: %{public}@"
+ "%{public}@: device disconnected: %{public}@"
+ "%{public}@: failed to deserialize summary: %@"
+ "%{public}@: multicast has been inactive for some time."
+ ">>>> Source block successfully decoded (%lu discarded)!"
+ "@\"<MIBUDataCollectorProtocol>\""
+ "@124@0:8@16@24@32@40@48@56@64@72@80Q88Q96Q104B112@116"
+ "@132@0:8@16@24@32@40@48@56@64@72@80Q88Q96Q104B112@116@124"
+ "@84@0:8@16@24@32@40Q48Q56Q64B72@76"
+ "B32@0:8^@16^Q24"
+ "B40@0:8Q16^@24^Q32"
+ "BytesConsumed"
+ "ClientControllerNanDataPathEnd"
+ "ClientControllerNanDataPathInit"
+ "ClientControllerNanDataPathStart"
+ "ClientControllerNanMulticastEnd"
+ "ClientControllerNanMulticastError"
+ "ClientControllerNanMulticastInit"
+ "ClientControllerNanMulticastStart"
+ "JSONObjectWithData:options:error:"
+ "LossRate"
+ "Multicast has been inactive for some time."
+ "PacketsConsumed"
+ "PacketsDiscarded"
+ "Summary"
+ "TQ,R,N,V_packetsDiscarded"
+ "Td,R,N"
+ "Td,R,N,V_lossRate"
+ "_dataCollector"
+ "_enableRA"
+ "_lossRate"
+ "_multicastSocketSem"
+ "_packetsDiscarded"
+ "_receivedVeryFirstPacketArray"
+ "_stopMulticast:"
+ "addKeyEvent:"
+ "checkOutWithError:withSummary:"
+ "clientControllerDidFailReceiving:error:"
+ "clientControllerDidFinishAssembly:withStats:"
+ "clientControllerDidFinishReceive:withStats:"
+ "clientDevice:didCheckOutWithError:withSummary:"
+ "d"
+ "d16@0:8"
+ "decodeAllSourceBlocks:discarded:"
+ "decodeBlock:error:discarded:"
+ "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:"
+ "initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:"
+ "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:"
+ "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:"
+ "lossRate"
+ "nanSubscriberDetectedMulticastError:"
+ "numberWithDouble:"
+ "packetsDiscarded"
+ "rangeOfString:"
+ "serverController:didReceiveClientDeviceCheckOut:withError:andSummary:"
+ "serverDeviceDidDisconnect:"
+ "setDynamicLinkRate:"
+ "setMulticastConfiguration:"
+ "stopMulticast"
+ "substringToIndex:"
+ "summaryReport"
+ "v20@0:8B16"
+ "v24@0:8@\"MIBUNANSubscriber\"16"
+ "v40@0:8@\"MIBUNWClientDevice\"16@\"NSError\"24@\"NSDictionary\"32"
- "\t'"
- ">>>> Source block successfully decoded!"
- "@120@0:8@16@24@32@40@48@56@64@72@80Q88Q96Q104@112"
- "@80@0:8@16@24@32@40Q48Q56Q64@72"
- "Acknowledging NAN client check in: %{public}@"
- "B24@0:8^@16"
- "B32@0:8Q16^@24"
- "checkInAck"
- "clientControllerDidFinishAssembly:"
- "clientControllerDidFinishReceive:"
- "clientDevice:didCheckOutWithError:"
- "decodeAllSourceBlocks:"
- "decodeBlock:error:"
- "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:controllerDelegate:"
- "initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:controllerDelegate:"
- "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:publisherDelegate:"
- "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:subscriberDelegate:"
- "serverController:didReceiveClientDeviceCheckOut:withError:"
- "v32@0:8@\"MIBUNWClientDevice\"16@\"NSError\"24"
- "v48@0:8@\"NSObject<OS_dispatch_data>\"16@\"NSDate\"24@?<v@?BB>32@\"NSObject<OS_dispatch_queue>\"40"

```
