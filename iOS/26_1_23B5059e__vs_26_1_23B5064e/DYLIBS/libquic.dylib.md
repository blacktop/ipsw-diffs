## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-5569.40.91.0.0
-  __TEXT.__text: 0xcfd14
-  __TEXT.__auth_stubs: 0x1aa0
+5569.40.106.0.1
+  __TEXT.__text: 0xd1b70
+  __TEXT.__auth_stubs: 0x1ab0
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x39d
-  __TEXT.__cstring: 0x8f35
-  __TEXT.__oslogstring: 0x11825
-  __TEXT.__unwind_info: 0xe28
+  __TEXT.__cstring: 0x903f
+  __TEXT.__oslogstring: 0x11a59
+  __TEXT.__unwind_info: 0xe58
   __TEXT.__objc_classname: 0xa
   __TEXT.__objc_methname: 0x7e6
   __TEXT.__objc_methtype: 0xd09
   __TEXT.__objc_stubs: 0x660
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x2408
+  __DATA_CONST.__const: 0x2490
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd58
-  __AUTH_CONST.__const: 0x2560
+  __AUTH_CONST.__auth_got: 0xd60
+  __AUTH_CONST.__const: 0x2580
   __AUTH_CONST.__cfstring: 0x1480
   __AUTH_CONST.__objc_const: 0xf8
   __AUTH.__objc_data: 0x50

   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x50
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x550
+  __DATA.__bss: 0x5c0
   __DATA_DIRTY.__data: 0x14
-  __DATA_DIRTY.__bss: 0x728
+  __DATA_DIRTY.__bss: 0x6a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A8A8CC1-2CFD-3B89-B410-5E91D882AD6F
-  Functions: 1158
-  Symbols:   3181
-  CStrings:  2929
+  UUID: 3B1C6FFC-7AB3-3A39-B8A7-06B5B571588A
+  Functions: 1169
+  Symbols:   3209
+  CStrings:  2944
 
