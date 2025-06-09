## OSASubmissionClient

> `/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient`

```diff

-758.120.5.0.0
-  __TEXT.__text: 0x1b24
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x268
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x20a
-  __TEXT.__oslogstring: 0x243
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x68
-  __TEXT.__objc_methname: 0x6f1
-  __TEXT.__objc_methtype: 0x202
-  __TEXT.__objc_stubs: 0x620
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x148
+912.0.0.0.0
+  __TEXT.__text: 0x25b8
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_methlist: 0x2b8
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0xb8
+  __TEXT.__cstring: 0x249
+  __TEXT.__oslogstring: 0x4a7
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_classname: 0x7f
+  __TEXT.__objc_methname: 0x7d0
+  __TEXT.__objc_methtype: 0x262
+  __TEXT.__objc_stubs: 0x740
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x278
+  __DATA_CONST.__objc_selrefs: 0x2d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__objc_arraydata: 0x60
+  __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x3c8
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__cfstring: 0x260
+  __AUTH_CONST.__objc_const: 0x3d8
+  __AUTH_CONST.__objc_dictobj: 0x78
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7ECDAB95-ABFD-30A9-85FF-6A5CD141BEC3
-  Functions: 33
-  Symbols:   250
-  CStrings:  189
+  UUID: 2B3503D9-E8F7-3C87-AA1E-BD91656F6FEA
+  Functions: 49
+  Symbols:   317
+  CStrings:  220
 
Symbols:
+ +[OSASubmissionClient submissionOptionsFromClientOptions:]
+ +[OSASubmissionScheduler scheduleCleanupForUser:]
+ -[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath]
+ -[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath].cold.1
+ -[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath].cold.2
+ -[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath].cold.3
+ -[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath].cold.4
+ -[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath].cold.5
+ -[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath].cold.6
+ -[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath].cold.7
+ -[OSASubmissionClient(OSADRESubmissionClient) submitDRETelemetryAndDiagnostics:]
+ -[OSASubmissionClient(OSADRESubmissionClient) submitDRETelemetryAndDiagnostics:].cold.1
+ -[OSASubmissionClient(OSADRESubmissionClient) submitDRETelemetryAndDiagnostics:].cold.2
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table29
+ _AnalyticsRolloverEvents
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSXPCEncoder
+ _OBJC_CLASS_$_OverrideMountPathRequest
+ _OSASandboxExtensionForPath
+ _OSASyncCrashReporter
+ _OSAnalyticsHelperServiceConnection
+ _OUTLINED_FUNCTION_0
+ _SANDBOX_EXTENSION_NOFOLLOW
+ __OBJC_$_CLASS_METHODS_OSASubmissionClient
+ __OBJC_$_INSTANCE_METHODS_OSASubmissionClient(OSADRESubmissionClient)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_OSASubmissionServices
+ ___49+[OSASubmissionScheduler scheduleCleanupForUser:]_block_invoke
+ ___49+[OSASubmissionScheduler scheduleCleanupForUser:]_block_invoke.45
+ ___49+[OSASubmissionScheduler scheduleCleanupForUser:]_block_invoke_2
+ ___64-[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath]_block_invoke
+ ___64-[OSASubmissionClient(OSADRESubmissionClient) overrideMountPath]_block_invoke.cold.1
+ ___80-[OSASubmissionClient(OSADRESubmissionClient) submitDRETelemetryAndDiagnostics:]_block_invoke
+ ___80-[OSASubmissionClient(OSADRESubmissionClient) submitDRETelemetryAndDiagnostics:]_block_invoke.cold.1
+ ___80-[OSASubmissionClient(OSADRESubmissionClient) submitDRETelemetryAndDiagnostics:]_block_invoke.cold.2
+ ___block_descriptor_40_e8_32r_e22_v16?0"NSDictionary"8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ ___error
+ __xpc_error_key_description
+ __xpc_type_dictionary
+ __xpc_type_error
+ _objc_msgSend$addObject:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$beginEncoding
+ _objc_msgSend$boolValue
+ _objc_msgSend$count
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$finishEncoding
+ _objc_msgSend$initWithSandboxExtensions:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$overrideMountPath
+ _objc_msgSend$overrideSubmissionServiceMountPath:withReply:
+ _objc_msgSend$pathContainerRoot
+ _objc_msgSend$pathRoot
+ _objc_msgSend$submissionOptionsFromClientOptions:
+ _objc_opt_new
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retain_x27
+ _strerror
+ _xpc_connection_send_message_with_reply_sync
+ _xpc_dictionary_create
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_string
+ _xpc_dictionary_set_uint64
+ _xpc_dictionary_set_value
+ _xpc_get_type
- +[OSASubmissionScheduler scheduleCleanupWithHomeDirectory:]
- -[OSASubmissionClient submitWithOptions:].cold.1
- _OBJC_CLASS_$_OSASubmitter
- _OSAIsACDCDevice
- _OSAIsRSDDisplay
- __OBJC_$_INSTANCE_METHODS_OSASubmissionClient
- ___59+[OSASubmissionScheduler scheduleCleanupWithHomeDirectory:]_block_invoke
- ___59+[OSASubmissionScheduler scheduleCleanupWithHomeDirectory:]_block_invoke.45
- ___59+[OSASubmissionScheduler scheduleCleanupWithHomeDirectory:]_block_invoke_2
- ___block_descriptor_48_e8_32s40r_e22_v16?0"NSDictionary"8lr40l8s32l8
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_msgSend$cleanupRetired:
- _objc_msgSend$dictionaryWithObject:forKey:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$optInApple
- _objc_msgSend$submissionPathsWithHomeDirectory:withProxies:
- _objc_release_x27
CStrings:
+ "B20@0:8B16"
+ "Connection error to %s: %s"
+ "Did not receive reply from %s"
+ "Error issuing sandbox extension to %@: %i (%s)"
+ "Failed to establish connection to %s"
+ "Failed to issue all necessary sandbox extensions"
+ "Failed to override mount path for log-writing service"
+ "Failed to override mount path for submission service"
+ "Failed to override mount path locally"
+ "Failed to rollover CoreAnalytics log"
+ "Failed to sync with ReportCrash: %@"
+ "Issued sandbox extension to %@"
+ "OSADRESubmissionClient"
+ "Submission failed"
+ "Submission results: %@"
+ "Successful CoreAnalytics log rollover"
+ "Successful submission"
+ "Successful sync with ReportCrash"
+ "Successfully overrode mount path for log-writing service"
+ "Successfully overrode mount path for submission service"
+ "Unexpected reply from %s"
+ "addObject:"
+ "arrayWithObjects:count:"
+ "beginEncoding"
+ "boolValue"
+ "cleanupWithHomeDirectoryLocation:options:"
+ "com.apple.osanalytics.osanalyticshelper"
+ "count"
+ "dre_overrideMountPath"
+ "encodeObject:forKey:"
+ "finishEncoding"
+ "initWithSandboxExtensions:"
+ "localizedDescription"
+ "operation"
+ "overrideMountPath"
+ "overrideSubmissionServiceMountPath:withReply:"
+ "pathContainerRoot"
+ "pathRoot"
+ "scheduleCleanupForUser:"
+ "submissionOptionsFromClientOptions:"
+ "submitDRETelemetryAndDiagnostics:"
+ "v12@?0B8"
+ "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
+ "v32@0:8@\"OverrideMountPathRequest\"16@?<v@?B>24"
- "Cancelling submission due to opt-out."
- "Log submission results: %@"
- "Opted out. Not submitting logs..."
- "cleanupRetired:"
- "dictionaryWithObject:forKey:"
- "error"
- "isEqualToString:"
- "optInApple"
- "scheduleCleanupWithHomeDirectory:"
- "submissionPathsWithHomeDirectory:withProxies:"
- "submissions"

```
