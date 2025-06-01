## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-745.13.4.0.0
-  __TEXT.__text: 0x7ec10
+750.14.1.4.0
+  __TEXT.__text: 0x80e54
   __TEXT.__auth_stubs: 0x2b30
   __TEXT.__objc_methlist: 0x7a4
-  __TEXT.__cstring: 0x2439a
+  __TEXT.__cstring: 0x24ea9
   __TEXT.__const: 0x204
-  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__gcc_except_tab: 0x2dc
   __TEXT.__oslogstring: 0x16e
-  __TEXT.__unwind_info: 0x13e8
+  __TEXT.__unwind_info: 0x142c
   __TEXT.__objc_classname: 0xfa
-  __TEXT.__objc_methname: 0x2ba1
+  __TEXT.__objc_methname: 0x2c0b
   __TEXT.__objc_methtype: 0xab2
-  __TEXT.__objc_stubs: 0x2c80
+  __TEXT.__objc_stubs: 0x2ce0
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x2b88
+  __DATA_CONST.__const: 0x2b48
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x12a8
-  __DATA_CONST.__objc_selrefs: 0xbd8
+  __DATA_CONST.__objc_selrefs: 0xbf0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__const: 0x29c0
-  __AUTH_CONST.__cfstring: 0x4f60
+  __AUTH_CONST.__const: 0x29d8
+  __AUTH_CONST.__cfstring: 0x5040
   __AUTH_CONST.__objc_const: 0x1f8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FE9EABC3-416C-389F-8522-31D183AC8E45
-  Functions: 1650
-  Symbols:   5247
-  CStrings:  4776
+  UUID: F905FEFA-BFDC-3178-9CA0-3C8D3A4FA360
+  Functions: 1676
+  Symbols:   5297
+  CStrings:  4836
 
