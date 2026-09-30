## STSXPCHelper

> `/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper`

```diff

-4.5.1.0.0
-  __TEXT.__text: 0x37f7c
+5.0.12.0.0
+  __TEXT.__text: 0x391e4
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0x44c0
-  __TEXT.__objc_methlist: 0x2708
-  __TEXT.__const: 0x150
-  __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__objc_methname: 0x5dbb
-  __TEXT.__cstring: 0x8cd9
-  __TEXT.__objc_classname: 0x7e5
-  __TEXT.__objc_methtype: 0x1b15
-  __TEXT.__gcc_except_tab: 0x6d4
+  __TEXT.__delay_helper: 0x220
+  __TEXT.__objc_stubs: 0x45a0
+  __TEXT.__objc_methlist: 0x2858
+  __TEXT.__const: 0x140
+  __TEXT.__objc_methname: 0x6067
+  __TEXT.__cstring: 0x8f08
+  __TEXT.__objc_classname: 0x825
+  __TEXT.__objc_methtype: 0x1d96
+  __TEXT.__gcc_except_tab: 0x710
   __TEXT.__oslogstring: 0xac4
-  __TEXT.__unwind_info: 0xad0
+  __TEXT.__unwind_info: 0xae0
   __DATA_CONST.__auth_got: 0x588
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0xf08
-  __DATA_CONST.__cfstring: 0x5720
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0xe90
+  __DATA_CONST.__cfstring: 0x5900
+  __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_intobj: 0x1e0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x5d38
-  __DATA.__objc_selrefs: 0x1728
-  __DATA.__objc_ivar: 0x4a4
-  __DATA.__objc_data: 0x1270
-  __DATA.__data: 0xa20
-  __DATA.__bss: 0xc0
+  __DATA.__objc_const: 0x6158
+  __DATA.__objc_selrefs: 0x1778
+  __DATA.__objc_ivar: 0x4d0
+  __DATA.__objc_data: 0x1360
+  __DATA.__data: 0xa28
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred
+  - /System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DF61D495-E650-378E-AD26-275B87D5E227
-  Functions: 934
-  Symbols:   282
-  CStrings:  3214
+  UUID: BCFA9134-939E-34AA-88C3-6EEA6EC88E6C
+  Functions: 952
+  Symbols:   288
+  CStrings:  3274
 
Symbols:
+ _OBJC_CLASS_$_CIDCSessionCryptarch
+ _OBJC_CLASS_$_DCPresentmentRequest
+ _OBJC_CLASS_$_DCPresentmentSelection
+ _OBJC_CLASS_$_DCPresentmentSession
+ _OBJC_CLASS_$_DCPresentmentSessionOptions
+ _OBJC_CLASS_$_STSReaderCryptarch
+ __os_feature_enabled_impl
+ _dlopen
+ _objc_retain_x6
- __sl_dlopen
- _abort_report_np
- _objc_getClass
CStrings:
+ "-[STSXPClientNotification connectionEstablishedWithSTSReaderCryptarch:sessionTranscript:]_block_invoke"
+ "/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred"
+ "/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder"
+ "1.1"
+ "<%@ isHandoverSessionEstablishmentSupported=%@ isReaderAuthAllSupported=%@>"
+ "<Version=%@, COSEKey=%@, CipherSuites=%@, OriginInfos=%@ Capabilities=%@ Proprietary=%@, DeviceRetrievalMethods=%@>"
+ "@\"ISODeviceEngagementCapabilities\""
+ "@40@0:8Q16Q24@32"
+ "CoreIDV"
+ "Device engagement major version supported. Version %@. Proceeding further"
+ "Device engagement version nil"
+ "ISO18013_5SecondEditionSupport"
+ "ISODeviceEngagementCapabilities"
+ "ISODeviceEngagementCapabilitiesHandoverSessionEstablishmentSupported"
+ "ISODeviceEngagementCapabilitiesReaderAuthAllSupported"
+ "ISOOriginInfo"
+ "Invalid OriginInfo"
+ "STSReaderCryptarch"
+ "T@\"NSData\",R,N,V_privateKey"
+ "TQ,R,N,V_curve"
+ "TQ,R,N,V_variant"
+ "Vv32@0:8@\"STSReaderCryptarch\"16@\"NSData\"24"
+ "_capabilities"
+ "_category"
+ "_curve"
+ "_curve=%lu, _variant=%lu, _privateKey=%@"
+ "_details"
+ "_handoverSessionEstablishmentSupported"
+ "_originInfos"
+ "_privateKey"
+ "_readerAuthAllSupported"
+ "_readerCryptor"
+ "_variant"
+ "capabilities"
+ "cat"
+ "connectionEstablishedWithSTSReaderCryptarch:sessionTranscriptBytes:"
+ "curve"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "details"
+ "initWithCurve:variant:privateKey:"
+ "longLongValue"
+ "not implemented"
+ "originInfos"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "setWithArray:"
+ "v48@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40"
+ "v52@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44"
+ "v52@0:8@16@24I32@36@44"
+ "v56@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40Q48"
+ "v56@0:8@16@24@32@40Q48"
+ "v60@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44Q52"
+ "v60@0:8@16@24I32@36@44Q52"
+ "variant"
- "-[STSXPClientNotification sessionTranscriptGenerated:]_block_invoke"
- "<COSEKey=%@, CipherSuites=%@, Proprietary=%@, DeviceRetrievalMethods=%@>"
- "CIDCSessionCryptarch"
- "DCPresentmentRequest"
- "DCPresentmentSelection"
- "DCPresentmentSession"
- "DCPresentmentSessionOptions"
- "Unable to find class %s"
- "Vv24@0:8@\"NSData\"16"
- "_readerCrptyor"
- "sessionTranscriptGenerated:"
- "softlink:r:path:/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred"
- "softlink:r:path:/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder"

```
