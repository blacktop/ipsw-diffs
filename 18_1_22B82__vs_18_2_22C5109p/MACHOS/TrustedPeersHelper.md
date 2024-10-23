## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61439.42.2.0.0
-  __TEXT.__text: 0x21c384
-  __TEXT.__auth_stubs: 0x1e60
-  __TEXT.__objc_stubs: 0x2b00
-  __TEXT.__objc_methlist: 0x2c14
-  __TEXT.__const: 0x94a8
-  __TEXT.__cstring: 0x16499
-  __TEXT.__objc_methname: 0x853f
-  __TEXT.__oslogstring: 0x9ea2
+61439.60.91.502.1
+  __TEXT.__text: 0x21ce70
+  __TEXT.__auth_stubs: 0x1e50
+  __TEXT.__objc_stubs: 0x2860
+  __TEXT.__objc_methlist: 0x2b24
+  __TEXT.__const: 0x94a0
+  __TEXT.__cstring: 0x16165
+  __TEXT.__objc_methname: 0x81b1
+  __TEXT.__oslogstring: 0xa011
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x32ec
-  __TEXT.__swift5_typeref: 0x3548
+  __TEXT.__constg_swiftt: 0x3304
+  __TEXT.__swift5_typeref: 0x359a
   __TEXT.__swift5_fieldmd: 0x23ac
   __TEXT.__swift5_reflstr: 0x1de7
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x360
   __TEXT.__swift5_proto: 0x838
   __TEXT.__swift5_types: 0x264
-  __TEXT.__objc_classname: 0x4c5
-  __TEXT.__objc_methtype: 0x20fb
+  __TEXT.__objc_classname: 0x48c
+  __TEXT.__objc_methtype: 0x20c2
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x3440
-  __TEXT.__gcc_except_tab: 0x1d4
+  __TEXT.__swift5_capture: 0x34fc
+  __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__dlopen_cstrs: 0x216
-  __TEXT.__unwind_info: 0x4eb0
+  __TEXT.__dlopen_cstrs: 0x11a
+  __TEXT.__unwind_info: 0x4e60
   __TEXT.__eh_frame: 0x6f70
-  __DATA_CONST.__auth_got: 0xf40
-  __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__auth_ptr: 0x650
-  __DATA_CONST.__const: 0xf928
-  __DATA_CONST.__cfstring: 0x20c0
-  __DATA_CONST.__objc_classlist: 0x268
+  __DATA_CONST.__auth_got: 0xf38
+  __DATA_CONST.__got: 0x828
+  __DATA_CONST.__auth_ptr: 0x640
+  __DATA_CONST.__const: 0xf9a8
+  __DATA_CONST.__cfstring: 0x1f20
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x7f88
-  __DATA.__objc_selrefs: 0x1f90
-  __DATA.__objc_ivar: 0x2cc
-  __DATA.__objc_data: 0x2ad8
-  __DATA.__data: 0x72d8
+  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA.__objc_const: 0x7d78
+  __DATA.__objc_selrefs: 0x1ec0
+  __DATA.__objc_ivar: 0x2b4
+  __DATA.__objc_data: 0x2a40
+  __DATA.__data: 0x72f8
   __DATA.__objc_stublist: 0x90
   __DATA.__common: 0x8d0
-  __DATA.__bss: 0x103f0
+  __DATA.__bss: 0x10378
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
+  - /System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8079
-  Symbols:   498
-  CStrings:  3427
+  Functions: 8072
+  Symbols:   496
+  CStrings:  3360
 
