## libMIPCSdk.dylib

> `/usr/lib/libMIPCSdk.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`

```diff

-176.0.0.0.0
-  __TEXT.__text: 0x37b7e4
-  __TEXT.__const: 0x14970
-  __TEXT.__gcc_except_tab: 0x1e3b4
-  __TEXT.__cstring: 0x145a7
-  __TEXT.__unwind_info: 0xc4a8
+177.0.0.0.0
+  __TEXT.__text: 0x37c488
+  __TEXT.__const: 0x14a00
+  __TEXT.__gcc_except_tab: 0x1e450
+  __TEXT.__cstring: 0x145f5
+  __TEXT.__unwind_info: 0xc4f0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2d100
+  __AUTH_CONST.__const: 0x2d238
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x158
   __AUTH.__data: 0x10
   __DATA.__bss: 0x60
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 11154
-  Symbols:   18975
-  CStrings:  2021
+  Functions: 11172
+  Symbols:   19004
+  CStrings:  2023
 
Symbols:
+ __ZN4mipc12ConfirmationILt63281EED0Ev
+ __ZN4mipc12ConfirmationILt63281EED1Ev
+ __ZN4mipc9dale_skpr27Service_Priority_Update_Cnf11deserializeEv
+ __ZN4mipc9dale_skpr27Service_Priority_Update_CnfC1ENS_5ErrorENS_5SimIdE
+ __ZN4mipc9dale_skpr27Service_Priority_Update_CnfC1EPKhm
+ __ZN4mipc9dale_skpr27Service_Priority_Update_CnfC2ENS_5ErrorENS_5SimIdE
+ __ZN4mipc9dale_skpr27Service_Priority_Update_CnfC2EPKhm
+ __ZN4mipc9dale_skpr27Service_Priority_Update_CnfD0Ev
+ __ZN4mipc9dale_skpr27Service_Priority_Update_CnfD1Ev
+ __ZN4mipc9dale_skpr27Service_Priority_Update_CnfD2Ev
+ __ZN4mipc9dale_skpr27Service_Priority_Update_ReqC1ENS_5SimIdE
+ __ZN4mipc9dale_skpr27Service_Priority_Update_ReqC2ENS_5SimIdE
+ __ZN4mipc9dale_skpr27Service_Priority_Update_ReqD0Ev
+ __ZN4mipc9dale_skpr27Service_Priority_Update_ReqD1Ev
+ __ZN4mipc9dale_skpr27Service_Priority_Update_ReqD2Ev
+ __ZNK4mipc9dale_skpr27Service_Priority_Update_Cnf7getSizeEv
+ __ZNK4mipc9dale_skpr27Service_Priority_Update_Req7getSizeEv
+ __ZNK4mipc9dale_skpr27Service_Priority_Update_Req9serializeEv
+ __ZTIN4mipc12ConfirmationILt63281EEE
+ __ZTIN4mipc7RequestILt63281EEE
+ __ZTIN4mipc9dale_skpr27Service_Priority_Update_CnfE
+ __ZTIN4mipc9dale_skpr27Service_Priority_Update_ReqE
+ __ZTSN4mipc12ConfirmationILt63281EEE
+ __ZTSN4mipc7RequestILt63281EEE
+ __ZTSN4mipc9dale_skpr27Service_Priority_Update_CnfE
+ __ZTSN4mipc9dale_skpr27Service_Priority_Update_ReqE
+ __ZTVN4mipc12ConfirmationILt63281EEE
+ __ZTVN4mipc9dale_skpr27Service_Priority_Update_CnfE
+ __ZTVN4mipc9dale_skpr27Service_Priority_Update_ReqE
CStrings:
+ "dale_skpr::Service_Priority_Update_Cnf"
+ "dale_skpr::Service_Priority_Update_Req"
```
