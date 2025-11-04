## libAONConnection.dylib

> `/usr/lib/libAONConnection.dylib`

```diff

-123.40.2.0.0
-  __TEXT.__text: 0x8238
+123.60.2.0.0
+  __TEXT.__text: 0x8360
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__const: 0x188
   __TEXT.__cstring: 0x166d

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B350991F-E034-377E-A626-0D60E47F17E8
+  UUID: 0FC7CD6C-73F6-3143-941A-2D9EEC70C225
   Functions: 134
-  Symbols:   421
+  Symbols:   422
   CStrings:  172
 
Symbols:
+ __ZZZ20aon_net_service_initEUb_E49debug_detected_buffer_leak_in_previous_completion
Functions:
~ ___aon_net_service_init_block_invoke_5 : 784 -> 824
~ _aonnetworking_networkingservice_connectflow : 2772 -> 3028
CStrings:
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[41c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"

```
