## DeviceManagement

> `/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement`

```diff

-220.1.1.0.0
-  __TEXT.__text: 0x38718
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x6dd0
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x5079
-  __TEXT.__gcc_except_tab: 0x2c8
-  __TEXT.__oslogstring: 0x1043
+221.2.2.0.0
+  __TEXT.__text: 0x361c0
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x6db0
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x503c
+  __TEXT.__oslogstring: 0xe06
   __TEXT.__ustring: 0xb64
-  __TEXT.__unwind_info: 0xe88
+  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__unwind_info: 0xe60
   __TEXT.__objc_classname: 0x173b
-  __TEXT.__objc_methname: 0x9e4b
-  __TEXT.__objc_methtype: 0xafd
-  __TEXT.__objc_stubs: 0x4fa0
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0xf68
+  __TEXT.__objc_methname: 0x9b1d
+  __TEXT.__objc_methtype: 0xade
+  __TEXT.__objc_stubs: 0x4c20
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0xe18
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d78
+  __DATA_CONST.__objc_selrefs: 0x1cc0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4b8
   __DATA_CONST.__objc_arraydata: 0x680
-  __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x7400
-  __AUTH_CONST.__objc_const: 0x10358
-  __AUTH_CONST.__objc_intobj: 0x1518
+  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__const: 0x480
+  __AUTH_CONST.__cfstring: 0x73a0
+  __AUTH_CONST.__objc_const: 0x10320
+  __AUTH_CONST.__objc_intobj: 0x14b8
   __AUTH_CONST.__objc_arrayobj: 0x858
   __AUTH.__objc_data: 0x3520
-  __DATA.__objc_ivar: 0x8b4
+  __DATA.__objc_ivar: 0x89c
   __DATA.__data: 0x430
-  __DATA.__bss: 0x118
+  __DATA.__bss: 0x158
   __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2246
-  Symbols:   3036
-  CStrings:  3101
+  Functions: 2248
+  Symbols:   3029
+  CStrings:  3061
 
Symbols:
- _CPCopyBundleIdentifierAndTeamFromApplicationIdentifier
- _CTCategoryIdentifierProductivity
- _CTCategoryIdentifierSocialNetworking
- _DMFEffectivePolicyTypeDowntime
- _DMFEffectivePolicyTypeShield
- _OBJC_CLASS_$_LSApplicationRecord
- _OBJC_CLASS_$_NSConditionLock
- ___NSDictionary0__struct
CStrings:
+ "Failed to request communication policies for %!l(MISSING)u bundleIdentifiers with error: %!{(MISSING)public}@"
+ "Failed to request communication policies for %!l(MISSING)u bundleIdentifierswith error: %!{(MISSING)public}@"
+ "Failed to request communication policies with error: %!{(MISSING)public}@"
+ "Failed to request policies for %!l(MISSING)u bundleIdentifiers with error: %!{(MISSING)public}@"
+ "Failed to request policies for %!l(MISSING)u bundleIdentifierswith error: %!{(MISSING)public}@"
+ "Failed to request policies for %!l(MISSING)u categoryIdentifiers with error: %!{(MISSING)public}@"
+ "Failed to request policies for %!l(MISSING)u websiteURLs with error: %!{(MISSING)public}@"
+ "Successfully requested communication policies for %!l(MISSING)u bundleIdentifiers"
+ "Successfully requested policies for %!l(MISSING)u bundleIdentifiers"
+ "Successfully requested policies for %!l(MISSING)u categoryIdentifiers"
+ "Successfully requested policies for %!l(MISSING)u websiteURLs"
+ "requestCommunicationPoliciesForBundleIdentifiers:completionHandler:"
+ "requestCommunicationPoliciesForBundleIdentifiers:replyHandler:"
+ "requestCommunicationPoliciesForBundleIdentifiers:withError:"
+ "requestPoliciesForBundleIdentifiers:replyHandler:"
+ "requestPoliciesForCategoryIdentifiers:replyHandler:"
+ "requestPoliciesForWebsiteURLs:completionHandler:"
+ "requestPoliciesForWebsiteURLs:replyHandler:"
- "%!@(MISSING): %!@(MISSING)"
- "@\"DMFApplicationPolicyMonitor\""
- "Canceling current policy request because a more recent request is in-flight"
- "Failed fetching categories for bundle identifiers with error: %!{(MISSING)public}@"
- "Failed fetching categories for domain URLs with error: %!{(MISSING)public}@"
- "Failed looking up parent bundle identifier for app clip: %!{(MISSING)public}@ with parent application identifier %!{(MISSING)public}@"
- "Failed to request application policies: %!{(MISSING)public}@"
- "No application record for bundle identifier: %!{(MISSING)public}@ with error: %!{(MISSING)public}@"
- "No policies are set, everything is OK"
- "Requested application %!{(MISSING)public}@ failed to categorize parent application %!{(MISSING)public}@"
- "Requested application %!{(MISSING)public}@ has parent applications %!{(MISSING)public}@"
- "Requested application %!{(MISSING)public}@ has policy %!{(MISSING)public}@, associated categories:%!{(MISSING)public}@ associated sites:%!{(MISSING)public}@ equivalent bundle identifiers:%!{(MISSING)public}@"
- "Requested application %!{(MISSING)public}@ is missing categorization"
- "Requested application %!{(MISSING)public}@ is unblockable"
- "Requested application %!{(MISSING)public}@ with associated category %!{(MISSING)public}@ is unblockable"
- "Requested category %!{(MISSING)public}@ has policy %!{(MISSING)public}@"
- "Requested category %!{(MISSING)public}@ is unblockable"
- "Requested website URL does not have a host, marking policy %!{(MISSING)public}@"
- "Requested website with associated bundle identifier %!{(MISSING)public}@ is unblockable"
- "Requested website with associated category %!{(MISSING)public}@ is unblockable"
- "Requested websites policy counts: %!{(MISSING)public}@"
- "T@\"DMFApplicationPolicyMonitor\",R,N,V_applicationPolicyMonitor"
- "_applicationPolicyMonitor"
- "_calculateCommunicationPoliciesWithApplicationPoliciesByBundleIdentifier:categoryEffectivePolicy:applicationCategoryEffectivePolicy:"
- "_categoryForCommunicationBundleIdentifier:"
- "_equivalentCommunicationBundleIdentifiersForCommunicationBundleIdentifier:"
- "_fetchCategoriesForBundleIdentifiers:completionHandler:"
- "_fetchCategoriesForBundleIdentifiers:withError:"
- "_fetchCategoriesIfNeededForWebsiteURLs:response:"
- "_lastRequestDateByBundleIdentifiers"
- "_transformEffectivePoliciesIntoCommunicationPolicies:"
- "_updateWithPoliciesByBundleIdentifier:categoryEffectivePolicy:applicationCategoryEffectivePolicy:"
- "appClipMetadata"
- "applicationPolicyMonitor"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "categoriesForBundleIDs:completionHandler:"
- "categoriesForDomainURLs:completionHandler:"
- "dateWithTimeIntervalSinceNow:"
- "downtime"
- "equivalentBundleIdentifiers"
- "fetchParentBundleIdentifiersForBundleIdentifiers:"
- "host"
- "initWithArray:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithCondition:"
- "isEqualToDate:"
- "lock"
- "lockWhenCondition:beforeDate:"
- "mutableCopy"
- "parentApplicationIdentifiers"
- "setWithObject:"
- "shield"
- "unlock"
- "unlockWithCondition:"
- "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
- "webDomains"

```
