## libcryptex_interface.dylib

> `/usr/lib/libcryptex_interface.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-761.0.15.0.0
-  __TEXT.__text: 0x752c
+761.0.17.502.1
+  __TEXT.__text: 0x7574
   __TEXT.__objc_methlist: 0x110
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0xc7e
+  __TEXT.__const: 0x158
+  __TEXT.__cstring: 0xc8e
   __TEXT.__oslogstring: 0x934
   __TEXT.__gcc_except_tab: 0x2bc
   __TEXT.__unwind_info: 0x280

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 179
-  Symbols:   408
+  Symbols:   409
   CStrings:  177
 
Symbols:
+ _xpc_dictionary_get_uint64
Functions:
~ _remote_service_install_request_valid : 476 -> 548
CStrings:
+ "761.0.17.502.1"
+ "@(#)VERSION:Cryptex IPC Interface Version 2.0.0: Tue Aug  4 23:52:58 PDT 2026; root:libcryptex-761.0.17.502.1~2/libcryptex_interface/RELEASE_ARM64E"
+ "Cryptex IPC Interface Version 2.0.0: Tue Aug  4 23:52:58 PDT 2026; root:libcryptex-761.0.17.502.1~2/libcryptex_interface/RELEASE_ARM64E"
- "761.0.15"
- "@(#)VERSION:Cryptex IPC Interface Version 2.0.0: Fri Jul 10 21:51:26 PDT 2026; root:libcryptex-761.0.15~13/libcryptex_interface/RELEASE_ARM64E"
- "Cryptex IPC Interface Version 2.0.0: Fri Jul 10 21:51:26 PDT 2026; root:libcryptex-761.0.15~13/libcryptex_interface/RELEASE_ARM64E"
```
