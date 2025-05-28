## OnBoardingKit

> `/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit`

```diff

-3538.0.0.0.0
-  __TEXT.__text: 0x330fc
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x43fc
+3711.0.0.0.0
+  __TEXT.__text: 0x3490c
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x44f4
   __TEXT.__const: 0x388
-  __TEXT.__cstring: 0x141a
-  __TEXT.__oslogstring: 0x783
+  __TEXT.__cstring: 0x14ef
+  __TEXT.__oslogstring: 0x8a3
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0xc08
+  __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__unwind_info: 0xc44
   __TEXT.__objc_classname: 0x9e3
-  __TEXT.__objc_methname: 0xce0d
-  __TEXT.__objc_methtype: 0x1aa1
-  __TEXT.__objc_stubs: 0x90e0
+  __TEXT.__objc_methname: 0xd223
+  __TEXT.__objc_methtype: 0x1aab
+  __TEXT.__objc_stubs: 0x9320
   __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__const: 0x550
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa3e0
-  __DATA_CONST.__objc_selrefs: 0x2c28
+  __DATA_CONST.__objc_const: 0xa4a0
+  __DATA_CONST.__objc_selrefs: 0x2ce0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x3b0
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__objc_const: 0x1ed0
-  __AUTH_CONST.__cfstring: 0x1b00
+  __AUTH_CONST.__cfstring: 0x1be0
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH.__objc_data: 0x1090
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x3a0
-  __DATA.__objc_superrefs: 0x268
-  __DATA.__objc_ivar: 0x4d8
-  __DATA.__data: 0x688
-  __DATA.__bss: 0x18
+  __DATA.__objc_ivar: 0x4e8
+  __DATA.__data: 0x680
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1418
-  Symbols:   5427
-  CStrings:  2722
+  Functions: 1443
+  Symbols:   5510
+  CStrings:  2768
 
Symbols:
+ +[OBBundle bundleAtPath:isLinkBundle:isReplacementBundle:]
+ +[OBPrivacyLinkController linkWithPrivacyBundle:]
+ -[OBBundle initWithBundle:isLinkBundle:isReplacementBundle:]
+ -[OBBundle isReplacementBundle]
+ -[OBBundle replaceeIdentifierSetsCache]
+ -[OBBundle replacementPreconditionCache]
+ -[OBBundle setIsReplacementBundle:]
+ -[OBBundle setReplaceeIdentifierSetsCache:]
+ -[OBBundle setReplacementPreconditionCache:]
+ -[OBBundleManager _allLinkBundles]
+ -[OBBundleManager _bundleWithIdentifier:usingSearchPath:includePlaceholder:isLinkBundle:isReplacementBundle:]
+ -[OBBundleManager _bundlesInSearchPath:withBundleCreationBlock:]
+ -[OBBundleManager _isPreconditionSatisfiedForReplacementBundle:]
+ -[OBBundleManager _modifyBundles:asNecessaryWithReplacementBundles:]
+ -[OBBundleManager _subarrayHavingPreconditionSatisfiedOfReplacementBundles:]
+ -[OBBundleManager allReplacementBundles]
+ -[OBBundleManager orderedPrivacyBundlesWithInclusionOptions:]
+ -[OBCapabilities .cxx_destruct]
+ -[OBCapabilities eligibleForChlorine]
+ -[OBCapabilities eligibleForChlorine].cold.1
+ -[OBCapabilities overrideEligibleForChlorine]
+ -[OBCapabilities setOverrideEligibleForChlorine:]
+ -[OBPrivacyFlow replaceeIdentifierSets]
+ -[OBPrivacyFlow replacementPrecondition]
+ -[OBStackedIconTextList traitCollectionDidChange:]
+ -[OBStackedIconTextList updateSpacing]
+ GCC_except_table4
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_OBBundle._isReplacementBundle
+ _OBJC_IVAR_$_OBBundle._replaceeIdentifierSetsCache
+ _OBJC_IVAR_$_OBBundle._replacementPreconditionCache
+ _OBJC_IVAR_$_OBCapabilities._overrideEligibleForChlorine
+ __OBJC_$_PROP_LIST_OBPrivacyBundleProvider.68
+ __Unwind_Resume
+ ___34-[OBBundleManager _allLinkBundles]_block_invoke
+ ___36+[OBCapabilities sharedCapabilities]_block_invoke
+ ___40-[OBBundleManager allReplacementBundles]_block_invoke
+ ___61-[OBBundleManager orderedPrivacyBundlesWithInclusionOptions:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e28_"OBBundle"16?0"NSString"8ls32l8s40l8
+ ___block_literal_global.2
+ ___block_literal_global.33
+ ___block_literal_global.89
+ ___objc_personality_v0
+ _objc_msgSend$_allLinkBundles
+ _objc_msgSend$_bundleWithIdentifier:usingSearchPath:includePlaceholder:isLinkBundle:isReplacementBundle:
+ _objc_msgSend$_bundlesInSearchPath:withBundleCreationBlock:
+ _objc_msgSend$_isPreconditionSatisfiedForReplacementBundle:
+ _objc_msgSend$_modifyBundles:asNecessaryWithReplacementBundles:
+ _objc_msgSend$_subarrayHavingPreconditionSatisfiedOfReplacementBundles:
+ _objc_msgSend$allReplacementBundles
+ _objc_msgSend$bundleAtPath:isLinkBundle:isReplacementBundle:
+ _objc_msgSend$bundlesWithIdentifiers:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:constant:
+ _objc_msgSend$eligibleForChlorine
+ _objc_msgSend$initWithBundle:isLinkBundle:isReplacementBundle:
+ _objc_msgSend$isSubsetOfSet:
+ _objc_msgSend$linkWithPrivacyBundle:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$orderedPrivacyBundlesWithInclusionOptions:
+ _objc_msgSend$replaceeIdentifierSets
+ _objc_msgSend$replaceeIdentifierSetsCache
+ _objc_msgSend$replacementPrecondition
+ _objc_msgSend$replacementPreconditionCache
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$unionSet:
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_eligibility_get_domain_answer
+ _sharedCapabilities.onceToken
+ _sharedCapabilities.sharedInstance
- +[OBBundle bundleAtPath:isLinkBundle:]
- -[OBBundle initWithBundle:isLinkBundle:]
- -[OBBundleManager bundleWithIdentifier:usingSearchPath:includePlaceholder:isLinkBundle:]
- -[OBBundleManager orderedPrivacyBundlesWithPrivacyPaneBundle:]
- __OBJC_$_PROP_LIST_OBPrivacyBundleProvider.67
- ___62-[OBBundleManager orderedPrivacyBundlesWithPrivacyPaneBundle:]_block_invoke
- ___block_literal_global.23
- ___block_literal_global.88
- _objc_msgSend$bundleAtPath:isLinkBundle:
- _objc_msgSend$bundleWithIdentifier:usingSearchPath:includePlaceholder:isLinkBundle:
- _objc_msgSend$initWithBundle:isLinkBundle:
- _objc_msgSend$orderedPrivacyBundlesWithPrivacyPaneBundle:
- _sharedInstance
CStrings:
+ "\x01\x15"
+ "@\"OBBundle\"16@?0@\"NSString\"8"
+ "@32@0:8@16@?24"
+ "@32@0:8@16B24B28"
+ "@44@0:8@16@24B32B36B40"
+ "Failed to create bundle with identifier %@ including placeholder %@ using search path %@"
+ "Failed to get eligibility for chlorine with error %d"
+ "OBPrivacy: Client directly requested placeholder bundle %@"
+ "OBPrivacy: Failed to get contents of %@ directory: %@"
+ "Placeholder bundles are only supported for regular bundles."
+ "Precondition"
+ "Privacy link controller encountered nil flow for bundle identifier %@"
+ "ReplaceeSets"
+ "Replacement bundle %@ has unsupported precondition %@"
+ "ReplacementBundles"
+ "ReplacementInfo"
+ "T@\"NSArray\",&,N,V_replaceeIdentifierSetsCache"
+ "T@\"NSNumber\",&,N,V_overrideEligibleForChlorine"
+ "T@\"NSString\",&,N,V_replacementPreconditionCache"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,N,V_isReplacementBundle"
+ "Tq,?,N"
+ "_allLinkBundles"
+ "_bundleWithIdentifier:usingSearchPath:includePlaceholder:isLinkBundle:isReplacementBundle:"
+ "_bundlesInSearchPath:withBundleCreationBlock:"
+ "_isPreconditionSatisfiedForReplacementBundle:"
+ "_isReplacementBundle"
+ "_modifyBundles:asNecessaryWithReplacementBundles:"
+ "_overrideEligibleForChlorine"
+ "_replaceeIdentifierSetsCache"
+ "_replacementPreconditionCache"
+ "_subarrayHavingPreconditionSatisfiedOfReplacementBundles:"
+ "allReplacementBundles"
+ "bundleAtPath:isLinkBundle:isReplacementBundle:"
+ "chlorine"
+ "constraintLessThanOrEqualToAnchor:constant:"
+ "eligibleForChlorine"
+ "initWithBundle:isLinkBundle:isReplacementBundle:"
+ "isReplacementBundle"
+ "isSubsetOfSet:"
+ "linkWithPrivacyBundle:"
+ "numberWithBool:"
+ "orderedPrivacyBundlesWithInclusionOptions:"
+ "overrideEligibleForChlorine"
+ "replaceeIdentifierSets"
+ "replaceeIdentifierSetsCache"
+ "replacementPrecondition"
+ "replacementPreconditionCache"
+ "setIsReplacementBundle:"
+ "setOverrideEligibleForChlorine:"
+ "setReplaceeIdentifierSetsCache:"
+ "setReplacementPreconditionCache:"
+ "setWithArray:"
+ "unionSet:"
- "\x01\x13"
- "@20@0:8B16"
- "@28@0:8@16B24"
- "@40@0:8@16@24B32B36"
- "No privacy bundle with identifier %@"
- "T@\"UITextInputPasswordRules\",C,N"
- "TB,N,GisSecureTextEntry"
- "Tq,N"
- "bundleAtPath:isLinkBundle:"
- "bundleWithIdentifier:usingSearchPath:includePlaceholder:isLinkBundle:"
- "initWithBundle:isLinkBundle:"
- "orderedPrivacyBundlesWithPrivacyPaneBundle:"

```
