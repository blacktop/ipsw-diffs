## rapportd

> `/usr/libexec/rapportd`

```diff

-716.300.121.0.0
-  __TEXT.__text: 0x157ad8
-  __TEXT.__auth_stubs: 0x3710
-  __TEXT.__objc_stubs: 0x10920
-  __TEXT.__objc_methlist: 0x86f4
-  __TEXT.__const: 0x5ce0
-  __TEXT.__cstring: 0x2f6a1
+716.300.222.0.0
+  __TEXT.__text: 0x1595c8
+  __TEXT.__auth_stubs: 0x36d0
+  __TEXT.__objc_stubs: 0x109a0
+  __TEXT.__objc_methlist: 0x8724
+  __TEXT.__const: 0x5d80
+  __TEXT.__cstring: 0x2f9b1
   __TEXT.__objc_classname: 0xaa1
-  __TEXT.__objc_methtype: 0x3d73
+  __TEXT.__objc_methtype: 0x3d87
   __TEXT.__gcc_except_tab: 0x2094
-  __TEXT.__objc_methname: 0x17e8d
-  __TEXT.__oslogstring: 0x2912
-  __TEXT.__swift5_typeref: 0x1534
-  __TEXT.__swift5_capture: 0xb40
-  __TEXT.__swift5_reflstr: 0xde4
+  __TEXT.__objc_methname: 0x17f23
+  __TEXT.__oslogstring: 0x29b2
+  __TEXT.__swift5_typeref: 0x1562
+  __TEXT.__swift5_capture: 0xb44
+  __TEXT.__swift5_reflstr: 0xdf4
   __TEXT.__swift5_assocty: 0x130
-  __TEXT.__constg_swiftt: 0xc18
+  __TEXT.__constg_swiftt: 0xc48
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_fieldmd: 0xe44
+  __TEXT.__swift5_fieldmd: 0xe6c
   __TEXT.__swift5_proto: 0x1dc
-  __TEXT.__swift5_types: 0xf4
+  __TEXT.__swift5_types: 0xfc
   __TEXT.__swift_as_entry: 0x210
   __TEXT.__swift_as_ret: 0x25c
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4cc8
-  __TEXT.__eh_frame: 0x4c1c
-  __DATA_CONST.__auth_got: 0x1b98
-  __DATA_CONST.__got: 0x980
+  __TEXT.__unwind_info: 0x4d40
+  __TEXT.__eh_frame: 0x4ddc
+  __DATA_CONST.__auth_got: 0x1b78
+  __DATA_CONST.__got: 0x988
   __DATA_CONST.__auth_ptr: 0x5a8
-  __DATA_CONST.__const: 0x7620
-  __DATA_CONST.__cfstring: 0x5ec0
+  __DATA_CONST.__const: 0x76d8
+  __DATA_CONST.__cfstring: 0x5ee0
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x160

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xefa8
-  __DATA.__objc_selrefs: 0x5238
+  __DATA.__objc_const: 0xef68
+  __DATA.__objc_selrefs: 0x5258
   __DATA.__objc_ivar: 0xe8c
-  __DATA.__objc_data: 0x24b8
-  __DATA.__data: 0x34f8
-  __DATA.__bss: 0x4740
-  __DATA.__common: 0xc8
+  __DATA.__objc_data: 0x24a8
+  __DATA.__data: 0x34c8
+  __DATA.__bss: 0x4750
+  __DATA.__common: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 11C608CB-49E5-30B5-BF80-79A7D61C2295
-  Functions: 7141
-  Symbols:   1364
-  CStrings:  10353
+  UUID: FAF4816F-CC40-3F8B-B845-D71F1E03BC99
+  Functions: 7169
+  Symbols:   1359
+  CStrings:  10373
 
Symbols:
- _$s10Foundation4DataVSHAAMc
- _$s7Network10NWEndpointO2nwSo03OS_C9_endpoint_pSgvg
- _$sSD11descriptionSSvg
- _$sSS7cStringSSSPys4Int8VG_tcfC
- _nw_endpoint_get_bonjour_service_name
CStrings:
+ "%@ Did not find match to update existingEndpoint: %@. Removing existing out of date mapping and adding new one."
+ "%@ Failed to parse UUID from endpoint identifier: %@"
+ "%@ LISTEN: No PIN info available in callback"
+ "%@ RESOLVE: Bonjour resolve - calling browseResponse: %@, with resolvedEndpoints: %@"
+ "%@ RESOLVE: Failed to extract server public key, browseClient: %@"
+ "%@ RESOLVE: PINs Changed - calling browseResponse: %@, with updatedEndpoint: %@"
+ "%@ Skipping active pairing discovery for %@\n"
+ "+[RPNWEndpoint removeEndpointsFromDiscoverySessionID:currentUUIDs:]"
+ "-[RPNWAgentClient startPairingDiscovery:agentUUID:applicationService:browseMode:]_block_invoke"
+ "-[RPNWNetworkAgent(Pairing) continueCreatingPairingListener:endpoint:pin:advertiseSensitiveInfo:]"
+ "-[RPNWNetworkAgent(Pairing) continueCreatingPairingListener:endpoint:pin:advertiseSensitiveInfo:]_block_invoke"
+ "-[RPNWNetworkAgent(Pairing) continueCreatingPairingListener:endpoint:pin:advertiseSensitiveInfo:]_block_invoke_2"
+ "-[RPNWNetworkAgent(Pairing) continueCreatingPairingListener:endpoint:pin:advertiseSensitiveInfo:]_block_invoke_3"
+ "AXGuestPassServer"
+ "Closing encryption stream for: %s"
+ "ContactID"
+ "Falling back to legacy SPAKE client identity"
+ "Found matching prePairingEndpoint PAKE configuration for %s"
+ "Maximum pairing attempts reached for %s"
+ "No prePairingEndpoint for temporary pairing"
+ "Removing endpoints from discovery session '%@', current UUIDs: %@"
+ "Removing pre-pairing endpoint: %s"
+ "Starting PairVerify with: %s"
+ "T@\"NSDate\",N,R"
+ "TQ,N,R"
+ "Updating browse results with newly paired endpoint %s"
+ "_shouldStartActivePairingDiscovery:"
+ "activeBrowserEndpointsChanged: %ld endpoints"
+ "continueCreatingPairingListener:endpoint:pin:advertiseSensitiveInfo:"
+ "createdAt"
+ "identityFeatureFlags"
+ "removeEndpointsFromDiscoverySessionID:currentUUIDs:"
+ "v40@?0@\"NSData\"8@\"NSUUID\"16@\"NSString\"24@\"NSError\"32"
+ "v44@0:8@16@24@32B40"
+ "v48@0:8@\"RPNWEndpoint\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"NSData\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "+[RPNWEndpoint removeAllEndpointsDiscoverySessionID:]"
- "-[RPNWNetworkAgent(Pairing) createPairingListener:endpoint:pin:]_block_invoke_2"
- "-[RPNWNetworkAgent(Pairing) createPairingListener:endpoint:pin:]_block_invoke_3"
- "-[RPNWNetworkAgent(Pairing) createPairingListener:endpoint:pin:]_block_invoke_4"
- "Maximum pairing attempts reached for %@"
- "No pre-pairing endpoint found for identifier %s"
- "Removing endpoint all endpoints for discovery session '%@'"
- "Removing pre-pairing endpoint: %@"
- "Starting PairVerify with: %@"
- "Updating browse results with newly paired endpoint %@"
- "activeBrowserEndpointsChanged: %s"
- "attemptCounts"
- "currentPairingEndpoints"
- "currentPrePairingEndpoints"
- "encryptionStreams"
- "peerIdentityMap"
- "removeAllEndpointsDiscoverySessionID:"
- "v32@?0@\"NSData\"8@\"NSUUID\"16@\"NSError\"24"
- "v48@0:8@\"RPNWEndpoint\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"NSData\"@\"NSUUID\"@\"NSError\">40"

```
