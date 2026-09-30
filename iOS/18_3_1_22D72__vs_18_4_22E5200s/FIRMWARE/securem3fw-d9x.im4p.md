## securem3fw-d9x.im4p

> `securem3fw-d9x.im4p`

```diff

 
-  __TEXT.__text: 0x12818
-  __TEXT.__const: 0x2dc0
-  __TEXT.__cstring: 0x16d9
+  __TEXT.__text: 0x12bc0
+  __TEXT.__const: 0x2df0
+  __TEXT.__cstring: 0x441
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0xc0
   __TEXT.__rtk_vtor: 0x254
   __TEXT.__data_copy: 0x878
   __DATA.__tb_ipc_buf: 0x600
   __DATA.__data: 0x876
-  __DATA._rtk_patchbay: 0xcc
+  __DATA._rtk_patchbay: 0xec
   __DATA._rtk_power: 0x8
   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__m3_coredump: 0x10c
   __DATA.__boot_count: 0x8
-  __DATA.__zerofill: 0xedc4
+  __DATA.__zerofill: 0xee04
   Functions: 0
   Symbols:   0
-  CStrings:  53
+  CStrings:  46
 
CStrings:
+ "03:17:54"
+ "3.504.13"
+ "Feb 16 2025"
- "03:02:19"
- "3.410"
- "Jan 16 2025"
- "v8@?0r^{acicommands_aci_isp_to_m3_msg_s={acicommands_aci_msg_hdr_s=CCCC}{acicommands_aci_isp_to_m3_payload_types__opt=B{acicommands_aci_isp_to_m3_payload_types=Q(?={?={acicommands_aci_config_shim_main_line_count_s=II}}{?={acicommands_aci_config_be_generic_packet_s=CC}}{?={acicommands_aci_disable_aci_shim_s=B}}{?={acicommands_aci_config_aci_be_generic_packet_s=CCC}}{?={acicommands_aci_config_shim_generic_packets_s=CCC}}{?={acicommands_aci_configure_aci_shim_s=BCB[2{acicommands_aci_frame_info_s=CCSSS}]}})}}}4"
- "v8@?0r^{i2ccommands_i2c_isp_to_m3_msg_s={i2ccommands_i2c_msg_hdr_s=CCC}{i2ccommands_i2c_isp_to_m3_payload_types__opt=B{i2ccommands_i2c_isp_to_m3_payload_types=Q(?={?={i2ccommands_i2c_read_s={i2ccommands_i2c_read_header_s=ISBSCCC}}}{?={i2ccommands_i2c_write_s={i2ccommands_i2c_write_header_s=ISBSCCC}{i2ccommands_i2c_write_data_s=[8Q]}}}{?={i2ccommands_i2c_block_request_s={i2ccommands_i2c_block_request_header_s=IISBSCCCC}{i2ccommands_i2c_block_request_data_s=[340C][170C]}}})}}}4"
- "v8@?0r^{isp_securem3_ipc_msg_s={isp_securem3_ipc_msg_hdr_s=CCCC}{isp_securem3_ipc_payload_types__opt=B{isp_securem3_ipc_payload_types=Q(?={?={isp_securem3_ipc_log_16_rec_s=QSSSSSCC}}{?={isp_securem3_ipc_log_32_rec_s=QIISCC}}{?={isp_securem3_ipc_log_64_rec_s=QQSCC}}{?={isp_securem3_ipc_log_float_rec_s=QIISCC}}{?={isp_securem3_ipc_device_init_s=CCCCC}}{?={isp_securem3_ipc_buildinfo_send_s=[25C][25C][12C][9C]}}{?={isp_securem3_ipc_sys_pmu_otp_overwrite_s=CCB}}{?=I}{?={isp_securem3_ipc_sensor_readout_set_s=CSSS}}{?={isp_securem3_ipc_sensor_output_size_set_s=CSS}}{?={isp_securem3_ipc_sensor_settings_set_s=I}}{?={isp_securem3_ipc_sensor_send_configs_tot_s=I}}{?={isp_securem3_ipc_sensor_req_config_s=I}}{?={isp_securem3_ipc_sensor_send_config_s={isp_securem3_ipc_sensor_config_s=ISSCCSIISSIIISISSII}}}{?={isp_securem3_ipc_sensor_agc_set_s=S}}{?={isp_securem3_ipc_sensor_agc_sifr_set_s=S}}{?={isp_securem3_ipc_sensor_dig_gain_set_s=S}}{?={isp_securem3_ipc_sensor_dig_gain_sifr_set_s=S}}{?={isp_securem3_ipc_sensor_shuttervalue_set_s=S}}{?={isp_securem3_ipc_sensor_enablestreaming_set_s=B}})}}}4"
- "v8@?0r^{lpdpcommands_lpdp_isp_to_m3_msg_s={lpdpcommands_lpdp_msg_hdr_s=CCCC}{lpdpcommands_lpdp_isp_to_m3_payload_types__opt=B{lpdpcommands_lpdp_isp_to_m3_payload_types=Q(?={?={lpdpcommands_lpdp_channel_info_s=cccCSCcC[6c]QC[7C]}}{?={lpdpcommands_lpdp_status_poll_s=CCI}}{?={lpdpcommands_lpdp_power_on_off_s=B}}{?={lpdpcommands_lpdp_resolution_info_s=II}}{?={lpdpcommands_lpdp_receiver_tuning_value_s=[2C]}}{?={lpdpcommands_lpdp_set_phy_adapative_eq_s=CCIIIIIII}}{?={lpdpcommands_lpdp_error_check_s=cC[6c]I}}{?={lpdpcommands_lpdp_send_eq_s=CCCCCCCC}}{?={lpdpcommands_lpdp_send_ad_eq_s=CBCCCCCCCC}}{?={lpdpcommands_lpdp_be_rx_info_s=cII}}{?={lpdpcommands_lpdp_dprxc_training_pattern_s=C}}{?={lpdpcommands_lpdp_device_info_s=CCCCC}})}}}4"
- "v8@?0r^{mipicommands_mipi_isp_to_m3_msg_s={mipicommands_mipi_msg_hdr_s=BC}{mipicommands_mipi_isp_to_m3_payload_types__opt=B{mipicommands_mipi_isp_to_m3_payload_types=Q(?={?={mipicommands_mipi_resolution_info_s=II}}{?={mipicommands_mipi_pixel_format_s=C}}{?={mipicommands_mipi_lane_count_s=C}}{?={mipicommands_mipi_phy_info_s=CI}}{?={mipicommands_mipi_error_check_s=I}}{?={mipicommands_mipi_dphy_polarity_ctrl_data_s=C}}{?={mipicommands_mipi_config_aci_shim_s=CBCBCCCCSSSSSS}}{?={mipicommands_mipi_aci_shim_debug_reg_s=II}})}}}4"
- "v8@?0r^{spmicommands_spmi_isp_to_m3_msg_s={spmicommands_spmi_msg_hdr_s=CCC}{spmicommands_spmi_isp_to_m3_payload_types__opt=B{spmicommands_spmi_isp_to_m3_payload_types=Q(?={?={spmicommands_spmi_register_int_entry_s=IBB}}{?={spmicommands_spmi_read_entry_s={spmicommands_spmi_read_entry_header_s=IISCCB}{spmicommands_spmi_read_entry_data_s=[32C]}}}{?={spmicommands_spmi_write_entry_s={spmicommands_spmi_write_entry_header_s=IISCCB}{spmicommands_spmi_write_entry_data_s=[32C][32C]}}}{?={spmicommands_spmi_error_code_s=I}})}}}4"
- "v8@?0r^{vcroutercommands_vcrouter_isp_to_m3_msg_s={vcroutercommands_vcrouter_msg_hdr_s=CC}{vcroutercommands_vcrouter_isp_to_m3_payload_types__opt=B{vcroutercommands_vcrouter_isp_to_m3_payload_types=Q(?={?={vcroutercommands_vcrouter_err_status_s={vcroutercommands_vcrouter_common_s=c}IIII}}{?={vcroutercommands_vcrouter_err_status_s={vcroutercommands_vcrouter_common_s=c}IIII}}{?={vcroutercommands_vcrouter_config_s={vcroutercommands_vcrouter_common_s=c}BCCC}}{?={vcroutercommands_vcrouter_inputstage_config_s={vcroutercommands_vcrouter_common_s=c}CB}}{?={vcroutercommands_vcrouter_config_exclave_s={vcroutercommands_vcrouter_common_s=c}BCC}}{?={vcroutercommands_vcrouter_exclave_get_dst_s={vcroutercommands_vcrouter_common_s=c}I}}{?={vcroutercommands_vcrouter_qchain_info=Cc}}{?={vcroutercommands_vcrouter_latency_factor_info=Sc}}{?={vcroutercommands_vcrouter_latency_factor_info=Sc}})}}}4"

```
