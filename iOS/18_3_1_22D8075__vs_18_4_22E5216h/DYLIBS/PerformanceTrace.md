## PerformanceTrace

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace`

```diff

-200.2.0.0.0
-  __TEXT.__text: 0x3bb4
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_methlist: 0x48c
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__cstring: 0x62a
-  __TEXT.__oslogstring: 0x1ad
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methname: 0x105e
-  __TEXT.__objc_methtype: 0x309
-  __TEXT.__objc_stubs: 0xe00
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x90
+218.1.0.0.0
+  __TEXT.__text: 0x4ae0
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_methlist: 0x6b8
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__cstring: 0x8c6
+  __TEXT.__oslogstring: 0x24c
+  __TEXT.__unwind_info: 0x150
+  __TEXT.__objc_classname: 0xa8
+  __TEXT.__objc_methname: 0x13b2
+  __TEXT.__objc_methtype: 0x348
+  __TEXT.__objc_stubs: 0x11a0
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x5b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x138
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0xd78
+  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0xa80
+  __AUTH_CONST.__objc_const: 0xa88
   __AUTH_CONST.__objc_intobj: 0x90
-  __DATA.__objc_ivar: 0x7c
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 115
-  Symbols:   184
-  CStrings:  350
+  Functions: 126
+  Symbols:   223
+  CStrings:  424
 
Symbols:
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
+ _dispatch_async
+ _dispatch_queue_create
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x19
+ _objc_retain_x26
+ _objc_retain_x28
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "\x01\x13"
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
+ "com.apple.springboard"
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
- "\x13"
- "A#C"

```
