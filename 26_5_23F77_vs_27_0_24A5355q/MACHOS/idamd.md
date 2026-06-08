## idamd

> `/usr/libexec/idamd`

```diff

 24.0.0.0.0
-  __TEXT.__text: 0xabc
-  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__text: 0xa04
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x169
+  __TEXT.__cstring: 0x168
   __TEXT.__oslogstring: 0x2c3
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0xf0
-  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__auth_got: 0xe8
+  __DATA_CONST.__got: 0x30
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblockdown.dylib
-  UUID: E1A81E1A-6811-32DC-8593-2CA3E8398997
+  UUID: 38EB8CFF-0D7D-325A-BB54-7F3F41E812E2
   Functions: 7
-  Symbols:   41
+  Symbols:   39
   CStrings:  44
 
Symbols:
- ___stack_chk_fail
- ___stack_chk_guard
Functions:
~ sub_100000888 : 948 -> 904
~ sub_100000c3c -> sub_100000c10 : 260 -> 216
~ sub_100000d40 -> sub_100000ce8 : 236 -> 192
~ sub_100000e2c -> sub_100000da8 : 1080 -> 1028
CStrings:
+ "MonarchLowEndHardware"
- "s+gaKNe68Gs3PfqKrZhi1w"

```
