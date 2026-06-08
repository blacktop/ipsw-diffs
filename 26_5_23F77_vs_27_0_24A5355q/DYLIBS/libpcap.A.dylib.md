## libpcap.A.dylib

> `/usr/lib/libpcap.A.dylib`

```diff

-146.0.0.0.0
-  __TEXT.__text: 0x20b4c
-  __TEXT.__auth_stubs: 0x4f0
+148.0.0.0.0
+  __TEXT.__text: 0x20c84
   __TEXT.__const: 0xc330
-  __TEXT.__cstring: 0x6b9d
-  __TEXT.__unwind_info: 0x520
-  __DATA_CONST.__got: 0x20
+  __TEXT.__cstring: 0x6c2e
+  __TEXT.__unwind_info: 0x590
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x14c0
-  __AUTH_CONST.__auth_got: 0x278
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x10
+  __AUTH_CONST.__auth_got: 0x278
   __DATA.__data: 0xd7
   __DATA.__bss: 0x503
   __DATA.__common: 0x8
   __DATA_DIRTY.__bss: 0x545
   - /usr/lib/libSystem.B.dylib
-  UUID: 29315DCA-66E4-3A5B-9F39-64932DD03F2A
-  Functions: 522
-  Symbols:   935
-  CStrings:  1074
+  UUID: B56D7262-16AA-3C71-9EE7-83B3144E192C
+  Functions: 524
+  Symbols:   939
+  CStrings:  1079
 
Symbols:
+ _get_pktap_param
+ _memchr
+ _pcap_free_dumper
- ___memmove_chk
Functions:
~ _pcap_filter_with_aux_data : 1104 -> 1140
~ _pcap_next_etherent : 700 -> 704
~ _pcap_findalldevs_interfaces : 368 -> 372
~ _pcap_compile : 1856 -> 1860
~ _finish_parse : 3528 -> 3536
~ _gen_protochain : 1820 -> 1840
~ _gen_mcode6 : 492 -> 496
~ _gen_bcmp : 464 -> 468
~ _pcap_nametoaddr : 68 -> 72
~ _bpf_optimize : 1512 -> 1532
~ _opt_loop : 4896 -> 4932
~ _convert_code_r : 852 -> 864
~ _propedom : 112 -> 116
~ _opt_j : 396 -> 416
~ _pcap_activate_bpf : 2484 -> 2480
~ _remove_non_802_11 : 80 -> 84
~ _remove_802_11 : 120 -> 124
~ _pcap_read_bpf : 1088 -> 1180
~ _pcap_setup_pktap_interface : 1916 -> 1884
+ _get_pktap_param
~ _pcap_ng_dump_pktap_comment : 1280 -> 1332
~ _pcap_ng_dump_pktap_v2 : 1200 -> 1412
~ _pcap_sendpacket_multiple : 892 -> 844
~ _pcap_get_divert_input : 116 -> 108
~ _pcap_if_info_set_clear : 108 -> 112
~ _pcap_proc_info_set_clear : 108 -> 112
~ _pcap_proc_info_set_find_uuid : 308 -> 316
~ _pcap_set_datalink : 300 -> 304
~ _pcap_strcasecmp : 48 -> 56
~ _pcap_datalink_name_to_val : 104 -> 112
~ _pcap_tstamp_type_name_to_val : 108 -> 116
~ _pcap_ng_block_reset : 344 -> 348
~ _pcap_ng_block_packet_copy_data : 404 -> 412
~ _pcap_ng_block_add_option_with_value : 328 -> 336
~ _pcap_ng_block_get_option : 300 -> 304
~ _pcapng_block_iterate_options : 340 -> 344
~ _pcapng_block_iterate_name_records : 252 -> 256
~ _pcap_ng_block_add_name_record_with_ip4 : 36 -> 40
~ _pcap_ng_block_add_name_record_common : 460 -> 464
~ _pcap_ng_block_add_name_record_with_ip6 : 36 -> 40
~ _pcap_ng_externalize_block : 560 -> 568
~ _pcap_ng_dump_block : 464 -> 472
~ _pcap_fopen_offline_internal : 636 -> 640
+ _pcap_free_dumper
~ _pcap_dump_close : 100 -> 96
~ _pcap_ng_dump_open : 368 -> 344
~ _pcap_ng_setup_dump : 128 -> 132
~ _pcap_ng_next_internal : 1484 -> 1488
~ _pcap_parse : 5732 -> 5184
~ _pcap_lex : 3704 -> 3716
~ _stou : 348 -> 360
~ _yy_get_previous_state : 196 -> 204
~ _pcap__scan_bytes : 132 -> 136
CStrings:
+ "%s: Droptap header too short"
+ "%s: ifname not terminated"
+ "device name too long"
+ "no interface name"
+ "pcap_sendpacket_multiple: j %u >= send_iovec_count %u"
+ "pcap_sendpacket_multiple: writev %d failed:"
- "pcap_sendpacket_multiple: writev %d failed: %s"

```
