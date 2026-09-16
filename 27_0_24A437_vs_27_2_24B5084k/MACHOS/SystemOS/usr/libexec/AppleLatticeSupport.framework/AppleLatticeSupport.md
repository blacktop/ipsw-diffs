## AppleLatticeSupport

> `/usr/libexec/AppleLatticeSupport.framework/AppleLatticeSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`

```diff

-187.0.1.0.0
-  __TEXT.__text: 0x118c
-  __TEXT.__objc_methlist: 0x98
+197.0.0.502.1
+  __TEXT.__text: 0x11a0
+  __TEXT.__objc_methlist: 0xb0
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x170
   __TEXT.__cstring: 0x29e

   __TEXT.__objc_stubs: 0x100
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x1c9
+  __TEXT.__objc_methname: 0x1ea
   __TEXT.__objc_methtype: 0x102
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x58
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0x110
+  __AUTH_CONST.__objc_const: 0x128
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x168

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 27
-  Symbols:   130
-  CStrings:  69
+  Functions: 28
+  Symbols:   133
+  CStrings:  71
 
Symbols:
+ +[AppleLatticeServiceRef serviceModuleName]
+ GCC_except_table12
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table4
+ __OBJC_$_CLASS_METHODS_AppleLatticeServiceRef
+ __OBJC_$_CLASS_PROP_LIST_AppleLatticeServiceRef
- GCC_except_table0
- GCC_except_table11
- GCC_except_table20
- GCC_except_table23
Functions:
+ +[AppleLatticeServiceRef serviceModuleName]
CStrings:
+ "T@\"NSString\",R"
+ "serviceModuleName"
```
