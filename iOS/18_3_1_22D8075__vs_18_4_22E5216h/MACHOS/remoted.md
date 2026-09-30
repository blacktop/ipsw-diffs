## remoted

> `/usr/libexec/remoted`

```diff

-172.80.4.0.0
-  __TEXT.__text: 0x4091c
-  __TEXT.__auth_stubs: 0x1810
-  __TEXT.__objc_stubs: 0x2220
-  __TEXT.__objc_methlist: 0x1370
-  __TEXT.__const: 0x21a
-  __TEXT.__oslogstring: 0x81a4
-  __TEXT.__cstring: 0x1ec3
-  __TEXT.__objc_methname: 0x22a4
+172.100.9.0.0
+  __TEXT.__text: 0x41eb0
+  __TEXT.__auth_stubs: 0x1820
+  __TEXT.__objc_stubs: 0x2280
+  __TEXT.__objc_methlist: 0x13b8
+  __TEXT.__const: 0x1fa
+  __TEXT.__oslogstring: 0x81bc
+  __TEXT.__cstring: 0x1f61
+  __TEXT.__objc_methname: 0x22f5
   __TEXT.__objc_classname: 0x27b
-  __TEXT.__objc_methtype: 0x6e6
-  __TEXT.__gcc_except_tab: 0x16c0
-  __TEXT.__unwind_info: 0xe00
-  __DATA_CONST.__auth_got: 0xc18
-  __DATA_CONST.__got: 0x218
+  __TEXT.__objc_methtype: 0x6e9
+  __TEXT.__gcc_except_tab: 0x1618
+  __TEXT.__unwind_info: 0xed0
+  __DATA_CONST.__auth_got: 0xc20
+  __DATA_CONST.__got: 0x220
   __DATA_CONST.__const: 0x12d8
-  __DATA_CONST.__cfstring: 0xca0
+  __DATA_CONST.__cfstring: 0xd00
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x2420
-  __DATA.__objc_selrefs: 0x8c0
-  __DATA.__objc_ivar: 0x200
+  __DATA.__objc_const: 0x2480
+  __DATA.__objc_selrefs: 0x8d8
+  __DATA.__objc_ivar: 0x208
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x670
   __DATA.__bss: 0x39a

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1284
-  Symbols:   488
-  CStrings:  1723
+  Functions: 1341
+  Symbols:   490
+  CStrings:  1736
 
Symbols:
+ _NSUnderlyingErrorKey
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/RemoteServiceDiscovery_executables/remoted/modules/identity.m"
+ "FileName"
+ "FunctionName"
+ "IPV6Address"
+ "LineNumber"
+ "SCRT root CA auth failed with error: %{public}@"
+ "Tr*,R,N,V_ipv6_str"
+ "UCRT root CA auth failed with error: %{public}@"
+ "_ipv6_str"
+ "assertion failure: \"!(uuid_is_null(self->remote_device_uuid))\" -> %llu"
+ "assertion failure: \"!adp_iokit_ctx\" -> %llu"
+ "assertion failure: \"!ncm_iokit_ctx\" -> %llu"
+ "assertion failure: \"!uuid_is_null(*uuid_out)\" -> %llu"
+ "assertion failure: \"!uuid_is_null(boot_session_uuid)\" -> %llu"
+ "assertion failure: \"!uuid_is_null(local_device_uuid)\" -> %llu"
+ "assertion failure: \"!uuid_is_null(remote_device_uuid)\" -> %llu"
+ "assertion failure: \"!uuid_is_null(self->bonjour_uuid)\" -> %llu"
+ "assertion failure: \"!uuid_is_null(self->remote_device_uuid)\" -> %llu"
+ "assertion failure: \"(strncmp(ifname, \"en\", strlen(\"en\")) == 0) || (strncmp(ifname, \"anpi\", strlen(\"anpi\")) == 0)\" -> %llu"
+ "assertion failure: \"*fd >= 0\" -> %llu"
+ "assertion failure: \"CFGetTypeID(answer) == CFStringGetTypeID()\" -> %llu"
+ "assertion failure: \"_uuid != ((void*)0)\" -> %llu"
+ "assertion failure: \"address\" -> %llu"
+ "assertion failure: \"adp_iokit_ctx\" -> %llu"
+ "assertion failure: \"advertise_descriptor\" -> %llu"
+ "assertion failure: \"asyncReply\" -> %llu"
+ "assertion failure: \"attach_notification\" -> %llu"
+ "assertion failure: \"bonjour_browser\" -> %llu"
+ "assertion failure: \"bonjour_listener\" -> %llu"
+ "assertion failure: \"boot_session_uuid_unparsed\" -> %llu"
+ "assertion failure: \"bp\" -> %llu"
+ "assertion failure: \"br != ((void*)0)\" -> %llu"
+ "assertion failure: \"browser\" -> %llu"
+ "assertion failure: \"cfuuid != ((void*)0)\" -> %llu"
+ "assertion failure: \"cfuuid_str != ((void*)0)\" -> %llu"
+ "assertion failure: \"clock_gettime(_CLOCK_REALTIME, &ts)\" -> %llu"
+ "assertion failure: \"connection_timer\" -> %llu"
+ "assertion failure: \"ctx\" -> %llu"
+ "assertion failure: \"ctx->notification\" -> %llu"
+ "assertion failure: \"ctx->queue\" -> %llu"
+ "assertion failure: \"current_state_int < kHostStateCount\" -> %llu"
+ "assertion failure: \"device\" -> %llu"
+ "assertion failure: \"device_name_map\" -> %llu"
+ "assertion failure: \"enabled_interface_name_cfstr\" -> %llu"
+ "assertion failure: \"endpoint\" -> %llu"
+ "assertion failure: \"endpoint_uuids\" -> %llu"
+ "assertion failure: \"entry\" -> %llu"
+ "assertion failure: \"fd != -1\" -> %llu"
+ "assertion failure: \"if_index\" -> %llu"
+ "assertion failure: \"ifindex\" -> %llu"
+ "assertion failure: \"ifname\" -> %llu"
+ "assertion failure: \"interface\" -> %llu"
+ "assertion failure: \"interfaces\" -> %llu"
+ "assertion failure: \"listener_source\" -> %llu"
+ "assertion failure: \"local_conn != ((void*)0)\" -> %llu"
+ "assertion failure: \"loopback_device != ((void*)0)\" -> %llu"
+ "assertion failure: \"loopback_device == ((void*)0)\" -> %llu"
+ "assertion failure: \"mac_addr\" -> %llu"
+ "assertion failure: \"matching_dict\" -> %llu"
+ "assertion failure: \"name\" -> %llu"
+ "assertion failure: \"ncm_iokit_ctx\" -> %llu"
+ "assertion failure: \"new_state == RSD_NCM_INTERFACE_STATE_ACTIVE || new_state == RSD_NCM_INTERFACE_STATE_DETACHED\" -> %llu"
+ "assertion failure: \"new_state == RSD_NCM_INTERFACE_STATE_ATTACHED || new_state == RSD_NCM_INTERFACE_STATE_ADDRESSED || new_state == RSD_NCM_INTERFACE_STATE_DETACHED\" -> %llu"
+ "assertion failure: \"new_state == RSD_NCM_INTERFACE_STATE_ATTACHED || new_state == RSD_NCM_INTERFACE_STATE_DETACHED\" -> %llu"
+ "assertion failure: \"notification\" -> %llu"
+ "assertion failure: \"nw_endpoint_copy_interface(endpoint)\" -> %llu"
+ "assertion failure: \"nw_endpoint_get_type(browsed_endpoint) == nw_endpoint_type_bonjour_service\" -> %llu"
+ "assertion failure: \"nw_endpoint_get_type(remote_endpoint) == nw_endpoint_type_address\" -> %llu"
+ "assertion failure: \"nwconn\" -> %llu"
+ "assertion failure: \"option->connection_timeout > 0\" -> %llu"
+ "assertion failure: \"parent_matching_dict\" -> %llu"
+ "assertion failure: \"parent_property_matching_dict\" -> %llu"
+ "assertion failure: \"path_interface\" -> %llu"
+ "assertion failure: \"payload_data\" -> %llu"
+ "assertion failure: \"reflector_conn != ((void*)0)\" -> %llu"
+ "assertion failure: \"remoted_queue\" -> %llu"
+ "assertion failure: \"reply\" -> %llu"
+ "assertion failure: \"required_ent\" -> %llu"
+ "assertion failure: \"result\" -> %llu"
+ "assertion failure: \"sa\" -> %llu"
+ "assertion failure: \"self->_canceled\" -> %llu"
+ "assertion failure: \"self.address_endpoint\" -> %llu"
+ "assertion failure: \"self.bonjour_endpoint\" -> %llu"
+ "assertion failure: \"self.browser != ((void*)0)\" -> %llu"
+ "assertion failure: \"self.browser == ((void*)0)\" -> %llu"
+ "assertion failure: \"self.connection == ((void*)0)\" -> %llu"
+ "assertion failure: \"self.device.state != REMOTED_DEVICE_STATE_GONE\" -> %llu"
+ "assertion failure: \"self.endpoint\" -> %llu"
+ "assertion failure: \"self.public_properties != ((void*)0)\" -> %llu"
+ "assertion failure: \"self.type != REMOTE_DEVICE_TYPE_INVALID_OR_UNKNOWN\" -> %llu"
+ "assertion failure: \"service != ((void *)0)\" -> %llu"
+ "assertion failure: \"service\" -> %llu"
+ "assertion failure: \"service_len > 0 && service_len < 64\" -> %llu"
+ "assertion failure: \"service_name\" -> %llu"
+ "assertion failure: \"sntp_request_payload\" -> %llu"
+ "assertion failure: \"sntp_response_payload\" -> %llu"
+ "assertion failure: \"str != ((void*)0)\" -> %llu"
+ "assertion failure: \"success\" -> %llu"
+ "assertion failure: \"tmp\" -> %llu"
+ "assertion failure: \"xpc_get_type(clientMessage) == (&_xpc_type_dictionary)\" -> %llu"
+ "assertion failure: \"xpcconn\" -> %llu"
+ "evaluateDcrt"
+ "ipv6_str"
+ "numberWithInt:"
+ "populateInterfaceProperties"
+ "r*"
- "Peer's DCRT failed trust evaluation with error: %{public}@"
- "assertion failure: \"!(uuid_is_null(self->remote_device_uuid))\" -> %lld"
- "assertion failure: \"!adp_iokit_ctx\" -> %lld"
- "assertion failure: \"!ncm_iokit_ctx\" -> %lld"
- "assertion failure: \"!uuid_is_null(*uuid_out)\" -> %lld"
- "assertion failure: \"!uuid_is_null(boot_session_uuid)\" -> %lld"
- "assertion failure: \"!uuid_is_null(local_device_uuid)\" -> %lld"
- "assertion failure: \"!uuid_is_null(remote_device_uuid)\" -> %lld"
- "assertion failure: \"!uuid_is_null(self->bonjour_uuid)\" -> %lld"
- "assertion failure: \"!uuid_is_null(self->remote_device_uuid)\" -> %lld"
- "assertion failure: \"(strncmp(ifname, \"en\", strlen(\"en\")) == 0) || (strncmp(ifname, \"anpi\", strlen(\"anpi\")) == 0)\" -> %lld"
- "assertion failure: \"*fd >= 0\" -> %lld"
- "assertion failure: \"CFGetTypeID(answer) == CFStringGetTypeID()\" -> %lld"
- "assertion failure: \"_uuid != ((void *)0)\" -> %lld"
- "assertion failure: \"address\" -> %lld"
- "assertion failure: \"adp_iokit_ctx\" -> %lld"
- "assertion failure: \"advertise_descriptor\" -> %lld"
- "assertion failure: \"asyncReply\" -> %lld"
- "assertion failure: \"attach_notification\" -> %lld"
- "assertion failure: \"bonjour_browser\" -> %lld"
- "assertion failure: \"bonjour_listener\" -> %lld"
- "assertion failure: \"boot_session_uuid_unparsed\" -> %lld"
- "assertion failure: \"bp\" -> %lld"
- "assertion failure: \"br != ((void *)0)\" -> %lld"
- "assertion failure: \"browser\" -> %lld"
- "assertion failure: \"cfuuid != ((void *)0)\" -> %lld"
- "assertion failure: \"cfuuid_str != ((void *)0)\" -> %lld"
- "assertion failure: \"clock_gettime(_CLOCK_REALTIME, &ts)\" -> %lld"
- "assertion failure: \"connection_timer\" -> %lld"
- "assertion failure: \"ctx\" -> %lld"
- "assertion failure: \"ctx->notification\" -> %lld"
- "assertion failure: \"ctx->queue\" -> %lld"
- "assertion failure: \"current_state_int < kHostStateCount\" -> %lld"
- "assertion failure: \"device\" -> %lld"
- "assertion failure: \"device_name_map\" -> %lld"
- "assertion failure: \"enabled_interface_name_cfstr\" -> %lld"
- "assertion failure: \"endpoint\" -> %lld"
- "assertion failure: \"endpoint_uuids\" -> %lld"
- "assertion failure: \"entry\" -> %lld"
- "assertion failure: \"fd != -1\" -> %lld"
- "assertion failure: \"if_index\" -> %lld"
- "assertion failure: \"ifindex\" -> %lld"
- "assertion failure: \"ifname\" -> %lld"
- "assertion failure: \"interface\" -> %lld"
- "assertion failure: \"interfaces\" -> %lld"
- "assertion failure: \"listener_source\" -> %lld"
- "assertion failure: \"local_conn != ((void *)0)\" -> %lld"
- "assertion failure: \"loopback_device != ((void *)0)\" -> %lld"
- "assertion failure: \"loopback_device == ((void *)0)\" -> %lld"
- "assertion failure: \"mac_addr\" -> %lld"
- "assertion failure: \"matching_dict\" -> %lld"
- "assertion failure: \"name\" -> %lld"
- "assertion failure: \"ncm_iokit_ctx\" -> %lld"
- "assertion failure: \"new_state == RSD_NCM_INTERFACE_STATE_ACTIVE || new_state == RSD_NCM_INTERFACE_STATE_DETACHED\" -> %lld"
- "assertion failure: \"new_state == RSD_NCM_INTERFACE_STATE_ATTACHED || new_state == RSD_NCM_INTERFACE_STATE_ADDRESSED || new_state == RSD_NCM_INTERFACE_STATE_DETACHED\" -> %lld"
- "assertion failure: \"new_state == RSD_NCM_INTERFACE_STATE_ATTACHED || new_state == RSD_NCM_INTERFACE_STATE_DETACHED\" -> %lld"
- "assertion failure: \"notification\" -> %lld"
- "assertion failure: \"nw_endpoint_copy_interface(endpoint)\" -> %lld"
- "assertion failure: \"nw_endpoint_get_type(browsed_endpoint) == nw_endpoint_type_bonjour_service\" -> %lld"
- "assertion failure: \"nw_endpoint_get_type(remote_endpoint) == nw_endpoint_type_address\" -> %lld"
- "assertion failure: \"nwconn\" -> %lld"
- "assertion failure: \"option->connection_timeout > 0\" -> %lld"
- "assertion failure: \"parent_matching_dict\" -> %lld"
- "assertion failure: \"parent_property_matching_dict\" -> %lld"
- "assertion failure: \"path_interface\" -> %lld"
- "assertion failure: \"payload_data\" -> %lld"
- "assertion failure: \"reflector_conn != ((void *)0)\" -> %lld"
- "assertion failure: \"remoted_queue\" -> %lld"
- "assertion failure: \"reply\" -> %lld"
- "assertion failure: \"required_ent\" -> %lld"
- "assertion failure: \"result\" -> %lld"
- "assertion failure: \"sa\" -> %lld"
- "assertion failure: \"self->_canceled\" -> %lld"
- "assertion failure: \"self.address_endpoint\" -> %lld"
- "assertion failure: \"self.bonjour_endpoint\" -> %lld"
- "assertion failure: \"self.browser != ((void *)0)\" -> %lld"
- "assertion failure: \"self.browser == ((void *)0)\" -> %lld"
- "assertion failure: \"self.connection == ((void *)0)\" -> %lld"
- "assertion failure: \"self.device.state != REMOTED_DEVICE_STATE_GONE\" -> %lld"
- "assertion failure: \"self.endpoint\" -> %lld"
- "assertion failure: \"self.public_properties != ((void *)0)\" -> %lld"
- "assertion failure: \"self.type != REMOTE_DEVICE_TYPE_INVALID_OR_UNKNOWN\" -> %lld"
- "assertion failure: \"service != ((void *)0)\" -> %lld"
- "assertion failure: \"service\" -> %lld"
- "assertion failure: \"service_len > 0 && service_len < 64\" -> %lld"
- "assertion failure: \"service_name\" -> %lld"
- "assertion failure: \"sntp_request_payload\" -> %lld"
- "assertion failure: \"sntp_response_payload\" -> %lld"
- "assertion failure: \"str != ((void *)0)\" -> %lld"
- "assertion failure: \"success\" -> %lld"
- "assertion failure: \"tmp\" -> %lld"
- "assertion failure: \"xpc_get_type(clientMessage) == (&_xpc_type_dictionary)\" -> %lld"
- "assertion failure: \"xpcconn\" -> %lld"

```
