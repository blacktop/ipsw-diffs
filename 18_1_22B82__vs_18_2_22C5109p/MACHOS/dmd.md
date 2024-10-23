## dmd

> `/usr/libexec/dmd`

```diff

-220.1.1.0.0
-  __TEXT.__text: 0x7e9dc
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_stubs: 0xe460
-  __TEXT.__objc_methlist: 0x6ef4
+221.2.2.0.0
+  __TEXT.__text: 0x82c68
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_stubs: 0xe860
+  __TEXT.__objc_methlist: 0x6fec
   __TEXT.__const: 0x150
-  __TEXT.__objc_classname: 0x1e1e
-  __TEXT.__objc_methname: 0x1105f
-  __TEXT.__objc_methtype: 0x1d43
-  __TEXT.__cstring: 0x52fe
-  __TEXT.__oslogstring: 0xa72f
-  __TEXT.__gcc_except_tab: 0xdcc
+  __TEXT.__objc_classname: 0x1e1b
+  __TEXT.__objc_methname: 0x116fe
+  __TEXT.__objc_methtype: 0x1d57
+  __TEXT.__cstring: 0x5300
+  __TEXT.__oslogstring: 0xad0c
+  __TEXT.__gcc_except_tab: 0xe78
   __TEXT.__ustring: 0x810
   __TEXT.__dlopen_cstrs: 0xaf
-  __TEXT.__unwind_info: 0x1e28
-  __DATA_CONST.__auth_got: 0x770
-  __DATA_CONST.__got: 0x12c0
-  __DATA_CONST.__const: 0x2690
+  __TEXT.__unwind_info: 0x1ea8
+  __DATA_CONST.__auth_got: 0x780
+  __DATA_CONST.__got: 0x12e8
+  __DATA_CONST.__const: 0x2708
   __DATA_CONST.__cfstring: 0x5720
   __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x198

   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x4f0
   __DATA_CONST.__objc_arrayobj: 0x918
-  __DATA_CONST.__objc_intobj: 0x300
+  __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1e2c8
-  __DATA.__objc_selrefs: 0x3e80
-  __DATA.__objc_ivar: 0x41c
+  __DATA.__objc_const: 0x1e3e8
+  __DATA.__objc_selrefs: 0x3fa0
+  __DATA.__objc_ivar: 0x428
   __DATA.__objc_data: 0x44c0
   __DATA.__data: 0xc60
   __DATA.__bss: 0x4e8

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 2919
-  Symbols:   899
-  CStrings:  4518
+  Functions: 2959
+  Symbols:   906
+  CStrings:  4582
 
Symbols:
+ _CPCopyBundleIdentifierAndTeamFromApplicationIdentifier
+ _DMFPolicyUnlocalizedDisplayName
+ _OBJC_CLASS_$_CTCategories
+ _OBJC_CLASS_$_DMFApplicationPolicyMonitor
+ _OBJC_CLASS_$_DMFCategoryPolicyMonitor
+ _OBJC_CLASS_$_DMFCommunicationPolicyMonitor
+ _OBJC_CLASS_$_DMFPrioritizedPolicy
+ _OBJC_CLASS_$_DMFWebsitePolicyMonitor
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSConditionLock
- _DMFEffectivePolicyTypeDowntime
- _DMFEffectivePolicyTypeShield
- _OBJC_CLASS_$_NSMapTable
CStrings:
+ "@\"NSCache\""
+ "Categories lookup timed out"
+ "Error recalculating effectivePolicy for type %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "Error recalculating effectivePolicy for types %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "Failed fetching categories for bundle identifiers with error: %!{(MISSING)public}@"
+ "Failed fetching categories for websites with error: %!{(MISSING)public}@"
+ "Failed looking up parent bundle identifier for app clip: %!{(MISSING)public}@ with parent application identifier %!{(MISSING)public}@"
+ "No application record for bundle identifier: %!{(MISSING)public}@ with error: %!{(MISSING)public}@"
+ "No policies are set, everything is OK"
+ "Requested application %!{(MISSING)public}@ failed to categorize parent application %!{(MISSING)public}@"
+ "Requested application %!{(MISSING)public}@ has parent applications %!{(MISSING)public}@"
+ "Requested application %!{(MISSING)public}@ has policy %!{(MISSING)public}@, associated categories:%!{(MISSING)public}@ associated sites:%!{(MISSING)public}@ equivalent bundle identifiers:%!{(MISSING)public}@"
+ "Requested application %!{(MISSING)public}@ is missing categorization"
+ "Requested application %!{(MISSING)public}@ is unblockable"
+ "Requested application %!{(MISSING)public}@ with associated category %!{(MISSING)public}@ is unblockable"
+ "Requested category %!{(MISSING)public}@ has policy %!{(MISSING)public}@"
+ "Requested category %!{(MISSING)public}@ is unblockable"
+ "Requested website %!{(MISSING)public}@ has policy %!{(MISSING)public}@, associated categories:%!{(MISSING)public}@ associated sites:%!{(MISSING)public}@ equivalent bundle identifiers:%!{(MISSING)public}@"
+ "Requested website URL does not have a host, marking policy %!{(MISSING)public}@"
+ "Requested website with associated bundle identifier %!{(MISSING)public}@ is unblockable"
+ "Requested website with associated category %!{(MISSING)public}@ is unblockable"
+ "T@\"NSCache\",R,N,V_bundleIdentifierPolicyCache"
+ "T@\"NSCache\",R,N,V_categoryIdentifierPolicyCache"
+ "T@\"NSCache\",R,N,V_effectivePolicyCache"
+ "T@\"NSCache\",R,N,V_websiteURLsPolicyCache"
+ "_appendPolicyForBundleIdentifiers:toPolicies:categories:parentBundleIdentifiers:policiesByType:"
+ "_appendPolicyForCategoryIdentifiers:toPolicies:policiesByType:"
+ "_appendPolicyForWebsiteURLs:toPolicies:categories:policiesByType:"
+ "_bundleIdentifierPolicyCache"
+ "_categoryIdentifierPolicyCache"
+ "_clearPolicyCachesForTypes:"
+ "_effectivePoliciesForTypes:outError:"
+ "_effectivePolicyCache"
+ "_effectivePolicyForType:outError:"
+ "_fetchCategoriesForBundleIdentifiers:withError:"
+ "_fetchCategoriesIfNeededForWebsiteURLs:withError:"
+ "_fetchParentBundleIdentifiersForBundleIdentifiers:"
+ "_handleChangesToPolicyTypes:"
+ "_notifyClientsRegisteredForPolicyTypes:"
+ "_performBackgroundTaskAndWait:"
+ "_recalculateEffectivePolicyForType:outError:"
+ "_recalculateEffectivePolicyForTypes:"
+ "_websiteURLsPolicyCache"
+ "arbitratePolicyForPrioritizedPolicies:"
+ "bundleIdentifierPolicyCache"
+ "categoriesForBundleIDs:completionHandler:"
+ "categoriesForDomainURLs:completionHandler:"
+ "categoryIdentifierPolicyCache"
+ "communicationPolicyForApplicationPolicy:downtimeEnforced:"
+ "downtimeEnforced"
+ "effectivePolicyCache"
+ "equivalentBundleIdentifiers"
+ "initWithCondition:"
+ "intersectsSet:"
+ "lock"
+ "lockWhenCondition:beforeDate:"
+ "parentApplicationIdentifiers"
+ "prioritizedPoliciesForAppPolicy:appCategoryPolicy:bundleIdentifiers:categoryPolicy:categoryIdentifiers:webPolicy:webCategoryPolicy:webDomains:"
+ "requestCommunicationPoliciesForBundleIdentifiers:replyHandler:"
+ "requestPoliciesForBundleIdentifiers:replyHandler:"
+ "requestPoliciesForCategoryIdentifiers:replyHandler:"
+ "requestPoliciesForWebsiteURLs:replyHandler:"
+ "sharedCategories"
+ "unblockableBundleIdentifiers"
+ "unblockableCategoryIdentifiers"
+ "unlock"
+ "unlockWithCondition:"
+ "v56@0:8@16@24@32@40@48"
+ "websiteURLsPolicyCache"
- "\x01\x15"
- "@\"NSMapTable\""
- "_contextsByXPCConnection"
- "_notifyClientsRegisteredForPolicyType:"
- "currentConnection"
- "initWithKeyOptions:valueOptions:capacity:"

```
