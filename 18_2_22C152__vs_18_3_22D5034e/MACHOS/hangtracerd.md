## hangtracerd

> `/usr/libexec/hangtracerd`

```diff

-331.1.0.0.0
-  __TEXT.__text: 0x3025c
+331.3.0.0.0
+  __TEXT.__text: 0x304c4
   __TEXT.__auth_stubs: 0xe90
   __TEXT.__objc_stubs: 0x52c0
   __TEXT.__objc_methlist: 0x1d44

   __TEXT.__objc_methname: 0x8476
   __TEXT.__objc_methtype: 0x108c
   __TEXT.__gcc_except_tab: 0x644
-  __TEXT.__oslogstring: 0x562f
+  __TEXT.__oslogstring: 0x568c
   __TEXT.__unwind_info: 0x8b8
   __DATA_CONST.__auth_got: 0x758
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2050
+  __DATA_CONST.__const: 0x2070
   __DATA_CONST.__cfstring: 0x66c0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x58

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 955
+  Functions: 957
   Symbols:   372
-  CStrings:  2857
+  CStrings:  2859
 
CStrings:
+ "Current display state: %d, time: %llu"
+ "Display state changed %d -> %d,  time: %llu"
+ "Error listening to display state changes. Error code: %u"
- "Display state changed %d -> %llu,  time: %llu"

```
