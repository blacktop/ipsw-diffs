## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-1663.0.0.0.1
-  __TEXT.__text: 0xcef94
-  __TEXT.__objc_methlist: 0x5ba4
+1673.0.0.0.0
+  __TEXT.__text: 0xce76c
+  __TEXT.__objc_methlist: 0x5b94
   __TEXT.__const: 0xdb30
-  __TEXT.__cstring: 0x1855e
+  __TEXT.__cstring: 0x183ee
   __TEXT.__gcc_except_tab: 0xde0
-  __TEXT.__oslogstring: 0x91f
   __TEXT.__dlopen_cstrs: 0x111
+  __TEXT.__oslogstring: 0x8c1
   __TEXT.__swift5_typeref: 0x30
-  __TEXT.__unwind_info: 0x19d0
+  __TEXT.__unwind_info: 0x19c8
   __TEXT.__eh_frame: 0x398
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xfd8
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__const: 0x1000
+  __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3090
+  __DATA_CONST.__objc_selrefs: 0x30a8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0xb10
-  __DATA_CONST.__got: 0x500
+  __DATA_CONST.__got: 0x4f0
   __AUTH_CONST.__const: 0x4d88
-  __AUTH_CONST.__cfstring: 0xd4e0
-  __AUTH_CONST.__objc_const: 0xa480
+  __AUTH_CONST.__cfstring: 0xd460
+  __AUTH_CONST.__objc_const: 0xa740
   __AUTH_CONST.__objc_dictobj: 0x1248
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__auth_got: 0xc08
   __AUTH.__objc_data: 0x1180
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x5c4
-  __DATA.__data: 0xe68
+  __DATA.__objc_ivar: 0x5c0
+  __DATA.__data: 0xf38
   __DATA.__bss: 0x2d0
   __DATA.__common: 0xaa4
-  __DATA_DIRTY.__objc_data: 0x500
+  __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2409
-  Symbols:   5036
-  CStrings:  2263
+  Functions: 2402
+  Symbols:   5034
+  CStrings:  2260
 
