## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

-63.120.18.0.0
-  __TEXT.__text: 0x63a5c
-  __TEXT.__auth_stubs: 0x1150
-  __TEXT.__objc_stubs: 0x60e0
-  __TEXT.__objc_methlist: 0x2ee4
-  __TEXT.__cstring: 0x3399
-  __TEXT.__objc_methname: 0x62e8
-  __TEXT.__objc_classname: 0x4c4
-  __TEXT.__objc_methtype: 0x119c
-  __TEXT.__const: 0x24f1
-  __TEXT.__oslogstring: 0x5de9
-  __TEXT.__gcc_except_tab: 0x13e0
+63.120.33.0.0
+  __TEXT.__text: 0x68014
+  __TEXT.__auth_stubs: 0x1170
+  __TEXT.__objc_stubs: 0x6400
+  __TEXT.__objc_methlist: 0x3084
+  __TEXT.__cstring: 0x3708
+  __TEXT.__objc_methname: 0x666b
+  __TEXT.__objc_classname: 0x4f6
+  __TEXT.__objc_methtype: 0x1232
+  __TEXT.__const: 0x2a81
+  __TEXT.__oslogstring: 0x62b0
+  __TEXT.__gcc_except_tab: 0x1548
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x15c8
-  __DATA_CONST.__auth_got: 0x8b8
-  __DATA_CONST.__got: 0x328
+  __TEXT.__unwind_info: 0x16b0
+  __DATA_CONST.__auth_got: 0x8c8
+  __DATA_CONST.__got: 0x338
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x8a98
-  __DATA_CONST.__cfstring: 0x2b20
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__const: 0x9548
+  __DATA_CONST.__cfstring: 0x3100
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__objc_intobj: 0x16b0
+  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_intobj: 0x17b8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__objc_arraydata: 0x4b8
-  __DATA_CONST.__objc_arrayobj: 0x4f8
+  __DATA_CONST.__objc_arraydata: 0x4e8
+  __DATA_CONST.__objc_arrayobj: 0x540
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x73d0
-  __DATA.__objc_selrefs: 0x1c40
-  __DATA.__objc_ivar: 0x300
-  __DATA.__objc_data: 0xb90
-  __DATA.__data: 0x1aa0
+  __DATA.__objc_const: 0x7950
+  __DATA.__objc_selrefs: 0x1d10
+  __DATA.__objc_ivar: 0x324
+  __DATA.__objc_data: 0xbe0
+  __DATA.__data: 0x1b00
   __DATA.__bss: 0x110
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
+  - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2818
-  Symbols:   388
-  CStrings:  2617
+  Functions: 2925
+  Symbols:   391
+  CStrings:  2738
 
