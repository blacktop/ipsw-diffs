## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-3.26.0.0.0
-  __TEXT.__text: 0x27918
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x212c
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x44c
-  __TEXT.__cstring: 0x28c3
-  __TEXT.__oslogstring: 0x34cd
+3.26.2.3.0
+  __TEXT.__text: 0x28b2c
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_methlist: 0x21b4
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x460
+  __TEXT.__cstring: 0x2a09
+  __TEXT.__oslogstring: 0x3570
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0xa4c
-  __TEXT.__objc_classname: 0x3d2
-  __TEXT.__objc_methname: 0x7e8a
-  __TEXT.__objc_methtype: 0x1119
-  __TEXT.__objc_stubs: 0x4ae0
+  __TEXT.__unwind_info: 0xa88
+  __TEXT.__objc_classname: 0x3e4
+  __TEXT.__objc_methname: 0x8034
+  __TEXT.__objc_methtype: 0x110a
+  __TEXT.__objc_stubs: 0x4ca0
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0xc38
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__const: 0xd00
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2ac8
-  __DATA_CONST.__objc_selrefs: 0x1cb0
-  __AUTH_CONST.__cfstring: 0x2f40
+  __DATA_CONST.__objc_const: 0x2b98
+  __DATA_CONST.__objc_selrefs: 0x1d18
+  __AUTH_CONST.__cfstring: 0x3220
   __AUTH_CONST.__objc_const: 0xfc0
-  __AUTH_CONST.__const: 0xb40
+  __AUTH_CONST.__const: 0xba0
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0x708
-  __AUTH.__objc_data: 0xb40
-  __DATA.__objc_classrefs: 0x258
-  __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0x190
+  __AUTH_CONST.__auth_got: 0x710
+  __AUTH.__objc_data: 0xb90
+  __DATA.__objc_classrefs: 0x268
+  __DATA.__objc_superrefs: 0x88
+  __DATA.__objc_ivar: 0x194
   __DATA.__data: 0x3a1
-  __DATA.__bss: 0x768
+  __DATA.__bss: 0x7a0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DF0DCAB3-08C9-38EC-A212-5F5B599AFD9F
-  Functions: 1001
-  Symbols:   3804
-  CStrings:  2518
+  UUID: 13674FCD-285E-3241-B933-FDF02316FC9E
+  Functions: 1025
+  Symbols:   3890
+  CStrings:  2583
 
