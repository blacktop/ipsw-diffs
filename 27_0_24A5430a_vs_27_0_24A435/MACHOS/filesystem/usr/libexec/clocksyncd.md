## clocksyncd

> `/usr/libexec/clocksyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1501.6.0.0.0
-  __TEXT.__text: 0x3b364
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_stubs: 0x5a00
+  __TEXT.__text: 0x3b498
+  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__objc_stubs: 0x5a40
   __TEXT.__objc_methlist: 0x36b4
   __TEXT.__const: 0x129
-  __TEXT.__cstring: 0x2835
-  __TEXT.__oslogstring: 0x592c
-  __TEXT.__gcc_except_tab: 0x1aa8
-  __TEXT.__objc_methname: 0x919d
+  __TEXT.__cstring: 0x2866
+  __TEXT.__oslogstring: 0x5945
+  __TEXT.__gcc_except_tab: 0x1ab4
+  __TEXT.__objc_methname: 0x91d0
   __TEXT.__objc_classname: 0x508
   __TEXT.__objc_methtype: 0x197a
   __TEXT.__unwind_info: 0xe80
-  __DATA_CONST.__const: 0x948
-  __DATA_CONST.__cfstring: 0x1f00
+  __DATA_CONST.__const: 0x968
+  __DATA_CONST.__cfstring: 0x1f60
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x6b0
-  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__auth_got: 0x6b8
+  __DATA_CONST.__got: 0x288
   __DATA_CONST.__auth_ptr: 0x110
   __DATA.__objc_const: 0x6a28
-  __DATA.__objc_selrefs: 0x1da0
+  __DATA.__objc_selrefs: 0x1db0
   __DATA.__objc_ivar: 0x514
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x5a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1532
-  Symbols:   281
-  CStrings:  2459
+  Functions: 1534
+  Symbols:   284
+  CStrings:  2466
 
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_TSMSGService
+ __os_feature_enabled_impl
CStrings:
+ "Genlock"
+ "Localizable"
+ "Localized clockName: %@\n"
+ "bundleForClass:"
+ "fall_2026"
+ "genlock-clock-name"
+ "localizedStringForKey:value:table:"
```
