## safetycheckd

> `/usr/libexec/safetycheckd`

```diff

-423.0.44.0.0
-  __TEXT.__text: 0x1068
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x600
-  __TEXT.__objc_methlist: 0x1dc
+423.0.53.0.0
+  __TEXT.__text: 0xd50
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_stubs: 0x560
+  __TEXT.__objc_methlist: 0x138
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xaf
-  __TEXT.__objc_classname: 0x2b
-  __TEXT.__objc_methname: 0x4df
-  __TEXT.__objc_methtype: 0xbd
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x130
-  __DATA_CONST.__got: 0x80
+  __TEXT.__cstring: 0x93
+  __TEXT.__objc_classname: 0x1a
+  __TEXT.__objc_methname: 0x42b
+  __TEXT.__objc_methtype: 0x85
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x48
-  __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x8
+  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x370
-  __DATA.__objc_selrefs: 0x1d8
-  __DATA.__objc_ivar: 0x18
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x68
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x230
+  __DATA.__objc_selrefs: 0x188
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x8
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 38
-  Symbols:   60
-  CStrings:  100
+  Functions: 26
+  Symbols:   53
+  CStrings:  78
 
Symbols:
+ _OBJC_CLASS_$_SCPair
- _objc_opt_class
- _objc_opt_isKindOfClass
- _objc_release
- _objc_retain_x19
- _objc_retain_x2
- _objc_retain_x20
- _objc_retain_x21
- _objc_setProperty_nonatomic_copy
CStrings:
- "<%!@(MISSING): %!p(MISSING) first:%!@(MISSING) second:%!@(MISSING)>"
- "@"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "B24@0:8@16"
- "NSCopying"
- "Q16@0:8"
- "SCPair"
- "T@,C,N,V_first"
- "T@,C,N,V_second"
- "_first"
- "_second"
- "copyWithZone:"
- "description"
- "hash"
- "initNonMemoizedWithFirst:second:"
- "isEqual:"
- "isEqualToPair:"
- "second"
- "setFirst:"
- "setSecond:"
- "stringWithFormat:"

```
