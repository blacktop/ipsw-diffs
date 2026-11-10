## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Versions/A/InstallCoordination`

```diff

-842.0.1.0.0
-  __TEXT.__text: 0x66734
-  __TEXT.__objc_methlist: 0x4708
+849.40.7.0.2
+  __TEXT.__text: 0x680c4
+  __TEXT.__objc_methlist: 0x4a38
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x185ec
+  __TEXT.__cstring: 0x18b86
   __TEXT.__gcc_except_tab: 0x1c10
   __TEXT.__oslogstring: 0x195
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1738
+  __TEXT.__unwind_info: 0x17b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x980
-  __DATA_CONST.__objc_classlist: 0x1e8
+  __DATA_CONST.__const: 0x9d0
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2250
+  __DATA_CONST.__objc_selrefs: 0x22e8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x19a0
-  __AUTH_CONST.__cfstring: 0x5e40
-  __AUTH_CONST.__objc_const: 0xcd10
+  __AUTH_CONST.__const: 0x19d0
+  __AUTH_CONST.__cfstring: 0x6060
+  __AUTH_CONST.__objc_const: 0xd7c0
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x370
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x348
-  __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x244
-  __DATA.__data: 0xcc8
+  __DATA.__objc_classrefs: 0x350
+  __DATA.__objc_superrefs: 0x190
+  __DATA.__objc_ivar: 0x260
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x90
-  __DATA.__common: 0x1
-  __DATA_DIRTY.__objc_data: 0xfa0
-  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__objc_data: 0x14a0
+  __DATA_DIRTY.__data: 0xaf0
   __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1778
-  Symbols:   3937
-  CStrings:  1889
+  Functions: 1837
+  Symbols:   4067
+  CStrings:  1916
 
Symbols:
+ +[IXAppInstallCoordinator(IXAppReplacement) appReplacementRefusedForAppIdentity:options:error:]
+ +[IXAppInstallCoordinator(IXAppReplacement) getAppReplacementSource:forAppIdentity:options:error:]
+ +[IXAppInstallCoordinator(IXAppReplacement) managedAppBundleIdentifiersWithError:]
+ +[IXAppInstallCoordinator(IXAppReplacement) performAppReplacementFromAppIdentity:toAppIdentity:options:error:]
+ +[IXAppInstallCoordinator(IXAppReplacement) prepareForAppReplacementSourceLookupWithOptions:error:]
+ +[IXAppInstallCoordinator(IXAppReplacement) resumeInterruptedAppReplacementWithOptions:completion:]
+ +[IXAppInstallCoordinator(IXAppReplacement_Private) resetAppReplacementStateForAppIdentity:options:error:]
+ +[IXAppReplacementOptions supportsSecureCoding]
+ +[IXAppReplacementRefusalOptions supportsSecureCoding]
+ +[IXAppReplacementSourceOptions supportsSecureCoding]
+ +[IXAppReplacementStateResetOptions supportsSecureCoding]
+ +[IXDataReplacementRequest supportsSecureCoding]
+ -[IXAppReplacementOptions copyWithZone:]
+ -[IXAppReplacementOptions encodeWithCoder:]
+ -[IXAppReplacementOptions initForTesting]
+ -[IXAppReplacementOptions initWithCoder:]
+ -[IXAppReplacementOptions isEqual:]
+ -[IXAppReplacementRefusalOptions copyWithZone:]
+ -[IXAppReplacementRefusalOptions encodeWithCoder:]
+ -[IXAppReplacementRefusalOptions initForTesting]
+ -[IXAppReplacementRefusalOptions initWithCoder:]
+ -[IXAppReplacementRefusalOptions isEqual:]
+ -[IXAppReplacementSourceCacheOptions copyWithZone:]
+ -[IXAppReplacementSourceCacheOptions hash]
+ -[IXAppReplacementSourceCacheOptions initForTesting]
+ -[IXAppReplacementSourceCacheOptions isEqual:]
+ -[IXAppReplacementSourceOptions copyWithZone:]
+ -[IXAppReplacementSourceOptions encodeWithCoder:]
+ -[IXAppReplacementSourceOptions initForTesting]
+ -[IXAppReplacementSourceOptions initWithCoder:]
+ -[IXAppReplacementSourceOptions isEqual:]
+ -[IXAppReplacementSourceResolver .cxx_destruct]
+ -[IXAppReplacementSourceResolver identity]
+ -[IXAppReplacementSourceResolver initWithIdentity:managedAppBundleIdentifiers:]
+ -[IXAppReplacementSourceResolver managedAppBundleIdentifiers]
+ -[IXAppReplacementSourceResolver resolveAppReplacementSource:replacementRuledOut:replacementCandidate:error:]
+ -[IXAppReplacementStateResetOptions copyWithZone:]
+ -[IXAppReplacementStateResetOptions encodeWithCoder:]
+ -[IXAppReplacementStateResetOptions initForTesting]
+ -[IXAppReplacementStateResetOptions initWithCoder:]
+ -[IXAppReplacementStateResetOptions isEqual:]
+ -[IXApplicationIdentity hasUnresolvedPersona]
+ -[IXApplicationIdentity initWithLSApplicationIdentity:]
+ -[IXDataReplacementRequest .cxx_destruct]
+ -[IXDataReplacementRequest copyWithZone:]
+ -[IXDataReplacementRequest dataContainerURL]
+ -[IXDataReplacementRequest description]
+ -[IXDataReplacementRequest destinationIdentity]
+ -[IXDataReplacementRequest encodeWithCoder:]
+ -[IXDataReplacementRequest entityType]
+ -[IXDataReplacementRequest hash]
+ -[IXDataReplacementRequest initWithCoder:]
+ -[IXDataReplacementRequest initWithSourceIdentity:destinationIdentity:entityType:dataContainerURL:]
+ -[IXDataReplacementRequest isEqual:]
+ -[IXDataReplacementRequest sourceIdentity]
+ -[IXPlaceholderAttributes alternateDisplayNames]
+ -[IXPlaceholderAttributes setAlternateDisplayNames:]
+ OBJC_IVAR_$_IXAppReplacementSourceResolver._identity
+ OBJC_IVAR_$_IXAppReplacementSourceResolver._managedAppBundleIdentifiers
+ OBJC_IVAR_$_IXDataReplacementRequest._dataContainerURL
+ OBJC_IVAR_$_IXDataReplacementRequest._destinationIdentity
+ OBJC_IVAR_$_IXDataReplacementRequest._entityType
+ OBJC_IVAR_$_IXDataReplacementRequest._sourceIdentity
+ OBJC_IVAR_$_IXPlaceholderAttributes._alternateDisplayNames
+ _IXAppReplacementErrorDomain
+ _IXStringForReplacementEntityType
+ _OBJC_CLASS_$_IXAppReplacementOptions
+ _OBJC_CLASS_$_IXAppReplacementRefusalOptions
+ _OBJC_CLASS_$_IXAppReplacementSourceCacheOptions
+ _OBJC_CLASS_$_IXAppReplacementSourceOptions
+ _OBJC_CLASS_$_IXAppReplacementSourceResolver
+ _OBJC_CLASS_$_IXAppReplacementStateResetOptions
+ _OBJC_CLASS_$_IXDataReplacementRequest
+ _OBJC_METACLASS_$_IXAppReplacementOptions
+ _OBJC_METACLASS_$_IXAppReplacementRefusalOptions
+ _OBJC_METACLASS_$_IXAppReplacementSourceCacheOptions
+ _OBJC_METACLASS_$_IXAppReplacementSourceOptions
+ _OBJC_METACLASS_$_IXAppReplacementSourceResolver
+ _OBJC_METACLASS_$_IXAppReplacementStateResetOptions
+ _OBJC_METACLASS_$_IXDataReplacementRequest
+ __OBJC_$_CLASS_METHODS_IXAppInstallCoordinator(IXAppReplacement|IXAppReplacement_Private|IXTesting|IXPersonaBasedMultiUser|IXDiskImageMounter|IXRootContentRegistration|IXSimpleInstaller|IXSimpleInstallerPrivate|IXPersona|IXPersona_Private|IXOSModuleRegistration|IXPersonaConstruction|IXDemoteToPlaceholder|IXDemoteToPlaceholderTesting)
+ __OBJC_$_CLASS_METHODS_IXAppReplacementOptions
+ __OBJC_$_CLASS_METHODS_IXAppReplacementRefusalOptions
+ __OBJC_$_CLASS_METHODS_IXAppReplacementSourceOptions
+ __OBJC_$_CLASS_METHODS_IXAppReplacementStateResetOptions
+ __OBJC_$_CLASS_METHODS_IXDataReplacementRequest
+ __OBJC_$_CLASS_PROP_LIST_IXAppReplacementOptions
+ __OBJC_$_CLASS_PROP_LIST_IXAppReplacementRefusalOptions
+ __OBJC_$_CLASS_PROP_LIST_IXAppReplacementSourceOptions
+ __OBJC_$_CLASS_PROP_LIST_IXAppReplacementStateResetOptions
+ __OBJC_$_CLASS_PROP_LIST_IXDataReplacementRequest
+ __OBJC_$_INSTANCE_METHODS_IXAppReplacementOptions
+ __OBJC_$_INSTANCE_METHODS_IXAppReplacementRefusalOptions
+ __OBJC_$_INSTANCE_METHODS_IXAppReplacementSourceCacheOptions
+ __OBJC_$_INSTANCE_METHODS_IXAppReplacementSourceOptions
+ __OBJC_$_INSTANCE_METHODS_IXAppReplacementSourceResolver
+ __OBJC_$_INSTANCE_METHODS_IXAppReplacementStateResetOptions
+ __OBJC_$_INSTANCE_METHODS_IXDataReplacementRequest
+ __OBJC_$_INSTANCE_VARIABLES_IXAppReplacementSourceResolver
+ __OBJC_$_INSTANCE_VARIABLES_IXDataReplacementRequest
+ __OBJC_$_PROP_LIST_IXAppReplacementSourceResolver
+ __OBJC_$_PROP_LIST_IXDataReplacementRequest
+ __OBJC_CLASS_PROTOCOLS_$_IXAppReplacementOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXAppReplacementRefusalOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXAppReplacementSourceCacheOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXAppReplacementSourceOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXAppReplacementStateResetOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXDataReplacementRequest
+ __OBJC_CLASS_RO_$_IXAppReplacementOptions
+ __OBJC_CLASS_RO_$_IXAppReplacementRefusalOptions
+ __OBJC_CLASS_RO_$_IXAppReplacementSourceCacheOptions
+ __OBJC_CLASS_RO_$_IXAppReplacementSourceOptions
+ __OBJC_CLASS_RO_$_IXAppReplacementSourceResolver
+ __OBJC_CLASS_RO_$_IXAppReplacementStateResetOptions
+ __OBJC_CLASS_RO_$_IXDataReplacementRequest
+ __OBJC_METACLASS_RO_$_IXAppReplacementOptions
+ __OBJC_METACLASS_RO_$_IXAppReplacementRefusalOptions
+ __OBJC_METACLASS_RO_$_IXAppReplacementSourceCacheOptions
+ __OBJC_METACLASS_RO_$_IXAppReplacementSourceOptions
+ __OBJC_METACLASS_RO_$_IXAppReplacementSourceResolver
+ __OBJC_METACLASS_RO_$_IXAppReplacementStateResetOptions
+ __OBJC_METACLASS_RO_$_IXDataReplacementRequest
+ ___43-[IXPlaceholderAttributes infoPlistContent]_block_invoke
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24l
+ _objc_msgSend$alternateDisplayNames
+ _objc_msgSend$dataContainerURL
+ _objc_msgSend$destinationIdentity
+ _objc_msgSend$entityType
+ _objc_msgSend$initWithSourceIdentity:destinationIdentity:entityType:dataContainerURL:
+ _objc_msgSend$setAlternateDisplayNames:
+ _objc_msgSend$sourceIdentity
- __OBJC_$_CLASS_METHODS_IXAppInstallCoordinator(IXTesting|IXPersonaBasedMultiUser|IXDiskImageMounter|IXRootContentRegistration|IXSimpleInstaller|IXSimpleInstallerPrivate|IXPersona|IXPersona_Private|IXOSModuleRegistration|IXPersonaConstruction|IXDemoteToPlaceholder|IXDemoteToPlaceholderTesting)
CStrings:
+ "%s not supported on this platform."
+ "%s: %s not supported on this platform. : %@"
+ "+[IXAppInstallCoordinator(IXAppReplacement) appReplacementRefusedForAppIdentity:options:error:]"
+ "+[IXAppInstallCoordinator(IXAppReplacement) getAppReplacementSource:forAppIdentity:options:error:]"
+ "+[IXAppInstallCoordinator(IXAppReplacement) managedAppBundleIdentifiersWithError:]"
+ "+[IXAppInstallCoordinator(IXAppReplacement) performAppReplacementFromAppIdentity:toAppIdentity:options:error:]"
+ "+[IXAppInstallCoordinator(IXAppReplacement) prepareForAppReplacementSourceLookupWithOptions:error:]"
+ "+[IXAppInstallCoordinator(IXAppReplacement) resumeInterruptedAppReplacementWithOptions:completion:]"
+ "+[IXAppInstallCoordinator(IXAppReplacement_Private) resetAppReplacementStateForAppIdentity:options:error:]"
+ "-[IXAppReplacementSourceResolver resolveAppReplacementSource:replacementRuledOut:replacementCandidate:error:]"
+ "<%@: %@ -> %@ (entityType: %@, dataContainer: %@)>"
+ "App Replacement source is being restored from backup."
+ "App Replacement source is being updated."
+ "App Replacement source is unavailable due to an in-flight install."
+ "AppExtension"
+ "CFBundleDisplayName#"
+ "Car"
+ "Failed to replace data container."
+ "IXAppReplacementErrorDomain"
+ "Unhandled reason for code: %lu in domain IXAppReplacementErrorDomain"
+ "Unknown IXReplacementEntityType value: %lu"
+ "alternateDisplayNames"
+ "dataContainerURL"
+ "destinationIdentity"
+ "entityType"
+ "sourceIdentity"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
```
