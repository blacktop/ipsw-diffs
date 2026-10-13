## IDSFoundation

> `/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation`

```diff

-2003.200.61.0.0
-  __TEXT.__text: 0x4e2e0c
-  __TEXT.__objc_methlist: 0x1bfdc
-  __TEXT.__const: 0x406f0
-  __TEXT.__cstring: 0x35dad
-  __TEXT.__oslogstring: 0x2d0ba
-  __TEXT.__gcc_except_tab: 0xc018
+2003.200.71.2.3
+  __TEXT.__text: 0x4f06e0
+  __TEXT.__objc_methlist: 0x1c04c
+  __TEXT.__const: 0x409a0
+  __TEXT.__cstring: 0x3604d
+  __TEXT.__oslogstring: 0x2d96a
+  __TEXT.__gcc_except_tab: 0xc0a8
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x188
-  __TEXT.__swift5_typeref: 0xb9a6
-  __TEXT.__constg_swiftt: 0xcb54
-  __TEXT.__swift5_reflstr: 0x6c76
-  __TEXT.__swift5_fieldmd: 0xb938
+  __TEXT.__swift5_typeref: 0xba36
+  __TEXT.__constg_swiftt: 0xcc3c
+  __TEXT.__swift5_reflstr: 0x6d66
+  __TEXT.__swift5_fieldmd: 0xba50
   __TEXT.__swift5_builtin: 0x3c0
   __TEXT.__swift5_assocty: 0x970
-  __TEXT.__swift5_proto: 0x34b0
-  __TEXT.__swift5_types: 0xef8
+  __TEXT.__swift5_proto: 0x34c8
+  __TEXT.__swift5_types: 0xf10
   __TEXT.__swift5_capture: 0x1668
-  __TEXT.__swift_as_entry: 0x3b8
-  __TEXT.__swift_as_ret: 0x33c
-  __TEXT.__swift_as_cont: 0x618
-  __TEXT.__swift5_protos: 0x9c
+  __TEXT.__swift_as_entry: 0x3c4
+  __TEXT.__swift_as_ret: 0x344
+  __TEXT.__swift_as_cont: 0x61c
+  __TEXT.__swift5_protos: 0xa0
   __TEXT.__swift5_acfuncs: 0x1cc
   __TEXT.__swift5_mpenum: 0x164
   __TEXT.__swift5_types2: 0x20
-  __TEXT.__unwind_info: 0x19e60
-  __TEXT.__eh_frame: 0x167cc
+  __TEXT.__unwind_info: 0x1a008
+  __TEXT.__eh_frame: 0x1682c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x76e8
+  __DATA_CONST.__const: 0x7700
   __DATA_CONST.__objc_classlist: 0x12c8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb350
+  __DATA_CONST.__objc_selrefs: 0xb380
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xb38
   __DATA_CONST.__objc_arraydata: 0x1558
-  __DATA_CONST.__got: 0x1570
-  __AUTH_CONST.__const: 0x1abb8
-  __AUTH_CONST.__cfstring: 0x2d680
-  __AUTH_CONST.__objc_const: 0x3f250
+  __DATA_CONST.__got: 0x1578
+  __AUTH_CONST.__const: 0x1ae70
+  __AUTH_CONST.__cfstring: 0x2d720
+  __AUTH_CONST.__objc_const: 0x3f2b0
   __AUTH_CONST.__objc_intobj: 0xc78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x1e90
-  __AUTH_CONST.__auth_got: 0x2a68
+  __AUTH_CONST.__auth_got: 0x2a90
   __AUTH.__objc_data: 0xa4b8
-  __AUTH.__data: 0xafd8
+  __AUTH.__data: 0xb0e8
   __DATA.__objc_ivar: 0x2914
-  __DATA.__data: 0xf580
+  __DATA.__data: 0xf610
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x220
+  __DATA.__common: 0x228
   __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__data: 0x1f8
   __DATA_DIRTY.__bss: 0x108

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 32071
-  Symbols:   5129
-  CStrings:  8514
+  Functions: 32169
+  Symbols:   5133
+  CStrings:  8536
 
Symbols:
+ _IDSGroupSessionClientParametersKey
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "%@ is marked for final disconnection - cancelling and creating new connection"
+ "IDSGLLinkEngineCommon.linkConnectNotAttempted: %s: connect request was not attempted (%ld attempt(s) in a row came back with nothing); connectable again, but not before %s"
+ "IDSGLLinkEngineCommon.linkConnectNotAttempted: %s: no link"
+ "IDSGLLinkEngineCommon.linkConnectNotAttempted: %s: not awaiting a connect (%s); nothing to report"
+ "IDSGLLinkEngineCommon.linkDidDisconnect: %s (attempt ending: %s)"
+ "IDSGLLinkEngineCommon.linkDidDisconnect: %s: disconnected before the connect attempt got anywhere (%ld in a row); not offering it again before %s"
+ "IDSGLLinkEngineCommon.linkDidFail: %s: failed before the connect attempt got anywhere (%ld in a row); not offering it again before %s"
+ "IDSGLLinkEngineCommon.resetConnectEligibility: explicit connect request: cleared backoff and stalled-connect counts; failed links offered again: %s"
+ "LinkEngineConnectBestController.logIfOfferedInPlaceOfHeldLinks: %s: offered in place of higher-priority %s, held after connect attempts that achieved nothing. They are offered again when their hold ends, and take over from this link if they connect."
+ "LinkEngineConnectBestController.update: %s: %s wants a retry, but is held until %s"
+ "LinkEngineConnectBestController.update: %s: %s, but held until %s"
+ "LinkEngineConnectFirstController.logIfOfferedInPlaceOfHeldLinks: %s: offered in place of higher-priority %s, held after connect attempts that achieved nothing. If this link connects first it is kept, and %s will not be offered again until it fails."
+ "LinkEngineConnectFirstController.update: %s: %s wants a retry, but is held until %s"
+ "LinkEngineConnectFirstController.update: %s: %s, but held until %s"
+ "LinkEngine[%s].get: %ld there is another scheduled update. triggering... (%s)"
+ "_IDSGLLinkEngine.init: Connect bounce backoff: disabled=%{bool}d"
+ "_IDSGLLinkEngine.init: Pre-join connect hold: disabled=%{bool}d"
+ "_connectWithSessionInfo%@: session is now joining; giving every link another chance"
+ "_relayConnectionBehaviorForSession[%@]: shared session has not joined, but the pre-join hold is disabled (pjh); connecting, and the send path will refuse"
+ "_relayConnectionBehaviorForSession[%@]: shared session has not joined; holding off connecting new links"
+ "connect bounce backoff"
+ "connectRelayLinkFromCandidate[%@]: update state (%s->%s) for %@ before info request."
+ "connectRelayLinkFromCandidate[%@]: update state (%s->%s) for %@; LinkEngine is retrying it."
+ "connectTCP: %@ is marked for final disconnection - cancelling and creating new connection"
+ "gs-client-parameters-key"
+ "info request would be refused while the pair is disconnecting"
+ "pre join connect hold"
+ "setSharedSessionHasJoined: %@; re-driving links"
- "IDSGLLinkEngineCommon.linkDidDisconnect: %s"
- "LinkEngineConnectBestController.update: %s: %s -> connecting (retry plugin)"
- "LinkEngine[%s].shouldContinueUpdating.get: %ld there is another scheduled update. triggering... (%s)"
- "setSharedSessionHasJoined: joined; re-driving links in case an allocbind was dropped pre-join"
- "this H/2 connection cannot be reused"
- "this QUIC connection cannot be reused"
```
