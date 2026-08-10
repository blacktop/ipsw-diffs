## DeviceManagement

> `/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-260.0.0.0.0
-  __TEXT.__text: 0x39260
-  __TEXT.__objc_methlist: 0x75c4
+261.2.5.0.0
+  __TEXT.__text: 0x39b14
+  __TEXT.__objc_methlist: 0x75ec
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x511d
   __TEXT.__oslogstring: 0xeac
   __TEXT.__ustring: 0xb64
   __TEXT.__gcc_except_tab: 0x27c
-  __TEXT.__unwind_info: 0xfa0
+  __TEXT.__unwind_info: 0xfa8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1dc8
+  __DATA_CONST.__objc_selrefs: 0x1e08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x6b8
-  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__got: 0x378
   __AUTH_CONST.__const: 0x4a0
   __AUTH_CONST.__cfstring: 0x7440
   __AUTH_CONST.__objc_const: 0x106c8

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2395
-  Symbols:   5514
+  Functions: 2398
+  Symbols:   5523
   CStrings:  1028
 
Symbols:
+ -[DMFEffectivePolicy excludesIdentifier:]
+ -[DMFEffectivePolicy policyByAddingExcludedIdentifiers:]
+ -[DMFEffectivePolicy policyByRemovingIdentifiers:minimumPriority:]
+ GCC_except_table20
+ ___kCFBooleanTrue
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$unionSet:
- GCC_except_table17
```
