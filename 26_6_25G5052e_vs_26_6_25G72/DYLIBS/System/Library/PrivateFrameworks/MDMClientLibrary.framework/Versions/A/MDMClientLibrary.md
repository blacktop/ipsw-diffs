## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/Versions/A/MDMClientLibrary`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-59.160.5.0.0
-  __TEXT.__text: 0x1ee40
+59.160.6.0.0
+  __TEXT.__text: 0x1eecc
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_methlist: 0x1c1c
   __TEXT.__const: 0xb9

   __TEXT.__objc_classname: 0x336
   __TEXT.__objc_methname: 0x4fe7
   __TEXT.__objc_methtype: 0xaad
-  __TEXT.__objc_stubs: 0x3460
+  __TEXT.__objc_stubs: 0x34a0
   __DATA_CONST.__got: 0x410
   __DATA_CONST.__const: 0xa70
   __DATA_CONST.__objc_classlist: 0xc8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 658
-  Symbols:   2010
+  Symbols:   2012
   CStrings:  1473
 
Symbols:
+ _objc_msgSend$initWithCloudConfigDetails:
+ _objc_msgSend$setAsideDetails
Functions:
~ +[MDMConfiguration getManagementStateForMAID] : 292 -> 432
```
