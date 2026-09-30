## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`

```diff

-151.3.0.0.0
-  __TEXT.__text: 0x46278
+151.5.0.0.0
+  __TEXT.__text: 0x4a518
   __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x5f8c
-  __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x16b20
-  __TEXT.__oslogstring: 0xda5
-  __TEXT.__gcc_except_tab: 0x2a4
+  __TEXT.__objc_methlist: 0x6304
+  __TEXT.__const: 0x228
+  __TEXT.__cstring: 0x16d8c
+  __TEXT.__oslogstring: 0xed6
+  __TEXT.__gcc_except_tab: 0x2b0
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x11e8
-  __TEXT.__objc_classname: 0xcfc
-  __TEXT.__objc_methname: 0xe44e
-  __TEXT.__objc_methtype: 0x106a
-  __TEXT.__objc_stubs: 0x8660
-  __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0x928
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __TEXT.__unwind_info: 0x12d8
+  __TEXT.__objc_classname: 0xd5b
+  __TEXT.__objc_methname: 0xee8b
+  __TEXT.__objc_methtype: 0x1172
+  __TEXT.__objc_stubs: 0x8d20
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0xa48
+  __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2818
-  __DATA_CONST.__objc_superrefs: 0x278
+  __DATA_CONST.__objc_selrefs: 0x2a00
+  __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x4ea8
   __AUTH_CONST.__auth_got: 0x2d8
-  __AUTH_CONST.__const: 0x900
-  __AUTH_CONST.__cfstring: 0x17ce0
-  __AUTH_CONST.__objc_const: 0xd2c0
+  __AUTH_CONST.__const: 0x980
+  __AUTH_CONST.__cfstring: 0x17f80
+  __AUTH_CONST.__objc_const: 0xd918
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x28
-  __DATA.__objc_ivar: 0x8a8
-  __DATA.__data: 0xae8
-  __DATA.__bss: 0x350
+  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH.__objc_data: 0xc8
+  __DATA.__objc_ivar: 0x900
+  __DATA.__data: 0xb48
+  __DATA.__bss: 0x370
   __DATA_DIRTY.__objc_data: 0x1c98
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2219
-  Symbols:   2737
-  CStrings:  5757
+  Functions: 2311
+  Symbols:   2835
+  CStrings:  5907
 
Symbols:
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_SignpostGPURenderInterval
+ _OBJC_CLASS_$_SignpostUpdateSequenceInterval
+ _OBJC_METACLASS_$_SignpostGPURenderInterval
+ _OBJC_METACLASS_$_SignpostUpdateSequenceInterval
+ _SSCAIsUCMetadataSubsystemCategory
+ _SignpostScalarTypeFromNumber
+ _SignpostScalarTypeIsIntegral
+ _SignpostScalarTypeIsSigned
+ _SignpostScalarTypeSizeOf
CStrings:
+ "\x0f\b"
+ "\x15!"
+ "\x1f\x04"
+ "(?:^|\\s)([a-zA-Z0-9_]+)[:=]?$"
+ "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]"
+ "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:]"
+ "@\"SignpostGPURenderInterval\""
+ "@28@0:8@16I24"
+ "@32@0:8@16^{?=iiii}24"
+ "@56@0:8@16@24@32@40@48"
+ "@56@0:8@16Q24Q32d40Q48"
+ "@64@0:8@16I24@28Q36I44S48C52C56C60"
+ "@72@0:8@16Q24@32@40@48@56@64"
+ "@92@0:8@16I24I28I32B36C40Q44Q52Q60@68@76@84"
+ "ArgumentScalarType"
+ "B24@?0@\"SignpostUpdateSequenceInterval\"8@\"NSDictionary\"16"
+ "B32@?0@\"SignpostCommitInterval\"8Q16^B24"
+ "B32@?0@\"SignpostUpdateSequenceInterval\"8Q16^B24"
+ "D"
+ "Deprecated"
+ "FrameGPUExecute"
+ "FrameGPUExecution"
+ "FrameLifetime has %ld commits unrelated to UpdateSequence"
+ "FrameLifetime with server side updates only has %u updates."
+ "FrameLifetimeInterval"
+ "FrameModifierTarget"
+ "FramePrevious"
+ "FrameRender"
+ "FrameUpdate"
+ "FrameUpdate %llx is long with no contributors"
+ "FrameUpdate contributor length not a multiple of contributor size"
+ "Missing name for pid %@"
+ "Q32@0:8@16@24"
+ "Requested to handle a generated hid interval"
+ "Requested to handle a generated latency interval"
+ "S"
+ "ScalarType"
+ "SignpostGPURenderInterval"
+ "SignpostOverrunChecking"
+ "SignpostUpdateSequenceInterval"
+ "T@\"NSArray\",&,N,V_updateIntervals"
+ "T@\"NSDictionary\",&,N,V_processNameToPidsDict"
+ "T@\"NSMutableArray\",R,N,V_allUpateIntervals"
+ "T@\"NSMutableArray\",R,N,V_queueCommitIntervals"
+ "T@\"NSMutableArray\",R,N,V_queueUpdateIntervals"
+ "T@\"NSMutableDictionary\",R,N,V_pidToProcessNameDictionary"
+ "T@\"SignpostEvent\",R,N,V_beginEvent"
+ "T@\"SignpostEvent\",R,N,V_endEvent"
+ "T@\"SignpostFrameLatencyInterval\",&,N,V_frameLatencyInterval"
+ "T@\"SignpostFrameLifetimeInterval\",R,N,V_frameLifetime"
+ "T@\"SignpostFrameLifetimeInterval\",W,N,V_frameLifetime"
+ "T@\"SignpostGPURenderInterval\",R,N,V_gpuInterval"
+ "T@?,C,N,V_gpuBlock"
+ "T@?,C,N,V_updateIntervalBlock"
+ "TB,N,V_hasRelativeMcts"
+ "TB,N,V_isGenerated"
+ "TB,R,N,GisImplicit,V_implicit"
+ "TB,R,N,GisPotentiallyLong"
+ "TB,R,N,V_lifetimeIsLong"
+ "TQ,R,N,V_scalarType"
+ "TemporaryAnimationInterval"
+ "Ti,N,V_pid"
+ "UpdateCycle"
+ "UpdateSequence"
+ "Z\x11"
+ "_allUpateIntervals"
+ "_argumentObjectWithPrefix:"
+ "_argumentObjectWithPrefix:expectedClass:"
+ "_baseMCTForEvent:"
+ "_dataArgumentWithPrefix:"
+ "_frameLifetime"
+ "_gpuBlock"
+ "_gpuInterval"
+ "_handleCommitInterval:"
+ "_handleFrameLifetime:isLong:isConcise:pidToNameDict:"
+ "_handleFrameLifetimeBegin:isLong:"
+ "_handleUpdateInterval:"
+ "_handleUpdateSequenceInterval:"
+ "_hasRelativeMcts"
+ "_implicit"
+ "_isGenerated"
+ "_numberArgumentWithPrefix:"
+ "_pidToProcessNameDictionary"
+ "_queueCommitIntervals"
+ "_queueUpdateIntervals"
+ "_removeOrphansFromQueue:preceedingEvent:"
+ "_scalarType"
+ "_scalarTypeForArgumentObject:scalarTypeNumber:"
+ "_stringArgumentWithPrefix:"
+ "_updateIntervalBlock"
+ "_updateIntervals"
+ "_updatesMatchingFrameLifetime:"
+ "allUpateIntervals"
+ "args1"
+ "args2"
+ "bytes"
+ "c"
+ "collectPIDToProcessNameForEvent:"
+ "com.apple.AppKit"
+ "containsIndex:"
+ "contributors"
+ "d40@0:8@16@24Q32"
+ "firstIndex"
+ "firstMatchInString:options:range:"
+ "frameLifetime"
+ "gpuBlock"
+ "gpuInterval"
+ "hasRelativeMcts"
+ "hasRenderServerUpdateOnly"
+ "implicit"
+ "indexGreaterThanIndex:"
+ "indexesOfObjectsPassingTest:"
+ "initWithArgumentObject:scalarType:typeNamespace:type:tokens:stringPrefix:privacy:"
+ "initWithContextInfoEvent:contributor:"
+ "initWithFrameLifetime:startMCT:endMCT:timebaseRatio:class:"
+ "initWithFrameLifetimes:"
+ "initWithInterval:contextArray:hidLatencyInterval:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:"
+ "initWithInterval:contextArray:renderInterval:gpuInterval:frameSeedToSkippedRenderIntervals:"
+ "initWithInterval:frameSeed:"
+ "initWithInterval:frameSeed:renderSkipReason:refreshInterval:displayID:passCount:compileCount:cacheMissCount:fallbackDrawCount:"
+ "initWithInterval:swapID:frameSeed:displayID:skipRequested:bufferCount:refreshInterval:previousPresentationMCT:inProcessTargetMCT:contextArray:renderInterval:gpuInterval:"
+ "isGenerated"
+ "isGeneratedInterval"
+ "isImplicit"
+ "isPotentiallyLong"
+ "numberOfRanges"
+ "objCType"
+ "objectsAtIndexes:"
+ "overrunIntervalForOverrunQuery:frameLifetimes:"
+ "pidToProcessNameDictionary"
+ "potentiallyLong"
+ "q24@?0@\"SignpostUpdateSequenceInterval\"8@\"SignpostUpdateSequenceInterval\"16"
+ "queueCommitIntervals"
+ "queueUpdateIntervals"
+ "rangeAtIndex:"
+ "regularExpressionWithPattern:options:error:"
+ "removeObjectsInRange:"
+ "s"
+ "scalarType"
+ "setFrameLatencyInterval:"
+ "setFrameLifetime:"
+ "setGpuBlock:"
+ "setHasRelativeMcts:"
+ "setIsGenerated:"
+ "setPid:"
+ "setProcessNameToPidsDict:"
+ "setUpdateIntervalBlock:"
+ "setUpdateIntervals:"
+ "setValue:forKey:"
+ "sortDescriptorWithKey:ascending:"
+ "sortUsingDescriptors:"
+ "sortWithOptions:usingComparator:"
+ "stringWithCString:encoding:"
+ "substringWithRange:"
+ "timeRatioMSPerSForOverrunQuery:frameLifetimes:applyPerceptionAdjustments:"
+ "updateIntervalBlock"
+ "updateIntervals"
+ "updateIntervalsForPID:"
+ "v16@?0@\"SignpostUpdateSequenceInterval\"8"
+ "v24@?0@\"NSIndexSet\"8Q16"
+ "v28@0:8@16B24"
+ "v40@0:8@16B24B28@32"
+ "\xb1"
- "\x0f\a"
- "\x14!"
- "\x1f"
- "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:]"
- "-[SignpostFrameLifetimeInterval initWithInterval:contextArray:renderInterval:frameSeedToSkippedRenderIntervals:]"
- "@48@0:8Q16Q24d32Q40"
- "HIDLatency frame seed mismatch: %#x vs %#x"
- "T@\"NSDictionary\",R,N,V_processNameToPidsDict"
- "T@\"SignpostFrameLatencyInterval\",R,N,V_frameLatencyInterval"
- "TB,N,V_lifetimeIsLong"
- "X\x11"
- "_handleFrameLifetime:isLong:isConcise:"
- "_handleFrameLifetimeBegin:"
- "_handleLongFrameLifetimeBegin:"
- "addIndexes:"
- "initWithArgumentObject:typeNamespace:type:tokens:stringPrefix:privacy:"
- "initWithInterval:contextArray:hidLatencyInterval:renderInterval:frameLatencyInterval:frameSeedToSkippedRenderIntervals:"
- "initWithInterval:contextArray:renderInterval:frameSeedToSkippedRenderIntervals:"
- "initWithStartMCT:endMCT:timebaseRatio:class:"
- "setLifetimeIsLong:"

```
