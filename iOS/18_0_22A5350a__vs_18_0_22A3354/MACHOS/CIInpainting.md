## CIInpainting

> `/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting`

```diff

 1500.92.0.0.0
-  __TEXT.__text: 0xc874
+  __TEXT.__text: 0xd134
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x1380
+  __TEXT.__objc_stubs: 0x13e0
   __TEXT.__objc_methlist: 0x440
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x18f4
-  __TEXT.__cstring: 0x17e5
+  __TEXT.__gcc_except_tab: 0x1a48
+  __TEXT.__cstring: 0x1821
   __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0x135c
+  __TEXT.__objc_methname: 0x13b5
   __TEXT.__objc_methtype: 0x2cb
-  __TEXT.__oslogstring: 0x366
+  __TEXT.__oslogstring: 0x53b
   __TEXT.__dlopen_cstrs: 0x91
   __TEXT.__inpbpm: 0x944
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x440
   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0x270
-  __DATA_CONST.__cfstring: 0xcc0
+  __DATA_CONST.__cfstring: 0xd60
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x678
-  __DATA.__objc_selrefs: 0x630
+  __DATA.__objc_selrefs: 0x648
   __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0x140
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0x100
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 160
+  Functions: 167
   Symbols:   164
-  CStrings:  445
+  CStrings:  457
 
CStrings:
+ "%!{(MISSING)public}@: The inpaint.mlmodelc is no longer part of the filter bundle. It needs to be passed to the filter using the inputModel argument.\n"
+ "%!{(MISSING)public}@: could not load the default inpaint model.\n"
+ "inpaintModelPath"
+ "deep_transfer"
+ "fileURLWithPath:isDirectory:"
+ "mlmodelc"
+ "refinementModelPath"
+ "URLForResource:withExtension:"
+ "%!{(MISSING)public}@: using model \"%!{(MISSING)public}@\" at path: %!{(MISSING)public}@."
+ "%!{(MISSING)public}@: The deep_transfer.mlmodelc is no longer part of the filter bundle. It needs to be passed to the filter using the inputRefinementModel argument.\n"
+ "%!{(MISSING)public}@: could not load the default refinement model.\n"
+ "modelWithContentsOfURL:error:"

```
