## CrashReporterSupport

> `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport`

```diff

-14278.0.0.0.0
-  __TEXT.__text: 0x6080
-  __TEXT.__auth_stubs: 0x7e0
+14280.0.0.0.0
+  __TEXT.__text: 0x60ac
   __TEXT.__objc_methlist: 0x230
   __TEXT.__const: 0x108
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0xe49
+  __TEXT.__cstring: 0xe65
   __TEXT.__oslogstring: 0x8d3
-  __TEXT.__unwind_info: 0x258
-  __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0xc53
-  __TEXT.__objc_methtype: 0x1fe
-  __TEXT.__objc_stubs: 0xd80
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x408
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x430
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_selrefs: 0x488
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x400
+  __DATA_CONST.__objc_arraydata: 0x58
+  __DATA_CONST.__got: 0x178
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x1460
+  __AUTH_CONST.__cfstring: 0x14c0
   __AUTH_CONST.__objc_const: 0x2d0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xc9
   __DATA.__bss: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81B78669-C1FB-3C00-BC31-B2BBB6070501
+  UUID: E9AF37D4-E9B4-3690-86D0-25ADE23A7781
   Functions: 137
-  Symbols:   670
-  CStrings:  594
+  Symbols:   675
+  CStrings:  415
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OSAGetSubmittableLogsWithMetadata
+ ___OSAGetSubmittableLogsWithMetadata_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e15_v16?0"NSURL"8ls32l8s40l8s48l8
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$bugType
+ _objc_msgSend$initWithPath:forRouting:usingConfig:options:error:
+ _objc_msgSend$isOnDeviceLogType:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "<exempt>"
+ "none"
+ "onDeviceLog"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<OTATaskingAgent>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@28@0:8i16@20"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B40@0:8@16@24@32"
- "B48@0:8@16@24@32^v40"
- "I24@0:8@16"
- "NSObject"
- "OTATaskingAgent"
- "OTATaskingAgentClient"
- "Q16@0:8"
- "StructuredDataReport"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByDeletingPathExtension"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_connection"
- "_log_type"
- "_raw_logfile"
- "_synchRemoteObjectProxy"
- "addObject:"
- "appleCareDetails"
- "array"
- "arrayWithObjects:count:"
- "attributesOfItemAtPath:error:"
- "autorelease"
- "awdKey"
- "awdKeyWithReply:"
- "boolValue"
- "bytes"
- "checkResourceIsReachableAndReturnError:"
- "class"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "crashReporterKey"
- "crashreporterKey"
- "crashreporterKeyWithReply:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createFileAtPath:contents:attributes:"
- "createForSubmission:metadata:options:error:writing:"
- "createSymbolicLinkAtURL:withDestinationURL:error:"
- "dataUsingEncoding:allowLossyConversion:"
- "dataWithContentsOfFile:"
- "dataWithJSONObject:options:error:"
- "dataWithLength:"
- "date"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "debugDescription"
- "defaultManager"
- "deletePreference:forUser:inDomain:"
- "deletePreferenceForDomain:preference:UID:withReply:"
- "dictionary"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithObjects:forKeys:count:"
- "effectiveBoolValueForSetting:"
- "fileExistsAtPath:isDirectory:"
- "fileSystemRepresentation"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "fileURLWithPathComponents:"
- "generateCustomLogAtLevel:withBlock:"
- "generateLogAtLevel:withBlock:"
- "getPrefsKey:forDomain:withOptions:"
- "hash"
- "i28@0:8B16@?20"
- "incidentID"
- "init"
- "initWithArray:"
- "initWithFileDescriptor:"
- "initWithFormat:"
- "initWithMachServiceName:options:"
- "initWithObjects:"
- "initWithType:withFile:"
- "initWithUTF8String:"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "isActionable"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "iterateLogsWithOptions:usingBlock:"
- "lastPathComponent"
- "length"
- "modelCode"
- "moveItemAtPath:toPath:error:"
- "multiUserMode"
- "mutableBytes"
- "mutableCopy"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "pathExtension"
- "pathPreferences"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "problemType"
- "processIdentifier"
- "processInfo"
- "processName"
- "productName"
- "productNameVersionBuildString"
- "propertyListWithData:options:format:error:"
- "rangeOfString:options:"
- "release"
- "removeItemAtPath:error:"
- "removeLastObject"
- "removeObjectForKey:"
- "reportNamePrefix"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "saveWithOptions:"
- "self"
- "setLength:"
- "setMaximumSignificantDigits:"
- "setObject:forKeyedSubscript:"
- "setPreference:forUser:inDomain:toValue:"
- "setPreferenceForDomain:preference:value:UID:withReply:"
- "setRemoteObjectInterface:"
- "setResourceValue:forKey:error:"
- "setUsesSignificantDigits:"
- "sharedClient"
- "sharedConnection"
- "sharedInstance"
- "stream"
- "streamContentAtLevel:withBlock:"
- "stringByAppendingPathComponent:"
- "stringByDeletingLastPathComponent"
- "stringForObjectValue:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "submitWithOptions:resultsCallback:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSinceDate:"
- "uidForUser:"
- "v16@0:8"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v28@0:8B16@?20"
- "v44@0:8@\"NSString\"16@\"NSString\"24I32@?<v@?B>36"
- "v44@0:8@16@24I32@?36"
- "v52@0:8@\"NSString\"16@\"NSString\"24@32I40@?<v@?B>44"
- "v52@0:8@16@24@32I40@?44"
- "valueForKey:"
- "writeToURL:atomically:"
- "zone"

```
