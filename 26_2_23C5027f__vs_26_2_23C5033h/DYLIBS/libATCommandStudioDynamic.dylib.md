## libATCommandStudioDynamic.dylib

> `/usr/lib/libATCommandStudioDynamic.dylib`

```diff

-1399.2.0.0.0
-  __TEXT.__text: 0x5785c
-  __TEXT.__auth_stubs: 0xe90
+1399.4.0.0.0
+  __TEXT.__text: 0x57324
+  __TEXT.__auth_stubs: 0xe80
   __TEXT.__init_offsets: 0x10
   __TEXT.__const: 0x1b5c
-  __TEXT.__gcc_except_tab: 0x5a94
-  __TEXT.__cstring: 0x1d3e
-  __TEXT.__oslogstring: 0x2666
-  __TEXT.__unwind_info: 0x22c8
+  __TEXT.__gcc_except_tab: 0x59c0
+  __TEXT.__cstring: 0x1d49
+  __TEXT.__oslogstring: 0x2645
+  __TEXT.__unwind_info: 0x22b0
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0xa48
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0x24d8
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x108

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmav_ipc_router_dynamic.dylib
-  UUID: 02B93BAB-9A47-3AD9-B6EC-DBB2E1F5AED3
+  UUID: 50BF4804-42F4-3C11-9016-64F35C3E2AC3
   Functions: 1423
-  Symbols:   3537
-  CStrings:  540
+  Symbols:   3538
+  CStrings:  539
 
Symbols:
- _.str.29
- __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
Functions:
~ __ZNK13QMIServiceMsg9serializeEv : 452 -> 376
~ __ZN3qmi6Client5State4sendERNS0_9SendProxyE : 1480 -> 1264
~ __ZN3qmi11ClientProxy5State15handleSend_syncERKN3xpc4dictERKNS2_6objectE : 1448 -> 752
~ __ZN13QMIServiceMsg17createFromRawDataEPKhth : 204 -> 8
~ __ZN13QMIServiceMsg17createFromRawDataERKNSt3__16vectorIhNS0_9allocatorIhEEEEh : 92 -> 8
~ __ZNK13QMIServiceMsg9serializeEPvm : 352 -> 284
CStrings:
- "#I [%s]: Sending RAW Request: %s"

```
