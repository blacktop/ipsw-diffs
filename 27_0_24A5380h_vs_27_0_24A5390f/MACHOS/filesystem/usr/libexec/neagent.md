## neagent

> `/usr/libexec/neagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2322.0.0.0.1
-  __TEXT.__text: 0x1adb0
+2331.0.0.0.1
+  __TEXT.__text: 0x1ae4c
   __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_stubs: 0x25a0
   __TEXT.__objc_methlist: 0x1210

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 361
+  Functions: 362
   Symbols:   218
   CStrings:  1174
 
Functions:
~ sub_100003864 : 220 -> 304
+ sub_100003994
```
