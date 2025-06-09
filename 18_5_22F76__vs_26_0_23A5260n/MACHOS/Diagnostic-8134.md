## Diagnostic-8134

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8134.appex/Diagnostic-8134`

```diff

-820.122.1.0.0
-  __TEXT.__text: 0x20b4
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x35c
-  __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x84
-  __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0xba7
-  __TEXT.__objc_methtype: 0x175
-  __TEXT.__oslogstring: 0x141
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x120
-  __DATA_CONST.__cfstring: 0xa0
-  __DATA_CONST.__objc_classlist: 0x18
+1053.0.0.0.0
+  __TEXT.__text: 0x308
+  __TEXT.__auth_stubs: 0xe0
+  __TEXT.__objc_stubs: 0x220
+  __TEXT.__objc_methlist: 0x1dc
+  __TEXT.__objc_classname: 0x5a
+  __TEXT.__objc_methname: 0x395
+  __TEXT.__objc_methtype: 0x115
+  __TEXT.__cstring: 0x46
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__auth_got: 0x78
+  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0x550
-  __DATA.__objc_selrefs: 0x3b8
-  __DATA.__objc_ivar: 0x2c
-  __DATA.__objc_data: 0xf0
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x340
+  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
-  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
-  - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
-  - /System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState
-  - /usr/lib/libMobileGestalt.dylib
+  - /System/Library/PrivateFrameworks/EnhancedLogging.framework/EnhancedLogging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85D69448-E9D0-3093-896C-DD76407B9573
-  Functions: 59
-  Symbols:   91
-  CStrings:  202
+  UUID: 2DB17517-9AD9-3ACA-9329-A35554EE4A30
+  Functions: 12
+  Symbols:   33
+  CStrings:  86
 
