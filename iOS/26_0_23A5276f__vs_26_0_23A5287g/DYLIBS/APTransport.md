## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-890.66.3.0.0
-  __TEXT.__text: 0xa4760
-  __TEXT.__auth_stubs: 0x3200
+890.68.4.0.0
+  __TEXT.__text: 0xa5928
+  __TEXT.__auth_stubs: 0x32b0
   __TEXT.__objc_methlist: 0x1368
-  __TEXT.__cstring: 0x2ae64
+  __TEXT.__cstring: 0x2b3d9
   __TEXT.__const: 0x328
   __TEXT.__gcc_except_tab: 0x4cc
   __TEXT.__oslogstring: 0x16e
   __TEXT.__dlopen_cstrs: 0x18b
-  __TEXT.__unwind_info: 0x2670
+  __TEXT.__unwind_info: 0x26e0
   __TEXT.__objc_classname: 0x1f5
-  __TEXT.__objc_methname: 0x48b3
+  __TEXT.__objc_methname: 0x48cf
   __TEXT.__objc_methtype: 0xf40
-  __TEXT.__objc_stubs: 0x4080
+  __TEXT.__objc_stubs: 0x40a0
   __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x35a0
+  __DATA_CONST.__const: 0x3618
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_selrefs: 0x13f0
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1910
+  __AUTH_CONST.__auth_got: 0x1968
   __AUTH_CONST.__const: 0x2b48
-  __AUTH_CONST.__cfstring: 0x5f20
+  __AUTH_CONST.__cfstring: 0x5fa0
   __AUTH_CONST.__objc_const: 0x1c90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A00987C9-A128-3B2A-A06F-0493A000B6BF
-  Functions: 4496
-  Symbols:   11679
-  CStrings:  5838
+  UUID: 163C32ED-6560-3A5A-9C8D-C46EA6F42763
+  Functions: 4507
+  Symbols:   11712
+  CStrings:  5872
 
Symbols:
+ _OUTLINED_FUNCTION_23
+ ___block_descriptor_56_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_tmp.234
+ ___block_descriptor_tmp.238
+ ___block_descriptor_tmp.49
+ ___block_descriptor_tmp.53
+ ___block_descriptor_tmp.76
+ ___block_descriptor_tmp.78
+ ___block_descriptor_tmp.80
+ ___block_descriptor_tmp.95
+ ___block_literal_global.236
+ ___block_literal_global.240
+ ___bonjourCacheHomeKit_introspector_cmd_injectDevices_block_invoke
+ ___unbufnwGuts_handleNewConnectionGroupInternal_block_invoke_3
+ ___unbufnwGuts_handleNewConnectionGroupInternal_block_invoke_4
+ _bonjourCacheHomeKit_introspector_cmd_injectDevices
+ _bonjourCacheHomeKit_introspector_cmd_injectDevices.cold.1
+ _browser_handleConnectivityHelperEventInternal.cold.14
+ _kAPTransportConnectionProperty_BoundLocalNetworkIPAddress
+ _kAPTransportConnectionProperty_HopLimit
+ _nw_connection_copy_connected_local_endpoint
+ _nw_connection_group_copy_descriptor
+ _nw_connection_group_copy_parameters
+ _nw_connection_group_create
+ _nw_connection_group_set_receive_handler
+ _nw_connection_group_state_to_string
+ _nw_group_descriptor_create_multicast
+ _nw_group_descriptor_get_type
+ _nw_ip_options_set_hop_limit
+ _nw_multicast_group_descriptor_set_disable_unicast_traffic
+ _nw_multicast_group_descriptor_set_specific_source
+ _objc_msgSend$stringWithCString:encoding:
+ _unbufnwGuts_handleNewConnectionGroupInternal
+ _unbufnwGuts_handleNewConnectionGroupInternal.cold.1
+ _unbufnwGuts_handleNewConnectionGroupInternal.cold.2
- ___block_descriptor_tmp.228
- ___block_descriptor_tmp.232
- ___block_descriptor_tmp.50
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.63
- ___block_descriptor_tmp.83
- ___block_descriptor_tmp.86
- ___block_literal_global.230
- ___block_literal_global.234
- ___unbufnw_Resume_block_invoke_4.cold.1
CStrings:
+ "890.68.4"
+ "BonjourCacheHomeKit_InjectDevices"
+ "BoundLocalNetworkIPAddress"
+ "Failed to query WiFi power state: %#m."
+ "HopLimit"
+ "Injecting device: %@ %'@\n"
+ "Injecting into cache for network signature: %@\n"
+ "WiFi power changed %s -> %s."
+ "WiFi powered %s."
+ "[%{ptr}] %s err=%#m"
+ "[%{ptr}] BonjourCacheHomeKit_InjectDevices"
+ "[%{ptr}] BonjourCacheHomeKit_InjectDevices: %@ %'@"
+ "[%{ptr}] connection group state '%s'%?{end} err=%#m"
+ "[%{ptr}] multicast connected from '%s' (to '%##a' using '%s' interface) in %1.3f ms"
+ "[%{ptr}] multicast listener started on %##a"
+ "disconnected"
+ "err: current network signature is unavailable\n"
+ "err: failed to prepare info: %@\n"
+ "err: failed to read file: %@\n"
+ "err: invalid file argument\n"
+ "err: invalid value for key: %'@\n"
+ "err: item is not a dictionary: %@\n"
+ "err: missing file argument\n"
+ "err: no items to add\n"
+ "failed to connect"
+ "inject device-infos in plist-file into cache"
+ "stringWithCString:encoding:"
+ "v28@?0^{dispatch_data_s=}8^{nw_content_context=}16B24"
+ "void bonjourCacheHomeKit_introspector_cmd_injectDevices(const void *, FILE *, int, char **)"
+ "void bonjourCacheHomeKit_introspector_cmd_injectDevices(const void *, FILE *, int, char **)_block_invoke"
+ "void unbufnwGuts_multicastConnectionGroupStateChangedHandler(APTransportConnectionUnbufferedNWGutsRef, nw_connection_group_t, nw_connection_group_state_t, nw_error_t)"
+ "void unbufnwGuts_multiplexConnectionGroupStateChangedHandler(APTransportConnectionUnbufferedNWGutsRef, nw_connection_group_t, nw_connection_group_state_t, nw_error_t)"
- "890.66.3"
- "<power reading not available, assuming no>"

```
