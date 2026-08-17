## libQMIParserDynamic.dylib

> `/usr/lib/libQMIParserDynamic.dylib`

```diff

 1585.0.0.0.0
-  __TEXT.__text: 0x16fe8
+  __TEXT.__text: 0x16dec
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x87c
-  __TEXT.__cstring: 0x24b0
-  __TEXT.__gcc_except_tab: 0x19cc
-  __TEXT.__unwind_info: 0x898
+  __TEXT.__cstring: 0x2485
+  __TEXT.__gcc_except_tab: 0x1990
+  __TEXT.__unwind_info: 0x878
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x80
   __DATA_CONST.__weak_got: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 450
-  Symbols:   764
-  CStrings:  391
+  Functions: 449
+  Symbols:   761
+  CStrings:  390
 
Symbols:
+ __ZNSt3__110shared_ptrIN3qmi17SerializedMessageEED2B9noe220106Ev
- __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
- __ZNSt13runtime_errorC1EPKc
- __ZNSt13runtime_errorD1Ev
- __ZNSt3__110shared_ptrIN3qmi17SerializedMessageEED1B9noe220106Ev
Functions:
~ __ZN3qmi18stripRequestHeaderEhRKNSt3__110shared_ptrIKNS_17SerializedMessageEEE : 152 -> 44
~ __ZN3qmi11fixupHeaderERKNSt3__110shared_ptrINS_17SerializedMessageEEEhh : 84 -> 72
- __ZN3qmi16createRawRequestEhNS_11buffer_viewEm
CStrings:
- "This API cannot be called for raw messages"
```
