## pcapd

> `/usr/libexec/pcapd`

```diff

-62.0.0.0.0
-  __TEXT.__text: 0x3538
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x89e
-  __TEXT.__oslogstring: 0x51e
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xa0
-  __DATA.__data: 0x4
+63.0.0.0.0
+  __TEXT.__text: 0xbfdc
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0xce7
+  __TEXT.__oslogstring: 0x24ec
+  __TEXT.__unwind_info: 0x178
+  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x2f8
+  __DATA.__data: 0x290
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1048
-  __DATA.__common: 0xc
+  __DATA.__bss: 0x1058
+  __DATA.__common: 0x14
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 47
-  Symbols:   74
-  CStrings:  112
+  Functions: 158
+  Symbols:   166
+  CStrings:  350
 
Symbols:
+ __Block_object_dispose
+ ___assert_rtn
+ __dispatch_main_q
+ __dispatch_source_type_timer
+ __os_log_default
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_error_key_description
+ __xpc_error_termination_imminent
+ __xpc_type_array
+ __xpc_type_bool
+ __xpc_type_connection
+ __xpc_type_data
+ __xpc_type_date
+ __xpc_type_dictionary
+ __xpc_type_double
+ __xpc_type_endpoint
+ __xpc_type_error
+ __xpc_type_fd
+ __xpc_type_int64
+ __xpc_type_null
+ __xpc_type_shmem
+ __xpc_type_string
+ __xpc_type_uint64
+ __xpc_type_uuid
+ _dispatch_get_current_queue
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _dispatch_queue_create
+ _dispatch_retain
+ _dispatch_set_context
+ _dispatch_set_finalizer_f
+ _dispatch_source_set_cancel_handler
+ _dispatch_source_set_timer
+ _dispatch_source_testcancel
+ _getpid
+ _gettimeofday
+ _localtime_r
+ _mach_absolute_time
+ _mach_timebase_info
+ _malloc_type_calloc
+ _memmove
+ _mkdir
+ _os_release
+ _os_transaction_create
+ _pcap_close
+ _pcap_geterr
+ _pcap_ng_dump_close
+ _pcap_ng_dump_kern_event
+ _pcap_ng_dump_open
+ _pcap_ng_dump_pktap
+ _pcap_ng_dump_pktap_v2
+ _pcap_open_dead
+ _pthread_main_np
+ _realpath$DARWIN_EXTSN
+ _recv
+ _socket
+ _strdup
+ _strlen
+ _strncmp
+ _strnstr
+ _time
+ _uuid_copy
+ _uuid_is_null
+ _uuid_unparse
+ _xpc_bool_get_value
+ _xpc_connection_activate
+ _xpc_connection_cancel
+ _xpc_connection_create_mach_service
+ _xpc_connection_get_audit_token
+ _xpc_connection_get_context
+ _xpc_connection_get_pid
+ _xpc_connection_resume
+ _xpc_connection_send_message
+ _xpc_connection_set_context
+ _xpc_connection_set_event_handler
+ _xpc_connection_set_finalizer_f
+ _xpc_connection_set_target_queue
+ _xpc_copy_description
+ _xpc_copy_entitlement_for_token
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_remote_connection
+ _xpc_dictionary_get_string
+ _xpc_dictionary_get_uint64
+ _xpc_dictionary_get_value
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_string
+ _xpc_get_type
+ _xpc_int64_get_value
+ _xpc_release
+ _xpc_retain
+ _xpc_string_get_string_ptr
+ _xpc_uint64_get_value
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
CStrings:
+ " "
+ "%s%s%s-%02d-%02d-%04d-%02d%02d%02d-%09lu-%lu.pcapng"
+ "%s/"
+ "%s:%d %s pktap_filters are full\n"
+ "%s:%d Can't start unknown command %{public}s\n"
+ "%s:%d Can't stop unknown command %{public}s\n"
+ "%s:%d RRM NOT ALLOWED command: %{public}s from pid: %u\n"
+ "%s:%d Starting %{public}s\n"
+ "%s:%d Stopping %{public}s\n"
+ "%s:%d command: %{public}s from pid: %u\n"
+ "%s:%d pcap_gen_count %lu pcc->pcc_nsecs %lu\n"
+ "%s:%d pcap_opts->pco_compression %d\n"
+ "%s:%d setting BIOCSHDRCOMP with %d\n"
+ "%s:%d tapping %s over %s"
+ "%s:%d tapping %s over %s\n"
+ "%s:%d transaction dropped for %{public}s\n"
+ "%s:%d transaction held for %{public}s\n"
+ "%{public}s%{public}s  %{public}s%{public}s\n"
+ "%{public}s:%d \n"
+ "%{public}s:%d %{public}s flags: 0x%u\n"
+ "%{public}s:%d %{public}s: PCOF_ALWAYS_ON not on always_on_bpf_pcc\n"
+ "%{public}s:%d %{public}s: always_on_bpf_pcc with PCOF_SETUP_FROM_AOPCAP\n"
+ "%{public}s:%d %{public}s: out_file_path is NULL for %{public}s\n"
+ "%{public}s:%d %{public}s: pcap_ng_dump_open(%{public}s) failed: %{public}s\n"
+ "%{public}s:%d - error %{public}s (%d) BIOCGBLEN\n"
+ "%{public}s:%d - error %{public}s (%d) BIOCGHDRCOMPON\n"
+ "%{public}s:%d - error %{public}s (%d) BIOCGSTATS\n"
+ "%{public}s:%d - error %{public}s (%d) Skipping ioctl(BIOCGETUUID) until sandbox updated\n"
+ "%{public}s:%d - error %{public}s (%d) Skipping ioctl(BIOCSPKTHDRV2) until sandbox is updated\n"
+ "%{public}s:%d - error %{public}s (%d) Skipping ioctl(BIOCSTRUNCATE) until sandbox is fixed\n"
+ "%{public}s:%d - error %{public}s (%d) calloc()\n"
+ "%{public}s:%d - error %{public}s (%d) fcntl(F_GETFL)\n"
+ "%{public}s:%d - error %{public}s (%d) fcntl(F_SETFL)\n"
+ "%{public}s:%d - error %{public}s (%d) get_current_time() failed\n"
+ "%{public}s:%d - error %{public}s (%d) gettimeofday\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCGBLEN)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCGHEADDROP, 1)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCSBLEN)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCSDLT)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCSETIF)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCSETUP)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCSHDRCOMP)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCSHEADDROP, 1)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCSRTIMEOUT)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(BIOCSWANTPKTAP)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(SIOCGDRVSPEC, %s)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(SIOCSDRVSPEC, %s)\n"
+ "%{public}s:%d - error %{public}s (%d) ioctl(SIOCSKEVFILT)\n"
+ "%{public}s:%d - error %{public}s (%d) malloc(%u)\n"
+ "%{public}s:%d - error %{public}s (%d) malloc(%zu) failed\n"
+ "%{public}s:%d - error %{public}s (%d) open(%{public}s)\n"
+ "%{public}s:%d - error %{public}s (%d) ppc_final_file_path - mkdir(%{public}s)\n"
+ "%{public}s:%d - error %{public}s (%d) ppc_final_file_path - realpath(%{public}s)\n"
+ "%{public}s:%d - error %{public}s (%d) ppc_final_file_path - strdup(%{public}s)\n\n"
+ "%{public}s:%d - error %{public}s (%d) ppc_final_file_path NULL - strdup(%{public}s)\n\n"
+ "%{public}s:%d - error %{public}s (%d) ppc_temp_file_path - strdup(strdup(pcc->ppc_final_file_path)\n\n"
+ "%{public}s:%d - error %{public}s (%d) ppc_temp_file_path NULL - realpath(%{public}s)\n\n"
+ "%{public}s:%d - error %{public}s (%d) read bpf\n"
+ "%{public}s:%d - error %{public}s (%d) read kevfd\n"
+ "%{public}s:%d - error %{public}s (%d) skipping ioctl(BIOCSETFNR) until sandbox is fixed\n"
+ "%{public}s:%d - error %{public}s (%d) socket(PF_INET, SOCK_DGRAM) failed\n"
+ "%{public}s:%d - error %{public}s (%d) socket(PF_SYSTEM, SOCK_RAW, SYSPROTO_EVENT)\n"
+ "%{public}s:%d - error %{public}s (%d) time() failed\n\n"
+ "%{public}s:%d BIOCGHEADDROP is 0\n"
+ "%{public}s:%d BIOCSBLEN %u\n"
+ "%{public}s:%d Can't start command with no key\n"
+ "%{public}s:%d Can't stop command with no key\n"
+ "%{public}s:%d Ethernet not IP or IPv6 type: 0x%04x\n\n"
+ "%{public}s:%d Ethernet type 0x%04x (ARP)\n\n"
+ "%{public}s:%d Ethernet type 0x%04x length %u / %u\n"
+ "%{public}s:%d IP length %u / %u\n\n"
+ "%{public}s:%d IPv6 length %u / %u\n\n"
+ "%{public}s:%d XPC_ERROR_CONNECTION_INTERRUPTED for peer %p\n"
+ "%{public}s:%d XPC_ERROR_CONNECTION_INVALID for peer %p\n"
+ "%{public}s:%d XPC_ERROR_TERMINATION_IMMINENT for peer %p\n"
+ "%{public}s:%d alloc_pcap_file_name() failed\n\n"
+ "%{public}s:%d bad pth_protocol_family %u\n\n"
+ "%{public}s:%d bh_caplen shorter than pktap pth_frame_pre_length\n\n"
+ "%{public}s:%d bh_caplen shorter than pktap pth_length\n\n"
+ "%{public}s:%d bh_caplen shorter than struct pktap_header\n\n"
+ "%{public}s:%d bh_complen prev_caplen bh_complen %u prev_caplen %u caplen %u \n\n"
+ "%{public}s:%d bufsize truncated to %u from %u\n"
+ "%{public}s:%d calloc failed\n\n"
+ "%{public}s:%d calloc() failed\n"
+ "%{public}s:%d cancelling notifier: %p\n"
+ "%{public}s:%d cancelling timer source for func %{public}s\n\n"
+ "%{public}s:%d cancelling tsk->tsk_stderr_source\n"
+ "%{public}s:%d cancelling tsk->tsk_stdout_source\n"
+ "%{public}s:%d connection %p event: %{public}s\n"
+ "%{public}s:%d connection: %p context is NULL\n"
+ "%{public}s:%d connection: %p context: %p bad ctx_connection %p \n"
+ "%{public}s:%d connection: %p context: %p is_main_context %d\n"
+ "%{public}s:%d connection: %p context: %p type: %d peer: %p is_main_context %d\n"
+ "%{public}s:%d datap underflow bh_complen %u prev_caplen %u caplen %u \n\n"
+ "%{public}s:%d dispatch_group_create() failed\n"
+ "%{public}s:%d dispatch_queue_create() failed\n"
+ "%{public}s:%d dispatch_source_create timer failed\n"
+ "%{public}s:%d dispatch_source_create() for DISPATCH_SOURCE_TYPE_READ failed.\n"
+ "%{public}s:%d dispatch_source_set_cancel_handler pcc_bpf_handler %p\n"
+ "%{public}s:%d dispatch_source_set_event_handler pcc_kev_handler %p\n"
+ "%{public}s:%d done\n"
+ "%{public}s:%d entered group %p\n"
+ "%{public}s:%d failed\n"
+ "%{public}s:%d failed to allocate pcc_device\n\n"
+ "%{public}s:%d failed to allocate pcc_prefix\n\n"
+ "%{public}s:%d flags 0x%x uuid %{uuid_t}.16P bufsize %u packets captured %u dropped %u\n"
+ "%{public}s:%d free context: %p connection: %p peer: %p\n"
+ "%{public}s:%d freeing %p\n"
+ "%{public}s:%d key: %{public}s\n"
+ "%{public}s:%d key: %{public}s timeout: %u\n"
+ "%{public}s:%d leave group %p\n"
+ "%{public}s:%d malloc failed\n"
+ "%{public}s:%d need file or powerlog flag\n\n"
+ "%{public}s:%d open_bpf_device %{public}s pcc_flags 0x%x\n"
+ "%{public}s:%d open_bpf_device(%{public}s) failed\n\n"
+ "%{public}s:%d pcap_open_dead(DLT_PCAPNG, MAX_PACKET_LEN) failed\n\n"
+ "%{public}s:%d pcap_opts is NULL\n\n"
+ "%{public}s:%d pcap_setup_pktap_interface() always_on_bpf_pcc already opened\n"
+ "%{public}s:%d pcap_setup_pktap_interface() fail - %{public}s\n"
+ "%{public}s:%d pcc or ppc_temp_file_path is NULL\n"
+ "%{public}s:%d ppc_final_file_path is NULL\n"
+ "%{public}s:%d prev_datap NULL bh_complen %u prev_caplen %u caplen %u \n\n"
+ "%{public}s:%d proto 0x%x length %u / %u\n\n"
+ "%{public}s:%d pti_group notify %p\n"
+ "%{public}s:%d received invalid dictionary from peer(%d)\n:%{public}s\n"
+ "%{public}s:%d received message from peer(%d)\n:%{public}s\n"
+ "%{public}s:%d reply message to peer(%d)\n: %{public}s\n"
+ "%{public}s:%d ret_len %u length greater than bh_caplen %u\n\n"
+ "%{public}s:%d skipped func %{public}s terminated\n\n"
+ "%{public}s:%d starting %{public}s on %{public}s timeout %u in_file_dir_path %{public}s snaplen %u buffersize %u\n"
+ "%{public}s:%d stopping func %{public}s\n\n"
+ "%{public}s:%d strdup() failed\n"
+ "%{public}s:%d strdup(pktap) failed\n"
+ "%{public}s:%d too short for Ethernet header\n\n"
+ "%{public}s:%d xpc listener error: %s\n"
+ "%{public}s:%d xpc listener new connection %p\n\n"
+ "%{public}s:%d xpc listener unknown message type\n"
+ "%{public}s:%d xpc_connection_create_mach_service(%s) failed\n"
+ "''"
+ "/"
+ "/Library/Logs/CrashReporter/"
+ "/private/var/tmp/"
+ "<XPC_TYPE_UNKNOWN>"
+ "Dropped %u packets for %u captured\n"
+ "Starting packet capture over %{public}s to %{public}s\n"
+ "Starting packet capture over %{public}s to PowerLog\n"
+ "XPC_TYPE_ARRAY"
+ "XPC_TYPE_BOOL"
+ "XPC_TYPE_CONNECTION"
+ "XPC_TYPE_DATA"
+ "XPC_TYPE_DATE"
+ "XPC_TYPE_DICTIONARY"
+ "XPC_TYPE_DOUBLE"
+ "XPC_TYPE_ENDPOINT"
+ "XPC_TYPE_ERROR"
+ "XPC_TYPE_FD"
+ "XPC_TYPE_INT64"
+ "XPC_TYPE_NULL"
+ "XPC_TYPE_SHMEM"
+ "XPC_TYPE_STRING"
+ "XPC_TYPE_UINT64"
+ "XPC_TYPE_UUID"
+ "alloc_pcap_file_name"
+ "alloc_pti"
+ "capture_packet"
+ "capture_packet_block_invoke"
+ "com.apple.packetcapturetest"
+ "com.apple.pcapd-local"
+ "com.apple.private.pcapd-local"
+ "command"
+ "create_local_pcap_xpc_listener"
+ "create_local_pcap_xpc_listener_block_invoke"
+ "droptap"
+ "droptapcap"
+ "droptappcap"
+ "filegid"
+ "filemode"
+ "filename"
+ "fileuid"
+ "free_connection_context"
+ "free_tasklet"
+ "get_packet_truncated_length"
+ "get_pcc_info"
+ "get_tasklet_out_file_path"
+ "handle_pcapd_service"
+ "handle_pcapd_service_block_invoke"
+ "is_main_context()"
+ "key"
+ "local-pcap.c"
+ "move_pcap_files"
+ "new_connection_context"
+ "new_tasklet"
+ "not terminated %p\n"
+ "open_bpf_device"
+ "open_kev_socket"
+ "open_pcap_file"
+ "packet_capture_context_finalizer"
+ "packetcapture"
+ "packets"
+ "pcap_opts_from_request"
+ "pcapbuffersize"
+ "pcapcompress"
+ "pcapifname"
+ "pcappktapv2"
+ "pcapsnaplen"
+ "peer_context_finalizer"
+ "peer_event_handler"
+ "process_peer_request"
+ "process_start_pcap_request"
+ "process_start_pcap_request_block_invoke"
+ "process_task_run"
+ "process_task_stop"
+ "pth2_comm %{public}s pth2_ecomm %{public}s\n\n"
+ "pth2_dlt %u\n\n"
+ "pth2_flags 0x%x\n\n"
+ "pth2_flowid %u\n\n"
+ "pth2_frame_pre_length %u pth2_frame_post_length %u\n\n"
+ "pth2_ifname %{public}s pth2_iftype %d\n\n"
+ "pth2_ipproto %u\n\n"
+ "pth2_length %u (sizeof(struct pktap_v2_hdr) %lu)\n\n"
+ "pth2_pid %u pth2_e_pid %u\n\n"
+ "pth2_protocol_family %u\n\n"
+ "pth2_svc %u\n\n"
+ "pth2_uuid %{public}s pth2_euuid %{public}s\n\n"
+ "pth_comm %{public}s pth_ecomm %{public}s\n\n"
+ "pth_dlt %u\n\n"
+ "pth_flags 0x%x\n\n"
+ "pth_flowid %u\n\n"
+ "pth_frame_pre_length %u pth_frame_post_length %u\n\n"
+ "pth_ifname %{public}s pth_iftype %d\n\n"
+ "pth_ipproto %u\n\n"
+ "pth_length %u (sizeof(struct pktap_header) %lu) ts %ld.%d\n\n"
+ "pth_pid %u pth_epid %u\n\n"
+ "pth_protocol_family %u\n\n"
+ "pth_svc %u\n\n"
+ "pth_type_next %u\n\n"
+ "pth_uuid %{public}s pth_euuid %{public}s\n\n"
+ "run"
+ "run_func"
+ "set_always_on_pktap_filter"
+ "set_nonblocking"
+ "set_snaplen"
+ "set_tasklet_timeout"
+ "setup_lockdown_notification"
+ "setup_lockdown_notification_block_invoke"
+ "start_pcap"
+ "status"
+ "stop"
+ "stop_func"
+ "task %{public}s already exists\n"
+ "task %{public}s skipped terminated\n"
+ "timeout"
+ "timeout %llu too big, capped to %u\n"
+ "timeout cancelled for %{public}s\n"
+ "timeout fired for %{public}s\n"
+ "v16@?0^v8"
- "%s%u"
- "%s:%d Timed out waiting for the service to checkin in."
- "%s:%d Timed out waiting for the service to checkin in.\n"
- "%s:%d dispatch_semaphore_create() failed"
- "%s:%d dispatch_semaphore_create() failed\n"
- "%s:%d pktap_hdr == NULL"
- "%s:%d pktap_hdr == NULL\n"
- "%s:%d taping %s over %s"
- "%s:%d taping %s over %s\n"
- "input"
- "ipsec"
- "iptap: %s hdr_length: %d length: %d frame_pre_length: %dframe_pst_length: %d version: %d type: %d ifname: %s%d process %s.%d svc %d tstamp %d.%d flags 0x%x (%s)"
- "main_block_invoke"
- "output"
- "pktap_hdr == NULL"
- "rvi_iptap_to_pktap"
- "rvi_log_iptap_header"
- "utun"

```
