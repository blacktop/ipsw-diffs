## gcore

> `/usr/bin/gcore`

```diff

-1012.80.2.0.0
-  __TEXT.__text: 0xf2f4
+1026.100.5.0.0
+  __TEXT.__text: 0xfa90
   __TEXT.__auth_stubs: 0xa00
   __TEXT.__const: 0x168
-  __TEXT.__cstring: 0x41d6
-  __TEXT.__unwind_info: 0x288
+  __TEXT.__cstring: 0x4442
+  __TEXT.__unwind_info: 0x2a0
   __DATA_CONST.__auth_got: 0x500
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x5c8
-  __DATA.__data: 0x80
+  __DATA_CONST.__const: 0x5d8
+  __DATA.__data: 0x98
   __DATA.__common: 0x18
   __DATA.__bss: 0x20
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libutil.dylib
-  UUID: 25B34EFC-46F6-3379-ACE0-BAF8B6C3A83A
-  Functions: 396
+  UUID: BC0CECE0-470B-3D04-92FE-F09125F34964
+  Functions: 400
   Symbols:   178
-  CStrings:  686
+  CStrings:  699
 
CStrings:
+ "Adding forced regions"
+ "Checking region\n"
+ "Nerging subregions (%llx-%llx + %llx-%llx) -- adjacent pages\n"
+ "Post-macho headers insertion"
+ "Pre-macho headers insertion"
+ "can be removed\n"
+ "comparing name %s with %s\n"
+ "creating shared libraries macho headers section"
+ "data_size == 2 * sizeof(*exc_data)"
+ "have to be protected\n"
+ "illegal flag combination, cannot create a extended skinny coredump"
+ "illegal flag combination, cannot create a skinny extended coredump"
+ "inserting shared library macho header section at address 0x%16.16llx size %llu name %s\n"
+ "invalid address at %llx"
+ "shared library macho header section at address 0x%16.16llx size %llu name %s\n"
+ "skinny"
+ "skipping shared library macho header section at address 0x%16.16llx size %llu name %s\n"
+ "vdskNxgCFSZ:o:c:b:t:f:"
- "data_size == 2 * sizeof(mach_exception_data_t)"
- "new_subregion"
- "vdsxgCFNSZ:o:c:b:tf:"
- "vmaddr < vmaddr + vmsize"
- "vmsize <= INT32_MAX"

```
