## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-5569.80.42.502.1
-  __TEXT.__text: 0xcfaa8
+5569.80.53.0.2
+  __TEXT.__text: 0xcfbe4
   __TEXT.__auth_stubs: 0x1ac0
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x3ad

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6ACBBDAA-3AC7-3BA6-BF73-30D58A76286D
+  UUID: 4806EFAC-331B-32B1-8CBF-B07C7E4617A2
   Functions: 1150
   Symbols:   3159
   CStrings:  2931
Symbols:
+ _____quic_signpost_is_enabled_block_invoke.4789
+ ___block_descriptor_tmp.12.4844
+ ___block_descriptor_tmp.4622
+ ___block_descriptor_tmp.4787
+ ___block_descriptor_tmp.60.4712
+ ___block_literal_global.4620
+ ___block_literal_global.4774
+ ___quic_signpost_is_enabled._quic_signposts_enabled.4775
+ ___quic_signpost_is_enabled._quic_signposts_once.4773
- _____quic_signpost_is_enabled_block_invoke.4788
- ___block_descriptor_tmp.12.4843
- ___block_descriptor_tmp.4621
- ___block_descriptor_tmp.4786
- ___block_descriptor_tmp.60.4711
- ___block_literal_global.4619
- ___block_literal_global.4773
- ___quic_signpost_is_enabled._quic_signposts_enabled.4774
- ___quic_signpost_is_enabled._quic_signposts_once.4772
Functions:
~ _quic_packet_parser_inner : 12176 -> 12464
~ __quic_packet_destroy : 876 -> 884
~ _quic_frame_list_flush : 520 -> 528
~ _quic_crypto_queue_process : 1092 -> 1108
~ ___quic_conn_destroy_block_invoke : 456 -> 416
~ __quic_crypto_queue_destroy : 496 -> 504
~ _quic_migration_probe_path : 3504 -> 3512
~ _quic_migration_received_challenge : 2788 -> 2796
~ _quic_conn_migrate_to_path : 3092 -> 3100
~ ___quic_migration_create_block_invoke : 456 -> 480
~ -[QUICLog addFrameList:frame_list:] : 4864 -> 4872
~ _qpod_conn_free : 268 -> 236
~ _quic_ack_destroy_multipath_pn_space : 444 -> 448

```
