## remoted

> `/usr/libexec/remoted`

```diff

-172.80.4.0.0
-  __TEXT.__text: 0x445dc
-  __TEXT.__auth_stubs: 0x17e0
-  __TEXT.__objc_stubs: 0x2280
-  __TEXT.__objc_methlist: 0x1420
-  __TEXT.__const: 0x21a
-  __TEXT.__oslogstring: 0x8894
-  __TEXT.__cstring: 0x216c
-  __TEXT.__objc_methname: 0x2324
+172.100.9.0.0
+  __TEXT.__text: 0x45cc0
+  __TEXT.__auth_stubs: 0x17f0
+  __TEXT.__objc_stubs: 0x22e0
+  __TEXT.__objc_methlist: 0x1468
+  __TEXT.__const: 0x202
+  __TEXT.__oslogstring: 0x88a6
+  __TEXT.__cstring: 0x2250
+  __TEXT.__objc_methname: 0x2375
   __TEXT.__objc_classname: 0x2a7
-  __TEXT.__objc_methtype: 0x71b
-  __TEXT.__gcc_except_tab: 0x1564
-  __TEXT.__unwind_info: 0xe30
-  __DATA_CONST.__auth_got: 0xc00
+  __TEXT.__objc_methtype: 0x71e
+  __TEXT.__gcc_except_tab: 0x14bc
+  __TEXT.__unwind_info: 0xef0
+  __DATA_CONST.__auth_got: 0xc08
   __DATA_CONST.__got: 0x228
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1618
-  __DATA_CONST.__cfstring: 0xc40
+  __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x2530
-  __DATA.__objc_selrefs: 0x8d8
-  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_const: 0x2590
+  __DATA.__objc_selrefs: 0x8f0
+  __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0x6a0
   __DATA.__bss: 0x3aa

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10C533A5-2CA6-3874-8D2B-66686588222F
-  Functions: 1343
-  Symbols:   486
-  CStrings:  1890
+  UUID: 1C593D99-F98E-3022-BFD9-FF6A12D10DE4
+  Functions: 1398
+  Symbols:   488
+  CStrings:  1906
 
Symbols:
+ _NSUnderlyingErrorKey
+ _strrchr
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RemoteServiceDiscovery_executables/remoted/modules/identity.m"
+ "FileName"
+ "FunctionName"
+ "IPV6Address"
+ "LineNumber"
+ "SCRT root CA auth failed with error: %{public}@"
+ "Tr*,R,N,V_ipv6_str"
+ "UCRT root CA auth failed with error: %{public}@"
+ "_ipv6_str"
+ "assertion failure: \"!(uuid_is_null(self->remote_device_uuid))\" -> %llu"
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
+ "assertion failure: \"advertise_descriptor\" -> %llu"
+ "assertion failure: \"answers != ((void*)0)\" -> %llu"
+ "assertion failure: \"asyncReply\" -> %llu"
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
+ "assertion failure: \"device\" -> %llu"
+ "assertion failure: \"device_name_map\" -> %llu"
+ "assertion failure: \"enabled_interface_name_cfstr\" -> %llu"
+ "assertion failure: \"endpoint\" -> %llu"
+ "assertion failure: \"endpoint_uuids\" -> %llu"
+ "assertion failure: \"entry\" -> %llu"
+ "assertion failure: \"eos_device_is_connected(&eos_is_connected)\" -> %llu"
+ "assertion failure: \"err\" -> %llu"
+ "assertion failure: \"error\" -> %llu"
+ "assertion failure: \"fd != -1\" -> %llu"
+ "assertion failure: \"if_index\" -> %llu"
+ "assertion failure: \"ifindex\" -> %llu"
+ "assertion failure: \"ifname\" -> %llu"
+ "assertion failure: \"interface\" -> %llu"
+ "assertion failure: \"interfaces\" -> %llu"
+ "assertion failure: \"key != ((void*)0)\" -> %llu"
+ "assertion failure: \"key_string != ((void*)0)\" -> %llu"
+ "assertion failure: \"listener_source\" -> %llu"
+ "assertion failure: \"local_conn != ((void*)0)\" -> %llu"
+ "assertion failure: \"local_rsd_device.multiverse_device == ((void*)0)\" -> %llu"
+ "assertion failure: \"local_rsd_device.multiverse_device == device\" -> %llu"
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
+ "assertion failure: \"rawkeys != ((void*)0)\" -> %llu"
+ "assertion failure: \"reflector_conn != ((void*)0)\" -> %llu"
+ "assertion failure: \"remote_device != ((void*)0)\" -> %llu"
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
+ "assertion failure: \"sockfd != -1\" -> %llu"
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
- "assertion failure: \"advertise_descriptor\" -> %lld"
- "assertion failure: \"answers != ((void *)0)\" -> %lld"
- "assertion failure: \"asyncReply\" -> %lld"
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
- "assertion failure: \"device\" -> %lld"
- "assertion failure: \"device_name_map\" -> %lld"
- "assertion failure: \"enabled_interface_name_cfstr\" -> %lld"
- "assertion failure: \"endpoint\" -> %lld"
- "assertion failure: \"endpoint_uuids\" -> %lld"
- "assertion failure: \"entry\" -> %lld"
- "assertion failure: \"eos_device_is_connected(&eos_is_connected)\" -> %lld"
- "assertion failure: \"err\" -> %lld"
- "assertion failure: \"error\" -> %lld"
- "assertion failure: \"fd != -1\" -> %lld"
- "assertion failure: \"if_index\" -> %lld"
- "assertion failure: \"ifindex\" -> %lld"
- "assertion failure: \"ifname\" -> %lld"
- "assertion failure: \"interface\" -> %lld"
- "assertion failure: \"interfaces\" -> %lld"
- "assertion failure: \"key != ((void *)0)\" -> %lld"
- "assertion failure: \"key_string != ((void *)0)\" -> %lld"
- "assertion failure: \"listener_source\" -> %lld"
- "assertion failure: \"local_conn != ((void *)0)\" -> %lld"
- "assertion failure: \"local_rsd_device.multiverse_device == ((void *)0)\" -> %lld"
- "assertion failure: \"local_rsd_device.multiverse_device == device\" -> %lld"
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
- "assertion failure: \"rawkeys != ((void *)0)\" -> %lld"
- "assertion failure: \"reflector_conn != ((void *)0)\" -> %lld"
- "assertion failure: \"remote_device != ((void *)0)\" -> %lld"
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
- "assertion failure: \"sockfd != -1\" -> %lld"
- "assertion failure: \"str != ((void *)0)\" -> %lld"
- "assertion failure: \"success\" -> %lld"
- "assertion failure: \"tmp\" -> %lld"
- "assertion failure: \"xpc_get_type(clientMessage) == (&_xpc_type_dictionary)\" -> %lld"
- "assertion failure: \"xpcconn\" -> %lld"

```
