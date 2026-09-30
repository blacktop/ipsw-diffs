## SPPlatformReporter

> `/System/Library/SystemProfiler/SPPlatformReporter.spreporter/Contents/MacOS/SPPlatformReporter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-198.0.0.0.0
-  __TEXT.__text: 0x2098
+200.0.0.0.0
+  __TEXT.__text: 0x215c
   __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0x620
+  __TEXT.__objc_stubs: 0x640
   __TEXT.__objc_methlist: 0xd4
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__cstring: 0x884
-  __TEXT.__objc_methname: 0x3c6
+  __TEXT.__cstring: 0x919
+  __TEXT.__objc_methname: 0x3dd
   __TEXT.__objc_classname: 0x13
   __TEXT.__objc_methtype: 0x1b
   __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__const: 0x70
-  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__got: 0x58
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x190
+  __DATA.__objc_selrefs: 0x198
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa

   - /usr/lib/libobjc.A.dylib
   Functions: 24
   Symbols:   60
-  CStrings:  176
+  CStrings:  179
 
Symbols:
+ _snprintf
- _IORegistryEntryGetProperty
Functions:
~ sub_1750 : 488 -> 956
~ sub_29f8 -> sub_2bcc : 920 -> 648
CStrings:
+ "%s errno = %d, falling back to total core count"
+ "Efficiency"
+ "Performance"
+ "Super"
+ "Unrecognized hw.perflevel%u.name='%s', falling back to total core count"
+ "hw.nperflevels"
+ "hw.nperflevels errno = %d, falling back to total core count"
+ "hw.perflevel%u.name"
+ "hw.perflevel%u.physicalcpu"
+ "numberWithUnsignedInt:"
- "Error fetching hw.cpufamily: %i"
- "IODeviceTree:/cpus"
- "e-core-count"
- "hw.cpufamily"
- "hw.cpufamily: 0x%x"
- "m-core-count"
- "p-core-count"
```
