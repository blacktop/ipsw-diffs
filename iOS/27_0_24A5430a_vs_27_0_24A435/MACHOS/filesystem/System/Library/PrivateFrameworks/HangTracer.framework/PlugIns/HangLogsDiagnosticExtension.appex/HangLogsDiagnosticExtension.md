## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 426.0.0.0.0
-  __TEXT.__text: 0x14a70
-  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__text: 0x14a88
+  __TEXT.__auth_stubs: 0xac0
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_stubs: 0x1d20
   __TEXT.__objc_methlist: 0xd2c
-  __TEXT.__const: 0x280
+  __TEXT.__const: 0x2b0
   __TEXT.__cstring: 0x281c
   __TEXT.__oslogstring: 0x2145
   __TEXT.__gcc_except_tab: 0x1cc

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x568
+  __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0x1d0
   __DATA.__objc_const: 0x21c8
   __DATA.__objc_selrefs: 0xcc0

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 484
-  Symbols:   503
+  Symbols:   504
   CStrings:  1284
 
Symbols:
+ _objc_retain_x27
Functions:
~ _checkForAssertionOverlap : 1396 -> 1392
~ sub_100006b2c -> sub_100006b28 : 7656 -> 7684
~ sub_10000b9f8 -> sub_10000ba10 : 16 -> 12
~ sub_10000ba08 -> sub_10000ba1c : 12 -> 36
~ sub_10000ba14 -> sub_10000ba40 : 36 -> 16
```
