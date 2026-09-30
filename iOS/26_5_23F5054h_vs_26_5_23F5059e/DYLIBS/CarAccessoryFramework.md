## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-515.26.0.0.0
-  __TEXT.__text: 0x1207a0
+515.28.0.0.0
+  __TEXT.__text: 0x120d34
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x1859c
+  __TEXT.__objc_methlist: 0x185fc
   __TEXT.__const: 0x198
-  __TEXT.__cstring: 0x7bfb
+  __TEXT.__cstring: 0x7c27
   __TEXT.__oslogstring: 0x3a1f
   __TEXT.__gcc_except_tab: 0x604
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x3da8
   __TEXT.__objc_classname: 0x3dc0
-  __TEXT.__objc_methname: 0x1f96c
+  __TEXT.__objc_methname: 0x1f9c0
   __TEXT.__objc_methtype: 0x4cc4
-  __TEXT.__objc_stubs: 0x148a0
+  __TEXT.__objc_stubs: 0x14900
   __DATA_CONST.__got: 0xec0
-  __DATA_CONST.__const: 0x2648
+  __DATA_CONST.__const: 0x2650
   __DATA_CONST.__objc_classlist: 0xd90
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x608
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a38
+  __DATA_CONST.__objc_selrefs: 0x7a50
   __DATA_CONST.__objc_protorefs: 0x5a8
   __DATA_CONST.__objc_superrefs: 0x7d0
-  __DATA_CONST.__objc_arraydata: 0xb828
+  __DATA_CONST.__objc_arraydata: 0xb898
   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0xa80
-  __AUTH_CONST.__cfstring: 0xda80
-  __AUTH_CONST.__objc_const: 0x4e788
+  __AUTH_CONST.__cfstring: 0xdaa0
+  __AUTH_CONST.__objc_const: 0x4e800
   __AUTH_CONST.__objc_dictobj: 0x6360
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x2c10
-  __DATA.__objc_ivar: 0x664
+  __DATA.__objc_ivar: 0x668
   __DATA.__data: 0x4880
   __DATA.__bss: 0x3c0
   __DATA_DIRTY.__objc_data: 0x5b90

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 09C1FA97-F53B-3314-BC4D-EA73BBDFBD2C
-  Functions: 7565
-  Symbols:   25168
-  CStrings:  9908
+  UUID: 4EBE0890-E0D6-3D68-BA2F-A691D6765581
+  Functions: 7572
+  Symbols:   25187
+  CStrings:  9913
 
Symbols:
+ -[CAFRouteLeg identifier]
+ -[CAFRouteLeg initWithCoordinates:destination:identifier:origin:]
+ -[CAFRouteSharing hasIdentifier]
+ -[CAFRouteSharing identifierCharacteristic]
+ -[CAFRouteSharing identifierInvalid]
+ -[CAFRouteSharing identifier]
+ -[CAFRouteSharing registeredForIdentifier]
+ -[CAFRouteSharing setIdentifier:]
+ _CARPKeyRouteLegIdentifier
+ _OBJC_IVAR_$_CAFRouteLeg._identifier
+ _objc_msgSend$hasIdentifier
+ _objc_msgSend$identifierInvalid
+ _objc_msgSend$routeSharingService:didUpdateIdentifier:
- -[CAFRouteLeg initWithCoordinates:destination:origin:]
CStrings:
+ "<%@: %p { %@: %@, %@: %@, %@: %@, %@: %@ }>"
+ "hasIdentifier"
+ "identifierInvalid"
+ "initWithCoordinates:destination:identifier:origin:"
+ "routeSharingService:didUpdateIdentifier:"
- "initWithCoordinates:destination:origin:"

```
