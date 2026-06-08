## CentauriDiagnostic

> `/System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic`

```diff

-92.0.0.0.0
-  __TEXT.__text: 0x6950
-  __TEXT.__auth_stubs: 0x2e0
+123.0.0.0.1
+  __TEXT.__text: 0x6504
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0xa1
-  __TEXT.__cstring: 0x194f
+  __TEXT.__cstring: 0x193e
   __TEXT.__oslogstring: 0xce1
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x71f
-  __TEXT.__objc_methtype: 0xc0
-  __TEXT.__objc_stubs: 0x7c0
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x148
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x8a0
   __AUTH_CONST.__objc_const: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x1e0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5B35C1E8-140A-383A-880C-D532E90DD032
-  Functions: 58
-  Symbols:   300
-  CStrings:  334
+  UUID: 81AC9CF5-8A87-328E-97D4-E725D47781BE
+  Functions: 56
+  Symbols:   298
+  CStrings:  233
 
Symbols:
+ ___block_literal_global.107
+ ___block_literal_global.109
+ ___block_literal_global.111
+ _getTotalSizeForPath.cold.1
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
- _OUTLINED_FUNCTION_2
- ___block_literal_global.108
- ___block_literal_global.110
- ___block_literal_global.112
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "^(COEX\\.rta\\.bin|BT2G\\.(dmem|imem|aslr)\\.bin|BT5G\\.(dmem|imem|aslr)\\.bin|BTLPS\\.(dmem|imem|aslr|regdump)\\.bin|BTMAIN\\.(apiram|dtcm|itcm|memswapptt|aslr|regdump|sram)\\.bin|BTSEC\\.(dtcm|itcm|aslr|regdump)\\.bin)(\\.synced)?$"
+ "^(COEX\\.rta\\.bin|BT2G\\.(dmem|imem|aslr)\\.bin|BT5G\\.(dmem|imem|aslr)\\.bin|BTLPS\\.(dmem|imem|aslr|regdump)\\.bin|BTMAIN\\.(apiram|dtcm|itcm|memswapptt|aslr|regdump|sram)\\.bin|BTSEC\\.(dtcm|itcm|aslr|regdump)\\.bin|MemSwapWorkingCopy\\.bin)(\\.synced)?$"
+ "^(COEX\\.rta\\.bin|WFL2G\\.(dmem|imem|aslr|recipeoverride|recipeoverridesram|regdump|rtmem|txscr)\\.bin|WFL5G\\.(dmem|imem|aslr|recipeoverride|recipeoverridesram|regdump|rtmem|txscr)\\.bin|WFMAIN\\.(dtcm|itcm|aslr|regdump|socram|sram|memswapptt)\\.bin|WFP2G\\.(dmem|imem|aslr|regdump|rtmem)\\.bin|WFP5G\\.(dmem|imem|aslr|regdump|rtmem)\\.bin|WFRX\\.(dmem|imem|aslr|regdump|rtmem)\\.bin|WFSC\\.(dmem|imem|aslr|regdump|rtmem)\\.bin|WFTX\\.(dmem|imem|aslr|regdump|rtmem)\\.bin|MemSwapWorkingCopy\\.bin)(\\.synced)?$"
+ "^(CentauriConfigAccessLog|CentauriEventLog|CentauriMSILog|CentauriPowerStateLog|CentauriStateDump|CentauriChipInfo)\\.txt(\\.synced)?$"
- ".cxx_destruct"
- "@\"NSDate\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSURL\""
- "@16@0:8"
- "@40@0:8@16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24Q32"
- "B48@0:8@16@24@32Q40"
- "CDFAlphaDiagnostics"
- "CDFBetaDiagnostics"
- "CDFCollectionItem"
- "CDFControlDiagnostics"
- "CDFSubsystemDiagnostics"
- "Q"
- "Q16@0:8"
- "T@\"NSDate\",R,V_date"
- "T@\"NSNumber\",R,V_size"
- "T@\"NSString\",R,V_name"
- "T@\"NSURL\",R,V_path"
- "TB,R,V_collectCoredumps"
- "TQ,R,V_buildEnv"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "^(COEX\\.rta\\.bin|BT2G\\.(dmem|imem|mxwrap)\\.bin|BT5G\\.(dmem|imem|mxwrap)\\.bin|BTLPS\\.(dmem|imem|mxwrap|regdump)\\.bin|BTMAIN\\.(apiram|dtcm|itcm|memswapptt|mxwrap|regdump|sram)\\.bin|BTSEC\\.(dtcm|itcm|mxwrap|regdump)\\.bin)(\\.synced)?$"
- "^(COEX\\.rta\\.bin|BT2G\\.(dmem|imem|mxwrap)\\.bin|BT5G\\.(dmem|imem|mxwrap)\\.bin|BTLPS\\.(dmem|imem|mxwrap|regdump)\\.bin|BTMAIN\\.(apiram|dtcm|itcm|memswapptt|mxwrap|regdump|sram)\\.bin|BTSEC\\.(dtcm|itcm|mxwrap|regdump)\\.bin|MemSwapWorkingCopy\\.bin)(\\.synced)?$"
- "^(COEX\\.rta\\.bin|WFL2G\\.(dmem|imem|mxwrap|recipeoverride|recipeoverridesram|regdump|rtmem|txscr)\\.bin|WFL5G\\.(dmem|imem|mxwrap|recipeoverride|recipeoverridesram|regdump|rtmem|txscr)\\.bin|WFMAIN\\.(dtcm|itcm|mxwrap|regdump|socram|sram|memswapptt)\\.bin|WFP2G\\.(dmem|imem|mxwrap|regdump|rtmem)\\.bin|WFP5G\\.(dmem|imem|mxwrap|regdump|rtmem)\\.bin|WFRX\\.(dmem|imem|mxwrap|regdump|rtmem)\\.bin|WFSC\\.(dmem|imem|mxwrap|regdump|rtmem)\\.bin|WFTX\\.(dmem|imem|mxwrap|regdump|rtmem)\\.bin|MemSwapWorkingCopy\\.bin)(\\.synced)?$"
- "^(CentauriConfigAccessLog|CentauriEventLog|CentauriMSILog|CentauriPowerStateLog|CentauriStateDump)\\.txt(\\.synced)?$"
- "_buildEnv"
- "_collectCoredumps"
- "_date"
- "_name"
- "_path"
- "_size"
- "addObject:"
- "addObjectsFromArray:"
- "allObjects"
- "array"
- "arrayWithObjects:count:"
- "boolValue"
- "buildEnv"
- "bundleIdentifier"
- "cStringUsingEncoding:"
- "code"
- "collectCCMetadataFrom:to:"
- "collectCoredumps"
- "collectFWLogsFrom:to:runtimeFlags:"
- "collectFileWithRegex:from:to:mostRecent:"
- "collectFilesWithRegex:from:to:"
- "collectFilesWithRegexes:from:to:mostRecent:"
- "collectLPMDebugDataFrom:to:"
- "collectLogsFrom:to:runtimeFlags:"
- "collectStateSnapshotsFrom:to:runtimeFlags:"
- "collectTextLogsFrom:to:"
- "collectTextLogsFrom:to:runtimeFlags:"
- "collectWLANPacketCapsFrom:to:runtimeFlags:"
- "compare:"
- "containsString:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "copyItemAtURL:toURL:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createSubsystemDirectoryStructure:outputDir:subDirectoryList:"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "defaultManager"
- "domain"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "fileExistsAtPath:"
- "fileURLWithPath:isDirectory:"
- "getResourceValue:forKey:error:"
- "init"
- "initWithPathURL:date:fileSize:"
- "isCentauriPlatform"
- "isFatalCollection:"
- "itemWithPathURL:date:fileSize:"
- "lastPathComponent"
- "length"
- "localizedDescription"
- "localizedFailureReason"
- "localizedStandardCompare:"
- "mainBundle"
- "name"
- "now"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "path"
- "rangeOfFirstMatchInString:options:range:"
- "regularExpressionWithPattern:options:error:"
- "removeObjectForKey:"
- "setObject:forKey:"
- "size"
- "sleepForTimeInterval:"
- "sortedArrayUsingComparator:"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "unsignedLongLongValue"
- "v16@0:8"
- "v32@0:8@16@24"
- "v40@0:8@16@24Q32"

```
