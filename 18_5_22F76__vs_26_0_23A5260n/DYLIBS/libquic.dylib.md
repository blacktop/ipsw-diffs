## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-4277.122.6.0.0
-  __TEXT.__text: 0xceb40
-  __TEXT.__auth_stubs: 0x19b0
-  __TEXT.__objc_methlist: 0x238
-  __TEXT.__const: 0x365
-  __TEXT.__cstring: 0x8da1
-  __TEXT.__oslogstring: 0x115c5
-  __TEXT.__unwind_info: 0xde8
+5569.0.37.0.12
+  __TEXT.__text: 0xce6dc
+  __TEXT.__auth_stubs: 0x1a30
+  __TEXT.__objc_methlist: 0x244
+  __TEXT.__const: 0x39d
+  __TEXT.__cstring: 0x8f25
+  __TEXT.__oslogstring: 0x115dc
+  __TEXT.__unwind_info: 0xe08
   __TEXT.__objc_classname: 0xa
-  __TEXT.__objc_methname: 0x7c5
-  __TEXT.__objc_methtype: 0xbd0
-  __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x2428
+  __TEXT.__objc_methname: 0x7e6
+  __TEXT.__objc_methtype: 0xd09
+  __TEXT.__objc_stubs: 0x660
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x23b8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e0
+  __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xce0
-  __AUTH_CONST.__const: 0x25c0
+  __AUTH_CONST.__auth_got: 0xd20
+  __AUTH_CONST.__const: 0x2560
   __AUTH_CONST.__cfstring: 0x1480
   __AUTH_CONST.__objc_const: 0xf8
+  __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x110
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x4c
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x5d8
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x5b0
   __DATA_DIRTY.__data: 0x1c
   __DATA_DIRTY.__bss: 0x6b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EECA0681-A157-3A18-AEB0-244D0317613A
-  Functions: 1161
-  Symbols:   3180
-  CStrings:  2912
+  UUID: E197C14B-59FC-344E-B77F-604D26908931
+  Functions: 1153
+  Symbols:   3162
+  CStrings:  2915
 
