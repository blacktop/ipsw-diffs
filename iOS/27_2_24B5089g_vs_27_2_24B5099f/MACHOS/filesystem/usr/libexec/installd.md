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

-1680.40.8.0.1
-  __TEXT.__text: 0x72d00
-  __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_stubs: 0x9340
-  __TEXT.__objc_methlist: 0x3a24
+1680.40.14.0.0
+  __TEXT.__text: 0x7651c
+  __TEXT.__auth_stubs: 0x1780
+  __TEXT.__objc_stubs: 0x9580
+  __TEXT.__objc_methlist: 0x3c0c
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x19733
-  __TEXT.__objc_classname: 0x6af
-  __TEXT.__objc_methtype: 0x2535
-  __TEXT.__objc_methname: 0xdb77
-  __TEXT.__gcc_except_tab: 0x3eac
-  __TEXT.__oslogstring: 0x14e7
+  __TEXT.__cstring: 0x1a123
+  __TEXT.__objc_classname: 0x70f
+  __TEXT.__objc_methtype: 0x2605
+  __TEXT.__objc_methname: 0xe087
+  __TEXT.__gcc_except_tab: 0x41e4
+  __TEXT.__oslogstring: 0x1687
   __TEXT.__ustring: 0x84
   __TEXT.__swift5_typeref: 0xe6
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__swift5_capture: 0x80
-  __TEXT.__unwind_info: 0x19a0
+  __TEXT.__unwind_info: 0x1a78
   __TEXT.__eh_frame: 0x218
-  __DATA_CONST.__const: 0x1638
-  __DATA_CONST.__cfstring: 0xaac0
-  __DATA_CONST.__objc_classlist: 0x168
+  __DATA_CONST.__const: 0x1750
+  __DATA_CONST.__cfstring: 0xae20
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_intobj: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x670
   __DATA_CONST.__objc_dictobj: 0x1018
-  __DATA_CONST.__auth_got: 0xbc8
-  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__auth_got: 0xbd0
+  __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA.__objc_const: 0x6518
-  __DATA.__objc_selrefs: 0x29d0
-  __DATA.__objc_ivar: 0x2b0
-  __DATA.__objc_data: 0xe90
+  __DATA.__objc_const: 0x67f8
+  __DATA.__objc_selrefs: 0x2a70
+  __DATA.__objc_ivar: 0x2cc
+  __DATA.__objc_data: 0xf30
   __DATA.__data: 0xbf8
   __DATA.__common: 0x10
   __RESTRICT.__restrict: 0x0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1615
-  Symbols:   544
-  CStrings:  4008
+  Functions: 1661
+  Symbols:   545
+  CStrings:  4081
 
