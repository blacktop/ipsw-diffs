## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2022.100.23.0.0
-  __TEXT.__text: 0x254fc8
-  __TEXT.__auth_stubs: 0x22d0
-  __TEXT.__objc_methlist: 0x16ea0
-  __TEXT.__cstring: 0x23231
-  __TEXT.__const: 0xa78
-  __TEXT.__gcc_except_tab: 0x5188
-  __TEXT.__oslogstring: 0x405b2
+2022.100.25.0.0
+  __TEXT.__text: 0x258ee8
+  __TEXT.__auth_stubs: 0x22e0
+  __TEXT.__objc_methlist: 0x17290
+  __TEXT.__cstring: 0x23957
+  __TEXT.__const: 0xab8
+  __TEXT.__gcc_except_tab: 0x5218
+  __TEXT.__oslogstring: 0x40c55
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.evaluator_cfg: 0x6417
   __TEXT.default_clp: 0x2fe0

   __TEXT.network_clp: 0x4b40
   __TEXT.baseband_clp: 0xee70
   __TEXT.bb_MAV_clp: 0xa690
-  __TEXT.bb_INT_clp: 0x68f0
+  __TEXT.bb_INT_clp: 0x68e0
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x6600
-  __TEXT.__objc_classname: 0x1cc4
-  __TEXT.__objc_methname: 0x3b53a
-  __TEXT.__objc_methtype: 0x65d8
-  __TEXT.__objc_stubs: 0x24d00
+  __TEXT.__unwind_info: 0x66c8
+  __TEXT.__objc_classname: 0x1d37
+  __TEXT.__objc_methname: 0x3b996
+  __TEXT.__objc_methtype: 0x6a34
+  __TEXT.__objc_stubs: 0x251a0
   __DATA_CONST.__got: 0xdf0
-  __DATA_CONST.__const: 0x64e8
-  __DATA_CONST.__objc_classlist: 0x830
+  __DATA_CONST.__const: 0x6508
+  __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x190
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc670
+  __DATA_CONST.__objc_selrefs: 0xc7a0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x578
-  __DATA_CONST.__objc_arraydata: 0x820
-  __AUTH_CONST.__auth_got: 0x1180
+  __DATA_CONST.__objc_superrefs: 0x588
+  __DATA_CONST.__objc_arraydata: 0x810
+  __AUTH_CONST.__auth_got: 0x1188
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x2340
-  __AUTH_CONST.__cfstring: 0x1c040
-  __AUTH_CONST.__objc_const: 0x39f48
+  __AUTH_CONST.__const: 0x2360
+  __AUTH_CONST.__cfstring: 0x1c9e0
+  __AUTH_CONST.__objc_const: 0x3b0a0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
-  __AUTH_CONST.__objc_dictobj: 0x8c0
-  __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__objc_dictobj: 0x898
+  __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0x1428
-  __DATA.__objc_ivar: 0x2c64
-  __DATA.__data: 0x1c00
+  __AUTH.__objc_data: 0x1568
+  __DATA.__objc_ivar: 0x2ccc
+  __DATA.__data: 0x1c60
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x358
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x3db8
   __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x15a8
+  __DATA_DIRTY.__bss: 0x15c8
   __DATA_DIRTY.__common: 0x1a0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10827
-  Symbols:   12268
-  CStrings:  22174
+  Functions: 10909
+  Symbols:   12351
+  CStrings:  22374
 
