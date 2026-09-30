## STSXPCHelper

> `/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-6.0.15.0.0
-  __TEXT.__text: 0x39934
+6.1.3.0.0
+  __TEXT.__text: 0x39b60
   __TEXT.__auth_stubs: 0xb00
   __TEXT.__delay_helper: 0x114
   __TEXT.__objc_stubs: 0x46c0
   __TEXT.__objc_methlist: 0x28e8
   __TEXT.__const: 0x158
   __TEXT.__objc_methname: 0x62b7
-  __TEXT.__cstring: 0x95b7
+  __TEXT.__cstring: 0x9626
   __TEXT.__objc_classname: 0x7d7
   __TEXT.__objc_methtype: 0x1f01
-  __TEXT.__gcc_except_tab: 0x7c4
+  __TEXT.__gcc_except_tab: 0x7bc
   __TEXT.__oslogstring: 0xb4e
-  __TEXT.__ustring: 0x268
+  __TEXT.__ustring: 0x34c
   __TEXT.__unwind_info: 0xd40
   __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__cfstring: 0x5d00
+  __DATA_CONST.__cfstring: 0x5d60
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc0

   - /usr/lib/libobjc.A.dylib
   Functions: 962
   Symbols:   292
-  CStrings:  2533
+  CStrings:  2536
 
Functions:
~ sub_100017b20 : 1116 -> 1572
~ sub_10001e890 -> sub_10001ea58 : 884 -> 876
~ sub_1000345c4 -> sub_100034784 : 848 -> 924
~ sub_100034914 -> sub_100034b20 : 760 -> 784
~ sub_100034c1c -> sub_100034e40 : 204 -> 212
CStrings:
+ "LE: writeData %s (completion observed at stall check)"
+ "LE: writeData hit %.0fs backstop while still draining; pendingBytes=%lu — failing write"
+ "LE: writeData progressing, remaining=%lu (elapsed %.1fs)"
+ "LE: writeData stalled — no progress for %.1fs (elapsed %.1fs); pendingBytes=%lu — failing write"
- "LE: writeData timed out after %.1fs; pendingBytes=%lu — failing write"
```
