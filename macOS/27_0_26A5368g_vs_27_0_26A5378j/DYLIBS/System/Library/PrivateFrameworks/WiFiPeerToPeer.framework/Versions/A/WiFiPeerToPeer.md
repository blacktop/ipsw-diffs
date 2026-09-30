## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer`

```diff

-  __TEXT.__text: 0x40e28
-  __TEXT.__objc_methlist: 0x5494
-  __TEXT.__const: 0x250
-  __TEXT.__oslogstring: 0x1332
+  __TEXT.__text: 0x42e68
+  __TEXT.__objc_methlist: 0x54a4
+  __TEXT.__const: 0x280
+  __TEXT.__oslogstring: 0x1bf5
   __TEXT.__swift5_typeref: 0x8c
-  __TEXT.__cstring: 0x869c
+  __TEXT.__cstring: 0x9780
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_reflstr: 0x7
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
   __TEXT.__gcc_except_tab: 0x2f0
-  __TEXT.__unwind_info: 0xf18
+  __TEXT.__unwind_info: 0xf20
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
   __AUTH_CONST.__const: 0x1528
   __AUTH_CONST.__cfstring: 0x6a80
-  __AUTH_CONST.__objc_const: 0x9b20
+  __AUTH_CONST.__objc_const: 0x9b88
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x450
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
   Functions: 1750
-  Symbols:   4238
-  CStrings:  1922
+  Symbols:   4241
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
+ OBJC_IVAR_$_WiFiAwareDataSession._logger
+ OBJC_IVAR_$_WiFiAwarePublisher._logger
+ OBJC_IVAR_$_WiFiAwareSubscriber._logger
Functions:
~ -[WiFiAwareDataSession initWithDiscoveryResult:serviceType:serviceSpecificInfo:passphrase:pmk:pmkID:] : 596 -> 724
~ -[WiFiAwareDataSession handleError:] : 128 -> 228
~ -[WiFiAwareDataSession startConnectionUsingProxy:completionHandler:] : 556 -> 632
~ -[WiFiAwareDataSession start] : 8 -> 140
~ -[WiFiAwareDataSession stop] : 16 -> 260
~ -[WiFiAwareDataSession reportIssue:] : 160 -> 276
~ -[WiFiAwareDataSession updateLinkStatus:] : 112 -> 240
~ -[WiFiAwareDataSession generateStatisticsReportWithCompletionHandler:] : 256 -> 356
~ -[WiFiAwareDataSession generateCurrentNetworkRecordForInternetSharingSession:] : 256 -> 356
~ -[WiFiAwareDataSession setWantsPeerRSSIUpdates:withCompletionHandler:] : 112 -> 264
~ -[WiFiAwareDataSession generateDiversifiedPINWithCompletionHandler:] : 328 -> 428
~ -[WiFiAwareDataSession datapathStartedWithInstanceID:initiatorDataAddress:localInterfaceIndex:] : 192 -> 288
~ -[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:] : 136 -> 232
~ -[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:] : 200 -> 316
~ -[WiFiAwareDataSession datapathReceivedControlDataAddress:serviceSpecificInfo:onInterfaceIndex:] : 172 -> 280
~ -[WiFiAwareDataSession datapathUpdatedInternetSharingPolicy:] : 8 -> 160
~ -[WiFiAwareDataSession datapathPairingDidSucceedWithPairingKeyStoreID:deviceID:] : 228 -> 224
~ -[WiFiAwareDataSession datapathFailedToStartWithError:] : 104 -> 208
~ -[WiFiAwareDataSession datapathTerminatedWithReason:] : 104 -> 208
~ -[WiFiAwareDataSession .cxx_destruct] : 216 -> 228
~ -[WiFiAwareSubscriber initWithConfiguration:] : 260 -> 388
~ -[WiFiAwareSubscriber handleError:] : 132 -> 232
~ -[WiFiAwareSubscriber startConnectionUsingProxy:completionHandler:] : 136 -> 224
~ -[WiFiAwareSubscriber start] : 8 -> 140
~ -[WiFiAwareSubscriber stop] : 16 -> 260
~ -[WiFiAwareSubscriber sendMessage:toPeerAddress:withInstanceID:completionHandler:] : 236 -> 416
~ -[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:] : 12 -> 268
~ -[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:] : 244 -> 440
~ -[WiFiAwareSubscriber updateTimeout:completionHandler:] : 112 -> 264
~ -[WiFiAwareSubscriber subscribeStartedWithInstanceID:] : 128 -> 232
~ -[WiFiAwareSubscriber subscribeLostDiscoveryResultForPublishID:address:] : 116 -> 224
~ -[WiFiAwareSubscriber subscribeReceivedDiscoveryResult:] : 324 -> 428
~ -[WiFiAwareSubscriber subscribeDetectedMulticastError:fromMulticastSender:] : 116 -> 224
~ -[WiFiAwareSubscriber subscribeReceivedDataBlobForMulticastSession:fromPeer:] : 136 -> 272
~ -[WiFiAwareSubscriber subscribeTerminatedWithReason:] : 112 -> 212
~ -[WiFiAwareSubscriber subscribeFailedToStartWithError:] : 112 -> 212
~ -[WiFiAwareSubscriber subscribeReceivedMessage:fromPublishID:address:] : 172 -> 324
~ -[WiFiAwareSubscriber .cxx_destruct] : 88 -> 100
~ -[WiFiAwarePublisher initWithConfiguration:] : 328 -> 456
~ -[WiFiAwarePublisher handleError:] : 132 -> 232
~ -[WiFiAwarePublisher startConnectionUsingProxy:completionHandler:] : 388 -> 480
~ -[WiFiAwarePublisher start] : 8 -> 140
~ -[WiFiAwarePublisher stop] : 16 -> 260
~ -[WiFiAwarePublisher sendMessage:toPeerAddress:withInstanceID:completionHandler:] : 236 -> 416
~ -[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:] : 12 -> 268
~ -[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:] : 236 -> 436
~ -[WiFiAwarePublisher terminateDataSession:completionHandler:] : 176 -> 304
~ -[WiFiAwarePublisher terminateMulticastSession:completionHandler:] : 176 -> 304
~ -[WiFiAwarePublisher updateServiceSpecificInfo:completionHandler:] : 216 -> 328
~ -[WiFiAwarePublisher updateDatapathServiceSpecificInfo:completionHandler:] : 216 -> 328
~ -[WiFiAwarePublisher updateTimeout:completionHandler:] : 112 -> 264
~ -[WiFiAwarePublisher reportIssue:forDataSession:] : 212 -> 328
~ -[WiFiAwarePublisher updateLinkStatus:forDataSession:] : 164 -> 292
~ -[WiFiAwarePublisher generateStatisticsReportForDataSession:completionHandler:] : 308 -> 408
~ -[WiFiAwarePublisher generateDiversifiedPINForDataSession:completionHandler:] : 380 -> 480
~ -[WiFiAwarePublisher publishStartedWithInstanceID:maximumNANDataPath:] : 176 -> 284
~ -[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:] : 184 -> 292
~ -[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:] : 212 -> 328
~ -[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:] : 228 -> 356
~ -[WiFiAwarePublisher publishDataTerminatedForHandle:reason:] : 148 -> 256
~ -[WiFiAwarePublisher publishFailedToStartWithError:] : 112 -> 212
~ -[WiFiAwarePublisher publishReceivedMessage:fromSubscriberID:subscriberAddress:] : 172 -> 320
~ -[WiFiAwarePublisher publishDetectedMulticastError:fromMulticastReceiver:] : 116 -> 224
~ -[WiFiAwarePublisher publishReceivedDataBlobForMulticastSession:fromPeer:] : 136 -> 272
~ -[WiFiAwarePublisher publishReceivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:] : 112 -> 232
~ -[WiFiAwarePublisher publishKeysBlobForMulticastSession:] : 180 -> 176
~ -[WiFiAwarePublisher publishTerminatedWithReason:] : 112 -> 212
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
