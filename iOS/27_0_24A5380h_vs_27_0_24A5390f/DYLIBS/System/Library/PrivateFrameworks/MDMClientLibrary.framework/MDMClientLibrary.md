## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x1e714
+113.0.2.0.0
+  __TEXT.__text: 0x1e77c
   __TEXT.__objc_methlist: 0x1db4
   __TEXT.__const: 0xe1
   __TEXT.__gcc_except_tab: 0x50c

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 685
-  Symbols:   2126
+  Symbols:   2127
   CStrings:  646
 
Symbols:
+ _objc_msgSend$initWithCloudConfigDetails:
+ _objc_msgSend$setAsideDetails
- _objc_msgSend$enrollmentServerURL
Functions:
~ +[MDMConfiguration getManagementStateForMAID] : 228 -> 332
```
