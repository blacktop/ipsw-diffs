## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

```diff

-770.26.0.0.0
-  __TEXT.__text: 0x116030
-  __TEXT.__auth_stubs: 0x2f10
-  __TEXT.__objc_methlist: 0x9740
-  __TEXT.__cstring: 0x234ab
-  __TEXT.__const: 0x22d8
-  __TEXT.__gcc_except_tab: 0x1c68
-  __TEXT.__oslogstring: 0x563
-  __TEXT.__unwind_info: 0x38f8
+780.12.0.0.0
+  __TEXT.__text: 0x11a6dc
+  __TEXT.__auth_stubs: 0x3010
+  __TEXT.__objc_methlist: 0x9c18
+  __TEXT.__cstring: 0x227ba
+  __TEXT.__const: 0x22f8
+  __TEXT.__gcc_except_tab: 0x1d44
+  __TEXT.__oslogstring: 0xd69
+  __TEXT.__unwind_info: 0x3a10
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0xbe4
-  __TEXT.__objc_methname: 0x14ddb
-  __TEXT.__objc_methtype: 0x40eb
-  __TEXT.__objc_stubs: 0x9f00
-  __DATA_CONST.__got: 0x630
-  __DATA_CONST.__const: 0x29a0
-  __DATA_CONST.__objc_classlist: 0x308
+  __TEXT.__objc_classname: 0xcd0
+  __TEXT.__objc_methname: 0x157f9
+  __TEXT.__objc_methtype: 0x42ba
+  __TEXT.__objc_stubs: 0xa2a0
+  __DATA_CONST.__got: 0x660
+  __DATA_CONST.__const: 0x29c0
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a10
+  __DATA_CONST.__objc_selrefs: 0x4c10
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x208
-  __AUTH_CONST.__auth_got: 0x1798
+  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__objc_arraydata: 0x8
+  __AUTH_CONST.__auth_got: 0x1818
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x1f70
-  __AUTH_CONST.__cfstring: 0x4380
-  __AUTH_CONST.__objc_const: 0x13080
-  __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH.__objc_data: 0x1bd0
-  __AUTH.__data: 0xb08
-  __DATA.__objc_ivar: 0x14d0
-  __DATA.__data: 0x3240
-  __DATA.__bss: 0x10d0
+  __AUTH_CONST.__const: 0x1ff0
+  __AUTH_CONST.__cfstring: 0x4400
+  __AUTH_CONST.__objc_const: 0x13c08
+  __AUTH_CONST.__objc_intobj: 0x258
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x1f40
+  __AUTH.__data: 0xb18
+  __DATA.__objc_ivar: 0x1534
+  __DATA.__data: 0x31b0
+  __DATA.__bss: 0x1110
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x178

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5643
-  Symbols:   6767
-  CStrings:  9501
+  Functions: 5749
+  Symbols:   6908
+  CStrings:  9639
 
Symbols:
+ _CUPrintNSDataHexDump
+ _CUPrintTXTRecordNSData
+ _HTTPClientSetConnectionProgressHandler
+ _OBJC_CLASS_$_CUFile
+ _OBJC_CLASS_$_CUNANPairingPromptInfo
+ _OBJC_CLASS_$_CUNANPairingShowInfo
+ _OBJC_CLASS_$_CUSPAKEM1
+ _OBJC_CLASS_$_CUSPAKEM2
+ _OBJC_CLASS_$_CUSPAKEM3
+ _OBJC_CLASS_$_CUSPAKEProver
+ _OBJC_CLASS_$_CUSPAKEVerifier
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_METACLASS_$_CUFile
+ _OBJC_METACLASS_$_CUNANPairingPromptInfo
+ _OBJC_METACLASS_$_CUNANPairingShowInfo
+ _OBJC_METACLASS_$_CUSPAKEM1
+ _OBJC_METACLASS_$_CUSPAKEM2
+ _OBJC_METACLASS_$_CUSPAKEM3
+ _OBJC_METACLASS_$_CUSPAKEProver
+ _OBJC_METACLASS_$_CUSPAKEVerifier
+ _cc_clear
+ _ccscrypt
+ _ccscrypt_storage_size
+ _ccspake_cp_256_rfc
+ _ccspake_generate_L
+ _ccspake_kex_generate
+ _ccspake_kex_process
+ _ccspake_mac_compute
+ _ccspake_mac_hkdf_hmac_sha256
+ _ccspake_mac_verify_and_get_session_key
+ _ccspake_prover_initialize
+ _ccspake_reduce_w
+ _ccspake_sizeof_ctx
+ _ccspake_sizeof_point
+ _ccspake_sizeof_w
+ _ccspake_verifier_initialize
CStrings:
+ "\x01\x11(\""
+ "\x01\x12\x11"
+ "\x01\x12."
+ "\x01\xa2\x19"
+ "### SendMessage failed: %@"
+ "### SendMessage failed: EP %@, Data %@, %@"
+ "### WFA DataSession confirmed for existing session: %@"
+ "### WFA DataSession confirmed missing identifier"
+ "### WFA DataSession start failed: %@, %@"
+ "### WFA DataSession terminated missing identifier: %@"
+ "### WFA DataSession terminated untracked: '%@', %@, %@"
+ "### WFA discovery result missing identifier"
+ "### WFA lost result missing identifier"
+ "### WFAPublisher start failed: '%@', %@"
+ "### WFASubscriber start failed: '%@', %@"
+ "### tryPairingPassword with no input handler"
+ "%##{txt}"
+ "%.1H"
+ "%{txt}"
+ "(no handler)"
+ ", IP %@"
+ "@24@0:8r*16"
+ "@32@0:8r^v16Q24"
+ "@40@0:8@16Q24@32"
+ "Activate '%@', %@"
+ "Activate: endpoint=%@, controlFlags=%@, trafficFlags=%@, pair=%s"
+ "Activate: serviceType=%@, name='%@', port=%d, trafficFlags=%@, customData=%@, textInfo=%@, pair=%s"
+ "B48@0:8@16*24Q32^@40"
+ "CID 0x%08X"
+ "CUFile"
+ "CUFile closed"
+ "CUFile deleted"
+ "CUFileReadRequest"
+ "CUFileWriteRequest"
+ "CUNANPairingPromptInfo"
+ "CUNANPairingShowInfo"
+ "CUSPAKECommon"
+ "CUSPAKEM1"
+ "CUSPAKEM2"
+ "CUSPAKEM3"
+ "CUSPAKEProver"
+ "CUSPAKEVerifier"
+ "Create parent failed"
+ "DataSession ended: %@"
+ "DataSession started: %@"
+ "Endpoint changed: %@, %@"
+ "Endpoint found: %@"
+ "Endpoint lost: %@"
+ "F_NOCACHE failed"
+ "F_PREALLOCATE failed"
+ "F_RDAHEAD failed"
+ "F_SINGLE_WRITER failed"
+ "Get parent URL failed"
+ "No path"
+ "PairSetup-SPAKE2-Context"
+ "PairSetup-SPAKE2-ProverID"
+ "PairSetup-SPAKE2-Salt"
+ "PairSetup-SPAKE2-VerifierID"
+ "PairingPrompt: %@ %s"
+ "PairingShow: %@"
+ "SendMessage completed: EP %@, Data %@"
+ "SendMessage start: EP %@, Data %@"
+ "T@\"NSData\",C,N,V_confirmPData"
+ "T@\"NSData\",C,N,V_confirmVData"
+ "T@\"NSData\",C,N,V_sharePData"
+ "T@\"NSData\",C,N,V_shareVData"
+ "T@\"NSDictionary\",R,C,N,V_textInfo"
+ "T@\"NSString\",R,C,N,V_pinCode"
+ "T@?,C,N,V_pairingPromptHandler"
+ "T@?,C,N,V_pairingShowHandler"
+ "TB,N,V_wfaPairingCacheEnabled"
+ "TQ,N,V_length"
+ "TQ,N,V_offset"
+ "Tq,N,V_wfaPairingMethod"
+ "URLByDeletingLastPathComponent"
+ "WFA DataSession indicated: '%@', %@"
+ "WFA DataSession request started: %@"
+ "WFA DataSession terminate completed: %@"
+ "WFA DataSession terminate start"
+ "WFA DataSession terminated: %@, %@"
+ "WFA DataSession terminated: '%@', %@, %@"
+ "WFA discovery result: PA <%@>, PI %u, SV '%@', SI <%@>"
+ "WFA lost result missing not found: %@"
+ "WFA lost result: PA <%@>, PI %u"
+ "WFAPublisher restarting after unexpected termination"
+ "WFAPublisher started: '%@'"
+ "WFAPublisher terminated: '%@', %s"
+ "WFASubscriber restarting after unexpected termination"
+ "WFASubscriber started: '%@'"
+ "WFASubscriber terminated: '%@', %s"
+ "WiFiAwareDataSessionPairingDelegate"
+ "WiFiAwarePairingConfiguration"
+ "WiFiAwarePublishDatapathSecurityConfiguration"
+ "WiFiAwarePublisherPairingDelegate"
+ "^{ccspake_ctx=^{ccspake_cp}^{ccspake_mac}^{ccrng_state}BQ[20C]C[26{ccdigest_ctx=[1C]}][64C][0Q]}"
+ "_completeReadRequest:data:error:"
+ "_confirmPData"
+ "_confirmVData"
+ "_newZeroingDataWithBytes:length:"
+ "_openForReadingAndReturnError:"
+ "_openForWritingAndReturnError:"
+ "_pairingPromptHandler"
+ "_pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:"
+ "_pairingShowHandler"
+ "_passwordData"
+ "_pinCode"
+ "_pinCodeInputCompletionHandler"
+ "_processRead:"
+ "_processWrite:"
+ "_readQueue"
+ "_readRequest:"
+ "_sessionKey"
+ "_sharePData"
+ "_shareVData"
+ "_spakeContext"
+ "_totalLength"
+ "_url"
+ "_wfaPairingCacheEnabled"
+ "_wfaPairingMethod"
+ "_writeQueue"
+ "_writeRequest:"
+ "bad scrypt storage size: %lld bytes"
+ "ccscrypt failed: %d"
+ "ccspake verify failed: %d"
+ "ccspake_ctx malloc failed"
+ "ccspake_generate_L"
+ "ccspake_kex_generate failed: %d"
+ "ccspake_kex_process failed: %d"
+ "ccspake_mac_compute failed: %d"
+ "ccspake_prover_initialize failed: %d"
+ "ccspake_reduce_w failed w0: %d"
+ "ccspake_reduce_w failed w1: %d"
+ "closeWithCompletionHandler:"
+ "confirmP"
+ "confirmPData"
+ "confirmV"
+ "confirmVData"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dictionaryRepresentation"
+ "finishWithM3:error:"
+ "generate session key failed"
+ "generateM1AndReturnError:"
+ "generateM2WithM1:error:"
+ "generateM3WithM2:error:"
+ "get confirmP failed: %d"
+ "get confirmV failed: %d"
+ "get sharePData failed: %d"
+ "get shareV failed: %d"
+ "i24@0:8^@16"
+ "initForReadingFromURL:dispatchQueue:"
+ "initForWritingToURL:dispatchQueue:"
+ "initForWritingToURL:totalLength:dispatchQueue:"
+ "initWithDataSession:"
+ "initWithPairingConfiguration:usingPairingDelegate:"
+ "initWithPasswordCString:"
+ "initWithPasswordPtr:passwordLength:"
+ "initWithPasswordString:"
+ "initWithSubscriberInfo:pinCode:"
+ "initWithSupportedPairSetupMethods:pairingCachingEnabled:"
+ "lseek failed"
+ "malloc failed: %zu bytes"
+ "name=%@"
+ "no session key"
+ "no spake context"
+ "not prepared for reading"
+ "not prepared for writing"
+ "offset"
+ "open failed"
+ "openWithCompletionHandler:"
+ "pairingPromptHandler"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingNFCTag:"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingPINCode:"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingPassphrase:"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingQRCodeInformation:"
+ "pairingRequestStartedForDataSession:nfcTagScannedCompletionHandler:"
+ "pairingRequestStartedForDataSession:passphraseInputCompletionHandler:"
+ "pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:"
+ "pairingRequestStartedForDataSession:qrCodeScannedCompletionHandler:"
+ "pairingShowHandler"
+ "pinCode"
+ "pinCode=%@"
+ "re-open after close not allowed"
+ "read failed"
+ "readLength:completionHandler:"
+ "readLength:offset:completionHandler:"
+ "scrypt storage malloc failed: %lld bytes"
+ "scryptWithPasswordData:outputPtr:outputLen:error:"
+ "setConfirmPData:"
+ "setConfirmVData:"
+ "setDisableCompactVoice:"
+ "setOffset:"
+ "setPairingCachingEnabled:"
+ "setPairingMethod:"
+ "setPairingPromptHandler:"
+ "setPairingShowHandler:"
+ "setSharePData:"
+ "setShareVData:"
+ "setWfaPairingCacheEnabled:"
+ "setWfaPairingMethod:"
+ "shareP"
+ "sharePData"
+ "shareV"
+ "shareVData"
+ "super init failed"
+ "textInfo=%@"
+ "tryPairingPassword:"
+ "tryPairingPassword: length=%d"
+ "v32@0:8@\"WiFiAwareDataSession\"16@?<v@?@\"NSData\">24"
+ "v32@0:8@\"WiFiAwareDataSession\"16@?<v@?@\"NSString\">24"
+ "v40@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublishServiceSpecificInfo\"24@\"NSData\"32"
+ "v40@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublishServiceSpecificInfo\"24@\"NSString\"32"
+ "v40@0:8Q16Q24@?32"
+ "wfaPairingCacheEnabled"
+ "wfaPairingMethod"
+ "write failed"
+ "writeData:completionHandler:"
+ "writeData:offset:completionHandler:"
- "\x01\x11\x11."
- "\x01H\x12"
- "\x01\xb2\x1a"
- "### SendMessage failed: %{error}"
- "### SendMessage failed: EP %@, Data %.12@, %{error}"
- "### WFA DataSession confirmed for existing session: %@\n"
- "### WFA DataSession confirmed missing identifier\n"
- "### WFA DataSession start failed: %@, %#m\n"
- "### WFA DataSession terminated missing identifier: %#m\n"
- "### WFA DataSession terminated untracked: '%@', %@, %#m\n"
- "### WFA discovery result missing identifier\n"
- "### WFA lost result missing identifier\n"
- "### WFAPublisher start failed: '%@', %#m\n"
- "### WFASubscriber start failed: '%@', %#m\n"
- ", IP %##a"
- "-[CUNANDataSession _activateWithCompletion:]"
- "-[CUNANDataSession _invalidate]"
- "-[CUNANDataSession _invalidated]"
- "-[CUNANDataSession _terminateServerDataSession]"
- "-[CUNANDataSession _terminateServerDataSession]_block_invoke_2"
- "-[CUNANDataSession dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:]_block_invoke"
- "-[CUNANDataSession dataSession:failedToStartWithError:]_block_invoke"
- "-[CUNANDataSession dataSession:terminatedWithReason:]_block_invoke"
- "-[CUNANDataSession dataSessionRequestStarted:]_block_invoke"
- "-[CUNANDataSession reportIssue:]_block_invoke"
- "-[CUNANDataSession updateLinkStatus:]_block_invoke"
- "-[CUNANPublisher _activateWithCompletion:]"
- "-[CUNANPublisher _invalidate]"
- "-[CUNANPublisher _invalidated]"
- "-[CUNANPublisher _publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]"
- "-[CUNANPublisher _updateServiceSpecificInfo]"
- "-[CUNANPublisher _updateServiceSpecificInfo]_block_invoke"
- "-[CUNANPublisher publisher:dataIndicatedForHandle:serviceSpecificInfo:]"
- "-[CUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke"
- "-[CUNANPublisher publisher:failedToStartWithError:]_block_invoke"
- "-[CUNANPublisher publisher:receivedMessage:fromSubscriberID:subscriberAddress:]_block_invoke"
- "-[CUNANPublisher publisher:terminatedWithReason:]_block_invoke"
- "-[CUNANPublisher publisherStarted:]_block_invoke"
- "-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke"
- "-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke_2"
- "-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke_4"
- "-[CUNANPublisher updateLinkStatus:]_block_invoke"
- "-[CUNANSubscriber _activateWithCompletion:]"
- "-[CUNANSubscriber _invalidate]"
- "-[CUNANSubscriber _invalidated]"
- "-[CUNANSubscriber _lostAllEndpoints]_block_invoke"
- "-[CUNANSubscriber _subscriber:lostDiscoveryResultForPublishID:address:]"
- "-[CUNANSubscriber _subscriber:receivedDiscoveryResult:]"
- "-[CUNANSubscriber reportMockEndpointFound:]_block_invoke"
- "-[CUNANSubscriber reportMockEndpointLost:]_block_invoke"
- "-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke"
- "-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke_2"
- "-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke_4"
- "-[CUNANSubscriber subscriber:failedToStartWithError:]_block_invoke"
- "-[CUNANSubscriber subscriber:receivedMessage:fromPublishID:address:]_block_invoke"
- "-[CUNANSubscriber subscriber:terminatedWithReason:]_block_invoke"
- "-[CUNANSubscriber subscriberStarted:]_block_invoke"
- "Activate '%@', %#{flags}\n"
- "Activate: endpoint=%@, controlFlags=%@, trafficFlags=%@"
- "Activate: serviceType=%@, name='%@', port=%d, trafficFlags=%@, customData=%@, textInfo=%@"
- "DataSession ended: %@\n"
- "DataSession started: %@\n"
- "Endpoint changed: %@, %#{flags}\n"
- "Endpoint found: %@\n"
- "Endpoint lost: %@\n"
- "SendMessage completed: EP %@, Data %.12@"
- "SendMessage start: EP %@, Data %.12@"
- "WFA DataSession indicated: '%@', %@\n"
- "WFA DataSession request started: %@\n"
- "WFA DataSession terminate completed: %#m\n"
- "WFA DataSession terminate start\n"
- "WFA DataSession terminated: %@, %#m\n"
- "WFA DataSession terminated: '%@', %@, %#m\n"
- "WFA discovery result: PA <%@>, PI %u, SV '%@', SI <%@>\n"
- "WFA lost result missing not found: %@\n"
- "WFA lost result: PA <%@>, PI %u\n"
- "WFAPublisher restarting after unexpected termination\n"
- "WFAPublisher started: '%@'\n"
- "WFAPublisher terminated: '%@', %s\n"
- "WFASubscriber restarting after unexpected termination\n"
- "WFASubscriber started: '%@'\n"
- "WFASubscriber terminated: '%@', %s\n"

```
