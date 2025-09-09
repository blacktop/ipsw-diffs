## CoreDiagnostics

> `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics`

```diff

 47.0.0.0.0
-  __TEXT.__text: 0x4bfcc
-  __TEXT.__auth_stubs: 0x1c20
+  __TEXT.__text: 0x4ca8c
+  __TEXT.__auth_stubs: 0x1c60
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_methlist: 0xa0c
-  __TEXT.__const: 0x3cc4
-  __TEXT.__cstring: 0x61b2
-  __TEXT.__oslogstring: 0x16a1
+  __TEXT.__objc_methlist: 0xa24
+  __TEXT.__const: 0x3cd4
+  __TEXT.__cstring: 0x62a2
+  __TEXT.__oslogstring: 0x1761
   __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__swift5_typeref: 0xf74
+  __TEXT.__swift5_typeref: 0xf86
   __TEXT.__swift5_capture: 0x2d0
-  __TEXT.__constg_swiftt: 0xf60
+  __TEXT.__constg_swiftt: 0xf70
   __TEXT.__swift5_reflstr: 0x6d7
   __TEXT.__swift5_fieldmd: 0xf80
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x10c0
+  __TEXT.__unwind_info: 0x10e8
   __TEXT.__eh_frame: 0x15f8
   __TEXT.__objc_classname: 0x119
-  __TEXT.__objc_methname: 0x2049
+  __TEXT.__objc_methname: 0x2084
   __TEXT.__objc_methtype: 0x70d
-  __TEXT.__objc_stubs: 0x1d40
-  __DATA_CONST.__got: 0x450
+  __TEXT.__objc_stubs: 0x1d60
+  __DATA_CONST.__got: 0x470
   __DATA_CONST.__const: 0x540
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d8
+  __DATA_CONST.__objc_selrefs: 0x9e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0xe20
-  __AUTH_CONST.__const: 0x32d8
-  __AUTH_CONST.__cfstring: 0x53e0
+  __AUTH_CONST.__auth_got: 0xe40
+  __AUTH_CONST.__const: 0x3330
+  __AUTH_CONST.__cfstring: 0x5400
   __AUTH_CONST.__objc_const: 0x16b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH.__objc_data: 0x688
+  __AUTH.__objc_data: 0x690
   __AUTH.__data: 0x2c8
   __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0xa98
+  __DATA.__data: 0xac8
   __DATA.__bss: 0x5610
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x4d0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D441E820-8390-3DC2-A623-E6EEC6C5C428
-  Functions: 1557
-  Symbols:   1732
-  CStrings:  2144
+  UUID: CF95156D-A103-39CA-A6B9-2591FCCB6FF1
+  Functions: 1568
+  Symbols:   1738
+  CStrings:  2157
 
Symbols:
+ __CLASS_METHODS__TtC15CoreDiagnostics27TextualRepresentationBridge
+ ___swift_memcpy4_4
+ _objc_msgSend$formatMTEPageTags:report:
+ _symbolic Say_____G s6UInt64V
+ _symbolic ypSgSg
CStrings:
+ "Address Range: [Start, End)"
+ "MTE Malloc Size Class: "
+ "MTE Page Tags (faulting address: %p)"
+ "Process:             $(procName|\"???\") [$(pid)]\nPath:                $(procPath|\"???\")\nIdentifier:          $(bundleInfo.CFBundleIdentifier|procName|\"???\")\n^(bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleShortVersionString) ($(bundleInfo.CFBundleVersion|\"???\"))\n^(!bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleVersion|\"???\")\n^(buildInfo.ProductBuildVersion)Build Info:          $(buildInfo.ProjectName|\"Unknown\")-$(buildInfo.SourceVersion|\"Unknown\")~$(buildInfo.BuildVersion|\"Unknown\") ($(buildInfo.ProductBuildVersion))\n^(buildInfo&!buildInfo.ProductBuildVersion)Build Info:          $(buildInfo.ProjectName|\"Unknown\")-$(buildInfo.SourceVersion|\"Unknown\")~$(buildInfo.BuildVersion|\"Unknown\")\n^(bundleInfo.DTAppStoreToolsBuild)AppStoreTools:       $(bundleInfo.DTAppStoreToolsBuild)\n^(storeInfo.applicationVariant)AppVariant:          $(storeInfo.applicationVariant)\n^(isBeta)Beta:                YES\n^(!*translated)Code Type:           $(cpuType) (Native)\n^(*translated)Code Type:           $(cpuType) (Translated)\nRole:                $(procRole|\"Unspecified\")\nParent Process:      $(parentProc|\"???\") [$(parentPid|\"Unknown\")]\nCoalition:           $(coalitionName|\"<none>\") [$(coalitionID)]\n^(responsiblePid&responsibleProc)Responsible Process: $(responsibleProc) [$(responsiblePid)]\n^(responsiblePid&!responsibleProc)Responsible PID:     $(responsiblePid)\nUser ID:             $(userID)\n\n^(plugin)PlugIn Path:             $(plugin.ExecutablePath)\n^(plugin)PlugIn Identifier:       $(plugin.Identifier)\n^(plugin)PlugIn Version:          $(plugin.ShortVersionString) ($(plugin.Version|\"???\"))\n^(plugin)\nDate/Time:           $(captureTime)\nLaunch Time:         $(procLaunch)\nHardware Model:      $(modelCode)\n^(codeName)Device Model:        $(codeName)\nOS Version:          $(osVersion.train) ($(osVersion.build))\nRelease Type:        $(osVersion.releaseType)\n^(bridgeVersion.train)Bridge OS Version:     $(bridgeVersion.train) ($(bridgeVersion.build))\n^(bridgeVersion.status)Bridge OS Version:     $(bridgeVersion.status)\n^(basebandVersion)Baseband Version:    $(basebandVersion)\n\n^(!isBeta)Crash Reporter Key:  $(crashReporterKey)\n^(isBeta)Beta Identifier:     $(storeInfo.deviceIdentifierForVendor|\"Unknown\")\n^(systemID)UDID:                $(systemID)\nIncident Identifier: $(metadata:incident_id)\n\n^(sleepWakeUUID)Sleep/Wake UUID:       $(sleepWakeUUID)\n^(sleepWakeUUID)\n^(uptime)Time Awake Since Boot: $(uptime) seconds\n^(wakeTime)Time Since Wake:       $(wakeTime) seconds\n^(sip)\n^(sip)System Integrity Protection: $(sip)\n\n^(legacyInfo.threadTriggered.name&legacyInfo.threadTriggered.queue)Triggered by Thread: $(faultingThread)  $(legacyInfo.threadTriggered.name), Dispatch Queue: $(legacyInfo.threadTriggered.queue)\n^(legacyInfo.threadTriggered.name&!legacyInfo.threadTriggered.queue)Triggered by Thread: $(faultingThread)  $(legacyInfo.threadTriggered.name)\n^(!legacyInfo.threadTriggered.name&legacyInfo.threadTriggered.queue)Triggered by Thread: $(faultingThread), Dispatch Queue: $(legacyInfo.threadTriggered.queue)\n^(!legacyInfo.threadTriggered.name&!legacyInfo.threadTriggered.queue)Triggered by Thread: $(faultingThread)\n^(!faultingThread&legacyInfo.threadHighlighted)Highlighted by Thread: $(legacyInfo.threadHighlighted)\n^(!faultingThread&!legacyInfo.threadHighlighted)Triggered by Thread: Unknown\n\n^(exception.signal)Exception Type:    $(exception.type) ($(exception.signal))\n^(!exception.signal)Exception Type:    $(exception.type)\n^(exception.subtype)Exception Subtype: $(exception.subtype)\n^(exception.message)Exception Message: $(exception.message)\n^(exception.rawCodes)Exception Codes:   $(exception.rawCodes)\n^(exceptionReason.composed_message)Exception Reason:  $(exceptionReason.composed_message)\n^(simulatedCaller)Exception Note:    SIMULATED (this is NOT a crash) requested by $(simulatedCaller)\n^(!simulatedCaller&isSimulated)Exception Note:    SIMULATED (this is NOT a crash)\n^(!isSimulated&isCorpse)Exception Note:    EXC_CORPSE_NOTIFY\n^(!isSimulated&isNonFatal)Exception Note:    NON-FATAL CONDITION (this is NOT a crash)\n\n^(termination)Termination Reason:  Namespace $(termination.namespace), Code $(termination.code), $(termination.indicator)\n^(termination.reasons)$(termination.reasons)\n^(termination.details)$(termination.details)\n^(termination.byPid)Terminating Process: $(termination.byProc|\"<unknown>\") [$(termination.byPid)]\n^(termination)\n^(fatalDyldError)Dyld Error Message:\n^(fatalDyldError)  $(fatalDyldError)\n^(fatalDyldError)\n\n#(format_workQueueLimit\n$(<key>) Reached: $(<value>) (too many dispatch threads blocked in synchronous operations)\n)#\n^(workQueueLimits)$(format_workQueueLimit#workQueueLimits)\n^(*extMods.warnings)External Modification Warnings:\n^(*extMods.targeted.thread_create)Thread creation by external task.\n^(*extMods.targeted.thread_set_state)Debugger attached to process.\n^(*extMods.caller.task_for_pid)Process used task_for_pid().\n^(*extMods.warnings)\n^(vmRegionInfo)VM Region Info: $(vmRegionInfo)\n^(vmRegionInfo)\n^(externalGPUInfo)$(externalGPUInfo)\n^(externalGPUInfo)\n^(asi)Application Specific Information:\n#(format_asi\n$(<value>)\n)#\n^(asi)$(format_asi#asi)\n^(asi)\n^(asiSignatures)Application Specific Signatures:\n^(asiSignatures)$(asiSignatures)\n^(asiSignatures)\n#(format_asiBacktraces\nApplication Specific Backtrace $(<index>):\n$(<item>)\n)#\n^(asiBacktraces)$(format_asiBacktraces#asiBacktraces)\n^(asiBacktraces)\n^(dyldMessages)Dyld Error Message:$(dyldMessages)\n^(dyldMessages)\n^(lastExceptionBacktrace)Last Exception Backtrace:\n^(lastExceptionBacktrace)$(lastExceptionBacktrace)\n^(lastExceptionBacktrace)\n^(ktriageinfo)Kernel Triage:\n^(ktriageinfo)$(ktriageinfo)\n^(ktriageinfo)\n$(threads|\"Backtrace not available\")\n\n$(threadState|\"No thread state (register information) available\")\n\nBinary Images:\n$(usedImages|\"Binary images description not available\")\n\n^(extMods)External Modification Summary:\n^(extMods)  Calls made by other processes targeting this process:\n^(extMods)    task_for_pid: $(extMods.targeted.task_for_pid)\n^(extMods)    thread_create: $(extMods.targeted.thread_create)\n^(extMods)    thread_set_state: $(extMods.targeted.thread_set_state)\n^(extMods)  Calls made by this process:\n^(extMods)    task_for_pid: $(extMods.caller.task_for_pid)\n^(extMods)    thread_create: $(extMods.caller.thread_create)\n^(extMods)    thread_set_state: $(extMods.caller.thread_set_state)\n^(extMods)  Calls made by all processes on this machine:\n^(extMods)    task_for_pid: $(extMods.system.task_for_pid)\n^(extMods)    thread_create: $(extMods.system.thread_create)\n^(extMods)    thread_set_state: $(extMods.system.thread_set_state)\n^(extMods)\n^(vmSummary)VM Region Summary:\n^(vmSummary)$(vmSummary)\n^(vmSummary)\n^(mtePageTags)$(mtePageTags)\n^(reportNotes)Error Formulating Crash Report:\n^(reportNotes)$(reportNotes)\n^(reportNotes)\n^(filteredLog)Filtered log messages:\n^(filteredLog)$(filteredLog)\n^(filteredLog)\n#(format_diagnosticOutput\nDiagnostic Output: $(<key>)\n$(<value>)\n)#\n^(diagnosticOutput)$(format_diagnosticOutput#diagnosticOutput)\n^(diagnosticOutput)"
+ "Report has missing or malformed exception codes."
+ "Unable to determine malloc size class for empty MTE tags"
+ "Unable to determine malloc size class for uniform MTE tags"
+ "__swift_objectForKeyedSubscript:"
+ "com.apple.corediagnostics.visualization"
+ "formatMTEPageTags:report:"
+ "mtePageTags"
+ "textualRepresentation"
- "Process:             $(procName|\"???\") [$(pid)]\nPath:                $(procPath|\"???\")\nIdentifier:          $(bundleInfo.CFBundleIdentifier|procName|\"???\")\n^(bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleShortVersionString) ($(bundleInfo.CFBundleVersion|\"???\"))\n^(!bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleVersion|\"???\")\n^(buildInfo.ProductBuildVersion)Build Info:          $(buildInfo.ProjectName|\"Unknown\")-$(buildInfo.SourceVersion|\"Unknown\")~$(buildInfo.BuildVersion|\"Unknown\") ($(buildInfo.ProductBuildVersion))\n^(buildInfo&!buildInfo.ProductBuildVersion)Build Info:          $(buildInfo.ProjectName|\"Unknown\")-$(buildInfo.SourceVersion|\"Unknown\")~$(buildInfo.BuildVersion|\"Unknown\")\n^(bundleInfo.DTAppStoreToolsBuild)AppStoreTools:       $(bundleInfo.DTAppStoreToolsBuild)\n^(storeInfo.applicationVariant)AppVariant:          $(storeInfo.applicationVariant)\n^(isBeta)Beta:                YES\n^(!*translated)Code Type:           $(cpuType) (Native)\n^(*translated)Code Type:           $(cpuType) (Translated)\nRole:                $(procRole|\"Unspecified\")\nParent Process:      $(parentProc|\"???\") [$(parentPid|\"Unknown\")]\nCoalition:           $(coalitionName|\"<none>\") [$(coalitionID)]\n^(responsiblePid&responsibleProc)Responsible Process: $(responsibleProc) [$(responsiblePid)]\n^(responsiblePid&!responsibleProc)Responsible PID:     $(responsiblePid)\nUser ID:             $(userID)\n\n^(plugin)PlugIn Path:             $(plugin.ExecutablePath)\n^(plugin)PlugIn Identifier:       $(plugin.Identifier)\n^(plugin)PlugIn Version:          $(plugin.ShortVersionString) ($(plugin.Version|\"???\"))\n^(plugin)\nDate/Time:           $(captureTime)\nLaunch Time:         $(procLaunch)\nHardware Model:      $(modelCode)\n^(codeName)Device Model:        $(codeName)\nOS Version:          $(osVersion.train) ($(osVersion.build))\nRelease Type:        $(osVersion.releaseType)\n^(bridgeVersion.train)Bridge OS Version:     $(bridgeVersion.train) ($(bridgeVersion.build))\n^(bridgeVersion.status)Bridge OS Version:     $(bridgeVersion.status)\n^(basebandVersion)Baseband Version:    $(basebandVersion)\n\n^(!isBeta)Crash Reporter Key:  $(crashReporterKey)\n^(isBeta)Beta Identifier:     $(storeInfo.deviceIdentifierForVendor|\"Unknown\")\n^(systemID)UDID:                $(systemID)\nIncident Identifier: $(metadata:incident_id)\n\n^(sleepWakeUUID)Sleep/Wake UUID:       $(sleepWakeUUID)\n^(sleepWakeUUID)\n^(uptime)Time Awake Since Boot: $(uptime) seconds\n^(wakeTime)Time Since Wake:       $(wakeTime) seconds\n^(sip)\n^(sip)System Integrity Protection: $(sip)\n\n^(legacyInfo.threadTriggered.name&legacyInfo.threadTriggered.queue)Triggered by Thread: $(faultingThread)  $(legacyInfo.threadTriggered.name), Dispatch Queue: $(legacyInfo.threadTriggered.queue)\n^(legacyInfo.threadTriggered.name&!legacyInfo.threadTriggered.queue)Triggered by Thread: $(faultingThread)  $(legacyInfo.threadTriggered.name)\n^(!legacyInfo.threadTriggered.name&legacyInfo.threadTriggered.queue)Triggered by Thread: $(faultingThread), Dispatch Queue: $(legacyInfo.threadTriggered.queue)\n^(!legacyInfo.threadTriggered.name&!legacyInfo.threadTriggered.queue)Triggered by Thread: $(faultingThread)\n^(!faultingThread&legacyInfo.threadHighlighted)Highlighted by Thread: $(legacyInfo.threadHighlighted)\n^(!faultingThread&!legacyInfo.threadHighlighted)Triggered by Thread: Unknown\n\n^(exception.signal)Exception Type:    $(exception.type) ($(exception.signal))\n^(!exception.signal)Exception Type:    $(exception.type)\n^(exception.subtype)Exception Subtype: $(exception.subtype)\n^(exception.message)Exception Message: $(exception.message)\n^(exception.rawCodes)Exception Codes:   $(exception.rawCodes)\n^(exceptionReason.composed_message)Exception Reason:  $(exceptionReason.composed_message)\n^(simulatedCaller)Exception Note:    SIMULATED (this is NOT a crash) requested by $(simulatedCaller)\n^(!simulatedCaller&isSimulated)Exception Note:    SIMULATED (this is NOT a crash)\n^(!isSimulated&isCorpse)Exception Note:    EXC_CORPSE_NOTIFY\n^(!isSimulated&isNonFatal)Exception Note:    NON-FATAL CONDITION (this is NOT a crash)\n\n^(termination)Termination Reason:  Namespace $(termination.namespace), Code $(termination.code), $(termination.indicator)\n^(termination.reasons)$(termination.reasons)\n^(termination.details)$(termination.details)\n^(termination.byPid)Terminating Process: $(termination.byProc|\"<unknown>\") [$(termination.byPid)]\n^(termination)\n^(fatalDyldError)Dyld Error Message:\n^(fatalDyldError)  $(fatalDyldError)\n^(fatalDyldError)\n\n#(format_workQueueLimit\n$(<key>) Reached: $(<value>) (too many dispatch threads blocked in synchronous operations)\n)#\n^(workQueueLimits)$(format_workQueueLimit#workQueueLimits)\n^(*extMods.warnings)External Modification Warnings:\n^(*extMods.targeted.thread_create)Thread creation by external task.\n^(*extMods.targeted.thread_set_state)Debugger attached to process.\n^(*extMods.caller.task_for_pid)Process used task_for_pid().\n^(*extMods.warnings)\n^(vmRegionInfo)VM Region Info: $(vmRegionInfo)\n^(vmRegionInfo)\n^(externalGPUInfo)$(externalGPUInfo)\n^(externalGPUInfo)\n^(asi)Application Specific Information:\n#(format_asi\n$(<value>)\n)#\n^(asi)$(format_asi#asi)\n^(asi)\n^(asiSignatures)Application Specific Signatures:\n^(asiSignatures)$(asiSignatures)\n^(asiSignatures)\n#(format_asiBacktraces\nApplication Specific Backtrace $(<index>):\n$(<item>)\n)#\n^(asiBacktraces)$(format_asiBacktraces#asiBacktraces)\n^(asiBacktraces)\n^(dyldMessages)Dyld Error Message:$(dyldMessages)\n^(dyldMessages)\n^(lastExceptionBacktrace)Last Exception Backtrace:\n^(lastExceptionBacktrace)$(lastExceptionBacktrace)\n^(lastExceptionBacktrace)\n^(ktriageinfo)Kernel Triage:\n^(ktriageinfo)$(ktriageinfo)\n^(ktriageinfo)\n$(threads|\"Backtrace not available\")\n\n$(threadState|\"No thread state (register information) available\")\n\nBinary Images:\n$(usedImages|\"Binary images description not available\")\n\n^(extMods)External Modification Summary:\n^(extMods)  Calls made by other processes targeting this process:\n^(extMods)    task_for_pid: $(extMods.targeted.task_for_pid)\n^(extMods)    thread_create: $(extMods.targeted.thread_create)\n^(extMods)    thread_set_state: $(extMods.targeted.thread_set_state)\n^(extMods)  Calls made by this process:\n^(extMods)    task_for_pid: $(extMods.caller.task_for_pid)\n^(extMods)    thread_create: $(extMods.caller.thread_create)\n^(extMods)    thread_set_state: $(extMods.caller.thread_set_state)\n^(extMods)  Calls made by all processes on this machine:\n^(extMods)    task_for_pid: $(extMods.system.task_for_pid)\n^(extMods)    thread_create: $(extMods.system.thread_create)\n^(extMods)    thread_set_state: $(extMods.system.thread_set_state)\n^(extMods)\n^(vmSummary)VM Region Summary:\n^(vmSummary)$(vmSummary)\n^(vmSummary)\n^(reportNotes)Error Formulating Crash Report:\n^(reportNotes)$(reportNotes)\n^(reportNotes)\n^(filteredLog)Filtered log messages:\n^(filteredLog)$(filteredLog)\n^(filteredLog)\n#(format_diagnosticOutput\nDiagnostic Output: $(<key>)\n$(<value>)\n)#\n^(diagnosticOutput)$(format_diagnosticOutput#diagnosticOutput)\n^(diagnosticOutput)"

```
