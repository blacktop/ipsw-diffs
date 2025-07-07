## libAONConnection.dylib

> `/usr/lib/libAONConnection.dylib`

```diff

-106.0.0.0.0
-  __TEXT.__text: 0x7a1c
+119.0.0.0.0
+  __TEXT.__text: 0x7ad8
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__const: 0x168
-  __TEXT.__cstring: 0x1634
-  __TEXT.__gcc_except_tab: 0x138
-  __TEXT.__oslogstring: 0x6c0
+  __TEXT.__const: 0x178
+  __TEXT.__cstring: 0x1605
+  __TEXT.__gcc_except_tab: 0xec
+  __TEXT.__oslogstring: 0x757
   __TEXT.__unwind_info: 0x218
   __TEXT.__objc_classname: 0x1
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__const: 0x3c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x350
   __AUTH_CONST.__const: 0x160

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A82770E5-CC70-32BB-9D47-6FD12BACB74B
-  Functions: 130
-  Symbols:   397
+  UUID: F3173633-2AFD-317D-867C-59770C5CAB5B
+  Functions: 132
+  Symbols:   399
   CStrings:  147
 
Symbols:
+ GCC_except_table38
+ GCC_except_table43
+ __ZL30aon_net_tx_submission_doorbellPvjPtj
+ __ZL8fileName
+ ___aon_net_service_init_block_invoke.17
+ ___aon_net_service_init_block_invoke.18
+ ___block_literal_global.29
+ _aonnetworking_networkingservice_connectflow
+ _ncalpn8__v_count
+ _ncpsk8__v_count
+ _ncpskid8__v_count
- GCC_except_table30
- GCC_except_table40
- GCC_except_table49
- __ZL30aon_net_tx_submission_doorbellP14aon_net_clientjPtj
- ___aon_net_service_init_block_invoke_10
- ___aon_net_service_init_block_invoke_7
- ___aon_net_service_init_block_invoke_8
- ___aon_net_service_init_block_invoke_9
- ___block_descriptor_40_ea8_32r_e11_v20?0Q8C16lr32l8
- ___block_descriptor_48_ea8_32r_e11_v20?0Q8C16lr32l8
- ___block_literal_global.30
CStrings:
+ "%s:%d channel %p destructed"
+ "%s:%d init() failed, baseAddr %p memSize %u bufferSize %u syncBatch %u # of rings %u"
+ "%s:%d processCompletion() channel %p numBuffers %u"
+ "%s:%d processSubmission() channel %p ringId %u numBuffers %u"
+ "%s:%d reset() channel %p"
+ "Failed to allocate memory for PSK"
+ "Failed to allocate memory for PSK ID"
+ "Invalid ALPN at index %zu"
+ "Invalid PSK ID size: %zu"
+ "Invalid PSK size: %zu"
+ "Invalid psk id info"
+ "Invalid psk info"
- "AONNetSharedMemChannel [%p] destroy"
- "AONNetSharedMemChannel [%p] init. mem=[%p], size=[%u]"
- "AONNetSharedMemChannel [%p] reset"
- "[%p] processCompletion of numBuffers=[%u]"
- "[%p] processSubmission ring=[%u], numBuffers=[%u]"
- "aon_net_service_init_block_invoke_6"
- "invalid psk"
- "invalid psk id"
- "missing psk id info"
- "missing psk info"
- "psk"
- "psk_id"

```
