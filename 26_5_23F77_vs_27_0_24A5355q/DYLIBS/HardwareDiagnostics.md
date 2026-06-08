## HardwareDiagnostics

> `/System/Library/PrivateFrameworks/HardwareDiagnostics.framework/HardwareDiagnostics`

```diff

 33.0.0.0.0
-  __TEXT.__text: 0x7634
-  __TEXT.__auth_stubs: 0x340
+  __TEXT.__text: 0x7058
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xa44
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x1e4
-  __TEXT.__cstring: 0x8c6
+  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__cstring: 0x8d1
   __TEXT.__oslogstring: 0x1bf
-  __TEXT.__unwind_info: 0x2f8
-  __TEXT.__objc_classname: 0x145
-  __TEXT.__objc_methname: 0xfa7
-  __TEXT.__objc_methtype: 0x2e3
-  __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0x108
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x560
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xa20
   __AUTH_CONST.__objc_const: 0x19d8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x240

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E971796F-CB3F-3C38-8B4A-71036C86163E
-  Functions: 187
+  UUID: E7C3D53C-2640-3BE3-8E83-D11F9819E491
+  Functions: 185
   Symbols:   843
-  CStrings:  485
+  CStrings:  184
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HDAnalysis>\""
- "@\"<HDAnalysis>\"16@0:8"
- "@\"<HDExperiment>\""
- "@\"<HDExperiment>\"16@0:8"
- "@\"HDBound\""
- "@\"HDDescription\"16@0:8"
- "@\"HDLimit\""
- "@\"HDReport\"40@0:8@\"NSDictionary\"16@\"<HDDiagnosticHost>\"24^@32"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMeasurement\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "AlphaNumerics"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"<NSObject>\"16^@24"
- "B32@0:8@16^@24"
- "DictionaryRepresentation"
- "HDAnalysisResult"
- "HDBound"
- "HDDescription"
- "HDDiagnostic"
- "HDDimensionlessUnit"
- "HDExperimentResult"
- "HDKeyedObjectParameter"
- "HDLab"
- "HDLimit"
- "HDMeasuredResult"
- "HDNumberParameter"
- "HDParameterDescription"
- "HDReport"
- "HDSimpleDiagnostic"
- "HDStringParameter"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<HDAnalysis>\",&,N,V_analysis"
- "T@\"<HDExperiment>\",&,N,V_experiment"
- "T@\"HDBound\",C,N,V_lowerBound"
- "T@\"HDBound\",C,N,V_upperBound"
- "T@\"HDDimensionlessUnit\",R,N"
- "T@\"HDLab\",R,N"
- "T@\"HDLimit\",C,N,V_limit"
- "T@\"NSArray\",R,N"
- "T@\"NSDate\",C,N,V_endTime"
- "T@\"NSDate\",C,N,V_startTime"
- "T@\"NSDictionary\",C,N,V_auxiliaryData"
- "T@\"NSDictionary\",C,N,V_metadata"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_keys"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSMeasurement\",C,N,V_value"
- "T@\"NSMeasurement\",R,C,N,V_measurement"
- "T@\"NSMutableArray\",R,N,V_measuredResults"
- "T@\"NSMutableDictionary\",R,N,V_auxiliaryData"
- "T@\"NSMutableDictionary\",R,N,V_files"
- "T@\"NSMutableDictionary\",R,N,V_measurements"
- "T@\"NSString\",&,N,V_summary"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_summary"
- "T@\"NSString\",R,C"
- "TB,N,V_open"
- "TB,N,V_required"
- "TB,R"
- "TB,R,N,V_valueWithinLimits"
- "TQ,R"
- "Tq,R,N,V_status"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_analyses"
- "_analysis"
- "_auxiliaryData"
- "_diagnostics"
- "_endTime"
- "_error"
- "_experiment"
- "_experiments"
- "_files"
- "_keys"
- "_limit"
- "_lowerBound"
- "_measuredResults"
- "_measurement"
- "_measurements"
- "_metadata"
- "_name"
- "_open"
- "_parameters"
- "_required"
- "_results"
- "_startTime"
- "_status"
- "_summary"
- "_upperBound"
- "_value"
- "_valueWithinLimits"
- "absoluteString"
- "addAnalysisWithName:block:"
- "addDiagnosticWithName:block:"
- "addDiagnosticWithName:experimentName:analysisName:block:"
- "addDiagnosticWithName:summary:experimentName:analysisName:"
- "addEntriesFromDictionary:"
- "addExperimentWithName:block:"
- "addFile:forName:"
- "addKey:forName:"
- "addKeys:"
- "addObject:"
- "addObjectsFromArray:"
- "addParameter:forName:"
- "addResult:"
- "allKeys"
- "allocWithZone:"
- "alphanumericCharacterSet"
- "analysisDescription"
- "analysisWithName:"
- "analyzeExperimentResult:error:"
- "attemptToSetPassed"
- "autorelease"
- "auxiliaryData"
- "availableAnalyses"
- "availableDiagnostics"
- "availableExperiments"
- "bundleForClass:"
- "bundleWithPath:"
- "canBeConvertedToUnit:"
- "class"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "counts"
- "date"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultLab"
- "description"
- "descriptionWithSummary:"
- "diagnosticDescription"
- "diagnosticWithName:"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endTime"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "errors"
- "events"
- "experimentDescription"
- "experimentWithName:"
- "failedForError:"
- "frames"
- "hash"
- "init"
- "initWithArray:copyItems:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithExperiment:analysis:"
- "initWithFormat:arguments:"
- "initWithName:"
- "initWithName:measurement:"
- "initWithSummary:"
- "initWithSummary:required:"
- "initWithSymbol:"
- "initWithValue:open:"
- "invertedSet"
- "isAlphaNumeric"
- "isEqual:"
- "isEqualToAnalysisResult:"
- "isEqualToArray:"
- "isEqualToBound:"
- "isEqualToDictionary:"
- "isEqualToExperimentResult:"
- "isEqualToLimit:"
- "isEqualToMeasuredResult:"
- "isEqualToSet:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "keys"
- "load"
- "localizedDescription"
- "lowerBound"
- "measuredResults"
- "measurementByConvertingToUnit:"
- "measurementWithinBounds:"
- "metadata"
- "numberWithDouble:"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "parameters"
- "path"
- "pathsForResourcesOfType:inDirectory:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "raise:format:"
- "rangeOfCharacterFromSet:"
- "release"
- "required"
- "resourcePath"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "run:"
- "runWithParameters:host:error:"
- "self"
- "setAnalysis:"
- "setAuxiliaryData:"
- "setDateStyle:"
- "setEndTime:"
- "setExperiment:"
- "setLimit:"
- "setLowerBound:"
- "setMetadata:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOpen:"
- "setRequired:"
- "setStartTime:"
- "setSummary:"
- "setTimeStyle:"
- "setUpperBound:"
- "setValue:"
- "setWithArray:"
- "setWithObjects:"
- "setupWithParameters:host:error:"
- "startTime"
- "stringFromDate:"
- "stringWithFormat:"
- "summary"
- "superclass"
- "supportsSecureCoding"
- "symbol"
- "teardown:"
- "unit"
- "upperBound"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "validateAgainstValues:error:"
- "validateValue:error:"
- "valueWithinLimits"
- "zone"

```
