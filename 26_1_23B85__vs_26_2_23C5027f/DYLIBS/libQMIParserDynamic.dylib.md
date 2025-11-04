## libQMIParserDynamic.dylib

> `/usr/lib/libQMIParserDynamic.dylib`

```diff

-1397.0.0.0.0
-  __TEXT.__text: 0x1aed8
-  __TEXT.__auth_stubs: 0x5b0
+1399.2.0.0.0
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
-  UUID: CE783424-D39A-32EF-AD9D-E40FBECDDE38
-  Functions: 536
-  Symbols:   1192
-  CStrings:  392
+  UUID: 99781961-8A03-3FEE-B384-FA6A735DBA98
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
~ __ZNK18QmiMessageRegistry27getAllQmiMessageDefinitionsEv : 748 -> 760
~ __ZN3qmi18stripRequestHeaderEhRKNSt3__110shared_ptrIKNS_17SerializedMessageEEE : 44 -> 152
~ __ZN3qmi11fixupHeaderERKNSt3__110shared_ptrINS_17SerializedMessageEEEhh : 72 -> 84
+ __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
~ __ZN3ctu9split_anyENS_4llvm9StringRefES1_ : 452 -> 464
~ __ZN3ctu14split_any_copyENS_4llvm9StringRefES1_ : 584 -> 596
CStrings:
+ "This API cannot be called for raw messages"

```
