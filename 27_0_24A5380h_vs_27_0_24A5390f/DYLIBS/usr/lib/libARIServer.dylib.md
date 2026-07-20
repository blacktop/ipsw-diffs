## libARIServer.dylib

> `/usr/lib/libARIServer.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-1636.0.0.0.0
-  __TEXT.__text: 0x28b20
+1638.0.0.0.0
+  __TEXT.__text: 0x28b30
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x3a00
   __TEXT.__gcc_except_tab: 0x2288
-  __TEXT.__cstring: 0x3617
+  __TEXT.__cstring: 0x363f
   __TEXT.__oslogstring: 0x2234
   __TEXT.__unwind_info: 0xc50
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libc++.1.dylib
   Functions: 602
   Symbols:   1116
-  CStrings:  529
+  CStrings:  530
 
Functions:
~ __ZN3Ari22AriXpcServerConnectionC2EP17_xpc_connection_sNSt3__18functionIFvNS3_10shared_ptrIS0_EEEEE : 208 -> 224
CStrings:
+ "AriHostRtIPC connection queue (multiple instances)"
+ "AriHostRtIPC listen queue"
- "ConnectionQueue (multiple instances)"
```
