## libATCommandStudioDynamic.dylib

> `/usr/lib/libATCommandStudioDynamic.dylib`

```diff

-1585.0.0.0.0
-  __TEXT.__text: 0x54854
+1594.0.0.0.0
+  __TEXT.__text: 0x54cd4
   __TEXT.__init_offsets: 0x10
   __TEXT.__const: 0x1b20
-  __TEXT.__gcc_except_tab: 0x57f0
-  __TEXT.__cstring: 0x203d
-  __TEXT.__oslogstring: 0x257f
-  __TEXT.__unwind_info: 0x2520
+  __TEXT.__gcc_except_tab: 0x58bc
+  __TEXT.__cstring: 0x2032
+  __TEXT.__oslogstring: 0x259d
+  __TEXT.__unwind_info: 0x2538
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xa80
   __DATA_CONST.__weak_got: 0x48

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmav_ipc_router_dynamic.dylib
   Functions: 1435
-  Symbols:   2295
-  CStrings:  539
+  Symbols:   2296
+  CStrings:  540
 
Symbols:
+ __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
Functions:
~ __ZN3qmi11ClientProxy5State15handleSend_syncERKN3xpc4dictERKNS2_6objectE : 704 -> 1216
~ __ZN3qmi6Client5State4sendERNS0_9SendProxyE : 1244 -> 1472
~ __ZNK13QMIServiceMsg9serializeEv : 376 -> 452
~ __ZN13QMIServiceMsg17createFromRawDataEPKhth : 8 -> 204
~ __ZN13QMIServiceMsg17createFromRawDataERKNSt3__16vectorIhNS0_9allocatorIhEEEEh : 8 -> 92
~ __ZNK13QMIServiceMsg9serializeEPvm : 272 -> 328
CStrings:
+ "[%s]: Sending RAW Request: %s"
```
