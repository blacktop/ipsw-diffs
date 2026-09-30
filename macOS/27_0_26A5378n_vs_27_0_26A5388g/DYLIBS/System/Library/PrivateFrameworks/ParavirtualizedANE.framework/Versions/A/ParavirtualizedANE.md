## ParavirtualizedANE

> `/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/Versions/A/ParavirtualizedANE`

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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`

```diff

-382.11.1.0.0
-  __TEXT.__text: 0x21954
+382.12.0.0.0
+  __TEXT.__text: 0x21a10
   __TEXT.__objc_methlist: 0x7e4
   __TEXT.__const: 0x188
   __TEXT.__cstring: 0xf6e
-  __TEXT.__oslogstring: 0x642d
-  __TEXT.__gcc_except_tab: 0x3bc0
+  __TEXT.__oslogstring: 0x6475
+  __TEXT.__gcc_except_tab: 0x3bcc
   __TEXT.__unwind_info: 0x738
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_const: 0x540
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x48
   __DATA.__bss: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 542
-  Symbols:   846
-  CStrings:  557
+  Functions: 543
+  Symbols:   848
+  CStrings:  558
 
Symbols:
+ _strlcpy
+ _strnlen
Functions:
~ -[_ANEVirtualPlatformClient exchangeBuildVersionInfo:] : 916 -> 996
~ _OUTLINED_FUNCTION_22 : 28 -> 12
~ _OUTLINED_FUNCTION_23 : 12 -> 28
+ -[_ANEVirtualPlatformClient exchangeBuildVersionInfo:].cold.4
CStrings:
+ "%@: buildVersion (%zu bytes) larger than max buffer size %d, truncated\n"
```
