## SiriNCService

> `/System/Library/CoreServices/Siri.app/Contents/XPCServices/SiriNCService.xpc/Contents/MacOS/SiriNCService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3600.46.14.0.0
-  __TEXT.__text: 0x11e04
+3600.46.19.14.4
+  __TEXT.__text: 0x11e90
   __TEXT.__auth_stubs: 0x880
   __TEXT.__objc_stubs: 0x3840
   __TEXT.__objc_methlist: 0x154c

   __TEXT.__objc_methname: 0x4659
   __TEXT.__objc_methtype: 0x10a1
   __TEXT.__cstring: 0x18a0
-  __TEXT.__oslogstring: 0x12d8
+  __TEXT.__oslogstring: 0x1388
   __TEXT.__gcc_except_tab: 0x194
   __TEXT.__swift5_typeref: 0x4b
   __TEXT.__constg_swiftt: 0x44

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 473
+  Functions: 474
   Symbols:   293
-  CStrings:  1131
+  CStrings:  1132
 
Functions:
~ sub_10000dce8 : 2420 -> 2480
+ sub_100013984
CStrings:
+ "%s [Invocation] SiriNCActionPrewarm reached handleAction: — it should be filtered out in -[SiriNCService invokeService:...] and never arrive here. Listed for switch exhaustiveness."
```
