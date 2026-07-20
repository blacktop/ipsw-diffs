## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

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
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1072.0.0.0.0
-  __TEXT.__text: 0x41b00
-  __TEXT.__objc_methlist: 0x5b98
+1078.0.0.0.0
+  __TEXT.__text: 0x41bf4
+  __TEXT.__objc_methlist: 0x5ba8
   __TEXT.__const: 0x140
   __TEXT.__cstring: 0x4853
   __TEXT.__oslogstring: 0x27cb

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xcb8
+  __DATA_CONST.__const: 0xcc0
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d60
+  __DATA_CONST.__objc_selrefs: 0x1d68
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__got: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2328
-  Symbols:   4608
+  Functions: 2329
+  Symbols:   4610
   CStrings:  1063
 
Symbols:
+ +[RBSExtensionProcessIdentity _extensionIdentityFromDataRepresentation:correctedToInstanceUUID:]
+ _objc_msgSend$_extensionIdentityFromDataRepresentation:correctedToInstanceUUID:
Functions:
~ -[RBSExtensionProcessIdentity _copyWithCorrectedInstanceUUID:] : 372 -> 196
+ +[RBSExtensionProcessIdentity _extensionIdentityFromDataRepresentation:correctedToInstanceUUID:]
~ -[RBSExtensionProcessIdentity initWithDecodeFromJob:uuid:] : 456 -> 600
```
