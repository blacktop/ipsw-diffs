## rapportd

> `/usr/libexec/rapportd`

```diff

-  __TEXT.__text: 0x17efe0
-  __TEXT.__auth_stubs: 0x34b0
-  __TEXT.__objc_stubs: 0x118a0
-  __TEXT.__objc_methlist: 0x8f70
+  __TEXT.__text: 0x17fda0
+  __TEXT.__auth_stubs: 0x34f0
+  __TEXT.__objc_stubs: 0x11980
+  __TEXT.__objc_methlist: 0x8fa8
   __TEXT.__const: 0x5f50
-  __TEXT.__cstring: 0x2f946
+  __TEXT.__cstring: 0x2fb66
   __TEXT.__objc_classname: 0xf4f
-  __TEXT.__objc_methtype: 0x44a1
-  __TEXT.__gcc_except_tab: 0x2344
-  __TEXT.__objc_methname: 0x19920
+  __TEXT.__objc_methtype: 0x44b1
+  __TEXT.__gcc_except_tab: 0x2348
+  __TEXT.__objc_methname: 0x19a30
   __TEXT.__oslogstring: 0x3132
   __TEXT.__swift5_typeref: 0x16d4
   __TEXT.__swift5_capture: 0xb38

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5120
-  __TEXT.__eh_frame: 0x4bec
+  __TEXT.__unwind_info: 0x5128
+  __TEXT.__eh_frame: 0x4bb4
   __DATA_CONST.__const: 0x8000
   __DATA_CONST.__cfstring: 0x6100
   __DATA_CONST.__objc_classlist: 0x368

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x1a68
-  __DATA_CONST.__got: 0x980
+  __DATA_CONST.__auth_got: 0x1a88
+  __DATA_CONST.__got: 0xa18
   __DATA_CONST.__auth_ptr: 0x660
-  __DATA.__objc_const: 0x10640
-  __DATA.__objc_selrefs: 0x5608
-  __DATA.__objc_ivar: 0xfbc
+  __DATA.__objc_const: 0x10680
+  __DATA.__objc_selrefs: 0x5638
+  __DATA.__objc_ivar: 0xfc4
   __DATA.__objc_data: 0x2b50
   __DATA.__data: 0x3578
-  __DATA.__bss: 0x4580
-  __DATA.__common: 0xc8
+  __DATA.__bss: 0x4590
+  __DATA.__common: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7808
-  Symbols:   1351
-  CStrings:  10770
+  Functions: 7820
+  Symbols:   1355
+  CStrings:  10789
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_acfuncs : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _nw_advertise_descriptor_get_advertise_scope
+ _nw_array_is_empty
+ _nw_endpoint_copy_dictionary
+ _nw_endpoint_create_from_dictionary
+ _nw_endpoint_get_application_service_alias
+ _nw_endpoint_set_application_service_alias
- _nw_framer_connection_state_copy_object_value
- _nw_framer_connection_state_set_object_value
CStrings:
+ "### Activation of BLE CBServer failed: %@"
+ "+[QRServiceDiscoveryEndpointInfo resolvedEndpointFromBrowseEndpoint:sessionUUID:]"
+ "-[QRServiceDiscoveryEndpointInfo browseEndpointForService:agentClientID:]"
+ "-[QRServiceDiscoveryQueryResult browseEndpointForAgentClientID:]"
+ "-[RPCompanionLinkDaemon _restartBLECBServer]"
+ "-[RPCompanionLinkDaemon _startBLECBServer]_block_invoke_2"
+ "-[RPServiceDiscoveryClient _systemMonitorStart]_block_invoke_3"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YO2Bx7/Sources/Rapport_executables/Rapport/Pairing/RPPairingClient.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YO2Bx7/Sources/Rapport_executables/Rapport/Pairing/RPPairingDistributedActor.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YO2Bx7/Sources/Rapport_executables/Rapport/Pairing/RPPairingHelpers.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YO2Bx7/Sources/Rapport_executables/Rapport/Pairing/RPPairingSession.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YO2Bx7/Sources/Rapport_executables/Rapport/Swift/RPUtilities.swift"
+ "B28@0:8@16I24"
+ "BackgroundLow"
+ "Failed to obtain advertise descriptor for service\n"
+ "FindNearbyLocalFindableAccessoryExtendedRange"
+ "Rejecting unauthorized request\n"
+ "Resolved QR endpoint to %@ from browse %@"
+ "Restart BLE CBServer after %lu seconds"
+ "Unable to resolve QR endpoint - no alias"
+ "Unable to resolve QR endpoint - no placeholder"
+ "_bleCBServerRestartInterval"
+ "_bleCBServerRestartTimer"
+ "_restartBLECBServer"
+ "_stopBLECBServer"
+ "advertiseScopeForDevice:"
+ "browseEndpointForAgentClientID:"
+ "browseEndpointForService:agentClientID:"
+ "canIncomingRequestFromDevice:accessAdvertiseScope:"
+ "intersectSet:"
+ "resolvedEndpointFromBrowseEndpoint:sessionUUID:"
- "-[QRServiceDiscoveryEndpointInfo endpointForService:sessionUUID:]"
- "-[QRServiceDiscoveryQueryResult endpointWithSessionUUID:]"
- "-[RPServiceDiscoveryClient _systemMonitorStart]_block_invoke_2"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AtOYI6/Sources/Rapport_executables/Rapport/Pairing/RPPairingClient.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AtOYI6/Sources/Rapport_executables/Rapport/Pairing/RPPairingDistributedActor.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AtOYI6/Sources/Rapport_executables/Rapport/Pairing/RPPairingHelpers.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AtOYI6/Sources/Rapport_executables/Rapport/Pairing/RPPairingSession.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AtOYI6/Sources/Rapport_executables/Rapport/Swift/RPUtilities.swift"
- "endpointForService:sessionUUID:"
- "endpointWithSessionUUID:"
- "started"
- "true"

```
