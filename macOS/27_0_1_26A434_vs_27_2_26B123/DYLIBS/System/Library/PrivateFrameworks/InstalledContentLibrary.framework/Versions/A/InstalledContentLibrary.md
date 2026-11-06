## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/Versions/A/InstalledContentLibrary`

```diff

-1674.0.0.0.0
-  __TEXT.__text: 0xce57c
-  __TEXT.__objc_methlist: 0x50a4
-  __TEXT.__const: 0x7ac0
-  __TEXT.__cstring: 0x13f5e
+1680.40.14.0.0
+  __TEXT.__text: 0xd3390
+  __TEXT.__objc_methlist: 0x5374
+  __TEXT.__const: 0x7ae0
+  __TEXT.__cstring: 0x1468e
   __TEXT.__oslogstring: 0x5e5
-  __TEXT.__gcc_except_tab: 0x9e8
+  __TEXT.__gcc_except_tab: 0x9f0
   __TEXT.__dlopen_cstrs: 0x5d
-  __TEXT.__swift5_typeref: 0x30
-  __TEXT.__unwind_info: 0x1570
-  __TEXT.__eh_frame: 0x320
+  __TEXT.__swift5_typeref: 0x38
+  __TEXT.__unwind_info: 0x16b8
+  __TEXT.__eh_frame: 0x4e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8f8
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2968
+  __DATA_CONST.__objc_selrefs: 0x2a90
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x810
-  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__got: 0x428
   __AUTH_CONST.__const: 0x8520
-  __AUTH_CONST.__cfstring: 0xb100
-  __AUTH_CONST.__objc_const: 0x9ca8
+  __AUTH_CONST.__cfstring: 0xb2e0
+  __AUTH_CONST.__objc_const: 0xa118
   __AUTH_CONST.__objc_dictobj: 0xf78
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__auth_got: 0xa78
+  __AUTH_CONST.__auth_got: 0xad8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x57c
-  __DATA.__data: 0xdf8
-  __DATA.__bss: 0x1e0
+  __AUTH.__objc_data: 0x338
+  __AUTH.__data: 0x58
+  __DATA.__objc_ivar: 0x588
+  __DATA.__data: 0xe48
+  __DATA.__bss: 0x1f0
   __DATA.__common: 0x9f8
-  __DATA_DIRTY.__objc_data: 0x1130
+  __DATA_DIRTY.__objc_data: 0x11a8
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2139
-  Symbols:   4427
-  CStrings:  1877
+  Functions: 2245
+  Symbols:   4507
+  CStrings:  1918
 
Symbols:
+ -[ICLBundleRecord appReplacementSourceBundleIdentifier]
+ -[ICLBundleRecord isInstallationHoldActive]
+ -[ICLBundleRecord setAppReplacementSourceBundleIdentifier:]
+ -[ICLBundleRecord setIsInstallationHoldActive:]
+ -[ICLWorkspace getAppLaunchProhibition:forBundleContainerURL:error:]
+ -[ICLWorkspace getAppReplacementState:forBundleContainerURL:error:]
+ -[MIBundle hasAtLeastOneExtensionImplementingExtensionPointIn:error:]
+ -[MIBundleContainer appLaunchProhibitionURL]
+ -[MIBundleContainer appReplacementStateURL]
+ -[MIBundleContainer getAppLaunchProhibition:withError:]
+ -[MIBundleContainer getAppReplacementState:withError:]
+ -[MIBundleContainer removeAppLaunchProhibitionWithError:]
+ -[MIBundleContainer removeAppReplacementStateWithError:]
+ -[MIBundleContainer saveAppLaunchProhibition:withError:]
+ -[MIBundleContainer saveAppReplacementState:withError:]
+ -[MIExecutableBundle getHasExecutableSliceForArchSupportingPAC:withError:]
+ -[MIGlobalConfiguration OSBuildVersionWithError:]
+ -[MIMCMContainer setMcmContainer:]
+ -[MIMachOImageSlice initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:supportsPAC:]
+ -[MIMachOImageSlice setSupportsPAC:]
+ -[MIMachOImageSlice supportsPAC]
+ GCC_except_table22
+ GCC_except_table41
+ GCC_except_table57
+ GCC_except_table90
+ OBJC_IVAR_$_ICLBundleRecord._appReplacementSourceBundleIdentifier
+ OBJC_IVAR_$_ICLBundleRecord._isInstallationHoldActive
+ OBJC_IVAR_$_MIMachOImageSlice._supportsPAC
+ _MIAppExtensionPointToExtensionPointIdentifierString
+ _MIAppReplacementMinimumBuildVersion
+ _MIAppReplacementStatusExpectsSourceAppIdentity
+ _MICopySupersededApplicationIdentifiersEntitlement
+ _MIHasHomeExtensionEntitlement
+ _MIHasHomeKitEntitlement
+ _MIIsRecordableAppReplacementStatus
+ _MIMachOHasRunnableSliceSupportingPAC
+ _MIStringForAppReplacementStatus
+ _OBJC_CLASS_$_MIAppLaunchProhibition
+ _OBJC_CLASS_$_MIAppReplacementState
+ _OBJC_METACLASS_$_MIAppLaunchProhibition
+ _OBJC_METACLASS_$_MIAppReplacementState
+ _PROTOCOLS_MIAppLaunchProhibition
+ _PROTOCOLS_MIAppReplacementState
+ __CLASS_METHODS_MIAppLaunchProhibition
+ __CLASS_METHODS_MIAppReplacementState
+ __CLASS_PROPERTIES_MIAppLaunchProhibition
+ __CLASS_PROPERTIES_MIAppReplacementState
+ __CopyRunnableArchNames
+ __CopyRunnablePlatforms
+ __DATA_MIAppLaunchProhibition
+ __DATA_MIAppReplacementState
+ __INSTANCE_METHODS_MIAppLaunchProhibition
+ __INSTANCE_METHODS_MIAppReplacementState
+ __IVARS_MIAppLaunchProhibition
+ __IVARS_MIAppReplacementState
+ __METACLASS_DATA_MIAppLaunchProhibition
+ __METACLASS_DATA_MIAppReplacementState
+ __PROPERTIES_MIAppLaunchProhibition
+ __PROPERTIES_MIAppReplacementState
+ __PROTOCOLS_MIAppLaunchProhibition
+ __PROTOCOLS_MIAppReplacementState
+ ___block_descriptor_40_e8_32s_e23_B32?0i8i12I16I20I24B28l
+ ___block_descriptor_57_e8_32bs40r_e14_v20?0I8I12I16l
+ _macho_supports_pointer_authentication
+ _objc_msgSend$_osBuildVersion
+ _objc_msgSend$_sourceAppIdentity
+ _objc_msgSend$_status
+ _objc_msgSend$appLaunchProhibitionURL
+ _objc_msgSend$appReplacementStateURL
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$displayName
+ _objc_msgSend$getProhibition:fromURL:error:
+ _objc_msgSend$getState:fromURL:error:
+ _objc_msgSend$initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:supportsPAC:
+ _objc_msgSend$initWithOSBuildVersion:
+ _objc_msgSend$initWithStatus:sourceAppIdentity:osBuildVersion:
+ _objc_msgSend$initWithUnsignedInteger:
+ _objc_msgSend$osBuildVersion
+ _objc_msgSend$prohibitionURLForBundleContainerURL:
+ _objc_msgSend$removeProhibitionForBundleContainerURL:error:
+ _objc_msgSend$removeStateForBundleContainerURL:error:
+ _objc_msgSend$setSupportsPAC:
+ _objc_msgSend$sourceAppIdentity
+ _objc_msgSend$stateURLForBundleContainerURL:
+ _objc_msgSend$supportsPAC
+ _swift_errorRetain
+ _symbolic ______p s5ErrorP
- -[MIMachOImageSlice initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:]
- GCC_except_table40
- GCC_except_table56
- GCC_except_table89
- ___block_descriptor_40_e8_32s_e20_B28?0i8i12I16I20I24l
- ___block_descriptor_56_e8_32bs40r_e14_v20?0I8I12I16l
- _objc_msgSend$initWithCPUType:cpuSubtype:platform:sdkVersion:minOSVersion:
CStrings:
+ " osBuildVersion="
+ " with a source app identity to ["
+ " without a source app identity to ["
+ "%@ does not have any app extensions that implement any of the required extension points for its configuration. Based on its configuration, this app must have at least one app extension that implements one of these extension points: %@."
+ "*J"
+ ", osBuildVersion="
+ ", sourceAppIdentity="
+ "-[ICLWorkspace getAppLaunchProhibition:forBundleContainerURL:error:]"
+ "-[ICLWorkspace getAppReplacementState:forBundleContainerURL:error:]"
+ "-[MIBundle hasAtLeastOneExtensionImplementingExtensionPointIn:error:]"
+ "-[MIGlobalConfiguration OSBuildVersionWithError:]"
+ "24B"
+ "AppLaunchProhibition.plist"
+ "AppReplacementState.plist"
+ "B32@?0i8i12I16I20I24B28"
+ "BuildVersion"
+ "Decoded a nil app replacement state from ["
+ "Failed to copy the OS build version"
+ "Failed to decode app launch prohibition from ["
+ "Failed to decode app replacement state from ["
+ "Failed to read app launch prohibition from ["
+ "Failed to read app replacement state from ["
+ "Failed to remove app launch prohibition at ["
+ "Failed to remove app replacement state at ["
+ "Failed to serialize app launch prohibition ["
+ "Failed to serialize app replacement state for ["
+ "Failed to write serialized app launch prohibition to ["
+ "Failed to write serialized app replacement state to ["
+ "InstalledContentLibrary.MIAppLaunchProhibition"
+ "InstalledContentLibrary.MIAppReplacementState"
+ "MIAppReplacementStatusCompleted"
+ "MIAppReplacementStatusInProgress"
+ "MIAppReplacementStatusMax"
+ "MIAppReplacementStatusNotApplicable"
+ "MIAppReplacementStatusRefused"
+ "MIAppReplacementStatusUnknown"
+ "Refusing to write "
+ "The executable at \"%s\" does not contain code for any platform and CPU architecture combination that is runnable on this device. The executable has code for these platforms and architectures: %@. This device can run code for these platforms: %@"
+ "Unknown MIAppReplacementStatus: %lu"
+ "com.apple.Home.HomeExtension"
+ "com.apple.developer.home"
+ "com.apple.developer.homekit"
+ "com.apple.developer.superseded-application-identifiers"
+ "sourceAppIdentity"
- "*I"
- "B28@?0i8i12I16I20I24"
- "The executable at \"%s\" does not contain code for any platform and CPU architecture combination that is runnable on this device. The executable has code for these platforms and architectures: %@. This device can run code for these architectures: %@. This device can run code for these platforms: %@"
```
