## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-842.0.1.0.0
-  __TEXT.__text: 0x6b5a8
-  __TEXT.__objc_methlist: 0x48b0
+849.40.2.502.1
+  __TEXT.__text: 0x6df7c
+  __TEXT.__objc_methlist: 0x4b90
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x102c0
-  __TEXT.__oslogstring: 0x86c9
-  __TEXT.__gcc_except_tab: 0x1ef8
+  __TEXT.__cstring: 0x10831
+  __TEXT.__oslogstring: 0x885d
+  __TEXT.__gcc_except_tab: 0x1f58
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2328
+  __TEXT.__unwind_info: 0x2448
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e98
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__const: 0x1ee0
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2360
+  __DATA_CONST.__objc_selrefs: 0x2458
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x120
-  __DATA_CONST.__got: 0x4d0
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x6240
-  __AUTH_CONST.__objc_const: 0xcb68
+  __DATA_CONST.__got: 0x510
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0x6480
+  __AUTH_CONST.__objc_const: 0xd440
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__auth_got: 0x608
-  __AUTH.__objc_data: 0x410
-  __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x258
+  __AUTH.__objc_data: 0x5a0
+  __AUTH.__data: 0x20
+  __DATA.__objc_ivar: 0x268
   __DATA.__data: 0xae8
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2206
-  Symbols:   3899
-  CStrings:  1897
+  Functions: 2277
+  Symbols:   4032
+  CStrings:  1929
 
