## mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

-4024.100.99.0.0
-  __TEXT.__text: 0x2e6d64
-  __TEXT.__auth_stubs: 0x4df0
-  __TEXT.__objc_stubs: 0x20e20
-  __TEXT.__objc_methlist: 0x10bd0
-  __TEXT.__objc_methname: 0x33e2f
-  __TEXT.__cstring: 0x1989a
+4024.110.3.0.0
+  __TEXT.__text: 0x2e4e84
+  __TEXT.__auth_stubs: 0x4e00
+  __TEXT.__objc_stubs: 0x20d00
+  __TEXT.__objc_methlist: 0x10a90
+  __TEXT.__objc_methname: 0x33d1d
+  __TEXT.__cstring: 0x197aa
   __TEXT.__objc_classname: 0x282b
-  __TEXT.__objc_methtype: 0x6588
-  __TEXT.__const: 0x5e8a
-  __TEXT.__gcc_except_tab: 0x5400
-  __TEXT.__oslogstring: 0x1c03a
+  __TEXT.__objc_methtype: 0x6589
+  __TEXT.__const: 0x5e0a
+  __TEXT.__gcc_except_tab: 0x53fc
+  __TEXT.__oslogstring: 0x1bdfa
   __TEXT.__dlopen_cstrs: 0x9a
-  __TEXT.__swift5_typeref: 0x3718
+  __TEXT.__swift5_typeref: 0x36f0
   __TEXT.__swift5_capture: 0x2a74
-  __TEXT.__swift5_fieldmd: 0x2824
-  __TEXT.__constg_swiftt: 0x4398
-  __TEXT.__swift5_reflstr: 0x2d02
+  __TEXT.__swift5_fieldmd: 0x27a4
+  __TEXT.__constg_swiftt: 0x4270
+  __TEXT.__swift5_reflstr: 0x2cb2
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_proto: 0x4b4
-  __TEXT.__swift5_types: 0x2c4
+  __TEXT.__swift5_types: 0x2bc
   __TEXT.__swift5_assocty: 0x380
-  __TEXT.__info_plist: 0x4d6
-  __TEXT.__unwind_info: 0x9ab8
+  __TEXT.__info_plist: 0x4cc
+  __TEXT.__unwind_info: 0x9a58
   __TEXT.__eh_frame: 0x5280
-  __DATA_CONST.__auth_got: 0x2708
-  __DATA_CONST.__got: 0x23a8
-  __DATA_CONST.__auth_ptr: 0xb20
-  __DATA_CONST.__const: 0x12a98
-  __DATA_CONST.__cfstring: 0xd300
-  __DATA_CONST.__objc_classlist: 0x898
+  __DATA_CONST.__auth_got: 0x2710
+  __DATA_CONST.__got: 0x2398
+  __DATA_CONST.__auth_ptr: 0xb18
+  __DATA_CONST.__const: 0x12a48
+  __DATA_CONST.__cfstring: 0xd2e0
+  __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x530
+  __DATA_CONST.__objc_protolist: 0x528
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x138
+  __DATA_CONST.__objc_protorefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_intobj: 0x6a8
   __DATA_CONST.__objc_arraydata: 0x918
   __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0x23c70
-  __DATA.__objc_selrefs: 0xa3e8
-  __DATA.__objc_ivar: 0x1480
-  __DATA.__objc_data: 0x7e08
-  __DATA.__data: 0x8898
+  __DATA.__objc_const: 0x23a50
+  __DATA.__objc_selrefs: 0xa3a0
+  __DATA.__objc_ivar: 0x1484
+  __DATA.__objc_data: 0x7ba8
+  __DATA.__data: 0x8808
   __DATA.__bss: 0x7990
   __DATA.__common: 0x178
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 13307
-  Symbols:   2659
-  CStrings:  13231
+  Functions: 13246
+  Symbols:   2658
+  CStrings:  13205
 