Symbols:
+ +[QUICLog packetSentReceivedTriggerString:]
+ -[QUICLog createEvent:timestamp:]
+ -[QUICLog packetSent:timestamp:]
+ -[QUICLog processPacketSentAndPacketReceived:]
+ _____quic_signpost_is_enabled_block_invoke.2541
+ _____quic_signpost_is_enabled_block_invoke.3086
+ _____quic_signpost_is_enabled_block_invoke.3617
+ _____quic_signpost_is_enabled_block_invoke.3852
+ _____quic_signpost_is_enabled_block_invoke.678
+ _____quic_signpost_is_enabled_block_invoke.952
+ ___block_descriptor_tmp.1.3124
+ ___block_descriptor_tmp.10.3480
+ ___block_descriptor_tmp.101
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.104
+ ___block_descriptor_tmp.11.2484
+ ___block_descriptor_tmp.11.3343
+ ___block_descriptor_tmp.11.3751
+ ___block_descriptor_tmp.113
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.12.3084
+ ___block_descriptor_tmp.12.3517
+ ___block_descriptor_tmp.1228
+ ___block_descriptor_tmp.124
+ ___block_descriptor_tmp.13.2487
+ ___block_descriptor_tmp.13.2996
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.136
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.14.2087
+ ___block_descriptor_tmp.14.4456
+ ___block_descriptor_tmp.146
+ ___block_descriptor_tmp.149.4215
+ ___block_descriptor_tmp.15.2485
+ ___block_descriptor_tmp.15.2853
+ ___block_descriptor_tmp.15.3913
+ ___block_descriptor_tmp.154
+ ___block_descriptor_tmp.158.3769
+ ___block_descriptor_tmp.16.3912
+ ___block_descriptor_tmp.1615
+ ___block_descriptor_tmp.1693
+ ___block_descriptor_tmp.17.3170
+ ___block_descriptor_tmp.17.346
+ ___block_descriptor_tmp.17.3752
+ ___block_descriptor_tmp.1813
+ ___block_descriptor_tmp.188
+ ___block_descriptor_tmp.1915
+ ___block_descriptor_tmp.194
+ ___block_descriptor_tmp.196
+ ___block_descriptor_tmp.2054
+ ___block_descriptor_tmp.207
+ ___block_descriptor_tmp.208
+ ___block_descriptor_tmp.211
+ ___block_descriptor_tmp.212
+ ___block_descriptor_tmp.213
+ ___block_descriptor_tmp.214
+ ___block_descriptor_tmp.215
+ ___block_descriptor_tmp.22.3909
+ ___block_descriptor_tmp.220
+ ___block_descriptor_tmp.2220
+ ___block_descriptor_tmp.226
+ ___block_descriptor_tmp.227
+ ___block_descriptor_tmp.228
+ ___block_descriptor_tmp.229
+ ___block_descriptor_tmp.23.3190
+ ___block_descriptor_tmp.23.3753
+ ___block_descriptor_tmp.23.397
+ ___block_descriptor_tmp.2391
+ ___block_descriptor_tmp.24.2548
+ ___block_descriptor_tmp.24.3188
+ ___block_descriptor_tmp.246
+ ___block_descriptor_tmp.2477
+ ___block_descriptor_tmp.249
+ ___block_descriptor_tmp.27.2549
+ ___block_descriptor_tmp.27.387
+ ___block_descriptor_tmp.27.3906
+ ___block_descriptor_tmp.2709
+ ___block_descriptor_tmp.28.2575
+ ___block_descriptor_tmp.28.3905
+ ___block_descriptor_tmp.2843
+ ___block_descriptor_tmp.29.3754
+ ___block_descriptor_tmp.3.3711
+ ___block_descriptor_tmp.3.433
+ ___block_descriptor_tmp.30.2550
+ ___block_descriptor_tmp.31.2571
+ ___block_descriptor_tmp.3101
+ ___block_descriptor_tmp.33.2551
+ ___block_descriptor_tmp.33.3902
+ ___block_descriptor_tmp.3385
+ ___block_descriptor_tmp.34.3615
+ ___block_descriptor_tmp.34.3755
+ ___block_descriptor_tmp.35
+ ___block_descriptor_tmp.35.2560
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.37.2552
+ ___block_descriptor_tmp.37.3899
+ ___block_descriptor_tmp.3920
+ ___block_descriptor_tmp.4.1619
+ ___block_descriptor_tmp.4.2903
+ ___block_descriptor_tmp.4.3709
+ ___block_descriptor_tmp.40.2582
+ ___block_descriptor_tmp.42.3756
+ ___block_descriptor_tmp.4278
+ ___block_descriptor_tmp.43
+ ___block_descriptor_tmp.438
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.4559
+ ___block_descriptor_tmp.46.3757
+ ___block_descriptor_tmp.48.1212
+ ___block_descriptor_tmp.48.3758
+ ___block_descriptor_tmp.5.2140
+ ___block_descriptor_tmp.5.2475
+ ___block_descriptor_tmp.5.3399
+ ___block_descriptor_tmp.5.3957
+ ___block_descriptor_tmp.50.3759
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.53.2491
+ ___block_descriptor_tmp.55
+ ___block_descriptor_tmp.60.4649
+ ___block_descriptor_tmp.676
+ ___block_descriptor_tmp.7.3178
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.72.3764
+ ___block_descriptor_tmp.74.3760
+ ___block_descriptor_tmp.78.3972
+ ___block_descriptor_tmp.79
+ ___block_descriptor_tmp.79.3973
+ ___block_descriptor_tmp.8.3265
+ ___block_descriptor_tmp.80.3974
+ ___block_descriptor_tmp.83
+ ___block_descriptor_tmp.85.3742
+ ___block_descriptor_tmp.86.3995
+ ___block_descriptor_tmp.9.2553
+ ___block_descriptor_tmp.9.304
+ ___block_descriptor_tmp.9.3276
+ ___block_descriptor_tmp.9.3474
+ ___block_descriptor_tmp.9.3916
+ ___block_descriptor_tmp.94
+ ___block_descriptor_tmp.950
+ ___block_descriptor_tmp.98
+ ___block_literal_global.106
+ ___block_literal_global.112
+ ___block_literal_global.1178
+ ___block_literal_global.121
+ ___block_literal_global.127
+ ___block_literal_global.156
+ ___block_literal_global.1613
+ ___block_literal_global.1811
+ ___block_literal_global.19
+ ___block_literal_global.1913
+ ___block_literal_global.193
+ ___block_literal_global.217
+ ___block_literal_global.2218
+ ___block_literal_global.2389
+ ___block_literal_global.246
+ ___block_literal_global.248
+ ___block_literal_global.25
+ ___block_literal_global.2537
+ ___block_literal_global.30
+ ___block_literal_global.3080
+ ___block_literal_global.3609
+ ___block_literal_global.3708
+ ___block_literal_global.431
+ ___block_literal_global.4557
+ ___block_literal_global.609
+ ___block_literal_global.7.3955
+ ___block_literal_global.8
+ ___block_literal_global.90
+ ___block_literal_global.946
+ ___quic_conn_copy_info_block_invoke.147
+ ___quic_conn_copy_metadata_block_invoke_4
+ ___quic_conn_handle_stop_inner_block_invoke_2
+ ___quic_conn_link_advisory_block_invoke.141
+ ___quic_conn_preferred_path_block_invoke
+ ___quic_conn_preferred_path_block_invoke.157
+ ___quic_conn_send_frames_for_key_state_block_invoke.206
+ ___quic_conn_set_mss_block_invoke.84
+ ___quic_crypto_error_block_invoke
+ ___quic_crypto_finalize_output_frames_block_invoke.76
+ ___quic_crypto_setup_sec_options_block_invoke_10
+ ___quic_crypto_tls_ready_inner_block_invoke.69
+ ___quic_migration_evaluate_server_block_invoke.38
+ ___quic_migration_fallback_block_invoke
+ ___quic_migration_migrate_block_invoke_2
+ ___quic_migration_path_event_block_invoke.26
+ ___quic_signpost_is_enabled._quic_signposts_enabled.2538
+ ___quic_signpost_is_enabled._quic_signposts_enabled.3081
+ ___quic_signpost_is_enabled._quic_signposts_enabled.3610
+ ___quic_signpost_is_enabled._quic_signposts_enabled.3850
+ ___quic_signpost_is_enabled._quic_signposts_enabled.610
+ ___quic_signpost_is_enabled._quic_signposts_enabled.947
+ ___quic_signpost_is_enabled._quic_signposts_once.2536
+ ___quic_signpost_is_enabled._quic_signposts_once.3079
+ ___quic_signpost_is_enabled._quic_signposts_once.3608
+ ___quic_signpost_is_enabled._quic_signposts_once.3849
+ ___quic_signpost_is_enabled._quic_signposts_once.608
+ ___quic_signpost_is_enabled._quic_signposts_once.945
+ _l4s_developer
+ _network_config_get_l4s_enabled
+ _networkd_settings_get_bool
+ _nw_interface_get_l4s_mode
+ _nw_interface_get_type
+ _nw_protocol_definition_is_equal
+ _nw_protocol_establishment_report_set_quic_migration_supported
+ _nw_protocol_instance_copy_initial_data_for_path
+ _nw_protocol_instance_drop_outbound
+ _nw_protocol_options_is_quic_connection
+ _nw_quic_connection_execute_pmtud_update_block
+ _nw_quic_connection_get_ignore_path_errors
+ _nw_quic_connection_get_phone_call_relay_optimization
+ _nw_quic_connection_get_pmtud_update_interval
+ _nw_quic_connection_get_setup_placeholder
+ _nw_sec_protocol_options_iterate_application_protocols
+ _nw_setting_pqtls_enable_non_h3_quic
+ _nw_settings_get_quic_migration_enabled
+ _objc_msgSend$createEvent:timestamp:
+ _objc_msgSend$packetSent:timestamp:
+ _objc_msgSend$packetSentReceivedTriggerString:
+ _objc_msgSend$processPacketSentAndPacketReceived:
+ _quic_cid_array_retire_by_seq_num
+ _quic_cid_array_should_insert
+ _quic_conn_application_close
+ _quic_conn_preferred_path
+ _quic_conn_preferred_path_with_condition
+ _quic_frame_alloc_STOP_SENDING
+ _quic_migration_fillout_data_transfer_snapshot
+ _quic_packet_builder_has_non_probing_frame
+ _quic_path_setup_l4s_state
+ _quic_pmtud_search_complete_notify
+ _quiclog_packet_sent
+ _sec_protocol_options_get_pqtls_mode
+ _sec_protocol_options_set_pqtls_mode
- +[QUICLog packetSentRecievedTriggerString:]
- -[QUICLog packetSent:]
- -[QUICLog processPacketSentAndPacketRecieved:]
- _____quic_signpost_is_enabled_block_invoke.2523
- _____quic_signpost_is_enabled_block_invoke.3026
- _____quic_signpost_is_enabled_block_invoke.3118
- _____quic_signpost_is_enabled_block_invoke.3656
- _____quic_signpost_is_enabled_block_invoke.3889
- _____quic_signpost_is_enabled_block_invoke.696
- _____quic_signpost_is_enabled_block_invoke.970
- ___block_descriptor_tmp.1.3039
- ___block_descriptor_tmp.1.3156
- ___block_descriptor_tmp.10.3519
- ___block_descriptor_tmp.106
- ___block_descriptor_tmp.107
- ___block_descriptor_tmp.11.2467
- ___block_descriptor_tmp.11.3382
- ___block_descriptor_tmp.11.3792
- ___block_descriptor_tmp.111
- ___block_descriptor_tmp.116
- ___block_descriptor_tmp.117
- ___block_descriptor_tmp.12.3116
- ___block_descriptor_tmp.12.3556
- ___block_descriptor_tmp.120
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.1242
- ___block_descriptor_tmp.126
- ___block_descriptor_tmp.13.2470
- ___block_descriptor_tmp.13.2971
- ___block_descriptor_tmp.131
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.14.2074
- ___block_descriptor_tmp.14.4491
- ___block_descriptor_tmp.140
- ___block_descriptor_tmp.149.4247
- ___block_descriptor_tmp.15.2468
- ___block_descriptor_tmp.15.2828
- ___block_descriptor_tmp.15.334
- ___block_descriptor_tmp.15.3950
- ___block_descriptor_tmp.156
- ___block_descriptor_tmp.157.4256
- ___block_descriptor_tmp.158.4260
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.16.3949
- ___block_descriptor_tmp.160.4218
- ___block_descriptor_tmp.1611
- ___block_descriptor_tmp.1689
- ___block_descriptor_tmp.17.3793
- ___block_descriptor_tmp.18.3639
- ___block_descriptor_tmp.1810
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.1907
- ___block_descriptor_tmp.195
- ___block_descriptor_tmp.198
- ___block_descriptor_tmp.201
- ___block_descriptor_tmp.204
- ___block_descriptor_tmp.2041
- ___block_descriptor_tmp.206
- ___block_descriptor_tmp.21.3246
- ___block_descriptor_tmp.21.3946
- ___block_descriptor_tmp.217
- ___block_descriptor_tmp.218
- ___block_descriptor_tmp.22.2564
- ___block_descriptor_tmp.22.3945
- ___block_descriptor_tmp.2208
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.23.3794
- ___block_descriptor_tmp.230
- ___block_descriptor_tmp.231
- ___block_descriptor_tmp.233
- ___block_descriptor_tmp.234
- ___block_descriptor_tmp.237
- ___block_descriptor_tmp.2379
- ___block_descriptor_tmp.238
- ___block_descriptor_tmp.239
- ___block_descriptor_tmp.24.2531
- ___block_descriptor_tmp.24.402
- ___block_descriptor_tmp.240
- ___block_descriptor_tmp.2460
- ___block_descriptor_tmp.25.180
- ___block_descriptor_tmp.25.2556
- ___block_descriptor_tmp.255
- ___block_descriptor_tmp.258
- ___block_descriptor_tmp.26.3235
- ___block_descriptor_tmp.2688
- ___block_descriptor_tmp.27.2532
- ___block_descriptor_tmp.27.3942
- ___block_descriptor_tmp.28.2552
- ___block_descriptor_tmp.28.3226
- ___block_descriptor_tmp.28.3941
- ___block_descriptor_tmp.2818
- ___block_descriptor_tmp.29.3795
- ___block_descriptor_tmp.3.3007
- ___block_descriptor_tmp.3.3748
- ___block_descriptor_tmp.3.428
- ___block_descriptor_tmp.30.1692
- ___block_descriptor_tmp.30.2533
- ___block_descriptor_tmp.30.3227
- ___block_descriptor_tmp.3003
- ___block_descriptor_tmp.31.2534
- ___block_descriptor_tmp.31.3224
- ___block_descriptor_tmp.3133
- ___block_descriptor_tmp.34.3654
- ___block_descriptor_tmp.34.3796
- ___block_descriptor_tmp.3424
- ___block_descriptor_tmp.37.3936
- ___block_descriptor_tmp.39.2526
- ___block_descriptor_tmp.3957
- ___block_descriptor_tmp.4.1615
- ___block_descriptor_tmp.4.2878
- ___block_descriptor_tmp.4.3746
- ___block_descriptor_tmp.42.3797
- ___block_descriptor_tmp.4318
- ___block_descriptor_tmp.433
- ___block_descriptor_tmp.4594
- ___block_descriptor_tmp.46.3798
- ___block_descriptor_tmp.47
- ___block_descriptor_tmp.48.2476
- ___block_descriptor_tmp.48.3799
- ___block_descriptor_tmp.5.2124
- ___block_descriptor_tmp.5.2458
- ___block_descriptor_tmp.5.3025
- ___block_descriptor_tmp.5.3438
- ___block_descriptor_tmp.5.3996
- ___block_descriptor_tmp.50.3800
- ___block_descriptor_tmp.52.3801
- ___block_descriptor_tmp.60.4685
- ___block_descriptor_tmp.65
- ___block_descriptor_tmp.67.3810
- ___block_descriptor_tmp.69.3802
- ___block_descriptor_tmp.694
- ___block_descriptor_tmp.7.269
- ___block_descriptor_tmp.7.3214
- ___block_descriptor_tmp.74.3803
- ___block_descriptor_tmp.75
- ___block_descriptor_tmp.8.3304
- ___block_descriptor_tmp.82.4011
- ___block_descriptor_tmp.84.3781
- ___block_descriptor_tmp.86.3782
- ___block_descriptor_tmp.89
- ___block_descriptor_tmp.9.2535
- ___block_descriptor_tmp.9.3315
- ___block_descriptor_tmp.9.3513
- ___block_descriptor_tmp.9.3953
- ___block_descriptor_tmp.95.3925
- ___block_descriptor_tmp.968
- ___block_literal_global.102
- ___block_literal_global.105
- ___block_literal_global.113
- ___block_literal_global.119
- ___block_literal_global.1196
- ___block_literal_global.128
- ___block_literal_global.134
- ___block_literal_global.1609
- ___block_literal_global.17
- ___block_literal_global.1808
- ___block_literal_global.1905
- ___block_literal_global.20
- ___block_literal_global.200
- ___block_literal_global.203
- ___block_literal_global.21
- ___block_literal_global.2206
- ___block_literal_global.227
- ___block_literal_global.23
- ___block_literal_global.2377
- ___block_literal_global.238
- ___block_literal_global.2519
- ___block_literal_global.257
- ___block_literal_global.3021
- ___block_literal_global.3112
- ___block_literal_global.3648
- ___block_literal_global.3745
- ___block_literal_global.426
- ___block_literal_global.4592
- ___block_literal_global.627
- ___block_literal_global.7.3994
- ___block_literal_global.91
- ___block_literal_global.964
- ___nw_create_backtrace_string
- ___nwlog_fault
- ___nwlog_obj
- ___quic_conn_copy_info_block_invoke.154
- ___quic_conn_copy_metadata_block_invoke.79
- ___quic_conn_force_send_frames_block_invoke
- ___quic_conn_initialize_inner_block_invoke.192
- ___quic_conn_inject_packet_block_invoke_3
- ___quic_conn_link_advisory_block_invoke.148
- ___quic_conn_send_frames_block_invoke
- ___quic_conn_send_frames_for_key_state_block_invoke.216
- ___quic_conn_set_mss_block_invoke.85
- ___quic_crypto_finalize_output_frames_block_invoke.71
- ___quic_crypto_tls_ready_inner_block_invoke.66
- ___quic_fc_continue_sending_block_invoke_3
- ___quic_fc_stream_path_affinity_block_invoke_2
- ___quic_fc_stream_path_affinity_block_invoke_3
- ___quic_migration_path_event_block_invoke.22
- ___quic_pacer_continue_sending_block_invoke
- ___quic_pacer_send_packet_block_invoke
- ___quic_pacer_service_queue_block_invoke
- ___quic_signpost_is_enabled._quic_signposts_enabled.2520
- ___quic_signpost_is_enabled._quic_signposts_enabled.3022
- ___quic_signpost_is_enabled._quic_signposts_enabled.3113
- ___quic_signpost_is_enabled._quic_signposts_enabled.3649
- ___quic_signpost_is_enabled._quic_signposts_enabled.3887
- ___quic_signpost_is_enabled._quic_signposts_enabled.628
- ___quic_signpost_is_enabled._quic_signposts_enabled.965
- ___quic_signpost_is_enabled._quic_signposts_once.2518
- ___quic_signpost_is_enabled._quic_signposts_once.3020
- ___quic_signpost_is_enabled._quic_signposts_once.3111
- ___quic_signpost_is_enabled._quic_signposts_once.3647
- ___quic_signpost_is_enabled._quic_signposts_once.3886
- ___quic_signpost_is_enabled._quic_signposts_once.626
- ___quic_signpost_is_enabled._quic_signposts_once.963
- __os_log_impl
- __os_log_send_and_compose_impl
- __quic_pacer_destroy
- _mach_absolute_time
- _mach_wait_until
- _nw_protocol_metadata_create_singleton
- _nw_quic_stream_set_has_datagram_variant_flow_id
- _objc_msgSend$packetSent:
- _objc_msgSend$packetSentRecievedTriggerString:
- _objc_msgSend$processPacketSentAndPacketRecieved:
- _os_variant_has_internal_diagnostics
- _paced_packet_create
- _quic_cid_array_remove_by_seq_num
- _quic_cid_entry_erase
- _quic_conn_initialize_inner.onceToken
- _quic_conn_is_user_pacing
- _quic_conn_select_next_path
- _quic_disable_kernel_pacing
- _quic_migration_compare_paths
- _quic_pacer_continue_sending
- _quic_pacer_create
- _quic_pacer_get_burst_gap
- _quic_pacer_get_packet_tx_time.size
- _quic_pacer_packet_sent
- _quic_pacer_send_now
- _quic_pacer_send_packet
- _quic_pacer_service_queue
- _quic_pacer_set_gap
- _quic_pacer_wait_until_next_deadline
- _quic_reassq_recalculate_size
- _sec_framer_debug
CStrings:
+ "%{public}s "
+ "%{public}s %{public}s [%{public}s-%{public}s] L4S is enabled for this connection"
+ "%{public}s %{public}s [%{public}s-%{public}s] TLS alert error %d"
+ "%{public}s %{public}s [%{public}s-%{public}s] TLS error (security error %d) (state %{public}s)"
+ "%{public}s %{public}s [%{public}s-%{public}s] TLS error means \"%{public}s\""
+ "%{public}s %{public}s [%{public}s-%{public}s] available path is not yet primary, ignoring it"
+ "%{public}s %{public}s [%{public}s-%{public}s] bringing up all available paths with priority %d while probing path over %{public}s"
+ "%{public}s %{public}s [%{public}s-%{public}s] fallback event, no longer in fallback mode"
+ "%{public}s Copied incomplete bytes"
+ "%{public}s Setting up flow %llx as QUIC tunnel placeholder"
+ "%{public}s link received congestion notification, reduced congestion window is %llu bytes"
+ "%{public}s new_primary_path is null or 0"
+ "%{public}s path validation in progress, ignoring established event"
+ "%{public}s secret derivation failed, result %d, size %u, algorithm %u"
+ "%{public}s tried to set path->mss to 0 from quic_conn_get_mss_from_interface()"
+ "%{public}s using path over %{public}s while probing"
+ "-[QUICLog createEvent:timestamp:]"
+ "-[QUICLog packetSent:timestamp:]"
+ "-[QUICLog processPacketSentAndPacketReceived:]"
+ "B16@?0^{quic_frame=QS[6c](?={?=CcsS}{?=QQQ}{?=QQQ*}{?=Q}{?=QQ}{?=Q}{?=Q}{?=Q}{?=QQ}{?=Q}{?=Q}{?=QQ[21C][16C][3c]}{?=Q}{?=QQ}{?=Q[21C][3c]}{?=Q[21C][3c]}{?=C[7c]QQQQQQQ^{quic_ack_range}Q}{?=b1b7[7c]Q*}{?=b1b1b1b5[7c]QQQ*{nw_frame_array_s=^{nw_frame}^^{nw_frame}}}{?=Cb1b7[6c]QQ*}{?=b1b1b1b5[7c]QQQ*{nw_frame_array_s=^{nw_frame}^^{nw_frame}}}{?=QQQb1b63}{?=QQQQ*}{?=QQQQ}){?=^{quic_frame}^^{quic_frame}}^{quic_frame_pool}b1b1b1b5[7c]}8"
+ "B16@?0^{quic_path=Q^{nw_interface}C[21C][21C]cI[12{?=QQ}]{quic_frame_list=^{quic_frame}^^{quic_frame}}^{quic_rtt}[16c]IIQ{?=^{quic_path}^^{quic_path}}QQIIQ^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_pacer}^{quic_pmtud}^{quic_loss_recovery_path_state}^{quic_ecn_path_state}{quic_path_statistics=QQQQIIII}SSSCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b2[6c]}8"
+ "B16@?0r*8"
+ "B24@?0Q8^{quic_stream=Q^{quic_conn}^{nw_protocol_metadata}QQQQQ{sbuf=QQ}{sbuf=QQ}QQQQQQQQQQQ{nw_frame_array_s=^{nw_frame}^^{nw_frame}}QQQQQQSCCI^{quic_reassq}^{quic_reassq}^{quic_reassq}^{quic_reassq}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b12[4c]}16"
+ "TLS alert error"
+ "^{quiclog_event=i[4c]Q(?={?=QQQQQ[32c][21C][21C][21C]cccC{quic_preferred_address={in_addr=I}S{in6_addr=(?=[16C][8S][4I])}S[21C][16C]}QQQQQQ}{?=i[4c]^{packet_header}{quic_frame_list=^{quic_frame}^^{quic_frame}}c[3c](?=iC)}{?=QCCC[1c]C[3c]}{?=QQQQQQQQQc[7c]}{?=CCC}{?=QCCC[5c]}){?=^{quiclog_event}}}28@0:8i16Q20"
+ "access denied"
+ "bad certificate"
+ "bad certificate hash value"
+ "bad certificate status response"
+ "bad record mac"
+ "certificate expired"
+ "certificate required"
+ "certificate revoked"
+ "certificate unknown"
+ "certificate unobtainable"
+ "close notify"
+ "createEvent:timestamp:"
+ "cubic_process_link_congestion_info"
+ "decode error"
+ "decompression failure"
+ "decrypt error"
+ "decryption failed"
+ "export restriction"
+ "handshake failure"
+ "illegal parameter"
+ "inappropriate fallback"
+ "insufficient security"
+ "internal error"
+ "ledbat_process_link_congestion_info"
+ "missing extension"
+ "no application protocol"
+ "no certificate"
+ "no renegotiation"
+ "packetSent:timestamp:"
+ "packetSentReceivedTriggerString:"
+ "processPacketSentAndPacketReceived:"
+ "protocol version"
+ "quic_cc_new_reno_process_link_congestion_info"
+ "quic_cid_array_retire_by_seq_num"
+ "quic_cid_array_should_insert"
+ "quic_conn_application_close"
+ "quic_conn_preferred_path"
+ "quic_conn_preferred_path_with_condition"
+ "quic_crypto_error_block_invoke"
+ "quic_migration_fillout_data_transfer_snapshot"
+ "quic_packet_builder_has_non_probing_frame"
+ "quic_path_setup_l4s_state"
+ "quic_pmtud_search_complete_notify"
+ "record overflow"
+ "unexpected message"
+ "unknown ca"
+ "unknown psk identity"
+ "unrecognized name"
+ "unsupported certificate"
+ "unsupported extension"
+ "user canceled"
+ "v32@0:8^{quic_packet=*****[21C][21C]CCCCCCSSS(?=SS)(?=*^I)iIQQQ^{quic_packet_pool}^{quic_path}{?=^{quic_frame}^^{quic_frame}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}}Qb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b17[4C]}16Q24"
- "%s hmac="
- "%s hp="
- "%s iv="
- "%s key="
- "%s: AES-128 (qpod),"
- "%s: AES-128,"
- "%s: AES-256,"
- "%s: ChaCha20Poly1305,"
- "%{public}s   [%llu, %llu)"
- "%{public}s %{private}s"
- "%{public}s %{public}s [%{public}s-%{public}s] L4S is enabled for this connection, ACK compression is %s"
- "%{public}s %{public}s [%{public}s-%{public}s] TLS error %d (state %{public}s)"
- "%{public}s TAILQ_EMPTY(&pacer->outgoing_packets) is null or 0"
- "%{public}s TLS %p sent error %d"
- "%{public}s called with null definition"
- "%{public}s called with null definition, backtrace limit exceeded"
- "%{public}s called with null definition, dumping backtrace:%{public}s"
- "%{public}s called with null definition, no backtrace"
- "%{public}s cid_entry is null or 0"
- "%{public}s fallback_interface is null or 0"
- "%{public}s frame %s len %u"
- "%{public}s pacer->conn is null or 0"
- "%{public}s pacer->packet_pool is null or 0"
- "%{public}s packet->data is null or 0"
- "%{public}s packet->quic_packet is null or 0"
- "%{public}s packet_pool is null or 0"
- "%{public}s path already validated, ignoring established event"
- "%{public}s path->mss == path->initial_mss is null or 0"
- "%{public}s reached max sending limit sent=%u, allowed_gap=%u deferring dequeuing"
- "%{public}s reassq state:"
- "%{public}s secret derivation failed"
- "-[QUICLog createEvent:]"
- "-[QUICLog packetSent:]"
- "-[QUICLog processPacketSentAndPacketRecieved:]"
- "B16@?0^{quic_frame=QS[6c](?={?=CcsS}{?=QQQ}{?=QQQ*}{?=Q}{?=QQ}{?=Q}{?=Q}{?=Q}{?=QQ}{?=Q}{?=Q}{?=QQ[21C][16C][3c]}{?=Q}{?=QQ}{?=Q[21C][3c]}{?=Q[21C][3c]}{?=C[7c]QQQQQQQ^{quic_ack_range}Q}{?=b1b7[7c]Q*}{?=b1b1b1b5[7c]QQQ*{nw_frame_array_s=^{nw_frame}^^{nw_frame}}}{?=Cb1b7[6c]QQ*}{?=b1b1b6[7c]QQQ*{nw_frame_array_s=^{nw_frame}^^{nw_frame}}}{?=QQQb1b63}{?=QQQQ*}{?=QQQQ}){?=^{quic_frame}^^{quic_frame}}^{quic_frame_pool}b1b1b1b5[7c]}8"
- "B16@?0^{quic_path=Q^{nw_interface}C[21C][21C]cI[12{?=QQ}]{quic_frame_list=^{quic_frame}^^{quic_frame}}^{quic_rtt}[16c]IIQ{?=^{quic_path}^^{quic_path}}QQIIQ^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_pacer}^{quic_pmtud}^{quic_loss_recovery_path_state}^{quic_ecn_path_state}SSSCb1b1b1b1b1b1b1b1b1b1b1b1b1b3[7c]}8"
- "B24@?0Q8^{quic_stream=Q^{quic_conn}^{nw_protocol_metadata}QQQQQ{sbuf=QQ}{sbuf=QQ}QQQQQQQQQQQ{nw_frame_array_s=^{nw_frame}^^{nw_frame}}QQQQQQSCCI^{quic_reassq}^{quic_reassq}^{quic_reassq}^{quic_reassq}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b13[4c]}16"
- "QUIC_USE_L4S"
- "_quic_pacer_destroy"
- "com.apple.network.quic.testing.keys"
- "disable_kernel_pacing"
- "paced_packet_create"
- "packetSent:"
- "packetSentRecievedTriggerString:"
- "packets_sent"
- "processPacketSentAndPacketRecieved:"
- "quic_cid_array_remove_by_seq_num"
- "quic_cid_entry_erase"
- "quic_conn_is_pacing"
- "quic_conn_is_user_pacing"
- "quic_conn_select_next_path"
- "quic_crypto_error"
- "quic_migration_establish_paths_with_priority"
- "quic_pacer_continue_sending"
- "quic_pacer_get_burst_gap"
- "quic_pacer_packet_sent"
- "quic_pacer_send_now"
- "quic_pacer_send_packet"
- "quic_pacer_service_queue"
- "quic_pacer_set_gap"
- "quic_pacer_wait_until_next_deadline"
- "quic_reassq_recalculate_size"
- "read-0-rtt"
- "read-1rrt-0"
- "read-1rrt-1"
- "read-handshake"
- "read-initial"
- "sec_framer_debug"
- "v24@0:8^{quic_packet=*****[21C][21C]CCCCCCSSS(?=SS)(?=*^I)iIQQQ^{quic_packet_pool}^{quic_path}{?=^{quic_frame}^^{quic_frame}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}}Qb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b17[4C]}16"
- "write-0-rtt"
- "write-1rrt-0"
- "write-1rrt-1"
- "write-handshake"
- "write-initial"

```
