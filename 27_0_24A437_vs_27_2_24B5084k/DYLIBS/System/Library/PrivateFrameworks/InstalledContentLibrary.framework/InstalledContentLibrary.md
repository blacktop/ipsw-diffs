## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1674.2.1.0.0
-  __TEXT.__text: 0xcce98
-  __TEXT.__objc_methlist: 0x5be4
-  __TEXT.__const: 0xdb30
-  __TEXT.__cstring: 0x183ee
+1680.40.6.502.1
+  __TEXT.__text: 0xd18a4
+  __TEXT.__objc_methlist: 0x5eb4
+  __TEXT.__const: 0xdb50
+  __TEXT.__cstring: 0x18bee
   __TEXT.__gcc_except_tab: 0xde8
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__oslogstring: 0x8c1
-  __TEXT.__swift5_typeref: 0x30
-  __TEXT.__unwind_info: 0x1f70
-  __TEXT.__eh_frame: 0x398
+  __TEXT.__swift5_typeref: 0x38
+  __TEXT.__unwind_info: 0x20e8
+  __TEXT.__eh_frame: 0x558
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1000
-  __DATA_CONST.__objc_classlist: 0x228
+  __DATA_CONST.__const: 0x1078
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30c0
+  __DATA_CONST.__objc_selrefs: 0x31e0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0xb10
-  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__got: 0x508
   __AUTH_CONST.__const: 0x4d88
-  __AUTH_CONST.__cfstring: 0xd4a0
-  __AUTH_CONST.__objc_const: 0xa7d0
+  __AUTH_CONST.__cfstring: 0xd6c0
+  __AUTH_CONST.__objc_const: 0xac00
   __AUTH_CONST.__objc_dictobj: 0x1248
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__auth_got: 0xc10
-  __AUTH.__objc_data: 0x1180
-  __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x5cc
-  __DATA.__data: 0xf38
+  __AUTH_CONST.__auth_got: 0xc68
+  __AUTH.__objc_data: 0x1260
+  __AUTH.__data: 0xd8
+  __DATA.__objc_ivar: 0x5d0
+  __DATA.__data: 0xf88
   __DATA.__common: 0xaa4
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x50

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2412
-  Symbols:   5051
-  CStrings:  2262
+  Functions: 2510
+  Symbols:   5120
+  CStrings:  2306
 
Symbols:
+ -[ICLBundleRecord appReplacementSourceBundleIdentifier]
+ -[ICLBundleRecord setAppReplacementSourceBundleIdentifier:]
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
+ -[MIDataContainer supersedeExistingContainer:error:]
+ -[MIGlobalConfiguration OSBuildVersionWithError:]
+ -[MIMCMContainer supersedeExistingContainer:error:]
+ GCC_except_table56
+ _MIAppExtensionPointToExtensionPointIdentifierString
+ _MIAppReplacementMinimumBuildVersion
+ _MIAppReplacementStatusExpectsSourceAppIdentity
+ _MICopySupersededApplicationIdentifiersEntitlement
+ _MIHasHomeKitEntitlement
+ _MIIsRecordableAppReplacementStatus
+ _MIStringForAppReplacementStatus
+ _OBJC_CLASS_$_MIAppLaunchProhibition
+ _OBJC_CLASS_$_MIAppReplacementState
+ _OBJC_IVAR_$_ICLBundleRecord._appReplacementSourceBundleIdentifier
+ _OBJC_METACLASS_$_MIAppLaunchProhibition
+ _OBJC_METACLASS_$_MIAppReplacementState
+ __CLASS_METHODS_MIAppLaunchProhibition
+ __CLASS_METHODS_MIAppReplacementState
+ __CLASS_PROPERTIES_MIAppLaunchProhibition
+ __CLASS_PROPERTIES_MIAppReplacementState
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
+ _objc_msgSend$_osBuildVersion
+ _objc_msgSend$_sourceAppIdentity
+ _objc_msgSend$_status
+ _objc_msgSend$appLaunchProhibitionURL
+ _objc_msgSend$appReplacementSourceBundleIdentifier
+ _objc_msgSend$appReplacementStateURL
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$displayName
+ _objc_msgSend$getAppReplacementState:withError:
+ _objc_msgSend$getProhibition:forBundleContainerURL:error:
+ _objc_msgSend$getProhibition:fromURL:error:
+ _objc_msgSend$getState:forBundleContainerURL:error:
+ _objc_msgSend$getState:fromURL:error:
+ _objc_msgSend$initWithOSBuildVersion:
+ _objc_msgSend$initWithStatus:sourceAppIdentity:osBuildVersion:
+ _objc_msgSend$initWithUnsignedInteger:
+ _objc_msgSend$osBuildVersion
+ _objc_msgSend$prohibitionURLForBundleContainerURL:
+ _objc_msgSend$removeProhibitionForBundleContainerURL:error:
+ _objc_msgSend$removeStateForBundleContainerURL:error:
+ _objc_msgSend$setAppReplacementSourceBundleIdentifier:
+ _objc_msgSend$sourceAppIdentity
+ _objc_msgSend$stateURLForBundleContainerURL:
+ _objc_msgSend$supersedeExistingContainer:error:
+ _swift_errorRetain
+ _symbolic ______p s5ErrorP
- GCC_except_table48
- GCC_except_table54
CStrings:
+ " osBuildVersion="
+ " with a source app identity to ["
+ " without a source app identity to ["
+ "%@ does not have any app extensions that implement any of the required extension points for its configuration. Based on its configuration, this app must have at least one app extension that implements one of these extension points: %@."
+ "*I"
+ ", osBuildVersion="
+ ", sourceAppIdentity="
+ "-[ICLWorkspace getAppLaunchProhibition:forBundleContainerURL:error:]"
+ "-[ICLWorkspace getAppReplacementState:forBundleContainerURL:error:]"
+ "-[MIBundle hasAtLeastOneExtensionImplementingExtensionPointIn:error:]"
+ "-[MIDataContainer supersedeExistingContainer:error:]"
+ "-[MIGlobalConfiguration OSBuildVersionWithError:]"
+ "24B"
+ "AppLaunchProhibition.plist"
+ "AppReplacementState.plist"
+ "BuildVersion"
+ "Decoded a nil app replacement state from ["
+ "Failed to copy the OS build version"
+ "Failed to decode app launch prohibition from ["
+ "Failed to decode app replacement state from ["
+ "Failed to get app replacement state from %@ : %@"
+ "Failed to read app launch prohibition from ["
+ "Failed to read app replacement state from ["
+ "Failed to remove app launch prohibition at ["
+ "Failed to remove app replacement state at ["
+ "Failed to serialize app launch prohibition ["
+ "Failed to serialize app replacement state for ["
+ "Failed to supersede container %@ with %@"
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
+ "Unknown MIAppReplacementStatus: %lu"
+ "appReplacementSourceBundleIdentifier"
+ "bundleContainerURL parameter was not a valid URL"
+ "com.apple.developer.homekit"
+ "com.apple.developer.superseded-application-identifiers"
+ "sourceAppIdentity"
- "*H"
```
