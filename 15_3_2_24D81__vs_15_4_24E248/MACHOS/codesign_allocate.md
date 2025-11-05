## codesign_allocate

> `/usr/libexec/DeveloperTools/codesign_allocate`

```diff

-1022.1.0.0.0
-  __TEXT.__text: 0x111f8
+1024.3.0.0.0
+  __TEXT.__text: 0x11154
   __TEXT.__stubs: 0x2c4
   __TEXT.__stub_helper: 0x2dc
-  __TEXT.__const: 0x78c
-  __TEXT.__cstring: 0xaa63
+  __TEXT.__const: 0x680
+  __TEXT.__cstring: 0xac58
   __TEXT.__unwind_info: 0x170
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x18

   __DATA.__common: 0x24
   __DATA.__bss: 0xa4
   - /usr/lib/libSystem.B.dylib
-  UUID: B041F44D-1095-339A-8CE2-DC69C985CE04
-  Functions: 138
-  Symbols:   258
-  CStrings:  672
+  UUID: 86A1D12B-C6A1-35D1-A2FB-9AF7624D5B79
+  Functions: 137
+  Symbols:   257
+  CStrings:  676
 
Symbols:
- _get_arch_name_if_known
CStrings:
+ "LC_FUNCTION_VARIANTS"
+ "LC_FUNCTION_VARIANT_FIXUPS"
+ "function variant fixups"
+ "function variants"
+ "function variants out of place"
+ "malformed file (more than one LC_FUNCTION_VARIANTS load command): "
+ "malformed file (more than one LC_FUNCTION_VARIANT_FIXUPS load command): "
+ "malformed object (LC_TARGET_TRIPLE command %u has too small cmdsize field)"
+ "malformed object (LC_TARGET_TRIPLE: cmdsize too small) in command %u"
+ "truncated or malformed object (path.offset field of LC_TARGET_TRIPLE command %u extends past the end of the file)"
- "-A"
- "-a"
- "-i"
- "-o"
- "-p"
- "-r"

```
