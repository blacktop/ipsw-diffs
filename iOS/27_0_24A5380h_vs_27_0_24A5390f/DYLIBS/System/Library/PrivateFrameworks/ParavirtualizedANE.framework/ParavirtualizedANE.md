## ParavirtualizedANE

> `/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`

```diff

-382.11.0.0.0
-  __TEXT.__text: 0x1fa8c
+382.12.0.0.0
+  __TEXT.__text: 0x1fb48
   __TEXT.__objc_methlist: 0x7e4
   __TEXT.__const: 0x190
   __TEXT.__cstring: 0xf6e
-  __TEXT.__oslogstring: 0x645e
-  __TEXT.__gcc_except_tab: 0x3b3c
+  __TEXT.__oslogstring: 0x64a6
+  __TEXT.__gcc_except_tab: 0x3b48
   __TEXT.__unwind_info: 0x6f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_const: 0x540
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_got: 0x320
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x48
   __DATA.__bss: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 538
-  Symbols:   853
-  CStrings:  558
+  Functions: 539
+  Symbols:   855
+  CStrings:  559
 
Symbols:
+ _strlcpy
+ _strnlen
Functions:
~ -[_ANEVirtualPlatformClient exchangeBuildVersionInfo:] : 860 -> 944
~ _OUTLINED_FUNCTION_22 : 28 -> 12
~ _OUTLINED_FUNCTION_23 : 12 -> 28
+ -[_ANEVirtualPlatformClient exchangeBuildVersionInfo:].cold.4
CStrings:
+ "%@: buildVersion (%zu bytes) larger than max buffer size %d, truncated\n"
```
