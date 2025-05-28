## tursd

> `/usr/libexec/tursd`

```diff

-1042.2.11.0.0
-  __TEXT.__text: 0x7710
+1042.4.11.0.0
+  __TEXT.__text: 0x7400
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_stubs: 0x1a40
-  __TEXT.__objc_methlist: 0xa6c
-  __TEXT.__cstring: 0x8af
-  __TEXT.__oslogstring: 0x2bd
+  __TEXT.__objc_stubs: 0x1980
+  __TEXT.__objc_methlist: 0xa54
+  __TEXT.__cstring: 0x87e
+  __TEXT.__oslogstring: 0x2a4
   __TEXT.__const: 0x40
-  __TEXT.__objc_methname: 0x356e
+  __TEXT.__objc_methname: 0x34e6
   __TEXT.__objc_classname: 0x150
   __TEXT.__objc_methtype: 0x884
-  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__unwind_info: 0x2d8
   __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x5d8

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2000
-  __DATA.__objc_selrefs: 0x8d0
-  __DATA.__objc_classrefs: 0x138
-  __DATA.__objc_superrefs: 0x40
+  __DATA.__objc_const: 0x1ff0
+  __DATA.__objc_selrefs: 0x8a0
   __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x1e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 262
-  Symbols:   143
-  CStrings:  706
+  Functions: 260
+  Symbols:   142
+  CStrings:  699
 
Symbols:
- _OBJC_CLASS_$_TUICFInterface
CStrings:
+ "T@\"NSString\",?,R,C"
+ "blockedCall"
- "%s: %@ destinationID: %@"
- "-[TUCall(NanoPhone) nph_isDestinationIDBlocked:]"
- "allowCallForDestinationID:providerIdentifier:"
- "callWithBlockedMembers"
- "hasBlockedMembers"
- "identifier"
- "isFromBlockList"
- "mergedRemoteMembers"
- "nph_isDestinationIDBlocked:"

```
