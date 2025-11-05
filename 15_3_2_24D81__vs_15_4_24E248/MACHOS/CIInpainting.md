## CIInpainting

> `/System/Library/CoreImage/CIInpainting.cifilter/Contents/MacOS/CIInpainting`

```diff

-1510.80.3.0.0
-  __TEXT.__text: 0x1addc
+1510.100.3.0.0
+  __TEXT.__text: 0x1af14
   __TEXT.__auth_stubs: 0x5a0
   __TEXT.__objc_stubs: 0x25a0
   __TEXT.__objc_methlist: 0xcfc
-  __TEXT.__gcc_except_tab: 0x31ac
+  __TEXT.__gcc_except_tab: 0x31d0
   __TEXT.__const: 0x168
-  __TEXT.__cstring: 0x2af3
-  __TEXT.__oslogstring: 0x72c
+  __TEXT.__cstring: 0x2b40
+  __TEXT.__oslogstring: 0x83c
   __TEXT.__objc_classname: 0x189
   __TEXT.__objc_methtype: 0xa02
   __TEXT.__objc_methname: 0x3498

   __DATA_CONST.__auth_got: 0x2e8
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0x2b8
-  __DATA_CONST.__cfstring: 0x15a0
+  __DATA_CONST.__cfstring: 0x15e0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4FA3F6EB-E650-3F8D-9903-23639E408090
-  Functions: 388
+  UUID: 6DA7BABA-24E9-3266-AAD8-B9210D9B1623
+  Functions: 396
   Symbols:   181
-  CStrings:  1032
+  CStrings:  1039
 
CStrings:
+ "%{public}@: CIInpaintFilter inputModel value should be a NSString object when inputVersion is 0."
+ "%{public}@: CIInpaintFilter using v0 inpaint model at path: %{public}@."
+ "%{public}@: could not load the v0 inpaint model specified by the inputModel argument path: %{public}@\n"
+ "espresso.net"
+ "inp_gen_eds2_00_q16"
+ "kernel vec4 CIIP_invertMask (__sample s) { return vec4(1.0-s.rrr,s.a); }"
- "inp_gen_eds2_00_q16.espresso"

```
