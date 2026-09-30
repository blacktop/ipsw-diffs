## libATCommandStudioDynamic.dylib

> `/usr/lib/libATCommandStudioDynamic.dylib`

```diff

 1249.1.0.0.0
-  __TEXT.__text: 0x56948
-  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__text: 0x563ec
+  __TEXT.__auth_stubs: 0xf60
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x1acd
-  __TEXT.__gcc_except_tab: 0x5a48
-  __TEXT.__cstring: 0x346f
-  __TEXT.__oslogstring: 0x100e
-  __TEXT.__unwind_info: 0x22a0
+  __TEXT.__gcc_except_tab: 0x5964
+  __TEXT.__cstring: 0x347a
+  __TEXT.__oslogstring: 0xfed
+  __TEXT.__unwind_info: 0x2288
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0xac0
-  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH_CONST.__const: 0x2670
   __DATA.__bss: 0x8
   __DATA.__common: 0x10

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmav_ipc_router_dynamic.dylib
-  UUID: EF6C44DD-FDE1-34FA-9685-358AE0111B2B
+  UUID: EAE91B2A-5430-3881-B39E-DA5E1C9B72A8
   Functions: 1446
-  Symbols:   3580
-  CStrings:  539
+  Symbols:   3581
+  CStrings:  538
 
Symbols:
- _.str.29
- _.str.30
- __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
Functions:
~ __ZNK13QMIServiceMsg9serializeEv : 484 -> 376
~ __ZN3qmi6Client5State4sendERNS0_9SendProxyE : 1480 -> 1264
~ __ZN3qmi11ClientProxy5State15handleSend_syncERKN3xpc4dictERKNS2_6objectE : 1452 -> 752
~ __ZN13QMIServiceMsg17createFromRawDataEPKhth : 204 -> 8
~ __ZN13QMIServiceMsg17createFromRawDataERKNSt3__16vectorIhNS0_9allocatorIhEEEEh : 92 -> 8
~ __ZNK13QMIServiceMsg9serializeEPvm : 352 -> 284
CStrings:
- "#I [%s]: Sending RAW Request: %s"

```