Symbols:
+ +[MIBundleContainer enumerateAppBundleContainersInDomain:forPersona:isTransient:usingBundleMetadataProviderBlock:]
+ -[MIGlobalConfiguration internalLibraryDirectory]
+ -[MIGlobalConfiguration internalMobileInstallationContentDirectory]
+ -[MIGlobalConfiguration internalSupersededAppAdditionsPlistURL]
+ -[MIStoreMetadata contentDescriptors]
+ -[MIStoreMetadata secondaryGenreID]
+ -[MIStoreMetadata setContentDescriptors:]
+ -[MIStoreMetadata setSecondaryGenreID:]
+ -[MIStoreMetadataContentDescriptor identifier]
+ -[MIStoreMetadataContentDescriptor initWithIdentifier:]
+ -[MIStoreMetadataContentDescriptor setIdentifier:]
+ GCC_except_table48
+ GCC_except_table54
+ GCC_except_table60
+ GCC_except_table66
+ _OBJC_IVAR_$_MIStoreMetadata._contentDescriptors
+ _OBJC_IVAR_$_MIStoreMetadata._secondaryGenreID
+ _OBJC_IVAR_$_MIStoreMetadataContentDescriptor._identifier
+ __OBJC_$_PROP_LIST_MIBundleMetadataProvider
+ __OBJC_$_PROTOCOL_CLASS_METHODS_MIBundleMetadataProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MIBundleMetadataProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MIUserManagementDaemonContainerResolver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MIBundleMetadataProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MIUserManagementDaemonContainerResolver
+ __OBJC_$_PROTOCOL_REFS_MIBundleMetadataProvider
+ __OBJC_CLASS_PROTOCOLS_$_MIBundleContainer
+ __OBJC_CLASS_PROTOCOLS_$_MIUserManagement
+ __OBJC_LABEL_PROTOCOL_$_MIBundleMetadataProvider
+ __OBJC_LABEL_PROTOCOL_$_MIUserManagementDaemonContainerResolver
+ __OBJC_PROTOCOL_$_MIBundleMetadataProvider
+ __OBJC_PROTOCOL_$_MIUserManagementDaemonContainerResolver
+ ___114+[MIBundleContainer enumerateAppBundleContainersInDomain:forPersona:isTransient:usingBundleMetadataProviderBlock:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e27_B16?0"MIBundleContainer"8ls32l8
+ _contentDescriptorID
+ _objc_msgSend$daemonContainerForPersonaUniqueString:personaVolumeMount:personaVolumeUUID:extensionTokenHandle:error:
+ _objc_msgSend$enumerateAppBundleContainersInDomain:forPersona:isTransient:usingBlock:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$internalLibraryDirectory
+ _objc_msgSend$internalMobileInstallationContentDirectory
+ _objc_msgSend$secondaryGenreID
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setSecondaryGenreID:
+ _secondaryGenreID
- +[MIStoreMetadataContentLevel supportsSecureCoding]
- -[MIGlobalConfiguration internalFrameworksRootDirectory]
- -[MIStoreMetadata contentLevels]
- -[MIStoreMetadata setContentLevels:]
- -[MIStoreMetadataContentDescriptor initWithKindDescriptor:]
- -[MIStoreMetadataContentDescriptor kind]
- -[MIStoreMetadataContentDescriptor setKind:]
- -[MIStoreMetadataContentLevel .cxx_destruct]
- -[MIStoreMetadataContentLevel contentDescriptors]
- -[MIStoreMetadataContentLevel copyWithZone:]
- -[MIStoreMetadataContentLevel dictionaryRepresentation]
- -[MIStoreMetadataContentLevel encodeWithCoder:]
- -[MIStoreMetadataContentLevel hash]
- -[MIStoreMetadataContentLevel initWithCoder:]
- -[MIStoreMetadataContentLevel initWithKindDescriptor:contentDescriptors:]
- -[MIStoreMetadataContentLevel isEqual:]
- -[MIStoreMetadataContentLevel kind]
- -[MIStoreMetadataContentLevel setContentDescriptors:]
- -[MIStoreMetadataContentLevel setKind:]
- GCC_except_table46
- GCC_except_table52
- GCC_except_table56
- GCC_except_table61
- GCC_except_table78
- _OBJC_CLASS_$_MIStoreMetadataContentLevel
- _OBJC_IVAR_$_MIStoreMetadata._contentLevels
- _OBJC_IVAR_$_MIStoreMetadataContentDescriptor._kind
- _OBJC_IVAR_$_MIStoreMetadataContentLevel._contentDescriptors
- _OBJC_IVAR_$_MIStoreMetadataContentLevel._kind
- _OBJC_METACLASS_$_MIStoreMetadataContentLevel
- __OBJC_$_CLASS_METHODS_MIStoreMetadataContentLevel
- __OBJC_$_CLASS_PROP_LIST_MIStoreMetadataContentLevel
- __OBJC_$_INSTANCE_METHODS_MIStoreMetadataContentLevel
- __OBJC_$_INSTANCE_VARIABLES_MIStoreMetadataContentLevel
- __OBJC_$_PROP_LIST_MIStoreMetadataContentLevel
- __OBJC_CLASS_PROTOCOLS_$_MIStoreMetadataContentLevel
- __OBJC_CLASS_RO_$_MIStoreMetadataContentLevel
- __OBJC_METACLASS_RO_$_MIStoreMetadataContentLevel
- _contentLevels
- _kMISValidationOptionAllowLaunchWarning
- _objc_msgSend$contentLevels
- _objc_msgSend$initWithKindDescriptor:
- _objc_msgSend$initWithKindDescriptor:contentDescriptors:
- _objc_msgSend$internalFrameworksRootDirectory
- _objc_msgSend$setContentLevels:
CStrings:
+ "-[MIGlobalConfiguration internalSupersededAppAdditionsPlistURL]"
+ "B16@?0@\"MIBundleContainer\"8"
+ "CoreOS"
+ "Failed to create URL for internal superseded app additions plist."
+ "Failed to set up daemon container for persona %@: %@"
+ "InternalSupersededAppAdditions.plist"
+ "_ParseContentDescriptors"
+ "id"
+ "secondaryGenreID"
+ "secondaryGenreId"
- "%s: Got daemon container at %@ for data separated persona %@ that was not on persona mount %@"
- "Expected contentLevels element to be a dictionary."
- "Expected contentLevels element to have a string value for '%@'."
- "Expected contentLevels element to have array value for '%@'."
- "Failed to determine volume UUID for daemon container for persona %@ at %@ : %@"
- "Failed to determine volume UUID for persona volume mount %@ : %@"
- "Failed to get daemon container URL from %@"
- "Failed to get daemon container for persona %@: %@"
- "Failed to get sandbox extension for daemon container for persona %@ at %@"
- "Got daemon container at %@ for data separated persona %@ that was not on persona mount %@"
- "_ParseContentLevels"
- "contentLevels"
- "contentLevels element has no valid contentDescriptors; dropping."
```
