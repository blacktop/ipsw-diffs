## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-  __TEXT.__text: 0x3d44c
-  __TEXT.__objc_methlist: 0x5494
-  __TEXT.__const: 0x250
-  __TEXT.__oslogstring: 0x1332
+  __TEXT.__text: 0x3f2ec
+  __TEXT.__objc_methlist: 0x54a4
+  __TEXT.__const: 0x270
+  __TEXT.__oslogstring: 0x1bf5
   __TEXT.__swift5_typeref: 0x8c
-  __TEXT.__cstring: 0x869c
+  __TEXT.__cstring: 0x9780
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_reflstr: 0x7
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
   __TEXT.__gcc_except_tab: 0x2f0
-  __TEXT.__unwind_info: 0xf48
+  __TEXT.__unwind_info: 0xf60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2230
+  __DATA_CONST.__objc_selrefs: 0x2238
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__got: 0x328
   __AUTH_CONST.__const: 0x4a8
   __AUTH_CONST.__cfstring: 0x6a80
-  __AUTH_CONST.__objc_const: 0x9b20
+  __AUTH_CONST.__objc_const: 0x9b88
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x560
-  __AUTH.__objc_data: 0x98
-  __DATA.__objc_ivar: 0x718
+  __AUTH.__objc_data: 0x48
+  __DATA.__objc_ivar: 0x724
   __DATA.__data: 0xc80
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x17f8
+  __DATA_DIRTY.__objc_data: 0x1848
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x70

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 1722
-  Symbols:   5904
-  CStrings:  1922
+  Symbols:   5907
+  CStrings:  2023
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _OBJC_IVAR_$_WiFiAwareDataSession._logger
+ _OBJC_IVAR_$_WiFiAwarePublisher._logger
+ _OBJC_IVAR_$_WiFiAwareSubscriber._logger
Functions:
~ -[WiFiAwareDataSession initWithDiscoveryResult:serviceType:serviceSpecificInfo:passphrase:pmk:pmkID:] : 512 -> 636
~ -[WiFiAwareDataSession handleError:] : 116 -> 224
~ -[WiFiAwareDataSession startConnectionUsingProxy:completionHandler:] : 508 -> 584
~ -[WiFiAwareDataSession start] : 8 -> 140
~ -[WiFiAwareDataSession stop] : 16 -> 260
~ -[WiFiAwareDataSession reportIssue:] : 152 -> 264
~ -[WiFiAwareDataSession updateLinkStatus:] : 112 -> 240
~ -[WiFiAwareDataSession generateStatisticsReportWithCompletionHandler:] : 244 -> 344
~ -[WiFiAwareDataSession generateCurrentNetworkRecordForInternetSharingSession:] : 244 -> 344
~ -[WiFiAwareDataSession setWantsPeerRSSIUpdates:withCompletionHandler:] : 112 -> 256
~ -[WiFiAwareDataSession generateDiversifiedPINWithCompletionHandler:] : 316 -> 416
~ -[WiFiAwareDataSession datapathStartedWithInstanceID:initiatorDataAddress:localInterfaceIndex:] : 196 -> 276
~ -[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:] : 128 -> 212
~ -[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:] : 184 -> 288
~ -[WiFiAwareDataSession datapathReceivedControlDataAddress:serviceSpecificInfo:onInterfaceIndex:] : 156 -> 260
~ -[WiFiAwareDataSession datapathUpdatedInternetSharingPolicy:] : 8 -> 160
~ -[WiFiAwareDataSession datapathPairingDidSucceedWithPairingKeyStoreID:deviceID:] : 216 -> 212
~ -[WiFiAwareDataSession datapathFailedToStartWithError:] : 100 -> 204
~ -[WiFiAwareDataSession datapathTerminatedWithReason:] : 100 -> 204
~ -[WiFiAwareDataSession .cxx_destruct] : 216 -> 228
~ -[WiFiAwareSubscriber initWithConfiguration:] : 240 -> 364
~ -[WiFiAwareSubscriber handleError:] : 120 -> 228
~ -[WiFiAwareSubscriber startConnectionUsingProxy:completionHandler:] : 128 -> 204
~ -[WiFiAwareSubscriber start] : 8 -> 140
~ -[WiFiAwareSubscriber stop] : 16 -> 260
~ -[WiFiAwareSubscriber sendMessage:toPeerAddress:withInstanceID:completionHandler:] : 216 -> 376
~ -[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:] : 12 -> 244
~ -[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:] : 224 -> 400
~ -[WiFiAwareSubscriber updateTimeout:completionHandler:] : 112 -> 256
~ -[WiFiAwareSubscriber subscribeStartedWithInstanceID:] : 136 -> 224
~ -[WiFiAwareSubscriber subscribeLostDiscoveryResultForPublishID:address:] : 116 -> 212
~ -[WiFiAwareSubscriber subscribeReceivedDiscoveryResult:] : 312 -> 416
~ -[WiFiAwareSubscriber subscribeDetectedMulticastError:fromMulticastSender:] : 116 -> 212
~ -[WiFiAwareSubscriber subscribeReceivedDataBlobForMulticastSession:fromPeer:] : 128 -> 244
~ -[WiFiAwareSubscriber subscribeTerminatedWithReason:] : 108 -> 208
~ -[WiFiAwareSubscriber subscribeFailedToStartWithError:] : 108 -> 208
~ -[WiFiAwareSubscriber subscribeReceivedMessage:fromPublishID:address:] : 156 -> 296
~ -[WiFiAwareSubscriber .cxx_destruct] : 88 -> 100
~ -[WiFiAwarePublisher initWithConfiguration:] : 296 -> 420
~ -[WiFiAwarePublisher handleError:] : 120 -> 228
~ -[WiFiAwarePublisher startConnectionUsingProxy:completionHandler:] : 360 -> 452
~ -[WiFiAwarePublisher start] : 8 -> 140
~ -[WiFiAwarePublisher stop] : 16 -> 260
~ -[WiFiAwarePublisher sendMessage:toPeerAddress:withInstanceID:completionHandler:] : 216 -> 376
~ -[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:] : 12 -> 244
~ -[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:] : 216 -> 396
~ -[WiFiAwarePublisher terminateDataSession:completionHandler:] : 168 -> 284
~ -[WiFiAwarePublisher terminateMulticastSession:completionHandler:] : 168 -> 284
~ -[WiFiAwarePublisher updateServiceSpecificInfo:completionHandler:] : 196 -> 300
~ -[WiFiAwarePublisher updateDatapathServiceSpecificInfo:completionHandler:] : 196 -> 300
~ -[WiFiAwarePublisher updateTimeout:completionHandler:] : 112 -> 256
~ -[WiFiAwarePublisher reportIssue:forDataSession:] : 192 -> 304
~ -[WiFiAwarePublisher updateLinkStatus:forDataSession:] : 156 -> 280
~ -[WiFiAwarePublisher generateStatisticsReportForDataSession:completionHandler:] : 284 -> 384
~ -[WiFiAwarePublisher generateDiversifiedPINForDataSession:completionHandler:] : 356 -> 456
~ -[WiFiAwarePublisher publishStartedWithInstanceID:maximumNANDataPath:] : 180 -> 272
~ -[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:] : 168 -> 272
~ -[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:] : 196 -> 300
~ -[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:] : 204 -> 328
~ -[WiFiAwarePublisher publishDataTerminatedForHandle:reason:] : 148 -> 244
~ -[WiFiAwarePublisher publishFailedToStartWithError:] : 108 -> 208
~ -[WiFiAwarePublisher publishReceivedMessage:fromSubscriberID:subscriberAddress:] : 156 -> 292
~ -[WiFiAwarePublisher publishDetectedMulticastError:fromMulticastReceiver:] : 116 -> 212
~ -[WiFiAwarePublisher publishReceivedDataBlobForMulticastSession:fromPeer:] : 128 -> 244
~ -[WiFiAwarePublisher publishReceivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:] : 112 -> 228
~ -[WiFiAwarePublisher publishKeysBlobForMulticastSession:] : 168 -> 164
~ -[WiFiAwarePublisher publishTerminatedWithReason:] : 108 -> 208
~ -[WiFiAwarePublisher .cxx_destruct] : 160 -> 172
CStrings:
+ "%{public}s: %{public}@"
+ "%{public}s: ccaIBSS=%u, ccaOBSS=%u, ccaNonWiFi=%u, %{public}@"
+ "%{public}s: discoveryResult=%{public}@, %{public}@"
+ "%{public}s: error=%ld, %{public}@"
+ "%{public}s: error=%ld, multicastReceiverAddress=%{public}@, %{public}@"
+ "%{public}s: error=%ld, multicastSenderAddress=%{public}@, %{public}@"
+ "%{public}s: handle=%{public}@, %{public}@"
+ "%{public}s: handle=%{public}@, localInterfaceIndex=%u, %{public}@"
+ "%{public}s: handle=%{public}@, localInterfaceIndex=%u, pairingKeyStoreID=%{public}@, %{public}@"
+ "%{public}s: handle=%{public}@, localInterfaceIndex=%u, pairingKeyStoreID=%{public}@, deviceID=%llu, %{public}@"
+ "%{public}s: handle=%{public}@, reason=%ld, %{public}@"
+ "%{public}s: instanceID=%d, %{public}@"
+ "%{public}s: instanceID=%d, initiatorDataAddress=%{public}@, localInterfaceIndex=%u, %{public}@"
+ "%{public}s: instanceID=%d, maximumNANDataPath=%u, %{public}@"
+ "%{public}s: linkStatus=%ld, %{public}@"
+ "%{public}s: linkStatus=%ld, handle=%{public}@, %{public}@"
+ "%{public}s: multicastReceiverAddress=%{public}@, %{public}@"
+ "%{public}s: newTimeout=%lu, %{public}@"
+ "%{public}s: no active datapath, skipping cancel, %{public}@"
+ "%{public}s: no active publish, skipping cancel, %{public}@"
+ "%{public}s: no active subscribe, skipping cancel, %{public}@"
+ "%{public}s: peer=%{public}@, dataLength=%lu, %{public}@"
+ "%{public}s: peerAddress=%{public}@, peerInstanceID=%d, messageLength=%lu, %{public}@"
+ "%{public}s: peerAddress=%{public}@, usingMulticastAddress=%d, %{public}@"
+ "%{public}s: peerAddress=%{public}@, usingMulticastAddress=%d, usingiGTK=%d, dataLength=%lu, %{public}@"
+ "%{public}s: peerControlDataAddress=%{public}@, onInterfaceIndex=%u, %{public}@"
+ "%{public}s: peerDataAddress=%{public}@, %{public}@"
+ "%{public}s: peerDataAddress=%{public}@, pairingKeyStoreID=%{public}@, deviceID=%llu, %{public}@"
+ "%{public}s: policy=%ld, %{public}@"
+ "%{public}s: publishID=%d, address=%{public}@, %{public}@"
+ "%{public}s: publishID=%d, address=%{public}@, messageLength=%lu, %{public}@"
+ "%{public}s: reason=%ld, %{public}@"
+ "%{public}s: report=%{public}@, %{public}@"
+ "%{public}s: report=%{public}@, handle=%{public}@, %{public}@"
+ "%{public}s: subscriberID=%d, subscriberAddress=%{public}@, messageLength=%lu, %{public}@"
+ "%{public}s: wantsUpdates=%d, %{public}@"
+ "-[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:]"
+ "-[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:]"
+ "-[WiFiAwareDataSession datapathFailedToStartWithError:]"
+ "-[WiFiAwareDataSession datapathReceivedControlDataAddress:serviceSpecificInfo:onInterfaceIndex:]"
+ "-[WiFiAwareDataSession datapathStartedWithInstanceID:initiatorDataAddress:localInterfaceIndex:]"
+ "-[WiFiAwareDataSession datapathTerminatedWithReason:]"
+ "-[WiFiAwareDataSession datapathUpdatedInternetSharingPolicy:]"
+ "-[WiFiAwareDataSession generateCurrentNetworkRecordForInternetSharingSession:]"
+ "-[WiFiAwareDataSession generateDiversifiedPINWithCompletionHandler:]"
+ "-[WiFiAwareDataSession generateStatisticsReportWithCompletionHandler:]"
+ "-[WiFiAwareDataSession handleError:]"
+ "-[WiFiAwareDataSession initWithDiscoveryResult:serviceType:serviceSpecificInfo:passphrase:pmk:pmkID:]"
+ "-[WiFiAwareDataSession reportIssue:]"
+ "-[WiFiAwareDataSession setWantsPeerRSSIUpdates:withCompletionHandler:]"
+ "-[WiFiAwareDataSession startConnectionUsingProxy:completionHandler:]"
+ "-[WiFiAwareDataSession start]"
+ "-[WiFiAwareDataSession stop]"
+ "-[WiFiAwareDataSession updateLinkStatus:]"
+ "-[WiFiAwarePublisher generateDiversifiedPINForDataSession:completionHandler:]"
+ "-[WiFiAwarePublisher generateStatisticsReportForDataSession:completionHandler:]"
+ "-[WiFiAwarePublisher handleError:]"
+ "-[WiFiAwarePublisher initWithConfiguration:]"
+ "-[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]"
+ "-[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:]"
+ "-[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:]"
+ "-[WiFiAwarePublisher publishDataTerminatedForHandle:reason:]"
+ "-[WiFiAwarePublisher publishDetectedMulticastError:fromMulticastReceiver:]"
+ "-[WiFiAwarePublisher publishFailedToStartWithError:]"
+ "-[WiFiAwarePublisher publishReceivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:]"
+ "-[WiFiAwarePublisher publishReceivedDataBlobForMulticastSession:fromPeer:]"
+ "-[WiFiAwarePublisher publishReceivedMessage:fromSubscriberID:subscriberAddress:]"
+ "-[WiFiAwarePublisher publishStartedWithInstanceID:maximumNANDataPath:]"
+ "-[WiFiAwarePublisher publishTerminatedWithReason:]"
+ "-[WiFiAwarePublisher reportIssue:forDataSession:]"
+ "-[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:]"
+ "-[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:]"
+ "-[WiFiAwarePublisher sendMessage:toPeerAddress:withInstanceID:completionHandler:]"
+ "-[WiFiAwarePublisher startConnectionUsingProxy:completionHandler:]"
+ "-[WiFiAwarePublisher start]"
+ "-[WiFiAwarePublisher stop]"
+ "-[WiFiAwarePublisher terminateDataSession:completionHandler:]"
+ "-[WiFiAwarePublisher terminateMulticastSession:completionHandler:]"
+ "-[WiFiAwarePublisher updateDatapathServiceSpecificInfo:completionHandler:]"
+ "-[WiFiAwarePublisher updateLinkStatus:forDataSession:]"
+ "-[WiFiAwarePublisher updateServiceSpecificInfo:completionHandler:]"
+ "-[WiFiAwarePublisher updateTimeout:completionHandler:]"
+ "-[WiFiAwareSubscriber handleError:]"
+ "-[WiFiAwareSubscriber initWithConfiguration:]"
+ "-[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:]"
+ "-[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:]"
+ "-[WiFiAwareSubscriber sendMessage:toPeerAddress:withInstanceID:completionHandler:]"
+ "-[WiFiAwareSubscriber startConnectionUsingProxy:completionHandler:]"
+ "-[WiFiAwareSubscriber start]"
+ "-[WiFiAwareSubscriber stop]"
+ "-[WiFiAwareSubscriber subscribeDetectedMulticastError:fromMulticastSender:]"
+ "-[WiFiAwareSubscriber subscribeFailedToStartWithError:]"
+ "-[WiFiAwareSubscriber subscribeLostDiscoveryResultForPublishID:address:]"
+ "-[WiFiAwareSubscriber subscribeReceivedDataBlobForMulticastSession:fromPeer:]"
+ "-[WiFiAwareSubscriber subscribeReceivedDiscoveryResult:]"
+ "-[WiFiAwareSubscriber subscribeReceivedMessage:fromPublishID:address:]"
+ "-[WiFiAwareSubscriber subscribeStartedWithInstanceID:]"
+ "-[WiFiAwareSubscriber subscribeTerminatedWithReason:]"
+ "-[WiFiAwareSubscriber updateTimeout:completionHandler:]"
+ "GCR: WiFiAwarePublisher.m: publishKeysBlobForMulticastSession - Received key blob from daemon: %{public}@"
+ "WiFiAwareDataSession"
+ "WiFiAwarePublisher"
+ "WiFiAwareSubscriber"
+ "datapathPairingDidSucceed PairingKeyStoreID: %{public}@ DeviceID: %llu"
+ "\xf1Q"
- "GCR: WiFiAwarePublisher.m: publishKeysBlobForMulticastSession - Received key blob from daemon: %@"
- "datapathPairingDidSucceed PairingKeyStoreID: %@ DeviceID: %llu"
- "q"
- "\xe1Q"

```
