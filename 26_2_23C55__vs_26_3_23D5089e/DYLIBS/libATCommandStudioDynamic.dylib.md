## libATCommandStudioDynamic.dylib

> `/usr/lib/libATCommandStudioDynamic.dylib`

```diff

-1399.5.0.0.0
-  __TEXT.__text: 0x57324
-  __TEXT.__auth_stubs: 0xe80
+1399.8.0.0.0
+  __TEXT.__text: 0x5785c
+  __TEXT.__auth_stubs: 0xe90
   __TEXT.__init_offsets: 0x10
   __TEXT.__const: 0x1b5c
-  __TEXT.__gcc_except_tab: 0x59c0
-  __TEXT.__cstring: 0x1d49
-  __TEXT.__oslogstring: 0x2645
-  __TEXT.__unwind_info: 0x22b0
+  __TEXT.__gcc_except_tab: 0x5a94
+  __TEXT.__cstring: 0x1d3e
+  __TEXT.__oslogstring: 0x2666
+  __TEXT.__unwind_info: 0x22c8
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0xa48
-  __AUTH_CONST.__auth_got: 0x748
+  __AUTH_CONST.__auth_got: 0x750
   __AUTH_CONST.__const: 0x24d8
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x108

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmav_ipc_router_dynamic.dylib
-  UUID: 4DEFD016-B5FE-3F46-B30C-34585AD2924A
+  UUID: 5134B3FB-E033-3593-80F6-B68AE109B3DD
   Functions: 1423
-  Symbols:   3538
-  CStrings:  539
+  Symbols:   3537
+  CStrings:  540
 
Symbols:
+ _.str.29
+ __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
Functions:
~ __ZNK13QMIServiceMsg9serializeEv : 376 -> 452
~ __ZN3qmi6Client5State4sendERNS0_9SendProxyE : 1264 -> 1480
~ __ZN3qmi11ClientProxy5State15handleSend_syncERKN3xpc4dictERKNS2_6objectE : 752 -> 1448
~ __ZN13QMIServiceMsg17createFromRawDataEPKhth : 8 -> 204
~ __ZN13QMIServiceMsg17createFromRawDataERKNSt3__16vectorIhNS0_9allocatorIhEEEEh : 8 -> 92
~ __ZNK13QMIServiceMsg9serializeEPvm : 284 -> 352
CStrings:
+ "#I [%s]: Sending RAW Request: %s"

```