Symbols:
+ _____quic_signpost_is_enabled_block_invoke.2596
+ _____quic_signpost_is_enabled_block_invoke.3140
+ _____quic_signpost_is_enabled_block_invoke.3673
+ _____quic_signpost_is_enabled_block_invoke.3918
+ _____quic_signpost_is_enabled_block_invoke.4808
+ _____quic_signpost_is_enabled_block_invoke.699
+ _____quic_signpost_is_enabled_block_invoke.973
+ ___block_descriptor_tmp.1.3178
+ ___block_descriptor_tmp.10.2114
+ ___block_descriptor_tmp.10.3533
+ ___block_descriptor_tmp.105.4168
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.107
+ ___block_descriptor_tmp.11.2539
+ ___block_descriptor_tmp.11.3396
+ ___block_descriptor_tmp.11.3810
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.117
+ ___block_descriptor_tmp.12.3570
+ ___block_descriptor_tmp.12.4863
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.123
+ ___block_descriptor_tmp.1247
+ ___block_descriptor_tmp.128
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.13.2542
+ ___block_descriptor_tmp.13.3051
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.14.2142
+ ___block_descriptor_tmp.140
+ ___block_descriptor_tmp.149.4281
+ ___block_descriptor_tmp.15.2540
+ ___block_descriptor_tmp.15.2908
+ ___block_descriptor_tmp.15.3975
+ ___block_descriptor_tmp.156
+ ___block_descriptor_tmp.157.4290
+ ___block_descriptor_tmp.158.4294
+ ___block_descriptor_tmp.159
+ ___block_descriptor_tmp.16.3974
+ ___block_descriptor_tmp.160.4247
+ ___block_descriptor_tmp.161.3828
+ ___block_descriptor_tmp.165
+ ___block_descriptor_tmp.1668
+ ___block_descriptor_tmp.17.3224
+ ___block_descriptor_tmp.17.346
+ ___block_descriptor_tmp.17.3811
+ ___block_descriptor_tmp.1746
+ ___block_descriptor_tmp.18.3656
+ ___block_descriptor_tmp.18.4535
+ ___block_descriptor_tmp.1867
+ ___block_descriptor_tmp.196
+ ___block_descriptor_tmp.1969
+ ___block_descriptor_tmp.199
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.204
+ ___block_descriptor_tmp.2108
+ ___block_descriptor_tmp.219
+ ___block_descriptor_tmp.22.3971
+ ___block_descriptor_tmp.220
+ ___block_descriptor_tmp.223
+ ___block_descriptor_tmp.2275
+ ___block_descriptor_tmp.23.3243
+ ___block_descriptor_tmp.23.3812
+ ___block_descriptor_tmp.231
+ ___block_descriptor_tmp.232
+ ___block_descriptor_tmp.233
+ ___block_descriptor_tmp.234
+ ___block_descriptor_tmp.235
+ ___block_descriptor_tmp.236
+ ___block_descriptor_tmp.237
+ ___block_descriptor_tmp.24.2603
+ ___block_descriptor_tmp.24.3241
+ ___block_descriptor_tmp.24.408
+ ___block_descriptor_tmp.2446
+ ___block_descriptor_tmp.2532
+ ___block_descriptor_tmp.254
+ ___block_descriptor_tmp.257
+ ___block_descriptor_tmp.27.2604
+ ___block_descriptor_tmp.27.3968
+ ___block_descriptor_tmp.2764
+ ___block_descriptor_tmp.28.2630
+ ___block_descriptor_tmp.28.3967
+ ___block_descriptor_tmp.2898
+ ___block_descriptor_tmp.29.3813
+ ___block_descriptor_tmp.29.413
+ ___block_descriptor_tmp.3.3769
+ ___block_descriptor_tmp.3.454
+ ___block_descriptor_tmp.30.1749
+ ___block_descriptor_tmp.30.2605
+ ___block_descriptor_tmp.3155
+ ___block_descriptor_tmp.33.2606
+ ___block_descriptor_tmp.33.3964
+ ___block_descriptor_tmp.34.2607
+ ___block_descriptor_tmp.34.3671
+ ___block_descriptor_tmp.34.3814
+ ___block_descriptor_tmp.3438
+ ___block_descriptor_tmp.35.2616
+ ___block_descriptor_tmp.37.2608
+ ___block_descriptor_tmp.37.3961
+ ___block_descriptor_tmp.38.3815
+ ___block_descriptor_tmp.3982
+ ___block_descriptor_tmp.4.1672
+ ___block_descriptor_tmp.4.2958
+ ___block_descriptor_tmp.4.3767
+ ___block_descriptor_tmp.40.2637
+ ___block_descriptor_tmp.41.3958
+ ___block_descriptor_tmp.42.3816
+ ___block_descriptor_tmp.4353
+ ___block_descriptor_tmp.4577
+ ___block_descriptor_tmp.459
+ ___block_descriptor_tmp.46.3817
+ ___block_descriptor_tmp.4640
+ ___block_descriptor_tmp.48.3818
+ ___block_descriptor_tmp.4806
+ ___block_descriptor_tmp.5.2195
+ ___block_descriptor_tmp.5.2530
+ ___block_descriptor_tmp.5.3452
+ ___block_descriptor_tmp.5.4022
+ ___block_descriptor_tmp.50.3819
+ ___block_descriptor_tmp.53.2546
+ ___block_descriptor_tmp.60.4731
+ ___block_descriptor_tmp.697
+ ___block_descriptor_tmp.72.3824
+ ___block_descriptor_tmp.74.3820
+ ___block_descriptor_tmp.78.4037
+ ___block_descriptor_tmp.79.4038
+ ___block_descriptor_tmp.8.3318
+ ___block_descriptor_tmp.80.4039
+ ___block_descriptor_tmp.85.3801
+ ___block_descriptor_tmp.86.4060
+ ___block_descriptor_tmp.9.2609
+ ___block_descriptor_tmp.9.301
+ ___block_descriptor_tmp.9.3329
+ ___block_descriptor_tmp.9.3527
+ ___block_descriptor_tmp.9.3978
+ ___block_descriptor_tmp.971
+ ___block_literal_global.104
+ ___block_literal_global.110
+ ___block_literal_global.116
+ ___block_literal_global.1199
+ ___block_literal_global.125
+ ___block_literal_global.131
+ ___block_literal_global.163
+ ___block_literal_global.1666
+ ___block_literal_global.1865
+ ___block_literal_global.1967
+ ___block_literal_global.201
+ ___block_literal_global.225
+ ___block_literal_global.2273
+ ___block_literal_global.2444
+ ___block_literal_global.256
+ ___block_literal_global.2592
+ ___block_literal_global.3135
+ ___block_literal_global.3665
+ ___block_literal_global.3766
+ ___block_literal_global.452
+ ___block_literal_global.4638
+ ___block_literal_global.4793
+ ___block_literal_global.630
+ ___block_literal_global.7.4020
+ ___block_literal_global.967
+ ___os_log_helper_1_2_9_8_34_8_34_8_34_8_34_4_0_4_0_4_0_4_0_4_0
+ ___quic_conn_check_current_path_block_invoke
+ ___quic_conn_copy_info_block_invoke.154
+ ___quic_conn_idle_state_block_invoke
+ ___quic_conn_is_idle_block_invoke
+ ___quic_conn_link_advisory_block_invoke.148
+ ___quic_conn_outbound_starting_block_invoke
+ ___quic_conn_preferred_path_block_invoke.164
+ ___quic_conn_send_frames_for_key_state_block_invoke.214
+ ___quic_signpost_is_enabled._quic_signposts_enabled.2593
+ ___quic_signpost_is_enabled._quic_signposts_enabled.3136
+ ___quic_signpost_is_enabled._quic_signposts_enabled.3666
+ ___quic_signpost_is_enabled._quic_signposts_enabled.3916
+ ___quic_signpost_is_enabled._quic_signposts_enabled.4794
+ ___quic_signpost_is_enabled._quic_signposts_enabled.631
+ ___quic_signpost_is_enabled._quic_signposts_enabled.968
+ ___quic_signpost_is_enabled._quic_signposts_once.2591
+ ___quic_signpost_is_enabled._quic_signposts_once.3134
+ ___quic_signpost_is_enabled._quic_signposts_once.3664
+ ___quic_signpost_is_enabled._quic_signposts_once.3915
+ ___quic_signpost_is_enabled._quic_signposts_once.4792
+ ___quic_signpost_is_enabled._quic_signposts_once.629
+ ___quic_signpost_is_enabled._quic_signposts_once.966
+ _nw_protocol_definition_set_idle_state_update
+ _quic_conn_check_current_path
+ _quic_conn_idle_state
+ _quic_conn_outbound_starting
+ _quic_migration_begin_validation
+ _quic_path_delayed_validation
+ _quic_recovery_get_ack_eliciting_in_flight
- _____quic_signpost_is_enabled_block_invoke.2578
- _____quic_signpost_is_enabled_block_invoke.3122
- _____quic_signpost_is_enabled_block_invoke.3655
- _____quic_signpost_is_enabled_block_invoke.3900
- _____quic_signpost_is_enabled_block_invoke.4774
- _____quic_signpost_is_enabled_block_invoke.688
- _____quic_signpost_is_enabled_block_invoke.962
- ___block_descriptor_tmp.1.3160
- ___block_descriptor_tmp.10.2096
- ___block_descriptor_tmp.10.3515
- ___block_descriptor_tmp.103
- ___block_descriptor_tmp.104
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.11.2521
- ___block_descriptor_tmp.11.3378
- ___block_descriptor_tmp.11.3793
- ___block_descriptor_tmp.110
- ___block_descriptor_tmp.115
- ___block_descriptor_tmp.12.3552
- ___block_descriptor_tmp.12.4829
- ___block_descriptor_tmp.1236
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.13.2524
- ___block_descriptor_tmp.13.3033
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.132
- ___block_descriptor_tmp.133
- ___block_descriptor_tmp.135
- ___block_descriptor_tmp.14.2124
- ___block_descriptor_tmp.146
- ___block_descriptor_tmp.149.4256
- ___block_descriptor_tmp.15.2522
- ___block_descriptor_tmp.15.2890
- ___block_descriptor_tmp.15.3956
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.158.3812
- ___block_descriptor_tmp.16.3955
- ___block_descriptor_tmp.1650
- ___block_descriptor_tmp.17.3206
- ___block_descriptor_tmp.17.343
- ___block_descriptor_tmp.17.3794
- ___block_descriptor_tmp.1728
- ___block_descriptor_tmp.18.3638
- ___block_descriptor_tmp.18.4501
- ___block_descriptor_tmp.1849
- ___block_descriptor_tmp.189.3757
- ___block_descriptor_tmp.192
- ___block_descriptor_tmp.195
- ___block_descriptor_tmp.1951
- ___block_descriptor_tmp.197
- ___block_descriptor_tmp.208
- ___block_descriptor_tmp.209
- ___block_descriptor_tmp.2090
- ___block_descriptor_tmp.212
- ___block_descriptor_tmp.213
- ___block_descriptor_tmp.214
- ___block_descriptor_tmp.22.3952
- ___block_descriptor_tmp.224
- ___block_descriptor_tmp.225
- ___block_descriptor_tmp.2257
- ___block_descriptor_tmp.226
- ___block_descriptor_tmp.227
- ___block_descriptor_tmp.23.3225
- ___block_descriptor_tmp.23.3795
- ___block_descriptor_tmp.230
- ___block_descriptor_tmp.24.2585
- ___block_descriptor_tmp.24.3223
- ___block_descriptor_tmp.24.397
- ___block_descriptor_tmp.2428
- ___block_descriptor_tmp.247
- ___block_descriptor_tmp.250
- ___block_descriptor_tmp.2514
- ___block_descriptor_tmp.27.2586
- ___block_descriptor_tmp.27.3949
- ___block_descriptor_tmp.2746
- ___block_descriptor_tmp.28.2612
- ___block_descriptor_tmp.28.3948
- ___block_descriptor_tmp.2880
- ___block_descriptor_tmp.29.3796
- ___block_descriptor_tmp.29.402
- ___block_descriptor_tmp.3.3751
- ___block_descriptor_tmp.3.443
- ___block_descriptor_tmp.30.1731
- ___block_descriptor_tmp.30.2587
- ___block_descriptor_tmp.3137
- ___block_descriptor_tmp.33.2588
- ___block_descriptor_tmp.33.3945
- ___block_descriptor_tmp.34.2589
- ___block_descriptor_tmp.34.3653
- ___block_descriptor_tmp.34.3797
- ___block_descriptor_tmp.3420
- ___block_descriptor_tmp.35.2598
- ___block_descriptor_tmp.37.2590
- ___block_descriptor_tmp.37.3942
- ___block_descriptor_tmp.38.3798
- ___block_descriptor_tmp.3963
- ___block_descriptor_tmp.4.1654
- ___block_descriptor_tmp.4.2940
- ___block_descriptor_tmp.4.3749
- ___block_descriptor_tmp.40.2619
- ___block_descriptor_tmp.41.3939
- ___block_descriptor_tmp.42.3799
- ___block_descriptor_tmp.4319
- ___block_descriptor_tmp.448
- ___block_descriptor_tmp.4543
- ___block_descriptor_tmp.46.3800
- ___block_descriptor_tmp.4606
- ___block_descriptor_tmp.4772
- ___block_descriptor_tmp.48.3801
- ___block_descriptor_tmp.5.2177
- ___block_descriptor_tmp.5.2512
- ___block_descriptor_tmp.5.3434
- ___block_descriptor_tmp.5.4001
- ___block_descriptor_tmp.50.3802
- ___block_descriptor_tmp.53.2528
- ___block_descriptor_tmp.60.4697
- ___block_descriptor_tmp.686
- ___block_descriptor_tmp.72.3807
- ___block_descriptor_tmp.74.3803
- ___block_descriptor_tmp.78.4016
- ___block_descriptor_tmp.79.4017
- ___block_descriptor_tmp.8.3300
- ___block_descriptor_tmp.80.4018
- ___block_descriptor_tmp.85.3784
- ___block_descriptor_tmp.86.4039
- ___block_descriptor_tmp.9.2591
- ___block_descriptor_tmp.9.299
- ___block_descriptor_tmp.9.3311
- ___block_descriptor_tmp.9.3509
- ___block_descriptor_tmp.9.3959
- ___block_descriptor_tmp.960
- ___block_literal_global.106
- ___block_literal_global.112
- ___block_literal_global.1188
- ___block_literal_global.121
- ___block_literal_global.127
- ___block_literal_global.156
- ___block_literal_global.1648
- ___block_literal_global.1847
- ___block_literal_global.194
- ___block_literal_global.1949
- ___block_literal_global.218
- ___block_literal_global.2255
- ___block_literal_global.2426
- ___block_literal_global.249
- ___block_literal_global.2574
- ___block_literal_global.3117
- ___block_literal_global.3647
- ___block_literal_global.3748
- ___block_literal_global.441
- ___block_literal_global.4604
- ___block_literal_global.4759
- ___block_literal_global.619
- ___block_literal_global.7.3999
- ___block_literal_global.956
- ___quic_conn_copy_info_block_invoke.147
- ___quic_conn_link_advisory_block_invoke.141
- ___quic_conn_preferred_path_block_invoke.157
- ___quic_conn_send_frames_for_key_state_block_invoke.207
- ___quic_signpost_is_enabled._quic_signposts_enabled.2575
- ___quic_signpost_is_enabled._quic_signposts_enabled.3118
- ___quic_signpost_is_enabled._quic_signposts_enabled.3648
- ___quic_signpost_is_enabled._quic_signposts_enabled.3898
- ___quic_signpost_is_enabled._quic_signposts_enabled.4760
- ___quic_signpost_is_enabled._quic_signposts_enabled.620
- ___quic_signpost_is_enabled._quic_signposts_enabled.957
- ___quic_signpost_is_enabled._quic_signposts_once.2573
- ___quic_signpost_is_enabled._quic_signposts_once.3116
- ___quic_signpost_is_enabled._quic_signposts_once.3646
- ___quic_signpost_is_enabled._quic_signposts_once.3897
- ___quic_signpost_is_enabled._quic_signposts_once.4758
- ___quic_signpost_is_enabled._quic_signposts_once.618
- ___quic_signpost_is_enabled._quic_signposts_once.955
CStrings:
+ "%{public}s %{public}s [%{public}s-%{public}s] beginning validation on path over %{public}s"
+ "%{public}s %{public}s [%{public}s-%{public}s] cannot start validation on path %lx with state %{public}s"
+ "%{public}s %{public}s [%{public}s-%{public}s] connection is now %{public}s"
+ "%{public}s %{public}s [%{public}s-%{public}s] delaying migration until we have more data to send"
+ "%{public}s %{public}s [%{public}s-%{public}s] delaying probes: unreliable? %d, idle? %d, primary? %d, fallback? %d, preferred? %d"
+ "%{public}s %{public}s [%{public}s-%{public}s] path %lx disappeared"
+ "B16@?0^{quic_path=Q^{nw_interface}C[21C][21C]cI[6{?=QQ}]{quic_frame_list=^{quic_frame}^^{quic_frame}}^{quic_rtt}[16c]QQ{?=^{quic_path}^^{quic_path}}QQIIQ^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_pacer}^{quic_pmtud}^{quic_loss_recovery_path_state}^{quic_ecn_path_state}{quic_path_statistics=QQQQIIII}CCSSSCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b6[3c]}8"
+ "active"
+ "quic_conn_check_current_path"
+ "quic_conn_check_current_path_block_invoke"
+ "quic_conn_idle_state"
+ "quic_conn_idle_state_block_invoke"
+ "quic_conn_outbound_starting"
+ "quic_migration_begin_validation"
+ "quic_path_delayed_validation"
+ "quic_recovery_get_ack_eliciting_in_flight"
- "B16@?0^{quic_path=Q^{nw_interface}C[21C][21C]cI[6{?=QQ}]{quic_frame_list=^{quic_frame}^^{quic_frame}}^{quic_rtt}[16c]QQ{?=^{quic_path}^^{quic_path}}QQIIQ^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_cc_algorithm}^{quic_pacer}^{quic_pmtud}^{quic_loss_recovery_path_state}^{quic_ecn_path_state}{quic_path_statistics=QQQQIIII}CCSSSCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b7[3c]}8"

```
