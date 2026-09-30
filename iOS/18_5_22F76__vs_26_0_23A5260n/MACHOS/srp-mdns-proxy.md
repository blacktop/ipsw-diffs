## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2600.120.12.0.0
-  __TEXT.__text: 0x73078
-  __TEXT.__auth_stubs: 0x1270
-  __TEXT.__const: 0x1fb
-  __TEXT.__cstring: 0x69de
-  __TEXT.__oslogstring: 0xfa68
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x4f0
-  __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x938
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x820
+2862.0.0.0.1
+  __TEXT.__text: 0x824a0
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_stubs: 0x180
+  __TEXT.__objc_methlist: 0x21c
+  __TEXT.__const: 0x282
+  __TEXT.__cstring: 0x75ea
+  __TEXT.__oslogstring: 0x11be9
+  __TEXT.__objc_classname: 0x38
+  __TEXT.__objc_methname: 0x4e6
+  __TEXT.__objc_methtype: 0x237
+  __TEXT.__unwind_info: 0x578
+  __DATA_CONST.__auth_got: 0x9b0
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x1c8
-  __DATA.__bss: 0x7e0
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x2c8
+  __DATA.__objc_selrefs: 0x180
+  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x818
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/IPConfiguration.framework/IPConfiguration
+  - /System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay
   - /System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
-  UUID: 8133B740-22ED-318E-B70E-B5605786BFA2
-  Functions: 395
-  Symbols:   990
-  CStrings:  2109
+  - /usr/lib/libobjc.A.dylib
+  UUID: 94207CAA-A855-37C7-8C9B-43787362EFE6
+  Functions: 450
+  Symbols:   1124
+  CStrings:  2439
 
