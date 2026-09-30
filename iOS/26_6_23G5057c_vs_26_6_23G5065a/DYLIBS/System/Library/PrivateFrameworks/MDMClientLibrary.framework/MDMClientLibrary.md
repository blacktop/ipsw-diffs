## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

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

-  __TEXT.__text: 0x20c7c
+  __TEXT.__text: 0x20d00
   __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_methlist: 0x1da4
   __TEXT.__const: 0xd1

   __TEXT.__objc_classname: 0x336
   __TEXT.__objc_methname: 0x5585
   __TEXT.__objc_methtype: 0xbd1
-  __TEXT.__objc_stubs: 0x3960
+  __TEXT.__objc_stubs: 0x39a0
   __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__const: 0x11c0
   __DATA_CONST.__objc_classlist: 0xc8

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 683
-  Symbols:   2117
+  Symbols:   2119
   CStrings:  1565
 
Symbols:
+ _objc_msgSend$initWithCloudConfigDetails:
+ _objc_msgSend$setAsideDetails
Functions:
~ +[MDMConfiguration getManagementStateForMAID] : 284 -> 416
```
