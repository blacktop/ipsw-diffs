## UserSafety

> `/System/Library/PrivateFrameworks/UserSafety.framework/UserSafety`

```diff

-130.4.1.0.0
-  __TEXT.__text: 0x1ac0
-  __TEXT.__auth_stubs: 0x1d0
+145.0.0.0.0
+  __TEXT.__text: 0x1a44
   __TEXT.__objc_methlist: 0x210
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0xed
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0x68
-  __TEXT.__objc_methname: 0x6bd
-  __TEXT.__objc_methtype: 0x1a6
-  __TEXT.__objc_stubs: 0x560
-  __DATA_CONST.__got: 0x90
+  __TEXT.__cstring: 0xf1
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x378
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x18
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 40F2D45E-A40A-3E33-ADE6-479520B40D56
+  UUID: 58CAEC58-CF2E-3CEE-9CAE-CCE7D74E0799
   Functions: 56
-  Symbols:   254
-  CStrings:  105
+  Symbols:   261
+  CStrings:  15
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x4
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"SCMediaAnalysisService\""
- "@\"SCSensitivityAnalysisAvailabilityObserver\""
- "@\"SCSensitivityAnalyzer\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8@16@24"
- "@32@0:8^{__CFString=}16#24"
- "@32@0:8^{__CFString=}16^{__SecTask=}24"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "T@\"SCMediaAnalysisService\",&,N,V_madService"
- "USAnalysisEnablementSubscription"
- "USEntitlements"
- "USLog"
- "USManagedSettingsReader"
- "USSensitivityAnalyzer"
- "_analysisAvailabilityObserver"
- "_dispatchQueue"
- "_isAnalysisEnabled:"
- "_isCommunicationSafetyEnabled:"
- "_isNudityDetectionEnabled:"
- "_isNudityDetectionEnabledForAnyOfServices:scanningPolicy:"
- "_isNudityDetectionEnabledForApplication:scanningPolicy:"
- "_isNudityDetectionEnabledForService:scanningPolicy:"
- "_madService"
- "_scsAnalyzer"
- "_setValueForEntitlement:expectedElementClass:"
- "_valueForEntitlement:expectedClass:"
- "_valueForEntitlement:secTask:"
- "addObject:"
- "analyzeCGImage:orientation:completionHandler:"
- "analyzeCGImage:withOrientation:completionHandler:"
- "analyzeImageFile:completionHandler:"
- "analyzeImageWithLocalIdentifier:fromPhotoLibraryWithURL:completionHandler:"
- "analyzeVideoFile:progressHandler:completionHandler:"
- "analyzeVideoFile:useBlastdoor:progressHandler:completionHandler:"
- "analyzeVideoWithLocalIdentifier:fromPhotoLibraryWithURL:progressHandler:completionHandler:"
- "applications"
- "cancel"
- "containsObject:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "currentInterventionType"
- "currentScanningPolicy"
- "dictionaryWithObjects:forKeys:count:"
- "entitlementsReaderClass"
- "init"
- "initWithBundleIdentifier:"
- "initWithDomain:code:userInfo:"
- "initWithObserver:"
- "initWithQueue:"
- "initWithQueue:madService:"
- "interventionType"
- "isAnalysisEnabled"
- "isCommunicationSafetyEnabled"
- "isNudityDetectionEnabled"
- "isNudityDetectionEnabledForAnyOfServices:"
- "isNudityDetectionEnabledForService:"
- "isSensitive"
- "madService"
- "policy"
- "publisherForGroups:"
- "readCurrentBundleIdentifier"
- "readCurrentServices"
- "scanningPolicy"
- "services"
- "set"
- "setMadService:"
- "setWithObject:"
- "settingsReaderClass"
- "sinkWithReceiveInput:"
- "subscribeForAnalysisAvailabilityChanges:"
- "subscribeForAnalysisEnabledChanges:"
- "subscribeForScanningPolicyChanges:"
- "userSafety"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@?24"
- "v36@0:8^{CGImage=}16I24@?28"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "v44@0:8@16B24@?28@?36"
- "v48@0:8@16@24@?32@?40"

```
