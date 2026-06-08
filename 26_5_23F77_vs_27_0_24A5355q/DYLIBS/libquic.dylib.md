## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-5812.122.1.0.0
-  __TEXT.__text: 0xc9bf0
-  __TEXT.__auth_stubs: 0x1ab0
+6681.0.372.502.1
+  __TEXT.__text: 0xca734
   __TEXT.__objc_methlist: 0x244
-  __TEXT.__const: 0x3c5
-  __TEXT.__cstring: 0x8697
-  __TEXT.__oslogstring: 0x1129e
-  __TEXT.__unwind_info: 0xd80
-  __TEXT.__objc_classname: 0xa
-  __TEXT.__objc_methname: 0x7e6
-  __TEXT.__objc_methtype: 0xcb9
-  __TEXT.__objc_stubs: 0x660
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x24d0
+  __TEXT.__const: 0x3a5
+  __TEXT.__cstring: 0x868b
+  __TEXT.__oslogstring: 0x1192b
+  __TEXT.__unwind_info: 0xcf8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2508
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd60
-  __AUTH_CONST.__const: 0xd10
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xcd0
   __AUTH_CONST.__cfstring: 0x1320
   __AUTH_CONST.__objc_const: 0xf8
+  __AUTH_CONST.__auth_got: 0xd98
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x110
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x58
+  __DATA.__data: 0x6c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x5b0
-  __DATA_DIRTY.__data: 0x14
-  __DATA_DIRTY.__bss: 0x6a8
+  __DATA.__bss: 0x528
+  __DATA_DIRTY.__data: 0x1c
+  __DATA_DIRTY.__bss: 0x690
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC94EF9D-E87A-3BA3-93DC-428CBD93A6AD
-  Functions: 1147
-  Symbols:   3142
-  CStrings:  2823
+  UUID: C59A0B90-580D-3D9B-B753-8B78DE0DAC69
+  Functions: 1139
+  Symbols:   3132
+  CStrings:  2728
 