Symbols:
+ +[IXAppInstallCoordinator(IXAppReplacement) _deviceHasPersonas]
+ +[IXAppInstallCoordinator(IXAppReplacement) _personaForIdentity:record:error:]
+ +[IXAppInstallCoordinator(IXAppReplacement) _personaForRecord:error:]
+ +[IXAppInstallCoordinator(IXAppReplacement) appReplacementRefusedForAppIdentity:options:error:]
+ +[IXAppInstallCoordinator(IXAppReplacement) getAppReplacementSource:forAppIdentity:options:error:]
+ +[IXAppInstallCoordinator(IXAppReplacement) performAppReplacementFromAppIdentity:toAppIdentity:options:error:]
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
+ -[IXAppReplacementSourceOptions copyWithZone:]
+ -[IXAppReplacementSourceOptions encodeWithCoder:]
+ -[IXAppReplacementSourceOptions initForTesting]
+ -[IXAppReplacementSourceOptions initWithCoder:]
+ -[IXAppReplacementSourceOptions isEqual:]
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
+ GCC_except_table12
+ _IXAppReplacementErrorDomain
+ _IXStringForReplacementEntityType
+ _LSUserApplicationType
+ _MobileInstallationPrepareAppReplacement
+ _MobileInstallationSetAppLaunchProhibited
+ _MobileInstallationSetAppReplacementStatus
+ _OBJC_CLASS_$_ICLWorkspace
+ _OBJC_CLASS_$_IXAppReplacementOptions
+ _OBJC_CLASS_$_IXAppReplacementRefusalOptions
+ _OBJC_CLASS_$_IXAppReplacementSourceOptions
+ _OBJC_CLASS_$_IXAppReplacementStateResetOptions
+ _OBJC_CLASS_$_IXDataReplacementRequest
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_MIUserManagement
+ _OBJC_IVAR_$_IXDataReplacementRequest._dataContainerURL
+ _OBJC_IVAR_$_IXDataReplacementRequest._destinationIdentity
+ _OBJC_IVAR_$_IXDataReplacementRequest._entityType
+ _OBJC_IVAR_$_IXDataReplacementRequest._sourceIdentity
+ _OBJC_METACLASS_$_IXAppReplacementOptions
+ _OBJC_METACLASS_$_IXAppReplacementRefusalOptions
+ _OBJC_METACLASS_$_IXAppReplacementSourceOptions
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
+ __OBJC_$_INSTANCE_METHODS_IXAppReplacementSourceOptions
+ __OBJC_$_INSTANCE_METHODS_IXAppReplacementStateResetOptions
+ __OBJC_$_INSTANCE_METHODS_IXDataReplacementRequest
+ __OBJC_$_INSTANCE_VARIABLES_IXDataReplacementRequest
+ __OBJC_$_PROP_LIST_IXDataReplacementRequest
+ __OBJC_CLASS_PROTOCOLS_$_IXAppReplacementOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXAppReplacementRefusalOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXAppReplacementSourceOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXAppReplacementStateResetOptions
+ __OBJC_CLASS_PROTOCOLS_$_IXDataReplacementRequest
+ __OBJC_CLASS_RO_$_IXAppReplacementOptions
+ __OBJC_CLASS_RO_$_IXAppReplacementRefusalOptions
+ __OBJC_CLASS_RO_$_IXAppReplacementSourceOptions
+ __OBJC_CLASS_RO_$_IXAppReplacementStateResetOptions
+ __OBJC_CLASS_RO_$_IXDataReplacementRequest
+ __OBJC_METACLASS_RO_$_IXAppReplacementOptions
+ __OBJC_METACLASS_RO_$_IXAppReplacementRefusalOptions
+ __OBJC_METACLASS_RO_$_IXAppReplacementSourceOptions
+ __OBJC_METACLASS_RO_$_IXAppReplacementStateResetOptions
+ __OBJC_METACLASS_RO_$_IXDataReplacementRequest
+ ___106+[IXAppInstallCoordinator(IXAppReplacement_Private) resetAppReplacementStateForAppIdentity:options:error:]_block_invoke
+ ___110+[IXAppInstallCoordinator(IXAppReplacement) performAppReplacementFromAppIdentity:toAppIdentity:options:error:]_block_invoke
+ ___95+[IXAppInstallCoordinator(IXAppReplacement) appReplacementRefusedForAppIdentity:options:error:]_block_invoke
+ ___98+[IXAppInstallCoordinator(IXAppReplacement) getAppReplacementSource:forAppIdentity:options:error:]_block_invoke
+ ___99+[IXAppInstallCoordinator(IXAppReplacement) resumeInterruptedAppReplacementWithOptions:completion:]_block_invoke
+ _objc_msgSend$_deviceHasPersonas
+ _objc_msgSend$_personaForIdentity:record:error:
+ _objc_msgSend$_personaForRecord:error:
+ _objc_msgSend$_remote_appReplacementRefusedForAppIdentity:options:completion:
+ _objc_msgSend$_remote_performAppReplacementFromAppIdentity:toAppIdentity:options:completion:
+ _objc_msgSend$_remote_recordAppReplacementNotApplicableForAppIdentity:options:completion:
+ _objc_msgSend$_remote_resetAppReplacementStateForAppIdentity:options:completion:
+ _objc_msgSend$_remote_resumeInterruptedAppReplacementWithOptions:completion:
+ _objc_msgSend$bundleContainerURL
+ _objc_msgSend$bundleRecordWithApplicationIdentifier:error:
+ _objc_msgSend$compare:options:
+ _objc_msgSend$dataContainerURL
+ _objc_msgSend$destinationIdentity
+ _objc_msgSend$deviceHasPersonas
+ _objc_msgSend$entitlements
+ _objc_msgSend$entityType
+ _objc_msgSend$getAppReplacementState:forBundleContainerURL:error:
+ _objc_msgSend$hasUnresolvedPersona
+ _objc_msgSend$initWithSourceIdentity:destinationIdentity:entityType:dataContainerURL:
+ _objc_msgSend$installBuildVersion
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_msgSend$objectForKey:ofClass:valuesOfClass:
+ _objc_msgSend$sourceIdentity
+ _objc_msgSend$status
+ _objc_msgSend$typeForInstallMachinery
- __OBJC_$_CLASS_METHODS_IXAppInstallCoordinator(IXTesting|IXPersonaBasedMultiUser|IXDiskImageMounter|IXRootContentRegistration|IXSimpleInstaller|IXSimpleInstallerPrivate|IXPersona|IXPersona_Private|IXOSModuleRegistration|IXPersonaConstruction|IXDemoteToPlaceholder|IXDemoteToPlaceholderTesting)
CStrings:
+ "%@ is not installed for persona %@. Found: %@"
+ "%s: %@ is not installed for persona %@. Found: %@ : %@"
+ "%s: Failed to record app replacement as not applicable: %@"
+ "%s: Failed to record app replacement refusal for %@: %@"
+ "%s: Failed to replace %@ with %@: %@"
+ "%s: Failed to reset app replacement state for %@: %@"
+ "%s: Failed to resume interrupted app replacement: %@"
+ "%s: Found %lu personas associated with %@; persona resolution is ambiguous. Found: %@ : %@"
+ "+[IXAppInstallCoordinator(IXAppReplacement) _personaForIdentity:record:error:]"
+ "+[IXAppInstallCoordinator(IXAppReplacement) _personaForRecord:error:]"
+ "+[IXAppInstallCoordinator(IXAppReplacement) appReplacementRefusedForAppIdentity:options:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXAppReplacement) getAppReplacementSource:forAppIdentity:options:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXAppReplacement) performAppReplacementFromAppIdentity:toAppIdentity:options:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXAppReplacement) resumeInterruptedAppReplacementWithOptions:completion:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXAppReplacement_Private) resetAppReplacementStateForAppIdentity:options:error:]_block_invoke"
+ "24B"
+ "<%@: %@ -> %@ (entityType: %@, dataContainer: %@)>"
+ "App Replacement source is being restored from backup."
+ "App Replacement source is being updated."
+ "App Replacement source is unavailable due to an in-flight install."
+ "AppExtension"
+ "Found %lu personas associated with %@; persona resolution is ambiguous. Found: %@"
+ "IXAppReplacementErrorDomain"
+ "Invalid"
+ "Unhandled reason for code: %lu in domain IXAppReplacementErrorDomain"
+ "Unknown IXReplacementEntityType value: %lu"
+ "com.apple.developer.appmanagedfeatures"
+ "com.apple.developer.superseded-application-identifiers"
+ "dataContainerURL"
+ "destinationIdentity"
+ "entityType"
+ "sourceIdentity"
```
