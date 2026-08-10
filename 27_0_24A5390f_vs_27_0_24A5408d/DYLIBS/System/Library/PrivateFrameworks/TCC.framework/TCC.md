## TCC

> `/System/Library/PrivateFrameworks/TCC.framework/TCC`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-910.0.0.0.0
-  __TEXT.__text: 0x15c28
+913.0.0.0.0
+  __TEXT.__text: 0x15c74
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__cstring: 0x3383
+  __TEXT.__cstring: 0x3389
   __TEXT.__oslogstring: 0x1665
   __TEXT.__const: 0x398
   __TEXT.__unwind_info: 0x618

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x2d8
-  __AUTH_CONST.__cfstring: 0x1700
+  __AUTH_CONST.__cfstring: 0x1720
   __AUTH_CONST.__objc_const: 0xf58
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190

   - /usr/lib/libobjc.A.dylib
   Functions: 598
   Symbols:   962
-  CStrings:  610
+  CStrings:  611
 
Functions:
~ ___TCCManagedOverridesCopyInformation_block_invoke.531 : 712 -> 788
CStrings:
+ "csreq"
```