Symbols:
+ +[DMCDateFormatterFactory isoLocalTimeZoneDateFormatter]
+ +[DMCHTTPRequestor jsonDictFromResponse:]
+ +[DMCHTTPRequestor parsePredefined403ErrorWithResponseDictionary:outError:]
+ -[ACAccountStore(DeviceManagementClient) _dmc_workerQueue]
+ -[DMCEvents .cxx_destruct]
+ -[DMCEvents _eventsFileFolder]
+ -[DMCEvents _eventsPlistFilePath]
+ -[DMCEvents _injectTimestamps:]
+ -[DMCEvents _logEvent:category:forTopic:]
+ -[DMCEvents _maximumEventCount]
+ -[DMCEvents errorFilePath]
+ -[DMCEvents init]
+ -[DMCEvents logErrorEventForTopic:reason:error:details:]
+ -[DMCEvents logRegularEventForTopic:reason:details:]
+ -[DMCEvents setErrorFilePath:]
+ -[DMCHTTPTransaction setTransactionCompletionBlock:]
+ -[DMCHTTPTransaction transactionCompletionBlock]
+ _DMCEventsFilePath
+ _DMCEventsFilePath.once
+ _DMCEventsFilePath.str
+ _DMCEventsTopicAccounts
+ _DMCEventsTopicOrgToken
+ _DMCEventsTopicPersona
+ _DMCEventsTopicPushToken
+ _DMCEventsTopicServerResponse
+ _DMCLoggingDirectory
+ _DMCLoggingDirectory.once
+ _DMCLoggingDirectory.str
+ _OBJC_CLASS_$_DMCDateFormatterFactory
+ _OBJC_CLASS_$_DMCEvents
+ _OBJC_CLASS_$_NSFileCoordinator
+ _OBJC_IVAR_$_DMCEvents._errorFilePath
+ _OBJC_IVAR_$_DMCHTTPTransaction._transactionCompletionBlock
+ _OBJC_METACLASS_$_DMCDateFormatterFactory
+ _OBJC_METACLASS_$_DMCEvents
+ __OBJC_$_CLASS_METHODS_DMCDateFormatterFactory
+ __OBJC_$_INSTANCE_METHODS_DMCEvents
+ __OBJC_$_INSTANCE_VARIABLES_DMCEvents
+ __OBJC_$_PROP_LIST_DMCEvents
+ __OBJC_CLASS_RO_$_DMCDateFormatterFactory
+ __OBJC_CLASS_RO_$_DMCEvents
+ __OBJC_METACLASS_RO_$_DMCDateFormatterFactory
+ __OBJC_METACLASS_RO_$_DMCEvents
+ ___17-[DMCEvents init]_block_invoke
+ ___41-[DMCEvents _logEvent:category:forTopic:]_block_invoke
+ ___41-[DMCEvents _logEvent:category:forTopic:]_block_invoke_2
+ ___41-[DMCEvents _logEvent:category:forTopic:]_block_invoke_3
+ ___42-[DMCHTTPTransaction performSynchronously]_block_invoke
+ ___45-[DMCHTTPTransaction performCompletionBlock:]_block_invoke.14
+ ___56+[DMCDateFormatterFactory isoLocalTimeZoneDateFormatter]_block_invoke
+ ___74-[ACAccountStore(DeviceManagementClient) dmc_removeAccounts:asynchronous:]_block_invoke.11
+ ___74-[ACAccountStore(DeviceManagementClient) dmc_removeAccounts:asynchronous:]_block_invoke_2
+ ___79-[ACAccountStore(DeviceManagementClient) _dmc_updateAccount:error:updateBlock:]_block_invoke_2
+ ___DMCEventsFilePath_block_invoke
+ ___DMCLoggingDirectory_block_invoke
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e25_v24?0"NSURL"8"NSURL"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.171
+ ___block_literal_global.184
+ ___block_literal_global.189
+ ___block_literal_global.195
+ ___block_literal_global.40
+ ___block_literal_global.45
+ ___block_literal_global.47
+ ___block_literal_global.52
+ ___block_literal_global.54
+ ___block_literal_global.59
+ __logEvent:category:forTopic:.onceToken
+ __logEvent:category:forTopic:.serialQueue
+ _init.onceToken
+ _isoLocalTimeZoneDateFormatter.dateFormatter
+ _isoLocalTimeZoneDateFormatter.onceToken
+ _objc_getAssociatedObject
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_beginTransaction
+ _objc_msgSend$_dmc_workerQueue
+ _objc_msgSend$_eventsFileFolder
+ _objc_msgSend$_eventsPlistFilePath
+ _objc_msgSend$_injectTimestamps:
+ _objc_msgSend$_logEvent:category:forTopic:
+ _objc_msgSend$_maximumEventCount
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:
+ _objc_msgSend$date
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$isoLocalTimeZoneDateFormatter
+ _objc_msgSend$jsonDictFromResponse:
+ _objc_msgSend$logErrorEventForTopic:reason:error:details:
+ _objc_msgSend$parsePredefined403ErrorWithResponseDictionary:outError:
+ _objc_msgSend$performCompletionBlock:
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$setFormatOptions:
+ _objc_msgSend$setTransactionCompletionBlock:
+ _objc_msgSend$transactionCompletionBlock
+ _objc_msgSend$underlyingErrors
+ _objc_setAssociatedObject
- +[DMCFeatureFlags isAppleWellKnownEnabled]
- +[DMCHTTPRequestor _jsonDictFromResponse:]
- +[DMCHTTPRequestor _parsePredefined403ErrorWithResponseDictionary:outError:]
- +[DMCWorkerThread theThread]
- -[DMCWorkerThread main]
- _OBJC_CLASS_$_DMCWorkerThread
- _OBJC_CLASS_$_NSRunLoop
- _OBJC_IVAR_$_DMCHTTPTransaction._doneSema
- _OBJC_METACLASS_$_DMCWorkerThread
- _OBJC_METACLASS_$_NSThread
- __OBJC_$_CLASS_METHODS_DMCWorkerThread
- __OBJC_$_INSTANCE_METHODS_DMCWorkerThread
- __OBJC_CLASS_RO_$_DMCWorkerThread
- __OBJC_METACLASS_RO_$_DMCWorkerThread
- ___28+[DMCWorkerThread theThread]_block_invoke
- ___74-[ACAccountStore(DeviceManagementClient) dmc_removeAccounts:asynchronous:]_block_invoke.10
- ___block_descriptor_49_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_literal_global.104
- ___block_literal_global.109
- ___block_literal_global.161
- ___block_literal_global.185
- ___block_literal_global.37
- ___block_literal_global.44
- ___block_literal_global.49
- ___block_literal_global.51
- _objc_msgSend$_jsonDictFromResponse:
- _objc_msgSend$_parsePredefined403ErrorWithResponseDictionary:outError:
- _objc_msgSend$currentRunLoop
- _objc_msgSend$initWithTimeIntervalSinceNow:
- _objc_msgSend$isCancelled
- _objc_msgSend$performSelector:onThread:withObject:waitUntilDone:
- _objc_msgSend$runUntilDate:
- _objc_msgSend$start
- _objc_msgSend$theThread
- _objc_retain_x28
- _theThread.pred
- _theThread.thread
CStrings:
+ "\x024\x16\x16"
+ "ACAccountStore+DMC"
+ "Account Identifier"
+ "Account Removal Failed"
+ "Accounts"
+ "DMCDateFormatterFactory"
+ "DMCEvents"
+ "DMCEvents.plist"
+ "Details"
+ "Error"
+ "Error Code"
+ "Error Description"
+ "Error Domain"
+ "Error Underlying Errors"
+ "Event category is not a dictionary"
+ "Failed to load event dictionary. Creating a new one"
+ "Logging"
+ "Org Token"
+ "Persona"
+ "Persona Removal Failed"
+ "Push Token"
+ "Reason"
+ "Regular"
+ "Server Response"
+ "T@\"NSString\",&,N,V_errorFilePath"
+ "T@?,C,N,V_transactionCompletionBlock"
+ "Timestamp"
+ "Timestamp (Localized)"
+ "Topic is not an array"
+ "Type"
+ "URLWithString:"
+ "[NSFileCoordinator coordinateReadingItemAtURL] failed with error: %{public}@"
+ "_dmc_workerQueue"
+ "_errorFilePath"
+ "_eventsFileFolder"
+ "_eventsPlistFilePath"
+ "_injectTimestamps:"
+ "_logEvent:category:forTopic:"
+ "_maximumEventCount"
+ "_transactionCompletionBlock"
+ "arrayWithArray:"
+ "coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:"
+ "date"
+ "dictionaryWithDictionary:"
+ "errorFilePath"
+ "insertObject:atIndex:"
+ "isoLocalTimeZoneDateFormatter"
+ "jsonDictFromResponse:"
+ "logErrorEventForTopic:reason:error:details:"
+ "logRegularEventForTopic:reason:details:"
+ "parsePredefined403ErrorWithResponseDictionary:outError:"
+ "persona ID"
+ "removeObjectsInRange:"
+ "setErrorFilePath:"
+ "setFormatOptions:"
+ "setTransactionCompletionBlock:"
+ "transactionCompletionBlock"
+ "underlyingErrors"
+ "v24@?0@\"NSURL\"8@\"NSURL\"16"
+ "v48@0:8@16@24@32@40"
- "\x024\x17\x15"
- "@\"NSObject<OS_dispatch_semaphore>\""
- "AppleWellKnown"
- "AppleWellKnownEnabled"
- "DMCWorkerThread"
- "TB,R,N,GisAppleWellKnownEnabled"
- "Worker thread starting"
- "_doneSema"
- "_jsonDictFromResponse:"
- "_parsePredefined403ErrorWithResponseDictionary:outError:"
- "currentRunLoop"
- "initWithTimeIntervalSinceNow:"
- "isAppleWellKnownEnabled"
- "isCancelled"
- "main"
- "performSelector:onThread:withObject:waitUntilDone:"
- "runUntilDate:"
- "start"
- "theThread"

```
