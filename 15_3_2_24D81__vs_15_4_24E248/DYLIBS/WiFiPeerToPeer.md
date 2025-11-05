## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer`

```diff

-685.5.0.0.0
-  __TEXT.__text: 0x1ba90
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0x21dc
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x3d91
-  __TEXT.__oslogstring: 0x278
-  __TEXT.__gcc_except_tab: 0x208
-  __TEXT.__unwind_info: 0x778
-  __TEXT.__objc_classname: 0x641
-  __TEXT.__objc_methname: 0x64e3
-  __TEXT.__objc_methtype: 0x14ce
-  __TEXT.__objc_stubs: 0x35e0
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x350
-  __DATA_CONST.__objc_classlist: 0x108
-  __DATA_CONST.__objc_protolist: 0xa8
+725.36.0.0.0
+  __TEXT.__text: 0x1d508
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0x2adc
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x3fd7
+  __TEXT.__oslogstring: 0x683
+  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__unwind_info: 0x7b8
+  __TEXT.__objc_classname: 0x6b3
+  __TEXT.__objc_methname: 0x69b7
+  __TEXT.__objc_methtype: 0x157a
+  __TEXT.__objc_stubs: 0x3880
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11f0
-  __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x220
-  __AUTH_CONST.__const: 0xc80
-  __AUTH_CONST.__cfstring: 0x2aa0
-  __AUTH_CONST.__objc_const: 0x51b8
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x340
-  __DATA.__data: 0x7e0
+  __DATA_CONST.__objc_selrefs: 0x1360
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x110
+  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__const: 0xc50
+  __AUTH_CONST.__cfstring: 0x2b80
+  __AUTH_CONST.__objc_const: 0x4b20
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x370
+  __DATA.__data: 0x840
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0E7EC8DE-0873-3616-8976-5114481C88B9
-  Functions: 825
-  Symbols:   2147
-  CStrings:  1928
+  UUID: 9393F831-FB13-3D14-8523-7FFD7CE50FF5
+  Functions: 877
+  Symbols:   2259
+  CStrings:  2002
 
Symbols:
+ +[WiFiAwareMulticastConfiguration supportsSecureCoding]
+ -[WiFiAwareMulticastConfiguration .cxx_destruct]
+ -[WiFiAwareMulticastConfiguration copyWithZone:]
+ -[WiFiAwareMulticastConfiguration description]
+ -[WiFiAwareMulticastConfiguration dynamicLinkRate]
+ -[WiFiAwareMulticastConfiguration encodeWithCoder:]
+ -[WiFiAwareMulticastConfiguration initWithCoder:]
+ -[WiFiAwareMulticastConfiguration init]
+ -[WiFiAwareMulticastConfiguration isEqual:]
+ -[WiFiAwareMulticastConfiguration multicastAddressConfigurationEqual:]
+ -[WiFiAwareMulticastConfiguration multicastAddress]
+ -[WiFiAwareMulticastConfiguration setDynamicLinkRate:]
+ -[WiFiAwareMulticastConfiguration setMulticastAddress:]
+ -[WiFiAwarePublishConfiguration channelConfigurationEqual:]
+ -[WiFiAwarePublishConfiguration channelInfo]
+ -[WiFiAwarePublishConfiguration countryCodeEqual:]
+ -[WiFiAwarePublishConfiguration countryCode]
+ -[WiFiAwarePublishConfiguration multicastConfigurationEqual:]
+ -[WiFiAwarePublishConfiguration multicastConfiguration]
+ -[WiFiAwarePublishConfiguration setChannelInfo:]
+ -[WiFiAwarePublishConfiguration setCountryCode:]
+ -[WiFiAwarePublishConfiguration setMulticastConfiguration:]
+ -[WiFiAwarePublisher publishDetectedMulticastError:fromMulticastReceiver:]
+ -[WiFiAwarePublisher publishReceivedDataBlobForMulticastSession:fromPeer:]
+ -[WiFiAwarePublisher publishStartedWithInstanceID:maximumNANDataPath:]
+ -[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:]
+ -[WiFiAwarePublisher terminateMulticastSession:completionHandler:]
+ -[WiFiAwareSubscribeConfiguration channelConfigurationEqual:]
+ -[WiFiAwareSubscribeConfiguration channelInfo]
+ -[WiFiAwareSubscribeConfiguration countryCodeEqual:]
+ -[WiFiAwareSubscribeConfiguration countryCode]
+ -[WiFiAwareSubscribeConfiguration multicastConfigurationEqual:]
+ -[WiFiAwareSubscribeConfiguration multicastConfiguration]
+ -[WiFiAwareSubscribeConfiguration setChannelInfo:]
+ -[WiFiAwareSubscribeConfiguration setCountryCode:]
+ -[WiFiAwareSubscribeConfiguration setMulticastConfiguration:]
+ -[WiFiAwareSubscribeConfiguration setTimeoutAfter:]
+ -[WiFiAwareSubscribeConfiguration timeoutAfter]
+ -[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:]
+ -[WiFiAwareSubscriber subscribeDetectedMulticastError:fromMulticastSender:]
+ -[WiFiAwareSubscriber subscribeReceivedDataBlobForMulticastSession:fromPeer:]
+ -[WiFiRemoteClientCountryCodeMonitor .cxx_destruct]
+ -[WiFiRemoteClientCountryCodeMonitor beginMonitoring]
+ -[WiFiRemoteClientCountryCodeMonitor endMonitoring]
+ -[WiFiRemoteClientCountryCodeMonitor exportedInterface]
+ -[WiFiRemoteClientCountryCodeMonitor exportedObject]
+ -[WiFiRemoteClientCountryCodeMonitor init]
+ -[WiFiRemoteClientCountryCodeMonitor setCountryCode:]
+ -[WiFiRemoteClientCountryCodeMonitor setCountryCodeHandler]
+ -[WiFiRemoteClientCountryCodeMonitor setSetCountryCodeHandler:]
+ -[WiFiRemoteClientCountryCodeMonitor startConnectionUsingProxy:completionHandler:]
+ OBJC_IVAR_$_WiFiAwareMulticastConfiguration._dynamicLinkRate
+ OBJC_IVAR_$_WiFiAwareMulticastConfiguration._multicastAddress
+ OBJC_IVAR_$_WiFiAwarePublishConfiguration._channelInfo
+ OBJC_IVAR_$_WiFiAwarePublishConfiguration._countryCode
+ OBJC_IVAR_$_WiFiAwarePublishConfiguration._multicastConfiguration
+ OBJC_IVAR_$_WiFiAwarePublisher._maximumNANDataPath
+ OBJC_IVAR_$_WiFiAwareSubscribeConfiguration._channelInfo
+ OBJC_IVAR_$_WiFiAwareSubscribeConfiguration._countryCode
+ OBJC_IVAR_$_WiFiAwareSubscribeConfiguration._multicastConfiguration
+ OBJC_IVAR_$_WiFiAwareSubscribeConfiguration._timeoutAfter
+ OBJC_IVAR_$_WiFiRemoteClientCountryCodeMonitor._setCountryCodeHandler
+ OBJC_IVAR_$_WiFiRemoteClientCountryCodeMonitor._xpcConnection
+ _OBJC_CLASS_$_WiFiAwareMulticastConfiguration
+ _OBJC_CLASS_$_WiFiRemoteClientCountryCodeMonitor
+ _OBJC_METACLASS_$_WiFiAwareMulticastConfiguration
+ _OBJC_METACLASS_$_WiFiRemoteClientCountryCodeMonitor
+ _WiFiAwareCipherSuiteString
+ _WiFiAwarePairingMethodString
+ __115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.111
+ __64-[WiFiP2PTrafficRegistrationReservation activateWithCompletion:]_block_invoke.217
+ __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.136
+ __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.137
+ __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.150
+ __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.156
+ __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke_2.155
+ __79-[WiFiAwarePublisher generateStatisticsReportForDataSession:completionHandler:]_block_invoke.101
+ __81-[AWDLServiceDiscoveryManager getActiveTrafficRegistrationWithCompletionHandler:]_block_invoke.165
+ __OBJC_$_CLASS_METHODS_WiFiAwareMulticastConfiguration
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareMulticastConfiguration
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareMulticastConfiguration
+ __OBJC_$_INSTANCE_METHODS_WiFiRemoteClientCountryCodeMonitor
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareMulticastConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_WiFiRemoteClientCountryCodeMonitor
+ __OBJC_$_PROP_LIST_WiFiAwareMulticastConfiguration
+ __OBJC_$_PROP_LIST_WiFiRemoteClientCountryCodeMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiRemoteClientCountryCodeMonitorXPCDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiRemoteClientCountryCodeMonitorXPCDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiRemoteClientCountryCodeMonitorXPCDelegate
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareMulticastConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_WiFiRemoteClientCountryCodeMonitor
+ __OBJC_CLASS_RO_$_WiFiAwareMulticastConfiguration
+ __OBJC_CLASS_RO_$_WiFiRemoteClientCountryCodeMonitor
+ __OBJC_LABEL_PROTOCOL_$_WiFiRemoteClientCountryCodeMonitorXPCDelegate
+ __OBJC_METACLASS_RO_$_WiFiAwareMulticastConfiguration
+ __OBJC_METACLASS_RO_$_WiFiRemoteClientCountryCodeMonitor
+ __OBJC_PROTOCOL_$_WiFiRemoteClientCountryCodeMonitorXPCDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiRemoteClientCountryCodeMonitorXPCDelegate
+ ___108-[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:]_block_invoke
+ ___109-[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:]_block_invoke
+ ___66-[WiFiAwarePublisher terminateMulticastSession:completionHandler:]_block_invoke
+ __block_literal_global.175
+ __block_literal_global.215
+ __block_literal_global.275
+ __block_literal_global.372
+ __block_literal_global.618
+ __block_literal_global.621
+ __os_log_debug_impl
+ _objc_msgSend$channelConfigurationEqual:
+ _objc_msgSend$channelInfo
+ _objc_msgSend$countryCodeEqual:
+ _objc_msgSend$dynamicLinkRate
+ _objc_msgSend$multicastConfiguration
+ _objc_msgSend$multicastConfigurationEqual:
+ _objc_msgSend$pairSetupServiceSpecificInfoEqual:
+ _objc_msgSend$publisher:detectedMulticastError:fromMulticastReceiver:
+ _objc_msgSend$publisher:receivedDataBlobForMulticastSession:fromPeer:
+ _objc_msgSend$sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:
+ _objc_msgSend$setChannelInfo:
+ _objc_msgSend$setCountryCode:
+ _objc_msgSend$setCountryCodeHandler
+ _objc_msgSend$setDynamicLinkRate:
+ _objc_msgSend$setMulticastConfiguration:
+ _objc_msgSend$setTimeoutAfter:
+ _objc_msgSend$startCountryCodeMonitoringWithCompletionHandler:
+ _objc_msgSend$subscriber:detectedMulticastError:fromMulticastSender:
+ _objc_msgSend$subscriber:receivedDataBlobForMulticastSession:fromPeer:
+ _objc_msgSend$terminateMulticastSession:completionHandler:
+ _objc_msgSend$timeoutAfter
- -[WiFiAwarePublisher publishStartedWithInstanceID:]
- __115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.126
- __64-[WiFiP2PTrafficRegistrationReservation activateWithCompletion:]_block_invoke.215
- __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.134
- __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.135
- __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.148
- __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.152
- __79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke_2.153
- __79-[WiFiAwarePublisher generateStatisticsReportForDataSession:completionHandler:]_block_invoke.94
- __81-[AWDLServiceDiscoveryManager getActiveTrafficRegistrationWithCompletionHandler:]_block_invoke.163
- ___block_descriptor_40_e8_32r_e18_v16?0"NSNumber"8l
- __block_literal_global.165
- __block_literal_global.213
- __block_literal_global.273
- __block_literal_global.370
- __block_literal_global.614
- __block_literal_global.619
CStrings:
+ "<WiFiAwareMulticastConfiguration: multicastAddress=%@, dynamicLinkRate=%s>"
+ "<WiFiAwarePublishConfiguration: serviceName=%@, serviceSpecificInfo=%@, furtherServiceDiscoveryRequired=%s, jumboMessages=%s, dataConfig=%@, fastDiscovery=%@, internetSharing=%@, channelInfo=%@, cc=%@, multicastConfiguration=%@>"
+ "<WiFiAwarePublisher: PublishID=%@, Service=%@, MaximumNANDataPathSupported=%@>"
+ "<WiFiAwareSubscribeConfiguration: name=%@, serviceSpecificInfo=%@, fastDiscoveryConfiguration=%@, multicastAddress=%@ timeoutAfter=%ld, channelInfo=%@, cc=%@, multicastConfiguration=%@>"
+ "@\"WiFiAwareMulticastConfiguration\""
+ "Invoking pairing delegate method pairingRequestIndicatedForPublisher for PIN"
+ "Invoking pairing delegate method pairingRequestIndicatedForPublisher for Passphrase"
+ "Invoking pairing delegate method pairingRequestStartedForDataSession for PIN"
+ "Invoking pairing delegate method pairingRequestStartedForDataSession for Passphrase"
+ "Invoking pairingAuthenticationGeneratedCompletionHandler callback"
+ "No pairing delegate, skipping invoking pairingRequestIndicatedForPublisher"
+ "No pairing delegate, skipping invoking pairingRequestStartedForDataSession"
+ "No passphrase supplied in passphraseInputCompletionHandler"
+ "No pin supplied in pinCodeInputCompletionHandler"
+ "Pairing delegate does not implement method pairingRequestIndicatedForPublisher"
+ "Pairing delegate does not implement method pairingRequestStartedForDataSession"
+ "Passphrase supplied, calling authenticationInputCompletion"
+ "Pin supplied, calling authenticationInputCompletion"
+ "T@\"NSString\",C,N,V_countryCode"
+ "T@\"WiFiAwareMulticastConfiguration\",C,N,V_multicastConfiguration"
+ "T@\"WiFiChannel\",C,N,V_channelInfo"
+ "T@?,C,N,V_setCountryCodeHandler"
+ "TB,N,V_dynamicLinkRate"
+ "Tq,N,V_timeoutAfter"
+ "WiFiAwareMulticastConfiguration"
+ "WiFiAwarePublishConfiguration.channelInfo"
+ "WiFiAwarePublishConfiguration.countryCode"
+ "WiFiAwarePublishConfiguration.dynamicLinkRate"
+ "WiFiAwarePublishConfiguration.multicastConfiguration"
+ "WiFiAwareSubscribeConfiguration.channelInfo"
+ "WiFiAwareSubscribeConfiguration.countryCode"
+ "WiFiAwareSubscribeConfiguration.timeout"
+ "WiFiRemoteClientCountryCodeMonitor"
+ "WiFiRemoteClientCountryCodeMonitorXPCDelegate"
+ "_channelInfo"
+ "_dynamicLinkRate"
+ "_maximumNANDataPath"
+ "_multicastConfiguration"
+ "_setCountryCodeHandler"
+ "_timeoutAfter"
+ "channelConfigurationEqual:"
+ "channelInfo"
+ "com.apple.wifip2p.WiFiRemoteClientCountryMonitor"
+ "countryCodeEqual:"
+ "datapathPairingRequestStartedWithPairingMethod: %ld"
+ "dynamicLinkRate"
+ "multicastConfiguration"
+ "multicastConfigurationEqual:"
+ "publishDetectedMulticastError:fromMulticastReceiver:"
+ "publishPairingRequestIndicatedBySubscriber with pairing method: %ld"
+ "publishReceivedDataBlobForMulticastSession:fromPeer:"
+ "publishStartedWithInstanceID:maximumNANDataPath:"
+ "publisher:detectedMulticastError:fromMulticastReceiver:"
+ "publisher:receivedDataBlobForMulticastSession:fromPeer:"
+ "sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:"
+ "setChannelInfo:"
+ "setCountryCode:"
+ "setCountryCodeHandler"
+ "setDynamicLinkRate:"
+ "setMulticastConfiguration:"
+ "setSetCountryCodeHandler:"
+ "setTimeoutAfter:"
+ "startCountryCodeMonitoringWithCompletionHandler:"
+ "subscribeDetectedMulticastError:fromMulticastSender:"
+ "subscribeReceivedDataBlobForMulticastSession:fromPeer:"
+ "subscriber:detectedMulticastError:fromMulticastSender:"
+ "subscriber:receivedDataBlobForMulticastSession:fromPeer:"
+ "terminateMulticastSession:completionHandler:"
+ "timeoutAfter"
+ "v24@0:8@?<v@?q>16"
+ "v24@0:8C16I20"
+ "v32@0:8@\"NSData\"16@\"WiFiMACAddress\"24"
+ "v32@0:8@\"WiFiMACAddress\"16@?<v@?q>24"
+ "v32@0:8q16@\"WiFiMACAddress\"24"
- "%lu"
- "1"
- "<WiFiAwarePublishConfiguration: serviceName=%@, serviceSpecificInfo=%@, furtherServiceDiscoveryRequired=%s, jumboMessages=%s, dataConfig=%@, fastDiscovery=%@, internetSharing=%@>"
- "<WiFiAwarePublisher: PublishID=%@, Service=%@>"
- "<WiFiAwareSubscribeConfiguration: name=%@, serviceSpecificInfo=%@, fastDiscoveryConfiguration=%@>"
- "publishStartedWithInstanceID:"
- "v16@?0@\"NSNumber\"8"

```
