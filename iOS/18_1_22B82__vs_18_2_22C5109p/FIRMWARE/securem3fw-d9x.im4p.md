## securem3fw-d9x.im4p

> `securem3fw-d9x.im4p`

```diff

 
-  __TEXT.__text: 0xecf0
-  __TEXT.__const: 0x3e0c
-  __TEXT.__data_copy: 0x4000
-  __TEXT.__cstring: 0x23a
+  __TEXT.__text: 0x11c08
+  __TEXT.__const: 0x2d70
+  __TEXT.__cstring: 0x17d4
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0xc0
   __TEXT.__rtk_vtor: 0x254
-  __DATA.__data: 0x7e9
-  __DATA.__boot_count: 0x8
-  __DATA._rtk_patchbay: 0x9e
-  __DATA.__m3_coredump: 0x10c
+  __TEXT.__data_copy: 0x870
+  __DATA.__tb_ipc_buf: 0x600
+  __DATA.__data: 0x86e
+  __DATA._rtk_patchbay: 0xcc
   __DATA._rtk_power: 0x8
   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
-  __DATA.__zerofill: 0xead8
+  __DATA.__m3_coredump: 0x10c
+  __DATA.__boot_count: 0x8
+  __DATA.__zerofill: 0xeeb4
   Functions: 0
   Symbols:   0
-  CStrings:  30
+  CStrings:  43
 
CStrings:
+ "12:42:35"
+ "AldaSTI2cController.c"
+ "CACIController.c"
+ "CSPMIBusController.c"
+ "Oct 16 2024"
+ "^{tb_message_s=ICIQQQ[4Q]I^{tb_transport_message_buffer_s}}12@?0^{tb_connection_s=(?=[32C]^v)}4^{tb_message_s=ICIQQQ[4Q]I^{tb_transport_message_buffer_s}}8"
+ "^{tb_message_s=ICIQQQ[4Q]I^{tb_transport_message_buffer_s}}8@?0^{tb_message_s=ICIQQQ[4Q]I^{tb_transport_message_buffer_s}}4"
+ "internal.h"
+ "isp_to_m3_tightbeam.c"
+ "m3_1"
+ "tb_connection.c"
+ "tb_message.c"
+ "tytbmxport"
+ "tytbmxport_client"
+ "tytbmxport_server"
+ "v8@?0r^{isp_securem3_ipc_msg_s={isp_securem3_ipc_msg_hdr_s=CCCC}{isp_securem3_ipc_payload_types__opt=B{isp_securem3_ipc_payload_types=Q(?={?={isp_securem3_ipc_lpdp_channel_mapping_info_entry_s=cccCSC}}{?={isp_securem3_ipc_lpdp_phy_info_entry_s=cC[6c]}}{?={isp_securem3_ipc_lpdp_phy_shutdown_entry_s=BC[6c]}}{?={isp_securem3_ipc_lpdp_max_frequency_entry_s=Q}}{?={isp_securem3_ipc_lpdp_status_poll_s=SSI}}{?={isp_securem3_ipc_lpdp_resolution_info_s=II}}{?={isp_securem3_ipc_lpdp_receiver_tuning_value_s=[2I]}}{?={isp_securem3_ipc_lpdp_sideband_type_list_s=C[7C]}}{?={isp_securem3_ipc_lpdp_power_on_off_s=B}}{?={isp_securem3_ipc_lpdp_set_phy_adapative_eq_s=SSIIIIIII}}{?={isp_securem3_ipc_lpdp_error_check_s=I}}{?={isp_securem3_ipc_lpdp_error_check_s=I}}{?={isp_securem3_ipc_lpdp_send_eq_s=IIIIIIII}}{?={isp_securem3_ipc_lpdp_send_eq_s=IIIIIIII}}{?={isp_securem3_ipc_lpdp_send_ad_eq_s=CCIIIIIIII}}{?={isp_securem3_ipc_lpdp_send_ad_eq_s=CCIIIIIIII}}{?={isp_securem3_ipc_lpdp_be_rx_info_s=III}}{?={isp_securem3_ipc_lpdp_be_rx_info_s=III}}{?={isp_securem3_ipc_lpdp_dprxc_training_pattern_s=C}}{?={isp_securem3_ipc_lpdp_send_dprxc_status_s=IIIIIIIIIIIII}}{?={isp_securem3_ipc_lpdp_device_info_s=CCCCC}}{?={isp_securem3_ipc_lpdp_send_rc_params_s=CC}}{?={isp_securem3_ipc_spmi_device_register_entry_s=CB}}{?={isp_securem3_ipc_spmi_set_clock_pause_s=CC}}{?={isp_securem3_ipc_spmi_register_int_entry_s=ICC}}{?={isp_securem3_ipc_spmi_set_spmi_ip_enable_s=B}}{?={isp_securem3_ipc_spmi_write_entry_s={isp_securem3_ipc_spmi_write_entry_header_s=IISCCC}{isp_securem3_ipc_spmi_write_entry_data_s=[32C][32C]}}}{?={isp_securem3_ipc_spmi_read_entry_s={isp_securem3_ipc_spmi_read_entry_header_s=IISCCC}{isp_securem3_ipc_spmi_read_entry_data_s=[32C]}}}{?={isp_securem3_ipc_spmi_read_done_s=[32C]}}{?={isp_securem3_ipc_spmi_error_code_s=I}}{?={isp_securem3_ipc_spmi_error_code_s=I}}{?={isp_securem3_ipc_i2c_read_fifo_s=C}}{?={isp_securem3_ipc_i2c_read_done_s=[8Q]CC}}{?={isp_securem3_ipc_i2c_write_s={isp_securem3_ipc_i2c_write_header_s=ISBCCCC}{isp_securem3_ipc_i2c_write_data_s=[8Q]}}}{?={isp_securem3_ipc_i2c_read_s={isp_securem3_ipc_i2c_read_header_s=ISBCCCC}}}{?={isp_securem3_ipc_i2c_block_request_s={isp_securem3_ipc_i2c_block_request_header_s=IISBCCCCC}{isp_securem3_ipc_i2c_block_request_data_s=[340C][170C]}}}{?={isp_securem3_ipc_mipi_power_on_off_s=B}}{?={isp_securem3_ipc_mipi_pixel_format_s=C}}{?={isp_securem3_ipc_mipi_resolution_info_s=II}}{?={isp_securem3_ipc_mipi_lane_count_s=C}}{?={isp_securem3_ipc_mipi_phy_info_s=CI}}{?={isp_securem3_ipc_mipi_error_check_s=I}}{?={isp_securem3_ipc_mipi_error_check_s=I}}{?={isp_securem3_ipc_mipi_version_get_s=I}}{?={isp_securem3_ipc_mipi_dphy_polarity_ctrl_data_s=I}}{?={isp_securem3_ipc_mipi_config_aci_shim_s=CCCCCCCCSSSSSS}}{?={isp_securem3_ipc_mipi_aci_shim_debug_reg_s=II}}{?={isp_securem3_ipc_mipi_aci_shim_debug_reg_s=II}}{?={isp_securem3_ipc_vcrouter_inputstage_config_s={isp_securem3_ipc_vcrouter_common_s=C}CC}}{?={isp_securem3_ipc_vcrouter_err_status_s={isp_securem3_ipc_vcrouter_common_s=C}IIII}}{?={isp_securem3_ipc_vcrouter_err_status_s={isp_securem3_ipc_vcrouter_common_s=C}IIII}}{?={isp_securem3_ipc_vcrouter_err_status_s={isp_securem3_ipc_vcrouter_common_s=C}IIII}}{?={isp_securem3_ipc_vcrouter_config_s={isp_securem3_ipc_vcrouter_common_s=C}IIII}}{?={isp_securem3_ipc_vcrouter_config_exclave_s={isp_securem3_ipc_vcrouter_common_s=C}IIII}}{?={isp_securem3_ipc_vcrouter_exclave_get_dst_s={isp_securem3_ipc_vcrouter_common_s=C}I}}{?={isp_securem3_ipc_vcrouter_exclave_get_dst_s={isp_securem3_ipc_vcrouter_common_s=C}I}}{?={isp_securem3_ipc_vcrouter_qchain_info=QQ}}{?={isp_securem3_ipc_vcrouter_latency_factor_info=QQ}}{?={isp_securem3_ipc_vcrouter_latency_factor_info=QQ}}{?={isp_securem3_ipc_vcrouter_latency_factor_info=QQ}}{?={isp_securem3_ipc_aci_config_shim_main_line_count_s=II}}{?={isp_securem3_ipc_aci_config_be_generic_packet_s=CC}}{?={isp_securem3_ipc_aci_disable_aci_shim_s=C}}{?={isp_securem3_ipc_aci_config_aci_be_generic_packet_s=iCC}}{?={isp_securem3_ipc_aci_config_shim_generic_packets_s=CCC}}{?={isp_securem3_ipc_aci_configure_aci_shim_s=CCC[2{isp_securem3_ipc_aci_frame_info_s=CCSSS}]}}{?={isp_securem3_ipc_aci_send_dprxc_status_s=IIIIIIIIIII[4I][4I][4I][4I]IIIC}}{?={isp_securem3_ipc_log_16_rec_s=QSSSSSCC}}{?={isp_securem3_ipc_log_32_rec_s=QIISCC}}{?={isp_securem3_ipc_log_64_rec_s=QQSCC}}{?={isp_securem3_ipc_log_float_rec_s=QIISCC}}{?={isp_securem3_ipc_device_init_s=CCCCC}}{?={isp_securem3_ipc_buildinfo_send_s=[25C][25C][12C][9C]}}{?=I}{?={isp_securem3_ipc_sensor_readout_set_s=CSSS}}{?={isp_securem3_ipc_sensor_output_size_set_s=CSS}}{?={isp_securem3_ipc_sensor_context_switch_s=III}}{?={isp_securem3_ipc_sensor_context_switch_info_s=II}}{?={isp_securem3_ipc_sensor_settings_set_s=I}}{?={isp_securem3_ipc_sensor_send_configs_tot_s=I}}{?={isp_securem3_ipc_sensor_req_config_s=I}}{?={isp_securem3_ipc_sensor_send_config_s={isp_securem3_ipc_sensor_config_s=ISSCCSIISSIIISISSII}}}{?={isp_securem3_ipc_sensor_agc_set_s=S}}{?={isp_securem3_ipc_sensor_dig_gain_set_s=S}}{?={isp_securem3_ipc_sensor_shutter_value_set_s=S}})}}}4"
- "22:50:56"
- "Sep 28 2024"
- "platformThread"

```
