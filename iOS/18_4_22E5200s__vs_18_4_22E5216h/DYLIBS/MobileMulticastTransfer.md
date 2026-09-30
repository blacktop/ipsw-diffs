## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-63.100.13.502.1
-  __TEXT.__text: 0x23938
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x10b0
-  __TEXT.__const: 0x48f0
-  __TEXT.__cstring: 0xa01
-  __TEXT.__oslogstring: 0x26a2
-  __TEXT.__gcc_except_tab: 0x634
-  __TEXT.__unwind_info: 0x990
-  __TEXT.__objc_classname: 0x28f
-  __TEXT.__objc_methname: 0x280f
-  __TEXT.__objc_methtype: 0xfa6
-  __TEXT.__objc_stubs: 0x1d80
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x678
-  __DATA_CONST.__objc_classlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x68
+63.100.22.0.0
+  __TEXT.__text: 0x27110
+  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__objc_methlist: 0x1280
+  __TEXT.__const: 0x48f8
+  __TEXT.__cstring: 0xb67
+  __TEXT.__oslogstring: 0x2d28
+  __TEXT.__gcc_except_tab: 0x620
+  __TEXT.__unwind_info: 0xad0
+  __TEXT.__objc_classname: 0x2d1
+  __TEXT.__objc_methname: 0x2cef
+  __TEXT.__objc_methtype: 0x118e
+  __TEXT.__objc_stubs: 0x2200
+  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__const: 0x6f0
+  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f0
-  __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x610
+  __DATA_CONST.__objc_selrefs: 0xb08
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x88
+  __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x1aa0
-  __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x3948
-  __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x1e8
-  __DATA.__data: 0x4e0
+  __AUTH_CONST.__const: 0x1d40
+  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__objc_const: 0x3fd8
+  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x214
+  __DATA.__data: 0x540
   __DATA.__bss: 0x30
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 967
-  Symbols:   1477
-  CStrings:  952
+  Functions: 1075
+  Symbols:   1623
+  CStrings:  1059
 
