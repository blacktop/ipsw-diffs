## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-655.99.0.0.0
-  __TEXT.__text: 0x17ad8
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x201c
+730.25.0.0.0
+  __TEXT.__text: 0x19388
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x21dc
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x3a19
+  __TEXT.__cstring: 0x3d91
   __TEXT.__oslogstring: 0x278
-  __TEXT.__gcc_except_tab: 0x1f0
-  __TEXT.__unwind_info: 0x6f0
-  __TEXT.__objc_classname: 0x61b
-  __TEXT.__objc_methname: 0x5c2d
-  __TEXT.__objc_methtype: 0x1386
-  __TEXT.__objc_stubs: 0x3300
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x998
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__gcc_except_tab: 0x208
+  __TEXT.__unwind_info: 0x758
+  __TEXT.__objc_classname: 0x641
+  __TEXT.__objc_methname: 0x64e3
+  __TEXT.__objc_methtype: 0x14ce
+  __TEXT.__objc_stubs: 0x35e0
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10e0
+  __DATA_CONST.__objc_selrefs: 0x11f0
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x2f8
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x28a0
-  __AUTH_CONST.__objc_const: 0x4e08
-  __DATA.__objc_ivar: 0x30c
+  __DATA_CONST.__objc_superrefs: 0x100
+  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x2aa0
+  __AUTH_CONST.__objc_const: 0x51b8
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x340
   __DATA.__data: 0x7e0
   __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 752
-  Symbols:   971
-  CStrings:  1507
+  Functions: 800
+  Symbols:   1021
+  CStrings:  1605
 
