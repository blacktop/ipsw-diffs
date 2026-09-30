## rapportd

> `/usr/libexec/rapportd`

```diff

-  __TEXT.__text: 0x1940b8
-  __TEXT.__auth_stubs: 0x39a0
-  __TEXT.__objc_stubs: 0x13520
-  __TEXT.__objc_methlist: 0xa0b0
+  __TEXT.__text: 0x194e64
+  __TEXT.__auth_stubs: 0x39e0
+  __TEXT.__objc_stubs: 0x135e0
+  __TEXT.__objc_methlist: 0xa0e8
   __TEXT.__const: 0x5fb0
-  __TEXT.__cstring: 0x36cb6
+  __TEXT.__cstring: 0x36ed6
   __TEXT.__objc_classname: 0x10bf
-  __TEXT.__objc_methtype: 0x4aa1
-  __TEXT.__gcc_except_tab: 0x24ac
-  __TEXT.__objc_methname: 0x1c650
+  __TEXT.__objc_methtype: 0x4ab1
+  __TEXT.__gcc_except_tab: 0x24b0
+  __TEXT.__objc_methname: 0x1c730
   __TEXT.__oslogstring: 0x3492
   __TEXT.__swift5_typeref: 0x1710
   __TEXT.__swift5_capture: 0xb78

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5948
-  __TEXT.__eh_frame: 0x4c7c
-  __DATA_CONST.__const: 0x8448
+  __TEXT.__unwind_info: 0x5968
+  __TEXT.__eh_frame: 0x4c44
+  __DATA_CONST.__const: 0x8470
   __DATA_CONST.__cfstring: 0x67a0
   __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x1ce0
-  __DATA_CONST.__got: 0xa28
+  __DATA_CONST.__auth_got: 0x1d00
+  __DATA_CONST.__got: 0xac0
   __DATA_CONST.__auth_ptr: 0x670
-  __DATA.__objc_const: 0x11c90
-  __DATA.__objc_selrefs: 0x5e30
-  __DATA.__objc_ivar: 0x1124
+  __DATA.__objc_const: 0x11cd0
+  __DATA.__objc_selrefs: 0x5e60
+  __DATA.__objc_ivar: 0x112c
   __DATA.__objc_data: 0x2d80
   __DATA.__data: 0x3ad8
-  __DATA.__bss: 0x4720
-  __DATA.__common: 0xc8
+  __DATA.__bss: 0x4730
+  __DATA.__common: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8571
-  Symbols:   1449
-  CStrings:  11807
+  Functions: 8583
+  Symbols:   1453
+  CStrings:  11826
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_acfuncs : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
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
+ "-[RPCompanionLinkDaemon _miscHandleLaunchAppRequest:responseHandler:]_block_invoke_4"
+ "-[RPCompanionLinkDaemon _restartBLECBServer]"
+ "-[RPCompanionLinkDaemon _startBLECBServer]_block_invoke_3"
+ "-[RPServiceDiscoveryClient _systemMonitorStart]_block_invoke_3"
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
- "-[RPCompanionLinkDaemon _miscHandleLaunchAppRequest:responseHandler:]_block_invoke_2"
- "-[RPServiceDiscoveryClient _systemMonitorStart]_block_invoke_2"
- "endpointForService:sessionUUID:"
- "endpointWithSessionUUID:"
- "started"
- "true"

```
