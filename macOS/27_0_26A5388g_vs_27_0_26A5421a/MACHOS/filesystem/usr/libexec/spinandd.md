## spinandd

> `/usr/libexec/spinandd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 142.0.0.0.0
-  __TEXT.__text: 0x10dc4
+  __TEXT.__text: 0x10db0
   __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_stubs: 0xe20
   __TEXT.__objc_methlist: 0x42c
   __TEXT.__const: 0x5e0
   __TEXT.__objc_methname: 0xcb6
-  __TEXT.__cstring: 0x40c2
+  __TEXT.__cstring: 0x40c3
   __TEXT.__objc_classname: 0x59
   __TEXT.__objc_methtype: 0x3b3
   __TEXT.__oslogstring: 0xcbe

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 446
+  Functions: 445
   Symbols:   126
   CStrings:  740
 
Functions:
~ sub_10000c4a0 : 5128 -> 5116
- sub_100010c10
+ sub_100010e88
~ sub_100010ed0 : 20 -> 12
- sub_100010ef0
CStrings:
+ "142~2170"
- "142~377"
```
