## RemoteServiceDiscovery

> `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery`

```diff

-219.120.2.0.0
-  __TEXT.__text: 0xea68
-  __TEXT.__auth_stubs: 0xa80
+243.0.0.0.0
+  __TEXT.__text: 0xf558
   __TEXT.__objc_methlist: 0x4a0
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x136a
-  __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__oslogstring: 0x1d19
-  __TEXT.__unwind_info: 0x520
-  __TEXT.__objc_classname: 0xbe
-  __TEXT.__objc_methname: 0xa99
-  __TEXT.__objc_methtype: 0x1fb
-  __TEXT.__objc_stubs: 0x900
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x135c
+  __TEXT.__gcc_except_tab: 0x3c0
+  __TEXT.__oslogstring: 0x1d11
+  __TEXT.__unwind_info: 0x540
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x698
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x550
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0xd90
+  __AUTH_CONST.__auth_got: 0x610
   __AUTH.__objc_data: 0x28
   __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x60

   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DFD0788-47E9-321B-B2C7-C51CC3074DCA
-  Functions: 473
-  Symbols:   1473
-  CStrings:  538
+  UUID: EE92EACF-E64C-3129-A670-656C38CE7A63
+  Functions: 504
+  Symbols:   1526
+  CStrings:  356
 
Symbols:
+ GCC_except_table125
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table174
+ GCC_except_table211
+ GCC_except_table213
+ ____remote_device_browse_matching_common_block_invoke.389
+ ____remote_device_browse_matching_common_block_invoke.389.cold.1
+ ____remote_device_browse_matching_common_block_invoke.389.cold.2
+ ____remote_device_start_browsing_block_invoke.384
+ ____remote_device_start_browsing_block_invoke.384.cold.1
+ ____remote_service_accept_block_invoke.392
+ ____remote_service_connect_socket_impl_block_invoke.360
+ ___assert_rtn
+ ___block_literal_global.266
+ ___block_literal_global.291
+ ___block_literal_global.296
+ ___block_literal_global.299
+ ___block_literal_global.302
+ ___block_literal_global.305
+ ___block_literal_global.308
+ ___block_literal_global.311
+ ___block_literal_global.315
+ ___block_literal_global.342
+ ___block_literal_global.345
+ ___block_literal_global.365
+ ___block_literal_global.368
+ ___block_literal_global.371
+ ___block_literal_global.386
+ ___block_literal_global.395
+ ___darwin_check_fd_set_overflow
+ ___remote_device_create_from_client_description_block_invoke.373
+ ___remote_service_listen_with_device_block_invoke.272
+ ___udivti3
+ __remote_service_accept.cold.3
+ _clock_gettime
+ _connect
+ _exchange_from_payload
+ _exchange_from_payload.cold.1
+ _freeaddrinfo
+ _ftruncate
+ _getaddrinfo
+ _in6addr_any
+ _mmap
+ _munmap
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _recv
+ _recvfrom
+ _remote_device_legacy_timesync
+ _select
+ _send
+ _sendto
+ _snprintf
+ _sntp_calc_delay
+ _sntp_calc_error
+ _sntp_calc_mean
+ _sntp_calc_offset
+ _sntp_client_exchange
+ _sntp_client_process_response
+ _sntp_client_unicast
+ _sntp_client_unicast.cold.1
+ _sntp_clock_select
+ _sntp_datestamp_from_double
+ _sntp_datestamp_from_timespec
+ _sntp_datestamp_subsecs_to_nsec
+ _sntp_datestamp_to_double
+ _sntp_datestamp_to_nsec
+ _sntp_datestamp_to_timespec
+ _sntp_datestamp_to_timeval
+ _sntp_header_hton
+ _sntp_header_mmap
+ _sntp_header_ntoh
+ _sntp_header_unmap
+ _sntp_packet_hton
+ _sntp_packet_ntoh
+ _sntp_precision_decode
+ _sntp_server_exchange
+ _sntp_server_exchange.cold.1
+ _sntp_server_respond
+ _sntp_shortstamp_hton
+ _sntp_shortstamp_ntoh
+ _sntp_timestamp_from_datestamp
+ _sntp_timestamp_from_shortstamp
+ _sntp_timestamp_gettime
+ _sntp_timestamp_gettime.cold.1
+ _sntp_timestamp_hton
+ _sntp_timestamp_ntoh
+ _sntp_timestamp_to_datestamp
+ _sntp_timestamp_to_shortstamp
+ _umask
+ _warn
+ _write
+ _xpc_copy
+ _xpc_data_get_bytes
- GCC_except_table124
- GCC_except_table128
- GCC_except_table133
- GCC_except_table173
- GCC_except_table210
- GCC_except_table212
- GCC_except_table375
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- ____remote_device_browse_matching_common_block_invoke.388
- ____remote_device_browse_matching_common_block_invoke.388.cold.1
- ____remote_device_browse_matching_common_block_invoke.388.cold.2
- ____remote_device_start_browsing_block_invoke.383
- ____remote_device_start_browsing_block_invoke.383.cold.1
- ____remote_service_accept_block_invoke.391
- ____remote_service_connect_socket_impl_block_invoke.358
- ___block_literal_global.265
- ___block_literal_global.289
- ___block_literal_global.294
- ___block_literal_global.297
- ___block_literal_global.300
- ___block_literal_global.303
- ___block_literal_global.306
- ___block_literal_global.309
- ___block_literal_global.313
- ___block_literal_global.340
- ___block_literal_global.343
- ___block_literal_global.364
- ___block_literal_global.367
- ___block_literal_global.370
- ___block_literal_global.385
- ___block_literal_global.394
- ___remote_device_create_from_client_description_block_invoke.372
- ___remote_service_listen_with_device_block_invoke.270
- ___remote_service_listen_with_device_block_invoke_3.cold.3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _remote_device_timesync.cold.1
- _remote_device_timesync.cold.2
CStrings:
+ "%u"
+ "%{public}s> remote_device_timesync: This is no longer supported!"
+ "Creating device from: %{public}s"
+ "Creating service from: %{public}s"
+ "TimesyncPayload"
+ "addresses"
+ "assertion failure: \"clock_gettime(_CLOCK_REALTIME, &ts)\" -> %llu"
+ "clockfunc"
+ "close"
+ "ftruncate"
+ "invalid sntp response payload"
+ "legacy_timesync"
+ "mmap"
+ "munmap"
+ "net.c"
+ "open"
+ "sntp_client_unicast"
+ "sntp_server_exchange"
+ "t1.seconds"
+ "t1.subsecs"
+ "write"
- "%{public}s> Received error sending TIMESYNC command"
- "%{public}s> remote_device_timesync: %{errno}d"
- "*"
- "*16@0:8"
- ".cxx_destruct"
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSObject<OS_xpc_object>\"28@0:8*16B24"
- "@\"OS_remote_device\""
- "@\"OS_remote_listening_service\""
- "@\"OS_remote_pending_event\""
- "@\"OS_xpc_remote_connection\""
- "@16@0:8"
- "@28@0:8*16B24"
- "@40@0:8i16@20@28B36"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B32@0:8r*16@\"NSObject<OS_xpc_object>\"24"
- "B32@0:8r*16@24"
- "B40@0:8@16@24@32"
- "Creating device from: %s"
- "Creating service from: %s"
- "I"
- "I16@0:8"
- "OS_remote_device"
- "OS_remote_device_browser"
- "OS_remote_listening_service"
- "OS_remote_pending_event"
- "OS_remote_service"
- "Q"
- "Q16@0:8"
- "RemoteDeviceCommon"
- "RemoteDeviceQuery"
- "T*,N,V_uuid"
- "T*,R,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_cbq"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_connected_callback_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_disconnected_callback_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dq"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_connection"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_properties"
- "T@\"OS_remote_device\",&,N,V_connected_callback_self_retain"
- "T@\"OS_remote_device\",&,N,V_disconnected_callback_self_retain"
- "T@\"OS_xpc_remote_connection\",R,N,V_peer"
- "T@?,C,N,V_callback"
- "T@?,C,N,V_connected_callback"
- "T@?,C,N,V_disconnected_callback"
- "T@?,C,N,V_onCancel"
- "TB,N,V_canceled"
- "TB,N,V_canceling"
- "TB,N,V_remotexpc_tls_enabled"
- "TI,N,V_device_type"
- "TI,N,V_state"
- "TI,N,V_type"
- "TI,R,N"
- "TQ,N,V_device_id"
- "TQ,N,V_messaging_protocol_version"
- "Ti,R,N,V_clientSock"
- "Ti,R,N,V_serverSock"
- "Tr*,N,V_availableService"
- "Tr*,N,V_name"
- "Tr*,N,V_uuid"
- "Tr*,R,N"
- "_availableService"
- "_callback"
- "_canceled"
- "_canceling"
- "_cbq"
- "_clientSock"
- "_connected_callback"
- "_connected_callback_queue"
- "_connected_callback_self_retain"
- "_connection"
- "_device_id"
- "_device_type"
- "_disconnected_callback"
- "_disconnected_callback_queue"
- "_disconnected_callback_self_retain"
- "_dq"
- "_messaging_protocol_version"
- "_name"
- "_onCancel"
- "_peer"
- "_properties"
- "_queue"
- "_remotexpc_tls_enabled"
- "_serverSock"
- "_state"
- "_type"
- "_uuid"
- "accept_block"
- "activate"
- "addObject:"
- "assertion failure: \"xpc_get_type(srv->properties) == (&_xpc_type_dictionary)\" -> %llu"
- "availableService"
- "bytes"
- "callback"
- "cancel"
- "canceled"
- "canceling"
- "cbq"
- "clientSock"
- "connected_callback"
- "connected_callback_queue"
- "connected_callback_self_retain"
- "connection"
- "copy"
- "copyProperty:allowSensitive:"
- "countByEnumeratingWithState:objects:count:"
- "data"
- "dataWithLength:"
- "dealloc"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "disconnected_callback"
- "disconnected_callback_queue"
- "disconnected_callback_self_retain"
- "dq"
- "event"
- "hasServiceWithName:peerMessage:"
- "i"
- "i16@0:8"
- "i20@0:8i16"
- "init"
- "initWithBytes:length:"
- "initWithSocket:device:queue:server:"
- "lastObject"
- "length"
- "matches:forMessage:log:"
- "messaging_protocol_version"
- "mutableBytes"
- "next"
- "onCancel"
- "peer"
- "proxies"
- "proxySocketOverRemoteXPC:"
- "queue"
- "r*"
- "r*16@0:8"
- "remote_device_timesync was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance."
- "remotexpc_tls_enabled"
- "removeObject:"
- "serverSock"
- "service_name"
- "setAvailableService:"
- "setCallback:"
- "setCanceled:"
- "setCanceling:"
- "setCbq:"
- "setConnected_callback:"
- "setConnected_callback_queue:"
- "setConnected_callback_self_retain:"
- "setConnection:"
- "setDevice_id:"
- "setDevice_type:"
- "setDisconnected_callback:"
- "setDisconnected_callback_queue:"
- "setDisconnected_callback_self_retain:"
- "setDq:"
- "setMessaging_protocol_version:"
- "setName:"
- "setOnCancel:"
- "setProperties:"
- "setRemotexpc_tls_enabled:"
- "setState:"
- "setType:"
- "setUuid:"
- "sha256"
- "shouldEncryptSocketData"
- "sortUsingComparator:"
- "state"
- "stringWithFormat:"
- "takeOwnershipOfClientSocket"
- "timesync"
- "type"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8*16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8r*16"
- "wildcard"

```
