## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-619.1.22.4.0
-  __TEXT.__text: 0xc0c9c
+619.1.26.20.1
+  __TEXT.__text: 0xc1ce8
   __TEXT.__auth_stubs: 0x1dc0
-  __TEXT.__objc_methlist: 0x8cf4
+  __TEXT.__objc_methlist: 0x8d8c
   __TEXT.__const: 0x60a
-  __TEXT.__gcc_except_tab: 0x5868
-  __TEXT.__cstring: 0xf2b5
+  __TEXT.__gcc_except_tab: 0x5954
+  __TEXT.__cstring: 0xf415
   __TEXT.__ustring: 0x2a2e
-  __TEXT.__oslogstring: 0x87fb
+  __TEXT.__oslogstring: 0x8a3b
   __TEXT.__dlopen_cstrs: 0xf3
-  __TEXT.__swift5_typeref: 0x2bd
-  __TEXT.__swift5_capture: 0x134
+  __TEXT.__swift5_typeref: 0x2bb
+  __TEXT.__swift5_capture: 0x1ac
   __TEXT.__constg_swiftt: 0xd0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0xce

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x4518
-  __TEXT.__eh_frame: 0x598
+  __TEXT.__unwind_info: 0x4568
+  __TEXT.__eh_frame: 0x5d0
   __TEXT.__objc_classname: 0x153a
-  __TEXT.__objc_methname: 0x1ead5
-  __TEXT.__objc_methtype: 0x3292
-  __TEXT.__objc_stubs: 0xf660
-  __DATA_CONST.__got: 0xa58
-  __DATA_CONST.__const: 0x43e8
+  __TEXT.__objc_methname: 0x1ecf5
+  __TEXT.__objc_methtype: 0x3311
+  __TEXT.__objc_stubs: 0xf6e0
+  __DATA_CONST.__got: 0xa60
+  __DATA_CONST.__const: 0x4428
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x150
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b98
+  __DATA_CONST.__objc_selrefs: 0x5c00
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x3b8
   __DATA_CONST.__objc_arraydata: 0x2a78
   __AUTH_CONST.__auth_got: 0xef8
   __AUTH_CONST.__auth_ptr: 0xf0
-  __AUTH_CONST.__const: 0x22f8
-  __AUTH_CONST.__cfstring: 0x172c0
-  __AUTH_CONST.__objc_const: 0xfc70
+  __AUTH_CONST.__const: 0x2448
+  __AUTH_CONST.__cfstring: 0x17400
+  __AUTH_CONST.__objc_const: 0xfcf0
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x630
-  __AUTH.__objc_data: 0x19b8
+  __AUTH.__objc_data: 0x428
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x910
-  __DATA.__data: 0xd28
-  __DATA.__bss: 0x760
+  __DATA.__data: 0xd58
+  __DATA.__bss: 0x780
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x14c8
+  __DATA_DIRTY.__objc_data: 0x2a58
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x3c0
+  __DATA_DIRTY.__bss: 0x3d0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4643
-  Symbols:   5617
-  CStrings:  8260
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4669
+  Symbols:   5652
+  CStrings:  8297
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _kLXLexiconEnumerateCachedOnlyOTAPaths
CStrings:
+ "Background task assertion expired while performing reasons: %!{(MISSING)public}@"
+ "Background task assertion was released by a prior item in the queue"
+ "Beginning new task assertion with reason: %!{(MISSING)public}@"
+ "Continuing background task assertion with reasons %!{(MISSING)public}@"
+ "Could not begin background task"
+ "Could not begin new background task to replace existing background task"
+ "DebugEnableScribble"
+ "DebugScribbleRequiresVisualSimilarity"
+ "Did begin task assertion with reason %!{(MISSING)public}@"
+ "Ending background task assertion"
+ "Ending task assertion with reason %!{(MISSING)public}@"
+ "Interrupting previous coalesced task assertion to be replaced with existing reasons: %!{(MISSING)public}@"
+ "Passkey sidecar fetching: SecItemCopyMatching failed to fetch sidecar items in access group %!{(MISSING)public}@, result %!i(MISSING)"
+ "Passkey sidecar fetching: no sidecar items found in access group %!{(MISSING)public}@"
+ "PasswordEvaluationResults"
+ "SuddenTerminationDisabler"
+ "_safari_personalSidecarDictionaryForPasskeyWithUserHandle:relyingPartyID:groupID:"
+ "_scoreForSavedAccount:issueTypes:topFraudTargets:"
+ "_scoreWarnings:topFraudTargets:"
+ "_scoredWarningForSavedAccount:topFraudTargets:breachResultRecord:"
+ "chagesMade"
+ "com.apple.Safari.Scribble.didCancelScribble"
+ "com.apple.Safari.Scribble.didClearScribble"
+ "com.apple.Safari.Scribble.didFinishScribble"
+ "com.apple.Safari.Scribble.didHideMoreItems"
+ "com.apple.Safari.Scribble.didToggleScribble"
+ "com.apple.Safari.Scribble.reportNumberOfWebsitesWithScribbleActive"
+ "didCancelScribbleSBA"
+ "didClearScribbleSBA"
+ "didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:"
+ "didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:"
+ "didFinishScribbleSBA:"
+ "didHideMoreItemsSBA"
+ "didToggleScribbleSBA"
+ "isOrigin:relatedToRelyingPartyIdentifier:completionHandler:"
+ "isScribbleEnabled"
+ "q40@0:8@16Q24@32"
+ "reportNumberOfWebsitesWithScribbleActiveSBA:"
+ "safari_setLastUsedDate:forPasskeyWithUserHandle:relyingPartyID:groupID:context:"
+ "scribbleRequiresVisualSimilarity"
+ "syncScribbleFeedbackUp:withCompletion:"
+ "uniqueIdentifierForPasswordManagerLegacy"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B>32"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40"
+ "v56@0:8@16@24@32@40@48"
+ "websites"
+ "wev"
- "@48@0:8@16@24q32@40"
- "Background task assertion expired while performing reasons: %!@(MISSING)"
- "Passkey custom title fetching: SecItemCopyMatching failed to fetch sidecar items in access group %!{(MISSING)public}@, result %!i(MISSING)"
- "Passkey custom title fetching: no sidecar items found in access group %!{(MISSING)public}@"
- "_scoreForSavedAccount:issueTypes:topFraudTargets:contextKitCategories:"
- "_scoreWarnings:contextKitCategoryMap:topFraudTargets:"
- "_scoredWarningForSavedAccount:topFraudTargets:contextKitCategories:breachResultRecord:"
- "didFillCredentialForUsername:inAppWithBundleIdentifier:"
- "q48@0:8@16Q24@32q40"
- "uniqueIdentifierForPasswordManager"
- "v32@0:8@\"NSString\"16@\"NSString\"24"

```
