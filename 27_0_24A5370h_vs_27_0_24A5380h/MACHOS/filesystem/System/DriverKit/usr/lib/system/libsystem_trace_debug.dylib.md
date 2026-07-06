## libsystem_trace_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_trace_debug.dylib`

```diff

-  __TEXT.__text: 0xa92c
-  __TEXT.__const: 0x60
+  __TEXT.__text: 0xa374
+  __TEXT.__const: 0x58
   __TEXT.__cstring: 0x407
   __TEXT.__unwind_info: 0x140
   __TEXT.__auth_stubs: 0x220
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
Functions:
~ _os_trace_blob_add_slow : 360 -> 344
~ _os_trace_blob_addns : 2424 -> 2360
~ _os_trace_blob_addnws : 776 -> 760
~ __os_trace_utf8_to_mbs : 388 -> 384
~ _os_trace_blob_vaddf : 544 -> 524
~ _os_trace_blob_add_localtime : 508 -> 512
~ _os_trace_blob_add_hexdump : 1764 -> 1688
~ _os_log_fmt_delimit : 1392 -> 1344
~ _os_log_fmt_parse_annotation : 900 -> 892
~ _addaster : 184 -> 188
~ __os_log_fmt_flatten_masked_data : 956 -> 944
~ __os_log_fmt_flatten_to_blob : 664 -> 600
~ __os_log_fmt_flatten_data_into_blob : 1240 -> 1200
~ _os_log_fmt_flatten : 3908 -> 3776
~ _os_log_fmt_read_scalar : 392 -> 416
~ _os_log_fmt_convert_trace : 388 -> 340
~ _os_log_fmt_extract_pubdata : 316 -> 328
~ _os_log_fmt_read_aster_if_necessary : 792 -> 784
~ _os_log_fmt_get_data : 1388 -> 1384
~ __os_log_fmt_compose_read_range : 292 -> 296
~ __os_log_fmt_validate_cmd : 664 -> 672
~ _os_log_fmt_compose : 1600 -> 1576
~ __os_log_fmt_compose_masked_digest : 728 -> 704
~ __os_log_fmt_compose_masked_partial_redacted : 3680 -> 3568
~ __os_log_fmt_decode_data_access_failure : 524 -> 512
~ __os_log_fmt_compose_annotated : 140 -> 148
~ __os_log_fmt_compose_scalar : 1892 -> 1756
~ __os_log_fmt_compose_data : 932 -> 868
~ __os_log_fmt_builtin_annotated : 372 -> 364
~ __os_log_fmt_builtin_bool : 844 -> 792
~ __os_log_fmt_builtin_darwin_mode : 992 -> 776
~ __os_log_fmt_builtin_darwin_signal : 320 -> 300
~ __os_log_fmt_builtin_multichar : 1312 -> 1256
~ __os_log_fmt_builtin_timespec : 400 -> 396
~ __os_log_fmt_builtin_uuid_t : 728 -> 724
~ __os_log_fmt_spec_is_integer : 116 -> 132
~ __os_log_fmt_builtin_scaled : 680 -> 632
~ __os_log_fmt_compose_format_copy : 196 -> 192
~ __os_log_to_kernel : 656 -> 540
~ __os_log_fmt_decode_give_up : 96 -> 92
~ __os_log_fmt_decode_error : 364 -> 352
~ __os_log_fmt_decode_cmd_mismatch : 1152 -> 1100
~ __os_log_fmt_decode_bad_range : 156 -> 144
~ __os_log_fmt_decode_masked_unknown : 220 -> 216

```
