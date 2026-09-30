## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/Versions/A/WiFiAnalytics`

```diff

-  __TEXT.__text: 0x160264
-  __TEXT.__objc_methlist: 0x105e0
+  __TEXT.__text: 0x160d54
+  __TEXT.__objc_methlist: 0x10678
   __TEXT.__const: 0x3e8
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x14831
-  __TEXT.__oslogstring: 0x11bd4
+  __TEXT.__cstring: 0x14cb8
+  __TEXT.__oslogstring: 0x118d3
   __TEXT.__constg_swiftt: 0x1e0
   __TEXT.__swift5_typeref: 0x154
   __TEXT.__swift5_reflstr: 0xb1

   __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x2570
-  __TEXT.__unwind_info: 0x2ad0
+  __TEXT.__unwind_info: 0x2af0
   __TEXT.__eh_frame: 0x2d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf20
-  __DATA_CONST.__objc_classlist: 0x480
+  __DATA_CONST.__const: 0xf00
+  __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c70
+  __DATA_CONST.__objc_selrefs: 0x8cc8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x388
+  __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0xa40
-  __DATA_CONST.__got: 0x7a8
-  __AUTH_CONST.__const: 0x25a0
+  __DATA_CONST.__got: 0x7b0
+  __AUTH_CONST.__const: 0x2330
   __AUTH_CONST.__cfstring: 0xef20
-  __AUTH_CONST.__objc_const: 0x16c20
+  __AUTH_CONST.__objc_const: 0x16dc0
   __AUTH_CONST.__objc_arrayobj: 0x8b8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x748
-  __AUTH.__objc_data: 0x548
-  __DATA.__objc_ivar: 0xfdc
+  __AUTH.__objc_data: 0x458
+  __DATA.__objc_ivar: 0xff4
   __DATA.__data: 0x398
-  __DATA.__bss: 0x28
-  __DATA.__common: 0x11d0
+  __DATA.__bss: 0x1c
+  __DATA.__common: 0x410
   __DATA_DIRTY.__objc_ivar: 0x120
-  __DATA_DIRTY.__objc_data: 0x2a08
+  __DATA_DIRTY.__objc_data: 0x2b48
   __DATA_DIRTY.__data: 0xa0
-  __DATA_DIRTY.__bss: 0x160
-  __DATA_DIRTY.__common: 0x28
+  __DATA_DIRTY.__bss: 0x168
+  __DATA_DIRTY.__common: 0xde8
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6084
-  Symbols:   10990
-  CStrings:  5976
+  Functions: 6097
+  Symbols:   11000
+  CStrings:  5978
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[WAUtil getMessageInstanceForKey:andGroupType:encodedSizeOut:]
+ -[WAClient _failInvocation:withError:]
+ -[WAModelTemplateLRU .cxx_destruct]
+ -[WAModelTemplateLRU _removeKey:]
+ -[WAModelTemplateLRU budgetEncodedBytes]
+ -[WAModelTemplateLRU entryCount]
+ -[WAModelTemplateLRU evictionCount]
+ -[WAModelTemplateLRU initWithBudgetBytes:]
+ -[WAModelTemplateLRU removeAllObjects]
+ -[WAModelTemplateLRU setTemplate:forKey:encodedSize:]
+ -[WAModelTemplateLRU templateForKey:]
+ -[WAModelTemplateLRU totalEncodedBytes]
+ GCC_except_table102
+ GCC_except_table108
+ GCC_except_table116
+ GCC_except_table126
+ GCC_except_table135
+ GCC_except_table139
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table154
+ GCC_except_table160
+ GCC_except_table166
+ GCC_except_table173
+ GCC_except_table185
+ GCC_except_table191
+ GCC_except_table197
+ GCC_except_table203
+ GCC_except_table209
+ GCC_except_table215
+ GCC_except_table221
+ GCC_except_table226
+ GCC_except_table42
+ GCC_except_table60
+ GCC_except_table78
+ GCC_except_table84
+ GCC_except_table90
+ GCC_except_table96
+ OBJC_IVAR_$_WAModelTemplateLRU._budgetEncodedBytes
+ OBJC_IVAR_$_WAModelTemplateLRU._evictionCount
+ OBJC_IVAR_$_WAModelTemplateLRU._keyToEncodedSize
+ OBJC_IVAR_$_WAModelTemplateLRU._keyToTemplate
+ OBJC_IVAR_$_WAModelTemplateLRU._lruOrder
+ OBJC_IVAR_$_WAModelTemplateLRU._totalEncodedBytes
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$_WAModelTemplateLRU
+ _OBJC_METACLASS_$_WAModelTemplateLRU
+ __OBJC_$_INSTANCE_METHODS_WAModelTemplateLRU
+ __OBJC_$_INSTANCE_VARIABLES_WAModelTemplateLRU
+ __OBJC_$_PROP_LIST_WAModelTemplateLRU
+ __OBJC_CLASS_RO_$_WAModelTemplateLRU
+ __OBJC_METACLASS_RO_$_WAModelTemplateLRU
+ ___101-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke_3
+ ___38-[WAClient _failInvocation:withError:]_block_invoke
+ ___50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke_2
+ ___52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke_2
+ ___56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke_3
+ ___62-[WAClient _processManagedFault:at:andReply:queuedInvocation:]_block_invoke_2
+ ___63-[WAClient _submitMessage:groupType:andReply:queuedInvocation:]_block_invoke_3
+ ___64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke_3
+ ___65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke_2
+ ___68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke_3
+ ___68-[WAClient _signalPotentialNewIORChannelsAndReply:queuedInvocation:]_block_invoke_2
+ ___70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke_2
+ ___70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke_2
+ ___71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke_3
+ ___74-[WAClient _triggerQueryForNWActivityWithPeers:andReply:queuedInvocation:]_block_invoke_2
+ ___75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke_2
+ ___78-[WAClient _getNewMessageForKey:groupType:withCopy:andReply:queuedInvocation:]_block_invoke_3
+ ___80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke_3
+ ___87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke_3
+ ___88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke_3
+ ___91-[WAClient _updateRoamPoliciesForSourceBssid:andUpdateRoamCache:andReply:queuedInvocation:]_block_invoke_2
+ ___93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke_2
+ ___95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8l
+ _objc_msgSend$_failInvocation:withError:
+ _objc_msgSend$_removeKey:
+ _objc_msgSend$getMessageInstanceForKey:andGroupType:encodedSizeOut:
+ _objc_msgSend$orderedSet
- GCC_except_table106
- GCC_except_table112
- GCC_except_table124
- GCC_except_table129
- GCC_except_table142
- GCC_except_table158
- GCC_except_table164
- GCC_except_table171
- GCC_except_table189
- GCC_except_table195
- GCC_except_table201
- GCC_except_table207
- GCC_except_table213
- GCC_except_table219
- GCC_except_table224
- GCC_except_table70
- GCC_except_table76
- GCC_except_table82
- GCC_except_table88
- GCC_except_table94
- ___block_descriptor_32_e17_v16?0"NSError"8l
CStrings:
+ "%{public}s::%d:Evicted template key=%@ encodedBytes=%lu (totalAfter=%lu, budget=%lu)"
+ "%{public}s::%d:WAModelTemplateLRU: accounting drift detected, totalBytes=%lu < entrySize=%lu for key=%@"
+ "%{public}s::%d:XPC: WAClient - %@ - error: %@"
+ "+[WAUtil getMessageInstanceForKey:andGroupType:encodedSizeOut:]"
+ "-[WAClient _failInvocation:withError:]"
+ "-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _processManagedFault:at:andReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _signalPotentialNewIORChannelsAndReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _triggerQueryForNWActivityWithPeers:andReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient _updateRoamPoliciesForSourceBssid:andUpdateRoamCache:andReply:queuedInvocation:]_block_invoke_2"
+ "-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke_2"
+ "-[WAModelTemplateLRU _removeKey:]"
+ "-[WAModelTemplateLRU setTemplate:forKey:encodedSize:]"
+ "WiFiAnalytics-830.53 Jun 29 2026 21:23:04"
- "%{public}s::%d:XPC: WAClient - _issueIOReportManagementCommand - error: %@"
- "%{public}s::%d:XPC: WAClient - _sendMemoryPressureRequestAndReply - error: %@"
- "%{public}s::%d:XPC: WAClient - clearMessageStoreAndReply - error: %@"
- "%{public}s::%d:XPC: WAClient - error: %@"
- "%{public}s::%d:XPC: WAClient - getDeviceAnalyticsConfigurationAndReply - error: %@"
- "%{public}s::%d:XPC: WAClient - getDpsStatsandReply - error: %@"
- "%{public}s::%d:XPC: WAClient - getMessagesModelAndReply - error: %@"
- "%{public}s::%d:XPC: WAClient - getNewMessageForKey - error: %@"
- "%{public}s::%d:XPC: WAClient - killDaemonAndReply - error: %@"
- "%{public}s::%d:XPC: WAClient - lqmCrashTracerNotify - error: %@"
- "%{public}s::%d:XPC: WAClient - lqmCrashTracerReceiveBlock - error: %@"
- "%{public}s::%d:XPC: WAClient - registerMessageGroup - error: %@"
- "%{public}s::%d:XPC: WAClient - setDeviceAnalyticsConfiguration - error: %@"
- "%{public}s::%d:XPC: WAClient - submitMessage - error: %@"
- "%{public}s::%d:XPC: WAClient - trapCrashMiniTracerDumpReady - error: %@"
- "+[WAUtil getMessageInstanceForKey:andGroupType:]"
- "WiFiAnalytics-830.49 Jun 12 2026 00:36:40"
- "WiFiAnalytics-830.49 Jun 12 2026 00:36:41"

```
