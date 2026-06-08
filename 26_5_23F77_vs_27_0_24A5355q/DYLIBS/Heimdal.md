## Heimdal

> `/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal`

```diff

-710.100.4.0.0
-  __TEXT.__text: 0x621f0
-  __TEXT.__auth_stubs: 0x1980
+720.0.0.0.0
+  __TEXT.__text: 0x6257c
   __TEXT.__const: 0x10a0
   __TEXT.__cstring: 0xf298
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x1600
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x172
-  __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__unwind_info: 0x15f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x7488
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
-  __AUTH_CONST.__auth_got: 0xcd0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1e70
   __AUTH_CONST.__cfstring: 0xc20
+  __AUTH_CONST.__auth_got: 0xcd0
   __DATA.__data: 0x2c50
   __DATA.__bss: 0x6f1
   __DATA.__common: 0x18

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: E1EFEDFA-C915-3FB6-A920-37F042CD2A12
+  UUID: 621B8BE9-11E0-32AA-85B0-6357A6973560
   Functions: 2510
-  Symbols:   1785
-  CStrings:  2362
+  Symbols:   1884
+  CStrings:  2343
 
Functions:
~ _krb5_print_address : 332 -> 336
~ _krb5_parse_address : 560 -> 568
~ _krb5_append_addresses : 272 -> 264
~ sub_25a1275f0 -> sub_2641705a4 : 288 -> 292
~ sub_25a1277f0 -> sub_2641707a8 : 328 -> 340
~ _krb5_aname_to_localname : 356 -> 360
~ _krb5_cc_register : 312 -> 316
~ _krb5_config_parse_file_multi : 1092 -> 1096
~ sub_25a12c3ac -> sub_26417537c : 392 -> 400
~ sub_25a12c534 -> sub_26417550c : 220 -> 268
~ sub_25a12cb1c -> sub_264175b24 : 204 -> 208
~ sub_25a12cbe8 -> sub_264175bf4 : 848 -> 884
~ _krb5_kerberos_enctypes : 100 -> 104
~ sub_25a12e6c4 -> sub_2641776f8 : 324 -> 332
~ _krb5_copy_host_realm : 204 -> 216
~ __krb5_crc_init_table : 92 -> 96
~ _krb5_encrypt_iov_ivec : 1152 -> 1156
~ _krb5_decrypt_iov_ivec : 864 -> 884
~ _krb5_create_checksum_iov : 460 -> 464
~ _krb5_verify_checksum_iov : 388 -> 392
~ _krb5_encrypt_ivec : 992 -> 1000
~ _krb5_decrypt_ivec : 1136 -> 1140
~ sub_25a131800 -> sub_26417a878 : 508 -> 520
~ _krb5_crypto_destroy : 160 -> 164
~ sub_25a132410 -> sub_26417b498 : 324 -> 328
~ sub_25a1325fc -> sub_26417b688 : 288 -> 292
~ _krb5_get_all_any_addrs : 364 -> 368
~ sub_25a1370a8 -> sub_26418013c : 808 -> 824
~ sub_25a1397b0 -> sub_264182854 : 232 -> 240
~ _krb5_get_forwarded_creds : 2720 -> 2724
~ sub_25a13a8b8 -> sub_264183968 : 520 -> 524
~ _krb5_get_host_realm : 548 -> 564
~ _krb5_process_last_request : 336 -> 344
~ sub_25a13cb48 -> sub_264185c14 : 432 -> 436
~ sub_25a13ccf8 -> sub_264185dc8 : 436 -> 444
~ sub_25a1400e0 -> sub_2641891b8 : 240 -> 232
~ sub_25a14102c -> sub_26418a0fc : 1216 -> 1220
~ sub_25a141df8 -> sub_26418aecc : 232 -> 236
~ _krb5_kt_register : 240 -> 244
~ _krb5_kt_resolve : 404 -> 408
~ __krb5_state_srv_sort : 388 -> 392
~ sub_25a144ff0 -> sub_26418e0d4 : 248 -> 252
~ sub_25a1454a0 -> sub_26418e588 : 2208 -> 2232
~ sub_25a1473bc -> sub_2641904bc : 128 -> 132
~ sub_25a147aa0 -> sub_264190ba4 : 1328 -> 1332
~ sub_25a1498b0 -> sub_2641929b8 : 156 -> 112
~ __krb5_s4u2self_to_checksumdata : 320 -> 324
~ _krb5_uuid_to_string : 156 -> 164
~ _krb5_string_to_uuid : 156 -> 160
~ _krb5_mk_priv : 712 -> 720
~ _krb5_mk_rep : 676 -> 680
~ sub_25a14bec8 -> sub_264194fc0 : 624 -> 640
~ _krb5_net_write_block : 360 -> 356
~ _krb5_pac_parse : 940 -> 944
~ _krb5_pac_add_buffer : 460 -> 472
~ _krb5_pac_get_types : 196 -> 204
~ __krb5_pac_sign : 1848 -> 1840
~ __krb5_pk_find_cert : 364 -> 372
~ __krb5_parse_moduli : 620 -> 624
~ __krb5_plugin_find : 1100 -> 1104
~ _krb5_load_plugins : 956 -> 960
~ sub_25a152d08 -> sub_26419be30 : 412 -> 416
~ _krb5_principal_match : 160 -> 168
~ _krb5_sname_to_principal : 456 -> 464
~ _krb5_rd_cred : 1540 -> 1548
~ _krb5_decrypt_ticket : 636 -> 640
~ _krb5_verify_ap_req2 : 1268 -> 1276
~ sub_25a156914 -> sub_26419fa64 : 316 -> 320
~ sub_25a157d28 -> sub_2641a0e7c : 328 -> 332
~ sub_25a15a38c -> sub_2641a34e4 : 544 -> 552
~ _krb5_set_default_realm : 312 -> 316
~ _krb5_ret_stringz : 224 -> 228
~ _krb5_store_principal : 164 -> 168
~ _krb5_ret_principal : 432 -> 436
~ _krb5_format_time : 168 -> 172
~ _krb5_domain_x500_decode : 1436 -> 1440
~ _krb5_domain_x500_encode : 308 -> 320
~ sub_25a160ee8 -> sub_2641aa06c : 728 -> 732
~ sub_25a161504 -> sub_2641aa68c : 396 -> 400
~ sub_25a162244 -> sub_2641ab3d0 : 232 -> 248
~ _krb5_get_pw_salt : 248 -> 260
~ __krb5_put_int : 40 -> 44
~ _base64_encode : 308 -> 320
~ sub_25a164f08 -> sub_2641ae0c0 : 164 -> 168
~ sub_25a1650b0 -> sub_2641ae26c : 132 -> 136
~ sub_25a165258 -> sub_2641ae418 : 636 -> 640
~ sub_25a1656e4 -> sub_2641ae8a8 : 372 -> 376
~ _rk_strpoolprintf : 228 -> 232
~ sub_25a165c68 -> sub_2641aee34 : 688 -> 684
~ sub_25a165f18 -> sub_2641af0e0 : 1520 -> 1524
~ sub_25a166508 -> sub_2641af6d4 : 648 -> 664
~ _rtbl_destroy : 200 -> 204
~ _rtbl_new_row : 316 -> 332
~ _rtbl_format_str : 1084 -> 1092
~ _wind_utf8ucs4 : 160 -> 164
~ sub_25a168030 -> sub_2641b122c : 224 -> 260
~ _wind_utf8ucs2 : 184 -> 188
~ _wind_ucs2utf8 : 180 -> 176
~ sub_25a16bb84 -> sub_2641b4da4 : 208 -> 220
~ sub_25a16cfd4 -> sub_2641b6200 : 3488 -> 3500
~ _hx509_cert_get_attribute : 120 -> 128
~ _hx509_cert_get_friendly_name : 304 -> 312
~ sub_25a16e8ac -> sub_2641b7af4 : 848 -> 852
~ sub_25a16f2b8 -> sub_2641b8504 : 412 -> 416
~ sub_25a16f454 -> sub_2641b86a4 : 588 -> 592
~ sub_25a171c5c -> sub_2641baeb0 : 132 -> 136
~ sub_25a171d20 -> sub_2641baf78 : 96 -> 100
~ sub_25a171d80 -> sub_2641bafdc : 204 -> 208
~ sub_25a171e4c -> sub_2641bb0ac : 192 -> 196
~ sub_25a171f0c -> sub_2641bb170 : 332 -> 336
~ sub_25a172058 -> sub_2641bb2c0 : 300 -> 304
~ _hx509_crypto_select : 568 -> 548
~ sub_25a173714 -> sub_2641bc96c : 180 -> 188
~ sub_25a1737c8 -> sub_2641bca28 : 104 -> 108
~ _hx509_crypto_available : 568 -> 584
~ sub_25a173ac4 -> sub_2641bcd38 : 152 -> 156
~ sub_25a173e7c -> sub_2641bd0f4 : 128 -> 132
~ sub_25a173fb8 -> sub_2641bd234 : 128 -> 132
~ _hx509_pem_read : 896 -> 936
~ sub_25a17639c -> sub_2641bf644 : 908 -> 912
~ sub_25a176ad4 -> sub_2641bfd80 : 780 -> 784
~ sub_25a178238 -> sub_2641c14e8 : 144 -> 152
~ sub_25a17840c -> sub_2641c16c4 : 292 -> 300
~ sub_25a178768 -> sub_2641c1a28 : 336 -> 340
~ sub_25a179444 -> sub_2641c2708 : 292 -> 288
~ _hx509_lock_reset_passwords : 84 -> 88
~ sub_25a179c34 -> sub_2641c2ef8 : 472 -> 480
~ sub_25a179e0c -> sub_2641c30d8 : 196 -> 204
~ sub_25a179ed0 -> sub_2641c31a4 : 704 -> 744
~ _hx509_name_expand : 608 -> 604
~ _hx509_bitstring_print : 304 -> 308
~ sub_25a17b614 -> sub_2641c4910 : 308 -> 312
~ sub_25a17bb14 -> sub_2641c4e14 : 516 -> 520
~ sub_25a17d02c -> sub_2641c6330 : 180 -> 184
~ _hx509_revoke_add_ocsp : 348 -> 356
~ _hx509_revoke_add_crl : 352 -> 356
~ _hx509_revoke_verify : 2120 -> 2128
~ sub_25a17e0dc -> sub_2641c73f8 : 516 -> 520
~ sub_25a17ee28 -> sub_2641c8148 : 244 -> 240
~ sub_25a181814 -> sub_2641cab30 : 48 -> 52
~ sub_25a181970 -> sub_2641cac90 : 68 -> 72
~ sub_25a1819b4 -> sub_2641cacd8 : 164 -> 168
~ sub_25a181a58 -> sub_2641cad80 : 344 -> 356
~ _hc_EVP_CipherUpdate : 436 -> 440
~ sub_25a18364c -> sub_2641cc984 : 760 -> 768
~ sub_25a183e9c -> sub_2641cd1dc : 284 -> 304
~ sub_25a184080 -> sub_2641cd3d4 : 284 -> 304
~ sub_25a18582c -> sub_2641ceb94 : 120 -> 76
CStrings:
- "URLWithString:"
- "UTF8String"
- "addValue:forHTTPHeaderField:"
- "bytes"
- "copy"
- "dataTaskWithRequest:completionHandler:"
- "dictionaryWithObjects:forKeys:count:"
- "ephemeralSessionConfiguration"
- "initWithBytesNoCopy:length:"
- "length"
- "localizedDescription"
- "numberWithInt:"
- "requestWithURL:"
- "resume"
- "sessionWithConfiguration:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "stringWithCString:encoding:"
- "stringWithUTF8String:"

```
