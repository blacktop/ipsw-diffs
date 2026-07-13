## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

```diff

-  __TEXT.__text: 0x44154
+  __TEXT.__text: 0x443d0
   __TEXT.__auth_stubs: 0xdc0
-  __TEXT.__objc_methlist: 0x5b70
+  __TEXT.__objc_methlist: 0x5b98
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x48bb
+  __TEXT.__cstring: 0x48c8
   __TEXT.__oslogstring: 0x2768
   __TEXT.__gcc_except_tab: 0x8d4
   __TEXT.__dlopen_cstrs: 0x76
   __TEXT.__unwind_info: 0x18a0
   __TEXT.__objc_classname: 0xf3c
-  __TEXT.__objc_methname: 0x81a3
+  __TEXT.__objc_methname: 0x8254
   __TEXT.__objc_methtype: 0x1595
-  __TEXT.__objc_stubs: 0x4b60
-  __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0xcf0
+  __TEXT.__objc_stubs: 0x4be0
+  __DATA_CONST.__got: 0x4e8
+  __DATA_CONST.__const: 0xcf8
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d30
+  __DATA_CONST.__objc_selrefs: 0x1d58
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e8
   __AUTH_CONST.__auth_got: 0x6f0
   __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x5fc0
+  __AUTH_CONST.__cfstring: 0x5fe0
   __AUTH_CONST.__objc_const: 0xaf78
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x1720

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2334
-  Symbols:   7313
-  CStrings:  3719
+  Functions: 2337
+  Symbols:   7324
+  CStrings:  3726
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[RBSExtensionProcessIdentity _extensionIdentityFromDataRepresentation:correctedToInstanceUUID:]
+ -[RBSExtensionProcessIdentity _copyWithCorrectedInstanceUUID:]
+ -[RBSProcessIdentity _copyWithCorrectedInstanceUUID:]
+ _OBJC_CLASS_$_NSJSONSerialization
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_extensionIdentityFromDataRepresentation:correctedToInstanceUUID:
+ _objc_msgSend$dataWithJSONObject:options:error:
Functions:
+ -[RBSProcessIdentity _copyWithCorrectedInstanceUUID:]
+ -[RBSExtensionProcessIdentity _copyWithCorrectedInstanceUUID:]
+ +[RBSExtensionProcessIdentity _extensionIdentityFromDataRepresentation:correctedToInstanceUUID:]
~ -[RBSExtensionProcessIdentity initWithDecodeFromJob:uuid:] : 484 -> 628
CStrings:
+ "JSONObjectWithData:options:error:"
+ "UUIDString"
+ "_copyWithCorrectedInstanceUUID:"
+ "_extensionIdentityFromDataRepresentation:correctedToInstanceUUID:"
+ "dataWithJSONObject:options:error:"

```
