## AKAppSSOExtension_macOS

> `System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension_macOS.appex/Contents/MacOS/AKAppSSOExtension_macOS`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`

```diff

-525.600.9.0.0
-  __TEXT.__text: 0xb468
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_stubs: 0x1180
-  __TEXT.__objc_methlist: 0x4d4
+525.600.11.0.0
+  __TEXT.__text: 0xd7e0
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x13e0
+  __TEXT.__objc_methlist: 0x594
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x4248
-  __TEXT.__objc_classname: 0x8f
-  __TEXT.__objc_methname: 0x13fe
-  __TEXT.__objc_methtype: 0x167
+  __TEXT.__cstring: 0x42f8
+  __TEXT.__objc_classname: 0x10b
+  __TEXT.__objc_methname: 0x1651
+  __TEXT.__objc_methtype: 0x211
   __TEXT.__gcc_except_tab: 0x49c
   __TEXT.__dlopen_cstrs: 0x21
-  __TEXT.__oslogstring: 0x751
-  __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x130
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x550
-  __DATA_CONST.__cfstring: 0x2520
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__oslogstring: 0xb23
+  __TEXT.__unwind_info: 0x150
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__cfstring: 0x2560
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arraydata: 0xee0
   __DATA_CONST.__objc_dictobj: 0xb90
   __DATA_CONST.__objc_arrayobj: 0x258
-  __DATA.__objc_const: 0x358
-  __DATA.__objc_selrefs: 0x6a0
-  __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0xc0
+  __DATA.__objc_const: 0xb50
+  __DATA.__objc_selrefs: 0x738
+  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x180
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
-  Functions: 107
-  Symbols:   163
-  CStrings:  588
+  Functions: 125
+  Symbols:   183
+  CStrings:  638
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFRelease
+ _OBJC_CLASS_$_AKBrowserEntitlementChecker
+ _OBJC_CLASS_$_AKRedirectDomainOwnershipChecker
+ _OBJC_CLASS_$_AKURLBag
+ _OBJC_CLASS_$__SWCServiceDetails
+ _OBJC_CLASS_$__SWCServiceSpecifier
+ _OBJC_METACLASS_$_AKBrowserEntitlementChecker
+ _OBJC_METACLASS_$_AKRedirectDomainOwnershipChecker
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ __SWCServiceTypeAuthServices
+ ___memcpy_chk
+ __dispatch_main_q
+ _dispatch_async
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
+ "isFirstPartyURLEntitlementCheckDisabled"
+ "serviceDetailsWithServiceSpecifier:limit:auditToken:error:"
+ "sharedBag"
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
