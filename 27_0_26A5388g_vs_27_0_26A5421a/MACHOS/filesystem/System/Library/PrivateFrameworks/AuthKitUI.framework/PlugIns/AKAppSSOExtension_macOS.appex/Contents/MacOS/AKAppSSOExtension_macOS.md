## AKAppSSOExtension_macOS

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension_macOS.appex/Contents/MacOS/AKAppSSOExtension_macOS`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x11af8
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x5ec
+559.0.0.0.0
+  __TEXT.__text: 0x141b4
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_stubs: 0x1b60
+  __TEXT.__objc_methlist: 0x6ac
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x4674
-  __TEXT.__objc_methname: 0x1b1b
-  __TEXT.__oslogstring: 0xd14
-  __TEXT.__objc_classname: 0xe9
-  __TEXT.__objc_methtype: 0x2e4
+  __TEXT.__cstring: 0x4724
+  __TEXT.__objc_classname: 0x165
+  __TEXT.__objc_methname: 0x1ea0
+  __TEXT.__objc_methtype: 0x38e
+  __TEXT.__oslogstring: 0x10e6
   __TEXT.__gcc_except_tab: 0x408
   __TEXT.__dlopen_cstrs: 0x21
-  __TEXT.__unwind_info: 0x1a0
-  __DATA_CONST.__const: 0x898
-  __DATA_CONST.__cfstring: 0x2740
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x18
+  __TEXT.__unwind_info: 0x1a8
+  __DATA_CONST.__const: 0x968
+  __DATA_CONST.__cfstring: 0x2780
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x1018
   __DATA_CONST.__objc_dictobj: 0xc30
   __DATA_CONST.__objc_arrayobj: 0x288
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x1a8
-  __DATA.__objc_const: 0x850
-  __DATA.__objc_selrefs: 0x818
-  __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x120
+  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x1e0
+  __DATA.__objc_const: 0x1048
+  __DATA.__objc_selrefs: 0x938
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x58
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AAAFoundation.framework/Versions/A/AAAFoundation
   - /System/Library/PrivateFrameworks/AppSSO.framework/Versions/A/AppSSO
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/AuthKitUI
+  - /System/Library/PrivateFrameworks/SharedWebCredentials.framework/Versions/A/SharedWebCredentials
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/URLFormatting.framework/Versions/A/URLFormatting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 165
-  Symbols:   189
-  CStrings:  699
+  Functions: 180
+  Symbols:   209
+  CStrings:  766
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFRelease
+ _OBJC_CLASS_$_AKBrowserEntitlementChecker
+ _OBJC_CLASS_$_AKRedirectDomainOwnershipChecker
+ _OBJC_CLASS_$_AKSiwACallerInfo
+ _OBJC_CLASS_$__SWCServiceDetails
+ _OBJC_CLASS_$__SWCServiceSpecifier
+ _OBJC_METACLASS_$_AKBrowserEntitlementChecker
+ _OBJC_METACLASS_$_AKRedirectDomainOwnershipChecker
+ _SOAuthorizationOptionInitiatingAction
+ _SOAuthorizationOptionUserActionInitiated
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ __SWCServiceTypeAuthServices
+ ___memcpy_chk
+ _kCFAllocatorDefault
+ _objc_opt_new
+ _objc_opt_respondsToSelector
CStrings:
+ "@48@0:8{?=[8I]}16"
+ "AKBrowserEntitlementChecker"
+ "AKBrowserEntitlementChecking"
+ "AKRedirectDomainOwnershipChecker"
+ "AKRedirectDomainOwnershipChecking"
+ "B24@0:8@\"NSString\"16"
+ "B32@0:8@16^{?=[8I]}24"
+ "Caller is not entitled for first party origin. Authorization request not handled."
+ "Caller is not entitled for first party redirect. Authorization request not handled."
+ "Caller is not entitled for third-party redirect. Authorization request not handled."
+ "Caller is valid and owns the redirect domain."
+ "Caller owns redirect domain via swcd-verified association."
+ "Entitlement %@ is not present"
+ "Error while waiting for site approval: %@"
+ "Missing audit token for third-party redirect. Authorization request not handled."
+ "No approved or pending association for caller; redirect-domain ownership denied."
+ "Process hasEntitlement to %@: %@"
+ "Redirect-domain association is not yet approved; waiting for swcd to resolve its site approval."
+ "SecTaskCopyValueForEntitlement failed for %@, error: %@"
+ "SecTaskCreateWithAuditToken failed for entitlement %@"
+ "Server has disabled the entitlement checks for first party URLs. Proceeding."
+ "Unexpected size of auditToken: %u"
+ "_applicationIdentifierForTeamID:bundleID:"
+ "_auditToken"
+ "_auditTokenFromData:auditToken:"
+ "_canProcessRequestForFirstParty:"
+ "_hasBrowserEntitlement:"
+ "_isFirstPartyRedirectURL:"
+ "_proceedWithClassificationForRequest:"
+ "auditTokenData"
+ "bytes"
+ "callerTeamIdentifier"
+ "com.apple.authentication-services.allow-authentication-request-any-rpid"
+ "com.apple.developer.web-browser.public-key-credential"
+ "hasEntitlement:"
+ "initWithAuditToken:"
+ "initWithServiceType:applicationIdentifier:domain:"
+ "isApproved"
+ "isCallerManaged"
+ "isFirstPartyURLEntitlementCheckDisabled"
+ "localizedCallerDisplayName"
+ "logCaller:"
+ "serviceDetailsWithServiceSpecifier:limit:auditToken:error:"
+ "setBundleID:"
+ "setDisplayName:"
+ "setEntitlementCheckDisabled:"
+ "setFrameID:"
+ "setHasBrowserEntitlement:"
+ "setInitiatingAction:"
+ "setIsManaged:"
+ "setRedirectURI:"
+ "setResponseMode:"
+ "setResponseType:"
+ "setScope:"
+ "setTeamID:"
+ "setUrlParamOrigin:"
+ "setUserActionInitiated:"
+ "setWebKitOrigin:"
+ "siteApprovalState"
+ "swcd service-details lookup failed: %@"
+ "v12@?0B8"
+ "v24@?0@\"_SWCServiceDetails\"8@\"NSError\"16"
+ "v80@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32{?=[8I]}40@?<v@?B>72"
+ "v80@0:8@16@24@32{?=[8I]}40@?72"
+ "verifyOwnershipOfRedirectURL:callerTeamID:callerBundleID:auditToken:completion:"
+ "waitForSiteApprovalWithCompletionHandler:"
+ "{?=\"val\"[8I]}"
```
