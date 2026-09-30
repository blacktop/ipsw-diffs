## tcpdump

> `/usr/sbin/tcpdump`

```diff

-  __TEXT.__text: 0x98724
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__const: 0xc39
-  __TEXT.__cstring: 0x383b1
+  __TEXT.__text: 0x97758
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__const: 0xc75
+  __TEXT.__cstring: 0x383d1
   __TEXT.__oslogstring: 0xb0
-  __TEXT.__unwind_info: 0xb30
+  __TEXT.__unwind_info: 0xb40
   __DATA_CONST.__const: 0x22910
-  __DATA_CONST.__auth_got: 0x668
+  __DATA_CONST.__auth_got: 0x670
   __DATA_CONST.__got: 0x40
   __DATA.__data: 0x3890
   __DATA.__bss: 0x161b29

   - /usr/lib/libpcap.A.dylib
   - /usr/lib/libssl.48.dylib
   Functions: 909
-  Symbols:   2284
-  CStrings:  12394
+  Symbols:   2287
+  CStrings:  12395
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
Symbols:
+ __exit
+ cleanup.cleanup_call_count
+ cleanup.msg
Functions:
~ _etheraddr_string : 440 -> 432
~ _le64addr_string : 256 -> 248
~ _linkaddr_string : 396 -> 384
~ _isonsap_string : 620 -> 612
~ _addrtostr : 204 -> 196
~ _Parse_fh : 1864 -> 1856
~ _get_token : 680 -> 672
~ _parse_not_expression : 572 -> 556
~ _ieee802_11_radio_print : 3216 -> 3200
~ _ieee802_15_4_print : 3788 -> 3780
~ _ieee802_15_4_print_header_ie_list : 2952 -> 2844
~ _ieee802_15_4_print_payload_ie_list : 4856 -> 4644
~ _ieee802_15_4_print_gts_info : 456 -> 444
~ _ieee802_15_4_print_pending_addresses : 488 -> 480
~ _ieee802_15_4_print_command_data : 1224 -> 1220
~ _ah_print : 472 -> 464
~ _ahcp_ipv6_addresses_print : 228 -> 220
~ _ahcp_ipv4_addresses_print : 228 -> 220
~ _ahcp_ipv6_prefixes_print : 256 -> 248
~ _ahcp_ipv4_prefixes_print : 256 -> 248
~ _aodv_print : 3300 -> 3276
~ _aoev1_mac_print : 516 -> 504
~ _aoev1_reserve_print : 384 -> 364
~ _isnonzero : 84 -> 76
~ _ascii_print : 340 -> 308
~ _hex_and_ascii_print : 628 -> 616
~ _hex_print_with_offset : 376 -> 368
~ _print_cstring : 220 -> 204
~ _ssh_print : 360 -> 368
~ _oam_print : 1092 -> 1056
~ _babel_print_v2_tlvs : 4500 -> 4536
~ _subtlvs_print : 972 -> 1032
~ _auth_print : 756 -> 748
~ _bgp_print : 5748 -> 5548
~ _bgp_attr_print : 5472 -> 5392
~ _rfc1048_print : 3620 -> 3560
~ _cdp_print_addr : 936 -> 908
~ _cdp_print_version : 180 -> 176
~ _cdp_print_prefixes : 308 -> 292
~ _cnfp_print : 4104 -> 3836
~ _dccp_print : 3628 -> 3572
~ _decnet_print : 2672 -> 2624
~ _dhcp6opt_print : 4168 -> 3896
~ _fqdn_print : 1004 -> 996
~ _ns_rprint : 3516 -> 3436
~ _dvmrp_print : 2244 -> 2204
~ _eap_print : 1120 -> 1116
~ _forces_print : 1924 -> 1932
~ _pdata_print : 1856 -> 1764
~ _q933_print : 1296 -> 1276
~ _geneve_opts_print : 552 -> 548
~ _gre_print : 2568 -> 2584
~ _hncp_print_rec : 3716 -> 3700
~ _icmp_print : 3892 -> 3872
~ _icmp6_print : 8128 -> 8000
~ _mldv2_query_print : 704 -> 688
~ _icmp6_opt_print : 1764 -> 1748
~ _print_lladdr : 220 -> 188
~ _dnsname_print : 404 -> 392
~ _igmp_print : 1620 -> 1596
~ _print_igmpv3_query : 700 -> 680
~ _igrp_print : 780 -> 768
~ _ip_optprint : 1464 -> 1436
~ _nextproto6_cksum : 556 -> 544
~ _ipx_print : 1600 -> 1584
~ _isakmp_print : 2328 -> 2324
~ _ikev1_id_print : 1752 -> 1748
~ _ikev2_ID_print : 892 -> 880
~ _ikev2_vid_print : 616 -> 604
~ _isoclns_print : 14160 -> 14036
~ _isis_print_id : 360 -> 356
~ _isis_print_ext_is_reach : 2736 -> 2748
~ _isis_print_tlv_ip_reach : 912 -> 784
~ _isis_print_extd_ip_reach : 1488 -> 1468
~ _isis_print_mt_port_cap_subtlv : 860 -> 844
~ _isis_print_mt_capability_subtlv : 1408 -> 1392
~ _juniper_parse_header : 2304 -> 2296
~ _c_print : 124 -> 116
~ _l2tp_print : 2296 -> 2280
~ _print_string : 108 -> 100
~ _ldp_print : 4328 -> 4312
~ _lldp_print : 9140 -> 9124
~ _lwres_printaddr : 368 -> 360
~ _lwres_printbinlen : 172 -> 164
~ _mpcp_print : 1280 -> 1272
~ _remove_addr_print : 188 -> 184
~ _parsefh : 580 -> 564
~ _nsh_print : 1548 -> 1564
~ _olsr_print : 3424 -> 3400
~ _olsr_print_neighbor : 192 -> 176
~ _olsr_print_lq_neighbor6 : 264 -> 256
~ _olsr_print_lq_neighbor4 : 264 -> 256
~ _of10_table_stats_reply_print : 640 -> 608
~ _of10_port_stats_reply_print : 1000 -> 936
~ _of10_queue_stats_reply_print : 472 -> 448
~ _ospf_te_lsa_print : 2320 -> 2268
~ _ospf_print : 5656 -> 5552
~ _ospf6_print : 4712 -> 4528
~ _pimv1_print : 2816 -> 2780
~ _cisco_autorp_print : 1004 -> 968
~ _handle_ppp : 4032 -> 3988
~ _pppoe_print : 1052 -> 1036
~ _print_attr_string : 636 -> 628
~ _print_vendor_attr : 464 -> 456
~ _resp_parse : 1080 -> 1016
~ _resp_print_string_error_integer : 252 -> 236
~ _resp_get_length : 344 -> 408
~ _rip_print : 1924 -> 1916
~ _rsvp_obj_print : 11640 -> 11588
~ _rt6_print : 848 -> 832
~ _brcm_tag_print : 480 -> 476
~ _rx_print : 3008 -> 2936
~ _fs_print : 5080 -> 5044
~ _cb_print : 1200 -> 1152
~ _prot_print : 1924 -> 1908
~ _vldb_print : 1192 -> 1176
~ _vol_print : 3436 -> 3416
~ _cb_reply_print : 560 -> 540
~ _prot_reply_print : 1116 -> 1092
~ _vldb_reply_print : 3076 -> 2992
~ _vol_reply_print : 2780 -> 2776
~ _sctp_print : 2696 -> 2592
~ _sll_if_print : 724 -> 712
~ _sll2_if_print : 908 -> 896
~ _quic_print : 1648 -> 1624
~ _asn1_parse : 1288 -> 1264
~ _asn1_print : 1140 -> 1128
~ _asn1_print_octets : 180 -> 164
~ _asn1_print_string : 332 -> 308
~ _stp_print_mstp_bpdu : 1360 -> 1352
~ _syslog_print : 592 -> 568
~ _tcp_print : 7548 -> 7536
~ _print_tcp_fastopen_option : 316 -> 312
~ _print_tcp_rst_data : 240 -> 232
~ _telnet_parse : 1212 -> 1208
~ _token_print : 1052 -> 1036
~ _vrrp_print : 1008 -> 992
~ _wb_print : 2164 -> 2140
~ _parse_field : 124 -> 104
~ _print_pktap_header : 4820 -> 4832
~ sub_10008dd28 -> sub_10008cd5c : 168 -> 172
~ _print_asc : 120 -> 108
~ _smb_fdata : 660 -> 652
~ _smb_fdata1 : 3068 -> 3080
~ _smb_errstr : 268 -> 276
~ _unistr : 500 -> 464
~ _strtoaddr : 368 -> 364
~ _copy_argv : 184 -> 188
~ _cleanup : 92 -> 144
~ _print_pcap_ng_block : 8348 -> 8360
~ sub_100096e84 -> sub_100095ed8 : 168 -> 172
~ _nd_printztn : 156 -> 148
~ _nd_printn : 144 -> 128
~ _nd_printjnp : 112 -> 104
~ _uint2tokary_internal : 88 -> 96
~ _fetch_token : 252 -> 248
~ _print_txt_line : 356 -> 348
CStrings:
+ "DROP_REASON_IP6_NDP_SELF_LLADDR"

```
