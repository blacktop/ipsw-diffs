## kperfdata

> `/System/Library/PrivateFrameworks/kperfdata.framework/kperfdata`

```diff

-161.0.0.0.0
-  __TEXT.__text: 0x81f8
-  __TEXT.__auth_stubs: 0x460
+164.0.0.0.0
+  __TEXT.__text: 0x8320
   __TEXT.__cstring: 0x350
   __TEXT.__const: 0x28
   __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__got: 0x20
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xc8
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x2e0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x91
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/kperf.framework/kperf
   - /usr/lib/libSystem.B.dylib
-  UUID: 37A2A2EB-9CC9-3238-BE43-92DE9CD6EA11
+  UUID: DFF4AC61-E743-3E49-B64A-C699DB24BF15
   Functions: 135
   Symbols:   275
   CStrings:  82
Functions:
~ _kpdecode_cursor_next_record : 4472 -> 4572
~ _add_thread_info_sched_data : 208 -> 212
~ __kpdecode_cursor_next_kevent : 508 -> 516
~ _batch_get_bytes : 696 -> 716
~ _kpep_config_create : 400 -> 404
~ _kpep_config_remove_event : 312 -> 316
~ _kpep_config_kpc_map : 112 -> 120
~ _kpep_config_kpc : 316 -> 324
~ _init_db_from_plist : 1552 -> 1576
~ _init_db_from_aliases_dict : 400 -> 412
~ _shipout : 180 -> 184
~ _get_to_stage_body : 492 -> 496
~ _kpfile_fdopenin_internal : 1436 -> 1440
~ _kpfile_read_next : 560 -> 568
~ _kpfile_read_events : 1168 -> 1172
~ _analyze_threadmap : 348 -> 356
~ _kpdecode_record_id_string_get_content : 572 -> 580
~ _add_string_data : 304 -> 300
~ _safe_encode : 956 -> 1000
~ _kdbg_comp_decode : 420 -> 436
~ _encode_row : 92 -> 100

```