Symbols:
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _dispatch_async
CStrings:
+ "<CuttlefishCurrentItem(%!@(MISSING))>"
+ "<CuttlefishCurrentItemSpecifier(%!@(MISSING)): %!@(MISSING)>"
+ "<CuttlefishPCSIdentity(%!@(MISSING))>"
+ "<CuttlefishPCSServiceIdentifier(%!@(MISSING)): %!@(MISSING)>"
+ "Finding bottleID failed for %!{(MISSING)public}s: %!{(MISSING)public}s"
+ "Finding bottleID for %!{(MISSING)public}s"
+ "Finding deviceNames failed for %!{(MISSING)public}s: %!{(MISSING)public}s"
+ "Finding deviceNames for %!{(MISSING)public}s"
+ "egoPeer: %!@(MISSING)"
+ "octagonPeerID Error finding peer with bottleID %!s(MISSING), privacy: .public): %!{(MISSING)public}s"
+ "octagonPeerID Unable to finding peer with peerID %!{(MISSING)public}s"
+ "octagonPeerID complete: %!{(MISSING)public}s"
+ "octagonPeerIDGivenBottleID"
+ "octagonPeerIDGivenBottleIDWithSpecificUser:bottleID:reply:"
+ "self peerID present but egoPeer not found"
+ "trustedDeviceNamesByPeerID"
+ "trustedDeviceNamesByPeerID complete: %!{(MISSING)public}s"
+ "trustedDeviceNamesByPeerIDWithSpecificUser:reply:"
+ "v40@0:8@\"TPSpecificUser\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "\x12"
- "@\"AAFAnalyticsEvent\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@56@0:8@16@24@32B40@44B52"
- "@72@0:8@16@24@32@40@48B56B60@64"
- "AAFAnalyticsEvent"
- "AAFAnalyticsEvent+Security.m"
- "AAFAnalyticsEventSecurity"
- "AAFAnalyticsReporter"
- "AAFAnalyticsTransportRTC"
- "AKAccountManager"
- "Class getAAFAnalyticsEventClass(void)_block_invoke"
- "Class getAAFAnalyticsReporterClass(void)_block_invoke"
- "Class getAAFAnalyticsTransportRTCClass(void)_block_invoke"
- "Class getAKAccountManagerClass(void)_block_invoke"
- "NSString *getkAAFDeviceSessionId(void)"
- "NSString *getkAAFFlowId(void)"
- "SecurityAnalyticsReporterRTC"
- "SecurityAnalyticsReporterRTC.m"
- "T@\"AAFAnalyticsEvent\",&,V_event"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
- "TB,V_areTestsEnabled"
- "TB,V_canSendMetrics"
- "TB,V_isAAAFoundationAvailable"
- "TB,V_isAuthKitAvailable"
- "_areTestsEnabled"
- "_canSendMetrics"
- "_event"
- "_isAAAFoundationAvailable"
- "_isAuthKitAvailable"
- "_queue"
- "aafanalyticsevent-security: failed to softlink AAAFoundation"
- "aafanalyticsevent-security: failed to softlink AuthKit"
- "accountAccessTelemetryOptInForAccount:"
- "analyticsReporterWithTransport:"
- "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
- "areTestsEnabled"
- "authKitAccountWithAltDSID returned error: %!@(MISSING)"
- "authKitAccountWithAltDSID:error:"
- "canSendMetrics"
- "com.apple.aaa.dnu"
- "com.apple.security.aafanalyticsevent.queue"
- "com.apple.security.allowedMIDHashMismatch"
- "com.apple.security.deletedMIDHashMismatch"
- "com.apple.security.duplicateMachineID"
- "com.apple.security.fetchAndPersistChanges"
- "com.apple.security.fetchPolicyDocument"
- "com.apple.security.midVanishedFromTDL"
- "com.apple.security.numberOfTrustedOctagonPeers"
- "com.apple.security.tdlProcessingSuccess"
- "com.apple.securityd"
- "didSucceed"
- "egoMachineIDVanishedFromTDL"
- "event"
- "fetchDeviceSessionIDFromAuthKit:"
- "getEvent"
- "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:sendMetric:"
- "initWithEventName:eventCategory:initData:"
- "initWithKeychainCircleMetrics:altDSID:eventName:category:"
- "isAAAFoundationAvailable"
- "isAuthKitAvailable"
- "kAAFDeviceSessionId"
- "kAAFFlowId"
- "numberOfTrustedPeers"
- "permittedToSendMetrics"
- "populateUnderlyingErrorsStartingWithRootError:"
- "primaryAuthKitAccount"
- "retryAttemptCount"
- "rtcAnalyticsReporter"
- "sendEvent:"
- "setAreTestsEnabled:"
- "setCanSendMetrics:"
- "setEvent:"
- "setIsAAAFoundationAvailable:"
- "setIsAuthKitAvailable:"
- "setQueue:"
- "sharedInstance"
- "softlink:o:path:/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation"
- "softlink:o:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"
- "telemetryDeviceSessionIDForAccount:"
- "totalRetryDuration"
- "v36@0:8@16B24@28"
- "void *AAAFoundationLibrary(void)"
- "void *AuthKitLibrary(void)"

```
