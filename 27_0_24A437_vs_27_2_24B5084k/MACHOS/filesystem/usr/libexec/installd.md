## installd

> `/usr/libexec/installd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1674.2.1.0.0
-  __TEXT.__text: 0x6fa3c
-  __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_stubs: 0x9000
-  __TEXT.__objc_methlist: 0x391c
+1680.40.6.502.1
+  __TEXT.__text: 0x72b3c
+  __TEXT.__auth_stubs: 0x1770
+  __TEXT.__objc_stubs: 0x9340
+  __TEXT.__objc_methlist: 0x3a24
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x18813
-  __TEXT.__objc_classname: 0x69f
-  __TEXT.__objc_methtype: 0x2405
-  __TEXT.__objc_methname: 0xd5c7
-  __TEXT.__gcc_except_tab: 0x3bb0
+  __TEXT.__cstring: 0x19583
+  __TEXT.__objc_classname: 0x6af
+  __TEXT.__objc_methtype: 0x2535
+  __TEXT.__objc_methname: 0xdb77
+  __TEXT.__gcc_except_tab: 0x3eac
   __TEXT.__oslogstring: 0x14e7
   __TEXT.__ustring: 0x84
   __TEXT.__swift5_typeref: 0xe6

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__swift5_capture: 0x80
-  __TEXT.__unwind_info: 0x1930
+  __TEXT.__unwind_info: 0x19a0
   __TEXT.__eh_frame: 0x218
-  __DATA_CONST.__const: 0x1610
-  __DATA_CONST.__cfstring: 0xa600
-  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__const: 0x1638
+  __DATA_CONST.__cfstring: 0xaa60
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_intobj: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x670
   __DATA_CONST.__objc_dictobj: 0x1018
-  __DATA_CONST.__auth_got: 0xbc0
-  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__auth_got: 0xbc8
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA.__objc_const: 0x6348
-  __DATA.__objc_selrefs: 0x28e0
-  __DATA.__objc_ivar: 0x2a4
-  __DATA.__objc_data: 0xe40
+  __DATA.__objc_const: 0x6518
+  __DATA.__objc_selrefs: 0x29d0
+  __DATA.__objc_ivar: 0x2b0
+  __DATA.__objc_data: 0xe90
   __DATA.__data: 0xbf8
   __DATA.__common: 0x10
   __RESTRICT.__restrict: 0x0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1593
-  Symbols:   538
-  CStrings:  3915
+  Functions: 1615
+  Symbols:   544
+  CStrings:  4005
 
Symbols:
+ _MIAppReplacementMinimumBuildVersion
+ _MIIsRecordableAppReplacementStatus
+ _MIStringForAppReplacementStatus
+ _OBJC_CLASS_$_MIAppLaunchProhibition
+ _OBJC_CLASS_$_MIAppReplacementState
+ _OBJC_CLASS_$_NSNull
+ ___NSDictionary0__struct
- _MGCopyAnswer
CStrings:
+ "\"%@\" has the entitlement \"%@\" = TRUE which is not allowed for this type of app."
+ "%@ cannot replace another app because it does not have a valid \"%@\" entitlement"
+ "%@ has no data container left to hand over to %@, so its replacement is being resumed"
+ "%@ has no data container left to hand over to its replacement, so its replacement is being resumed"
+ "%@ is being restored from a backup, marking app replacement as not applicable"
+ "-[MIAppReplacementOperation _bestEffortDiscardPreparationForReplacingApp:appBeingReplaced:]"
+ "-[MIAppReplacementOperation _getDataContainer:forExtensionBundle:parentPersona:allowingAbsentContainer:error:]"
+ "-[MIAppReplacementOperation prepareWithError:]"
+ "-[MIAppReplacementOperation prepareWithError:]_block_invoke"
+ "-[MIClientConnection prepareReplacementOfApp:byApp:extensionBundleIDs:withCompletion:]"
+ "-[MIClientConnection removeAppReplacementStateForApp:completion:]"
+ "-[MIClientConnection setAppReplacementStatus:forApp:replacingApp:completion:]"
+ "-[MIClientConnection setLaunchProhibited:forApp:withCompletion:]"
+ "-[MIInstallableBundle _performAppExtensionValidationForAppBundleSigningInfo:validatingResources:allowFreeProfileValidation:error:]"
+ "-[MIInstallableBundle _setAppReplacementStateWithError:]"
+ "ALLOWED"
+ "App %@ cannot replace itself"
+ "App Clip contains a DriverKit extension. This is not allowed."
+ "App Clip contains an embedded watch app. This is not allowed."
+ "App identity was nil or the wrong type for request to prepare an app replacement"
+ "App identity was nil or the wrong type for request to remove app replacement state"
+ "App identity was nil or the wrong type for request to set app replacement status"
+ "App identity was nil or the wrong type for request to set the app launch prohibition"
+ "B40@0:8@16B24B28^@32"
+ "B52@0:8^@16@24@32B40^@44"
+ "Cannot set the app replacement status of %@ to %@"
+ "Could not find an app bundle in the bundle container for %@"
+ "Expected source app %@ to be associated with the same persona as destination app %@"
+ "Expected to find only one container in persona %@ for %@; app replacement doesn't support SYSTEM/ANY persona extensions"
+ "Extension %@ cannot replace itself in the replacement of %@ by %@"
+ "Extension bundle IDs contained an entry that was not a pair of non-empty strings for request to prepare the replacement of %@ by %@"
+ "Extension bundle IDs were the wrong type for request to prepare the replacement of %@ by %@"
+ "Failed to allow launch again at %@ after preparing the replacement of %@ by %@ failed: %@"
+ "Failed to discard the app replacement state at %@ after preparing the replacement of %@ by %@ failed: %@"
+ "MIAppReplacementOperation"
+ "Not handing any data container over to %@ in %@, because %@ has no extension %@"
+ "Not handing the data container of %@ in %@ over to anything, because %@ has no extension %@"
+ "OSBuildVersionWithError:"
+ "PROHIBITED"
+ "Preparation of app replacement requested by client %@ for %@ replacing %@, carrying %lu extensions"
+ "PrepareAppReplacement"
+ "Previous install for %@ has no recorded build version, treating it as predating app replacement"
+ "Previous install for %@ on %@ predates app replacement (%@), marking it as not applicable"
+ "Removal of app replacement state requested by client %@ for %@"
+ "RemoveAppReplacementState"
+ "Set app launch prohibition to %@ requested by client %@ for %@"
+ "Set app replacement status to %@ requested by client %@ for %@ replacing %@"
+ "SetAppLaunchProhibited"
+ "SetAppReplacementStatus"
+ "Source app identity was nil or the wrong type for request to prepare an app replacement for %@"
+ "Source app identity was the wrong type for request to set app replacement status for %@"
+ "T@\"MIAppIdentity\",R,N,V_appIdentity"
+ "T@\"MIAppIdentity\",R,N,V_sourceAppIdentity"
+ "T@\"NSDictionary\",R,N,V_extensionBundleIDsBySourceExtensionBundleID"
+ "The XPCService at \"%@\" has the \"%@\" entitlement, which is not allowed on an XPCService."
+ "_appIdentity"
+ "_bestEffortDiscardPreparationForReplacingApp:appBeingReplaced:"
+ "_bundleContainerForIdentity:error:"
+ "_deviceHasPersonas"
+ "_extensionBundleIDsBySourceExtensionBundleID"
+ "_extensionBundleWithBundleID:fromExtensionBundles:"
+ "_getDataContainer:forExtensionBundle:parentPersona:allowingAbsentContainer:error:"
+ "_performAppExtensionValidationForAppBundleSigningInfo:validatingResources:allowFreeProfileValidation:error:"
+ "_setAppReplacementStateWithError:"
+ "_sourceAppIdentity"
+ "appIdentity"
+ "appLaunchProhibitionURL"
+ "appReplacementStateURL"
+ "com.apple.developer.homekit"
+ "com.apple.developer.superseded-application-identifiers"
+ "dataContainerForPersona:error:"
+ "extensionBundleIDsBySourceExtensionBundleID"
+ "getAppReplacementState:withError:"
+ "initWithAppIdentity:replacingAppWithIdentity:extensionBundleIDs:"
+ "initWithOSBuildVersion:"
+ "initWithStatus:sourceAppIdentity:osBuildVersion:"
+ "installBuildVersion"
+ "null"
+ "prepareReplacementOfApp:byApp:extensionBundleIDs:withCompletion:"
+ "prepareWithError:"
+ "removeAppLaunchProhibitionWithError:"
+ "removeAppReplacementStateForApp:completion:"
+ "removeAppReplacementStateWithError:"
+ "saveAppLaunchProhibition:withError:"
+ "saveAppReplacementState:withError:"
+ "setAppReplacementStatus:forApp:replacingApp:completion:"
+ "setLaunchProhibited:forApp:withCompletion:"
+ "sourceAppIdentity"
+ "supersedeExistingContainer:error:"
+ "v32@0:8@\"MIAppIdentity\"16@?<v@?@\"NSError\">24"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "v36@0:8B16@\"MIAppIdentity\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v48@0:8@\"MIAppIdentity\"16@\"MIAppIdentity\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
+ "v48@0:8Q16@\"MIAppIdentity\"24@\"MIAppIdentity\"32@?<v@?@\"NSError\">40"
- "App clip contains a DriverKit bundle"
- "App clip contains an embedded watch app"
- "BuildVersion"
- "Failed to copy build version for %@"
- "The XPCService extension at \"%@\" has the \"%@\" entitlement, which is not allowed on an XPCService."
```
