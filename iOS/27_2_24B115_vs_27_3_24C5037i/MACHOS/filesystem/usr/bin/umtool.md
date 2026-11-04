## umtool

> `/usr/bin/umtool`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-490.0.3.0.0
-  __TEXT.__text: 0x152b4
+490.60.1.0.0
+  __TEXT.__text: 0x152d8
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x1180
+  __TEXT.__objc_stubs: 0x11a0
   __TEXT.__objc_methlist: 0x368
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x29d8
+  __TEXT.__cstring: 0x29f8
   __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methname: 0xbaf
+  __TEXT.__objc_methname: 0xbb7
   __TEXT.__objc_methtype: 0xb3
   __TEXT.__gcc_except_tab: 0x15c
   __TEXT.__oslogstring: 0x190
   __TEXT.__unwind_info: 0x588
   __DATA_CONST.__const: 0xf8
-  __DATA_CONST.__cfstring: 0x14c0
+  __DATA_CONST.__cfstring: 0x14e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x438
-  __DATA.__objc_selrefs: 0x520
+  __DATA.__objc_selrefs: 0x528
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x6a
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   Functions: 498
   Symbols:   115
-  CStrings:  578
+  CStrings:  580
 
Functions:
~ sub_1000049ec : 1064 -> 1100
CStrings:
+ "Is Dirty                   : %@"
+ "isDirty"
```
