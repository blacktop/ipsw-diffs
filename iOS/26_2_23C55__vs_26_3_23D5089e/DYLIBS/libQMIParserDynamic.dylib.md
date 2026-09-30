## libQMIParserDynamic.dylib

> `/usr/lib/libQMIParserDynamic.dylib`

```diff

-1399.5.0.0.0
-  __TEXT.__text: 0x1aefc
-  __TEXT.__auth_stubs: 0x5b0
+1399.8.0.0.0
+  __TEXT.__text: 0x1b0ec
+  __TEXT.__auth_stubs: 0x5c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x8aa
-  __TEXT.__cstring: 0x24c7
-  __TEXT.__gcc_except_tab: 0x1c34
-  __TEXT.__unwind_info: 0xad0
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__cstring: 0x24f2
+  __TEXT.__gcc_except_tab: 0x1c74
+  __TEXT.__unwind_info: 0xaf0
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0xc50
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x308
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: A8FA87B4-D041-3034-8E7F-B6E9E27FB59A
-  Functions: 536
-  Symbols:   1192
-  CStrings:  392
+  UUID: B601EF61-D63F-32F1-A9F3-E8B846159C9A
+  Functions: 537
+  Symbols:   1197
+  CStrings:  393
 
Symbols:
+ __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorD1Ev
+ __ZNSt3__110shared_ptrIN3qmi17SerializedMessageEED1B8ne200100Ev
+ ___block_descriptor_tmp.7
- __ZNSt3__110shared_ptrIN3qmi17SerializedMessageEED2B8ne200100Ev
- ___block_descriptor_tmp.6
Functions:
~ __ZN3qmi18stripRequestHeaderEhRKNSt3__110shared_ptrIKNS_17SerializedMessageEEE : 44 -> 152
~ __ZN3qmi11fixupHeaderERKNSt3__110shared_ptrINS_17SerializedMessageEEEhh : 72 -> 84
+ __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
CStrings:
+ "This API cannot be called for raw messages"

```
