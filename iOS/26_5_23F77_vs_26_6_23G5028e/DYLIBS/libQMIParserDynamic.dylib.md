## libQMIParserDynamic.dylib

> `/usr/lib/libQMIParserDynamic.dylib`

```diff

 1418.1.0.0.0
-  __TEXT.__text: 0x1b4d0
-  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__text: 0x1b6ac
+  __TEXT.__auth_stubs: 0x5c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x8ba
-  __TEXT.__cstring: 0x24c7
-  __TEXT.__gcc_except_tab: 0x1bd8
-  __TEXT.__unwind_info: 0xac0
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__cstring: 0x24f2
+  __TEXT.__gcc_except_tab: 0x1c14
+  __TEXT.__unwind_info: 0xae0
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0xc50
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x308
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: BFB483F3-A346-320C-B93B-A4BBD04830C4
-  Functions: 535
-  Symbols:   1187
-  CStrings:  392
+  UUID: E9E3CD42-226A-3D94-A401-B07B5DB87B3A
+  Functions: 536
+  Symbols:   1192
+  CStrings:  393
 
Symbols:
+ __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorD1Ev
+ __ZNSt3__110shared_ptrIN3qmi17SerializedMessageEED1B9nqe210106Ev
+ ___block_descriptor_tmp.7
- __ZNSt3__110shared_ptrIN3qmi17SerializedMessageEED2B9nqe210106Ev
- ___block_descriptor_tmp.6
Functions:
~ __ZN3qmi18stripRequestHeaderEhRKNSt3__110shared_ptrIKNS_17SerializedMessageEEE : 44 -> 152
~ __ZN3qmi11fixupHeaderERKNSt3__110shared_ptrINS_17SerializedMessageEEEhh : 72 -> 84
+ __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
CStrings:
+ "This API cannot be called for raw messages"

```
