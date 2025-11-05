## libheimdal-asn1.dylib

> `/usr/lib/libheimdal-asn1.dylib`

```diff

-693.60.3.0.0
-  __TEXT.__text: 0x9efc
+693.100.10.0.0
+  __TEXT.__text: 0x9058
   __TEXT.__auth_stubs: 0x170
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x164

   __DATA.__common: 0x8
   __DATA.__bss: 0x64
   - /usr/lib/libSystem.B.dylib
-  UUID: BD048EB0-FE92-3D97-82D2-744937207C3B
+  UUID: DE84C1B9-711F-3346-BE9E-4B99BCD45CB0
   Functions: 154
   Symbols:   187
   CStrings:  32
Functions:
~ _der_heim_oid_cmp : 140 -> 136
~ _der_heim_octet_string_cmp : 136 -> 132
~ _der_heim_bit_string_cmp : 380 -> 360
~ _der_heim_integer_cmp : 196 -> 188
~ _der_heim_bmp_string_cmp : 140 -> 136
~ _der_heim_universal_string_cmp : 140 -> 136
~ _der_copy_general_string : 104 -> 96
~ _der_copy_printable_string : 188 -> 180
~ _der_copy_bmp_string : 200 -> 184
~ _der_copy_universal_string : 200 -> 184
~ _der_copy_octet_string : 184 -> 168
~ _der_copy_heim_integer : 200 -> 184
~ _der_copy_oid : 200 -> 184
~ _der_copy_bit_string : 200 -> 184
~ _der_parse_hex_heim_integer : 520 -> 488
~ _der_print_hex_heim_integer : 244 -> 220
~ _der_print_heim_oid : 388 -> 340
~ _der_parse_heim_oid : 476 -> 432
~ _der_get_unsigned : 260 -> 220
~ _der_get_integer : 252 -> 220
~ _der_get_length : 456 -> 408
~ _der_get_boolean : 140 -> 128
~ _der_get_general_string : 452 -> 416
~ _der_get_printable_string : 304 -> 284
~ _der_get_bmp_string : 636 -> 576
~ _der_get_universal_string : 640 -> 592
~ _der_get_octet_string : 224 -> 200
~ _der_get_octet_string_ber : 932 -> 808
~ _der_get_tag : 488 -> 452
~ _der_get_heim_integer : 880 -> 768
~ _der_get_time : 284 -> 256
~ _der_get_oid : 736 -> 676
~ _der_match_tag : 176 -> 164
~ _der_match_tag2 : 300 -> 272
~ _der_match_tag_and_length : 296 -> 268
~ __heim_fix_dce : 124 -> 116
~ _der_get_bit_string : 468 -> 416
~ _generalizedtime2time : 372 -> 360
~ __heim_len_unsigned : 144 -> 120
~ __heim_len_int : 300 -> 264
~ _der_length_len : 140 -> 124
~ _der_length_tag : 132 -> 116
~ _der_length_heim_integer : 192 -> 152
~ _der_length_oid : 176 -> 160
~ _der_put_unsigned : 416 -> 376
~ _der_put_integer : 564 -> 508
~ _der_put_length : 332 -> 304
~ _der_put_boolean : 140 -> 128
~ _der_put_general_string : 172 -> 164
~ _der_put_octet_string : 168 -> 164
~ _der_put_bmp_string : 292 -> 276
~ _der_put_universal_string : 356 -> 340
~ _der_put_heim_integer : 752 -> 668
~ _der_put_generalized_time : 228 -> 204
~ __heim_time2generalizedtime : 544 -> 496
~ _der_put_utctime : 228 -> 204
~ _der_put_oid : 472 -> 444
~ _der_put_tag : 416 -> 388
~ _der_put_length_and_tag : 280 -> 260
~ _der_put_bit_string : 308 -> 284
~ __heim_der_set_sort : 236 -> 216
~ _der_get_class_name : 76 -> 72
~ _get_type : 188 -> 168
~ _der_get_type_name : 76 -> 72
~ _der_get_tag_name : 76 -> 72
~ _decode_heim_any : 672 -> 624
~ __der_timegm : 820 -> 728
~ _is_leap : 172 -> 156
~ __der_gmtime : 508 -> 468
~ _encode_hex : 380 -> 360
~ _rk_hex_decode : 352 -> 332
~ _pos : 184 -> 172
~ _rk_strpoolfree : 88 -> 80
~ _rk_strpoolprintf : 400 -> 368
~ _rk_strpoolcollect : 120 -> 112
~ __asn1_bmember_isset_bit : 84 -> 80
~ __asn1_bmember_put_bit : 200 -> 180
~ __asn1_decode : 4040 -> 3548
~ __asn1_bmember_get_bit : 128 -> 116
~ __asn1_encode : 3748 -> 3312
~ __asn1_length : 1664 -> 1460
~ __asn1_free : 1344 -> 1160
~ __asn1_copy : 2240 -> 1940
~ __asn1_decode_top : 156 -> 148
~ __asn1_copy_top : 132 -> 124
CStrings:
+ "type larger then asn1_template_prim: %u"
+ "unknown opcode: %u"
- "type larger then asn1_template_prim: %d"
- "unknown opcode: %d"

```
