## Tightbeam

> `/System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`

```diff

-326.40.2.0.0
-  __TEXT.__text: 0x1a984
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__const: 0xcf6
-  __TEXT.__cstring: 0x283b
-  __TEXT.__constg_swiftt: 0xcc4
+326.60.64.0.0
+  __TEXT.__text: 0x1b87c
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__const: 0xd06
+  __TEXT.__cstring: 0x293b
+  __TEXT.__constg_swiftt: 0xccc
   __TEXT.__swift5_typeref: 0x726
-  __TEXT.__swift5_reflstr: 0x566
-  __TEXT.__swift5_fieldmd: 0xbb4
+  __TEXT.__swift5_reflstr: 0x576
+  __TEXT.__swift5_fieldmd: 0xbc0
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0xfc
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x780
+  __TEXT.__unwind_info: 0x858
   __TEXT.__eh_frame: 0x6d0
-  __DATA.__auth_got: 0x3c8
+  __DATA.__auth_got: 0x3d8
   __DATA.__got: 0xa0
   __DATA.__auth_ptr: 0x120
   __DATA.__const: 0x1ed8
   __DATA.__objc_classlist: 0x40
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x640
-  __DATA.__data: 0x9a8
+  __DATA.__data: 0x9b0
   __DATA.__bss: 0x658
   __DATA.__common: 0x10
   - /System/ExclaveKit/usr/lib/libSystem.dylib

   - /System/ExclaveKit/usr/lib/swift/libswift_errno.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_stdio.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_time.dylib
-  Functions: 967
-  Symbols:   2058
-  CStrings:  218
+  Functions: 1017
+  Symbols:   2105
+  CStrings:  224
 
Symbols:
+ _$s9Tightbeam0A8EndpointO14cL4NonBlockingyACSu_tcACmFWC
+ _$s9Tightbeam16ClientConnectionC10connectionACSv_tcfC
+ _$s9Tightbeam16ClientConnectionC10connectionACSv_tcfCTj
+ _$s9Tightbeam16ClientConnectionC10connectionACSv_tcfCTq
+ _$s9Tightbeam16ClientConnectionC10connectionACSv_tcfc
+ _$sSS7cStringSSSPys4Int8VG_tcfC
+ __tb_xrt_utils_fourcc_numeric
+ _dlerror
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
+ tb_message_configure_received.cold.1
+ tb_message_precheck_decoding.cold.1
+ tb_message_precheck_decoding.cold.2
+ tb_message_precheck_decoding.cold.3
+ tb_message_precheck_decoding.cold.4
+ tb_message_precheck_encoding.cold.1
+ tb_message_precheck_encoding.cold.2
+ tb_message_precheck_encoding.cold.3
CStrings:
+ "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS18.2.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
+ "Can't construct Array with count < 0"
+ "Swift/Array.swift"
+ "TB_FATAL: tb_message_raw_decode_f32_v2: %!d(MISSING) (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: tb_message_raw_decode_f64_v2: %!d(MISSING) (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: tb_message_raw_encode_f32_v2: %!d(MISSING) (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: tb_message_raw_encode_f64_v2: %!d(MISSING) (%!s(MISSING):%!d(MISSING))\n"
+ "could not load dylib at "
+ "dlerror() incorrectly returned nil"
+ "getting key %!l(MISSING)u which is deleted"
+ "getting key %!l(MISSING)u while destructors are running"
+ "setting key %!l(MISSING)u which is deleted"
+ "setting key %!l(MISSING)u while destructors running"
- "/AppleInternal/Library/BuildRoots/b4a7daee-7dd0-11ef-a7b2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS18.1.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
- "Cap move from %!l(MISSING)x to return slot should succeed"
- "Result cap move from %!l(MISSING)x to return slot should succeed"
- "getting key %!u(MISSING) which is deleted"
- "getting key %!u(MISSING) while destructors are running"
- "setting key %!u(MISSING) which is deleted"
- "setting key %!u(MISSING) while destructors running"

```
