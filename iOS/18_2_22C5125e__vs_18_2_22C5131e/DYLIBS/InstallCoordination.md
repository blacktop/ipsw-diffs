## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-631.60.47.0.0
-  __TEXT.__text: 0x60e28
+631.60.50.0.0
+  __TEXT.__text: 0x62d10
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x2db8
+  __TEXT.__objc_methlist: 0x2ee0
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xdb57
-  __TEXT.__oslogstring: 0x75c4
-  __TEXT.__gcc_except_tab: 0x1a58
-  __TEXT.__unwind_info: 0x1598
-  __TEXT.__objc_classname: 0x81c
-  __TEXT.__objc_methname: 0x9abe
-  __TEXT.__objc_methtype: 0x2157
-  __TEXT.__objc_stubs: 0x5820
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x18f0
-  __DATA_CONST.__objc_classlist: 0x178
+  __TEXT.__cstring: 0xdd70
+  __TEXT.__oslogstring: 0x7697
+  __TEXT.__gcc_except_tab: 0x1ab8
+  __TEXT.__unwind_info: 0x15f0
+  __TEXT.__objc_classname: 0x83a
+  __TEXT.__objc_methname: 0x9d26
+  __TEXT.__objc_methtype: 0x21be
+  __TEXT.__objc_stubs: 0x5980
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__const: 0x19b8
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d00
+  __DATA_CONST.__objc_selrefs: 0x1d78
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x5460
-  __AUTH_CONST.__objc_const: 0xb9e8
+  __AUTH_CONST.__cfstring: 0x54c0
+  __AUTH_CONST.__objc_const: 0xbc08
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __DATA.__objc_ivar: 0x1b0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x8a8
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xeb0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1758
-  Symbols:   2155
-  CStrings:  3208
+  Functions: 1814
+  Symbols:   2215
+  CStrings:  3244
 
Symbols:
+ _OBJC_CLASS_$_IXAppRemovabilityMetadataList
+ _OBJC_METACLASS_$_IXAppRemovabilityMetadataList
CStrings:
+ "%!s(MISSING): Failed to deserialize removability metadata for identity %!@(MISSING), version %!l(MISSING)u"
+ "%!s(MISSING): Failed to get removability dictionary for entry: %!@(MISSING)"
+ "%!s(MISSING): Returning locally read removability, %!@(MISSING) set by client %!@(MISSING), for identity:%!@(MISSING)"
+ "+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:completion:]_block_invoke"
+ "+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:error:]"
+ "+[IXAppInstallCoordinator removabilityForAppWithIdentity:byClient:error:]_block_invoke"
+ "IXAppRemovabilityMetadataList"
+ "IXCopyRemovabilityStorageWithChangeClockURL"
+ "Q32@0:8Q16Q24"
+ "Q40@0:8@16Q24^@32"
+ "RemovabilityMetadataWithMultipleSources.plist"
+ "T@\"NSDictionary\",&,N,V_clientToRemovabilityMetadataMap"
+ "_DeserializeRemovabilityMetadata"
+ "_GetRemovabilityData"
+ "_clientToRemovabilityMetadataMap"
+ "_remote_removabilityForAppWithIdentity:byClient:completion:"
+ "clientToRemovabilityMetadataMap"
+ "enumerateObjectsUsingBlock:"
+ "initWithInitialRemovability:client:"
+ "initWithInitialRemovabilityMetadata:"
+ "initWithSerializedDictionary:"
+ "isEmpty"
+ "isUnknown"
+ "mostRestrictiveRemovabilityMetadata"
+ "propertyListRepresentation"
+ "removabilityForAppWithIdentity:byClient:completion:"
+ "removabilityForAppWithIdentity:byClient:error:"
+ "removabilityForClient:notFoundRemovability:"
+ "setClientToRemovabilityMetadataMap:"
+ "updateRemovability:forClient:"
+ "updateRemovabilityWithMetadata:"
+ "v32@0:8Q16Q24"
+ "v32@?0@\"IXApplicationIdentity\"8@\"IXAppRemovabilityMetadataList\"16^B24"
+ "v32@?0@\"NSNumber\"8@\"IXAppRemovabilityMetadata\"16^B24"
+ "v32@?0@8Q16^B24"
+ "v40@0:8@\"IXApplicationIdentity\"16Q24@?<v@?Q@\"NSError\">32"
- "IXGetUncachedRemovabilityMetadataForApp"
- "unsignedIntValue"

```
