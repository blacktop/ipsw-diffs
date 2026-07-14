## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__common`

```diff

-  __TEXT.__text: 0x6e2cc
+  __TEXT.__text: 0x6e568
   __TEXT.__auth_stubs: 0x1b50
-  __TEXT.__objc_stubs: 0x4ea0
-  __TEXT.__objc_methlist: 0x28e4
-  __TEXT.__const: 0x4b0
+  __TEXT.__objc_stubs: 0x4ec0
+  __TEXT.__objc_methlist: 0x28fc
+  __TEXT.__const: 0x510
   __TEXT.__cstring: 0x6869
-  __TEXT.__objc_methname: 0x6c6d
+  __TEXT.__objc_methname: 0x6ca1
   __TEXT.__oslogstring: 0xc188
   __TEXT.__objc_classname: 0x328
-  __TEXT.__objc_methtype: 0x871
+  __TEXT.__objc_methtype: 0x883
   __TEXT.__gcc_except_tab: 0x4e0
   __TEXT.__dlopen_cstrs: 0x300
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x15b0
+  __TEXT.__unwind_info: 0x15c8
   __DATA_CONST.__auth_got: 0xdb8
-  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__got: 0x370
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x25b0
+  __DATA_CONST.__const: 0x25d0
   __DATA_CONST.__cfstring: 0x71c0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arraydata: 0x248
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x300
-  __DATA.__objc_const: 0x4a10
-  __DATA.__objc_selrefs: 0x1a38
+  __DATA.__objc_const: 0x4a18
+  __DATA.__objc_selrefs: 0x1a48
   __DATA.__objc_ivar: 0x3bc
   __DATA.__objc_data: 0x690
   __DATA.__data: 0xa34
   __DATA.__common: 0x11e8
-  __DATA.__bss: 0xc00
+  __DATA.__bss: 0xc10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2383
-  Symbols:   560
-  CStrings:  3760
+  Functions: 2388
+  Symbols:   561
+  CStrings:  3763
 
Symbols:
+ _OBJC_CLASS_$_NSSet
CStrings:
+ "getPowerModeUserInitiatedWithReply:"
+ "setWithObjects:"
+ "v24@0:8@?<v@?B>16"
```