Symbols:
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_WiFiAwarePairingConfiguration
+ _OBJC_METACLASS_$_WiFiAwarePairingConfiguration
+ _arc4random_uniform
CStrings:
+ "\x03!\x15!"
+ "\x04"
+ "\x11\x15\x11"
+ "%!C(MISSING)"
+ "%!d(MISSING)"
+ "%!l(MISSING)u"
+ "3\x11"
+ "<WiFiAwareDatapathConfiguration: discoveryResult=%!@(MISSING), serviceType=%!s(MISSING), passphrase=%!@(MISSING), pmk=%!@(MISSING), pmkID=%!@(MISSING), serviceSpecificInfo=%!@(MISSING), internetSharing=%!@(MISSING), pairingMethod=%!s(MISSING), pairingCaching=%!s(MISSING), pairSetupServiceSpecificInfo=%!@(MISSING)>"
+ "<WiFiAwareDiscoveryResult: name=%!@(MISSING), serviceSpecificInfo=%!@(MISSING), publishID=%!u(MISSING), publisherAddress=%!@(MISSING), datapath=%!s(MISSING), security=%!s(MISSING), cipherSuite=%!s(MISSING), FSD=%!s(MISSING), rssi=%!l(MISSING)d, pairSetup=%!s(MISSING), pairing=%!@(MISSING)>"
+ "<WiFiAwarePairing supportedMethods=%!@(MISSING), caching=%!s(MISSING)>"
+ "@\"<WiFiAwareDataSessionPairingDelegate>\""
+ "@\"<WiFiAwarePublisherPairingDelegate>\""
+ "@\"WiFiAwarePairingConfiguration\""
+ "@28@0:8@16B24"
+ "@88@0:8@16@24C32C36@40B48q52q60q68B76@80"
+ "@92@0:8@16q24@32@40@48@56@64q72B80@84"
+ "A"
+ "B24@0:8@?16"
+ "B32@0:8^@16^@24"
+ "GTK-CCMP-128"
+ "GTK-GCMP-256"
+ "LL_STATS_REDUCED_AWDL_BW"
+ "LL_STATS_REDUCED_BW_PERCENT_SESSION"
+ "NFC Tag"
+ "Opportunistic"
+ "PIN Code"
+ "PK-2WDH-CCM128"
+ "PK-2WDH-GCM256"
+ "PK-PASN-128"
+ "PK-PASN-256"
+ "Passphrase"
+ "QR Code"
+ "Skipped"
+ "T@\"<WiFiAwareDataSessionPairingDelegate>\",W,N,V_pairingDelegate"
+ "T@\"<WiFiAwarePublisherPairingDelegate>\",W,N,V_pairingDelegate"
+ "T@\"NSArray\",R,N,V_supportedPairSetupMethods"
+ "T@\"WiFiAwarePairingConfiguration\",R,N,V_pairingConfiguration"
+ "T@\"WiFiAwarePublishServiceSpecificInfo\",C,N,V_pairSetupServiceSpecificInfo"
+ "T@\"WiFiAwarePublishServiceSpecificInfo\",R,V_pairSetupServiceSpecificInfo"
+ "TB,R,N,V_pairSetupRequired"
+ "TB,R,N,V_pairingCachingEnabled"
+ "TB,R,V_pairingCachingEnabled"
+ "TB,V_pairingCachingEnabled"
+ "Tq,R,V_pairingMethod"
+ "Tq,V_pairingMethod"
+ "UUID"
+ "WiFiAwareDataRequest.pairSetupServiceSpecificInfo"
+ "WiFiAwareDataRequest.pairingCaching"
+ "WiFiAwareDataRequest.pairingMethod"
+ "WiFiAwareDiscoveryResult.pairSetupRequired"
+ "WiFiAwareDiscoveryResult.pairingConfiguration"
+ "WiFiAwarePairingConfiguration"
+ "WiFiAwarePairingConfiguration.pairingCaching"
+ "WiFiAwarePairingConfiguration.pairingMethods"
+ "WiFiAwarePublishDatapathSecurityConfiguration.pairingConfiguration"
+ "_pairSetupRequired"
+ "_pairSetupServiceSpecificInfo"
+ "_pairingCachingEnabled"
+ "_pairingConfiguration"
+ "_pairingDelegate"
+ "_pairingMethod"
+ "_supportedPairSetupMethods"
+ "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
+ "addAutoPairingBootstrapBlobForPeer:"
+ "characterAtIndex:"
+ "dataUsingEncoding:"
+ "datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:"
+ "fetchAutoPairingBootstrapBlob:error:"
+ "generateDiversifiedPINForDataSession:completionHandler:"
+ "generateDiversifiedPINWithCompletionHandler:"
+ "getActiveTrafficRegistrationWithCompletionHandler:"
+ "initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:"
+ "initWithPairingConfiguration:usingPairingDelegate:"
+ "initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:"
+ "initWithSupportedPairSetupMethods:pairingCachingEnabled:"
+ "low latency"
+ "pairSetupRequired"
+ "pairSetupServiceSpecificInfo"
+ "pairSetupServiceSpecificInfoEqual:"
+ "pairingCachingEnabled"
+ "pairingConfiguration"
+ "pairingDelegate"
+ "pairingMethod"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingNFCTag:"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingPINCode:"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingPassphrase:"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingQRCodeInformation:"
+ "pairingRequestStartedForDataSession:nfcTagScannedCompletionHandler:"
+ "pairingRequestStartedForDataSession:passphraseInputCompletionHandler:"
+ "pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:"
+ "pairingRequestStartedForDataSession:qrCodeScannedCompletionHandler:"
+ "publishPairingRequestIndicatedBySubscriber:withPairingMethod:pairingAuthenticationGeneratedCompletionHandler:"
+ "setPairSetupServiceSpecificInfo:"
+ "setPairingCachingEnabled:"
+ "setPairingDelegate:"
+ "setPairingMethod:"
+ "stringWithCString:encoding:"
+ "stringWithCapacity:"
+ "supportedPairSetupMethods"
+ "v16@?0@\"NSData\"8"
+ "v16@?0@\"NSNumber\"8"
+ "v16@?0@\"NSString\"8"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@0:8q16@?<v@?@\"NSData\">24"
+ "v40@0:8@\"WiFiAwarePublishServiceSpecificInfo\"16q24@?<v@?@\"NSData\">32"
+ "v40@0:8@16q24@?32"
+ "\xc1!"
- "\x01\x15"
- "\x03!\x15"
- "3"
- "<WiFiAwareDatapathConfiguration: discoveryResult=%!@(MISSING), serviceType=%!s(MISSING), passphrase=%!@(MISSING), pmk=%!@(MISSING), pmkID=%!@(MISSING), serviceSpecificInfo=%!@(MISSING), internetSharing=%!@(MISSING)>"
- "<WiFiAwareDiscoveryResult: name=%!@(MISSING), serviceSpecificInfo=%!@(MISSING), publishID=%!u(MISSING), publisherAddress=%!@(MISSING), datapath=%!s(MISSING), security=%!s(MISSING), cipherSuite=%!s(MISSING), FSD=%!s(MISSING), rssi=%!l(MISSING)d>"
- "@72@0:8@16q24@32@40@48@56@64"
- "@76@0:8@16@24C32C36@40B48q52q60q68"
- "initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:"
- "initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:"
- "\xc1"

```
