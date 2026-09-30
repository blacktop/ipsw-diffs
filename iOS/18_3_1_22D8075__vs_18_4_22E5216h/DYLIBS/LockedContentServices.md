## LockedContentServices

> `/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices`

```diff

-58.3.1.0.0
-  __TEXT.__text: 0xc264
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x980
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x2e8
-  __TEXT.__oslogstring: 0xcb9
-  __TEXT.__cstring: 0x949
-  __TEXT.__unwind_info: 0x3d0
-  __TEXT.__objc_classname: 0x321
-  __TEXT.__objc_methname: 0x2896
-  __TEXT.__objc_methtype: 0x7e7
-  __TEXT.__objc_stubs: 0x2000
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x4d0
-  __DATA_CONST.__objc_classlist: 0x70
+58.4.9.0.0
+  __TEXT.__text: 0xd5fc
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0xeb4
+  __TEXT.__const: 0xe8
+  __TEXT.__gcc_except_tab: 0x318
+  __TEXT.__oslogstring: 0xde5
+  __TEXT.__cstring: 0xa75
+  __TEXT.__unwind_info: 0x458
+  __TEXT.__objc_classname: 0x344
+  __TEXT.__objc_methname: 0x2d46
+  __TEXT.__objc_methtype: 0x883
+  __TEXT.__objc_stubs: 0x2340
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__const: 0x5b0
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x980
-  __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x2f8
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x3360
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0xf0
+  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_superrefs: 0x68
+  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__objc_const: 0x2e28
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xfc
   __DATA.__data: 0x6c0
-  __DATA.__bss: 0x48
-  __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x20
+  __DATA.__bss: 0x28
+  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 309
-  Symbols:   506
-  CStrings:  700
+  Functions: 347
+  Symbols:   549
+  CStrings:  756
 
Symbols:
+ _LCSCaptureApplicationLaunchTypeSupported
+ _NSStringFromBundleTarget
+ _NSStringFromLCSCaptureApplicationLaunchType
+ _NSStringFromLCSCaptureApplicationLaunchTypeMask
+ _OBJC_CLASS_$_LCSCaptureApplicationLaunchActions
+ _OBJC_CLASS_$_LNConnectionPolicySignals
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$__EXExtensionInstanceIdentifier
+ _OBJC_METACLASS_$_LCSCaptureApplicationLaunchActions
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "%p %@ bundle record for %{public}@ doesn't have %@ entitlement"
+ "%p Failure in retrieving the %@ bundle record for %{public}@: %{public}@; No %@ entitlement found"
+ "%p Failure in retrieving the bundle record for %{public}@: %{public}@; Warm launch is not allowed"
+ "@\"NSSet\"32@0:8Q16Q24"
+ "@32@0:8Q16Q24"
+ "Action metadata found in the action map: %@. Creating a link launch action with preferred bundle identifier: %@"
+ "B16@?0@\"<LCSCaptureApplicationDescribing>\"8"
+ "B24@0:8Q16"
+ "B24@?0@\"NSString\"8@\"<LCSCaptureApplicationDescribing>\"16"
+ "B32@0:8@\"LNSystemProtocol\"16Q24"
+ "B32@0:8@\"NSSet\"16Q24"
+ "B32@0:8@16Q24"
+ "CameraCaptureLaunch"
+ "Capture Application (%@) implements %@: application %{BOOL}u, extension %{BOOL}u"
+ "Clearing cached link actions for %@"
+ "Default Camera Capture Launch, "
+ "Extensions updated for %@ monitoring; Received %lu extensions: %@"
+ "LCSCaptureApplicationLaunchActions"
+ "None"
+ "Prewarming link actions for %@"
+ "T@\"LNAction\",R,N,V_applicationLaunchAction"
+ "T@\"LNAction\",R,N,V_extensionLaunchAction"
+ "TQ,R,N,V_supportedLaunchTypes"
+ "_applicationLaunchAction"
+ "_cachedLinkActionByLaunchIdentifier"
+ "_clearCachedLinkActions"
+ "_extensionLaunchAction"
+ "_filterCaptureApplications:launchType:"
+ "_generateCachedLinkActions"
+ "_hasCaptureAppIntentForExtension:"
+ "_launchActionsForTarget:launchType:"
+ "_lock_captureApplicationsFromKnownExtensions:currentCaptureApplications:"
+ "_lock_knownExtensions"
+ "_lock_supportedLaunchTypesForExtension:"
+ "_queue_knownCameraCaptureApplicationsByBundleIdentifierWithCompletionHandler:"
+ "_queue_launchActionsForType:"
+ "_queue_resolvedLinkActions"
+ "_queue_systemProtocolForLaunchType:"
+ "_resolvedLinkActionForLaunchTarget:launchType:"
+ "_supportedLaunchTypes"
+ "appendString:"
+ "applicationLaunchAction"
+ "captureApplicationProvider:didUpdateKnownCameraCaptureApplications:"
+ "com.apple.LockedContentServices.allowWarmLaunch"
+ "com.apple.camera.lockscreen"
+ "container"
+ "executeQuery:completionHandler:"
+ "extensionLaunchAction"
+ "hasCachedLinkActions"
+ "hasEntitlements:bundleTarget:"
+ "hasExtensionForBundleIdentifier:"
+ "hasImplementedAppIntentProtocol:bundleTarget:"
+ "initWithApplicationLaunchAction:extensionLaunchAction:"
+ "initWithCameraTCCStatus:supportedLaunchTypes:"
+ "initWithExtensionIdentity:instanceIdentifier:"
+ "initWithIdentifier:"
+ "isWarmLaunchAllowedForIdentity:"
+ "knownCameraCaptureApplicationsByBundleIdentifier"
+ "knownCameraCaptureApplicationsByBundleIdentifierWithCompletionHandler:"
+ "knownExtensions"
+ "knownExtensionsWithCompletionHandler:"
+ "launchActionsForTarget:launchType:"
+ "policyWithActionMetadata:signals:"
+ "setPreferredBundleIdentifier:"
+ "sharedInstance"
+ "string"
+ "supportedLaunchTypes"
+ "supportsLaunchType:"
+ "typeName"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"NSSet\"8"
+ "v24@0:8@?<v@?@\"NSDictionary\">16"
+ "v24@0:8@?<v@?@\"NSSet\">16"
- "Action metadata found in the action map: %@. Creating a link launch action"
- "B32@0:8@16@24"
- "Capture Application (%@): appHasCaptureAppIntent %{BOOL}u, extensionHasCaptureAppIntent %{BOOL}u"
- "Clearing cached link action for %@"
- "Extensions updated; Received %lu extensions: %@"
- "Prewarming link action for %@"
- "_cachedLinkAction"
- "_captureApplicationsFromKnownExtensions:currentCaptureApplications:"
- "_clearCachedLinkAction"
- "_generateCachedLinkAction"
- "_hasCaptureAppIntentForBundleIdentifier:extensionBundleIdentifier:"
- "_lock_knownCaptureExtensions"
- "_resolvedLinkAction"
- "hasCachedLinkAction"
- "initWithCameraTCCStatus:"
- "isCaptureExtension:"
- "knownCaptureExtensions"
- "policyWithActionMetadata:"

```
