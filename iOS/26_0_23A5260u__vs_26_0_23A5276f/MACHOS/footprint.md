## footprint

> `/usr/bin/footprint`

```diff

-301.0.0.0.0
-  __TEXT.__text: 0x1ac8c
+305.0.0.0.1
+  __TEXT.__text: 0x1ad64
   __TEXT.__auth_stubs: 0xc50
   __TEXT.__objc_stubs: 0x22a0
   __TEXT.__objc_methlist: 0x115c
-  __TEXT.__cstring: 0x330a
+  __TEXT.__cstring: 0x3365
   __TEXT.__objc_classname: 0x206
   __TEXT.__objc_methtype: 0x7ab
   __TEXT.__const: 0xe8

   __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x1768
-  __DATA_CONST.__cfstring: 0x2200
+  __DATA_CONST.__cfstring: 0x2220
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: BCA25BFC-DD48-3090-98DA-090AB5578B80
+  UUID: 1D5B4625-CAC7-35AE-A448-2B59256906EF
   Functions: 410
   Symbols:   276
-  CStrings:  1430
+  CStrings:  1434
 
Functions:
~ sub_100009ec8 : 692 -> 684
~ sub_10000b4f4 -> sub_10000b4ec : 3504 -> 3584
~ sub_100018284 -> sub_1000182cc : 388 -> 476
~ sub_100018408 -> sub_1000184a8 : 760 -> 816
CStrings:
+ "           start                end %*s     VRT     DRT%*s     CLN     RCL%*s   tag (detail)\n"
+ "        unmapped -         unmapped [%0*llx]"
+ "      ----------         ---------- %*s   -----   -----%*s   -----   -----%*s   ------------\n"
+ "%16llx - %16llx [%0*llx]"
+ "------------"
+ "--ioaccel is not compatible with memgraphs (%@) because they do not contain the required information."
+ "DFR"
+ "[object-id]"
- "           start                end  [object-id]     VRT     DRT%*s     CLN     RCL%*s   tag (detail)\n"
- "        unmapped -         unmapped [%010llx]"
- "      ----------         ---------- ------------   -----   -----%*s   -----   -----%*s   ------------\n"
- "%16llx - %16llx [%010llx]"
- "VM_KERN_MEMORY_MTAG"

```
