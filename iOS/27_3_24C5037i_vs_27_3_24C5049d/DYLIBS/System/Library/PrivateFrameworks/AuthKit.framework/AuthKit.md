## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-560.250.3.0.0
-  __TEXT.__text: 0x1ab144
-  __TEXT.__objc_methlist: 0x10ca4
+560.250.6.1.0
+  __TEXT.__text: 0x1ab758
+  __TEXT.__objc_methlist: 0x10ccc
   __TEXT.__const: 0xd40
-  __TEXT.__cstring: 0x137b0
-  __TEXT.__oslogstring: 0x16719
+  __TEXT.__cstring: 0x137b7
+  __TEXT.__oslogstring: 0x167ee
   __TEXT.__gcc_except_tab: 0x67c4
   __TEXT.__dlopen_cstrs: 0x267
   __TEXT.__ustring: 0x3be
-  __TEXT.__unwind_info: 0x7168
+  __TEXT.__unwind_info: 0x7180
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x84a8
+  __DATA_CONST.__objc_selrefs: 0x84d0
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x358
-  __DATA_CONST.__got: 0xbd8
-  __AUTH_CONST.__const: 0x1440
+  __DATA_CONST.__got: 0xbe0
+  __AUTH_CONST.__const: 0x1460
   __AUTH_CONST.__cfstring: 0x14920
-  __AUTH_CONST.__objc_const: 0x30218
+  __AUTH_CONST.__objc_const: 0x30240
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
+  - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6255
-  Symbols:   12634
-  CStrings:  4764
+  Functions: 6260
+  Symbols:   12643
+  CStrings:  4768
 
Symbols:
+ -[AKDevice isAuthenticatedGuestMode]
+ -[AKDevice isSharedIPad]
+ -[AKDevice supportsSharedIPadPasscodeAuth]
+ -[NSMutableURLRequest(AuthKit) ak_addAuthenticatedGuestModeHeader]
+ GCC_except_table149
+ GCC_except_table161
+ GCC_except_table165
+ GCC_except_table167
+ _AKApprovalFlowErrorIsEndWithoutFailure
+ _AKOSEDomainFirstPartyAppConsentRequired
+ _OBJC_CLASS_$_DMCMultiUserModeUtilities
+ __AKHTTPHeaderMultiUserGuestMode
+ ___24-[AKDevice isSharedIPad]_block_invoke
+ ___36-[AKDevice isAuthenticatedGuestMode]_block_invoke
+ _isAuthenticatedGuestMode.isAuthenticatedGuestMode
+ _isAuthenticatedGuestMode.onceToken
+ _isSharedIPad.isSharedIPad
+ _isSharedIPad.onceToken
+ _kAKFirstPartyAppConsentRequiredDomain
- -[AKDevice isMultiUserMode]
- GCC_except_table156
- GCC_except_table158
- GCC_except_table160
- GCC_except_table162
- ___27-[AKDevice isMultiUserMode]_block_invoke
- _isMultiUserMode.isMultiUserMode
- _isMultiUserMode.onceToken
- _kAKAnalyticsEventCodeDisplayedWithInvisibleInk
- _kAKAnalyticsEventInvisibleInkRemovedFromCode
CStrings:
+ "FIRST_PARTY_APP_CONSENT_REQUIRED"
+ "No area IDs found for domain %@ (%llu), falling back to age assurance region"
+ "No area IDs or age assurance region found for domain %@ (%llu)"
+ "OS_ELIGIBILITY_CONTEXT_AGE_ASSURANCE_REGION"
+ "Updating delegate heartbeat token failed: key not found in results"
+ "Updating delegate heartbeat token succeeded."
+ "X-Apple-I-MU-Guest-Mode"
- "No area IDs found for domain %@ (%llu)"
- "com.apple.authkit.codeDisplayedWithinvisibleInk"
- "com.apple.authkit.invisibleInkRemovedFromCode"
```
