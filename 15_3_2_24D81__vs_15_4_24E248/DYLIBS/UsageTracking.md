## UsageTracking

> `/System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTracking`

```diff

-377.3.2.0.0
-  __TEXT.__text: 0x30efc
+377.4.6.0.0
+  __TEXT.__text: 0x30f98
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x1384
+  __TEXT.__objc_methlist: 0x1538
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x980
   __TEXT.__cstring: 0x166d
   __TEXT.__oslogstring: 0x1590
-  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__unwind_info: 0x7f0
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x292
-  __TEXT.__objc_methname: 0x694c
-  __TEXT.__objc_methtype: 0xe0a
-  __TEXT.__objc_stubs: 0x4100
+  __TEXT.__objc_methname: 0x6987
+  __TEXT.__objc_methtype: 0xe25
+  __TEXT.__objc_stubs: 0x4120
   __DATA_CONST.__got: 0x358
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1298
+  __DATA_CONST.__objc_selrefs: 0x12d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x1090
   __AUTH_CONST.__cfstring: 0x1200
-  __AUTH_CONST.__objc_const: 0x2a38
+  __AUTH_CONST.__objc_const: 0x2738
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x1a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F59A08ED-C00C-3B8E-B559-9D5F0F4F5F44
-  Functions: 654
-  Symbols:   1871
-  CStrings:  1360
+  UUID: 0A81FB96-56E9-377D-9E04-487D6FAC4495
+  Functions: 666
+  Symbols:   1885
+  CStrings:  1362
 
Symbols:
+ +[USUsageQuerying userKnowledgeStore].cold.1
+ -[USBudget initWithCategories:applications:webDomains:schedule:calendarIdentifier:identifier:].cold.1
+ -[USBudget initWithCategories:applications:webDomains:schedule:calendarIdentifier:identifier:].cold.2
+ -[USDomainNormalization normalizeDomainName:].cold.2
+ -[USDomainNormalization normalizeDomainName:].cold.3
+ -[USDomainNormalization normalizeDomainName:].cold.4
+ -[USUsageQuerying _generateUsageTimeWithApplicationUsageIntervals:webUsageIntervalsByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByBundleIdentifier:categoryByWebDomain:applications:webDomains:categories:].cold.1
+ -[USUsageQuerying _generateUsageTimeWithApplicationUsageIntervals:webUsageIntervalsByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByBundleIdentifier:categoryByWebDomain:applications:webDomains:categories:].cold.2
+ -[USWebHistory init].cold.1
+ -[USWebpageUsage initWithURL:bundleIdentifier:profileIdentifier:auditToken:]
+ -[USWebpageUsage initWithURL:bundleIdentifier:profileIdentifier:auditToken:].cold.1
+ GCC_except_table13
+ __473-[USUsageQuerying _updateLocalReports:remoteReports:aggregateReports:nonIntersectingScreenTimeIntervals:intersectingScreenTimeIntervals:longestSessionByDevice:applicationUsageIntervals:unboundApplicationUsageIntervals:webUsageIntervalsByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByBundleIdentifier:categoryByWebDomain:notificationsByDevice:interval:timeZoneByDevice:lastEventDateByDevice:]_block_invoke.cold.1
+ __86-[USUsageQuerying queryForUncategorizedLocalWebUsageDuringInterval:completionHandler:]_block_invoke_2.cold.2
+ __87-[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke.78.cold.2
+ __90-[USUsageQuerying queryUsageDuringInterval:partitionInterval:focalOnly:completionHandler:]_block_invoke.27.cold.3
+ __94-[USBudget initWithCategories:applications:webDomains:schedule:calendarIdentifier:identifier:]_block_invoke.cold.1
+ _objc_msgSend$initWithURL:bundleIdentifier:profileIdentifier:auditToken:
- -[USWebpageUsage initWithURL:bundleIdentifier:auditToken:].cold.1
- GCC_except_table10
- GCC_except_table12
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
CStrings:
+ "@72@0:8@16@24@32{?=[8I]}40"
+ "initWithURL:bundleIdentifier:profileIdentifier:auditToken:"

```
