## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-620.2.4.10.7
-  __TEXT.__text: 0x21568
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x1828
-  __TEXT.__cstring: 0x23cf
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x1100
-  __TEXT.__oslogstring: 0xe66
+621.1.10.20.6
+  __TEXT.__text: 0x21abc
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_methlist: 0x1b5c
+  __TEXT.__cstring: 0x24ad
+  __TEXT.__const: 0x16a
+  __TEXT.__gcc_except_tab: 0x1144
+  __TEXT.__oslogstring: 0xed8
   __TEXT.__dlopen_cstrs: 0x156
   __TEXT.__ustring: 0x1ee
-  __TEXT.__unwind_info: 0xca0
+  __TEXT.__constg_swiftt: 0x60
+  __TEXT.__swift5_typeref: 0x9
+  __TEXT.__swift5_reflstr: 0x1c
+  __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0xca8
   __TEXT.__objc_classname: 0x49c
-  __TEXT.__objc_methname: 0x691a
-  __TEXT.__objc_methtype: 0xa94
-  __TEXT.__objc_stubs: 0x4360
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0xfe8
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__objc_methname: 0x6b21
+  __TEXT.__objc_methtype: 0xaa3
+  __TEXT.__objc_stubs: 0x4420
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0x10d8
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1488
+  __DATA_CONST.__objc_selrefs: 0x1578
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__objc_arraydata: 0x100
+  __AUTH_CONST.__auth_got: 0x3c0
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x1a20
-  __AUTH_CONST.__objc_const: 0x3310
+  __AUTH_CONST.__cfstring: 0x1b00
+  __AUTH_CONST.__objc_const: 0x2e70
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH.__data: 0xb8
   __DATA.__objc_ivar: 0x1a4
   __DATA.__data: 0x380
   __DATA.__bss: 0x98

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 798
-  Symbols:   1138
-  CStrings:  1396
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 819
+  Symbols:   1187
+  CStrings:  1415
 
Symbols:
+ _OBJC_CLASS_$_APApplication
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _SFCredentialProviderCapabilitiesSupportedCredentialExchangeFormatVersions
+ _WBSOngoingSharingGroupIDNone
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retainAutoreleasedReturnValue
+ _swift_bridgeObjectRelease
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
CStrings:
+ "%{sensitive, mask.hash}@ is expired; removing from cache"
+ ".sng.link"
+ "App %{sensitive, mask.hash}@ has web browser entitlement. Checking domain against website URL %{sensitive, mask.hash}@."
+ "Checking domain against associated domains for app %{sensitive, mask.hash}@."
+ "Could not fetch application record for application identifier: %{sensitive, mask.hash}@."
+ "Domain-bound verification code is %@valid for app %{sensitive, mask.hash}@."
+ "Domain-bound verification code is %@valid for frame URLs from web browser: %{sensitive, mask.hash}@"
+ "SupportedCredentialExchangeVersions"
+ "T@\"LSApplicationRecord\",R,C,N"
+ "Verification Code"
+ "_TtC16SafariFoundation39SymbolOfNewBeginningsInSafariFoundation"
+ "_getExtensionsIncludingDisabled:completionHandler:"
+ "_saveAdditionalSitesForSavedAccount:completionHandler:"
+ "_saveCustomTitleForSavedAccount:completionHandler:"
+ "_saveNotesEntryForSavedAccount:completionHandler:"
+ "_saveOneTimeCodeForSavedAccount:completionHandler:"
+ "applicationWithBundleIdentifier:"
+ "com.apple.MobileSMS"
+ "com.apple.mail"
+ "didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:externalProviderConditionalRegistrationRequester:"
+ "extensionSupportedCredentialExchangeFormatVersions:"
+ "getAllExtensionsForContainingApp:completion:"
+ "getAllExtensionsWithCompletion:"
+ "isLocked"
+ "requiresAuthentication"
+ "safari_arrayContainingObjectsOfClass:forKey:"
+ "saveAdditionalSites:forSavedAccount:completionHandler:"
+ "saveCustomTitle:forSavedAccount:completionHandler:"
+ "saveNotesEntry:forSavedAccount:completionHandler:"
+ "saveTOTPGenerator:forSavedAccount:completionHandler:"
+ "saveToKeychainWithCompletionHandler:"
+ "sf_applicationRecordForContainingApp"
+ "v28@0:8B16@?20"
+ "welcomeToTheWorldOfTomorrow"
- "%@ is expired; removing from cache"
- "App %@ has web browser entitlement. Checking domain against website URL %{sensitive, mask.hash}@."
- "Checking domain against associated domains for app %@."
- "Could not fetch application record for application identifier: %{private}@."
- "Domain-bound verification code is %@valid for app %@."
- "Domain-bound verification code is %@valid for frame URLs from web browser: %{private}@"
- "_saveAdditionalSitesForSavedAccount:"
- "_saveCustomTitleForSavedAccount:"
- "_saveNotesEntryForSavedAccount:"
- "_saveOneTimeCodeForSavedAccount:"
- "didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:"
- "didFillExternalCredential:inAppWithBundleIdentifier:"
- "saveAdditionalSites:forSavedAccount:"
- "saveCustomTitle:forSavedAccount:"
- "saveNotesEntry:forSavedAccount:"
- "saveTOTPGenerator:forSavedAccount:"
- "saveToKeychain"

```
