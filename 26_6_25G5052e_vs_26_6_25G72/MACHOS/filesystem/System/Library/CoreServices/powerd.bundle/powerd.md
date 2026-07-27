## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1846.160.2.0.0
-  __TEXT.__text: 0x63dd4
-  __TEXT.__auth_stubs: 0x1cb0
+1846.160.4.0.0
+  __TEXT.__text: 0x63e20
+  __TEXT.__auth_stubs: 0x1cc0
   __TEXT.__objc_stubs: 0x3b00
   __TEXT.__objc_methlist: 0x1a4c
   __TEXT.__const: 0x340
   __TEXT.__gcc_except_tab: 0x3a4
-  __TEXT.__cstring: 0x741a
+  __TEXT.__cstring: 0x742b
   __TEXT.__objc_methname: 0x577c
   __TEXT.__oslogstring: 0x9e77
   __TEXT.__objc_classname: 0x1cc
   __TEXT.__objc_methtype: 0x594
   __TEXT.__dlopen_cstrs: 0x152
   __TEXT.__unwind_info: 0x1218
-  __DATA_CONST.__auth_got: 0xe68
+  __DATA_CONST.__auth_got: 0xe70
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x24e0

   __DATA.__objc_selrefs: 0x1508
   __DATA.__objc_ivar: 0x2a0
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x848
-  __DATA.__bss: 0xd80
+  __DATA.__data: 0x84c
+  __DATA.__bss: 0xd78
   __DATA.__common: 0x11e8
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libspindump.dylib
   - /usr/lib/libsystemstats.dylib
   Functions: 2089
-  Symbols:   575
-  CStrings:  3407
+  Symbols:   576
+  CStrings:  3409
 
Symbols:
+ _strnstr
Functions:
~ sub_100059c00 : 344 -> 420
CStrings:
+ "boot-args"
+ "debug="
```
