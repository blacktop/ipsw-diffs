## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-582.0.4.0.0
-  __TEXT.__text: 0x2b334
+588.0.0.0.0
+  __TEXT.__text: 0x2b2e4
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x1dc4
-  __TEXT.__cstring: 0x13b0
+  __TEXT.__objc_methlist: 0x1dec
+  __TEXT.__cstring: 0x13c7
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0xd40
-  __TEXT.__oslogstring: 0x243a
+  __TEXT.__oslogstring: 0x2485
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x898
-  __TEXT.__objc_classname: 0x2a1
-  __TEXT.__objc_methname: 0x4a26
+  __TEXT.__unwind_info: 0x8a0
+  __TEXT.__objc_classname: 0x2a3
+  __TEXT.__objc_methname: 0x4aaa
   __TEXT.__objc_methtype: 0xa50
-  __TEXT.__objc_stubs: 0x4100
+  __TEXT.__objc_stubs: 0x4140
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0xca0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_selrefs: 0x1400
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1500
-  __AUTH_CONST.__objc_const: 0x4290
+  __AUTH_CONST.__cfstring: 0x1520
+  __AUTH_CONST.__objc_const: 0x42c0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x17c
+  __DATA.__objc_ivar: 0x180
   __DATA.__data: 0x4e8
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5616793-F50B-353D-BAB1-085DE5577935
-  Functions: 803
-  Symbols:   3070
-  CStrings:  1524
+  UUID: 2D0EE238-D4BC-3483-AA49-CF4A334CD63F
+  Functions: 805
+  Symbols:   3077
+  CStrings:  1533
 
Symbols:
+ -[DSIdentity displayName]
+ -[DSIdentity identityNameComponents]
+ -[DSIdentity setDisplayName:]
+ -[DSIdentity setIdentityNameComponents:]
+ -[DSXPCSharingPerson addName:]
+ -[DSXPCSharingPerson addName:].cold.1
+ _OBJC_IVAR_$_DSIdentity._displayName
+ _OBJC_IVAR_$_DSIdentity._identityNameComponents
+ _objc_msgSend$addName:
+ _objc_msgSend$identityNameComponents
+ _objc_msgSend$isIdentity:
+ _objc_msgSend$setIdentityNameComponents:
- -[DSContactProvider unifiedContactsDictionaryForIdentities:].cold.1
- -[DSIdentity name]
- -[DSIdentity setName:]
- -[DSXPCSharingPerson isIdentity:].cold.2
- _OBJC_IVAR_$_DSIdentity._name
- _objc_msgSend$ds_identifier
- _objc_msgSend$isLikeIdentity:
CStrings:
+ "Adding display name %{private}@ for %{public}@"
+ "Contact identifier %{private}@ wasn't recognized by ContactStore"
+ "Found sharing person %@ matching %@"
+ "Identity %@ has a unified contact identifier, but no matching contact was found-- checking handles for match"
+ "No sharing person found in model matching %@"
+ "Not adding display name %@ because we have a contact to use"
+ "T@\"NSPersonNameComponents\",&,N,V_identityNameComponents"
+ "T@\"NSString\",&,N,V_displayName"
+ "_identityNameComponents"
+ "addName:"
+ "identityNameComponents"
+ "setIdentityNameComponents:"
- "Adding a shared resource from %@ for identity %@ to person %@"
- "Found no identifying handles within %@ -- this should never happen!"
- "Identity %@ has a unified contact identifier, but no matching contact was found"
- "T@\"NSPersonNameComponents\",&,N,V_name"
- "sharingPersonForIdentities:completion: checking %ld sources for participants"

```
