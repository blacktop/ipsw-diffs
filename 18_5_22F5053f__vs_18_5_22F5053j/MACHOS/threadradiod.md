## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

-275.0.503.0.0
-  __TEXT.__text: 0x3cb948
+275.0.504.0.0
+  __TEXT.__text: 0x3cd07c
   __TEXT.__auth_stubs: 0x11470
   __TEXT.__objc_stubs: 0x9680
   __TEXT.__init_offsets: 0xa4
-  __TEXT.__objc_methlist: 0x64f0
+  __TEXT.__objc_methlist: 0x6500
   __TEXT.__objc_classname: 0x5f4
   __TEXT.__const: 0x81d0
-  __TEXT.__gcc_except_tab: 0x2a778
-  __TEXT.__objc_methname: 0xe952
-  __TEXT.__cstring: 0x2f3a7
-  __TEXT.__oslogstring: 0x2298b
-  __TEXT.__objc_methtype: 0x4450
-  __TEXT.__unwind_info: 0x7288
+  __TEXT.__gcc_except_tab: 0x2a934
+  __TEXT.__objc_methname: 0xe96a
+  __TEXT.__cstring: 0x2f3f7
+  __TEXT.__oslogstring: 0x22a13
+  __TEXT.__objc_methtype: 0x46b4
+  __TEXT.__unwind_info: 0x72f8
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x8a50
   __DATA_CONST.__got: 0x918
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xada8
+  __DATA_CONST.__const: 0xae10
   __DATA_CONST.__cfstring: 0x5ee0
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA.__objc_const: 0x84e8
-  __DATA.__objc_selrefs: 0x35b0
+  __DATA.__objc_selrefs: 0x35b8
   __DATA.__objc_ivar: 0x534
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x5b8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15784
-  Symbols:   82247
-  CStrings:  12115
+  Functions: 15798
+  Symbols:   82333
+  CStrings:  12123
 
