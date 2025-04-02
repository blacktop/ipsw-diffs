## CIInpainting

> `/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting`

```diff

-1510.100.2.0.0
-  __TEXT.__text: 0xb314
+1510.120.2.0.0
+  __TEXT.__text: 0xb48c
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x15bc
-  __TEXT.__cstring: 0x1925
+  __TEXT.__gcc_except_tab: 0x15e0
+  __TEXT.__cstring: 0x196e
   __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methname: 0x1262
   __TEXT.__objc_methtype: 0x24a
-  __TEXT.__oslogstring: 0x5b6
+  __TEXT.__oslogstring: 0x6c6
   __TEXT.__dlopen_cstrs: 0x91
   __TEXT.__inpbpm: 0x944
   __TEXT.__unwind_info: 0x440
   __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x1f8
-  __DATA_CONST.__cfstring: 0xc60
+  __DATA_CONST.__cfstring: 0xc80
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 171
+  Functions: 174
   Symbols:   163
-  CStrings:  427
+  CStrings:  431
 
CStrings:
+ "%{public}@: CIInpaintFilter inputModel value should be a NSString object when inputVersion is 0."
+ "%{public}@: CIInpaintFilter using v0 inpaint model at path: %{public}@."
+ "%{public}@: could not load the v0 inpaint model specified by the inputModel argument path: %{public}@\n"
+ "espresso.net"
+ "inp_gen_eds2_00_q16"
+ "kernel vec4 CIIP_invertMask (__sample s) { return vec4(1.0-s.rrr,s.a); }"
- "inp_gen_eds2_00_q16.espresso"
- "net"

```