Symbols:
+ OBJC_IVAR_$_MIBUNWDevice._connectOnDemand
+ OBJC_IVAR_$_MIBUNWDevice._message
+ _MobileInBoxUpdaterErrorDomain
+ _NSLocalizedDescriptionKey
+ _NSStringFromEtherAddr
+ _NSStringFromIfIndex
+ _NSStringFromIn6Addr
+ _NSStringToIPv6Addr
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_MIBUNANSubscriber
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_METACLASS_$_MIBUNANSubscriber
+ __createError
+ __dispatch_main_q
+ _exp2
+ _if_indextoname
+ _nanorq_get_max_esi
+ _os_unfair_lock_assert_owner
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _safeAssignError
+ _safeCreateError
CStrings:
+ "\x02\x11"
+ "\x03\x11"
+ "\t("
+ "$"
+ "%@: Received the very first array of packets!"
+ "%{public}@: Creating NAN data session!"
+ "%{public}@: Device checked in: %{public}@"
+ "%{public}@: Establishing NAN TCP connection with sender %{public}@"
+ "%{public}@: Failed to create NAN configuration from service name: %{public}@"
+ "%{public}@: Failed to create WiFiMACAddress from IPv6 group address: %{public}@"
+ "%{public}@: Failed to create server device over NAN."
+ "%{public}@: Failed to create server device over infra."
+ "%{public}@: Failed to send data to publisher via NAN: %ld"
+ "%{public}@: Handling NAN failure due to error: %{public}@ retry count: %lu"
+ "%{public}@: Ignore NAN data session termination."
+ "%{public}@: Invalid subscriber delegate specified."
+ "%{public}@: Invalidating NAN TCP connection."
+ "%{public}@: Multicast socket started."
+ "%{public}@: Multicast socket stopped with error: %{public}@"
+ "%{public}@: NAN data session already running."
+ "%{public}@: NAN data session confirmed for peer: %{public}@ using interface: %{public}@"
+ "%{public}@: NAN data session failed to start with error: %ld"
+ "%{public}@: NAN data session request started."
+ "%{public}@: NAN data session terminated with reason: %ld"
+ "%{public}@: NAN multicast session is not ready."
+ "%{public}@: NAN subscriber already started."
+ "%{public}@: NAN subscriber already stopped."
+ "%{public}@: NAN subscriber detected multicast error: %ld"
+ "%{public}@: NAN subscriber discovered result: %{public}@ (MAC: %{public}@)"
+ "%{public}@: NAN subscriber failed to start with error: %ld"
+ "%{public}@: NAN subscriber lost discovered result: %{public}@"
+ "%{public}@: NAN subscriber received multicast data blob: %@"
+ "%{public}@: NAN subscriber started!"
+ "%{public}@: NAN subscriber terminated with reason: %ld"
+ "%{public}@: Restarting NAN subscriber in %lld secs"
+ "%{public}@: Starting NAN subscriber with service name: %{public}@"
+ "%{public}@: Starting multicast receiver with config: %{public}@"
+ "%{public}@: Stopping NAN subscriber for reason: %{public}@"
+ "%{public}@: Stopping multicast receiver..."
+ "%{public}@: connection with host %{public}@:%{public}@ created, will bootstrap connection"
+ "%{public}@: not able to create connection with host %{public}@:%{public}@"
+ "%{public}@: ping through multicast failed with error %{public}@"
+ "%{public}@: ping through multicast: %@"
+ "%{public}@: state :%lu; progress = %@"
+ "%{public}@: state: %lu; packets: %lu/%lu (%lu missing), progress = %@"
+ "1"
+ "<%@: State=%@>"
+ "@\"<MIBUNANSubscriberDelegate>\""
+ "@\"MIBUNANSubscriber\""
+ "@\"MIBUNWMessage\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"WiFiAwareSubscribeConfiguration\""
+ "@52@0:8@16@24@32B40@44"
+ "B32@0:8@16@24"
+ "Error Occurred"
+ "ErrorCode"
+ "ErrorDomain"
+ "ErrorMessage"
+ "Failed to add symbol for symbol %lu for sbn %lu: %d. tag = 0x%x, lastTag = 0x%x, rq->max_esi = %u, esiCount = %lu"
+ "MIBUExtension"
+ "MIBUNANSubscriber"
+ "MIBUNANSubscriberDelegate"
+ "NAN data session control connection available for peer: %{public}@"
+ "NAN data session failed to start: %ld"
+ "NAN data session terminated: %ld"
+ "NAN multicast session data send failed: %@"
+ "NAN multicast session not ready"
+ "NAN publisher detected multicast error: %ld"
+ "NAN publisher received multicast data blob which decodes to: %@"
+ "NAN publisher received multicast data blob: %@"
+ "NAN subscriber failed to start: %ld"
+ "NAN subscriber terminated: %ld"
+ "READY"
+ "RUNNING"
+ "STARTING"
+ "STOPPED"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_syncSemaphore"
+ "T@\"NSString\",R,C,N"
+ "TCP device %{public}@ checked out with error: %@"
+ "TQ,N,V_retryLimit"
+ "UNKNOWN"
+ "_checkOutWithError:"
+ "_connectOnDemand"
+ "_consumePacket:arrivalTime:"
+ "_createDataSessionWithDiscoveryResult:"
+ "_createNANTCPConnectionUsingInterface:"
+ "_dataSession"
+ "_handleFailureDueToError:"
+ "_handleInboundPackets:arrivalTime:"
+ "_invalidateNANTCPConnection"
+ "_lastActivity"
+ "_message"
+ "_nanConfiguration"
+ "_nanSubscriber"
+ "_retryCount"
+ "_retryLimit"
+ "_sendData:withCompletion:"
+ "_sendMessage:"
+ "_startMulticastReceiverUsingInterface:"
+ "_startSubscriber"
+ "_stopSubscriberForReason:"
+ "_subscriberDelegate"
+ "_subscriberState"
+ "_syncSemaphore"
+ "_unfairLock"
+ "checkOutWithError:"
+ "clientControllerDidFinishAssembly:"
+ "clientControllerDidStartAssembly:"
+ "clientDevice:didCheckOutWithError:"
+ "code"
+ "com.apple.MobileInBoxUpdater.ErrorDomain"
+ "connect"
+ "consumePackets:arrivalTime:withCompletion:inQueue:"
+ "dictionaryWithDictionary:"
+ "dictionaryWithObject:forKey:"
+ "disconnect"
+ "domain"
+ "errorWithDomain:code:userInfo:"
+ "etherAddressString"
+ "initWithFormat:arguments:"
+ "initWithHostAddress:hostPort:interfaceName:connectOnDemand:statusDelegate:"
+ "initWithMulticastIPv6AddressString:"
+ "initWithServiceName:groupAddress:groupPort:subscriberDelegate:"
+ "integerValue"
+ "ipv6AddressString"
+ "isActive"
+ "localInterfaceIndex"
+ "multicastSocket:didReceivePackets:atTime:"
+ "nanSubscriber:didReceiveData:"
+ "nanSubscriberDidStart:withPeerIPAddress:usingInterface:forRetry:"
+ "nanSubscriberDidStop:withError:willRetry:"
+ "numberWithInteger:"
+ "pingThroughMulticast:"
+ "retryLimit"
+ "sendData:withCompletion:"
+ "sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:"
+ "serverController:didReceiveClientDeviceCheckOut:withError:"
+ "serviceName"
+ "setObject:forKeyedSubscript:"
+ "setRetryLimit:"
+ "setSyncSemaphore:"
+ "syncSemaphore"
+ "updateClientStatus:forDevice:"
+ "v20@?0Q8B16"
+ "v32@0:8@\"MIBUNANSubscriber\"16@\"NSData\"24"
+ "v32@0:8@\"MIBUNWClientDevice\"16@\"NSError\"24"
+ "v36@0:8@\"MIBUNANSubscriber\"16@\"NSError\"24B32"
+ "v36@0:8@16@24B32"
+ "v40@0:8@\"MIBUMulticastSocket\"16@\"NSMutableArray\"24@\"NSDate\"32"
+ "v44@0:8@\"MIBUNANSubscriber\"16@\"NSString\"24@\"NSString\"32B40"
+ "v44@0:8@16@24@32B40"
+ "v48@0:8@\"NSMutableArray\"16@\"NSDate\"24@?<v@?QB>32@\"NSObject<OS_dispatch_queue>\"40"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\b+"
- "\x11"
- "%@: Received the very first packet!"
- "%{public}@: %{public}@ checked in, invalidating unicast connection"
- "%{public}@: Failed to create TCP server device."
- "%{public}@: Failed to create server device."
- "%{public}@: state :%lu; progress = %lu"
- "%{public}@: state: %lu; packets: %lu/%lu (%lu missing), progress = %lu"
- "@22@0:8{ether_addr=[6C]}16"
- "Control connection available for peer: %{public}@"
- "Data session confirmed for peer: %{public}@"
- "Discovered publisher: %{public}@ (MAC: %{public}@)"
- "Establishing connection with sender %{public}@"
- "Failed to add symbol: %d"
- "Joining multicast with config: %{public}@"
- "NAN Subscribing to %{public}@ with service name %{public}@"
- "NAN session request failed with error: %ld"
- "NAN session request started"
- "NAN session terminated with reason: %ld"
- "NAN subscriber failed to start with error: %ld"
- "NAN subscriber lost discovery result for publisher: %{public}@"
- "NAN subscriber started"
- "NAN subscriber terminated with reason: %ld"
- "Setting host address to %{public}@"
- "Starting WiFi Aware Session..."
- "Stopping multicast data transfer..."
- "TCP device %{public}@ checked out"
- "_connectToSender"
- "_consumePacket:arrivalTime:withCompletion:inQueue:"
- "_convertEtherAddrToString:"
- "_convertIn6AddrToString:"
- "_handleInboundPacket:arrivalTime:"
- "_multicastConfig"
- "_session"
- "_startMulticastReceiver"
- "_subscribeToMulticastAddress:serviceName:"
- "_subscriber"
- "checkOut"
- "clientDeviceDidCheckOut:"
- "doubleValue"
- "initWithHostAddress:hostPort:interfaceName:statusDelegate:"
- "multicastSocket:didReceivePacket:atTime:"
- "numberWithDouble:"
- "numberWithUnsignedChar:"
- "v16@?0B8B12"
- "v40@0:8@\"MIBUMulticastSocket\"16@\"NSObject<OS_dispatch_data>\"24@\"NSDate\"32"

```