Symbols:
+ -[NRDeviceMonitorObjc .cxx_destruct]
+ -[NRDeviceMonitorObjc callback]
+ -[NRDeviceMonitorObjc deviceIsAsleepDidChange:isAsleep:]
+ -[NRDeviceMonitorObjc initWithDeviceIdentifier:callback:queue:]
+ -[NRDeviceMonitorObjc isAsleep]
+ -[NRDeviceMonitorObjc monitor]
+ -[NRDeviceMonitorObjc setCallback:]
+ -[NRDeviceMonitorObjc setMonitor:]
+ OBJC_IVAR_$_NRDeviceMonitorObjc._callback
+ OBJC_IVAR_$_NRDeviceMonitorObjc._monitor
+ _OBJC_CLASS_$_NRDeviceIdentifier
+ _OBJC_CLASS_$_NRDeviceMonitor
+ _OBJC_CLASS_$_NRDeviceMonitorObjc
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_PDRRegistry
+ _OBJC_METACLASS_$_NRDeviceMonitorObjc
+ _OBJC_METACLASS_$_NSObject
+ __Block_object_dispose
+ __OBJC_$_INSTANCE_METHODS_NRDeviceMonitorObjc
+ __OBJC_$_INSTANCE_VARIABLES_NRDeviceMonitorObjc
+ __OBJC_$_PROP_LIST_NRDeviceMonitorObjc
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NRDeviceMonitorDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NRDeviceMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_NRDeviceMonitorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_NRDeviceMonitorObjc
+ __OBJC_CLASS_RO_$_NRDeviceMonitorObjc
+ __OBJC_LABEL_PROTOCOL_$_NRDeviceMonitorDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_NRDeviceMonitorObjc
+ __OBJC_PROTOCOL_$_NRDeviceMonitorDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ ___block_descriptor_40_e8_v12?0B8l
+ ___comm_configure_device_monitor_block_invoke
+ ___nr_device_monitor_set_handler_block_invoke
+ __block_descriptor_tmp.106
+ __block_descriptor_tmp.109
+ __block_descriptor_tmp.112
+ __block_descriptor_tmp.115
+ __block_descriptor_tmp.122
+ __block_descriptor_tmp.125
+ __block_descriptor_tmp.1334
+ __block_descriptor_tmp.17.1424
+ __block_descriptor_tmp.18.1518
+ __block_descriptor_tmp.190
+ __block_descriptor_tmp.2514
+ __block_descriptor_tmp.497
+ __block_descriptor_tmp.8.1381
+ __block_descriptor_tmp.89
+ __block_descriptor_tmp.91
+ __block_descriptor_tmp.96
+ __block_descriptor_tmp.98
+ __block_literal_global.1425
+ __block_literal_global.495
+ __cti_event_handler_block_invoke.124
+ __cti_log_object_block_invoke.104
+ __cti_log_object_block_invoke.95
+ __cti_log_object_block_invoke_2.107
+ __cti_log_object_block_invoke_2.97
+ __init_connection_block_invoke.84
+ __objc_empty_cache
+ _adv_ctl_get_host_service
+ _adv_ctl_thread_shutdown_status_check
+ _cti_get_netdata_from_thread_tlvs
+ _cti_get_netdata_mode_
+ _cti_get_rloc16_
+ _cti_internal_netdata_mode_reply_callback
+ _cti_internal_onmesh_prefix_reply_callback
+ _cti_internal_prefix_reply_callback
+ _cti_internal_thread_netdata_reply_callback
+ _cti_iterate_through_netdata
+ _cti_prefix_create_
+ _cti_prefix_created
+ _cti_prefix_finalized
+ _cti_prefix_vec_create_
+ _cti_prefix_vec_created
+ _cti_prefix_vec_finalize
+ _cti_prefix_vec_finalized
+ _cti_route_created
+ _cti_route_finalized
+ _cti_route_vec_created
+ _cti_route_vec_finalize
+ _cti_route_vec_finalized
+ _cti_service_vec_create_
+ _cti_track_network_data_
+ _dns_edns0_header_to_wire_
+ _dns_key_tag_compute
+ _dns_label_create_
+ _dns_message_rr_group_free
+ _dnssd_hardwired_add_or_remove_address_in_domain
+ _dnssd_hardwired_add_or_remove_ptr_in_domain
+ _dnssd_hardwired_add_or_remove_ptr_record
+ _dnssd_hardwired_lbdomains_setup
+ _dnssd_hardwired_remove_record
+ _dp_answer_free
+ _is_valid_address_to_publish
+ _network_data_tracker_callback
+ _node_type_tracker_callback_add
+ _nw_connection_copy_current_path
+ _nw_path_uses_interface_subtype
+ _objc_alloc
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend
+ _objc_msgSend$bluetoothIdentifier
+ _objc_msgSend$callback
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_msgSend$initWithDeviceIdentifier:callback:queue:
+ _objc_msgSend$initWithDeviceIdentifier:delegate:queue:
+ _objc_msgSend$initWithUUID:
+ _objc_msgSend$isAsleep
+ _objc_msgSend$monitor
+ _objc_msgSend$newDeviceIdentifierWithBluetoothUUID:
+ _objc_msgSend$setCallback:
+ _objc_msgSend$setMonitor:
+ _objc_msgSend$sharedInstance
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x8
+ _objc_retainBlock
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
+ _objc_storeStrong
+ _old_cti_prefix_created
+ _old_cti_prefix_finalized
+ _old_cti_prefix_vec_created
+ _old_cti_prefix_vec_finalized
+ _old_cti_route_created
+ _old_cti_route_finalized
+ _old_cti_route_vec_created
+ _old_cti_route_vec_finalized
+ _old_omr_prefix_created
+ _old_omr_prefix_finalized
+ _old_omr_watcher_created
+ _old_omr_watcher_finalized
+ _omr_prefix_created
+ _omr_prefix_finalized
+ _omr_watcher_created
+ _omr_watcher_finalize
+ _omr_watcher_finalized
+ _omr_watcher_netdata_callback
+ _omr_watcher_netdata_mode_callback
+ _omr_watcher_onmesh_prefix_list_callback
+ _omr_watcher_onmesh_prefix_list_fetch
+ _omr_watcher_onmesh_prefixes_update
+ _omr_watcher_prefix_recheck_wakeup
+ _omr_watcher_route_update_callback
+ _omr_watcher_wakeup_release
+ _service_publisher_action_unpublishing_stale_service
+ _service_publisher_anycast_service_present
+ _service_publisher_deliver_event_to_all_publishers
+ _service_publisher_stale_service_present
+ _service_publisher_start_wait
+ _service_publisher_stop_publishing
+ _service_tracker_netdata_mode_callback
+ _srp_dns_evaluate
+ _srpk_decompress_instance_labels
+ _srpk_full_name_from_wire
+ _srpk_hostname_to_wire
+ _srpk_integer_from_wire_max_
+ _srpk_label_cache_
+ _srpk_label_from_wire_
+ _srpk_name_to_wire
+ _srpk_space_
+ _strtok_r
+ _thread_device_active_data_set_changed_callback
+ _thread_device_get_mesh_local_address_callback
+ _thread_device_neighbor_callback
+ _thread_device_node_type_callback
+ _thread_device_thread_tracker_callback
+ _thread_device_tunnel_name_callback
+ _thread_device_wed_callback
+ _thread_netdata_decode_tlv_with_entries
+ _thread_netdata_tlv_iterator_next
+ _thread_service_equal
+ _xpc_array_get_dictionary
- _OUTLINED_FUNCTION_0
- __MergedGlobals
- ___isPlatformVersionAtLeast
- __availability_version_check
- __block_descriptor_tmp.102
- __block_descriptor_tmp.105
- __block_descriptor_tmp.1107
- __block_descriptor_tmp.111
- __block_descriptor_tmp.113
- __block_descriptor_tmp.118
- __block_descriptor_tmp.121
- __block_descriptor_tmp.17.1211
- __block_descriptor_tmp.18.1312
- __block_descriptor_tmp.191
- __block_descriptor_tmp.501
- __block_descriptor_tmp.8.1152
- __block_descriptor_tmp.81
- __block_descriptor_tmp.87
- __block_descriptor_tmp.90
- __block_descriptor_tmp.92
- __block_literal_global.1212
- __block_literal_global.499
- __cti_event_handler_block_invoke.120
- __cti_log_object_block_invoke.100
- __cti_log_object_block_invoke.91
- __cti_log_object_block_invoke_2.103
- __cti_log_object_block_invoke_2.93
- __init_connection_block_invoke.80
- __initializeAvailabilityCheck
- __isPlatformVersionAtLeast.cold.1
- __isPlatformVersionAtLeast.cold.2
- _compatibilityInitializeAvailabilityCheck
- _cti_add_ml_eid_mapping_
- _dispatch_once_f
- _dlsym
- _dns_opt_parse
- _dp_question_answers_free
- _fclose
- _fopen
- _fread
- _fseek
- _ftell
- _initializeAvailabilityCheck
- _malloc
- _put_tlv_uint32
- _rewind
- _service_publisher_active_data_set_changed_callback
- _service_publisher_get_mesh_local_address_callback
- _service_publisher_have_anycast_service
- _service_publisher_neighbor_callback
- _service_publisher_thread_tracker_callback
- _service_publisher_tunnel_name_callback
- _service_publisher_unpublish_stale_service
- _service_publisher_wed_callback
- _sscanf
- _strlcpy
CStrings:
+ " (ncp)"
+ " (stable)"
+ " (user)"
+ " / blocked"
+ " / no listener address"
+ "#16@0:8"
+ "%{public}s: %{private, mask.hash}s: host TTL provided when there are no address records."
+ "%{public}s: %{private, mask.hash}s: malformed host ttl"
+ "%{public}s: %{private, mask.hash}s: malformed key ttl"
+ "%{public}s: %{public}s %x"
+ "%{public}s: %{public}s %{public}s%{private, mask.hash}s IN AAAA {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}"
+ "%{public}s: %{public}s %{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s"
+ "%{public}s: %{public}s PTR from %{private, mask.hash}s to %{private, mask.hash}s"
+ "%{public}s: %{public}s all needed services present -> false"
+ "%{public}s: %{public}s anycast SRP service on RLOC16 %x with sequence number %02x %{public}s"
+ "%{public}s: %{public}s apple anycast service on RLOC16 %x %{public}s"
+ "%{public}s: %{public}s cti_add_service failed: %d"
+ "%{public}s: %{public}s cti_remove_service failed: %d"
+ "%{public}s: %{public}s failed to setup SRP listener"
+ "%{public}s: %{public}s have_srp_listener is true but there's no listener!"
+ "%{public}s: %{public}s header setup failed"
+ "%{public}s: %{public}s is in net data"
+ "%{public}s: %{public}s is not in net data"
+ "%{public}s: %{public}s listener address should not be NULL here."
+ "%{public}s: %{public}s listener still present"
+ "%{public}s: %{public}s no listener address where there must be a listener address"
+ "%{public}s: %{public}s no listener address."
+ "%{public}s: %{public}s no pending service update"
+ "%{public}s: %{public}s published service still present: %p"
+ "%{public}s: %{public}s publisher is in an invalid state, so we shouldn't re-advertise anything."
+ "%{public}s: %{public}s request to unpublished service that's not present"
+ "%{public}s: %{public}s service %{private, mask.hash}s.%{private, mask.hash}s host not present -> true"
+ "%{public}s: %{public}s service %{private, mask.hash}s.%{private, mask.hash}s is present"
+ "%{public}s: %{public}s service still published!"
+ "%{public}s: %{public}s setting seen_service_list to false"
+ "%{public}s: %{public}s setting seen_service_list to true"
+ "%{public}s: %{public}s srp service %{private, mask.hash}s.%{private, mask.hash}s present as %{private, mask.hash}s but has no address on local mesh -> true"
+ "%{public}s: %{public}s srp service %{private, mask.hash}s.%{private, mask.hash}s present but no addresses -> true"
+ "%{public}s: %{public}s srp_service_needed == true -> true"
+ "%{public}s: %{public}s startup timeout"
+ "%{public}s: %{public}s the queue is empty."
+ "%{public}s: %{public}s there is a pending update at the head of the queue."
+ "%{public}s: %{public}s unadvertising %{private, mask.hash}s IN AAAA {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P} rec %p rref %p"
+ "%{public}s: %{public}s unadvertising %{private, mask.hash}s.%{private, mask.hash}s instance %p sdref %p"
+ "%{public}s: %{public}s unicast SRP service {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}%%%d, rloc16 %x %{public}s"
+ "%{public}s: %{public}s unsupported service type %d"
+ "%{public}s: %{public}s:%d: missing back pointer %llu (between %llu and %llu) doesn't point to a label."
+ "%{public}s: %{public}s:%d: unrecognized direct abbreviation %x"
+ "%{public}s: 6LoWPAN ID TLV value must be exactly 2 bytes long (was %lu bytes long)"
+ "%{public}s: Adding a special 0-length rdata response for DSO, possibly a removing update"
+ "%{public}s: Client uid %d pid %d sent a kDNSSDAdvertisingProxyGetHostService request."
+ "%{public}s: Context ID %d present but no prefixes"
+ "%{public}s: Could not store all prefixes in prefix vector."
+ "%{public}s: Could not store all routes in route vector."
+ "%{public}s: Could not store all services in service vector."
+ "%{public}s: Cound not decode Thread version (recieved version was %d)"
+ "%{public}s: Domain %{private, mask.hash}s has no interface"
+ "%{public}s: Failed to find my_name domain - my_name: %{private, mask.hash}s"
+ "%{public}s: Failed to find thread domain - domain: %{public}s"
+ "%{public}s: Failed to get my_name and unable to set hardwired response"
+ "%{public}s: Failed to get path information when checking the sleep suspension"
+ "%{public}s: Found Service entry in Thread network data"
+ "%{public}s: Got offmesh route {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P} len %d nat64:%{public}s stable:%{public}s preference:%d rloc:0x%04x next_hop_is_host:%{public}s"
+ "%{public}s: Got prefix (%{public}s) {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P} len %d stable:%{public}s flags:0x%04x metric:%d rloc:0x%04x"
+ "%{public}s: Got service id:%d enterprise_number:%llu (type:%d version:%d) rloc:0x%04x service_data_length:%zu server_data_length:%zu"
+ "%{public}s: Ignoring Thread TLV of type %d"
+ "%{public}s: Interface %{public}s"
+ "%{public}s: Invalid prefixes array %zu subdictionary %zu: no key"
+ "%{public}s: Invalid service data: length = %u"
+ "%{public}s: Need %lx, have %lx: no space in transaction at %{public}s:%d"
+ "%{public}s: No callback available for monitor."
+ "%{public}s: No device found for monitor."
+ "%{public}s: No memory for message!"
+ "%{public}s: No running queue available for monitor."
+ "%{public}s: Non IPv4/IPv6 address added for the interface - sa_family: %u"
+ "%{public}s: Non IPv4/IPv6 address in interface addresses - sa_family: %u"
+ "%{public}s: Received invalid network data length (was %lu, but the maximum allowed is %d)"
+ "%{public}s: Server TLV value must be at least 2 bytes long (was %u bytes long)"
+ "%{public}s: Skipping %{private, mask.hash}s"
+ "%{public}s: Skipping non IPv6/IPv4 address - addr:%{private, mask.hash}s"
+ "%{public}s: TLV of type %d is not supposed to be a TLV with entries"
+ "%{public}s: Unable to get prefix array %zu"
+ "%{public}s: Unexpected generative pattern type %d"
+ "%{public}s: Unknown dispatch byte %x"
+ "%{public}s: Unknown key in prefix array %zu subdictionary %zu: %{public}s"
+ "%{public}s: Unsupported signature type: %d"
+ "%{public}s: Watch sleeps soon."
+ "%{public}s: Watch wakes up."
+ "%{public}s: [CX%d] \"value\" field not present in Thread NetworkData reply"
+ "%{public}s: [CX%d] Not calling callback for %p"
+ "%{public}s: [CX%d] Not calling callback."
+ "%{public}s: [CX%d] got a response for thread network data"
+ "%{public}s: [DSO%u->Qu%d] Push query has pending updates through DSO session, sending updates now"
+ "%{public}s: [DSO%u->Qu%d] Removing all possibly expired records then adding all cached records -- qname: %{private, mask.hash}s, qtype: %{public}s"
+ "%{public}s: [Q%d][QU%d] adding zero-length DSO response for %{private, mask.hash}s %{public}s %d"
+ "%{public}s: [Q%d][QU%d] rdata didn't parse!!"
+ "%{public}s: [ST%lld] could not start CTI request for netdata mode: %d"
+ "%{public}s: [ST%lld] got error status from CTI: %d"
+ "%{public}s: [ST%lld] netdata get started"
+ "%{public}s: [ST%lld] netdata mode get started"
+ "%{public}s: abbreviation: %{public}s"
+ "%{public}s: address is not eligible to construct PTR record"
+ "%{public}s: adv_xpc_get_host_service: Unable to create reply dictionary."
+ "%{public}s: back pointer match"
+ "%{public}s: back pointer missing for label pointer"
+ "%{public}s: bogus prefix length provided by thread: %{public}s"
+ "%{public}s: can't create unicast service publisher."
+ "%{public}s: can't get onmesh prefix list: %d"
+ "%{public}s: can't get prefix_array %zu subdictionary %zu"
+ "%{public}s: cannot find/create new served domain"
+ "%{public}s: cannot start omr_watcher without knowing the netdata API mode"
+ "%{public}s: cannot start service_tracker without knowing the netdata API mode"
+ "%{public}s: comm_t object has NULL nw_connection object."
+ "%{public}s: could not add node_type_tracker_callback"
+ "%{public}s: could not add thread_tracker_callback"
+ "%{public}s: could not decode TLV of type %s, status code: %d"
+ "%{public}s: could not find served domain with the specified domain name - domain name: %{private, mask.hash}s"
+ "%{public}s: could not get the Thread netdata information from the TLV iterator: %d"
+ "%{public}s: could not get the next TLV from iterator: %d"
+ "%{public}s: could not get the next sub-TLV from sub-tlv iterator: %d"
+ "%{public}s: could not get the number of onmesh prefixes from the Thread netdata iterator: %d"
+ "%{public}s: could not init the Prefix TLV's sub-TLV iterator"
+ "%{public}s: could not initialize Thread netdata iterator: status %d"
+ "%{public}s: could not parse border_router TLV entry: error code %d"
+ "%{public}s: could not parse has_route TLV entry: error code %d"
+ "%{public}s: could not start a CTI request for getting Thread services, got status: %d"
+ "%{public}s: could not try to get a 6LoWPAN sub-TLV from sub-tlv iterator: %d"
+ "%{public}s: decoded %s TLV, length: %lu"
+ "%{public}s: dispatch: %x"
+ "%{public}s: double callback"
+ "%{public}s: expecting %d sub-dictionaries to prefix array %zu, but got %d."
+ "%{public}s: expecting flags rather than %{private, mask.hash}s at %d"
+ "%{public}s: expecting origin rather than %{private, mask.hash}s at %d"
+ "%{public}s: expecting prefix_len rather than %{private, mask.hash}s at %d"
+ "%{public}s: expecting rloc rather than %{private, mask.hash}s at %d"
+ "%{public}s: expecting table rather than %{private, mask.hash}s at %d"
+ "%{public}s: failed to %{public}s address record - domain name: %{private, mask.hash}s"
+ "%{public}s: failed to allocate addresses array for %{private, mask.hash}s"
+ "%{public}s: failed to allocate instance dictionary for %{private, mask.hash}s"
+ "%{public}s: failed to allocate instances array for %{private, mask.hash}s"
+ "%{public}s: failed to update address record for domain - domain: %{private, mask.hash}s"
+ "%{public}s: failed to update address record for domain - domain: %{public}s"
+ "%{public}s: falling through"
+ "%{public}s: found 6LoWPAN context ID: %d, compression allowed = %d"
+ "%{public}s: found Prefix entry in Thread network data"
+ "%{public}s: got %lu bytes of network data"
+ "%{public}s: got an error status when getting the network data mode: %d"
+ "%{public}s: got error status from cti_get_rloc16: %d"
+ "%{public}s: got error status when getting netdata mode: %d"
+ "%{public}s: got null prefixes from netdata callback"
+ "%{public}s: got prefix {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P} len %d origin:%{public}s stable:%{public}s flags:%x rloc:%04x"
+ "%{public}s: ignore Thread sub-TLV of type %d inside Prefix TLV"
+ "%{public}s: ignoring the address for interface - address: %{private, mask.hash, network:in_addr}.4P, address type: %{public}s."
+ "%{public}s: ignoring the address for interface - address: %{public}s%{private, mask.hash, network:in6_addr}.16P, address type: %{public}s."
+ "%{public}s: invalid ipv6 address %{private, mask.hash}s"
+ "%{public}s: invalid ipv6 address %{public}s"
+ "%{public}s: invalid prefix context id %d"
+ "%{public}s: length > 63 (%llu) at %d"
+ "%{public}s: literal label"
+ "%{public}s: literal txt record"
+ "%{public}s: no match."
+ "%{public}s: no matching hardwired_t found - record name: %{public}s, record type: %d"
+ "%{public}s: no permit list when removing %{public}s"
+ "%{public}s: not enough space in the TLV buffer to contain the %u bytes of service data"
+ "%{public}s: not present"
+ "%{public}s: null address"
+ "%{public}s: omw->prefixes = %p"
+ "%{public}s: onmesh prefix array not present in Thread:OnMeshPrefixes event."
+ "%{public}s: pointer to label: %x"
+ "%{public}s: prefix TLV payload cannot contain the IPv6 prefix of length %d (%d bytes) (only %lu bytes remaining)"
+ "%{public}s: prefix TLV payload must be at least 2 bytes long (was %u bytes long)"
+ "%{public}s: prefix TLV's prefix length is too large to fit in an IPv6 address (prefix is %d bits / %d bytes long)"
+ "%{public}s: prefix {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}/%d has 6LoWPAN context: id = %d"
+ "%{public}s: prefix {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}/%d is currently in the list %{public}s%{public}s%{public}s"
+ "%{public}s: prefix {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}/%d is in thread-supplied prefix list"
+ "%{public}s: prefix {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}/%d is not on-mesh, skipping"
+ "%{public}s: prefix {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}/%d showed up%{public}s%{public}s%{public}s"
+ "%{public}s: prefix {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}/%d went away%{public}s%{public}s%{public}s"
+ "%{public}s: prefixes array %zu: Address appears twice."
+ "%{public}s: prefixes array %zu: Metric appears twice."
+ "%{public}s: prefixes array %zu: destination is longer than maximum IPv6 address string: %{public}s"
+ "%{public}s: prefixes array not present in IPv6:Routes event."
+ "%{public}s: prefixes expected to be refreshed were not."
+ "%{public}s: prefixes: %p  count: %d"
+ "%{public}s: present"
+ "%{public}s: rdlen = %zd  tag = %x"
+ "%{public}s: received a message marked compressed that we could not decompress"
+ "%{public}s: received an empty array in the Thread NetworkData reply"
+ "%{public}s: received reserved route preference, defaulting to low"
+ "%{public}s: received thread version %d"
+ "%{public}s: response array does not have the required format (entry 0 should be a dictionary)"
+ "%{public}s: response array does not have the required format (entry 2 should be a dictionary)"
+ "%{public}s: response array does not have the required format (entry 3 should be a dictionary)"
+ "%{public}s: response array does not have the required format (should have exactly 4 entries)"
+ "%{public}s: result %d"
+ "%{public}s: resulting label is %{private, mask.hash}s"
+ "%{public}s: rv = %llu  byte = %llx  mask = %x"
+ "%{public}s: s_id = %d"
+ "%{public}s: service TLV value must be at least 2 bytes long (was %u bytes long)"
+ "%{public}s: service TLV value must be at least 6 bytes long (was %u bytes long)"
+ "%{public}s: skipping address type other than IPv4/IPv6 - type: %u"
+ "%{public}s: snprintf truncates the string - bytes_written: %d, limit: %zd"
+ "%{public}s: snprintf truncates the string - name length: %zu, domain length: %zu, buffer length: %zu"
+ "%{public}s: status: %d"
+ "%{public}s: strdup() failed"
+ "%{public}s: strict allocator failed"
+ "%{public}s: strict_calloc called with count 0"
+ "%{public}s: strict_calloc called with size 0"
+ "%{public}s: strict_calloc count * size would overflow"
+ "%{public}s: strict_calloc(%zu, %zu) failed"
+ "%{public}s: strict_malloc called with size 0"
+ "%{public}s: strict_strdup called with NULL string"
+ "%{public}s: strict_strlcpy called with NULL dst"
+ "%{public}s: strict_strlcpy called with NULL src"
+ "%{public}s: the provided buffer length is smaller than the decoded TLV length"
+ "%{public}s: txt record back pointer is not to a txt record."
+ "%{public}s: txt record back-pointer offset: %u %llu"
+ "%{public}s: unable to create shared connection for registration: %d"
+ "%{public}s: unexpected boolean state: %{private, mask.hash}s"
+ "%{public}s: unexpected origin: %{private, mask.hash}s"
+ "%{public}s: unhandled error %d"
+ "%{public}s: wrong response format: array entry 0 should contain thread data version"
+ "%{public}s: wrong response format: array entry 2 should contain network data version"
+ "%{public}s: wrong response format: array entry 3 should contain network data"
+ "%{public}s: wrong response format: network data should be an array of u8"
+ "%{public}s: wrong response format: network data should be of \"RAW\" type."
+ ".%u.%u.%u.%u"
+ ".%x"
+ ".cxx_destruct"
+ "/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/omr-watcher.c"
+ "/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/srp-decompress.c"
+ "00:42:26"
+ "6lowpan_id"
+ "@\"NRDeviceMonitor\""
+ "@\"NSString\"16@0:8"
+ "@16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@?24@32"
+ "@?"
+ "@?16@0:8"
+ "Addreess"
+ "Address"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "Current:Srp:NetdataMode"
+ "IPv6:Routes"
+ "May 25 2025"
+ "Metric"
+ "NRDeviceMonitorDelegate"
+ "NRDeviceMonitorObjc"
+ "NSObject"
+ "Q16@0:8"
+ "RAW"
+ "T#,R"
+ "T@\"NRDeviceMonitor\",&,N,V_monitor"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@?,C,N,V_callback"
+ "TQ,R"
+ "Thread:NetworkData"
+ "Thread:OnMeshPrefixes"
+ "Vv16@0:8"
+ "[SP%lld %s]"
+ "^{_NSZone=}16@0:8"
+ "_callback"
+ "_hap"
+ "_matterc"
+ "_matterd"
+ "_monitor"
+ "_strict_strlcpy"
+ "_tcp"
+ "_udp"
+ "aThreadVersion"
+ "aType"
+ "aVersion"
+ "adding"
+ "address"
+ "adv_ctl_get_host_service"
+ "autorelease"
+ "bluetoothIdentifier"
+ "border_router"
+ "callback"
+ "class"
+ "comm_configure_device_monitor_block_invoke"
+ "commissioning_data"
+ "conformsToProtocol:"
+ "continue apple service"
+ "cti_extract_thread_network_data_reply"
+ "cti_get_netdata_from_thread_tlvs"
+ "cti_get_onmesh_prefix_list_"
+ "cti_internal_netdata_mode_reply_callback"
+ "cti_internal_onmesh_prefix_reply_callback"
+ "cti_internal_prefix_reply_callback"
+ "cti_internal_thread_netdata_reply_callback"
+ "cti_iterate_through_netdata"
+ "cti_parse_onmesh_prefix_array"
+ "cti_parse_prefixes_array"
+ "cti_prefix_create_"
+ "cti_prefix_vec_create_"
+ "cti_prefix_vec_finalize"
+ "cti_prefix_vec_release_"
+ "cti_prefix_vec_retain_"
+ "cti_route_create_"
+ "cti_route_create_from_tlv"
+ "cti_route_vec_create_"
+ "cti_route_vec_finalize"
+ "cti_service_create_from_tlv"
+ "cti_track_network_data_"
+ "cti_xpc_copy_description"
+ "debugDescription"
+ "description"
+ "deviceHasUnpairedBluetooth:"
+ "deviceInfoDidChange:deviceInfo:"
+ "deviceIsAsleepDidChange:isAsleep:"
+ "deviceIsClassCConnectedDidChange:isClassCConnected:"
+ "deviceIsCloudConnectedDidChange:isCloudConnected:"
+ "deviceIsConnectedDidChange:isConnected:"
+ "deviceIsEnabledDidChange:isEnabled:"
+ "deviceIsNearbyDidChange:isNearby:"
+ "deviceIsRegisteredDidChange:isRegistered:"
+ "deviceLinkTypeDidChange:linkType:"
+ "deviceLinkTypeDidChange:linkType:linkSubtype:"
+ "devicePluggedInStateDidChange:pluggedIn:"
+ "deviceProxyServiceInterfaceNameDidChange:interfaceName:"
+ "deviceThermalPressureLevelDidChange:thermalPressureLevel:"
+ "dns_key_tag_compute"
+ "dns_label_create_"
+ "dns_name_copy"
+ "dns_opt_parse"
+ "dns_pres_name_parse"
+ "dnssd_hardwired_add_or_remove_address_in_domain"
+ "dnssd_hardwired_add_or_remove_ptr_in_domain"
+ "dnssd_hardwired_add_or_remove_ptr_record"
+ "dnssd_hardwired_generate_ptr_name"
+ "dnssd_hardwired_lbdomains_setup"
+ "dnssd_hardwired_process_addr_change"
+ "dnssd_hardwired_remove_record"
+ "dnssd_hardwired_setup"
+ "embiggen"
+ "error_code"
+ "flags:"
+ "get host service info"
+ "getActivePairedDeviceIncludingAltAccount"
+ "get_netdata_mode"
+ "get_onmesh_prefix_list"
+ "get_prefix_list"
+ "has_route"
+ "hash"
+ "host_name"
+ "in-addr.arpa."
+ "infra_state_changed"
+ "init"
+ "initWithDeviceIdentifier:callback:queue:"
+ "initWithDeviceIdentifier:delegate:queue:"
+ "initWithUUID:"
+ "instance_name"
+ "ioloop_comm_requires_sleep_suspension"
+ "ip6.arpa."
+ "is a competing service on an OMR prefix, so it wins."
+ "is not ours, and loses."
+ "is not ours, and wins."
+ "is on our rloc16 but is not our service, so it's stale."
+ "is on our rloc16 but we aren't publishing it, so it's stale."
+ "isAsleep"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "is_valid_address_to_publish"
+ "lease_time"
+ "link local"
+ "listener_address_changed"
+ "loopback"
+ "monitor"
+ "netdata.offmesh_routes"
+ "netdata.prefixes"
+ "netdata.services"
+ "newDeviceIdentifierWithBluetoothUUID:"
+ "no"
+ "normal label"
+ "nr_device_monitor_activate"
+ "nr_device_monitor_create"
+ "num_addresses"
+ "num_instances"
+ "offmesh"
+ "omr_prefix_create"
+ "omr_watcher_cancel"
+ "omr_watcher_create_"
+ "omr_watcher_finalize"
+ "omr_watcher_netdata_callback"
+ "omr_watcher_netdata_mode_callback"
+ "omr_watcher_onmesh_prefix_list_callback"
+ "omr_watcher_onmesh_prefix_list_fetch"
+ "omr_watcher_onmesh_prefixes_update"
+ "omr_watcher_prefix_recheck_wakeup"
+ "omr_watcher_release_"
+ "omr_watcher_route_update_callback"
+ "omr_watcher_start"
+ "omr_watcher_wakeup_release"
+ "onmesh"
+ "origin:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "prefix_len:"
+ "prefix_ret"
+ "prefixes"
+ "prefixes->prefixes[i]"
+ "re-advertise WED mle-id "
+ "re-advertise ml-eid "
+ "release"
+ "removing"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "rloc:"
+ "route_ret"
+ "routes"
+ "routes->routes[i]"
+ "self"
+ "server"
+ "service_publisher_action_unpublishing_stale_service"
+ "service_publisher_mesh_local_address_changed"
+ "service_tracker_netdata_mode_callback"
+ "service_type"
+ "setCallback:"
+ "setMonitor:"
+ "sharedInstance"
+ "srpk_decompress_host_block"
+ "srpk_decompress_service_add_block"
+ "srpk_decompress_txt_data"
+ "srpk_integer_from_wire_max_"
+ "srpk_label_cache_"
+ "srpk_label_from_wire_"
+ "srpk_message_decompress"
+ "srpk_space_"
+ "stable:"
+ "status_bitmap"
+ "stop apple service"
+ "stop_start"
+ "strict_strdup"
+ "superclass"
+ "thread_device_active_data_set_changed_callback"
+ "thread_device_get_mesh_local_address_callback"
+ "thread_device_neighbor_callback"
+ "thread_device_network_state_changed"
+ "thread_device_node_type_callback"
+ "thread_device_start_trackers"
+ "thread_device_thread_tracker_callback"
+ "thread_device_tunnel_name_callback"
+ "thread_device_wed_callback"
+ "thread_netdata_decode_6lowpan_id_payload"
+ "thread_netdata_decode_prefix_payload"
+ "thread_netdata_decode_server_payload"
+ "thread_netdata_decode_service_payload"
+ "thread_netdata_decode_tlv_with_entries"
+ "thread_netdata_tlv_iterator_next"
+ "track_thread_network_data"
+ "underline label"
+ "uni"
+ "unpublishing_stale_service"
+ "v12@?0B8"
+ "v16@0:8"
+ "v24@0:8@\"NRDeviceMonitor\"16"
+ "v24@0:8@16"
+ "v24@0:8@?16"
+ "v28@0:8@\"NRDeviceMonitor\"16B24"
+ "v28@0:8@\"NRDeviceMonitor\"16C24"
+ "v28@0:8@\"NRDeviceMonitor\"16i24"
+ "v28@0:8@16B24"
+ "v28@0:8@16C24"
+ "v28@0:8@16i24"
+ "v32@0:8@\"NRDeviceMonitor\"16@\"NRDeviceInfo\"24"
+ "v32@0:8@\"NRDeviceMonitor\"16@\"NSString\"24"
+ "v32@0:8@\"NRDeviceMonitor\"16C24C28"
+ "v32@0:8@16@24"
+ "v32@0:8@16C24C28"
+ "watcher"
+ "yes"
+ "zone"
- "%d.%d.%d"
- "%{public}s: %p: %{private, mask.hash}s: no memory for connection name."
- "%{public}s: %{public}s SRP service on RLOC16 %x with sequence number %02x %{public}s"
- "%{public}s: %{public}s SRP service {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}%%%d, rloc16 %x %{public}s"
- "%{public}s: %{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s"
- "%{public}s: %{public}s: no memory for return buffer"
- "%{public}s: No memory for connection"
- "%{public}s: No memory for connection name."
- "%{public}s: No memory for listener on %{private, mask.hash, network:in_addr}.4P#%d"
- "%{public}s: No memory for listener on <NULL>#%d"
- "%{public}s: No memory for listener on <family address other than AF_INET or AF_INET6: %d>#%d"
- "%{public}s: No memory for listener on {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}#%d"
- "%{public}s: No memory for prepared address"
- "%{public}s: Unable to allocate memory for query on %{private, mask.hash}s"
- "%{public}s: Unable to allocate memory for query response section on %{private, mask.hash}s"
- "%{public}s: Unable to allocate memory for question entry on %{private, mask.hash}s"
- "%{public}s: Unable to allocate served domain %s"
- "%{public}s: Unable to allocate served domain name %s"
- "%{public}s: Unable to allocate wakeup in order to re-attempt TLS listener creation."
- "%{public}s: Unable to allocate wakeup in order to set up TLS certificate rotation timer."
- "%{public}s: Unable to receive connection: no memory."
- "%{public}s: Unable to store service %lld %d %d: out of memory."
- "%{public}s: [C%d] %{private, mask.hash}s: no memory for a connection tracker object!"
- "%{public}s: [CX%d] no memory"
- "%{public}s: [Q%d] Unable to allocate memory for query response on %{private, mask.hash}s"
- "%{public}s: [Q%d][QU%d] rdata from mDNSResponder didn't parse!!"
- "%{public}s: [QU%d] strdup failed to copy the answer name: %{private, mask.hash}s"
- "%{public}s: [QU%d] unable to allocate memory for answer - name: %{private, mask.hash}s, rrtype: %{public}s, rrclass: %{public}s, rdlen: %u."
- "%{public}s: [ST%lld] %d"
- "%{public}s: [ST%lld] no memory"
- "%{public}s: [ST%lld] no memory for service."
- "%{public}s: [ST%lld] service list get failed: %d"
- "%{public}s: [TRK%d] no memory for idle timeout"
- "%{public}s: [TT%lld] no memory"
- "%{public}s: add_host_addr: no memory for record"
- "%{public}s: adv_instance:create: unable to allocate instance name."
- "%{public}s: adv_instance:create: unable to allocate instance type."
- "%{public}s: adv_instance:create: unable to allocate raw registration struct."
- "%{public}s: adv_instance:create: unable to allocate txt_data buffer"
- "%{public}s: adv_proxy_enable: unable to allocate srp_wanted structure."
- "%{public}s: all needed services present -> false"
- "%{public}s: calloc failed - allocated size: %lu"
- "%{public}s: calloc failed - allocated size: %zu"
- "%{public}s: calloc failed - name: %{private, mask.hash}s, allocate size: %lu"
- "%{public}s: can't allocate probe state wakeup"
- "%{public}s: can't create a wakeup to try to recover."
- "%{public}s: can't create connection dropper."
- "%{public}s: can't create node type tracker."
- "%{public}s: can't create service publisher."
- "%{public}s: can't create service tracker."
- "%{public}s: can't create thread tracker."
- "%{public}s: cti_add_service failed: %d"
- "%{public}s: cti_remove_service failed: %d"
- "%{public}s: dns_rdata_parse: no memory for TXT RR"
- "%{public}s: failed to create probe state"
- "%{public}s: failed to setup SRP listener"
- "%{public}s: have_srp_listener is true but there's no listener!"
- "%{public}s: ioloop_xpc_accept: no memory for xpc connection state."
- "%{public}s: listener still present"
- "%{public}s: malloc failed when allocating memory - for canonical_signer_name, len: %lu"
- "%{public}s: memory allocation for %u byte label (%.*s) failed.\n"
- "%{public}s: no memory"
- "%{public}s: no memory for %s %s"
- "%{public}s: no memory for add_addrs"
- "%{public}s: no memory for add_instances"
- "%{public}s: no memory for addresses"
- "%{public}s: no memory for advertisements"
- "%{public}s: no memory for base_type, comparison can't be done."
- "%{public}s: no memory for client ID"
- "%{public}s: no memory for client permitted interface list."
- "%{public}s: no memory for client update"
- "%{public}s: no memory for host address vector."
- "%{public}s: no memory for host data structure."
- "%{public}s: no memory for host instance vector."
- "%{public}s: no memory for host key."
- "%{public}s: no memory for hostname."
- "%{public}s: no memory for instance transaction."
- "%{public}s: no memory for key record"
- "%{public}s: no memory for listener name."
- "%{public}s: no memory for neighbor_ml_eid string!"
- "%{public}s: no memory for new_record"
- "%{public}s: no memory for new_record->rdata"
- "%{public}s: no memory for remove_addrs"
- "%{public}s: no memory for remove_instances"
- "%{public}s: no memory for renew_instances"
- "%{public}s: no memory for server ID"
- "%{public}s: no memory for server state"
- "%{public}s: no memory for srp_servers->object_allocation_stats_dump_wakeup"
- "%{public}s: no memory for update."
- "%{public}s: no memory for update_instances"
- "%{public}s: no memory for wake event on host"
- "%{public}s: no memory for wed_ext_address string!"
- "%{public}s: no memory for wed_ml_eid string!"
- "%{public}s: no memory to add permit for %{public}s"
- "%{public}s: no memory to allocate!"
- "%{public}s: no memory."
- "%{public}s: no pending service update"
- "%{public}s: prepare_update: no memory for add_instances"
- "%{public}s: published service still present: %p"
- "%{public}s: publisher is in an invalid state, so we shouldn't re-advertise anything."
- "%{public}s: re-advertising %{private, mask.hash}s IN AAAA {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}"
- "%{public}s: request to unpublished service that's not present"
- "%{public}s: service %{private, mask.hash}s.%{private, mask.hash}s host not present -> true"
- "%{public}s: service %{private, mask.hash}s.%{private, mask.hash}s is present"
- "%{public}s: setting seen_service_list to false"
- "%{public}s: setting seen_service_list to true"
- "%{public}s: srp service %{private, mask.hash}s.%{private, mask.hash}s present as %{private, mask.hash}s but has no address on local mesh -> true"
- "%{public}s: srp service %{private, mask.hash}s.%{private, mask.hash}s present but no addresses -> true"
- "%{public}s: srp_service_needed == true -> true"
- "%{public}s: startup timeout"
- "%{public}s: strdup failed to copy interface name - interface name: %{private, mask.hash}s"
- "%{public}s: the queue is empty."
- "%{public}s: there is a pending update at the head of the queue."
- "%{public}s: unable to allocate client state structure."
- "%{public}s: unable to allocate event to deliver"
- "%{public}s: unable to allocate memory for question name on %{private, mask.hash}s"
- "%{public}s: unable to create shared connection for registration."
- "%{public}s: unadvertising %{private, mask.hash}s IN AAAA {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P} rec %p rref %p"
- "%{public}s: unadvertising %{private, mask.hash}s.%{private, mask.hash}s instance %p sdref %p"
- "%{public}s: unicast service still published!"
- "%{public}s: unsupported service type %d"
- "%{public}s: wakeup timer alloc failed"
- "/System/Library/CoreServices/SystemVersion.plist"
- "06:56:14"
- "Apr 19 2025"
- "CFDataCreateWithBytesNoCopy"
- "CFDictionaryGetValue"
- "CFGetTypeID"
- "CFPropertyListCreateFromXMLData"
- "CFPropertyListCreateWithData"
- "CFRelease"
- "CFStringCreateWithCStringNoCopy"
- "CFStringGetCString"
- "CFStringGetTypeID"
- "ProductVersion"
- "Server data"
- "Service data"
- "[SP%lld]"
- "dp_start_dropping"
- "failed embiggen"
- "is a competing service."
- "is not ours and loses against ours."
- "is not ours and wins against ours."
- "kCFAllocatorNull"
- "new_question"
- "no memory for stale service to unpublish"
- "r"
- "service_publisher_active_data_set_changed_callback"
- "service_publisher_cancel"
- "service_publisher_get_mesh_local_address_callback"
- "service_publisher_neighbor_callback"
- "service_publisher_start"
- "service_publisher_thread_tracker_callback"
- "service_publisher_tunnel_name_callback"
- "service_publisher_wed_callback"

```
