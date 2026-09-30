## logd_reporter

> `/usr/libexec/logd_reporter`

```diff

-  __TEXT.__text: 0x41fc
+  __TEXT.__text: 0x4280
   __TEXT.__auth_stubs: 0x3a0
   __TEXT.__objc_stubs: 0xbe0
   __TEXT.__objc_methlist: 0x118
-  __TEXT.__const: 0xb0
+  __TEXT.__const: 0xa8
   __TEXT.__objc_methname: 0xa60
-  __TEXT.__oslogstring: 0x621
+  __TEXT.__oslogstring: 0x66d
   __TEXT.__cstring: 0x4fd
   __TEXT.__objc_classname: 0x1c
   __TEXT.__objc_methtype: 0xd5
-  __TEXT.__unwind_info: 0xe0
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__const: 0x210
   __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x10

   - /usr/lib/libobjc.A.dylib
   Functions: 50
   Symbols:   88
-  CStrings:  310
+  CStrings:  311
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
Functions:
~ sub_100002914 : 6040 -> 6016
~ sub_100004d30 -> sub_100004d18 : 608 -> 764
CStrings:
+ "DiagnosticRequest unavailable; %@ report at %{public}@ not submitted to DP."

```