Symbols:
+ _MIAppReplacementStatusExpectsSourceAppIdentity
CStrings:
+ "\"%@\" has the \"%@\" entitlement, which names the app's own application identifier \"%@\". An app can only supersede a different app."
+ "%@ is a potential candidate for app replacement; prohibiting its launch"
+ "%s: Encountered unexpected LS operation of class %@ for bundle ID %@ before set app replacement source operation"
+ "%s: Encountered unexpected LS operation of class %@ for bundle ID %@ before set installation hold operation"
+ "%s: Failed to restart set app replacement source operation for %@ -> %@ : %@"
+ "%s: Failed to restart set installation hold operation for %@/%c : %@"
+ "%s: Failed to restart set persona operation for %@/%@ : %@"
+ "-[MIClientConnection endAppReplacementWithStatus:forApp:completion:]"
+ "-[MIClientConnection pushReplacementInfoForApp:replacingApp:withCompletion:]"
+ "-[MIInstallableBundle _setAppLaunchProhibitionWithReplacementRuledOut:error:]"
+ "-[MIInstallableBundle _setAppReplacementStateRulingOutReplacement:error:]"
+ "-[MILaunchServicesOperationManager _onQueue_setAppReplacementSourceBundleID:forBundleID:inDomain:error:]"
+ "-[MILaunchServicesOperationManager _onQueue_setInstallationHold:forBundleID:inDomain:error:]"
+ "-[MILaunchServicesSetAppReplacementSourceOperation initWithCoder:]"
+ "-[MILaunchServicesSetInstallationHoldOperation initWithCoder:]"
+ "<%@: %@:%lu %@/%@/%@>"
+ "<%@: %@:%lu %@/%@/%c>"
+ "@52@0:8@16Q24B32@36Q44"
+ "@56@0:8@16@24Q32@40Q48"
+ "An app cannot replace itself in a request to push app replacement info for %@"
+ "App identity was nil or the wrong type for request to end app replacement"
+ "B36@0:8B16@20^@28"
+ "B44@0:8B16@20Q28^@36"
+ "Cannot end the app replacement of %@ with %@"
+ "Cannot end the app replacement of %@ with %@, which names an app being replaced"
+ "Destination app identity was nil or the wrong type for request to push app replacement info"
+ "Encountered unexpected LS operation of class %@ for bundle ID %@ before set app replacement source operation"
+ "Encountered unexpected LS operation of class %@ for bundle ID %@ before set installation hold operation"
+ "End of app replacement with status %@ requested by client %@ for %@"
+ "Failed to restart set app replacement source operation for %@ -> %@ : %@"
+ "Failed to restart set installation hold operation for %@/%c : %@"
+ "Failed to restart set persona operation for %@/%@ : %@"
+ "Failed to tell LaunchServices about the installation holds left by the failed replacement of %@ by %@ : %@"
+ "Invalid installation domain value when deserializing app replacement source for %@: %lu"
+ "Invalid installation domain value when deserializing installation hold for %@: %lu"
+ "MILaunchServicesSetAppReplacementSourceOperation"
+ "MILaunchServicesSetInstallationHoldOperation"
+ "Missing bundle ID when deserializing installation hold"
+ "Missing destination bundle ID when deserializing app replacement source operation"
+ "Missing source bundle ID when deserializing app replacement source operation"
+ "Push of app replacement info requested by client %@ for %@ replacing %@"
+ "Source app identity was nil or the wrong type for request to push app replacement info for %@"
+ "T@\"NSDictionary\",C,N,V_pendingInstallationHoldsByBundleID"
+ "T@\"NSString\",R,N,V_destinationBundleID"
+ "T@\"NSString\",R,N,V_sourceBundleID"
+ "TB,R,N,V_installationHold"
+ "The app extension at \"%@\" has the \"%@\" entitlement, which names the app extension's own application identifier \"%@\". An app extension can only supersede a different app extension."
+ "_destinationBundleID"
+ "_installationHold"
+ "_launchServicesOperationManagerInstance"
+ "_onQueue_setAppReplacementSourceBundleID:forBundleID:inDomain:error:"
+ "_onQueue_setInstallationHold:forBundleID:inDomain:error:"
+ "_pendingInstallationHoldsByBundleID"
+ "_setAppLaunchProhibitionWithReplacementRuledOut:error:"
+ "_setAppReplacementStateRulingOutReplacement:error:"
+ "_setInstallationHold:forBundleID:error:"
+ "_sourceBundleID"
+ "applyInstallationHoldsWithError:"
+ "destinationBundleID"
+ "endAppReplacementWithStatus:forApp:completion:"
+ "getAppLaunchProhibition:withError:"
+ "initWithBundleID:domain:installationHold:registrationUUID:serialNumber:"
+ "initWithSourceBundleID:destinationBundleID:domain:registrationUUID:serialNumber:"
+ "installationHold"
+ "pendingInstallationHoldsByBundleID"
+ "pushReplacementInfoForApp:replacingApp:withCompletion:"
+ "setAppReplacementSourceBundleID:forBundleID:inDomain:error:"
+ "setAppReplacementSourceBundleIdentifier:forApplicationWithBundleIdentifier:operationUUID:requestContext:saveObserver:error:"
+ "setInstallationHold:forBundleID:inDomain:error:"
+ "setInstallationHoldActive:onApplicationWithBundleIdentifier:operationUUID:requestContext:saveObserver:error:"
+ "setPendingInstallationHoldsByBundleID:"
+ "sourceBundleID"
+ "v40@0:8@\"MIAppIdentity\"16@\"MIAppIdentity\"24@?<v@?@\"NSError\">32"
+ "v40@0:8Q16@\"MIAppIdentity\"24@?<v@?@\"NSError\">32"
+ "v40@0:8Q16@24@?32"
- "-[MIInstallableBundle _setAppReplacementStateWithError:]"
- "_setAppReplacementStateWithError:"
```
