## UsageTracking

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking`

```diff

-377.5.1.0.0
-  __TEXT.__text: 0x27bac
+387.0.0.0.0
+  __TEXT.__text: 0x298c8
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x1550
+  __TEXT.__objc_methlist: 0x1618
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x730
-  __TEXT.__cstring: 0x11b3
-  __TEXT.__oslogstring: 0xe2c
-  __TEXT.__unwind_info: 0x690
+  __TEXT.__gcc_except_tab: 0x75c
+  __TEXT.__cstring: 0x126b
+  __TEXT.__oslogstring: 0x11cb
+  __TEXT.__unwind_info: 0x6e0
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x29f
-  __TEXT.__objc_methname: 0x69de
-  __TEXT.__objc_methtype: 0xf28
-  __TEXT.__objc_stubs: 0x40a0
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0xe08
+  __TEXT.__objc_methname: 0x6f96
+  __TEXT.__objc_methtype: 0xfb0
+  __TEXT.__objc_stubs: 0x4240
+  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__const: 0xe80
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1330
+  __DATA_CONST.__objc_selrefs: 0x13a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xd60
-  __AUTH_CONST.__objc_const: 0x2708
+  __AUTH_CONST.__cfstring: 0xdc0
+  __AUTH_CONST.__objc_const: 0x2798
   __AUTH_CONST.__objc_intobj: 0x60
-  __DATA.__objc_ivar: 0x188
+  __DATA.__objc_ivar: 0x194
   __DATA.__data: 0x300
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71F160C7-79EC-3E69-A1AD-6828B5BD950C
-  Functions: 560
-  Symbols:   2314
-  CStrings:  1281
+  UUID: FBF834CA-1378-3CC6-8944-70416143FE26
+  Functions: 591
+  Symbols:   2398
+  CStrings:  1326
 
