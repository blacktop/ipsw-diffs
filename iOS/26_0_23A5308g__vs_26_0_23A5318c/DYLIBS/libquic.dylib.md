## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-5569.0.275.0.6
-  __TEXT.__text: 0xcf434
+5569.2.2.0.0
+  __TEXT.__text: 0xcf458
   __TEXT.__auth_stubs: 0x1aa0
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x39d
-  __TEXT.__cstring: 0x8f86
+  __TEXT.__cstring: 0x8f10
   __TEXT.__oslogstring: 0x117b5
   __TEXT.__unwind_info: 0xe30
   __TEXT.__objc_classname: 0xa

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F2E4DB3-B8A2-3B71-8F02-E4ACD861F1C1
-  Functions: 1156
-  Symbols:   3175
+  UUID: 72AE4818-A458-31E0-BD37-7E6F929EF227
+  Functions: 1157
+  Symbols:   3177
   CStrings:  2926
 
Symbols:
+ _____quic_signpost_is_enabled_block_invoke.4770
+ ___block_descriptor_tmp.12.4825
+ ___block_descriptor_tmp.149.4254
+ ___block_descriptor_tmp.18.4499
+ ___block_descriptor_tmp.4317
+ ___block_descriptor_tmp.4602
+ ___block_descriptor_tmp.4768
+ ___block_descriptor_tmp.60.4693
+ ___block_literal_global.4600
+ ___block_literal_global.4755
+ ___quic_signpost_is_enabled._quic_signposts_enabled.4756
+ ___quic_signpost_is_enabled._quic_signposts_once.4754
+ _objc_retain_x26
+ _quic_path_has_migration_info
- _____quic_signpost_is_enabled_block_invoke.4773
- ___block_descriptor_tmp.12.4828
- ___block_descriptor_tmp.149.4256
- ___block_descriptor_tmp.18.4502
- ___block_descriptor_tmp.4319
- ___block_descriptor_tmp.4605
- ___block_descriptor_tmp.4771
- ___block_descriptor_tmp.60.4696
- ___block_literal_global.4603
- ___block_literal_global.4758
- ___quic_signpost_is_enabled._quic_signposts_enabled.4759
- ___quic_signpost_is_enabled._quic_signposts_once.4757
- _objc_retain_x27
Functions:
~ __quic_packet_builder_assemble : 7212 -> 7128
~ _quic_recovery_pto : 4340 -> 4152
~ _quic_migration_probe_path : 3464 -> 3488
+ _quic_path_has_migration_info
CStrings:
+ "quic_path_has_migration_info"
- "%s tag is not at the end of the buffer %p != %p (key_state %d, total_len %u, header_len %u, payload_len %u, pn %llu,  pn_len %u, frame_count %llu)"

```
