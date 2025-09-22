## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-153.0.1.0.0
-  __TEXT.__text: 0x2d1e0
+153.40.11.0.0
+  __TEXT.__text: 0x2de8c
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x1568
+  __TEXT.__objc_methlist: 0x1580
   __TEXT.__const: 0x4908
-  __TEXT.__cstring: 0xe08
-  __TEXT.__oslogstring: 0x36a9
+  __TEXT.__cstring: 0xe64
+  __TEXT.__oslogstring: 0x385e
   __TEXT.__gcc_except_tab: 0x654
-  __TEXT.__unwind_info: 0xca8
+  __TEXT.__unwind_info: 0xce8
   __TEXT.__objc_classname: 0x31a
-  __TEXT.__objc_methname: 0x366e
-  __TEXT.__objc_methtype: 0x159a
-  __TEXT.__objc_stubs: 0x28e0
+  __TEXT.__objc_methname: 0x3702
+  __TEXT.__objc_methtype: 0x1517
+  __TEXT.__objc_stubs: 0x2980
   __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x818
+  __DATA_CONST.__const: 0x840
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcc0
+  __DATA_CONST.__objc_selrefs: 0xce0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x650
-  __AUTH_CONST.__const: 0x2260
-  __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0x4988
+  __AUTH_CONST.__const: 0x2320
+  __AUTH_CONST.__cfstring: 0x980
+  __AUTH_CONST.__objc_const: 0x49a0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x274
+  __DATA.__objc_ivar: 0x278
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x38
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E97AF1E5-75C7-3217-8D8B-C418E3163489
-  Functions: 1249
-  Symbols:   4389
-  CStrings:  1283
+  UUID: 49ECD4A6-2392-3DCC-875A-4A37E012AB91
+  Functions: 1273
+  Symbols:   4464
+  CStrings:  1296
 
Symbols:
+ -[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:].cold.3
+ -[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]
+ -[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:].cold.1
+ -[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:].cold.2
+ -[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:].cold.3
+ -[MIBUNANPublisher terminateMulticastSessionWithPeer:withCompletion:]
+ -[WiFiMACAddress(MIBUExtension) initWithLinkIPv6AddressString:]
+ _OBJC_IVAR_$_MIBUNWServerController._nanIPv6AddrMapping
+ ___37-[MIBUNANPublisher publisherStarted:]_block_invoke.149
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.136
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.136.cold.1
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.139
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.139
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.139.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.139.cold.2
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.143
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.143.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.148
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.148.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.cold.4
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.140
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.140.cold.1
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.125
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.125.cold.1
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.125.cold.2
+ ___51-[MIBUNANPublisher publisher:terminatedWithReason:]_block_invoke.158
+ ___53-[MIBUNANPublisher publisher:failedToStartWithError:]_block_invoke.152
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.142
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.142.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.142.cold.2
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.143
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.143.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.180
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.180.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.180.cold.2
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.180.cold.3
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.183
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.183.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.186
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.93
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.93.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.99
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.99.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.99.cold.2
+ ___69-[MIBUNANPublisher terminateMulticastSessionWithPeer:withCompletion:]_block_invoke
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.108
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.108.cold.1
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.114
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.114.cold.1
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.114.cold.2
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.cold.1
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke_2
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke_2.cold.1
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.155
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.155.cold.1
+ ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.191
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.166
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.166.cold.1
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.166.cold.2
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.166.cold.3
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.169
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.169.cold.1
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.174
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke_2.176
+ ___block_descriptor_56_e8_32s40s48bs_e8_v16?0q8ls32l8s40l8s48l8
+ ___block_literal_global.107
+ ___block_literal_global.127
+ ___block_literal_global.132
+ ___block_literal_global.152
+ ___block_literal_global.157
+ ___block_literal_global.179
+ ___block_literal_global.182
+ ___block_literal_global.185
+ ___block_literal_global.188
+ ___block_literal_global.190
+ _objc_msgSend$_terminateMulticastSessionWithPeer:withCompletion:
+ _objc_msgSend$initWithLinkIPv6AddressString:
+ _objc_msgSend$initWithLinkLocalIPv6Address:
+ _objc_msgSend$terminateMulticastSession:completionHandler:
+ _objc_msgSend$terminateMulticastSessionWithPeer:withCompletion:
- ___37-[MIBUNANPublisher publisherStarted:]_block_invoke.132
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.119
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.119.cold.1
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.122
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.141
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.141.cold.1
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.108
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.108.cold.1
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.108.cold.2
- ___51-[MIBUNANPublisher publisher:terminatedWithReason:]_block_invoke.141
- ___53-[MIBUNANPublisher publisher:failedToStartWithError:]_block_invoke.135
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.125
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.125.cold.1
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.125.cold.2
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.126
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.126.cold.1
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.163
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.163.cold.1
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.163.cold.2
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.163.cold.3
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.166
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.166.cold.1
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.169
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.96
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.96.cold.1
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.96.cold.2
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.148
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.148.cold.1
- ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.174
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.149
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.149.cold.1
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.149.cold.2
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.149.cold.3
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.152
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.152.cold.1
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.157
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke_2.159
- ___block_literal_global.104
- ___block_literal_global.115
- ___block_literal_global.128
- ___block_literal_global.134
- ___block_literal_global.140
- ___block_literal_global.146
- ___block_literal_global.154
- ___block_literal_global.173
- ___block_literal_global.92
CStrings:
+ "%{public}@: Failed to create WiFiMACAddress from IPv6 address: %{public}@"
+ "%{public}@: Failed to terminate data session with peer: %{public}@ error: %ld"
+ "%{public}@: Failed to terminate multicast session with peer: %{public}@ error: %ld"
+ "%{public}@: Terminating NAN data session with peer: %{public}@"
+ "%{public}@: Terminating NAN multicast session with peer: %{public}@"
+ "Failed to terminate multicast session for device: %{public}@ error: %{public}@"
+ "Invalid NAN peer IPv6 address: %@"
+ "NAN data session with %@ failed to stop: %ld"
+ "NAN multicast session with %@ failed to stop: %ld"
+ "No NAN IPv6 address found for TCP device."
+ "_nanIPv6AddrMapping"
+ "_terminateMulticastSessionWithPeer:withCompletion:"
+ "initWithLinkIPv6AddressString:"
+ "initWithLinkLocalIPv6Address:"
+ "terminateMulticastSession:completionHandler:"
+ "terminateMulticastSessionWithPeer:withCompletion:"
- "%{public}@: Failed to terminate data session: %ld"
- "NAN data session failed to stop: %ld"
- "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
- "v48@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40"
- "v48@0:8@16@24@32@40"

```
