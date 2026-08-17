## libATCommandStudioDynamic.dylib

> `/usr/lib/libATCommandStudioDynamic.dylib`

```diff

 1585.0.0.0.0
-  __TEXT.__text: 0x55b7c
+  __TEXT.__text: 0x556f0
   __TEXT.__init_offsets: 0x10
   __TEXT.__const: 0x1b20
-  __TEXT.__gcc_except_tab: 0x58bc
-  __TEXT.__cstring: 0x2032
-  __TEXT.__oslogstring: 0x259d
-  __TEXT.__unwind_info: 0x2308
+  __TEXT.__gcc_except_tab: 0x57f0
+  __TEXT.__cstring: 0x203d
+  __TEXT.__oslogstring: 0x257f
+  __TEXT.__unwind_info: 0x22f0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xa80
   __DATA_CONST.__weak_got: 0x48

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmav_ipc_router_dynamic.dylib
   Functions: 1435
-  Symbols:   2296
-  CStrings:  540
+  Symbols:   2295
+  CStrings:  539
 
Symbols:
- __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
Functions:
~ __ZN3qmi11ClientProxy5State15handleSend_syncERKN3xpc4dictERKNS2_6objectE : 1216 -> 704
~ __ZN3qmi6Client5State4sendERNS0_9SendProxyE : 1472 -> 1244
~ __ZNK13QMIServiceMsg9serializeEv : 452 -> 376
~ __ZN13QMIServiceMsg17createFromRawDataEPKhth : 204 -> 8
~ __ZN13QMIServiceMsg17createFromRawDataERKNSt3__16vectorIhNS0_9allocatorIhEEEEh : 92 -> 8
~ __ZNK13QMIServiceMsg9serializeEPvm : 352 -> 284
CStrings:
- "[%s]: Sending RAW Request: %s"
```