Symbols:
+ _OBJC_CLASS_$_ELSessionConfigurator
- _DiagnosticLogHandleForCategory
- _ELSDefaultConsentHandles
- _ELSDefaultFollowUpOptions
- _ELSDefaultMetadata
- _ELSDefaultQueue
- _ELSFollowUpOptionFrequency
- _ELSFollowUpOptionUseSpringBoardNotification
- _ELSMetadataDeviceSerialNumber
- _ELSMetadataDeviceType
- _ELSMetadataEnrollmentTicketNumber
- _ELSMetadataPayload
- _ELSMetadataUserAppleID
- _ELSParameterCommand
- _ELSParameterPayload
- _ELSParameterPayloadsDict
- _ELSParameterPrivacyPolicy
- _ELSParameterRetries
- _ELSPrivacyPolicyDescriptionPolicyKey
- _ELSPrivacyPolicyDescriptionSensitiveInformationKey
- _ELSPrivacyPolicyDescriptionSuiteNameKey
- _ELSSubDefaultConsentHandleEntryHandle
- _ELSSubDefaultQueueEntryExecuteAfterDuration
- _ELSSubDefaultQueueEntryPlatform
- _ELSSubDefaultQueueEntryRetry
- _ELSSubDefaultQueueEntryType
- _MGCopyAnswer
- _OBJC_CLASS_$_ACAccountStore
- _OBJC_CLASS_$_DASharedTestStatusHelper
- _OBJC_CLASS_$_ELSManager
- _OBJC_CLASS_$_ELSPrivacyPolicyDescription
- _OBJC_CLASS_$_ELSQueueEntry
- _OBJC_CLASS_$_ELSWhitelist
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSCharacterSet
- _OBJC_CLASS_$_NSJSONSerialization
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSString
- _OBJC_METACLASS_$_DASharedTestStatusHelper
- __NSConcreteGlobalBlock
- __NSConcreteStackBlock
- __os_log_error_impl
- _objc_autoreleaseReturnValue
- _objc_enumerationMutation
- _objc_opt_class
- _objc_opt_isKindOfClass
- _objc_release
- _objc_release_x20
- _objc_release_x28
- _objc_release_x8
- _objc_retain
- _objc_retainBlock
- _objc_retain_x1
- _objc_retain_x19
- _objc_retain_x2
- _objc_retain_x20
- _objc_retain_x22
- _os_log_type_enabled
CStrings:
+ "T@\"NSDictionary\",&,N,V_rawSpecifications"
+ "_rawSpecifications"
+ "configureSessionWithParameters:ticket:error:"
+ "dictionaryWithObjects:forKeys:count:"
+ "parameters"
+ "rawSpecifications"
+ "setRawSpecifications:"
+ "specifications"
+ "statusCode"
- ","
- "@\"NSArray\""
- "@24@0:8@16"
- "@24@0:8^B16"
- "Attempted to commit an empty queue to enhanced logging state"
- "B16@?0@8"
- "Could not find primary Apple Account"
- "Could not find primary Apple Account username"
- "Could not open Apple Account Store"
- "DASharedTestStatusHelper"
- "Enhanced logging already queued for: %@"
- "Enhanced logging already running, cannot enroll"
- "Enhanced logging not already running, cannot unenroll"
- "ProductType"
- "Q"
- "SerialNumber"
- "T@\"NSArray\",&,N,V_consentHandles"
- "T@\"NSArray\",&,N,V_queue"
- "T@\"NSDictionary\",&,N,V_followUpOptions"
- "T@\"NSDictionary\",&,N,V_metadata"
- "T@\"NSDictionary\",&,N,V_parameterPayloads"
- "T@\"NSDictionary\",&,N,V_specificationPayloads"
- "T@\"NSDictionary\",&,N,V_topLevelPrivacyPolicy"
- "TQ,N,V_command"
- "Tq,N,V_retries"
- "_command"
- "_consentHandles"
- "_followUpOptions"
- "_metadata"
- "_parameterPayloads"
- "_queue"
- "_retries"
- "_specificationPayloads"
- "_topLevelPrivacyPolicy"
- "aa_primaryAppleAccount"
- "addAppleAccount:"
- "addDeviceSerialNumber:"
- "addDeviceType:"
- "addEnrollmentTicketNumber:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addPayload:"
- "addServerSuppliedMetadata:"
- "aggregateMetadata"
- "allKeys"
- "array"
- "arrayWithArray:"
- "boolValue"
- "bundleIdentifier"
- "code"
- "command"
- "componentsSeparatedByString:"
- "consentHandles"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createQueueEntryInputDictionary:"
- "dataWithJSONObject:options:error:"
- "dictionary"
- "dictionaryWithDictionary:"
- "dk_arrayFromKey:types:maxLength:defaultValue:failed:validator:"
- "dk_arrayFromRequiredKey:types:maxLength:failed:validator:"
- "dk_dictionaryFromKey:defaultValue:failed:"
- "dk_dictionaryFromKey:limitedToKeys:defaultValue:failed:"
- "dk_numberFromKey:lowerBound:upperBound:defaultValue:failed:"
- "dk_numberFromRequiredKey:lowerBound:upperBound:failed:"
- "doubleValue"
- "enrollWithFlush:commit:"
- "findEntryForParameterName:"
- "finishWithStatusCode:metadata:"
- "flush"
- "followUpOptions"
- "formatNewQueueEntries:"
- "getTopLevelPrivacyPolicy"
- "initWithData:encoding:"
- "initWithPolicyKey:andSuiteNameKey:andSensitiveInformationKey:"
- "initWithType:typeName:parameters:executeAfterDuration:retry:platform:"
- "integerValue"
- "lowercaseString"
- "metadata"
- "mutableCopy"
- "objectForKeyedSubscript:"
- "parameterPayloads"
- "platformAvailability"
- "q16@0:8"
- "queue"
- "refreshWithCompletion:"
- "retries"
- "retry"
- "setCommand:"
- "setConsentHandles:"
- "setFollowUpOptions:"
- "setMetadata:"
- "setObject:forKeyedSubscript:"
- "setParameterPayloads:"
- "setQueue:"
- "setRetries:"
- "setRetriesRemaining:"
- "setSpecificationPayloads:"
- "setStatus:"
- "setTopLevelPrivacyPolicy:"
- "setWithObject:"
- "setWithObjects:"
- "sharedManager"
- "snapshot"
- "specificationPayloads"
- "status"
- "statusCodeForArchiveError:"
- "stringByTrimmingCharactersInSet:"
- "topLevelPrivacyPolicy"
- "transactionWithBlock:completion:"
- "unenroll"
- "updateEnhancedLoggingStateWithNewQueueEntries:commit:"
- "username"
- "v16@?0@\"ELSSnapshot\"8"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v24@?0@\"ELSSnapshot\"8B16B20"
- "v28@0:8@16B24"
- "whitespaceAndNewlineCharacterSet"

```