Symbols:
+ -[CtrInternalClient trm_get_ot_data:output:]
+ GCC_except_table177
+ GCC_except_table214
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table230
+ GCC_except_table235
+ GCC_except_table294
+ GCC_except_table305
+ GCC_except_table310
+ GCC_except_table342
+ GCC_except_table435
+ GCC_except_table458
+ GCC_except_table459
+ GCC_except_table469
+ GCC_except_table481
+ GCC_except_table490
+ GCC_except_table496
+ GCC_except_table497
+ GCC_except_table506
+ GCC_except_table507
+ GCC_except_table514
+ GCC_except_table526
+ GCC_except_table527
+ GCC_except_table537
+ GCC_except_table538
+ GCC_except_table546
+ GCC_except_table547
+ GCC_except_table559
+ GCC_except_table560
+ GCC_except_table567
+ GCC_except_table568
+ GCC_except_table580
+ GCC_except_table581
+ GCC_except_table587
+ GCC_except_table588
+ _ZN14InternalIPCAPI23interface_send_ping_reqENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEtbS6_S6_N8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE.cold.1
+ _ZN14InternalIPCAPI25interface_trm_get_ot_dataENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES6_S6_N8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE.cold.1
+ _ZN14InternalIPCAPI30received_ping_stats_trm_updateERKN5boost3anyE.cold.1
+ _ZN14InternalIPCAPI30received_ping_stats_trm_updateERKN5boost3anyE.cold.2
+ __ZN14InternalClient15trm_get_ot_dataE21Ctr_trm_get_ot_data_tPN5boost3anyE
+ __ZN14InternalIPCAPI23interface_send_ping_reqENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEtbS6_S6_N8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE
+ __ZN14InternalIPCAPI25interface_trm_get_ot_dataENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES6_S6_N8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE
+ __ZN14InternalIPCAPI30received_ping_stats_trm_updateERKN5boost3anyE
+ __ZN14RcpHostContext20add_cmd_TrmGetOTDataE15HostTaskCommandP20_TRM_GET_OT_CMD_DATA
+ __ZN14RcpHostContext33getIsPrimaryResidentThreadCapableEv
+ __ZN21Ctr_trm_get_ot_data_tD1Ev
+ __ZN2ot15AddressResolver15GetMeshLocalEidERNS_3Ip67AddressES3_Rb
+ __ZN2ot15AddressResolver15GetMeshLocalIidERNS_3Ip67AddressERb
+ ___ZN14InternalClient12generatePSKcE16Ctr_generatePSKcPN5boost3anyE_block_invoke.142
+ ___ZN14InternalClient12getNCPStatusEPN5boost3anyE_block_invoke.150
+ ___ZN14InternalClient15trm_get_ot_dataE21Ctr_trm_get_ot_data_tPN5boost3anyE_block_invoke.29
+ ___ZN14InternalClient18send_ping_node_reqE20Ctr_send_ping_node_t_block_invoke.35
+ ___ZN14InternalClient20updateHomeThreadInfoE18Ctr_homeThreadInfo_block_invoke.78
+ ___ZN14InternalClient21updatePrimaryResidentE23Ctr_primaryResidentInfo_block_invoke.73
+ ___ZN14InternalClient24get_device_data_diag_reqE19Ctr_get_diag_data_t_block_invoke.41
+ ___ZN14InternalClient4formE8Ctr_form_block_invoke.61
+ ___ZN14InternalClient4joinE8Ctr_join_block_invoke.121
+ ___ZN14InternalClient4scanE8Ctr_scan_block_invoke.106
+ ___ZN14InternalClient4scanE8Ctr_scan_block_invoke.111
+ ___ZN14InternalClient4scanE8Ctr_scan_block_invoke.98
+ ___ZN14InternalClient5leaveEb_block_invoke.68
+ ___ZN14InternalClient5resetEb_block_invoke.132
+ ___ZN14InternalClient7wedStopEv_block_invoke.90
+ ___ZN14InternalClient8wedStartE13Ctr_wed_start_block_invoke.85
+ ___ZN14InternalIPCAPI16property_changedENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN5boost3anyE_block_invoke.28
+ ___ZN14InternalIPCAPI16property_changedENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN5boost3anyE_block_invoke.28.cold.1
+ ___ZN14InternalIPCAPI16property_changedENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN5boost3anyE_block_invoke.28.cold.2
+ ___ZN14InternalIPCAPI17IntBroadcastEventENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN5boost3anyEN8dispatch8callbackIU13block_pointerFvvEEE_block_invoke.31
+ ____ZN14InternalClient15trm_get_ot_dataE21Ctr_trm_get_ot_data_tPN5boost3anyE_block_invoke
+ ___copy_helper_block_e8_40c27_ZTS21Ctr_trm_get_ot_data_t96c58_ZTSN8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE
+ ___destroy_helper_block_e8_40c27_ZTS21Ctr_trm_get_ot_data_t96c58_ZTSN8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE
+ __block_descriptor_tmp.101
+ __block_descriptor_tmp.109
+ __block_descriptor_tmp.118
+ __block_descriptor_tmp.124
+ __block_descriptor_tmp.134
+ __block_descriptor_tmp.135
+ __block_descriptor_tmp.138
+ __block_descriptor_tmp.143
+ __block_descriptor_tmp.145
+ __block_descriptor_tmp.148
+ __block_descriptor_tmp.152
+ __block_descriptor_tmp.159
+ __block_descriptor_tmp.40
+ __block_descriptor_tmp.43
+ __block_descriptor_tmp.64
+ __block_descriptor_tmp.67
+ __block_descriptor_tmp.69
+ __block_descriptor_tmp.72
+ __block_descriptor_tmp.74
+ __block_descriptor_tmp.81
+ __block_descriptor_tmp.84
+ __block_descriptor_tmp.86
+ __block_descriptor_tmp.93
+ __block_descriptor_tmp.96
+ _otThreadGetMeshLocalEIdFromAddressCache
+ _otThreadLookUpRloc16
- GCC_except_table171
- GCC_except_table181
- GCC_except_table188
- GCC_except_table224
- GCC_except_table233
- GCC_except_table271
- GCC_except_table312
- GCC_except_table333
- GCC_except_table377
- GCC_except_table407
- GCC_except_table436
- GCC_except_table437
- GCC_except_table451
- GCC_except_table461
- GCC_except_table462
- GCC_except_table473
- GCC_except_table498
- GCC_except_table499
- GCC_except_table508
- GCC_except_table509
- GCC_except_table516
- GCC_except_table519
- GCC_except_table528
- GCC_except_table529
- GCC_except_table539
- GCC_except_table540
- GCC_except_table551
- GCC_except_table552
- GCC_except_table561
- GCC_except_table562
- GCC_except_table572
- GCC_except_table573
- GCC_except_table582
- GCC_except_table583
- _ZN14InternalIPCAPI23interface_send_ping_reqENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEtS6_S6_N8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE.cold.1
- __ZN14InternalIPCAPI23interface_send_ping_reqENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEtS6_S6_N8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE
- __ZN2ot15AddressResolver15GetMeshLocalIidERNS_3Ip67AddressE
- ___ZN14InternalClient12generatePSKcE16Ctr_generatePSKcPN5boost3anyE_block_invoke.136
- ___ZN14InternalClient12getNCPStatusEPN5boost3anyE_block_invoke.144
- ___ZN14InternalClient18send_ping_node_reqE20Ctr_send_ping_node_t_block_invoke.31
- ___ZN14InternalClient20updateHomeThreadInfoE18Ctr_homeThreadInfo_block_invoke.74
- ___ZN14InternalClient21updatePrimaryResidentE23Ctr_primaryResidentInfo_block_invoke.69
- ___ZN14InternalClient24get_device_data_diag_reqE19Ctr_get_diag_data_t_block_invoke.37
- ___ZN14InternalClient4formE8Ctr_form_block_invoke.57
- ___ZN14InternalClient4joinE8Ctr_join_block_invoke.117
- ___ZN14InternalClient4scanE8Ctr_scan_block_invoke.102
- ___ZN14InternalClient4scanE8Ctr_scan_block_invoke.107
- ___ZN14InternalClient4scanE8Ctr_scan_block_invoke.94
- ___ZN14InternalClient5leaveEb_block_invoke.64
- ___ZN14InternalClient5resetEb_block_invoke.124
- ___ZN14InternalClient7wedStopEv_block_invoke.86
- ___ZN14InternalClient8wedStartE13Ctr_wed_start_block_invoke.81
- ___ZN14InternalIPCAPI16property_changedENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN5boost3anyE_block_invoke.27
- ___ZN14InternalIPCAPI16property_changedENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN5boost3anyE_block_invoke.27.cold.1
- ___ZN14InternalIPCAPI16property_changedENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN5boost3anyE_block_invoke.27.cold.2
- ___ZN14InternalIPCAPI17IntBroadcastEventENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN5boost3anyEN8dispatch8callbackIU13block_pointerFvvEEE_block_invoke.30
- __block_descriptor_tmp.105
- __block_descriptor_tmp.110
- __block_descriptor_tmp.120
- __block_descriptor_tmp.123
- __block_descriptor_tmp.130
- __block_descriptor_tmp.132
- __block_descriptor_tmp.133
- __block_descriptor_tmp.139
- __block_descriptor_tmp.141
- __block_descriptor_tmp.146
- __block_descriptor_tmp.151
- __block_descriptor_tmp.60
- __block_descriptor_tmp.63
- __block_descriptor_tmp.65
- __block_descriptor_tmp.68
- __block_descriptor_tmp.70
- __block_descriptor_tmp.73
- __block_descriptor_tmp.80
- __block_descriptor_tmp.82
- __block_descriptor_tmp.85
- __block_descriptor_tmp.92
- __block_descriptor_tmp.97
CStrings:
+ " Morty_Version: V0.275.0.504"
+ "InternalIPCAPI::interface_address_cache_lookup: Handling \"%s\" method handler for \"%s\""
+ "Sending ping_stats_trm_update to internal-clients"
+ "TrmGetOTData"
+ "com.apple.wpantund.trm"
+ "trm:ping:stats"
+ "trm_get_ot_data:output:"
+ "trm_get_ot_data_block_invoke"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}48@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}SB}16"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}80@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}S{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}16^{any=^{placeholder}}72"
- " Morty_Version: V0.275.0.503"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}48@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}S}16"

```
