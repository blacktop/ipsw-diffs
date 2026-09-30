## logd_reporter

> `/usr/libexec/logd_reporter`

```diff

-  __TEXT.__text: 0x3e4c
+  __TEXT.__text: 0x3eb8
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0xc00
   __TEXT.__objc_methlist: 0x118
-  __TEXT.__const: 0xb0
+  __TEXT.__const: 0xa8
   __TEXT.__objc_methname: 0xa82
-  __TEXT.__oslogstring: 0x633
+  __TEXT.__oslogstring: 0x67f
   __TEXT.__cstring: 0x50e
   __TEXT.__objc_classname: 0x1c
   __TEXT.__objc_methtype: 0xd5

   - /usr/lib/libobjc.A.dylib
   Functions: 48
   Symbols:   113
-  CStrings:  314
+  CStrings:  315
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
Functions:
~ sub_10000275c : 5560 -> 5564
~ sub_10000485c -> sub_100004860 : 852 -> 956
CStrings:
+ "DiagnosticRequest unavailable; %@ report at %{public}@ not submitted to DP."

```
