## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/Versions/A/MDMClientLibrary`

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
- `__DATA.__data`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x1cb20
+113.0.2.0.0
+  __TEXT.__text: 0x1cb98
   __TEXT.__objc_methlist: 0x1c2c
   __TEXT.__const: 0xc1
   __TEXT.__gcc_except_tab: 0x4c4

   __AUTH_CONST.__objc_const: 0x39c0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x618
+  __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x124
   __DATA.__data: 0x540
   __DATA.__bss: 0x120
-  __DATA_DIRTY.__objc_data: 0x1b8
+  __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 660
-  Symbols:   2013
+  Symbols:   2014
   CStrings:  597
 
Symbols:
+ _objc_msgSend$initWithCloudConfigDetails:
+ _objc_msgSend$setAsideDetails
- _objc_msgSend$enrollmentServerURL
Functions:
~ +[MDMConfiguration getManagementStateForMAID] : 236 -> 356
```
