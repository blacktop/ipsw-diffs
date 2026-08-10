## AKAppSSOExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x11018
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_stubs: 0x1800
-  __TEXT.__objc_methlist: 0x5d4
+559.0.0.0.0
+  __TEXT.__text: 0x12278
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__objc_stubs: 0x1960
+  __TEXT.__objc_methlist: 0x66c
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x4578
-  __TEXT.__objc_methname: 0x1b95
-  __TEXT.__oslogstring: 0xe16
-  __TEXT.__objc_classname: 0xe9
-  __TEXT.__objc_methtype: 0x303
+  __TEXT.__cstring: 0x4628
+  __TEXT.__objc_classname: 0x165
+  __TEXT.__objc_methname: 0x1d20
+  __TEXT.__objc_methtype: 0x382
+  __TEXT.__oslogstring: 0x1026
   __TEXT.__gcc_except_tab: 0x408
   __TEXT.__dlopen_cstrs: 0x21
   __TEXT.__unwind_info: 0x190
-  __DATA_CONST.__const: 0x6e8
-  __DATA_CONST.__cfstring: 0x2680
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__const: 0x798
+  __DATA_CONST.__cfstring: 0x26c0
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x1018
   __DATA_CONST.__objc_dictobj: 0xc30
   __DATA_CONST.__objc_arrayobj: 0x288
-  __DATA_CONST.__auth_got: 0x180
-  __DATA_CONST.__got: 0x1b8
-  __DATA.__objc_const: 0x7d8
-  __DATA.__objc_selrefs: 0x860
-  __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x130
+  __DATA_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x1d0
+  __DATA.__objc_const: 0xfd0
+  __DATA.__objc_selrefs: 0x8b8
+  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x1f0
   __DATA.__bss: 0x58
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
+  - /System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 133
-  Symbols:   194
-  CStrings:  705
+  Functions: 143
+  Symbols:   202
+  CStrings:  737
 
Symbols:
+ _OBJC_CLASS_$_AKBrowserEntitlementChecker
+ _OBJC_CLASS_$_AKRedirectDomainOwnershipChecker
+ _OBJC_CLASS_$__SWCServiceDetails
+ _OBJC_CLASS_$__SWCServiceSpecifier
+ _OBJC_METACLASS_$_AKBrowserEntitlementChecker
+ _OBJC_METACLASS_$_AKRedirectDomainOwnershipChecker
+ __SWCServiceTypeAuthServices
+ _objc_opt_new
CStrings:
+ "@48@0:8{?=[8I]}16"
+ "AKBrowserEntitlementChecker"
+ "AKBrowserEntitlementChecking"
+ "AKRedirectDomainOwnershipChecker"
+ "AKRedirectDomainOwnershipChecking"
+ "B24@0:8@\"NSString\"16"
+ "Caller is not entitled for third-party redirect. Authorization request not handled."
+ "Caller is valid and owns the redirect domain."
+ "Caller owns redirect domain via swcd-verified association."
+ "Error while waiting for site approval: %@"
+ "Missing audit token for third-party redirect. Authorization request not handled."
+ "No approved or pending association for caller; redirect-domain ownership denied."
+ "Redirect-domain association is not yet approved; waiting for swcd to resolve its site approval."
+ "_applicationIdentifierForTeamID:bundleID:"
+ "_auditToken"
+ "_hasBrowserEntitlement:"
+ "_isFirstPartyRedirectURL:"
+ "_proceedWithClassificationForRequest:"
+ "com.apple.authentication-services.allow-authentication-request-any-rpid"
+ "com.apple.developer.web-browser.public-key-credential"
+ "hasEntitlement:"
+ "initWithAuditToken:"
+ "initWithServiceType:applicationIdentifier:domain:"
+ "isApproved"
+ "serviceDetailsWithServiceSpecifier:limit:auditToken:error:"
+ "siteApprovalState"
+ "swcd service-details lookup failed: %@"
+ "v12@?0B8"
+ "v24@?0@\"_SWCServiceDetails\"8@\"NSError\"16"
+ "v80@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32{?=[8I]}40@?<v@?B>72"
+ "v80@0:8@16@24@32{?=[8I]}40@?72"
+ "verifyOwnershipOfRedirectURL:callerTeamID:callerBundleID:auditToken:completion:"
+ "waitForSiteApprovalWithCompletionHandler:"
+ "{?=\"val\"[8I]}"
- "B56@0:8{?=[8I]}16@48"
- "checkEntitlementForAuditToken:entitlement:"
```