Symbols:
+ _inet_pton
CStrings:
+ "\x0f\x0f\x04"
+ "\"digest\" key doesn't supply a dictionary"
+ "\"enable\" key doesn't supply a number"
+ "\"immediate\" key doesn't supply a number"
+ "\"reference\" key doesn't supply a number"
+ "\"start\" key doesn't supply a number"
+ "%@ %-26s %@"
+ "<NULL>"
+ "@\"BasebandFlowInformer\""
+ "@24@0:8^(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})16"
+ "B32@0:8^(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})16@24"
+ "BB"
+ "BasebandFlowChecker"
+ "BasebandFlowChecker can't create digest from snapshot: %@"
+ "BasebandFlowChecker flow start for %@ %d -> %d %@"
+ "BasebandFlowChecker flow stop for %@  %d -> %d"
+ "BasebandFlowChecker flow stop prior to change %@"
+ "BasebandFlowChecker flowClassificationChange %@  %d -> %d, nothing reportable"
+ "BasebandFlowChecker flowClassificationChange no change on %@  %d -> %d"
+ "BasebandFlowChecker new poll interval %.3f, new cancel token %lld"
+ "BasebandFlowChecker non-cell flowClassificationChange %@  %d -> %d, new is reportable"
+ "BasebandFlowChecker: _administrativeDisable"
+ "BasebandFlowChecker: _administrativeEnable"
+ "BasebandFlowChecker: informer is %@"
+ "BasebandFlowChecker: keyPath: enabled, change: %@"
+ "BasebandFlowChecker: keypath for enabled had bad format for new, %@"
+ "BasebandFlowChecker: unrecognized keyPath: %@, change: %@"
+ "BasebandFlowDigest"
+ "BasebandFlowDigest initWithDictionary failure: %@ with input %{public}@"
+ "BasebandFlowDigest sockaddr init from dictionary fails: %@ input %@"
+ "BasebandFlowDigest type %s flags %s%s%s %s %s state %@ src %@ dest %@ protocol %s"
+ "BasebandFlowInformer"
+ "BasebandFlowInformer _receiveIndication %@ %@"
+ "BasebandFlowInformer created instance %p"
+ "BasebandFlowInformer enabled %d (indication %d symptom %d) immediate %d"
+ "BasebandFlowInformer enabled %d after %@"
+ "BasebandFlowInformer extant flow  %@ -> %@"
+ "BasebandFlowInformer relays message %@"
+ "BasebandFlowInformer reset after currentDataSIMIdentifier indication"
+ "BasebandFlowInformer reset on error %@"
+ "BasebandFlowInformerTestAccess supplied with %{public}@"
+ "BasebandFlowTraceEntry"
+ "CT client failed to send tagged info, error %@"
+ "Can't create jsonObject"
+ "Can't initialize with supplied digest"
+ "Can't use local addr"
+ "Can't use remote addr"
+ "Elephant"
+ "Exception trying to create JSON object %@"
+ "FAE: system has taggedInfo feature flag disabled"
+ "FAE: system has taggedInfo feature flag enabled, bbFlowChecker is %@"
+ "Flow start"
+ "Flow stop"
+ "FlowScrutinizerDelegate"
+ "Hit max flows"
+ "IPv4 address string format"
+ "IPv6 address string format"
+ "Incorrect version number"
+ "Invalid direction string"
+ "Invalid flow flags"
+ "Invalid foregroundBool"
+ "Invalid isQUICBool"
+ "Invalid wasForegroundBool"
+ "Message too small"
+ "No dest to init"
+ "No digest for flow start"
+ "No payload at eventQualifiers[@\"1\"]"
+ "No reference supplied"
+ "No start/stop supplied"
+ "No valid address"
+ "No valid address string"
+ "No valid dictionary"
+ "No valid family"
+ "No valid flow state"
+ "No valid flow type"
+ "No valid flowInfo"
+ "No valid local address"
+ "No valid portnum"
+ "No valid protocol"
+ "No valid remote address"
+ "No valid scopeId"
+ "Performed reset"
+ "QUIC"
+ "Set enableForcedViaSymptom"
+ "Set informImmediate"
+ "T"
+ "T@\"NSData\",R,N"
+ "T@\"NSDictionary\",R,N"
+ "T@,&,N,V_item"
+ "TB,N,V_taggedInfoFeatureFlagEnabled"
+ "TaggedInfoTestHandler gets informer at %p"
+ "TaggedInfoTestHandler set self for symptomstool -m %d"
+ "TaggedInfoTestHandler symptom processing: %@"
+ "Tr*,N,V_name"
+ "Unknown family"
+ "[32@\"BasebandFlowTraceEntry\"]"
+ "_addrDictFromStruct:"
+ "_enableForcedViaSymptom"
+ "_enabledViaBBIndication"
+ "_encodedData"
+ "_flows"
+ "_infoBlock"
+ "_informImmediate"
+ "_informer"
+ "_initSockaddr:fromDict:"
+ "_item"
+ "_maxFlowsPerBBMessage"
+ "_pending"
+ "_pollInterval"
+ "_pollMaxDelay"
+ "_pollMaxStale"
+ "_primeFromLocalAddress:remoteAddress:"
+ "_receiveIndication:"
+ "_relayMessage:"
+ "_resetOnError"
+ "_resetOnError:"
+ "_sendSingleDigest:"
+ "_taggedInfoFeatureFlagEnabled"
+ "_traceEntries"
+ "_traceSeqno"
+ "addr"
+ "bal"
+ "d/l"
+ "dataSIMIdentifer"
+ "direction"
+ "enableForcedViaSymptom"
+ "enabledViaBBIndication"
+ "family"
+ "flowFlags"
+ "flowInfo"
+ "flowStart,clearing"
+ "flowStart,not-enabled"
+ "flowStart,pending"
+ "flowStart,sending"
+ "flowStart:digest:"
+ "flowState"
+ "flowStop,not-enabled"
+ "flowStop,not-found"
+ "flowStop,pending"
+ "flowStop,sending"
+ "flowStop:"
+ "immediate"
+ "indication"
+ "informImmediate"
+ "isBalanced"
+ "isDownload"
+ "isElephant"
+ "isQUIC"
+ "isUpload"
+ "item"
+ "jsonObject not dictionary"
+ "no context"
+ "no selector for sendTaggedInfo:type:payload:completion:"
+ "no-direction"
+ "not-enabled"
+ "not-set"
+ "pending flow %@ -> %@"
+ "primeFromQUICLocalAddress:remoteAddress:"
+ "primeFromSnapshot:"
+ "primeFromTCPLocalAddress:remoteAddress:"
+ "primeFromUDPLocalAddress:remoteAddress:"
+ "protocol"
+ "relayMessage"
+ "remote"
+ "rxIndication"
+ "scopeId"
+ "sendSingleDigest"
+ "sendTaggedInfo"
+ "sendTaggedInfo:payload:"
+ "sendTaggedInfo:type:payload:completion:"
+ "setEnableForcedViaSymptom:"
+ "setEnabledViaBBIndication:"
+ "setInformImmediate:"
+ "setIsBalanced:"
+ "setIsDownload:"
+ "setIsElephant:"
+ "setIsQUIC:"
+ "setIsUpload:"
+ "setItem:"
+ "setTaggedInfoFeatureFlagEnabled:"
+ "setWasStartedInForeground:"
+ "startedForeground"
+ "taggedInfoFeatureFlagEnabled"
+ "tagged_info_reporting"
+ "tagged_info_reporting is %sabled"
+ "trace:item:"
+ "tracking flow %@ -> %@"
+ "u/l"
+ "v32@0:8r*16@24"
+ "v44@0:8I16@\"NSNumber\"20@\"FlowLedger\"28@\"NWStatsProtocolSnapshot\"36"
+ "wasStartedInForeground"
+ "{IBICallPsFlowInfoBlock=\"local\"(?=\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]}\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]}\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"protocol\"i\"flow_type\"i\"flow_flags\"i\"flow_state\"i\"reserved\"I}"
+ "\xa1"
- "not-supported"

```