Symbols:
+ +[USWebHistory _shouldDeleteEvent:timestamp:uniqueID:isStartEvent:deletionInterval:startEventByUniqueID:missedEventsToDelete:]
+ -[USBudget exemptBundleIdentifiers]
+ -[USBudget initWithCategories:applications:exemptApplications:webDomains:schedule:calendarIdentifier:identifier:]
+ -[USBudget initWithCategories:applications:exemptApplications:webDomains:schedule:calendarIdentifier:identifier:].cold.1
+ -[USBudget initWithCategories:applications:exemptApplications:webDomains:schedule:calendarIdentifier:identifier:].cold.2
+ -[USDeviceActivityEvent exemptApplicationTokens]
+ -[USDeviceActivityEvent exemptBundleIdentifiers]
+ -[USDeviceActivityEvent initWithApplicationTokens:exemptApplicationTokens:categoryTokens:webDomainTokens:threshold:includesPastActivity:]
+ -[USDeviceActivityEvent initWithBundleIdentifiers:exemptBundleIdentifiers:categoryIdentifiers:webDomains:threshold:includesPastActivity:]
+ -[USUsageQuerying _calculateAllExemptBundleIdentifiersFromExemptApplications:categoryByBundleIdentifier:]
+ -[USUsageQuerying _calculateAllExemptWebDomainsFromExemptApplications:categoryByBundleIdentifier:]
+ -[USUsageQuerying _computeApplicationUsageWithEvents:exemptApplications:exemptWebDomains:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:]
+ -[USUsageQuerying _computeUsageForApplications:exemptApplications:webDomains:categories:applicationUsageEvents:webUsageEvents:nowPlayingEvents:videoUsageEvents:categoryByBundleIdentifier:categoryByWebDomain:interval:referenceDate:focalOnly:]
+ -[USUsageQuerying _computeUsageForApplications:exemptApplications:webDomains:categories:applicationUsageEvents:webUsageEvents:nowPlayingEvents:videoUsageEvents:categoryByBundleIdentifier:categoryByWebDomain:interval:referenceDate:focalOnly:].cold.1
+ -[USUsageQuerying _computeUsageForApplications:exemptApplications:webDomains:categories:applicationUsageEvents:webUsageEvents:nowPlayingEvents:videoUsageEvents:categoryByBundleIdentifier:categoryByWebDomain:interval:referenceDate:focalOnly:].cold.2
+ -[USUsageQuerying _computeWebUsageWithEvents:exemptWebDomains:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:]
+ -[USUsageQuerying _enumerateCurrentApplicationUsageIntervalsDuringInterval:exemptApplications:referenceDate:focalOnly:block:]
+ -[USUsageQuerying _enumerateCurrentApplicationUsageIntervalsDuringInterval:exemptApplications:referenceDate:focalOnly:block:].cold.1
+ -[USUsageQuerying _enumerateCurrentApplicationUsageIntervalsDuringInterval:exemptApplications:referenceDate:focalOnly:block:].cold.2
+ -[USUsageQuerying _enumerateCurrentVideoUsageIntervalsDuringInterval:exemptApplications:exemptWebDomains:referenceDate:block:]
+ -[USUsageQuerying _enumerateCurrentVideoUsageIntervalsDuringInterval:exemptApplications:exemptWebDomains:referenceDate:block:].cold.1
+ -[USUsageQuerying _enumerateCurrentVideoUsageIntervalsDuringInterval:exemptApplications:exemptWebDomains:referenceDate:block:].cold.2
+ -[USUsageQuerying _enumerateCurrentVideoUsageIntervalsDuringInterval:exemptApplications:exemptWebDomains:referenceDate:block:].cold.3
+ -[USUsageQuerying _enumerateCurrentWebUsageIntervalsDuringInterval:exemptWebDomains:referenceDate:focalOnly:block:]
+ -[USUsageQuerying _enumerateCurrentWebUsageIntervalsDuringInterval:exemptWebDomains:referenceDate:focalOnly:block:].cold.1
+ -[USUsageQuerying _enumerateCurrentWebUsageIntervalsDuringInterval:exemptWebDomains:referenceDate:focalOnly:block:].cold.2
+ -[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:error:]
+ -[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:]
+ -[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:segmentInterval:error:]
+ -[USWebHistory _deleteBiomeEventsDuringInterval:webApplication:profileIdentifier:pruner:eventsPassingTest:]
+ -[USWebHistory _deleteBiomeHistoryDuringInterval:webApplication:profileIdentifier:]
+ -[USWebHistory _deleteBiomeMediaUsageDuringInterval:webApplication:profileIdentifier:]
+ -[USWebHistory _deleteBiomeWebUsageDuringInterval:webApplication:profileIdentifier:]
+ -[USWebHistory _deleteCoreDuetHistoryDuringInterval:webApplication:profileIdentifier:completionHandler:]
+ GCC_except_table26
+ GCC_except_table4
+ GCC_except_table43
+ GCC_except_table52
+ GCC_except_table8
+ _OBJC_IVAR_$_USBudget._exemptBundleIdentifiers
+ _OBJC_IVAR_$_USDeviceActivityEvent._exemptApplicationTokens
+ _OBJC_IVAR_$_USDeviceActivityEvent._exemptBundleIdentifiers
+ __OBJC_$_CLASS_METHODS_USWebHistory
+ ___105-[USUsageQuerying _calculateAllExemptBundleIdentifiersFromExemptApplications:categoryByBundleIdentifier:]_block_invoke
+ ___106-[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke
+ ___106-[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke.68
+ ___106-[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke.68.cold.1
+ ___106-[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke.69
+ ___106-[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke_2
+ ___106-[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke_2.cold.1
+ ___106-[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke_2.cold.2
+ ___107-[USWebHistory _deleteBiomeEventsDuringInterval:webApplication:profileIdentifier:pruner:eventsPassingTest:]_block_invoke
+ ___113-[USBudget initWithCategories:applications:exemptApplications:webDomains:schedule:calendarIdentifier:identifier:]_block_invoke
+ ___113-[USBudget initWithCategories:applications:exemptApplications:webDomains:schedule:calendarIdentifier:identifier:]_block_invoke.cold.1
+ ___267-[USUsageQuerying _computeWebUsageWithEvents:exemptWebDomains:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:]_block_invoke
+ ___267-[USUsageQuerying _computeWebUsageWithEvents:exemptWebDomains:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:]_block_invoke.93
+ ___267-[USUsageQuerying _computeWebUsageWithEvents:exemptWebDomains:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:]_block_invoke.cold.1
+ ___267-[USUsageQuerying _computeWebUsageWithEvents:exemptWebDomains:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:]_block_invoke_2
+ ___306-[USUsageQuerying _computeApplicationUsageWithEvents:exemptApplications:exemptWebDomains:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:]_block_invoke
+ ___306-[USUsageQuerying _computeApplicationUsageWithEvents:exemptApplications:exemptWebDomains:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:]_block_invoke.89
+ ___306-[USUsageQuerying _computeApplicationUsageWithEvents:exemptApplications:exemptWebDomains:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:]_block_invoke.cold.1
+ ___306-[USUsageQuerying _computeApplicationUsageWithEvents:exemptApplications:exemptWebDomains:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:]_block_invoke_2
+ ___84-[USWebHistory _deleteBiomeWebUsageDuringInterval:webApplication:profileIdentifier:]_block_invoke
+ ___84-[USWebHistory _deleteBiomeWebUsageDuringInterval:webApplication:profileIdentifier:]_block_invoke.cold.1
+ ___86-[USUsageQuerying queryForUncategorizedLocalWebUsageDuringInterval:completionHandler:]_block_invoke.81
+ ___86-[USWebHistory _deleteBiomeMediaUsageDuringInterval:webApplication:profileIdentifier:]_block_invoke
+ ___86-[USWebHistory _deleteBiomeMediaUsageDuringInterval:webApplication:profileIdentifier:]_block_invoke.cold.1
+ ___98-[USUsageQuerying _calculateAllExemptWebDomainsFromExemptApplications:categoryByBundleIdentifier:]_block_invoke
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96r104r_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r96l8r104l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104s112s120s_e18_v16?0"_DKEvent"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s_e18_v16?0"_DKEvent"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8
+ ___block_descriptor_161_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136r144r_e34_v24?0"NSDictionary"8"NSError"16lr136l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8r144l8s128l8
+ ___block_descriptor_161_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136r144r_e34_v24?0"NSDictionary"8"NSError"16lr136l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8r144l8
+ ___block_descriptor_48_e8_32s40s_e22_v24?0"NSString"8^B16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e26_B24?0"BMStoreEvent"8^B16ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e69_B40?0"BMStoreEvent"8"NSMutableDictionary"16"NSMutableArray"24^B32ls32l8s40l8s48l8s56l8
+ _objc_msgSend$_calculateAllExemptBundleIdentifiersFromExemptApplications:categoryByBundleIdentifier:
+ _objc_msgSend$_calculateAllExemptWebDomainsFromExemptApplications:categoryByBundleIdentifier:
+ _objc_msgSend$_computeApplicationUsageWithEvents:exemptApplications:exemptWebDomains:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:
+ _objc_msgSend$_computeUsageForApplications:exemptApplications:webDomains:categories:applicationUsageEvents:webUsageEvents:nowPlayingEvents:videoUsageEvents:categoryByBundleIdentifier:categoryByWebDomain:interval:referenceDate:focalOnly:
+ _objc_msgSend$_computeWebUsageWithEvents:exemptWebDomains:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:
+ _objc_msgSend$_deleteBiomeEventsDuringInterval:webApplication:profileIdentifier:pruner:eventsPassingTest:
+ _objc_msgSend$_deleteBiomeHistoryDuringInterval:webApplication:profileIdentifier:
+ _objc_msgSend$_deleteBiomeMediaUsageDuringInterval:webApplication:profileIdentifier:
+ _objc_msgSend$_deleteBiomeWebUsageDuringInterval:webApplication:profileIdentifier:
+ _objc_msgSend$_deleteCoreDuetHistoryDuringInterval:webApplication:profileIdentifier:completionHandler:
+ _objc_msgSend$_enumerateCurrentApplicationUsageIntervalsDuringInterval:exemptApplications:referenceDate:focalOnly:block:
+ _objc_msgSend$_enumerateCurrentVideoUsageIntervalsDuringInterval:exemptApplications:exemptWebDomains:referenceDate:block:
+ _objc_msgSend$_enumerateCurrentWebUsageIntervalsDuringInterval:exemptWebDomains:referenceDate:focalOnly:block:
+ _objc_msgSend$_shouldDeleteEvent:timestamp:uniqueID:isStartEvent:deletionInterval:startEventByUniqueID:missedEventsToDelete:
+ _objc_msgSend$deleteStoreEvent:
+ _objc_msgSend$exemptApplicationTokens
+ _objc_msgSend$exemptBundleIdentifiers
+ _objc_msgSend$initWithApplicationTokens:exemptApplicationTokens:categoryTokens:webDomainTokens:threshold:includesPastActivity:
+ _objc_msgSend$initWithBundleIdentifiers:exemptBundleIdentifiers:categoryIdentifiers:webDomains:threshold:includesPastActivity:
+ _objc_msgSend$initWithCategories:applications:exemptApplications:webDomains:schedule:calendarIdentifier:identifier:
+ _objc_msgSend$queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:
- -[USBudget initWithCategories:applications:webDomains:schedule:calendarIdentifier:identifier:].cold.1
- -[USBudget initWithCategories:applications:webDomains:schedule:calendarIdentifier:identifier:].cold.2
- -[USUsageQuerying _computeApplicationUsageWithEvents:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:]
- -[USUsageQuerying _computeUsageForApplications:webDomains:categories:applicationUsageEvents:webUsageEvents:nowPlayingEvents:videoUsageEvents:categoryByBundleIdentifier:categoryByWebDomain:interval:referenceDate:focalOnly:]
- -[USUsageQuerying _computeWebUsageWithEvents:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:]
- -[USUsageQuerying _enumerateCurrentApplicationUsageIntervalsDuringInterval:referenceDate:focalOnly:block:]
- -[USUsageQuerying _enumerateCurrentApplicationUsageIntervalsDuringInterval:referenceDate:focalOnly:block:].cold.1
- -[USUsageQuerying _enumerateCurrentVideoUsageIntervalsDuringInterval:referenceDate:block:].cold.1
- -[USUsageQuerying _enumerateCurrentWebUsageIntervalsDuringInterval:referenceDate:focalOnly:block:]
- -[USUsageQuerying _enumerateCurrentWebUsageIntervalsDuringInterval:referenceDate:focalOnly:block:].cold.1
- -[USUsageQuerying queryForApplications:webDomains:categories:interval:error:]
- -[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]
- -[USUsageQuerying queryForApplications:webDomains:categories:interval:segmentInterval:error:]
- GCC_except_table24
- GCC_except_table3
- GCC_except_table41
- GCC_except_table45
- GCC_except_table50
- GCC_except_table7
- ___250-[USUsageQuerying _computeWebUsageWithEvents:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:]_block_invoke
- ___250-[USUsageQuerying _computeWebUsageWithEvents:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:]_block_invoke_2
- ___250-[USUsageQuerying _computeWebUsageWithEvents:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:]_block_invoke_3
- ___270-[USUsageQuerying _computeApplicationUsageWithEvents:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:]_block_invoke
- ___270-[USUsageQuerying _computeApplicationUsageWithEvents:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:]_block_invoke_2
- ___270-[USUsageQuerying _computeApplicationUsageWithEvents:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:]_block_invoke_3
- ___86-[USUsageQuerying queryForUncategorizedLocalWebUsageDuringInterval:completionHandler:]_block_invoke.80
- ___87-[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke
- ___87-[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke.68
- ___87-[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke.68.cold.1
- ___87-[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke.69
- ___87-[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke_2
- ___87-[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke_2.cold.1
- ___87-[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke_2.cold.2
- ___94-[USBudget initWithCategories:applications:webDomains:schedule:calendarIdentifier:identifier:]_block_invoke
- ___94-[USBudget initWithCategories:applications:webDomains:schedule:calendarIdentifier:identifier:]_block_invoke.cold.1
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88r96r_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r88l8r96l8
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112s_e18_v16?0"_DKEvent"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s_e18_v16?0"_DKEvent"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
- ___block_descriptor_153_e8_32s40s48s56s64s72s80s88s96s104s112s120s128r136r_e34_v24?0"NSDictionary"8"NSError"16lr128l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8r136l8s120l8
- ___block_descriptor_153_e8_32s40s48s56s64s72s80s88s96s104s112s120s128r136r_e34_v24?0"NSDictionary"8"NSError"16lr128l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8r136l8
- _objc_msgSend$_computeApplicationUsageWithEvents:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:
- _objc_msgSend$_computeUsageForApplications:webDomains:categories:applicationUsageEvents:webUsageEvents:nowPlayingEvents:videoUsageEvents:categoryByBundleIdentifier:categoryByWebDomain:interval:referenceDate:focalOnly:
- _objc_msgSend$_computeWebUsageWithEvents:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:
- _objc_msgSend$_enumerateCurrentApplicationUsageIntervalsDuringInterval:referenceDate:focalOnly:block:
- _objc_msgSend$_enumerateCurrentVideoUsageIntervalsDuringInterval:referenceDate:block:
- _objc_msgSend$_enumerateCurrentWebUsageIntervalsDuringInterval:referenceDate:focalOnly:block:
- _objc_msgSend$initWithCategories:applications:webDomains:schedule:calendarIdentifier:identifier:
- _objc_msgSend$queryForApplications:webDomains:categories:interval:focalOnly:error:
CStrings:
+ " Exempt Applications: ("
+ "-[USUsageQuerying queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke_2"
+ "@100@0:8@16@24@32@40@48@56@64@72@80@88B96"
+ "@108@0:8@16@24@32^@40@48@56@64@72@80@88@96B104"
+ "@60@0:8@16@24@32@40@48B56"
+ "@64@0:8@16@24@32@40@48^@56"
+ "@68@0:8@16@24@32@40@48B56^@60"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "@72@0:8@16@24@32@40@48d56^@64"
+ "B40@?0@\"BMStoreEvent\"8@\"NSMutableDictionary\"16@\"NSMutableArray\"24^B32"
+ "B68@0:8@16@24@32B40@44@52@60"
+ "Computing next interval with start components: %{public}@, end components: %{public}@"
+ "Exempt bundleIdentifiers %{public}@ have associated web domains %{public}@"
+ "Exempt bundleIdentifiers was %{public}@ and has been expanded to %{public}@"
+ "ExemptApplicationTokens"
+ "ExemptBundleIdentifiers"
+ "Next end date is: %{public}@"
+ "Next start date is: %{public}@"
+ "Previous end date is: %{public}@"
+ "Previous start date is: %{public}@"
+ "Processing an event without a uniqueID: %{public}@"
+ "Skipping calculating usage for %{public}@ because it is considered exempt"
+ "Skipping calculating usage for event %{public}@ because it is considered exempt"
+ "Skipping calculating usage for in use app %{public}@ because it is considered exempt"
+ "Skipping calculating usage for in-use web domain %{public}@ because it is considered exempt"
+ "Skipping usage calculation for app video usage %{public}@ because it is considered exempt"
+ "Skipping usage calculation for web video usage %{public}@ because it is considered exempt"
+ "T@\"NSSet\",R,C,V_exemptApplicationTokens"
+ "T@\"NSSet\",R,C,V_exemptBundleIdentifiers"
+ "_calculateAllExemptBundleIdentifiersFromExemptApplications:categoryByBundleIdentifier:"
+ "_calculateAllExemptWebDomainsFromExemptApplications:categoryByBundleIdentifier:"
+ "_computeApplicationUsageWithEvents:exemptApplications:exemptWebDomains:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:"
+ "_computeUsageForApplications:exemptApplications:webDomains:categories:applicationUsageEvents:webUsageEvents:nowPlayingEvents:videoUsageEvents:categoryByBundleIdentifier:categoryByWebDomain:interval:referenceDate:focalOnly:"
+ "_computeWebUsageWithEvents:exemptWebDomains:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:"
+ "_deleteBiomeEventsDuringInterval:webApplication:profileIdentifier:pruner:eventsPassingTest:"
+ "_deleteBiomeHistoryDuringInterval:webApplication:profileIdentifier:"
+ "_deleteBiomeMediaUsageDuringInterval:webApplication:profileIdentifier:"
+ "_deleteBiomeWebUsageDuringInterval:webApplication:profileIdentifier:"
+ "_deleteCoreDuetHistoryDuringInterval:webApplication:profileIdentifier:completionHandler:"
+ "_enumerateCurrentApplicationUsageIntervalsDuringInterval:exemptApplications:referenceDate:focalOnly:block:"
+ "_enumerateCurrentVideoUsageIntervalsDuringInterval:exemptApplications:exemptWebDomains:referenceDate:block:"
+ "_enumerateCurrentWebUsageIntervalsDuringInterval:exemptWebDomains:referenceDate:focalOnly:block:"
+ "_exemptApplicationTokens"
+ "_exemptBundleIdentifiers"
+ "_shouldDeleteEvent:timestamp:uniqueID:isStartEvent:deletionInterval:startEventByUniqueID:missedEventsToDelete:"
+ "d116@0:8@16@24@32@40@48@56@64@72@80@88@96@104B112"
+ "deleteStoreEvent:"
+ "exemptApplicationTokens"
+ "exemptBundleIdentifiers"
+ "initWithApplicationTokens:exemptApplicationTokens:categoryTokens:webDomainTokens:threshold:includesPastActivity:"
+ "initWithBundleIdentifiers:exemptBundleIdentifiers:categoryIdentifiers:webDomains:threshold:includesPastActivity:"
+ "initWithCategories:applications:exemptApplications:webDomains:schedule:calendarIdentifier:identifier:"
+ "queryForApplications:exemptApplications:webDomains:categories:interval:error:"
+ "queryForApplications:exemptApplications:webDomains:categories:interval:focalOnly:error:"
+ "queryForApplications:exemptApplications:webDomains:categories:interval:segmentInterval:error:"
+ "v24@?0@\"NSString\"8^B16"
+ "v52@0:8@16@24@32B40@?44"
- "-[USUsageQuerying queryForApplications:webDomains:categories:interval:focalOnly:error:]_block_invoke_2"
- "@60@0:8@16@24@32@40B48^@52"
- "@64@0:8@16@24@32@40d48^@56"
- "@92@0:8@16@24@32@40@48@56@64@72@80B88"
- "@92@0:8@16^@24@32@40@48@56@64@72@80B88"
- "_computeApplicationUsageWithEvents:unboundApplicationUsageIntervalsByDevice:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:categoryByBundleIdentifier:partition:referenceDate:focalOnly:"
- "_computeUsageForApplications:webDomains:categories:applicationUsageEvents:webUsageEvents:nowPlayingEvents:videoUsageEvents:categoryByBundleIdentifier:categoryByWebDomain:interval:referenceDate:focalOnly:"
- "_computeWebUsageWithEvents:timeZoneByDevice:lastEventDateByDevice:categoryUsageIntervalsByDevice:aggregatedApplicationUsageIntervalsByDevice:aggregatedWebUsageIntervalsByDevice:categoryByWebDomain:partition:referenceDate:focalOnly:"
- "_enumerateCurrentApplicationUsageIntervalsDuringInterval:referenceDate:focalOnly:block:"
- "_enumerateCurrentWebUsageIntervalsDuringInterval:referenceDate:focalOnly:block:"
- "d108@0:8@16@24@32@40@48@56@64@72@80@88@96B104"
- "queryForApplications:webDomains:categories:interval:error:"
- "queryForApplications:webDomains:categories:interval:focalOnly:error:"
- "queryForApplications:webDomains:categories:interval:segmentInterval:error:"
- "v44@0:8@16@24B32@?36"

```
