## Tightbeam

> `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`

```diff

-326.40.2.0.0
-  __TEXT.__text: 0x292e0
+326.60.64.0.0
+  __TEXT.__text: 0x29e00
   __TEXT.__auth_stubs: 0x10e0
   __TEXT.__const: 0x161a
-  __TEXT.__cstring: 0x2a3c
-  __TEXT.__constg_swiftt: 0x14a0
+  __TEXT.__cstring: 0x2bbc
+  __TEXT.__constg_swiftt: 0x14a8
   __TEXT.__swift5_typeref: 0xb0e
-  __TEXT.__swift5_fieldmd: 0x1024
+  __TEXT.__swift5_fieldmd: 0x1030
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x839
+  __TEXT.__swift5_reflstr: 0x849
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0xb8
   __TEXT.__swift5_types: 0x15c

   __TEXT.__swift5_capture: 0xc4
   __TEXT.__oslogstring: 0x16e
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0xb30
+  __TEXT.__unwind_info: 0xbe8
   __TEXT.__eh_frame: 0x7f8
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x1de

   __DATA.__bss: 0xf90
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__data: 0x16e0
+  __DATA_DIRTY.__data: 0x16e8
   __DATA_DIRTY.__bss: 0x180
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1289
-  Symbols:   636
-  CStrings:  279
+  Functions: 1332
+  Symbols:   679
+  CStrings:  287
 
Symbols:
+ _tb_endpoint_get_interface_identifier
+ _tb_endpoint_set_interface_identifier
+ _tb_message_configure_received
+ _tb_message_precheck_decoding
+ _tb_message_precheck_encoding
+ _tb_message_raw_decode_bool
+ _tb_message_raw_decode_f32
+ _tb_message_raw_decode_f32_v2
+ _tb_message_raw_decode_f64
+ _tb_message_raw_decode_f64_v2
+ _tb_message_raw_decode_s16
+ _tb_message_raw_decode_s32
+ _tb_message_raw_decode_s64
+ _tb_message_raw_decode_s8
+ _tb_message_raw_decode_u16
+ _tb_message_raw_decode_u32
+ _tb_message_raw_decode_u64
+ _tb_message_raw_decode_u8
+ _tb_message_raw_encode_bool
+ _tb_message_raw_encode_f32
+ _tb_message_raw_encode_f32_v2
+ _tb_message_raw_encode_f64
+ _tb_message_raw_encode_f64_v2
+ _tb_message_raw_encode_s16
+ _tb_message_raw_encode_s32
+ _tb_message_raw_encode_s64
+ _tb_message_raw_encode_s8
+ _tb_message_raw_encode_u16
+ _tb_message_raw_encode_u32
+ _tb_message_raw_encode_u64
+ _tb_message_raw_encode_u8
CStrings:
+ "TB_FATAL: tb_message_raw_decode_f32_v2: %!d(MISSING)"
+ "TB_FATAL: tb_message_raw_decode_f32_v2: %!d(MISSING) (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: tb_message_raw_decode_f64_v2: %!d(MISSING)"
+ "TB_FATAL: tb_message_raw_decode_f64_v2: %!d(MISSING) (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: tb_message_raw_encode_f32_v2: %!d(MISSING)"
+ "TB_FATAL: tb_message_raw_encode_f32_v2: %!d(MISSING) (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: tb_message_raw_encode_f64_v2: %!d(MISSING)"
+ "TB_FATAL: tb_message_raw_encode_f64_v2: %!d(MISSING) (%!s(MISSING):%!d(MISSING))\n"

```