Symbols:
+ GCC_except_table44
+ _APBrokerGetInfo
+ _APBrokerGroupGetInfo
+ _APBrokerManagerGetInfoFromBrokerGroup
+ _APBrokeredReceiverGetBrokerGroupID
+ _APBrokeredReceiverGetLTPKHash
+ _APSIsPairingGroupEnabled
+ _APTransportDeviceCopyBrokeredReceiverInfo
+ __APBrokerManagerCallGetInfoCallback
+ __APBrokerManagerClearGetInfoCallbackState
+ __APBrokerManagerGetInfoFromBrokerGroup
+ __APBrokerManagerReleaseBrokerDiscovery
+ __APBrokerManagerRequestBrokerDiscovery
+ ___APBrokerGetInfo_block_invoke
+ ___APBrokerGroupGetInfo_block_invoke
+ ___APBrokerGroupGetInfo_block_invoke_2
+ ___APBrokerGroupGetInfo_block_invoke_3
+ ___APBrokerKeychainUtilsRemoveExpiredAuthTokens_block_invoke
+ ___APBrokerManagerGetInfoFromBrokerGroup_block_invoke
+ ___APBrokerManagerGetInfoFromBrokerGroup_block_invoke_2
+ ___APBrokerManagerGetInfoFromBrokerGroup_block_invoke_3
+ ____APBrokerGroupGetInfoWithOneBroker_block_invoke
+ ____APBrokerManagerCallGetInfoCallback_block_invoke
+ ____APBrokerManagerEnsureKnownNetworkProfileMonitoringStarted_block_invoke
+ ____APBrokerManagerEnsureKnownNetworkProfileMonitoringStarted_block_invoke_2
+ ____APBrokerManagerGetInfoFromBrokerGroup_block_invoke
+ ___block_descriptor_32_e15_v24?0r^v8r^v16l
+ ___block_descriptor_40_e131_v52?0^{__CFString=}8(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})16I44i48l
+ ___block_descriptor_40_e44_v28?0i8^{__CFString=}12^{__CFDictionary=}20l
+ ___block_descriptor_40_e8_32o_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_44_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_52_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_64_e8_32b_e29_v28?0i8^{__CFArray=}12I20S24ls32l8
+ ___block_descriptor_72_e5_v8?0l
+ ___block_descriptor_88_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_tmp.113
+ ___block_descriptor_tmp.115
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.42
+ ___block_descriptor_tmp.52
+ ___block_descriptor_tmp.56
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.67
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.75
+ ___block_literal_global.50
+ ___block_literal_global.62
+ ___browser_CopyBrokerInfoForDeviceID_block_invoke
+ _browser_CopyBrokerInfoForDeviceID
+ _kAPBrokerGetReceiverConnectivityInfoCallbackResponseKey_IfIndex
+ _kAPBrokerManagerGetInfoFromBrokerGroupCallbackResponseKey_BrokerGroupInfo
+ _objc_msgSend$initWithServiceType:
+ _objc_msgSend$isPublicAirPlayNetwork
+ _objc_msgSend$updatePairedPeersWithGroupID:groupInfo:options:completion:
- _CFSetSetValue
- ___block_descriptor_40_e128_v48?0^{__CFString=}8(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})16i44l
- ___block_descriptor_48_e10_v16?0r^v8l
- ___block_descriptor_64_e8_32b_e26_v24?0i8^{__CFArray=}12S20ls32l8
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.114
- ___block_descriptor_tmp.38
- ___block_descriptor_tmp.47
- ___block_descriptor_tmp.48
- ___block_descriptor_tmp.50
- ___block_descriptor_tmp.53
- ___block_descriptor_tmp.63
- ___block_descriptor_tmp.97
- ___block_descriptor_tmp.98
- ___block_literal_global.56
CStrings:
+ "%sDNS (forceModern=%s forceBroker=%s) for deviceID %llu: %s.\n"
+ "/public/info"
+ "750.14.1"
+ "APBrokerGetInfo"
+ "APBrokerGetInfo_block_invoke"
+ "APBrokerManager.corewifi.%{ptr}"
+ "APBrokerManagerBrowseMode _APBrokerManagerGetBrokerBrowseMode(APBrokerManagerRef)"
+ "APBrokerManagerGetInfoFromBrokerGroup"
+ "BrokerGroupInfo"
+ "Cleared pairing group info for %@\n"
+ "Failed to clear pairing group info for %@ due to error: %{error}\n"
+ "Failed to remove expired keychain authToken for %@ due to error: %{error}\n"
+ "Failed to start"
+ "Initial traffic registration %s by prefs.\n"
+ "LOUDNESSNORMALIZATION"
+ "LTPKHashBase64"
+ "OSStatus APBrokerCreateBrokeredReceiverConnectivityInfoFromBrokerResponse(CFDictionaryRef, uint32_t, CFDictionaryRef *)"
+ "OSStatus APBrokerManagerGetInfoFromBrokerGroup(APBrokerManagerRef, CFStringRef, APBrokerManagerGetInfoFromBrokerGroupCallbackBlock)"
+ "OSStatus APBrokerManagerSetBrowseMode(APBrokerManagerRef, APBrowserMode)"
+ "OSStatus APBrokeredReceiverCreateWithTXTRecordBase64(CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, APBrokeredReceiverRef *)"
+ "OSStatus _APBrokerManagerUpdateBrowsing(APBrokerManagerRef)"
+ "OSStatus httpconnection_addInitialTrafficRegistration(APTransportConnectionRef, sockaddr_ip *)"
+ "OSStatus httpconnection_connect(APTransportConnectionRef, const char *, uint32_t, int, Boolean)"
+ "Skipping traffic registration."
+ "[%{ptr}] %###s: register traffic failed with error %#m\n"
+ "[%{ptr}] %s monitoring known network profile, current network %s a public AirPlay network%?{end}: %@"
+ "[%{ptr}] Address resolved to %@:%d, ifIndex: %u\n"
+ "[%{ptr}] Async connecting to '%s' port %d ifIndex: %u\n"
+ "[%{ptr}] Broker GetInfo finished. Calling callback\n"
+ "[%{ptr}] Broker GetInfo timed out. Calling callback with error %#m\n"
+ "[%{ptr}] Brokered Discovery disabled in Presence mode by pref"
+ "[%{ptr}] Brokered browse mode set to %d\n"
+ "[%{ptr}] Browser browse mode set to %d\n"
+ "[%{ptr}] Detected network profile updated, isPublicAirPlayNetwork: %s -> %s"
+ "[%{ptr}] Failed to parse ifIndex from destination: %'s %#m\n"
+ "[%{ptr}] Get Info with broker group %@ finished: err=%#m%?{end} response=%@\n"
+ "[%{ptr}] Get broker group info%?{end} for %'@\n"
+ "[%{ptr}] Get info request finished. status=%ld, err=%#m%?{end}, data=%@\n"
+ "[%{ptr}] GetInfo\n"
+ "[%{ptr}] Got address from broker manager: %@, ifIndex %u port %d.\n"
+ "[%{ptr}] Requesting info for group: %@\n"
+ "[%{ptr}] Service resolved to %@ ifIndex %u\n"
+ "[%{ptr}] Unexpected event type: %ld"
+ "[%{ptr}] Unhandled browse mode: %d"
+ "[%{ptr}] Will not request Brokered Discovery in Presence mode, current network is not a public AirPlay network"
+ "[%{ptr}] [%{ptr}] Got GetInfo callback from broker [%{ptr}] with error: %#m%?{end} and response: %@\n"
+ "_APBrokerHTTPParseIfIndexFromDestination"
+ "_APBrokerManagerCallGetInfoCallback"
+ "brokerDisablePresence"
+ "browser_copyBrokerInfoForDeviceID"
+ "ifIndex"
+ "initWithServiceType:"
+ "is"
+ "is not"
+ "isPublicAirPlayNetwork"
+ "performInitialTrafficRegistration"
+ "supportedWiFiNetworkSSIDs"
+ "updatePairedPeersWithGroupID:groupInfo:options:completion:"
+ "v28@?0i8^{__CFArray=}12I20S24"
+ "v36@?0^{__CFString=}8I16i20^v24i32"
+ "v40@?0^{__CFDictionary=}8^{__CFData=}16I24q28i36"
+ "v52@?0^{__CFString=}8(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})16I44i48"
+ "void APBrokerGetInfo(APBrokerRef, APBrokerGetInfoCallbackBlock)"
+ "void APBrokerGetInfo(APBrokerRef, APBrokerGetInfoCallbackBlock)_block_invoke"
+ "void APBrokerGroupGetInfo(APBrokerGroupRef, APBrokerGroupGetInfoCallbackBlock)"
+ "void APBrokerKeychainUtilsRemoveExpiredAuthTokens(void)_block_invoke"
+ "void _APBrokerGroupHandleBrokerGetInfo(void *, APBrokerGroupOperationStatus *, OSStatus, void *, CFDictionaryRef)"
+ "void _APBrokerHTTPHandleResolveResponse(APBrokerHTTPRequestData *, CFStringRef, sockaddr_ip, uint32_t, OSStatus)"
+ "void _APBrokerManagerEnsureKnownNetworkProfileMonitoringStarted(APBrokerManagerRef)_block_invoke"
+ "void _APBrokerManagerEnsureKnownNetworkProfileMonitoringStarted(APBrokerManagerRef)_block_invoke_2"
+ "void _APBrokerManagerHandleBrokerGetInfoTimeout(APBrokerManagerRef)"
+ "void _APBrokerManagerHandleBrokerGroupGetInfoResponse(APBrokerManagerRef, OSStatus, CFStringRef, CFDictionaryRef)"
- "%sDNS (forceModern=%s) for deviceID %llu: %s.\n"
- "745.13.4"
- "Failed to remove expired keychain authToken for %@\n"
- "OSStatus APBrokerCreateBrokeredReceiverConnectivityInfoFromBrokerResponse(CFDictionaryRef, CFDictionaryRef *)"
- "OSStatus APBrokerManagerSetBrowseMode(APBrokerManagerRef, APBrokerManagerBrowseMode)"
- "OSStatus APBrokeredReceiverCreateWithTXTRecordBase64(CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, CFStringRef, APBrokeredReceiverRef *)"
- "OSStatus httpconnection_connect(APTransportConnectionRef, const char *, int, Boolean)"
- "[%{ptr}] %###s: register traffic failed with error %m\n"
- "[%{ptr}] Address resolved to %@:%d\n"
- "[%{ptr}] Async connecting to '%s' port %d\n"
- "[%{ptr}] Broker manager browse mode set to %d\n"
- "[%{ptr}] Got address from broker manager: %@, port %d.\n"
- "[%{ptr}] Service resolved to %@\n"
- "browser_getBrokerMode"
- "v24@?0i8^{__CFArray=}12S20"
- "v32@?0^{__CFString=}8i16^v20i28"
- "v36@?0^{__CFDictionary=}8^{__CFData=}16q24i32"
- "v48@?0^{__CFString=}8(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})16i44"
- "void _APBrokerHTTPHandleResolveResponse(APBrokerHTTPRequestData *, CFStringRef, sockaddr_ip, OSStatus)"

```
