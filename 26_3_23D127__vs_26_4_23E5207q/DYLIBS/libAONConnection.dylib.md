## libAONConnection.dylib

> `/usr/lib/libAONConnection.dylib`

```diff

-123.80.6.0.0
-  __TEXT.__text: 0x8360
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__const: 0x190
-  __TEXT.__cstring: 0x166d
+142.100.16.502.1
+  __TEXT.__text: 0x7fb4
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0x1a7a
   __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__oslogstring: 0x89f
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__oslogstring: 0x8de
+  __TEXT.__unwind_info: 0x230
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x8c
   __TEXT.__objc_stubs: 0x60
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x3e0
+  __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x380
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0xa0
   __DATA.__data: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70B2B71D-F2F2-312C-87C3-99E20C5926CB
-  Functions: 134
-  Symbols:   422
-  CStrings:  172
+  UUID: B67A04E4-32A4-3AC1-868B-39E6DBE74E1D
+  Functions: 122
+  Symbols:   386
+  CStrings:  187
 
Symbols:
+ _IOServiceGetMatchingServices
+ ___block_descriptor_tmp.126
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.128
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.27
+ _aon_net_get_ring_id_for_interface_type
+ _aon_net_get_tx_get_free_buffer_count
+ _aon_net_get_tx_ring_free_space
+ _aonnetworking_alpnstring__v_count
+ _ncbundle8__v_count
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _tb_message_copy_buffer
+ _tb_message_encode_buf
+ _tb_message_raw_encode_range_u8
+ _usleep
- _CFRunLoopAddTimer
- _CFRunLoopRemoveTimer
- _CFRunLoopTimerCreate
- _CFRunLoopTimerInvalidate
- _MatchTimeout
- ___aonnetworking_alpnstring__v_sizeof_block_invoke
- ___block_descriptor_tmp.107
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.11
- ___block_descriptor_tmp.110
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.114
- ___block_descriptor_tmp.115
- ___block_descriptor_tmp.116
- ___block_descriptor_tmp.117
- ___block_descriptor_tmp.118
- ___block_descriptor_tmp.119
- ___block_descriptor_tmp.12
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.17
- ___ncalpn8__v_raw_encode_block_invoke
- ___ncalpn8__v_sizeof_block_invoke
- ___ncbundle8__v_raw_encode_block_invoke
- ___ncbundle8__v_sizeof_block_invoke
- ___ncbundle8__v_visit_block_invoke
- ___ncpsk8__v_raw_encode_block_invoke
- ___ncpsk8__v_sizeof_block_invoke
- ___ncpskid8__v_raw_encode_block_invoke
- ___ncpskid8__v_sizeof_block_invoke
- _aonnetworking_alpnstring__v_visit
- _ncalpn8__v_visit
- _ncbundle8__v_visit
- _ncpsk8__v_visit
- _ncpskid8__v_visit
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
CStrings:
+ "/Library/Caches/com.apple.xbs/8485F0FA-60D3-4E4E-938D-F31555AEEE69/TemporaryDirectory.PojnBx/Binaries/RTKitNet_AP_Libraries/install/TempContent/Objects/RtKitNet.build/libAONConnection.build/DerivedSources/aon_networking.c"
+ "TB_FATAL: invalid tag in `[AONNetworking.ALPNString]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[AONNetworking.ALPNString]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCALPN8 (aka. UInt8)]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCALPN8 (aka. UInt8)]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCBUNDLE8 (aka. UInt8)]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCBUNDLE8 (aka. UInt8)]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCPSK8 (aka. UInt8)]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCPSK8 (aka. UInt8)]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCPSKID8 (aka. UInt8)]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCPSKID8 (aka. UInt8)]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: overflow detected when adding"
+ "TB_FATAL: overflow detected when adding (%s:%d)\n"
+ "TB_FATAL: overflow detected when multiplying"
+ "TB_FATAL: overflow detected when multiplying (%s:%d)\n"
+ "Unknown interface type %llu, defaulting to cellular ring ID %d"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[64c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "aon_net_get_tx_get_free_buffer_count"
+ "aon_net_get_tx_ring_free_space"
- "/Library/Caches/com.apple.xbs/Binaries/RTKitNet_AP_Libraries/install/TempContent/Objects/RtKitNet.build/libAONConnection.build/DerivedSources/aon_networking.c"
- "TB_FATAL: invalid tag in array metadata: 0x%x"
- "TB_FATAL: invalid tag in array metadata: 0x%x (%s:%d)\n"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[41c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"

```