Symbols:
+ _MRIRServiceTokenIdentifier
+ _MRPlaybackQueueToUserInfo
- _IRContextAppleTVControlKey
- _MRIRMediaRemoteDaemonServiceTokenIdentifier
- _MRIRTVRemoteServiceTokenIdentifier
CStrings:
+ "\x12\x13"
+ "\x1f\x02"
+ "\x1f\x04"
+ "4\x11"
+ "@\"IRServiceToken\""
+ "Static token %!@(MISSING) invalidated for session %!p(MISSING), discarding session and giving up - %!@(MISSING)"
+ "T@\"IRServiceToken\",&,N,V_serviceToken"
+ "T@\"NSError\",&,N,V_lastConnectionError"
+ "[MRDGroupSessionServer] Registering WHA identifier for connection failure: %!@(MISSING)"
+ "[MRDRRC].IRD Could not get token, error: %!@(MISSING)"
+ "[MRDRRC].IRD Created IRSession %!@(MISSING)"
+ "[MRDRRC].IRD Static token %!@(MISSING) invalidated for session %!p(MISSING), discarding session and giving up - %!@(MISSING)"
+ "_connectionFailedWHAIdentifiers"
+ "_lastConnectionError"
+ "initWithContentItems:location:withPropertiesFromPlaybackQueue:"
+ "initializeSessionWithCompletion:"
+ "lastConnectionError"
+ "registerConnectionFailureForWHAIdentifier:"
+ "runSession"
+ "runSession:"
+ "setLastConnectionError:"
+ "unregisterConnectionFailureForWHAIdentifier:"
- "\x11\x14"
- "\x1f\x01"
- "\x1f\x03"
- "5\x11"
- "Dynamic token %!@(MISSING) invalidated for session %!p(MISSING), discarding session and giving up - %!@(MISSING)"
- "IRContextUpdate_%!@(MISSING)"
- "Session not configured"
- "T@\"NSString\",&,N,V_contextKey"
- "T@\"NSString\",&,N,V_serviceIdentifier"
- "[MRDRRC].IRD Dynamic token %!@(MISSING) invalidated for session %!p(MISSING), discarding session and giving up - %!@(MISSING)"
- "[MRDRRC].IRD Invalidating Session"
- "[MRDRRC].IRD Session not configured"
- "[MRDRRC].IRD createRunningSession: no service token. Can't configure session."
- "[MRDRRC].IRD createRunningSession: service token found: %!@(MISSING)"
- "[MRDRRC].IRD createRunningSession: session created %!@(MISSING)"
- "[MRDRRC].IRD fetchServiceTokenWithCompletion: non user aware"
- "[MRDRRC].IRD getSessionWithLatestConfiguration:"
- "[MRDRRC].IRD getSessionWithLatestConfiguration: Session is nil. Cancel running code."
- "[ProximityController] Cluster mismatch - recommended: (%!@(MISSING)), response: (%!@(MISSING)) continuing to evaluate %!@(MISSING)"
- "_contextKey"
- "_deduplicateOutputDevices:"
- "_onQueue_createRunningSessionWithServiceToken:"
- "_onQueue_invalidateSession"
- "_serviceIdentifier"
- "contextKey"
- "contextOverrideDefaultsKey"
- "createRunningSession: no service token. Can't configure session."
- "daemonProvider"
- "fetchServiceTokenWithCompletion:"
- "getSessionWithLatestConfiguration:"
- "getSessionWithLatestConfiguration: Session is nil. Cancel running code."
- "initWithServiceIdentifier:contextKey:"
- "initializeSessionIfNeededWithCompletion:"
- "isMediaRemoteDaemonSession"
- "mediaremoted.MRDIntelligentRoutingDaemonLockScreenRoutingProvider"
- "recommendationWithIRCandidateResult:contextIdentifier:route:"
- "recommendationWithUntrustedIRCandidateResult:contextIdentifier:"
- "recommendations"
- "routeWithUnsafeCandidate:"
- "runSession:withMode:andServiceToken:"
- "serviceIdentifier"
- "setContextKey:"
- "setServiceIdentifier:"
- "tvRemoteProvider"
- "v16@?0@\"IRServiceToken\"8"
- "v16@?0@\"IRSession\"8"
- "v40@0:8@16q24@32"

```
