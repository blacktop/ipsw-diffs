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

-2322.0.0.501.1
-  __TEXT.__text: 0x1dd2c
+2331.0.0.0.1
+  __TEXT.__text: 0x1ddc8
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_stubs: 0x2620
   __TEXT.__objc_methlist: 0x1320

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 414
+  Functions: 415
   Symbols:   203
   CStrings:  1209
 
Functions:
~ sub_100003ad4 : 232 -> 316
+ sub_100003c10
```