Symbols:
+ _OBJC_CLASS_$__TtC17MobileInBoxUpdate24MIBULoopbackServerClient
+ _SecKeyCreateSignature
+ _kSecKeyAlgorithmECDSASignatureDigestX962SHA256
+ _objc_retain_x26
- ___NSDictionary0__struct
CStrings:
+ "\v"
+ "\x13"
+ "\x151"
+ "\x1f\v"
+ "&"
+ "/tmp/su/assets"
+ "@\"NSData\"16@0:8"
+ "BatteryLevel"
+ "CBConnection does NOT support taking LTK!"
+ "CBConnection supports taking LTK!"
+ "CBServer does NOT support taking LTK!"
+ "CBServer supports taking LTK!"
+ "CertChainBlob"
+ "ChallengeBlob"
+ "ClientController"
+ "Closing Bluetooth session"
+ "Creating data signature using SU cert for blob: %{public}@"
+ "Creating data signature using SU cert..."
+ "CurrentOSVersion"
+ "Data signature created: %{public}@"
+ "DataCollector: cannot create summary report before data collector is stopped."
+ "DataCollector: failed to save stats: %@"
+ "DataCollector: failed to serialize stats: %@"
+ "DataCollector: failed to serialize summary: %@"
+ "DataCollector: generating summary report."
+ "DataCollector: unknown tag name: %@"
+ "DataCollector: will clear files generated."
+ "Device ID derived: %{public}@ use case: %{public}@ timestamp: %u"
+ "DisableNarrativeAuthentication"
+ "EnableRateAdapter"
+ "Failed challenge payload serialization; payload does not have %{public}@ key"
+ "Failed receiving asset over multicast"
+ "Failed to create signature on data"
+ "Failed to dervie Device IDs for BT advertisement: %{public}@"
+ "Failed to dervie Device IDs for BT connection: %{public}@"
+ "Failed to deserialize cert chain blob"
+ "Failed to deserialize challenge blob from command"
+ "Failed to deserialize challenge command"
+ "Failed to deserialize payload for Challenge command"
+ "Failed to deserialize signature blob"
+ "Failed to deserialize timestamp from command"
+ "Failed to destroy local file server: %{public}@"
+ "Failed to load SU certificate"
+ "Failed to load SU private key"
+ "Failed to load existing key events: expecting dictionary but %@ is found"
+ "Failed to load existing stats: %@"
+ "Failed to serialize challenge response"
+ "Failed to sign challenge data using SU cert"
+ "Failed to spawn local file server: %{public}@"
+ "Handling challenge command..."
+ "KeyEvents"
+ "Loaded link encryption key: %{public}@"
+ "Long Term Key cannot be nil"
+ "MIBUChallengeResponse"
+ "MIBUDataCollectorProtocol"
+ "No challenge blob provided."
+ "PandoraKeyServerURL"
+ "SSU"
+ "SSUAssembleUpdateEnd"
+ "SSUAssembleUpdateStart"
+ "SSUBluetoothEnd"
+ "SSUBluetoothInit"
+ "SSUBluetoothStart"
+ "SSUDownloadUpdateEnd"
+ "SSUDownloadUpdateStart"
+ "SSUNanDataPathEnd"
+ "SSUNanDataPathInit"
+ "SSUNanDataPathStart"
+ "SSUNanMulticastEnd"
+ "SSUNanMulticastError"
+ "SSUNanMulticastInit"
+ "SSUNanMulticastStart"
+ "SSUStart"
+ "SSUUpdateEnd"
+ "SSUUpdateInstall"
+ "SSUUpdatePrepare"
+ "SSUWiFiInfraConnEnd"
+ "SSUWiFiInfraConnInit"
+ "SSUWiFiInfraConnStart"
+ "SSUWillReboot"
+ "SignatureBlob"
+ "SkipDeviceIdentityVerification"
+ "StartTime"
+ "Stopping local file server..."
+ "T@\"NSData\",&,N,V_certChainBlob"
+ "T@\"NSData\",&,N,V_signatureBlob"
+ "T@\"NSDictionary\",&,N,V_updateSummary"
+ "TB,N,V_collectMetrics"
+ "TB,N,V_enableRateAdapter"
+ "TB,N,V_shouldCloseSession"
+ "Thermal"
+ "ThermalEnd"
+ "ThermalPeak"
+ "ThermalStart"
+ "Use Python script for loopback server!"
+ "UsePythonLoopbackServer"
+ "_certChainBlob"
+ "_collectMetrics"
+ "_collectingKeyEvents"
+ "_convertTagName:"
+ "_currentThermalSummary"
+ "_deserializeChallenge"
+ "_enableRateAdapter"
+ "_handleChallenge:"
+ "_loadLinkEncryptionKey"
+ "_loadStats"
+ "_saveStats"
+ "_serializeChallenge"
+ "_shouldCloseSession"
+ "_signatureBlob"
+ "_startCBServerWithLTK:"
+ "_startUpdate"
+ "_thermalEnd"
+ "_thermalHistory"
+ "_thermalPeak"
+ "_thermalStart"
+ "_updateSummary"
+ "_updateThermalSummary:withValue:"
+ "addKeyEvent:"
+ "certChainBlob"
+ "clientControllerDidFailReceiving:error:"
+ "clientControllerDidFinishAssembly:withStats:"
+ "clientControllerDidFinishReceive:withStats:"
+ "collectMetrics"
+ "createSignatureUsingSUCertForData:withCompletion:"
+ "didConnect"
+ "didDisconnect"
+ "disableNarrativeAuthentication"
+ "enableRateAdapter"
+ "hasPrefix:"
+ "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:"
+ "pandoraKeyServerURL"
+ "setCertChainBlob:"
+ "setCollectMetrics:"
+ "setEnableRateAdapter:"
+ "setShouldCloseSession:"
+ "setSignatureBlob:"
+ "setUpdateSummary:"
+ "setUseCase:"
+ "shouldCloseSession"
+ "signatureBlob"
+ "skipDeviceIdentityVerification"
+ "startServerWithWebPort:webRoot:waitTillDone:error:"
+ "startWithRspIRK:usingLTK:outError:"
+ "stopMulticast"
+ "stopServerAndReturnError:"
+ "substringFromIndex:"
+ "tempLTK"
+ "updateSummary"
+ "usePythonLoopbackServer"
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8@\"MIBUNWClientController\"16@\"NSDictionary\"24"
+ "v32@0:8@\"MIBUNWClientController\"16@\"NSError\"24"
+ "v32@0:8@\"NSString\"16@24"
- "\x051"
- "\x06"
- "\x0f\f"
- "%"
- "@\"NSTask\""
- "DataCollector: failed to save non-thermal data: %@"
- "DataCollector: failed to serialize key events: %@"
- "DataCollector: will clear data generated."
- "Device ID derived: %{public}@ for timestamp: %u"
- "Failed to deserialize timestamp from command APDU"
- "Failed to load existing key events: %@"
- "Failed to load existing key events: expecting array but %@ is found"
- "File Server Console: %{public}@"
- "ShippingUpdateStart"
- "T@\"NSData\",&,N,V_advertisementPayload"
- "T@\"NSTask\",&,N,V_serverTask"
- "_advertisementPayload"
- "_didReceivePipeOutput:"
- "_keyEventsSaved"
- "_loadKeyEvents"
- "_saveKeyEvents"
- "_serverTask"
- "_startCBServer"
- "advertisementPayload"
- "availableData"
- "clientControllerDidFinishAssembly:"
- "clientControllerDidFinishReceive:"
- "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:controllerDelegate:"
- "object"
- "serverTask"
- "setAdvertisementPayload:"
- "setServerTask:"
- "startWithAdv:error:"
- "waitForDataInBackgroundAndNotify"

```
