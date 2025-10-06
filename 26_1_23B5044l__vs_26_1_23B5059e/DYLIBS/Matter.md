## Matter

> `/System/Library/Frameworks/Matter.framework/Matter`

```diff

-264.0.0.0.0
-  __TEXT.__text: 0x77fd64
+265.2.1.0.0
+  __TEXT.__text: 0x78ab2c
   __TEXT.__auth_stubs: 0x1260
-  __TEXT.__objc_methlist: 0x520cc
-  __TEXT.__const: 0x60cc9
-  __TEXT.__gcc_except_tab: 0xad378
-  __TEXT.__cstring: 0x29fbd
-  __TEXT.__oslogstring: 0x18485
-  __TEXT.__unwind_info: 0x41058
-  __TEXT.__objc_classname: 0xe650
-  __TEXT.__objc_methname: 0xbbb35
-  __TEXT.__objc_methtype: 0x703d
-  __TEXT.__objc_stubs: 0x305c0
-  __DATA_CONST.__got: 0x1f50
-  __DATA_CONST.__const: 0x12298
-  __DATA_CONST.__objc_classlist: 0x2a50
-  __DATA_CONST.__objc_protolist: 0x90
+  __TEXT.__objc_methlist: 0x5249c
+  __TEXT.__const: 0x612b9
+  __TEXT.__gcc_except_tab: 0xade28
+  __TEXT.__cstring: 0x2a2cf
+  __TEXT.__oslogstring: 0x19979
+  __TEXT.__unwind_info: 0x41310
+  __TEXT.__objc_classname: 0xe72a
+  __TEXT.__objc_methname: 0xbc4a1
+  __TEXT.__objc_methtype: 0x73bd
+  __TEXT.__objc_stubs: 0x30b60
+  __DATA_CONST.__got: 0x1f58
+  __DATA_CONST.__const: 0x12348
+  __DATA_CONST.__objc_classlist: 0x2a60
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19178
+  __DATA_CONST.__objc_selrefs: 0x19300
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1d98
+  __DATA_CONST.__objc_superrefs: 0x1da0
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x948
-  __AUTH_CONST.__const: 0x1ab70
-  __AUTH_CONST.__cfstring: 0x14a60
-  __AUTH_CONST.__objc_const: 0x651d8
+  __AUTH_CONST.__const: 0x1b0d0
+  __AUTH_CONST.__cfstring: 0x14aa0
+  __AUTH_CONST.__objc_const: 0x65f50
   __AUTH_CONST.__objc_intobj: 0x5880
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1a720
+  __AUTH.__objc_data: 0x1a7c0
   __AUTH.__data: 0x1a0
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x100
-  __DATA.__objc_ivar: 0x36cc
-  __DATA.__data: 0x5e00
+  __DATA.__objc_ivar: 0x370c
+  __DATA.__data: 0x5f88
   __DATA.__bss: 0x4710
-  __DATA.__common: 0x470
+  __DATA.__common: 0x490
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__common: 0x6f8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3002499E-EF05-3268-9A02-B44C6096CCA1
-  Functions: 47733
-  Symbols:   3080
-  CStrings:  28274
+  UUID: 999D9960-B58B-3B49-AA5D-D3B9CED36AF1
+  Functions: 47908
+  Symbols:   3082
+  CStrings:  28472
 
Symbols:
+ _OBJC_CLASS_$_MTRCommissioningOperation
+ _OBJC_CLASS_$_MTRTLSCertificateManagementClusterClientCSRParams
+ _OBJC_CLASS_$_MTRTLSCertificateManagementClusterClientCSRResponseParams
+ _OBJC_METACLASS_$_MTRCommissioningOperation
+ _OBJC_METACLASS_$_MTRTLSCertificateManagementClusterClientCSRParams
+ _OBJC_METACLASS_$_MTRTLSCertificateManagementClusterClientCSRResponseParams
- _OBJC_CLASS_$_MTRTLSCertificateManagementClusterTLSClientCSRParams
- _OBJC_CLASS_$_MTRTLSCertificateManagementClusterTLSClientCSRResponseParams
- _OBJC_METACLASS_$_MTRTLSCertificateManagementClusterTLSClientCSRParams
- _OBJC_METACLASS_$_MTRTLSCertificateManagementClusterTLSClientCSRResponseParams
CStrings:
+ "!activeConnection.IsNull()"
+ "%@ Can't set up commissioning session with address/port: commissioning %@ in progress"
+ "%@ Can't set up commissioning session with discovered device: commissioning %@ in progress"
+ "%@ Cannot start commissioning because commissioning %@ already in progress"
+ "%@ Cannot start commissioning with a non-concrete controller: %@"
+ "%@ Device commissioning failed with controller %@ metrics %@"
+ "%@ DeviceControllerDelegate network scan for nodeID 0x%016llx complete"
+ "%@ DeviceControllerDelegate network scan for nodeID 0x%016llx failed: %s"
+ "%@ Has no commissioning parameters"
+ "%@ Invalid nil argument to initWithParameters"
+ "%@ Notifying commissioning complete manually because %@ is being canceled while waiting after PASE establishment"
+ "%@ Unable to change commissioningFlow of concatenated QR code"
+ "%@ Unable to change discoveryCapabilities of concatenated QR code"
+ "%@ Unable to change discriminator of concatenated QR code"
+ "%@ Unable to change hasShortDiscriminator of concatenated QR code"
+ "%@ Unable to change productID of concatenated QR code"
+ "%@ Unable to change serialNumber of concatenated QR code"
+ "%@ Unable to change setupPasscode of concatenated QR code"
+ "%@ Unable to change vendorID of concatenated QR code"
+ "%@ Unable to change version of concatenated QR code"
+ "%@ Unable to modify vendor elements of concatenated QR code"
+ "%@ attempt to continue commissioning after device attestation with controller %@ failed: %@"
+ "%@ attempt to continue commissioning with Thread credentials with controller %@ failed: %@"
+ "%@ attempt to continue commissioning with Wi-Fi credentials with controller %@ failed: %@"
+ "%@ attempt to start commissioning with controller %@ and parameters %@ failed: %@"
+ "%@ commissioning %@ has already stopped and been replaced by %@"
+ "%@ failed to start commissioning with controller %@"
+ "%@ starting commissioning with controller %@"
+ "%@ starting new commissioning %@"
+ "%@ stopping commissioning %@"
+ "%@ suspended: can't start commissioning %@"
+ "%@ trying to start commissioning %@ but current commissioning is %@"
+ "%s NFCBase for Darwin NFCCommissioningManagerImpl"
+ "%s%llx"
+ ", concatenated: %@>"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/app/ClusterStateCache.h"
+ "/Library/Caches/com.apple.xbs/Sources/CHIPFramework/connectedhomeip/src/darwin/Framework/CHIP/MTRCommissioningOperation.mm"
+ "<%@: ccdid:%@; clientCertificate:%@; intermediateCertificates:%@; >"
+ "<%@: ccdid:%@; csr:%@; nonceSignature:%@; >"
+ "<%@: nonce:%@; ccdid:%@; >"
+ "<MTRCommissioningParameters: %p, has ssid: %d, has thread dataset: %d>, accepted terms: %@, accepted terms version: %@>"
+ "@\"<MTRCommissioningDelegate>\""
+ "@\"MTRCommissioningOperation\""
+ "@\"MTRCommissioningParameters\""
+ "@60@0:8@16@24@32B40@44@52"
+ "B40@0:8@16^v24^@32"
+ "Cannot send to NFC tag %u since reader transport is not valid"
+ "Clearing"
+ "ClientCSR"
+ "ClientCSRResponse"
+ "Commissionable node discovery over NFC failed, err = %s"
+ "Commissionable node discovery over NFC failed: %s"
+ "Commissionable node discovery over NFC since there is no valid NFC reader transport"
+ "Completed unpowered commissioning phase, marking commissioning as complete"
+ "Continuing commissioning after connect to network complete for device ID 0x%08X%08X"
+ "Couldn't get %s from storage: %s"
+ "Discovered device to be commissioned over NFC, Identifier: %u"
+ "Error, Long discriminator is required"
+ "EvictPreviousCaseSessions"
+ "Failed to Generate NOC: %s"
+ "Failed to SendMessage to NFC tag %u, due to error: %u"
+ "Failed to start commissionable node discovery over NFC: %s"
+ "Failed to stop commissionable node discovery over NFC since there is no valid NFC reader transport"
+ "Failure while trying to update network credentials during commissioning"
+ "FindOperationalForCommissioningComplete"
+ "FindOperationalForStayActive"
+ "Generated maximized certificate with %u DER bytes, %u TLV bytes"
+ "Generating ICAC"
+ "Generating NOC"
+ "Generating RCAC"
+ "Ignoring failure to read IsCommissioningWithoutPower: %s"
+ "Initializing Darwin NFC Commissioning Manager"
+ "Invalid state in NFCBase::CanSendToPeer()"
+ "MTRCommissioningDelegate"
+ "MTRCommissioningDelegate_Internal"
+ "MTRCommissioningOperation"
+ "MTRCommissioningOperation deallocated while waiting to continue after Thread network scan"
+ "MTRCommissioningOperation deallocated while waiting to continue after Wi-Fi network scan"
+ "MTRCommissioningOperation deallocated while waiting to continue after device attestation"
+ "MTRCommissioningOperationDeviceAttestationDelegate"
+ "MTRDeviceAttestationDelegate"
+ "MTRDeviceControllerDelegate_Internal"
+ "MTRTLSCertificateManagementClusterClientCSRParams"
+ "MTRTLSCertificateManagementClusterClientCSRResponseParams"
+ "MovementState"
+ "NFC commissioning does not support concatenated QR codes yet."
+ "NFC-based Commissioning Manager initialization failed: %s"
+ "NFCBase::Init"
+ "NFCBase::OnNfcTagError"
+ "NFCBase::OnNfcTagResponse"
+ "NFCCommissioningMgr shutdown"
+ "Parsing setup payload succeeded but resulted in no payloads"
+ "Providing certificate chain to the commissioner"
+ "Received failure response sending message to NFC tag %u, error: %u"
+ "Scan failed for unknown network type: %lu"
+ "Scan succeeded but for unknown network type: %lu"
+ "Sending message of length %lu bytes to NFC tag %u"
+ "Setting"
+ "Setting Darwin NFC Commissioning Reader Transport"
+ "Setup payload parsing succeeded but somehow did not create any payloads we can get a VID/PID from"
+ "Shutting down Darwin NFC Commissioning Manager and clearing reader transport"
+ "Sigma1 failed to peer %s: %s"
+ "Skipping commissionable node discovery over NFC since not supported by the controller!"
+ "Starting commissionable node discovery over NFC"
+ "Stopping commissionable node discovery over NFC by removing delegate"
+ "Stopping discovery of all NFC tags"
+ "Successfully sent message to NFC tag %u, received response buffer of length %lu bytes"
+ "T@\"MTRCommissioningOperation\",&,V_currentInternalCommissioning"
+ "T@\"MTRCommissioningOperation\",W,N,V_commissioningOperation"
+ "T@\"MTRCommissioningOperation\",W,V_currentCommissioning"
+ "T@\"NSData\",C,N,V_nonceSignature"
+ "T@\"NSString\",R,C,N,V_setupPayload"
+ "TB,N,V_isWaitingAfterPASEEstablished"
+ "TB,N,V_preventNetworkScans"
+ "TB,R,N,V_isInternallyCreated"
+ "TCP Connection established with peer %s, but no registered handler."
+ "T^v,R,N,V_deviceControllerDelegateBridge"
+ "Trying to cancelCommissioningForNodeID 0x%016llX (%@) when using MTRCommissioningOperation; call ignored"
+ "Trying to commissionNodeWithID: when using MTRCommissioningOperation; call ignored"
+ "Trying to continueCommissioningDevice: when using MTRCommissioningOperation; call ignored"
+ "Unable to generate a commissioning identifier: %s"
+ "Unable to handle ScanNetworks failure: missing required data: %@ %@ %@"
+ "Unable to handle ScanNetworks success: missing required data: %@ %@ %@"
+ "Unable to parse setup payload to extract VID/PID"
+ "Unable to send message to NFC tag %u since transport is not valid"
+ "Unauthenticated data received over %p for wrong connection %p. Dropping it!"
+ "Unicast data received over %p for wrong connection %p. Dropping it!"
+ "UnpoweredPhaseComplete"
+ "Verifying Certificate Signing Request"
+ "_cancelCommissioning:forNodeID:error:"
+ "_commissionNodeWithID:commissioningParams:error:"
+ "_commissioningDone:"
+ "_commissioningID"
+ "_commissioningOperation"
+ "_commissioningQueue"
+ "_concatenatedQRCode"
+ "_continueCommissioningDevice:ignoreAttestationFailure:error:"
+ "_currentCommissioning"
+ "_currentInternalCommissioning"
+ "_delegateQueue"
+ "_dispatchCommissioningCHIPError:"
+ "_dispatchCommissioningError:"
+ "_dispatchCommissioningError:forCommissioningID:withMetrics:"
+ "_dispatchCommissioningError:withMetrics:"
+ "_earlyFailCommissioning:"
+ "_internalDelegate"
+ "_isInternallyCreated"
+ "_isWaitingAfterPASEEstablished"
+ "_nonceSignature"
+ "_parameters"
+ "_preventNetworkScans"
+ "_setupPayload"
+ "activeConnection->GetReferenceCount() == 0"
+ "clientCSRWithParams:completion:"
+ "clientCSRWithParams:expectedValues:expectedValueInterval:completion:"
+ "commission:withCommissioningID:commissioningParams:error:"
+ "commissioning:completedDeviceAttestation:error:completion:"
+ "commissioning:failedWithError:forDeviceID:metrics:"
+ "commissioning:failedWithError:metrics:"
+ "commissioning:needsThreadNetworkSelectionWithScanResults:error:completion:"
+ "commissioning:needsWiFiNetworkSelectionWithScanResults:error:completion:"
+ "commissioning:paseSessionEstablishmentComplete:"
+ "commissioning:paseSessionEstablishmentComplete: notification for %@ but current commissioning is %@"
+ "commissioning:provisionedNetworkCredentialsForDeviceID:"
+ "commissioning:reachedCommissioningStage:"
+ "commissioning:readCommissioneeInfo:"
+ "commissioning:statusUpdate:"
+ "commissioning:statusUpdate: notification for %@ but current commissioning is %@"
+ "commissioning:succeededForNodeID: notification for %@ but current commissioning is %@"
+ "commissioning:succeededForNodeID:metrics:"
+ "commissioningDone:"
+ "commissioningOperation"
+ "commissioningProvisionedNetworkCredentials: notification for %@ but current commissioning is %@"
+ "continueCommissioning:withOperationalDataset:error:"
+ "continueCommissioning:withWiFiSSID:credentials:error:"
+ "continueCommissioningAfterAttestation:forOpaqueHandle:error:"
+ "continueCommissioningAfterConnectNetworkRequest"
+ "controller:scannedThreadNetworks:error:"
+ "controller:scannedWiFiNetworks:error:"
+ "core_commissioning_stage_unpowered_phase"
+ "currentCommissioning"
+ "currentInternalCommissioning"
+ "initWithParameters:setupPayload:commissioningID:isInternallyCreated:delegate:queue:"
+ "initWithParameters:setupPayload:delegate:queue:"
+ "isInternallyCreated"
+ "isWaitingAfterPASEEstablished"
+ "nonceSignature"
+ "org.csa-iot.matter.framework.commissioning.workqueue"
+ "preventNetworkScans"
+ "readAttributeMovementStateWithClusterStateCache:endpoint:queue:completion:"
+ "readAttributeMovementStateWithCompletion:"
+ "readAttributeMovementStateWithParams:"
+ "readCommissioneeInfo: notification for %@ but current commissioning is %@"
+ "setCommissioningOperation:"
+ "setCurrentCommissioning:"
+ "setCurrentInternalCommissioning:"
+ "setIsWaitingAfterPASEEstablished:"
+ "setNonceSignature:"
+ "setPreventNetworkScans:"
+ "setupPayload"
+ "src/controller/ExampleOperationalCredentialsIssuer.cpp"
+ "src/controller/OperationalCredentialsDelegate.h"
+ "src/platform/Darwin/NFCCommissioningManagerImpl.cpp"
+ "src/transport/raw/NFC.cpp"
+ "startCommissioning:withCommissioningID:"
+ "startWithController:"
+ "stopCommissioning:forCommissioningID:"
+ "subscribeAttributeMovementStateWithParams:subscriptionEstablished:reportHandler:"
+ "v16@?0@\"NSData\"8"
+ "v24@?0@\"NSData\"8@\"NSData\"16"
+ "v32@0:8@\"MTRCommissioningOperation\"16@\"MTRCommissioneeInfo\"24"
+ "v32@0:8@\"MTRCommissioningOperation\"16@\"NSError\"24"
+ "v32@0:8@\"MTRCommissioningOperation\"16@\"NSNumber\"24"
+ "v32@0:8@\"MTRCommissioningOperation\"16q24"
+ "v40@0:8@\"MTRCommissioningOperation\"16@\"NSError\"24@\"MTRMetrics\"32"
+ "v40@0:8@\"MTRCommissioningOperation\"16@\"NSNumber\"24@\"MTRMetrics\"32"
+ "v40@0:8@\"MTRDeviceController\"16@\"NSArray\"24@\"NSError\"32"
+ "v40@0:8@\"MTRDeviceController\"16^v24@\"NSError\"32"
+ "v40@0:8@16^v24@32"
+ "v48@0:8@\"MTRCommissioningOperation\"16@\"MTRDeviceAttestationDeviceInfo\"24@\"NSError\"32@?<v@?>40"
+ "v48@0:8@\"MTRCommissioningOperation\"16@\"NSArray\"24@\"NSError\"32@?<v@?@\"NSData\">40"
+ "v48@0:8@\"MTRCommissioningOperation\"16@\"NSArray\"24@\"NSError\"32@?<v@?@\"NSData\"@\"NSData\">40"
+ "v48@0:8@\"MTRCommissioningOperation\"16@\"NSError\"24@\"NSNumber\"32@\"MTRMetrics\"40"
+ "v48@0:8@\"MTRDeviceController\"16^v24@\"MTRDeviceAttestationDeviceInfo\"32@\"NSError\"40"
+ "v48@0:8@16^v24@32@40"
+ "{ChipError=II*}32@0:8@16@24"
+ "\x92"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa1"
- "<%@: ccdid:%@; clientCertificateDetails:%@; >"
- "<%@: ccdid:%@; csr:%@; nonce:%@; >"
- "<%@: nonce:%@; >"
- "<MTRCommissioningParameters: %p, has ssid: %d, has thread dataset: %d>, accepted terms: %@, accepted terms version: %@"
- ">"
- "@\"MTRTLSCertificateManagementClusterTLSClientCertificateDetailStruct\""
- "Data received over wrong connection %p. Dropping it!"
- "Disconnecting TCP connection from peer at %s."
- "Failed to Disconnect. Passed in Connection is null."
- "MTRTLSCertificateManagementClusterTLSClientCSRParams"
- "MTRTLSCertificateManagementClusterTLSClientCSRResponseParams"
- "T@\"MTRTLSCertificateManagementClusterTLSClientCertificateDetailStruct\",C,N,V_clientCertificateDetails"
- "TCP Connection established with peer %s, but no registered handler. Disconnecting."
- "TLSClientCSR"
- "TLSClientCSRResponse"
- "TLSClientCSRWithParams:completion:"
- "TLSClientCSRWithParams:expectedValues:expectedValueInterval:completion:"
- "T^{MTRDeviceControllerDelegateBridge=^^?@@@Q@},R,N,V_deviceControllerDelegateBridge"
- "Unable to get cluster info for Endpoint 0x%x, Cluster 0x%04X_%04X"
- "Write Version mismatch for Endpoint 0x%x, Cluster 0x%04X_%04X"
- "^{MTRDeviceControllerDelegateBridge=^^?@@@Q@}"
- "^{MTRDeviceControllerDelegateBridge=^^?@@@Q@}16@0:8"
- "_clientCertificateDetails"
- "activeConnection != nullptr"
- "clientCertificateDetails"
- "conn->mAppState != nullptr"
- "kEvictPreviousCaseSessions"
- "kFindOperationalForCommissioningComplete"
- "kFindOperationalForStayActive"
- "setClientCertificateDetails:"
- "\x91"
- "\xf0\xf0\xf0\xf0\xf0A\xf0\xf0\xf0\xf0\xf0\xb1\xd9q"

```
