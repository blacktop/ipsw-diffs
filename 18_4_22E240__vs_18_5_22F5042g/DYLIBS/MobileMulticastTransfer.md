## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-63.100.22.0.0
-  __TEXT.__text: 0x27110
+63.120.18.0.0
+  __TEXT.__text: 0x290f0
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0x1280
+  __TEXT.__objc_methlist: 0x13b0
   __TEXT.__const: 0x48f8
-  __TEXT.__cstring: 0xb67
-  __TEXT.__oslogstring: 0x2d28
+  __TEXT.__cstring: 0xbef
+  __TEXT.__oslogstring: 0x2f91
   __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__unwind_info: 0xad0
-  __TEXT.__objc_classname: 0x2d1
-  __TEXT.__objc_methname: 0x2cef
-  __TEXT.__objc_methtype: 0x118e
-  __TEXT.__objc_stubs: 0x2200
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x6f0
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__objc_classname: 0x2fb
+  __TEXT.__objc_methname: 0x2fe9
+  __TEXT.__objc_methtype: 0x12cc
+  __TEXT.__objc_stubs: 0x23a0
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x738
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb08
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_selrefs: 0xb78
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x1d40
-  __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0x3fd8
+  __AUTH_CONST.__const: 0x1ea0
+  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__objc_const: 0x45b8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x214
-  __DATA.__data: 0x540
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x234
+  __DATA.__data: 0x5a0
   __DATA.__bss: 0x30
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1075
-  Symbols:   1623
-  CStrings:  1059
+  Functions: 1145
+  Symbols:   1712
+  CStrings:  1097
 
Symbols:
+ _OBJC_CLASS_$_MIBUNANPublisher
+ _OBJC_CLASS_$_WiFiChannel
+ _OBJC_METACLASS_$_MIBUNANPublisher
+ _ipv6AddressForInterface
CStrings:
+ "\t'"
+ "\nA\x19"
+ "%%%@"
+ "%{public}@: Data session handle already created."
+ "%{public}@: Data session handle not found for peer: %{public}@"
+ "%{public}@: Data session handle not found."
+ "%{public}@: Failed to create NAN publisher."
+ "%{public}@: Failed to send data to subscriber via NAN: %ld"
+ "%{public}@: Failed to terminate data session: %ld"
+ "%{public}@: Invalid publisher delegate specified."
+ "%{public}@: NAN publisher already started."
+ "%{public}@: NAN publisher already stopped."
+ "%{public}@: NAN publisher confirmed data session for peer: %{public}@ with handle: %{public}@"
+ "%{public}@: NAN publisher detected multicast error: %ld"
+ "%{public}@: NAN publisher failed to start with error: %ld"
+ "%{public}@: NAN publisher received message: %{publc}@ from peer: %{public}@"
+ "%{public}@: NAN publisher received multicast data blob: %{public}@ from peer: %{public}@"
+ "%{public}@: NAN publisher started!"
+ "%{public}@: NAN publisher terminated data session for peer: %{public}@ with handle: %{public}@"
+ "%{public}@: NAN publisher terminated with reason: %ld"
+ "%{public}@: Restarting NAN publisher in %lld secs"
+ "%{public}@: Starting NAN publisher!"
+ "%{public}@: Stopping NAN publisher for reason: %{public}@"
+ "@\"<MIBUNANPublisherDelegate>\""
+ "@\"MIBUNANPublisher\""
+ "@\"WiFiAwarePublishConfiguration\""
+ "@120@0:8@16@24@32@40@48@56@64@72@80Q88Q96Q104@112"
+ "@80@0:8@16@24@32@40Q48Q56Q64@72"
+ "EOF Reached"
+ "Failed to terminate NAN data session for device: %{public}@ error: %{public}@"
+ "Invalidating NAN unicast connection for device: %{public}@ IPv6 address: %{public}@"
+ "MIBUNANPublisher"
+ "MIBUNANPublisherDelegate"
+ "NAN data session failed to stop: %@"
+ "NAN data session not found"
+ "NAN publisher failed to start: %ld"
+ "NAN publisher terminated: %ld"
+ "Packet Fetch Failed"
+ "Stopping NAN client lisenter and multicast socket."
+ "Stopping file sending loop"
+ "_band"
+ "_bandwidth"
+ "_channelName"
+ "_countryCode"
+ "_dataSessionMapping"
+ "_multicastData:withCompletion:"
+ "_nanPublisher"
+ "_publisherDelegate"
+ "_publisherState"
+ "_startPublisher"
+ "_stopMulticast"
+ "_stopPublisherForReason:"
+ "_terminateDataSessionWithPeer:withCompletion:"
+ "initWithChannelNumber:bandwidth:is2_4GHz:is5GHz:is6GHz:isDFS:extensionChannelAbove:"
+ "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:controllerDelegate:"
+ "initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:controllerDelegate:"
+ "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:publisherDelegate:"
+ "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:subscriberDelegate:"
+ "multicastData:withCompletion:"
+ "nanPublisher:didCreateDataSessionWithPeer:usingInterface:"
+ "nanPublisher:didDestoryDataSessionWithPeer:"
+ "nanPublisher:didReceiveData:fromPeer:"
+ "nanPublisherDidStart:forRetry:"
+ "nanPublisherDidStop:withError:willRetry:"
+ "removeAllObjects"
+ "removeObjectForKey:"
+ "setChannelInfo:"
+ "setCountryCode:"
+ "stringByAppendingFormat:"
+ "terminateDataSessionWithPeer:withCompletion:"
+ "v28@0:8@\"MIBUNANPublisher\"16B24"
+ "v32@0:8@\"MIBUNANPublisher\"16@\"NSString\"24"
+ "v36@0:8@\"MIBUNANPublisher\"16@\"NSError\"24B32"
+ "v40@0:8@\"MIBUNANPublisher\"16@\"NSData\"24@\"NSString\"32"
+ "v40@0:8@\"MIBUNANPublisher\"16@\"NSString\"24@\"NSString\"32"
- "\t("
- "\tC\x1a"
- "%@%%%@"
- "%@%@"
- "%nan0"
- "%{public}@ NDP terminated with error: %ld"
- "%{public}@ NDP termination timed out"
- "%{public}@ iPV6 address is %{public}@; handle = %@"
- "@32@0:8{in6_addr=(?=[16C][8S][4I])}16"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "Data confirmed for peer %{public}@ with data session handle: %{public}@"
- "Failed to convert %{public}@ to in6_addr"
- "Failed to fetch current interfaces"
- "Failed to find NDP data handle for %{public}@"
- "Fetching address for interface: %{public}@"
- "Invalidating NAN unicast connection for %{public}@"
- "NAN IPv6 Address: %{public}@; host address: %{public}@"
- "NAN publisher detected multicast error: %ld"
- "NAN publisher received multicast data blob: %@"
- "NAN publishing failed to start with error: %ld"
- "NAN publishing failed to start with reason: %ld"
- "NAN publishing started"
- "Received message %{publc}@ from subscriber: %{public}@"
- "Tear down"
- "Terminating NDP for %{public}@"
- "_convertToString:"
- "_datsSessionMapping"
- "_iPAddressForInterface:"
- "_multicastAddress"
- "_nanHostAddr"
- "_publisher"
- "cStringUsingEncoding:"
- "containsString:"
- "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:controllerDelegate:"
- "initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:controllerDelegate:"
- "initWithServiceName:groupAddress:groupPort:subscriberDelegate:"
- "setServiceSpecificInfo:"

```
