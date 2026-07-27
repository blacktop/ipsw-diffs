## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1015.100.16.0.0
-  __TEXT.__text: 0x4b004
+1015.160.2.0.1
+  __TEXT.__text: 0x4b2d8
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x5c60
+  __TEXT.__objc_methlist: 0x5c88
   __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x4a9c
+  __TEXT.__cstring: 0x4aa9
   __TEXT.__oslogstring: 0x2930
   __TEXT.__gcc_except_tab: 0x8cc
-  __TEXT.__unwind_info: 0x1778
+  __TEXT.__unwind_info: 0x1780
   __TEXT.__objc_classname: 0xf5c
-  __TEXT.__objc_methname: 0x8440
+  __TEXT.__objc_methname: 0x84e6
   __TEXT.__objc_methtype: 0x15be
-  __TEXT.__objc_stubs: 0x4dc0
-  __DATA_CONST.__got: 0x508
-  __DATA_CONST.__const: 0x6e0
+  __TEXT.__objc_stubs: 0x4e20
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__const: 0x6e8
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1df8
+  __DATA_CONST.__objc_selrefs: 0x1e18
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0xea0
-  __AUTH_CONST.__cfstring: 0x6380
+  __AUTH_CONST.__cfstring: 0x63a0
   __AUTH_CONST.__objc_const: 0xb170
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2413
-  Symbols:   4757
-  CStrings:  2836
+  Functions: 2416
+  Symbols:   4764
+  CStrings:  2840
 
Symbols:
+ +[RBSExtensionProcessIdentity _extensionIdentityFromDataRepresentation:correctedToInstanceUUID:]
+ -[RBSExtensionProcessIdentity _copyWithCorrectedInstanceUUID:]
+ -[RBSProcessIdentity _copyWithCorrectedInstanceUUID:]
+ _OBJC_CLASS_$_NSJSONSerialization
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$_extensionIdentityFromDataRepresentation:correctedToInstanceUUID:
+ _objc_msgSend$dataWithJSONObject:options:error:
Functions:
+ -[RBSProcessIdentity _copyWithCorrectedInstanceUUID:]
+ -[RBSExtensionProcessIdentity _copyWithCorrectedInstanceUUID:]
+ +[RBSExtensionProcessIdentity _extensionIdentityFromDataRepresentation:correctedToInstanceUUID:]
~ -[RBSExtensionProcessIdentity initWithDecodeFromJob:uuid:] : 580 -> 776
CStrings:
+ "JSONObjectWithData:options:error:"
+ "_copyWithCorrectedInstanceUUID:"
+ "_extensionIdentityFromDataRepresentation:correctedToInstanceUUID:"
+ "dataWithJSONObject:options:error:"
```
