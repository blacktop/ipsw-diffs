## IDSFoundation

> `/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation`

```diff

-1968.100.1.2.1
-  __TEXT.__text: 0x33b998
-  __TEXT.__auth_stubs: 0x4a30
-  __TEXT.__objc_methlist: 0x1a704
+1968.200.31.2.1
+  __TEXT.__text: 0x33e210
+  __TEXT.__auth_stubs: 0x4a50
+  __TEXT.__objc_methlist: 0x1a75c
   __TEXT.__const: 0x15840
-  __TEXT.__oslogstring: 0x26c34
-  __TEXT.__cstring: 0x32a11
-  __TEXT.__gcc_except_tab: 0xcf04
+  __TEXT.__oslogstring: 0x27524
+  __TEXT.__cstring: 0x32ef1
+  __TEXT.__gcc_except_tab: 0xcff8
   __TEXT.__ustring: 0xc
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__swift5_typeref: 0x5d37
-  __TEXT.__swift5_fieldmd: 0x5534
+  __TEXT.__swift5_typeref: 0x5d27
+  __TEXT.__swift5_fieldmd: 0x554c
   __TEXT.__constg_swiftt: 0x5178
   __TEXT.__swift5_builtin: 0x208
-  __TEXT.__swift5_reflstr: 0x2e10
+  __TEXT.__swift5_reflstr: 0x2e30
   __TEXT.__swift5_assocty: 0x2a8
   __TEXT.__swift5_protos: 0x84
   __TEXT.__swift5_proto: 0x12a0
   __TEXT.__swift5_types: 0x764
-  __TEXT.__swift5_capture: 0x12d4
-  __TEXT.__swift_as_entry: 0x280
-  __TEXT.__swift_as_ret: 0x220
+  __TEXT.__swift5_capture: 0x12e8
+  __TEXT.__swift_as_entry: 0x27c
+  __TEXT.__swift_as_ret: 0x228
   __TEXT.__swift5_mpenum: 0xa0
   __TEXT.__swift5_types2: 0x1c
-  __TEXT.__unwind_info: 0xb870
-  __TEXT.__eh_frame: 0x95e0
+  __TEXT.__unwind_info: 0xb888
+  __TEXT.__eh_frame: 0x9688
   __TEXT.__objc_classname: 0x391c
-  __TEXT.__objc_methname: 0x35d3d
+  __TEXT.__objc_methname: 0x35e81
   __TEXT.__objc_methtype: 0x7a8d
-  __TEXT.__objc_stubs: 0x1aae0
+  __TEXT.__objc_stubs: 0x1ab40
   __DATA_CONST.__got: 0x1468
-  __DATA_CONST.__const: 0x62d8
+  __DATA_CONST.__const: 0x6300
   __DATA_CONST.__objc_classlist: 0x1150
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa878
+  __DATA_CONST.__objc_selrefs: 0xa898
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xab8
   __DATA_CONST.__objc_arraydata: 0x1520
-  __AUTH_CONST.__auth_got: 0x2528
-  __AUTH_CONST.__const: 0x11230
-  __AUTH_CONST.__cfstring: 0x2a140
-  __AUTH_CONST.__objc_const: 0x39fc0
+  __AUTH_CONST.__auth_got: 0x2538
+  __AUTH_CONST.__const: 0x11260
+  __AUTH_CONST.__cfstring: 0x2a380
+  __AUTH_CONST.__objc_const: 0x3a0b0
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x1e60
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x97a8
   __AUTH.__data: 0x35d8
-  __DATA.__objc_ivar: 0x2694
+  __DATA.__objc_ivar: 0x26a8
   __DATA.__data: 0x5b88
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x23b10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1CBAA0EF-E37F-3513-B3A1-F61D7C6E66CC
-  Functions: 17900
-  Symbols:   4865
-  CStrings:  24863
+  UUID: 05020169-F63A-3DFC-87E5-64A0A590D27F
+  Functions: 17909
+  Symbols:   4872
+  CStrings:  24935
 
Symbols:
+ OBJC_IVAR_$_IDSGlobalLink._hasUseLinkEngineBeenProgramaticallyOverriden
+ _IDSGlobalLinkOptionAllowExpensiveQualityMetrics
+ _IDSMessageContextQueueOneIdentifierKey
+ _IDSRegistrationPropertySupportsAskToResponseUI
+ _IDSServicePropertyAllowExpensiveQualityMetrics
+ _swift_task_immediate
+ _swift_task_isCurrentExecutorWithFlags
CStrings:
+ "%@ has state [%s], not sending command %04x."
+ "%@%@ is in [%s] state, skip connecting to QR."
+ "%@%@ is in [%s] state, skip sending info request."
+ "%@Found no local interface available for QR."
+ "%@Found no local interface available for QR. - gathering ABC with packet capture"
+ "%@receive self allocate response for request %@."
+ "%@receive self allocate response for unknown request %@."
+ "%@selfAllocation count = %lu"
+ "%@update ids-session-id:%@ for cbuuid:%@."
+ "%s TwoWay[%s]:      have allocated links but some are not fully connected; not making another allocation until connection done"
+ "%s TwoWay[%s]:      have used our allocation budget; no new allocation needed"
+ "%s TwoWay[%s]:      want another allocation; checking if we've already asked"
+ "%s TwoWay[%s]:     calling connector with links:\n         %s"
+ "%s TwoWay[%s]:     found unused allocation (not matching affinity): %s"
+ "%s TwoWay[%s]:     found unused allocation matching %s-%s: %s"
+ "%s TwoWay[%s]:     have remaining tuples and have connected all allocations we've got; already asked for allocation for %s, no need to ask again..."
+ "%s TwoWay[%s]:     have remaining tuples and have connected all allocations we've got; need to allocate for tuple %s"
+ "%s TwoWay[%s]:     no initial allocation, so will not trigger any new ones."
+ "%s TwoWay[%s]:     no remaining tuples; no allocation needed."
+ "%s TwoWay[%s]:     still have allocations we've not allocated; no new allocation needed"
+ "%s TwoWay[%s]: allocations available: %s, desired link types: %s"
+ "%s TwoWay[%s]: for allocated link: %s, allocation: %s"
+ "%s TwoWay[%s]: is initiator; checking if we need another allocation..."
+ "%s TwoWay[%s]: new allocated links: %s"
+ "%s TwoWay[%s]: remaining link types after accounting for existing allocated links: %s"
+ "%s TwoWay[%s]: remaining link types after assigning links matching affinities: %s"
+ "%s TwoWay[%s]: remaining link types after assigning links not matching affinities: %s"
+ "%s[%s]"
+ "%s[%s]: %s: %s-%s"
+ "%s[%s]: no link connector"
+ "BlockHomeInvitationInHH1"
+ "IDSMessageContextQueueOneIdentifierKey"
+ "TB,R,N,V_allowExpensiveQualityMetrics"
+ "Ti,V_remoteInterfacePreference"
+ "[%@] "
+ "_IDSGLLinkEngine: calling allocate block with from: %s, to: %s"
+ "_allowExpensiveQualityMetrics"
+ "_connectTCPAndUpdateLocalCandidatePortToAvailablePortIfNeeded: TCP connection: change the local address from %s to: %s"
+ "_connectWithSessionInfo%@: IDSGlobalLinkSession SessionInfoDict: %@"
+ "_connectWithSessionInfo%@: _H2FallbackEnabled after reading forceH2FallbackEnabled: %@"
+ "_connectWithSessionInfo%@: _avcDataBlob: %@"
+ "_connectWithSessionInfo%@: ftPowerOptimizationEnabled is enabled by com.apple.ids default"
+ "_connectWithSessionInfo%@: ftPowerOptimizationEnabled is enabled by session info"
+ "_connectWithSessionInfo%@: ftPowerOptimizationEnabled nil in session info"
+ "_connectWithSessionInfo%@: groupID nil in session info."
+ "_connectWithSessionInfo%@: set _H2FallbackEnabled to %@"
+ "_connectWithSessionInfo%@: we are already joining session, ignore connect request here"
+ "_ensureSessionWithSessionInfo[%@]: session has push token %@"
+ "_ensureSessionWithSessionInfo[%@]: updating session info for session %@"
+ "_hasUseLinkEngineBeenProgramaticallyOverriden"
+ "_localCandidatesForRelaySession[%@]: %@ is in [%s] state, should have no active links."
+ "_localCandidatesForRelaySession[%@]: checking %@"
+ "_localCandidatesForRelaySession[%@]: skipping clat46 ipv4 address %@"
+ "_remoteCandidatesForRelaySession[%@]: %@ is in [%s] state, should have no active links."
+ "_remoteCandidatesForRelaySession[%@]: delay connectWithSessionInfo for if:%d nat64 prefix."
+ "_remoteCandidatesForRelaySession[%@]: nat64 prefix cache hit for if:%d"
+ "_remoteInterfacePreference"
+ "_sendAllocbindForCandidatePair[%@]: *** Connect as %s, tag: %@, IDSSessionID: %@, QRSessionID: %@, Accepted: %@."
+ "_sendAllocbindForCandidatePair[%@]: enable secure control message for Receiver."
+ "_sendAllocbindForCandidatePair[%@]: invite recv: %.6f, allocbind start: %.6f, accept delay: %08x/%.6f"
+ "_sendAllocbindForCandidatePair[%@]: invite sent: %.6f, allocbind start: %.6f."
+ "_sendAllocbindForCandidatePair[%@]: sending STUN..."
+ "_sendAllocbindForCandidatePair[%@]: sending over H2..."
+ "_sendAllocbindForCandidatePair[%@]: sending over H3..."
+ "_sendInfoRequestForCandidatePair[%@]: sending STUN..."
+ "_sendInfoRequestForCandidatePair[%@]: sending over H2..."
+ "_sendInfoRequestForCandidatePair[%@]: sending over H3..."
+ "_supportsAskToResponseUI"
+ "_updateLinksForSession[%@] %@ (allocateType %ld): remoteRelayCandidates: %@"
+ "_updateLinksForSession[%@]: %@ (allocateType %ld): acceptance status: session is accepted"
+ "_updateLinksForSession[%@]: %@ (allocateType %ld): acceptance status: session is in superposition of accepted and not accepted"
+ "_updateLinksForSession[%@]: %@ (allocateType %ld): acceptance status: session is not accepted"
+ "_updateLinksForSession[%@]: %@ (allocateType %ld): localRelayCandidates: %@"
+ "_updateLinksForSession[%@]: force IPv6 options server: %@; default: %@; manual: %@"
+ "_updateLinksForSession[%@]: scheduling update for relaySessionID=%@ allocateType=%ld qos=%d..."
+ "addAllocation(_:withAffinity:remoteAffinity:resolvedEndpoints:)"
+ "addTwoWayAllocation:localAffinity:remoteAffinity:resolvedCandidates:"
+ "allow-expensive-quality-metrics"
+ "allowExpensiveQualityMetrics"
+ "com.apple.private.alloy.lightrose"
+ "configureGLExperiments: recordExpensiveQualityMetrics: our value: %@; session info: %@; resolved: %@"
+ "configureGLExperimentsWithSessionInfo:"
+ "connectRelayLinkFromCandidate[%@]: %@ relaySessionID=%@ fromCandidate:%@ toCandidate:%@ replacesLinkWithUniqueID:%@ isRealloc:%@"
+ "connectRelayLinkFromCandidate[%@]: created candidate pair (tag: %@): %@"
+ "connectRelayLinkFromCandidate[%@]: creating candidate pair..."
+ "connectRelayLinkFromCandidate[%@]: setPropertiesWithRelaySessionInfo, qrSessionInfo = %@"
+ "connectRelayLinkFromCandidate[%@]: setting isRealloc=YES"
+ "connectRelayLinkFromCandidate[%@]: skip allocbind request for %@, state [%s]"
+ "connectRelayLinkFromCandidate[%@]: start allocbind for %@ (token %lu bytes, key %lu bytes), participantID:%llu (LinkEngine)"
+ "connectRelayLinkFromCandidate[%@]: start info for %@ (token %lu bytes, key %lu bytes), participantID:%llu (LinkEngine)"
+ "connectRelayLinkFromCandidate[%@]: update GL: %@ state (%s->%s)."
+ "dualModeConfig"
+ "gl-allow-expensive-metrics"
+ "idsGLRunInTaskImmediatelyWithInferredTaskPriority: in task at priority %s"
+ "idsGLRunInTaskImmediatelyWithInferredTaskPriority: is on transport thread"
+ "idsGLRunInTaskImmediatelyWithInferredTaskPriority: not on transport thread"
+ "initWithDeviceUniqueID: recordExpensiveQualityMetrics (may still be set to false later): %@ (coin flip: %@, chance: %f)"
+ "optout-failing"
+ "optout-success"
+ "remoteInterfacePreference"
+ "scheduleUpdate %s for ASAP creating Task.immediate (%s)"
+ "scheduleUpdate %s for ASAP in Task.immediate (%s)"
+ "setRemoteInterfacePreference:"
+ "startNewAllocationFromInterface[%@]: [%@]: not setting remote interface preference (reduceCellularUsage: %@)"
+ "startNewAllocationFromInterface[%@]: [%@]: setting remote interface preference (reduceCellularUsage: %@)"
+ "startNewAllocationFromInterface[%@]: set up new QR link [%@], accepted session %@, ids-session-id %@."
+ "supports-askto-responseUI"
+ "update %s created Task.immediate (%s)"
+ "v40@0:8@16i24i28@32"
- "%@ is in [%s] state, should have no active links."
- "%@ is in [%s] state, skip connecting to QR."
- "%@ is in [%s] state, skip sending info request."
- "%s TwoWay:      have used our allocation budget; no new allocation needed"
- "%s TwoWay:      want another allocation; checking if we've already asked"
- "%s TwoWay:     calling connector with links:\n         %s"
- "%s TwoWay:     found unused allocation (not matching affinity): %s"
- "%s TwoWay:     found unused allocation matching %s: %s"
- "%s TwoWay:     have remaining tuples and have connected all allocations we've got; already asked for allocation for %s, no need to ask again..."
- "%s TwoWay:     have remaining tuples and have connected all allocations we've got; need to allocate for tuple %s"
- "%s TwoWay:     no initial allocation, so will not trigger any new ones."
- "%s TwoWay:     no remaining tuples; no allocation needed."
- "%s TwoWay:     still have allocations we've not allocated; no new allocation needed"
- "%s TwoWay: allocations available: %s, desired link types: %s"
- "%s TwoWay: for allocated link: %s, allocation: %s"
- "%s TwoWay: is initiator; checking if we need another allocation..."
- "%s TwoWay: new allocated links: %s"
- "%s TwoWay: remaining link types after accounting for existing allocated links: %s"
- "%s TwoWay: remaining link types after assigning links matching affinities: %s"
- "%s TwoWay: remaining link types after assigning links not matching affinities: %s"
- "*** Connect as %s, tag: %@, IDSSessionID: %@, QRSessionID: %@, Accepted: %@."
- "ITWHomeHH1"
- "_connectWithSessionInfo: IDSGlobalLinkSession SessionInfoDict: %@"
- "_connectWithSessionInfo: _H2FallbackEnabled after reading forceH2FallbackEnabled: %@"
- "_connectWithSessionInfo: _avcDataBlob: %@"
- "_connectWithSessionInfo: ftPowerOptimizationEnabled is enabled by com.apple.ids default"
- "_connectWithSessionInfo: ftPowerOptimizationEnabled is enabled by session info"
- "_connectWithSessionInfo: ftPowerOptimizationEnabled nil in session info"
- "_connectWithSessionInfo: groupID nil in session info."
- "_connectWithSessionInfo: set _H2FallbackEnabled to %@"
- "_connectWithSessionInfo: we are already joining session, ignore connect request here"
- "_ensureSessionWithSessionInfo updating session info for session %@"
- "_ensureSessionWithSessionInfo: session has push token %@"
- "_localCandidatesForRelaySession: checking %@"
- "_localCandidatesForRelaySession: skipping clat46 ipv4 address %@"
- "_sendAllocbindForCandidatePair: sending STUN..."
- "_sendAllocbindForCandidatePair: sending over H2..."
- "_sendAllocbindForCandidatePair: sending over H3..."
- "_sendInfoRequestForCandidatePair: sending STUN..."
- "_sendInfoRequestForCandidatePair: sending over H2..."
- "_sendInfoRequestForCandidatePair: sending over H3..."
- "_updateLinks: scheduling update for relaySessionID=%@ allocateType=%ld qos=%d..."
- "_updateLinksForSession %@ (allocateType %ld): acceptance status: session is accepted"
- "_updateLinksForSession %@ (allocateType %ld): acceptance status: session is in superposition of accepted and not accepted"
- "_updateLinksForSession %@ (allocateType %ld): acceptance status: session is not accepted"
- "_updateLinksForSession %@ (allocateType %ld): localRelayCandidates: %@"
- "_updateLinksForSession %@ (allocateType %ld): remoteRelayCandidates: %@"
- "_updateLocalCandidatePortToAvailablePortIfNeeded: TCP connection: change the local address from %s to: %s"
- "addTwoWayAllocation:hasAffinityToCell:resolvedCandidates:"
- "configureGLExperiments"
- "connectRelayLinkFromCandidate: %@ relaySessionID=%@ fromCandidate:%@ toCandidate:%@ replacesLinkWithUniqueID:%@ isRealloc:%@"
- "connectRelayLinkFromCandidate: created candidate pair (tag: %@): %@"
- "connectRelayLinkFromCandidate: creating candidate pair..."
- "connectRelayLinkFromCandidate: setPropertiesWithRelaySessionInfo, qrSessionInfo = %@"
- "connectRelayLinkFromCandidate: setting isRealloc=YES"
- "initWithDeviceUniqueID: recordExpensiveQualityMetrics: %@ (coin flip: %@, chance: %f)"
- "optout"
- "receive self allocate response for request %@."
- "receive self allocate response for unknown request %@."
- "scheduleUpdate %s for ASAP creating Task (%s)"
- "scheduleUpdate %s for ASAP in Task (%s)"
- "selfAllocation count = %lu"
- "start allocbind for %@ (token %lu bytes, key %lu bytes), participantID:%llu (LinkEngine)"
- "start info for %@ (token %lu bytes, key %lu bytes), participantID:%llu (LinkEngine)"
- "update %s created Task (%s)"

```
