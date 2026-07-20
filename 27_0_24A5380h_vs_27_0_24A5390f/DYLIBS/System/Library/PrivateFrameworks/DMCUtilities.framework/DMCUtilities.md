## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x364f4
-  __TEXT.__objc_methlist: 0x2fb4
+113.0.2.0.0
+  __TEXT.__text: 0x36554
+  __TEXT.__objc_methlist: 0x2fbc
   __TEXT.__const: 0x1a8
   __TEXT.__gcc_except_tab: 0x5fc
-  __TEXT.__cstring: 0x3aea
+  __TEXT.__cstring: 0x3b06
   __TEXT.__oslogstring: 0x5a2f
   __TEXT.__dlopen_cstrs: 0x165
   __TEXT.__unwind_info: 0xe28

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1310
+  __DATA_CONST.__const: 0x1318
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26a8
+  __DATA_CONST.__objc_selrefs: 0x26b0
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__got: 0x6b8
   __AUTH_CONST.__const: 0xce0
-  __AUTH_CONST.__cfstring: 0x4420
+  __AUTH_CONST.__cfstring: 0x4440
   __AUTH_CONST.__objc_const: 0x4520
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x168

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1432
-  Symbols:   3628
-  CStrings:  1041
+  Functions: 1433
+  Symbols:   3630
+  CStrings:  1042
 
Symbols:
+ +[DMCFeatureOverrides essoDeclarationsWaitTimeoutWithDefaultValue:]
+ _DMCDefaultsKeyESSODeclarationsWaitTimeout
Functions:
+ +[DMCFeatureOverrides essoDeclarationsWaitTimeoutWithDefaultValue:]
~ +[DMCFeatureOverrides _allOverrides] : 600 -> 612
CStrings:
+ "ESSODeclarationsWaitTimeout"
```
