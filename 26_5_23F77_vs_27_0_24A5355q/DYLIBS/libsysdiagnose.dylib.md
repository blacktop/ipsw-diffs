## libsysdiagnose.dylib

> `/usr/lib/libsysdiagnose.dylib`

```diff

-1527.120.2.0.0
-  __TEXT.__text: 0x3134
-  __TEXT.__auth_stubs: 0x490
+1587.0.0.0.0
+  __TEXT.__text: 0x2ecc
   __TEXT.__objc_methlist: 0xe0
   __TEXT.__oslogstring: 0x1f8
   __TEXT.__cstring: 0x58e
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x60
   __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methname: 0x701
-  __TEXT.__objc_methtype: 0xd9
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
-  __AUTH_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0xe0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x540
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B2843EEB-970A-385F-8A79-92DD0DB6787E
+  UUID: 9B458E66-0279-301D-88FE-4CDA3F5E90B4
   Functions: 38
-  Symbols:   283
-  CStrings:  203
+  Symbols:   288
+  CStrings:  121
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_storeStrong
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
Functions:
~ _appendToCrashlogsDir : 188 -> 176
~ +[Libsysdiagnose setupConnection] : 204 -> 200
~ +[Libsysdiagnose createSysdiagnoseRequest:] : 852 -> 836
~ +[Libsysdiagnose addErrorString:withCode:forError:] : 256 -> 252
~ ___45+[Libsysdiagnose createMetrics:fromResponse:]_block_invoke : 172 -> 160
~ +[Libsysdiagnose verifyReply:withExpectedType:forError:] : 288 -> 284
~ _safeFetchStr : 68 -> 64
~ ___83+[Libsysdiagnose sendSysdiagnoseRequest:withMetrics:withError:withProgressHandler:]_block_invoke : 692 -> 660
~ _safeFetchErrorStr : 196 -> 180
~ ___83+[Libsysdiagnose sendSysdiagnoseRequest:withMetrics:withError:withProgressHandler:]_block_invoke.93 : 668 -> 580
~ +[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressCallback:] : 620 -> 592
~ ___85+[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressCallback:]_block_invoke : 264 -> 240
~ +[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressHandler:] : 620 -> 592
~ ___84+[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressHandler:]_block_invoke : 496 -> 464
~ ___84+[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressHandler:]_block_invoke_2 : 116 -> 112
~ +[Libsysdiagnose sysdiagnoseWithMetadata:onCompletion:] : 204 -> 212
~ +[Libsysdiagnose cancelActiveSysdiagnoseWithError:] : 240 -> 236
~ +[Libsysdiagnose fetchDiagnosticIDFromDeviceSource:WithMaxCount:withError:] : 1292 -> 1232
~ ___75+[Libsysdiagnose fetchDiagnosticIDFromDeviceSource:WithMaxCount:withError:]_block_invoke : 188 -> 140
~ _extractDiagnosticID : 568 -> 512
~ +[Libsysdiagnose fetchRemoteDiagnosticIDsWithError:] : 504 -> 488
~ +[Libsysdiagnose getSysdiagnoseCrashLog] : 1016 -> 932
~ ___40+[Libsysdiagnose getSysdiagnoseCrashLog]_block_invoke : 188 -> 140
CStrings:
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8@16^@24"
- "@40@0:8@16^@24@?32"
- "@40@0:8@16^@24^@32"
- "@40@0:8Q16Q24^@32"
- "@48@0:8@16^@24^@32@?40"
- "B24@0:8^@16"
- "B40@0:8@16^{_xpc_type_s=}24^@32"
- "Libsysdiagnose"
- "UTF8String"
- "absoluteString"
- "addErrorString:withCode:forError:"
- "addObject:"
- "allKeys"
- "allObjects"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithObjects:"
- "boolValue"
- "bytes"
- "cancelActiveSysdiagnoseWithError:"
- "compare:"
- "containsString:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createMetrics:fromResponse:"
- "createSysdiagnoseRequest:"
- "dateWithTimeIntervalSinceNow:"
- "defaultManager"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "errorWithDomain:code:userInfo:"
- "fetchDiagnosticIDFromDeviceSource:WithMaxCount:withError:"
- "fetchRemoteDiagnosticIDsWithError:"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "firstMatchInString:options:range:"
- "getResourceValue:forKey:error:"
- "getSysdiagnoseCrashLog"
- "hasSuffix:"
- "i40@0:8@16@24^@32"
- "indexSetWithIndexesInRange:"
- "intValue"
- "isSysdiagnoseInProgressWithError:"
- "lastPathComponent"
- "length"
- "localizedCaseInsensitiveCompare:"
- "localizedDescription"
- "numberWithDouble:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectsAtIndexes:"
- "pathSubmission"
- "range"
- "regularExpressionWithPattern:options:error:"
- "reverseObjectEnumerator"
- "sendSysdiagnoseRequest:withMetrics:withError:withProgressHandler:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setupConnection"
- "sharedInstance"
- "sortedArrayUsingSelector:"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringWithRange:"
- "sysdiagnoseWithMetadata:onCompletion:"
- "sysdiagnoseWithMetadata:withError:"
- "sysdiagnoseWithMetadata:withError:andProgressHandler:"
- "sysdiagnoseWithMetadata:withError:withProgressHandler:"
- "sysdiagnoseWithMetadata:withMetrics:withError:"
- "sysdiagnoseWithMetadata:withMetrics:withError:withProgressCallback:"
- "sysdiagnoseWithMetadata:withMetrics:withError:withProgressHandler:"
- "v32@0:8@16@?24"
- "v32@0:8^@16@24"
- "verifyReply:withExpectedType:forError:"

```
