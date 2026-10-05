## nfcd

> `/usr/libexec/nfcd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-371.7.0.0.0
-  __TEXT.__text: 0x1eb3e0
+371.8.0.0.0
+  __TEXT.__text: 0x1eb448
   __TEXT.__auth_stubs: 0x1920
   __TEXT.__delay_stubs: 0x540
   __TEXT.__delay_helper: 0x1878
   __TEXT.__objc_stubs: 0xe3e0
-  __TEXT.__objc_methlist: 0x9fcc
+  __TEXT.__objc_methlist: 0x9fc4
   __TEXT.__const: 0x143c
-  __TEXT.__cstring: 0x23254
-  __TEXT.__oslogstring: 0x20d8b
+  __TEXT.__cstring: 0x2325c
+  __TEXT.__oslogstring: 0x20d64
   __TEXT.__objc_classname: 0x1d7c
-  __TEXT.__objc_methname: 0x1600c
-  __TEXT.__objc_methtype: 0x4e7a
-  __TEXT.__unwind_info: 0x3a78
-  __DATA_CONST.__const: 0x9ae0
-  __DATA_CONST.__cfstring: 0x11920
+  __TEXT.__objc_methname: 0x1600b
+  __TEXT.__objc_methtype: 0x4e6c
+  __TEXT.__unwind_info: 0x3a80
+  __DATA_CONST.__const: 0x9b48
+  __DATA_CONST.__cfstring: 0x11900
   __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x390

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4350
+  Functions: 4351
   Symbols:   686
-  CStrings:  11591
+  CStrings:  11589
 
CStrings:
+ "%@/Library/Logs/nfcd_lpcd_false-detect-v2.plist"
+ "NFCD built from (B&I) Stockholm_Base-371.8"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "removeItemAtPath:error:"
+ "sortUsingComparator:"
+ "v32@?0@8Q16^B24"
- "%{public}s:%i Invoking TTR for %d 0x%x"
- "-[_NFSeshatSession maybeTTR:appletResult:]"
- "NFCD built from (B&I) Stockholm_Base-371.7"
- "Result: %d Applet Result: %d"
- "Seshat Failure!"
- "descriptionWithLocale:"
- "maybeTTR:appletResult:"
- "v24@0:8I16S20"
```
