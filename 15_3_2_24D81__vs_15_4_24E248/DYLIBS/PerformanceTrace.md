## PerformanceTrace

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/Versions/A/PerformanceTrace`

```diff

-200.2.0.0.0
-  __TEXT.__text: 0x40b0
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_methlist: 0x48c
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__cstring: 0x5fd
-  __TEXT.__oslogstring: 0x1ad
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methname: 0x105e
-  __TEXT.__objc_methtype: 0x309
-  __TEXT.__objc_stubs: 0xe00
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x40
+218.2.0.0.0
+  __TEXT.__text: 0x5230
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_methlist: 0x6b8
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__cstring: 0x883
+  __TEXT.__oslogstring: 0x24c
+  __TEXT.__unwind_info: 0x158
+  __TEXT.__objc_classname: 0xa8
+  __TEXT.__objc_methname: 0x13b2
+  __TEXT.__objc_methtype: 0x348
+  __TEXT.__objc_stubs: 0x11a0
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x5b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc8
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0xd78
+  __AUTH_CONST.__auth_got: 0x110
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0xa60
+  __AUTH_CONST.__objc_const: 0xa88
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x7c
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 236C1C95-B5E1-3FD2-AA3D-3FD9D0697FAB
-  Functions: 117
-  Symbols:   382
-  CStrings:  403
+  UUID: 882CEB01-1425-3820-8FDD-8BED7D4B3A28
+  Functions: 132
+  Symbols:   453
+  CStrings:  505
 
Symbols:
+ -[PTTraceConfig setTraceRecordArgs:]
+ -[PTTraceConfig setTraceRecordEndNotificationName:]
+ -[PTTraceConfig traceRecordArgs]
+ -[PTTraceConfig traceRecordEndNotificationName]
+ -[PTTraceSession displayTraceCompletedAlertWithTraceFileURL:additionalInfo:notificationTimeoutSecs:completionHandler:]
+ -[PTTraceSession displayTraceCompletedAlertWithTraceFileURL:additionalInfo:notificationTimeoutSecs:completionHandler:].cold.1
+ -[PTTraceSession displayTraceCompletedAlertWithTraceFileURL:additionalInfo:notificationTimeoutSecs:completionHandler:].cold.2
+ GCC_except_table17
+ GCC_except_table5
+ OBJC_IVAR_$_PTTraceConfig._traceRecordArgs
+ OBJC_IVAR_$_PTTraceConfig._traceRecordEndNotificationName
+ OBJC_IVAR_$_PTTraceSession._queue
+ _CFUserNotificationDisplayAlert
+ _NSLog
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _PTTraceSessionInfoKey_EndingFGSceneIdentifiers
+ _PTTraceSessionInfoKey_StartingFGSceneIdentifiers
+ __118-[PTTraceSession displayTraceCompletedAlertWithTraceFileURL:additionalInfo:notificationTimeoutSecs:completionHandler:]_block_invoke.cold.1
+ __32-[PTTraceConfig _initConnection]_block_invoke.177
+ __32-[PTTraceConfig _initConnection]_block_invoke.177.cold.1
+ __33-[PTTraceSession _initConnection]_block_invoke.29
+ __33-[PTTraceSession _initConnection]_block_invoke.29.cold.1
+ ___118-[PTTraceSession displayTraceCompletedAlertWithTraceFileURL:additionalInfo:notificationTimeoutSecs:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48b56r
+ ___copy_helper_block_e8_32w
+ ___destroy_helper_block_e8_32s40s48s56r
+ ___destroy_helper_block_e8_32w
+ __block_literal_global.179
+ __block_literal_global.181
+ __block_literal_global.87
+ _descriptionStringForScenes
+ _dispatch_async
+ _dispatch_queue_create
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$URL
+ _objc_msgSend$URLHostAllowedCharacterSet
+ _objc_msgSend$absoluteString
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$description
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$firstObject
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$openURL:configuration:error:
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$setTraceRecordArgs:
+ _objc_msgSend$stringByAddingPercentEncodingWithAllowedCharacters:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$traceRecordArgs
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _urlEncodedString
- __32-[PTTraceConfig _initConnection]_block_invoke.165
- __32-[PTTraceConfig _initConnection]_block_invoke.165.cold.1
- __33-[PTTraceSession _initConnection]_block_invoke.22
- __33-[PTTraceSession _initConnection]_block_invoke.22.cold.1
- __block_literal_global.167
- __block_literal_global.169
- __block_literal_global.24
- __block_literal_global.78
CStrings:
+ "\n"
+ " None"
+ "%@"
+ "%@ is not an array of strings."
+ "%@ is not an array type."
+ "@\"NSArray\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "A#E"
+ "Attachments"
+ "Attachments\n"
+ "Classification"
+ "Connection with PTService interrupted."
+ "Could not find trace file '%@'."
+ "Description"
+ "EndingFGSceneIdentifiers"
+ "Failed to create query item for key: %@, value: %@"
+ "Failed to open Tap-to-Radar: %@"
+ "Foreground scenes at end of trace:%@\n\n"
+ "Foreground scenes at start of trace:%@\n\n"
+ "More than one foreground scene passed in. Not setting Radar component."
+ "No, thanks"
+ "Not Applicable"
+ "Opening Tap-to-Radar with URL: %@"
+ "Performance"
+ "Radar"
+ "Reproducibility"
+ "StartingFGSceneIdentifiers"
+ "Summary:\n\n\nSteps to reproduce\n1.\n2.\n3.\n\n"
+ "T@\"NSArray\",&,N,V_traceRecordArgs"
+ "T@\"NSString\",&,N,V_traceRecordEndNotificationName"
+ "Trace Complete"
+ "Trace file: '%@'.\n"
+ "URL"
+ "URLHostAllowedCharacterSet"
+ "Your trace is complete at '%@'. Would you like to file a radar?"
+ "_queue"
+ "_traceRecordArgs"
+ "_traceRecordEndNotificationName"
+ "absoluteString"
+ "appendFormat:"
+ "appendString:"
+ "bundleID"
+ "com.apple.performancetrace.client"
+ "componentsJoinedByString:"
+ "defaultManager"
+ "defaultWorkspace"
+ "dictionaryWithObjectsAndKeys:"
+ "displayTraceCompletedAlertWithTraceFileURL:additionalInfo:notificationTimeoutSecs:completionHandler:"
+ "doubleValue"
+ "fileExistsAtPath:isDirectory:"
+ "firstObject"
+ "isEqualToArray:"
+ "lastPathComponent"
+ "new"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "openURL:configuration:error:"
+ "queryItemWithName:value:"
+ "setHost:"
+ "setObject:forKey:"
+ "setQueryItems:"
+ "setScheme:"
+ "setTraceRecordArgs:"
+ "setTraceRecordEndNotificationName:"
+ "stringByAddingPercentEncodingWithAllowedCharacters:"
+ "stringByAppendingString:"
+ "stringWithFormat:"
+ "stringWithString:"
+ "tap-to-radar"
+ "traceRecordArgs"
+ "traceRecordArgs: %@"
+ "traceRecordEndNotificationName"
+ "v48@0:8@16@24@32@?40"
- "A#C"

```
