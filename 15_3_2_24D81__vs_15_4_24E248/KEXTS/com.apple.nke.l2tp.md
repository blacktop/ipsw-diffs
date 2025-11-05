## com.apple.nke.l2tp

> `com.apple.nke.l2tp`

```diff

 1016.0.0.0.0
   __TEXT.__cstring: 0xacd
   __TEXT.__const: 0x58
-  __TEXT_EXEC.__text: 0x3f8c
+  __TEXT_EXEC.__text: 0x3f70
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1d8
   __DATA.__common: 0x150

   __DATA_CONST.__got: 0x88
   __DATA_CONST.__kalloc_type: 0x200
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 61CCDD93-2FE3-3FFA-AA51-CD521E9577BE
-  Functions: 65
-  Symbols:   197
+  UUID: FE0B348F-DDAC-36FF-9CAF-1D1227007D7B
+  Functions: 62
+  Symbols:   195
   CStrings:  74
 
Symbols:
- l2tp_rfc_command.cold.1
- l2tp_rfc_set_socket.cold.1
Functions:
~ _l2tp_domain_init : 248 -> 244
~ _l2tp_domain_terminate : 248 -> 244
~ _l2tp_attach : 188 -> 196
~ _l2tp_ctloutput : 888 -> 900
- sub_fffffe000b6205f0
~ _l2tp_rfc_init : 76 -> 68
~ _l2tp_rfc_dispose : 92 -> 96
~ _l2tp_rfc_free_client : 144 -> 152
~ _l2tp_rfc_free_now : 548 -> 524
~ _l2tp_rfc_command : 2376 -> 2352
~ _l2tp_rfc_accept : 252 -> 244
~ _l2tp_rfc_compare_address : 156 -> 172
~ _l2tp_rfc_slowtimer : 460 -> 464
~ _l2tp_rfc_output : 96 -> 84
~ _l2tp_handle_data : 480 -> 484
~ _l2tp_handle_control : 1392 -> 1360
~ _l2tp_rfc_handle_ack : 308 -> 300
~ _l2tp_rfc_lower_input : 488 -> 492
~ _l2tp_udp_dispose_threads : 372 -> 380
~ _l2tp_udp_thread_func : 232 -> 220
~ _l2tp_udp_output : 388 -> 492
~ _l2tp_udp_attach : 448 -> 468
~ _l2tp_udp_detach : 68 -> 84
~ _l2tp_wan_attach : 484 -> 480
~ _l2tp_wan_detach : 192 -> 188

```
