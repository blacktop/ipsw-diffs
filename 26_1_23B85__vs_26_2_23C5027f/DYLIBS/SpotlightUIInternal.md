## SpotlightUIInternal

> `/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal`

```diff

-181.1.14.0.0
-  __TEXT.__text: 0x29294
+181.2.4.0.0
+  __TEXT.__text: 0x29280
   __TEXT.__auth_stubs: 0xc40
   __TEXT.__objc_methlist: 0x3880
   __TEXT.__const: 0x3ba
-  __TEXT.__cstring: 0xeb3
+  __TEXT.__cstring: 0xf03
   __TEXT.__gcc_except_tab: 0x238
   __TEXT.__oslogstring: 0x64c
   __TEXT.__ustring: 0x4

   __TEXT.__objc_methname: 0xb750
   __TEXT.__objc_methtype: 0x1bca
   __TEXT.__objc_stubs: 0x9de0
-  __DATA_CONST.__got: 0x7a0
+  __DATA_CONST.__got: 0x780
   __DATA_CONST.__const: 0xab8
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x13a0
+  __AUTH_CONST.__cfstring: 0x1400
   __AUTH_CONST.__objc_const: 0x4e78
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 39B09328-A460-32CB-B5FD-C4CF846D6E21
+  UUID: 12F1D72A-0527-39C5-B10D-D0E72141EABE
   Functions: 1181
-  Symbols:   4799
-  CStrings:  2641
+  Symbols:   4795
+  CStrings:  2647
 
Symbols:
+ ___50-[SPUISearchViewController spotlightDidBackground]_block_invoke.791
+ ___60-[SPUISearchViewController searchViewWillPresentFromSource:]_block_invoke.781
+ ___70-[SPUISearchViewController activateFirstTimeExperienceViewIfNecessary]_block_invoke.814
+ ___block_literal_global.818
+ ___block_literal_global.824
- _SSNotificationNameRefreshZKW
- _SSSectionIdentifierSuggestions
- _SSSectionIdentifierTopHits
- _SSSectionIdentifierZKW
- ___50-[SPUISearchViewController spotlightDidBackground]_block_invoke.365
- ___60-[SPUISearchViewController searchViewWillPresentFromSource:]_block_invoke.355
- ___70-[SPUISearchViewController activateFirstTimeExperienceViewIfNecessary]_block_invoke.388
- ___block_literal_global.392
- ___block_literal_global.401
Functions:
~ -[SPUIResultsViewController _pushSectionsUpdate] : 1660 -> 1656
~ -[SPUIResultsViewController searchAgentUpdatedResults:] : 920 -> 916
~ ___45-[SPUISearchModelZKW updateWithQueryContext:]_block_invoke : 192 -> 188
~ -[SPUISearchViewController sectionShouldBeExpanded:] : 208 -> 204
~ -[SPUISearchViewController didChangeExpansionStateForSection:expanded:] : 192 -> 188
CStrings:
+ "com.apple.searchd.suggestions"
+ "com.apple.searchd.zkw.apps"
+ "com.apple.spotlight.tophits"

```
