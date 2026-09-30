## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1072.0.0.0.0
-  __TEXT.__text: 0x48764
-  __TEXT.__objc_methlist: 0x5c88
+1078.0.0.0.0
+  __TEXT.__text: 0x4887c
+  __TEXT.__objc_methlist: 0x5c98
   __TEXT.__const: 0x170
   __TEXT.__cstring: 0x4abd
   __TEXT.__oslogstring: 0x29d9

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6e0
+  __DATA_CONST.__const: 0x6e8
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e28
+  __DATA_CONST.__objc_selrefs: 0x1e30
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_arraydata: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2411
-  Symbols:   4776
+  Functions: 2412
+  Symbols:   4778
   CStrings:  1113
 
Symbols:
+ +[RBSExtensionProcessIdentity _extensionIdentityFromDataRepresentation:correctedToInstanceUUID:]
+ _objc_msgSend$_extensionIdentityFromDataRepresentation:correctedToInstanceUUID:
Functions:
~ -[RBSExtensionProcessIdentity _copyWithCorrectedInstanceUUID:] : 400 -> 212
+ +[RBSExtensionProcessIdentity _extensionIdentityFromDataRepresentation:correctedToInstanceUUID:]
~ -[RBSExtensionProcessIdentity initWithDecodeFromJob:uuid:] : 536 -> 708
```
