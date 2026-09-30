## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

```diff

-727.80.2.0.0
-  __TEXT.__text: 0x3f19c
+758.100.41.0.0
+  __TEXT.__text: 0x3f730
   __TEXT.__auth_stubs: 0x1440
-  __TEXT.__objc_methlist: 0x18d8
+  __TEXT.__objc_methlist: 0x1a50
   __TEXT.__const: 0x5e0
-  __TEXT.__oslogstring: 0x3378
-  __TEXT.__cstring: 0x90a3
-  __TEXT.__gcc_except_tab: 0x11e4
+  __TEXT.__oslogstring: 0x3419
+  __TEXT.__cstring: 0x91cc
+  __TEXT.__gcc_except_tab: 0x1208
   __TEXT.__dlopen_cstrs: 0x163
-  __TEXT.__unwind_info: 0xa28
+  __TEXT.__unwind_info: 0xa90
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_classname: 0x328
-  __TEXT.__objc_methname: 0x4cc5
+  __TEXT.__objc_methname: 0x4cf6
   __TEXT.__objc_methtype: 0xc67
-  __TEXT.__objc_stubs: 0x4540
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x1110
+  __TEXT.__objc_stubs: 0x4580
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__const: 0x11c0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1478
+  __DATA_CONST.__objc_selrefs: 0x1510
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xc60
   __AUTH_CONST.__auth_got: 0xa30
-  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0xa2a0
-  __AUTH_CONST.__objc_const: 0x38f0
+  __AUTH_CONST.__cfstring: 0xa3e0
+  __AUTH_CONST.__objc_const: 0x36a0
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x4b0
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x2b8
+  __DATA.__objc_ivar: 0x2bc
   __DATA.__data: 0x168
-  __DATA.__bss: 0x140
+  __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x290
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 949
-  Symbols:   1597
-  CStrings:  2962
+  Functions: 965
+  Symbols:   1625
+  CStrings:  2979
 
Symbols:
+ _OSAIsConfiguredRSDDevice
+ _OSAIsConfiguredRSDHost
- _OSAIsDebugEnabledForRSD
CStrings:
+ "\nIncident Identifier: $(metadata:incident_id)\n^(!isBeta)CrashReporter Key:   $(crashReporterKey)\n^(isBeta)Beta Identifier:     $(storeInfo.deviceIdentifierForVendor|\"Unknown\")\nHardware Model:      $(modelCode)\n^(codeName)Device Model:        $(codeName)\nProcess:             $(procName|\"???\") [$(pid)]\nPath:                $(procPath|\"???\")\nIdentifier:          $(bundleInfo.CFBundleIdentifier|procName|\"???\")\n^(bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleShortVersionString) ($(bundleInfo.CFBundleVersion|\"???\"))\n^(!bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleVersion|\"???\")\n^(bundleInfo.DTAppStoreToolsBuild)AppStoreTools:       $(bundleInfo.DTAppStoreToolsBuild)\n^(storeInfo.applicationVariant)AppVariant:          $(storeInfo.applicationVariant)\n^(isBeta)Beta:                YES\n^(!*translated)Code Type:           $(cpuType) (Native)\n^(*translated)Code Type:           $(cpuType) (Translated)\nRole:                $(procRole|\"Unspecified\")\nParent Process:      $(parentProc|\"???\") [$(parentPid|\"Unknown\")]\nCoalition:           $(coalitionName|\"<none>\") [$(coalitionID)]\n^(responsiblePid)Responsible Process: $(responsibleProc) [$(responsiblePid)]\n\nDate/Time:           $(captureTime)\nLaunch Time:         $(procLaunch)\nOS Version:          $(osVersion.train) ($(osVersion.build))\nRelease Type:        $(osVersion.releaseType)\n^(basebandVersion)Baseband Version:    $(basebandVersion)\n^(systemID)UDID:                $(systemID)\nReport Version:      104\n\n^(exception.signal)Exception Type:  $(exception.type) ($(exception.signal))\n^(!exception.signal)Exception Type:  $(exception.type)\n^(exception.subtype)Exception Subtype: $(exception.subtype)\n^(exception.message)Exception Message: $(exception.message)\n^(exception.rawCodes)Exception Codes: $(exception.rawCodes)\n^(vmRegionInfo)VM Region Info: $(vmRegionInfo)\n^(simulatedCaller)Exception Note:  SIMULATED (this is NOT a crash) requested by $(simulatedCaller)\n^(!simulatedCaller&isSimulated)Exception Note:  SIMULATED (this is NOT a crash)\n^(!isSimulated&isCorpse)Exception Note:  EXC_CORPSE_NOTIFY\n^(!isSimulated&isNonFatal)Exception Note:  NON-FATAL CONDITION (this is NOT a crash)\n^(termination)Termination Reason: $(termination.namespace) $(termination.code) $(termination.indicator)\n^(termination.reasons)$(termination.reasons)\n^(termination.details)$(termination.details)\n^(termination.byPid)Terminating Process: $(termination.byProc|\"<unknown>\") [$(termination.byPid)]\n^(termination)\n^(faultingThread)Triggered by Thread:  $(faultingThread)\n^(!faultingThread&legacyInfo.threadHighlighted)Highlighted by Thread:  $(legacyInfo.threadHighlighted)\n^(!faultingThread&!legacyInfo.threadHighlighted)Triggered by Thread:  Unknown\n\n^(asi)Application Specific Information:\n#(format_asi\n$(<value>)\n)#\n^(asi)$(format_asi#asi)\n^(asi)\n^(dyldMessages)Dyld Error Message:$(dyldMessages)\n^(dyldMessages)\n^(lastExceptionBacktrace)Last Exception Backtrace:\n^(lastExceptionBacktrace)$(lastExceptionBacktrace)\n^(lastExceptionBacktrace)\n^(ktriageinfo)Kernel Triage:\n^(ktriageinfo)$(ktriageinfo)\n^(ktriageinfo)\n$(threads|\"Backtrace not available\")\n\n$(threadState|\"No thread state (register information) available\")\n\nBinary Images:\n$(usedImages|\"Binary images description not available\")\n\n^(reportNotes)Error Formulating Crash Report:\n^(reportNotes)$(reportNotes)\n^(reportNotes)\n^(filteredLog)Filtered syslog:\n^(filteredLog)$(filteredLog)\n^(filteredLog)\n#(format_diagnosticOutput\nDiagnostic Output: $(<key>)\n$(<value>)\n)#\n^(diagnosticOutput)$(format_diagnosticOutput#diagnosticOutput)\n^(diagnosticOutput)\nEOF\n"
+ "%@-seed"
+ "-restore"
+ "-upgrade"
+ "Carrier"
+ "CarrierSeed"
+ "Configured value for submissionsDisabledSince key is not in the expected format: deleting key"
+ "Seed"
+ "Submissions were disabled over a week ago: re-enabling submissions"
+ "_factoryDevice"
+ "codeSigningAuxiliaryInfo"
+ "com.apple.osanalytics.factoryproxysync"
+ "configureProxyDevice"
+ "configureProxyHost"
+ "factoryDevice"
+ "seed"
+ "submissionsDisabled"
+ "submissionsDisabledSince"
+ "v20@?0I8r^Q12"
+ "v20@?0I8r^{exclave_textlayout_segment=[16C]Q}12"
- "\nIncident Identifier: $(metadata:incident_id)\n^(!isBeta)CrashReporter Key:   $(crashReporterKey)\n^(isBeta)Beta Identifier:     $(storeInfo.deviceIdentifierForVendor|\"Unknown\")\nHardware Model:      $(modelCode)\n^(codeName)Device Model:        $(codeName)\nProcess:             $(procName|\"???\") [$(pid)]\nPath:                $(procPath|\"???\")\nIdentifier:          $(bundleInfo.CFBundleIdentifier|procName|\"???\")\n^(bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleShortVersionString) ($(bundleInfo.CFBundleVersion|\"???\"))\n^(!bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleVersion|\"???\")\n^(bundleInfo.DTAppStoreToolsBuild)AppStoreTools:       $(bundleInfo.DTAppStoreToolsBuild)\n^(storeInfo.applicationVariant)AppVariant:          $(storeInfo.applicationVariant)\n^(isBeta)Beta:                YES\nCode Type:           $(cpuType) (Native)\nRole:                $(procRole|\"Unspecified\")\nParent Process:      $(parentProc|\"???\") [$(parentPid|\"Unknown\")]\nCoalition:           $(coalitionName|\"<none>\") [$(coalitionID)]\n^(responsiblePid)Responsible Process: $(responsibleProc) [$(responsiblePid)]\n\nDate/Time:           $(captureTime)\nLaunch Time:         $(procLaunch)\nOS Version:          $(osVersion.train) ($(osVersion.build))\nRelease Type:        $(osVersion.releaseType)\n^(basebandVersion)Baseband Version:    $(basebandVersion)\n^(systemID)UDID:                $(systemID)\nReport Version:      104\n\n^(exception.signal)Exception Type:  $(exception.type) ($(exception.signal))\n^(!exception.signal)Exception Type:  $(exception.type)\n^(exception.subtype)Exception Subtype: $(exception.subtype)\n^(exception.message)Exception Message: $(exception.message)\n^(exception.rawCodes)Exception Codes: $(exception.rawCodes)\n^(vmRegionInfo)VM Region Info: $(vmRegionInfo)\n^(simulatedCaller)Exception Note:  SIMULATED (this is NOT a crash) requested by $(simulatedCaller)\n^(!simulatedCaller&isSimulated)Exception Note:  SIMULATED (this is NOT a crash)\n^(!isSimulated&isCorpse)Exception Note:  EXC_CORPSE_NOTIFY\n^(!isSimulated&isNonFatal)Exception Note:  NON-FATAL CONDITION (this is NOT a crash)\n^(termination)Termination Reason: $(termination.namespace) $(termination.code) $(termination.indicator)\n^(termination.reasons)$(termination.reasons)\n^(termination.details)$(termination.details)\n^(termination.byPid)Terminating Process: $(termination.byProc|\"<unknown>\") [$(termination.byPid)]\n^(termination)\n^(faultingThread)Triggered by Thread:  $(faultingThread)\n^(!faultingThread&legacyInfo.threadHighlighted)Highlighted by Thread:  $(legacyInfo.threadHighlighted)\n^(!faultingThread&!legacyInfo.threadHighlighted)Triggered by Thread:  Unknown\n\n^(asi)Application Specific Information:\n#(format_asi\n$(<value>)\n)#\n^(asi)$(format_asi#asi)\n^(asi)\n^(dyldMessages)Dyld Error Message:$(dyldMessages)\n^(dyldMessages)\n^(lastExceptionBacktrace)Last Exception Backtrace:\n^(lastExceptionBacktrace)$(lastExceptionBacktrace)\n^(lastExceptionBacktrace)\n^(ktriageinfo)Kernel Triage:\n^(ktriageinfo)$(ktriageinfo)\n^(ktriageinfo)\n$(threads|\"Backtrace not available\")\n\n$(threadState|\"No thread state (register information) available\")\n\nBinary Images:\n$(usedImages|\"Binary images description not available\")\n\n^(reportNotes)Error Formulating Crash Report:\n^(reportNotes)$(reportNotes)\n^(reportNotes)\n^(filteredLog)Filtered syslog:\n^(filteredLog)$(filteredLog)\n^(filteredLog)\n#(format_diagnosticOutput\nDiagnostic Output: $(<key>)\n$(<value>)\n)#\n^(diagnosticOutput)$(format_diagnosticOutput#diagnosticOutput)\n^(diagnosticOutput)\nEOF\n"
- "GM"
- "enableDebugProxySync"

```
