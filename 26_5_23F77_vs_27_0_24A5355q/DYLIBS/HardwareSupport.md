## HardwareSupport

> `/System/Library/PrivateFrameworks/HardwareSupport.framework/HardwareSupport`

```diff

-35.0.0.0.0
-  __TEXT.__text: 0x7350
-  __TEXT.__auth_stubs: 0x6a0
+36.0.0.0.0
+  __TEXT.__text: 0x6be4
   __TEXT.__objc_methlist: 0xa3c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x876
+  __TEXT.__cstring: 0x921
   __TEXT.__oslogstring: 0x2e4
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x288
-  __TEXT.__objc_classname: 0x1e4
-  __TEXT.__objc_methname: 0x1088
-  __TEXT.__objc_methtype: 0x60b
-  __TEXT.__objc_stubs: 0xc80
-  __DATA_CONST.__got: 0x118
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_selrefs: 0x508
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0x118
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__cfstring: 0x780
   __AUTH_CONST.__objc_const: 0x1570
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x2a0

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E1AF0565-1C22-3D79-874A-5E7BD895E745
-  Functions: 201
-  Symbols:   828
-  CStrings:  459
+  UUID: D6CD72AF-A1CC-3EE6-B5BA-1B0A5D61B48B
+  Functions: 196
+  Symbols:   826
+  CStrings:  154
 
Symbols:
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ ___block_literal_global.167
+ ___block_literal_global.176
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
+ _tryLoadPluginForClass
+ _tryLoadPluginForClass.cold.1
+ _tryLoadPluginForClass.cold.2
+ _tryLoadPluginForClass.cold.3
+ _tryLoadPluginForClass.cold.4
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- ___block_literal_global.168
- ___block_literal_global.177
- _buildFactoryFunctionSignature
- _buildFactoryFunctionSignature.cold.1
- _buildFactoryFunctionSignature.cold.2
- _buildFactoryFunctionSignature.cold.3
- _buildFactoryFunctionSignature.cold.4
CStrings:
+ "Apple%@CamIn"
+ "AppleCamera"
- "#16@0:8"
- ".cxx_destruct"
- "@\"HSFigCaptureDevice\""
- "@\"HSIORChannelDescription\""
- "@\"HSIORChannelDescription\"16@0:8"
- "@\"NSArray\""
- "@\"NSData\"32@0:8q16^@24"
- "@\"NSDictionary\""
- "@\"NSNumber\""
- "@\"NSNumber\"16@0:8"
- "@\"NSSet<HSIOHIDDeviceInterface>\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"Protocol\""
- "@16@0:8"
- "@20@0:8I16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^@16"
- "@24@0:8^{OpaqueCMBaseObject=}16"
- "@24@0:8^{OpaqueFigCaptureDevice=}16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{__CFDictionary=}16"
- "@24@0:8^{__CFString=}16"
- "@24@0:8^{__IOHIDDevice=}16"
- "@24@0:8^{__IOHIDManager=}16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@32@0:8^{OpaqueFigCaptureStream=}16@24"
- "@32@0:8^{OpaqueFigCaptureSynchronizedStreamsGroup=}16@24"
- "@32@0:8^{__CFString=}16^@24"
- "@32@0:8q16^@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "B32@0:8@16^{__CFString=}24"
- "B40@0:8@16^{__CFString=}24^@32"
- "B40@0:8q16@\"NSData\"24^@32"
- "B40@0:8q16@24^@32"
- "B44@0:8q16i24@28^@36"
- "HSCMBaseObject"
- "HSCMBaseObjectInterface"
- "HSFigCaptureDevice"
- "HSFigCaptureStream"
- "HSFigCaptureSyncStreamsGroup"
- "HSHIDDevice"
- "HSHIDManager"
- "HSIOHIDDeviceInterface"
- "HSIOHIDManagerInterface"
- "HSIORChannelDescription"
- "HSIORSample"
- "HSIOReport"
- "HSIOReportSnapshot"
- "HSIOReporting"
- "HSIOSimpleReporting"
- "HSISPCapturePlugIn"
- "NSCopying"
- "NSObject"
- "Q16@0:8"
- "SimpleFormat"
- "Snapshot"
- "T#,R"
- "T@\"<HSIOReporting>\",R,N"
- "T@\"HSFigCaptureDevice\",R,N,V_device"
- "T@\"HSIORChannelDescription\",&,N,V_channelDescription"
- "T@\"NSArray\",&,N,V_channelDescriptions"
- "T@\"NSArray\",&,N,V_samples"
- "T@\"NSDictionary\",&,N,V_reportDictionary"
- "T@\"NSNumber\",&,N,V_count"
- "T@\"NSNumber\",&,N,V_driverIdentifier"
- "T@\"NSNumber\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_driverName"
- "T@\"NSString\",&,N,V_groupName"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_subGroupName"
- "T@\"NSString\",&,N,V_summary"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"Protocol\",&,N,V_reportingProtocol"
- "T@?,C,N,V_deviceEnumeratedCallback"
- "T@?,C,N,V_deviceRemovedCallback"
- "T@?,C,N,V_inputReportCallback"
- "TQ,R"
- "T^{OpaqueCMBaseObject=},R,N,V_underlyingObject"
- "T^{OpaqueFigCaptureDevice=},R,N,V_underlyingDevice"
- "T^{OpaqueFigCaptureStream=},R,N,V_underlyingStream"
- "T^{OpaqueFigCaptureSynchronizedStreamsGroup=},R,N,V_underlyingSyncStreamsGroup"
- "T^{__IOHIDDevice=},N,V_deviceRef"
- "UTF8String"
- "Vv16@0:8"
- "[16384C]"
- "^?"
- "^{OpaqueCMBaseObject=}"
- "^{OpaqueCMBaseObject=}16@0:8"
- "^{OpaqueFigCaptureDevice=}"
- "^{OpaqueFigCaptureDevice=}16@0:8"
- "^{OpaqueFigCaptureStream=}"
- "^{OpaqueFigCaptureStream=}16@0:8"
- "^{OpaqueFigCaptureSynchronizedStreamsGroup=}"
- "^{OpaqueFigCaptureSynchronizedStreamsGroup=}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__IOHIDDevice=}"
- "^{__IOHIDDevice=}16@0:8"
- "^{__IOHIDManager=}"
- "_active"
- "_cancelled"
- "_channelDescription"
- "_channelDescriptions"
- "_count"
- "_createFunction"
- "_device"
- "_deviceEnumeratedCallback"
- "_deviceRef"
- "_deviceRemovedCallback"
- "_driverIdentifier"
- "_driverName"
- "_groupName"
- "_identifier"
- "_inputReportCallback"
- "_managerRef"
- "_name"
- "_reportCallbackBuffer"
- "_reportDictionary"
- "_reportingProtocol"
- "_samples"
- "_setReportWithID:type:data:error:"
- "_subGroupName"
- "_summary"
- "_underlyingDevice"
- "_underlyingObject"
- "_underlyingStream"
- "_underlyingSyncStreamsGroup"
- "addObject:"
- "allObjects"
- "allocWithZone:"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "autorelease"
- "bytes"
- "cStringUsingEncoding:"
- "channel"
- "channelDescription"
- "channelDescriptions"
- "class"
- "close:"
- "compare:"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "defaultManager"
- "defaultPlugIn"
- "description"
- "device"
- "device:"
- "deviceEnumeratedCallback"
- "deviceRef"
- "deviceRemovedCallback"
- "devices"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "driverIdentifier"
- "driverName"
- "enumerateDevicesMatching:"
- "errorWithDomain:code:userInfo:"
- "featureReportWithID:error:"
- "fileExistsAtPath:"
- "firstMatchInString:options:range:"
- "firstObject"
- "groupName"
- "hash"
- "identifier"
- "init"
- "initWithBaseObject:"
- "initWithCaptureDevice:"
- "initWithCaptureStream:fromDevice:"
- "initWithCaptureSyncStreamsGroup:fromDevice:"
- "initWithData:encoding:"
- "initWithDeviceRef:"
- "initWithIOReportChannelRef:"
- "initWithIOReportSampleRef:"
- "initWithManagerRef:"
- "initWithReportDictionary:"
- "initWithService:"
- "inputReportCallback"
- "integerValue"
- "invalidate:"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToChannelDescription:"
- "isEqualToDevice:"
- "isEqualToReport:"
- "isEqualToSample:"
- "isEqualToSnapshot:"
- "isEqualToStream:"
- "isEqualToStreamsGroup:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "mutableCopy"
- "name"
- "new"
- "null"
- "numberOfRanges"
- "numberWithInt:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "open:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "raise:format:"
- "rangeAtIndex:"
- "regularExpressionWithPattern:options:error:"
- "release"
- "relinquishControlOfStreams:error:"
- "report:"
- "reportByFilteringChannels:"
- "reportDictionary"
- "reportWithOnlySimpleChannels"
- "reportWithOnlySimpleChannels:"
- "reportingProtocol"
- "requestControlOfStreams:error:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "samples"
- "scheduleWithRunLoop:mode:"
- "self"
- "setChannelDescription:"
- "setChannelDescriptions:"
- "setCount:"
- "setDeviceEnumeratedCallback:"
- "setDeviceRef:"
- "setDeviceRemovedCallback:"
- "setDriverIdentifier:"
- "setDriverName:"
- "setFeatureReportWithID:data:error:"
- "setGroupName:"
- "setIdentifier:"
- "setInputReportCallback:"
- "setName:"
- "setObject:forKey:"
- "setOutputReportWithID:data:error:"
- "setReportDictionary:"
- "setReportingProtocol:"
- "setSamples:"
- "setSubGroupName:"
- "setSummary:"
- "setValue:forProperty:"
- "setValue:forProperty:error:"
- "setWithCapacity:"
- "setWithSet:"
- "snapshot:"
- "snapshotByFilteringSamples:"
- "snapshotReport:error:"
- "snapshotWithBaseline:error:"
- "sortedArrayUsingComparator:"
- "start:"
- "statusDescription:"
- "stop:"
- "streams:"
- "stringByTrimmingCharactersInSet:"
- "stringWithFormat:"
- "subGroupName"
- "substringWithRange:"
- "summary"
- "superclass"
- "synchronizedStreamsGroups:"
- "underlyingDevice"
- "underlyingObject"
- "underlyingStream"
- "underlyingSyncStreamsGroup"
- "unscheduleFromRunLoop:mode:"
- "v16@0:8"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<HSIOHIDDeviceInterface>\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?q@\"NSData\"@\"NSError\">16"
- "v24@0:8^{__IOHIDDevice=}16"
- "v32@0:8^{__CFRunLoop=}16^{__CFString=}24"
- "valueForKey:"
- "valueForKeyPath:"
- "valueForProperty:"
- "valueForProperty:error:"
- "whitespaceAndNewlineCharacterSet"
- "zone"

```
