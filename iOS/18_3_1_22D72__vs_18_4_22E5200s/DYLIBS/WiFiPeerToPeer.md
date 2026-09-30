## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-750.3.4.1.0
-  __TEXT.__text: 0x19388
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x21dc
+780.39.0.0.0
+  __TEXT.__text: 0x1a5d0
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x29e4
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x3d91
-  __TEXT.__oslogstring: 0x278
-  __TEXT.__gcc_except_tab: 0x208
-  __TEXT.__unwind_info: 0x758
-  __TEXT.__objc_classname: 0x641
-  __TEXT.__objc_methname: 0x64e3
-  __TEXT.__objc_methtype: 0x14ce
-  __TEXT.__objc_stubs: 0x35e0
+  __TEXT.__cstring: 0x3ef3
+  __TEXT.__oslogstring: 0x683
+  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__unwind_info: 0x770
+  __TEXT.__objc_classname: 0x693
+  __TEXT.__objc_methname: 0x68c3
+  __TEXT.__objc_methtype: 0x1557
+  __TEXT.__objc_stubs: 0x37e0
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0xb20
-  __DATA_CONST.__objc_classlist: 0x108
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__const: 0xac8
+  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11f0
-  __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x300
+  __DATA_CONST.__objc_selrefs: 0x1338
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x108
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x2aa0
-  __AUTH_CONST.__objc_const: 0x51b8
+  __AUTH_CONST.__cfstring: 0x2b20
+  __AUTH_CONST.__objc_const: 0x4988
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x340
-  __DATA.__data: 0x7e0
-  __DATA_DIRTY.__objc_data: 0xa00
+  __DATA.__objc_ivar: 0x360
+  __DATA.__data: 0x840
+  __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 800
-  Symbols:   1021
-  CStrings:  1605
+  Functions: 833
+  Symbols:   1061
+  CStrings:  1659
 
Symbols:
+ _OBJC_CLASS_$_WiFiRemoteClientCountryCodeMonitor
+ _OBJC_METACLASS_$_WiFiRemoteClientCountryCodeMonitor
+ __os_log_debug_impl
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "\x04\x11"
+ "\x05!"
+ "\x15\x13"
+ "<WiFiAwarePublishConfiguration: serviceName=%@, serviceSpecificInfo=%@, furtherServiceDiscoveryRequired=%s, jumboMessages=%s, dataConfig=%@, fastDiscovery=%@, internetSharing=%@, channelInfo=%@, cc=%@>"
+ "<WiFiAwarePublisher: PublishID=%@, Service=%@, MaximumNANDataPathSupported=%@>"
+ "<WiFiAwareSubscribeConfiguration: name=%@, serviceSpecificInfo=%@, fastDiscoveryConfiguration=%@, multicastAddress=%@ timeoutAfter=%ld, channelInfo=%@, cc=%@>"
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
+ "T@\"WiFiChannel\",C,N,V_channelInfo"
+ "T@?,C,N,V_setCountryCodeHandler"
+ "Tq,N,V_timeoutAfter"
+ "WiFiAwarePublishConfiguration.channelInfo"
+ "WiFiAwarePublishConfiguration.countryCode"
+ "WiFiAwareSubscribeConfiguration.channelInfo"
+ "WiFiAwareSubscribeConfiguration.countryCode"
+ "WiFiAwareSubscribeConfiguration.timeout"
+ "WiFiRemoteClientCountryCodeMonitor"
+ "WiFiRemoteClientCountryCodeMonitorXPCDelegate"
+ "_channelInfo"
+ "_maximumNANDataPath"
+ "_setCountryCodeHandler"
+ "_timeoutAfter"
+ "channelConfigurationEqual:"
+ "channelInfo"
+ "com.apple.wifip2p.WiFiRemoteClientCountryMonitor"
+ "countryCodeEqual:"
+ "datapathPairingRequestStartedWithPairingMethod: %ld"
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
- "\x03\x11"
- "\x13\x13"
- "%lu"
- "1"
- "<WiFiAwarePublishConfiguration: serviceName=%@, serviceSpecificInfo=%@, furtherServiceDiscoveryRequired=%s, jumboMessages=%s, dataConfig=%@, fastDiscovery=%@, internetSharing=%@>"
- "<WiFiAwarePublisher: PublishID=%@, Service=%@>"
- "<WiFiAwareSubscribeConfiguration: name=%@, serviceSpecificInfo=%@, fastDiscoveryConfiguration=%@>"
- "publishStartedWithInstanceID:"
- "v16@?0@\"NSNumber\"8"

```