Symbols:
+ _____quic_signpost_is_enabled_block_invoke.2684
+ _____quic_signpost_is_enabled_block_invoke.3189
+ _____quic_signpost_is_enabled_block_invoke.3709
+ _____quic_signpost_is_enabled_block_invoke.3939
+ _____quic_signpost_is_enabled_block_invoke.4790
+ _____quic_signpost_is_enabled_block_invoke.685
+ _____quic_signpost_is_enabled_block_invoke.950
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.101.4142
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.107
+ ___block_descriptor_tmp.11.4035
+ ___block_descriptor_tmp.113
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.1173
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.12.2694
+ ___block_descriptor_tmp.12.3562
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.123
+ ___block_descriptor_tmp.128
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.13.2322
+ ___block_descriptor_tmp.13.3568
+ ___block_descriptor_tmp.13.4005
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.14.2348
+ ___block_descriptor_tmp.14.2620
+ ___block_descriptor_tmp.14.3101
+ ___block_descriptor_tmp.140
+ ___block_descriptor_tmp.143
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.149.4283
+ ___block_descriptor_tmp.15.3605
+ ___block_descriptor_tmp.15.3847
+ ___block_descriptor_tmp.15.4845
+ ___block_descriptor_tmp.150
+ ___block_descriptor_tmp.150.4282
+ ___block_descriptor_tmp.156
+ ___block_descriptor_tmp.157
+ ___block_descriptor_tmp.16.3286
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.164.4296
+ ___block_descriptor_tmp.167.4245
+ ___block_descriptor_tmp.1745
+ ___block_descriptor_tmp.1875
+ ___block_descriptor_tmp.19.376
+ ___block_descriptor_tmp.19.4002
+ ___block_descriptor_tmp.1951
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.2048
+ ___block_descriptor_tmp.205
+ ___block_descriptor_tmp.2072
+ ___block_descriptor_tmp.209
+ ___block_descriptor_tmp.21.3691
+ ___block_descriptor_tmp.21.3848
+ ___block_descriptor_tmp.210
+ ___block_descriptor_tmp.212
+ ___block_descriptor_tmp.2175
+ ___block_descriptor_tmp.227
+ ___block_descriptor_tmp.228
+ ___block_descriptor_tmp.229
+ ___block_descriptor_tmp.230
+ ___block_descriptor_tmp.2316
+ ___block_descriptor_tmp.239
+ ___block_descriptor_tmp.240
+ ___block_descriptor_tmp.241
+ ___block_descriptor_tmp.2476
+ ___block_descriptor_tmp.25.3999
+ ___block_descriptor_tmp.26.3998
+ ___block_descriptor_tmp.261
+ ___block_descriptor_tmp.2613
+ ___block_descriptor_tmp.264
+ ___block_descriptor_tmp.27.182
+ ___block_descriptor_tmp.27.2690
+ ___block_descriptor_tmp.27.3849
+ ___block_descriptor_tmp.28.2723
+ ___block_descriptor_tmp.2851
+ ___block_descriptor_tmp.29.187
+ ___block_descriptor_tmp.2980
+ ___block_descriptor_tmp.30.1954
+ ___block_descriptor_tmp.30.2691
+ ___block_descriptor_tmp.31.2715
+ ___block_descriptor_tmp.31.3995
+ ___block_descriptor_tmp.33.2692
+ ___block_descriptor_tmp.33.3850
+ ___block_descriptor_tmp.3354
+ ___block_descriptor_tmp.34.2711
+ ___block_descriptor_tmp.3473
+ ___block_descriptor_tmp.37.3707
+ ___block_descriptor_tmp.37.3992
+ ___block_descriptor_tmp.38.3851
+ ___block_descriptor_tmp.40.1164
+ ___block_descriptor_tmp.40.2693
+ ___block_descriptor_tmp.4009
+ ___block_descriptor_tmp.44.3852
+ ___block_descriptor_tmp.4522
+ ___block_descriptor_tmp.4564
+ ___block_descriptor_tmp.4628
+ ___block_descriptor_tmp.463
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.4788
+ ___block_descriptor_tmp.49.3853
+ ___block_descriptor_tmp.5.2399
+ ___block_descriptor_tmp.5.3431
+ ___block_descriptor_tmp.5.3487
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.53.3854
+ ___block_descriptor_tmp.55.4715
+ ___block_descriptor_tmp.56.2625
+ ___block_descriptor_tmp.57
+ ___block_descriptor_tmp.59
+ ___block_descriptor_tmp.6.3187
+ ___block_descriptor_tmp.6.3805
+ ___block_descriptor_tmp.6.458
+ ___block_descriptor_tmp.62
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.67
+ ___block_descriptor_tmp.683
+ ___block_descriptor_tmp.7.4034
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.72.3855
+ ___block_descriptor_tmp.75
+ ___block_descriptor_tmp.78.2671
+ ___block_descriptor_tmp.78.3858
+ ___block_descriptor_tmp.79
+ ___block_descriptor_tmp.8.2611
+ ___block_descriptor_tmp.8.478
+ ___block_descriptor_tmp.80.2778
+ ___block_descriptor_tmp.81.2775
+ ___block_descriptor_tmp.81.3856
+ ___block_descriptor_tmp.82.2768
+ ___block_descriptor_tmp.82.4046
+ ___block_descriptor_tmp.86.3836
+ ___block_descriptor_tmp.88.3837
+ ___block_descriptor_tmp.89.4066
+ ___block_descriptor_tmp.9.301
+ ___block_descriptor_tmp.91.3979
+ ___block_descriptor_tmp.948
+ ___block_descriptor_tmp.97
+ ___block_literal_global.105
+ ___block_literal_global.111
+ ___block_literal_global.121
+ ___block_literal_global.131
+ ___block_literal_global.137
+ ___block_literal_global.1873
+ ___block_literal_global.207
+ ___block_literal_global.2070
+ ___block_literal_global.2173
+ ___block_literal_global.232
+ ___block_literal_global.2474
+ ___block_literal_global.263
+ ___block_literal_global.2680
+ ___block_literal_global.3183
+ ___block_literal_global.3700
+ ___block_literal_global.3804
+ ___block_literal_global.417
+ ___block_literal_global.456
+ ___block_literal_global.4626
+ ___block_literal_global.4775
+ ___block_literal_global.629
+ ___block_literal_global.93
+ ___block_literal_global.944
+ ___os_log_helper_1_2_14_8_34_4_0_4_0_4_0_4_0_4_0_8_34_8_34_4_0_4_0_4_0_4_0_4_0_4_0
+ ___os_log_helper_1_2_8_8_34_8_34_8_34_8_34_8_0_4_0_8_32_8_32
+ ___quic_conn_application_close_async_block_invoke
+ ___quic_conn_application_close_async_block_invoke_2
+ ___quic_conn_cleanup_paths_block_invoke
+ ___quic_conn_copy_info_block_invoke.161
+ ___quic_conn_initialize_inner_block_invoke.201
+ ___quic_conn_link_advisory_block_invoke.155
+ ___quic_conn_set_metadata_handlers_block_invoke.52
+ ___quic_conn_set_metadata_handlers_block_invoke.54
+ ___quic_conn_set_metadata_handlers_block_invoke.56
+ ___quic_conn_set_metadata_handlers_block_invoke.58
+ ___quic_conn_set_metadata_handlers_block_invoke.68
+ ___quic_conn_set_metadata_handlers_block_invoke_2.45
+ ___quic_conn_set_metadata_handlers_block_invoke_2.60
+ ___quic_conn_set_metadata_handlers_block_invoke_2.69
+ ___quic_conn_set_metadata_handlers_block_invoke_3.46
+ ___quic_conn_set_metadata_handlers_block_invoke_3.63
+ ___quic_conn_set_metadata_handlers_block_invoke_3.73
+ ___quic_conn_set_metadata_handlers_block_invoke_4.64
+ ___quic_conn_set_metadata_handlers_block_invoke_4.74
+ ___quic_conn_set_mss_block_invoke.87
+ ___quic_crypto_finalize_output_frames_block_invoke.84
+ ___quic_crypto_tls_ready_inner_block_invoke.77
+ ___quic_frame_process_DATAGRAM_block_invoke.165
+ ___quic_migration_begin_validation_block_invoke
+ ___quic_migration_evaluate_server_block_invoke.32
+ ___quic_path_release_cid_block_invoke
+ ___quic_signpost_is_enabled._quic_signposts_enabled.2681
+ ___quic_signpost_is_enabled._quic_signposts_enabled.3184
+ ___quic_signpost_is_enabled._quic_signposts_enabled.3701
+ ___quic_signpost_is_enabled._quic_signposts_enabled.3937
+ ___quic_signpost_is_enabled._quic_signposts_enabled.4776
+ ___quic_signpost_is_enabled._quic_signposts_enabled.630
+ ___quic_signpost_is_enabled._quic_signposts_enabled.945
+ ___quic_signpost_is_enabled._quic_signposts_once.2679
+ ___quic_signpost_is_enabled._quic_signposts_once.3182
+ ___quic_signpost_is_enabled._quic_signposts_once.3699
+ ___quic_signpost_is_enabled._quic_signposts_once.3936
+ ___quic_signpost_is_enabled._quic_signposts_once.4774
+ ___quic_signpost_is_enabled._quic_signposts_once.628
+ ___quic_signpost_is_enabled._quic_signposts_once.943
+ _nw_interface_get_link_quality
+ _nw_interface_type_get_description
+ _nw_quic_connection_get_initial_destination_connection_id
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x8
+ _quic_cid_entry_set_stateless_reset_token
+ _quic_conn_announce_new_cids
+ _quic_conn_keepalive_reconfigure
+ _quic_conn_refresh_stateless_reset_token
+ _quic_conn_send_frames
+ _quic_frame_free_APPLICATION_CLOSE
+ _quic_frame_free_CONNECTION_CLOSE
+ _quic_get_flow_stats
+ _quic_migration_fallback_is_better
+ _quic_migration_fallback_threshold_ms
+ _quic_migration_get_multipath_type
+ _quic_migration_ignore_lqm
+ _quic_migration_pulse_start
+ _quic_migration_report_event
+ _quic_migration_timer
+ _quic_migration_timer_reschedule
+ _quic_path_get_lqm
+ _quic_path_lqm_description
+ _quic_path_release_cid
+ _quic_pulse_timeout_secs
+ _quic_recovery_get_pto_count
+ _quic_recovery_max_pto_duration_msec
+ _uuid_generate_random
- _____quic_signpost_is_enabled_block_invoke.2729
- _____quic_signpost_is_enabled_block_invoke.3230
- _____quic_signpost_is_enabled_block_invoke.3750
- _____quic_signpost_is_enabled_block_invoke.3987
- _____quic_signpost_is_enabled_block_invoke.4831
- _____quic_signpost_is_enabled_block_invoke.650
- _____quic_signpost_is_enabled_block_invoke.916
- ___block_descriptor_tmp.101.3865
- ___block_descriptor_tmp.104
- ___block_descriptor_tmp.105
- ___block_descriptor_tmp.11.4082
- ___block_descriptor_tmp.110
- ___block_descriptor_tmp.111
- ___block_descriptor_tmp.1138
- ___block_descriptor_tmp.117
- ___block_descriptor_tmp.12.2738
- ___block_descriptor_tmp.12.3603
- ___block_descriptor_tmp.120
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.126
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.13.2251
- ___block_descriptor_tmp.13.3609
- ___block_descriptor_tmp.13.4053
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.131
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.137
- ___block_descriptor_tmp.14.2277
- ___block_descriptor_tmp.14.2671
- ___block_descriptor_tmp.14.3142
- ___block_descriptor_tmp.145
- ___block_descriptor_tmp.148
- ___block_descriptor_tmp.148.4315
- ___block_descriptor_tmp.149.4321
- ___block_descriptor_tmp.15.3646
- ___block_descriptor_tmp.15.3887
- ___block_descriptor_tmp.15.4886
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.16.3327
- ___block_descriptor_tmp.160.4330
- ___block_descriptor_tmp.161.4333
- ___block_descriptor_tmp.166.4338
- ___block_descriptor_tmp.167.4342
- ___block_descriptor_tmp.170
- ___block_descriptor_tmp.1806
- ___block_descriptor_tmp.1880
- ___block_descriptor_tmp.19.4050
- ___block_descriptor_tmp.1977
- ___block_descriptor_tmp.20.4049
- ___block_descriptor_tmp.2001
- ___block_descriptor_tmp.203
- ___block_descriptor_tmp.206
- ___block_descriptor_tmp.21.3732
- ___block_descriptor_tmp.21.3888
- ___block_descriptor_tmp.2104
- ___block_descriptor_tmp.218
- ___block_descriptor_tmp.219
- ___block_descriptor_tmp.224
- ___block_descriptor_tmp.2245
- ___block_descriptor_tmp.225
- ___block_descriptor_tmp.231
- ___block_descriptor_tmp.232
- ___block_descriptor_tmp.233
- ___block_descriptor_tmp.234
- ___block_descriptor_tmp.2407
- ___block_descriptor_tmp.255
- ___block_descriptor_tmp.2578
- ___block_descriptor_tmp.258
- ___block_descriptor_tmp.26.4046
- ___block_descriptor_tmp.2664
- ___block_descriptor_tmp.27.2735
- ___block_descriptor_tmp.27.3889
- ___block_descriptor_tmp.27.394
- ___block_descriptor_tmp.28.2767
- ___block_descriptor_tmp.2894
- ___block_descriptor_tmp.29.180
- ___block_descriptor_tmp.30.1883
- ___block_descriptor_tmp.30.2736
- ___block_descriptor_tmp.3021
- ___block_descriptor_tmp.31.2759
- ___block_descriptor_tmp.31.4043
- ___block_descriptor_tmp.32.4042
- ___block_descriptor_tmp.33.3890
- ___block_descriptor_tmp.3395
- ___block_descriptor_tmp.34.2755
- ___block_descriptor_tmp.35
- ___block_descriptor_tmp.3514
- ___block_descriptor_tmp.37.3748
- ___block_descriptor_tmp.37.4039
- ___block_descriptor_tmp.38.3891
- ___block_descriptor_tmp.40.2737
- ___block_descriptor_tmp.4057
- ___block_descriptor_tmp.41.4036
- ___block_descriptor_tmp.428
- ___block_descriptor_tmp.45.4033
- ___block_descriptor_tmp.4565
- ___block_descriptor_tmp.46.3892
- ___block_descriptor_tmp.4607
- ___block_descriptor_tmp.4671
- ___block_descriptor_tmp.48.3920
- ___block_descriptor_tmp.4829
- ___block_descriptor_tmp.5.2328
- ___block_descriptor_tmp.5.3472
- ___block_descriptor_tmp.5.3528
- ___block_descriptor_tmp.50
- ___block_descriptor_tmp.52
- ___block_descriptor_tmp.54.3893
- ___block_descriptor_tmp.56.2676
- ___block_descriptor_tmp.56.3894
- ___block_descriptor_tmp.58.3895
- ___block_descriptor_tmp.6.3228
- ___block_descriptor_tmp.6.3848
- ___block_descriptor_tmp.6.423
- ___block_descriptor_tmp.60
- ___block_descriptor_tmp.63
- ___block_descriptor_tmp.648
- ___block_descriptor_tmp.66
- ___block_descriptor_tmp.68
- ___block_descriptor_tmp.7.4081
- ___block_descriptor_tmp.71
- ___block_descriptor_tmp.73
- ___block_descriptor_tmp.74
- ___block_descriptor_tmp.76
- ___block_descriptor_tmp.76.3904
- ___block_descriptor_tmp.78.2813
- ___block_descriptor_tmp.78.3896
- ___block_descriptor_tmp.8.2662
- ___block_descriptor_tmp.8.443
- ___block_descriptor_tmp.80.3901
- ___block_descriptor_tmp.81.3897
- ___block_descriptor_tmp.82.2787
- ___block_descriptor_tmp.83.3898
- ___block_descriptor_tmp.84.4093
- ___block_descriptor_tmp.9.281
- ___block_descriptor_tmp.91.4114
- ___block_descriptor_tmp.914
- ___block_descriptor_tmp.92
- ___block_descriptor_tmp.93
- ___block_literal_global.107
- ___block_literal_global.113
- ___block_literal_global.123
- ___block_literal_global.133
- ___block_literal_global.139
- ___block_literal_global.1804
- ___block_literal_global.1999
- ___block_literal_global.205
- ___block_literal_global.2102
- ___block_literal_global.228
- ___block_literal_global.2405
- ___block_literal_global.257
- ___block_literal_global.2576
- ___block_literal_global.26
- ___block_literal_global.2725
- ___block_literal_global.3224
- ___block_literal_global.365
- ___block_literal_global.3741
- ___block_literal_global.3847
- ___block_literal_global.421
- ___block_literal_global.4669
- ___block_literal_global.4816
- ___block_literal_global.594
- ___block_literal_global.910
- ___block_literal_global.95
- ___quic_cc_new_reno_identifier_block_invoke
- ___quic_conn_copy_info_block_invoke.163
- ___quic_conn_handle_stop_inner_block_invoke_2
- ___quic_conn_link_advisory_block_invoke.157
- ___quic_conn_migrate_to_path_block_invoke
- ___quic_conn_set_metadata_handlers_block_invoke.53
- ___quic_conn_set_metadata_handlers_block_invoke.55
- ___quic_conn_set_metadata_handlers_block_invoke.57
- ___quic_conn_set_metadata_handlers_block_invoke.59
- ___quic_conn_set_metadata_handlers_block_invoke.69
- ___quic_conn_set_metadata_handlers_block_invoke_2.44
- ___quic_conn_set_metadata_handlers_block_invoke_2.61
- ___quic_conn_set_metadata_handlers_block_invoke_2.70
- ___quic_conn_set_metadata_handlers_block_invoke_3.47
- ___quic_conn_set_metadata_handlers_block_invoke_3.64
- ___quic_conn_set_metadata_handlers_block_invoke_3.74
- ___quic_conn_set_metadata_handlers_block_invoke_4.65
- ___quic_conn_set_metadata_handlers_block_invoke_4.75
- ___quic_conn_set_metadata_handlers_block_invoke_5.79
- ___quic_conn_set_mss_block_invoke.89
- ___quic_crypto_finalize_output_frames_block_invoke.80
- ___quic_crypto_tls_ready_inner_block_invoke.73
- ___quic_frame_process_DATAGRAM_block_invoke.164
- ___quic_migration_evaluate_server_block_invoke.33
- ___quic_migration_path_event_block_invoke.21
- ___quic_signpost_is_enabled._quic_signposts_enabled.2726
- ___quic_signpost_is_enabled._quic_signposts_enabled.3225
- ___quic_signpost_is_enabled._quic_signposts_enabled.3742
- ___quic_signpost_is_enabled._quic_signposts_enabled.3985
- ___quic_signpost_is_enabled._quic_signposts_enabled.4817
- ___quic_signpost_is_enabled._quic_signposts_enabled.595
- ___quic_signpost_is_enabled._quic_signposts_enabled.911
- ___quic_signpost_is_enabled._quic_signposts_once.2724
- ___quic_signpost_is_enabled._quic_signposts_once.3223
- ___quic_signpost_is_enabled._quic_signposts_once.3740
- ___quic_signpost_is_enabled._quic_signposts_once.3984
- ___quic_signpost_is_enabled._quic_signposts_once.4815
- ___quic_signpost_is_enabled._quic_signposts_once.593
- ___quic_signpost_is_enabled._quic_signposts_once.909
- _g_new_reno_identifier
- _objc_retainAutoreleasedReturnValue
- _quic_cc_new_reno_ack_begin
- _quic_cc_new_reno_ack_end
- _quic_cc_new_reno_can_send_packet
- _quic_cc_new_reno_create
- _quic_cc_new_reno_destroy
- _quic_cc_new_reno_fillout_data_transfer_snapshot
- _quic_cc_new_reno_get_allowed_cwnd
- _quic_cc_new_reno_get_bytes_in_flight
- _quic_cc_new_reno_identifier.onceToken
- _quic_cc_new_reno_idle_timeout
- _quic_cc_new_reno_link_flow_controlled
- _quic_cc_new_reno_mss_changed
- _quic_cc_new_reno_packet_acked
- _quic_cc_new_reno_packet_discarded
- _quic_cc_new_reno_packet_sent
- _quic_cc_new_reno_packets_lost
- _quic_cc_new_reno_persistent_congestion
- _quic_cc_new_reno_process_ecn
- _quic_cc_new_reno_process_link_congestion_info
- _quic_cc_new_reno_reset
- _quic_cc_new_reno_spurious_rxmt
- _quic_cc_new_reno_switch
- _quic_conn_annouce_new_cids
- _quic_disable_cubic
- _quic_frame_alloc_RETIRE_CONNECTION_ID
- _quic_new_reno_congestion_event
- _quic_path_get_has_assigned_scid
- _quic_path_get_nw_interface
- _quic_path_set_migration_pending
- _quic_path_set_spin_value
- _quic_path_update_bdp
- _quic_recovery_max_pto_count
CStrings:
+ "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u\n\tMigration events: %u, paths validated: %u\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
+ "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u, ECN state: %s, L4S: %s\n\tRTT: base %llu ms, network %llu ms, latest %llu ms, minimum %llu ms, smoothed %llu ms (variance %llu ms)\n\tPath MTU: %hu, minimum MSS: %hu\n\tMigration events: %u, paths validated: %u\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
+ "%{public}s %{public}s [%{public}s-%{public}s] Connection in PTO recovery for >= %u ms, closing connection"
+ "%{public}s %{public}s [%{public}s-%{public}s] RTT too low for immediate fallback (%llu ms < %u ms) and LQM below threshold (current: %s, fallback: %s)"
+ "%{public}s %{public}s [%{public}s-%{public}s] cleaning up unusable paths"
+ "%{public}s %{public}s [%{public}s-%{public}s] closing connection because we have no more viable paths"
+ "%{public}s %{public}s [%{public}s-%{public}s] fallback event, interface %{public}s, should fallback? %d, weak? %d, preferred? %d"
+ "%{public}s %{public}s [%{public}s-%{public}s] fallback path RTT %llu ms >= current path RTT %llu ms"
+ "%{public}s %{public}s [%{public}s-%{public}s] ignoring fallback event since active migration is disabled"
+ "%{public}s %{public}s [%{public}s-%{public}s] keep-alive frame acknowledged (%s) with %u outstanding"
+ "%{public}s %{public}s [%{public}s-%{public}s] keepalive timer fired with no interval set"
+ "%{public}s %{public}s [%{public}s-%{public}s] migrated to path over %{public}s (%lx)"
+ "%{public}s %{public}s [%{public}s-%{public}s] migrating because PTO count is > %u"
+ "%{public}s %{public}s [%{public}s-%{public}s] migrating because fallback path RTT is better (%llu ms < %llu ms)"
+ "%{public}s %{public}s [%{public}s-%{public}s] phone call relay optimizations enabled"
+ "%{public}s %{public}s [%{public}s-%{public}s] pulse timer fired, closing connection"
+ "%{public}s %{public}s [%{public}s-%{public}s] re-probing path on %{public}s (challenges sent %u)"
+ "%{public}s %{public}s [%{public}s-%{public}s] received NEW_CONNECTION_ID with CID that has already been seen with different sequence number"
+ "%{public}s %{public}s [%{public}s-%{public}s] received NEW_CONNECTION_ID with CID that has already been seen with different token"
+ "%{public}s %{public}s [%{public}s-%{public}s] refreshing stateless reset token for initial CID"
+ "%{public}s %{public}s [%{public}s-%{public}s] reusing CID on path over %{public}s"
+ "%{public}s %{public}s [%{public}s-%{public}s] sending keep-alive frame (%s), already have %u outstanding"
+ "%{public}s %{public}s [%{public}s-%{public}s] server %{public}s migration, migration feature %{public}s"
+ "%{public}s %{public}s [%{public}s-%{public}s] started keep-alive timer for %s (%llu seconds)"
+ "%{public}s %{public}s [%{public}s-%{public}s] tried to remove a non-existing path %lx"
+ "%{public}s %{public}s [%{public}s-%{public}s] unable to find path for %{public}s"
+ "%{public}s %{public}s [%{public}s-%{public}s] updating stateless reset token for CID seq %llu"
+ "%{public}s initial CID not found in local CID array"
+ "%{public}s migration event %u: time %u ms, migration time %u ms, RTT %u ms -> %u ms, type '%{public}s' -> '%{public}s', LQM %d -> %d, fallback? %d primary? %d priority? %d loss? %d"
+ "%{public}s new_path is null or 0"
+ "%{public}s provided DCID is larger than maximum allowed length"
+ "%{public}s quic_path_get_is_fallback_path(fallback_path) is null or 0"
+ "%{public}s unable to query interface for path %lx (ifname %{public}s, state %{public}s)"
+ "%{public}s unable to query original interface for path %lx (ifname %{public}s, state %{public}s)"
+ "%{public}s unable to send NEW_CONNECTION_ID frame for stateless reset token refresh"
+ "<null>"
+ "B16@?0^{quic_path=Q^{nw_interface}C[21C][21C]cI[6{?=QQ}]{quic_frame_list=^{quic_frame}^^{quic_frame}}^{quic_rtt}[16c]QQ{?=^{quic_path}^^{quic_path}}QQIIQQQ^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_pacer}^{quic_pmtud}^{quic_loss_recovery_path_state}^{quic_ecn_path_state}{quic_path_statistics=QQQQIIII}CCSSSCCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b7[2c]}8"
+ "NEW_CONNECTION_ID: invalid sequence number"
+ "NEW_CONNECTION_ID: invalid token"
+ "application"
+ "conn->unacked_keepalive_count[effective_type]"
+ "conn->unacked_keepalive_count[type]"
+ "does NOT support"
+ "fallback_threshold_ms"
+ "good"
+ "ignore_lqm"
+ "max_pto_duration_msec"
+ "minimal"
+ "moderate"
+ "no more viable paths"
+ "probe-connectivity"
+ "pulse timeout"
+ "pulse_timeout"
+ "quic_cid_entry_set_stateless_reset_token"
+ "quic_conn_announce_new_cids"
+ "quic_conn_refresh_stateless_reset_token"
+ "quic_migration_fallback_is_better"
+ "quic_migration_get_multipath_type"
+ "quic_migration_report_event"
+ "quic_migration_timer"
+ "quic_path_get_lqm"
+ "quic_path_lqm_description"
+ "quic_recovery_get_pto_count"
+ "receiving"
+ "suports"
- "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Keep-alives sent/acknowledged: %u/%u\n\tMigration events: %u, paths validated: %u\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
- "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Keep-alives sent/acknowledged: %u/%u, ECN state: %s, L4S: %s\n\tRTT: base %llu ms, network %llu ms, latest %llu ms, minimum %llu ms, smoothed %llu ms (variance %llu ms)\n\tPath MTU: %hu, minimum MSS: %hu\n\tMigration events: %u, paths validated: %u\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
- "%{public}s %{public}s [%{public}s-%{public}s] Connection exceeded max PTO count %u, closing connection"
- "%{public}s %{public}s [%{public}s-%{public}s] RTT too low for fallback"
- "%{public}s %{public}s [%{public}s-%{public}s] fallback event, interface %{public}s, should fallback? %d, weak? %d"
- "%{public}s %{public}s [%{public}s-%{public}s] keep-alive frame acknowledged with %u outstanding"
- "%{public}s %{public}s [%{public}s-%{public}s] received NEW_CONNECTION_ID with CID that has already been seen with different sequence number or token"
- "%{public}s %{public}s [%{public}s-%{public}s] sending keep-alive frame, already have %u outstanding"
- "%{public}s %{public}s [%{public}s-%{public}s] started keep-alive timer (%llu seconds)"
- "%{public}s %{public}s [%{public}s-%{public}s] tried to remove a non-existing path on %{public}s"
- "%{public}s algorithm is null"
- "%{public}s cc is null"
- "%{public}s create new reno %p"
- "%{public}s destroying new reno %p"
- "%{public}s entering recovery"
- "%{public}s keepalive: now: %llu, last packet: %llu delta: %llu, interval: %llu"
- "%{public}s largest_acked_sent_time is null or 0"
- "%{public}s largest_lost_packet_sent_time is null or 0"
- "%{public}s new_reno is null"
- "%{public}s new_reno->c.prev_ssthresh > 0 is null or 0"
- "%{public}s new_reno->prev_cwnd > 0 is null or 0"
- "%{public}s sent_time is null or 0"
- "%{public}s total_lost_bytes_in_flight is null or 0"
- "%{public}s unable to find DCID %{public}s"
- "%{public}s unable to find path for %{public}s"
- "%{public}s unable to query interface for path %lx"
- "%{public}s unable to query original interface for path %lx"
- ".cxx_destruct"
- "@\"NSMutableDictionary\""
- "@16@0:8"
- "@20@0:8C16"
- "@20@0:8i16"
- "@24@0:8@16"
- "@24@0:8^{quiclog_event=i[4c]Q(?={?=QQQQQ[32c][21C][21C][21C]cccC{quic_preferred_address={in_addr=I}S{in6_addr=(?=[16C][8S][4I])}S[21C][16C]}QQQQQQ}{?=i[4c]^{packet_header}{quic_frame_list=^{quic_frame}^^{quic_frame}}c[3c](?=iC)}{?=QCCC[1c]C[3c]}{?=QQQQQQQQQc[7c]}{?=CCC}{?=QCCC[5c]}){?=^{quiclog_event}}}16"
- "@32@0:8@16^{packet_header=QQQ*CC[41c][41c][4c]}24"
- "@32@0:8@16^{quic_frame_list=^{quic_frame}^^{quic_frame}}24"
- "@32@0:8@16^{quiclog_event=i[4c]Q(?={?=QQQQQ[32c][21C][21C][21C]cccC{quic_preferred_address={in_addr=I}S{in6_addr=(?=[16C][8S][4I])}S[21C][16C]}QQQQQQ}{?=i[4c]^{packet_header}{quic_frame_list=^{quic_frame}^^{quic_frame}}c[3c](?=iC)}{?=QCCC[1c]C[3c]}{?=QQQQQQQQQc[7c]}{?=CCC}{?=QCCC[5c]}){?=^{quiclog_event}}}24"
- "@36@0:8@16@24c32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24r*32"
- "@44@0:8@16@24c32r*36"
- "@48@0:8@16@24Q32r*40"
- "@48@0:8@16@24r*32r*40"
- "B"
- "JSONObjectWithData:options:error:"
- "NEW_CONNECTION_ID: invalid sequence number or token"
- "QUICLog"
- "^{quiclog_event=i[4c]Q(?={?=QQQQQ[32c][21C][21C][21C]cccC{quic_preferred_address={in_addr=I}S{in6_addr=(?=[16C][8S][4I])}S[21C][16C]}QQQQQQ}{?=i[4c]^{packet_header}{quic_frame_list=^{quic_frame}^^{quic_frame}}c[3c](?=iC)}{?=QCCC[1c]C[3c]}{?=QQQQQQQQQc[7c]}{?=CCC}{?=QCCC[5c]}){?=^{quiclog_event}}}20@0:8i16"
- "^{quiclog_event=i[4c]Q(?={?=QQQQQ[32c][21C][21C][21C]cccC{quic_preferred_address={in_addr=I}S{in6_addr=(?=[16C][8S][4I])}S[21C][16C]}QQQQQQ}{?=i[4c]^{packet_header}{quic_frame_list=^{quic_frame}^^{quic_frame}}c[3c](?=iC)}{?=QCCC[1c]C[3c]}{?=QQQQQQQQQc[7c]}{?=CCC}{?=QCCC[5c]}){?=^{quiclog_event}}}28@0:8i16Q20"
- "addEventValues:event:"
- "addFrameList:frame_list:"
- "addMandatoryCharPointerToObject:key:value:function_name:"
- "addMandatorySuperBoolToObject:key:value:function_name:"
- "addMandatoryUint64ToObject:key:value:function_name:"
- "addObject:"
- "addOptionalCharPointerToObject:key:value:"
- "addOptionalSuperBoolToObject:key:value:"
- "addOptionalUint64ToObject:key:value:"
- "addPacketHeader:header:"
- "categoryString:"
- "congestionStateString:"
- "congestionTriggerString:"
- "conn->unacked_keepalive_count"
- "createEvent:"
- "createEvent:timestamp:"
- "createFileAtPath:contents:attributes:"
- "dataUsingEncoding:"
- "dataWithJSONObject:options:error:"
- "dealloc"
- "deallocEvent:"
- "defaultManager"
- "dictToJsonString:"
- "disableTimestamps:"
- "disable_cubic"
- "disable_timestamps"
- "dumpData:"
- "eventTypeString:"
- "events_list"
- "flowTypeString:"
- "i24@0:8^{quic_packet=*****[21C][21C]CCCCCCSSS(?=SS)(?=*^I)iIQQQ^{quic_path}{?=^{quic_frame}^^{quic_frame}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b17[4C]}16"
- "init"
- "initWithData:encoding:"
- "jsonStringToDict:"
- "logCongestionStateUpdated:new_state:trigger:"
- "logStreamTypeSet:owner:old_state:new_state:"
- "max_pto_count"
- "metricsUpdated:smoothed_rtt:latest_rtt:rtt_variance:pto_count:congestion_window:bytes_in_flight:ssthresh:packets_in_flight:in_recovery:"
- "new_reno"
- "new_reno->c.congestion_window"
- "numberWithInt:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "ownerString:"
- "packetLost:trigger:"
- "packetLostTriggerString:"
- "packetReceived:isCoalesced:"
- "packetSent:timestamp:"
- "packetSentReceivedTriggerString:"
- "packetType:"
- "packetTypeString:"
- "parametersSet:resumption_allowed:early_data_enabled:tls_cipher:original_dcid:initial_scid:retry_scid:disable_active_migration:max_idle_timeout:max_udp_payload_size:ack_delay_exponent:max_ack_delay:active_cid_limit:initial_max_data:initial_msd_bidi_remote:initial_msd_bidi_local:initial_msd_uni:initial_ms_bidi:initial_ms_uni:preferred_address:"
- "processCongestionStateUpdated:"
- "processMetricsUpdated:"
- "processPacketLost:"
- "processPacketSentAndPacketReceived:"
- "processParametersSet:"
- "processStreamStateUpdated:"
- "processStreamTypeSet:"
- "quic_cc_new_reno_ack_begin"
- "quic_cc_new_reno_ack_end"
- "quic_cc_new_reno_can_send_packet"
- "quic_cc_new_reno_create"
- "quic_cc_new_reno_destroy"
- "quic_cc_new_reno_fillout_data_transfer_snapshot"
- "quic_cc_new_reno_get_allowed_cwnd"
- "quic_cc_new_reno_get_bytes_in_flight"
- "quic_cc_new_reno_idle_timeout"
- "quic_cc_new_reno_link_flow_controlled"
- "quic_cc_new_reno_mss_changed"
- "quic_cc_new_reno_packet_acked"
- "quic_cc_new_reno_packet_discarded"
- "quic_cc_new_reno_packet_sent"
- "quic_cc_new_reno_packets_lost"
- "quic_cc_new_reno_persistent_congestion"
- "quic_cc_new_reno_process_ecn"
- "quic_cc_new_reno_process_link_congestion_info"
- "quic_cc_new_reno_reset"
- "quic_cc_new_reno_spurious_rxmt"
- "quic_cc_new_reno_switch"
- "quic_conn_annouce_new_cids"
- "quic_conn_set_metadata_handlers_block_invoke_5"
- "quic_new_reno_congestion_event"
- "quic_path_get_has_assigned_scid"
- "quic_path_get_nw_interface"
- "quic_path_set_migration_pending"
- "quic_path_set_spin_value"
- "quic_path_update_bdp"
- "recieving"
- "setEntryInTopLevelObject:value:"
- "setValue:forKey:"
- "streamSideString:"
- "streamStateUpdated:stream_type:old_state:new_state:stream_side:"
- "streamTypeString:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "top_level_object"
- "v160@0:8C16c20c24r*28^[21C]36^[21C]44^[21C]52c60Q64Q72Q80Q88Q96Q104Q112Q120Q128Q136Q144^{quic_preferred_address={in_addr=I}S{in6_addr=(?=[16C][8S][4I])}S[21C][16C]}152"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8^{quiclog_event=i[4c]Q(?={?=QQQQQ[32c][21C][21C][21C]cccC{quic_preferred_address={in_addr=I}S{in6_addr=(?=[16C][8S][4I])}S[21C][16C]}QQQQQQ}{?=i[4c]^{packet_header}{quic_frame_list=^{quic_frame}^^{quic_frame}}c[3c](?=iC)}{?=QCCC[1c]C[3c]}{?=QQQQQQQQQc[7c]}{?=CCC}{?=QCCC[5c]}){?=^{quiclog_event}}}16"
- "v28@0:8C16C20C24"
- "v28@0:8^{quic_packet=*****[21C][21C]CCCCCCSSS(?=SS)(?=*^I)iIQQQ^{quic_path}{?=^{quic_frame}^^{quic_frame}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b17[4C]}16B24"
- "v28@0:8^{quic_packet=*****[21C][21C]CCCCCCSSS(?=SS)(?=*^I)iIQQQ^{quic_path}{?=^{quic_frame}^^{quic_frame}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b17[4C]}16C24"
- "v32@0:8@16@24"
- "v32@0:8^{quic_packet=*****[21C][21C]CCCCCCSSS(?=SS)(?=*^I)iIQQQ^{quic_path}{?=^{quic_frame}^^{quic_frame}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}^^{quic_packet}}{?=^{quic_packet}}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b17[4C]}16Q24"
- "v36@0:8Q16C24C28C32"
- "v40@0:8Q16C24C28C32C36"
- "v92@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80c88"
- "writeToFile:atomically:"
- "{?=\"stqh_first\"^{quiclog_event}\"stqh_last\"^^{quiclog_event}}"

```
