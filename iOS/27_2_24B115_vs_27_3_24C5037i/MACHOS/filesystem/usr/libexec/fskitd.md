## fskitd

> `/usr/libexec/fskitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-974.40.12.0.0
-  __TEXT.__text: 0x4ca8c
+974.60.5.0.0
+  __TEXT.__text: 0x4cb5c
   __TEXT.__auth_stubs: 0xb50
   __TEXT.__objc_stubs: 0x5380
   __TEXT.__objc_methlist: 0x233c

   __TEXT.__cstring: 0x39e2
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methname: 0x6a18
-  __TEXT.__objc_methtype: 0x27ff
-  __TEXT.__unwind_info: 0x1878
-  __DATA_CONST.__const: 0x26b0
+  __TEXT.__objc_methtype: 0x2800
+  __TEXT.__unwind_info: 0x1880
+  __DATA_CONST.__const: 0x26d0
   __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x58

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1496
+  Functions: 1497
   Symbols:   304
   CStrings:  2127
 
CStrings:
+ "v56@0:8@\"NSString\"16@\"NSData\"24@\"FSAuditToken\"32Q40@?<v@?i@\"NSData\"Q@\"NSData\">48"
- "v56@0:8@\"NSString\"16@\"NSData\"24@\"FSAuditToken\"32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
```
