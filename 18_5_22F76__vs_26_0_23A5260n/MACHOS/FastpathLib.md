## FastpathLib

> `/System/Library/Extensions/AppleSPU.kext/PlugIns/FastpathLib.plugin/FastpathLib`

```diff

-1014.120.3.0.0
-  __TEXT.__text: 0x1b6c
+1046.0.1.0.0
+  __TEXT.__text: 0x1bc4
   __TEXT.__auth_stubs: 0x170
   __TEXT.__gcc_except_tab: 0x20
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x83
   __TEXT.__oslogstring: 0x52
-  __TEXT.__unwind_info: 0x128
+  __TEXT.__unwind_info: 0x120
   __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__got: 0x18
   __DATA.__data: 0xb0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: DE0925AE-EB68-305A-A39B-A45A4B217445
+  UUID: 998E957A-932B-3872-B25C-D693331D8C6E
   Functions: 86
   Symbols:   61
   CStrings:  8
Symbols:
+ _CFAllocatorAllocateTyped
- _CFAllocatorAllocate
Functions:
~ __ZN14FastpathDriver5allocEPK13__CFAllocator : 64 -> 80
~ sub_d74 -> sub_d84 : 16 -> 4
~ sub_da4 -> sub_da8 : 160 -> 204
~ _FastpathLibFactory : 164 -> 180
~ sub_1908 -> sub_1948 : 384 -> 408

```
