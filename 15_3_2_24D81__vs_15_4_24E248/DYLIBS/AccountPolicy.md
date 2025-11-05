## AccountPolicy

> `/System/Library/PrivateFrameworks/AccountPolicy.framework/Versions/A/AccountPolicy`

```diff

-61.0.0.0.0
-  __TEXT.__text: 0xf85c
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x11b4
-  __TEXT.__gcc_except_tab: 0x36c
-  __TEXT.__cstring: 0x1a80
-  __TEXT.__const: 0x38
-  __TEXT.__oslogstring: 0x3ce
+62.0.0.0.0
+  __TEXT.__text: 0x14220
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__objc_methlist: 0x1224
+  __TEXT.__gcc_except_tab: 0x490
+  __TEXT.__cstring: 0x19e5
+  __TEXT.__const: 0x50
+  __TEXT.__oslogstring: 0xa01
   __TEXT.__ustring: 0x26a
-  __TEXT.__unwind_info: 0x5e8
-  __TEXT.__objc_classname: 0x322
-  __TEXT.__objc_methname: 0x1c35
-  __TEXT.__objc_methtype: 0x272
-  __TEXT.__objc_stubs: 0x1940
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x198
+  __TEXT.__unwind_info: 0x638
+  __TEXT.__objc_classname: 0x333
+  __TEXT.__objc_methname: 0x1daf
+  __TEXT.__objc_methtype: 0x24a
+  __TEXT.__objc_stubs: 0x1c20
+  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b8
+  __DATA_CONST.__objc_selrefs: 0x860
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1b8
-  __AUTH_CONST.__const: 0x230
-  __AUTH_CONST.__cfstring: 0x19a0
-  __AUTH_CONST.__objc_const: 0x1e68
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__auth_got: 0x140
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x1b60
+  __AUTH_CONST.__objc_const: 0x1dc0
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0x128
-  __DATA.__bss: 0x30
+  __DATA.__objc_ivar: 0x50
+  __DATA.__data: 0x120
+  __DATA.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AccountPolicy.framework/Frameworks/CFAccountPolicy.framework/Versions/A/CFAccountPolicy
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 48BBE8B9-7485-3F6B-B89D-6D2E85F6DD7C
-  Functions: 369
-  Symbols:   1096
-  CStrings:  806
+  UUID: F6CB6A6E-A53A-387E-A594-0AFE369BCE67
+  Functions: 389
+  Symbols:   1137
+  CStrings:  880
 
Symbols:
+ +[APMessage messageWithType:data:]
+ +[APPolicy _localizedContentDescriptionsForFormat:].cold.1
+ -[APMessage initWithType:data:]
+ -[APMessage initWithType:data:].cold.1
+ -[APPolicySet attributesUsed].cold.1
+ -[APRequest(PolicyEvaluation) _createPolicyWithPredicate:]
+ -[APRequest(PolicyEvaluation) _evaluateGlobalPolicies:recordPolicies:inCategories:calculateExpiration:]
+ -[APRequest(PolicyEvaluation) _evaluateGlobalPolicies:recordPolicies:inCategories:calculateExpiration:].cold.1
+ -[APRequest(PolicyEvaluation) _evaluateGlobalPolicies:recordPolicies:inCategories:calculateExpiration:].cold.2
+ -[APRequest(PolicyEvaluation) _evaluatePolicy:withInfo:expectedResult:]
+ -[APRequest(PolicyEvaluation) _evaluatePolicy:withInfo:expectedResult:].cold.1
+ -[APRequest(PolicyEvaluation) _evaluatePolicy:withInfo:expectedResult:].cold.2
+ -[APRequest(PolicyEvaluation) _expectedResultForCategory:]
+ -[APRequest(PolicyEvaluation) _gatherPoliciesForCategories:]
+ -[APRequest(PolicyEvaluation) _policiesFromCacheOrRequest]
+ -[APRequest(PolicyEvaluation) _policiesFromCacheOrRequest].cold.1
+ -[APRequest(PolicyEvaluation) _policiesFromCacheOrRequest].cold.2
+ -[APRequest(PolicyEvaluation) _policiesFromCacheOrRequest].cold.3
+ -[APRequest(PolicyEvaluation) _removePoliciesFromGlobal:thatExistInRecord:]
+ -[APRequest(PolicyEvaluation) _removePoliciesFromGlobal:thatExistInRecord:].cold.1
+ -[APRequest(PolicyEvaluation) _updatePolicies:withNewPolicies:forCategories:]
+ -[APRequest(PolicyEvaluation) _updatePolicies:withNewPolicies:forCategories:].cold.1
+ -[APRequest(PolicyEvaluation) _validPolicy:]
+ -[APRequest(PolicyEvaluation) _validPolicy:].cold.1
+ -[APRequest(PolicyEvaluation) _validPolicy:].cold.2
+ -[APRequest(PolicyEvaluation) _validRecordInfo:]
+ -[APRequest(PolicyEvaluation) calculatePolicyExpirationInCategories:]
+ -[APRequest(PolicyEvaluation) evaluatePoliciesAndCreateResponse]
+ -[APRequest(PolicyEvaluation) evaluatePoliciesAndCreateResponse].cold.1
+ -[APRequest(PolicyEvaluation) evaluatePoliciesInCategories:]
+ -[APRequest(PolicyEvaluation) logPredicate:andParameters:]
+ -[APRequest(PolicyEvaluation) logPredicate:andParameters:].cold.1
+ -[APRequest(PolicyEvaluation) logPredicate:andParameters:].cold.2
+ GCC_except_table32
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSValue
+ _OBJC_EHTYPE_$_NSException
+ __OBJC_$_INSTANCE_METHODS_APRequest(PolicyEvaluation)
+ ___103-[APRequest(PolicyEvaluation) _evaluateGlobalPolicies:recordPolicies:inCategories:calculateExpiration:]_block_invoke
+ ___77-[APRequest(PolicyEvaluation) _updatePolicies:withNewPolicies:forCategories:]_block_invoke
+ ___NSDictionary0__struct
+ ____referenceTimeAttribute_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e15_v32?08Q16^B24l
+ ___copy_helper_block_e8_32s40s48s
+ ___destroy_helper_block_e8_32s40s48s
+ ___getSharedLogHandle_block_invoke
+ __block_literal_global.124
+ __calculateExpirationForEnableAtTimeOfDay
+ __calculateExpirationForEnableOnDate
+ __calculateExpirationForEnableOnDayOfWeek
+ __calculateExpirationForExpiresAtTimeOfDay
+ __calculateExpirationForExpiresInDays
+ __calculateExpirationForExpiresOnDate
+ __calculateExpirationForExpiresOnDayOfWeek
+ __os_assert_log
+ __os_crash
+ __stringWithExpirationTime
+ _calculateExpirationForExpiresInDays.cold.1
+ _evaluateGlobalPolicies:recordPolicies:inCategories:calculateExpiration:.expirationAttrsAndFunctions
+ _evaluateGlobalPolicies:recordPolicies:inCategories:calculateExpiration:.once
+ _kAPAttributeEnableAtTimeOfDay
+ _kAPAttributeEnableOnDate
+ _kAPAttributeEnableOnDayOfWeek
+ _kAPAttributeExpiresAtTimeOfDay
+ _kAPAttributeExpiresEveryNDays
+ _kAPAttributeExpiresOnDayOfWeek
+ _kAPAttributeGlobalPolicies
+ _kAPAttributeGlobalPoliciesGUID
+ _kAPAttributeIsAdministrativelyDisabled
+ _kAPAttributeRecordPolicies
+ _kAPAttributeRecordPoliciesGUID
+ _objc_msgSend$_createPolicyWithPredicate:
+ _objc_msgSend$_evaluateGlobalPolicies:recordPolicies:inCategories:calculateExpiration:
+ _objc_msgSend$_evaluatePolicy:withInfo:expectedResult:
+ _objc_msgSend$_expectedResultForCategory:
+ _objc_msgSend$_gatherPoliciesForCategories:
+ _objc_msgSend$_policiesFromCacheOrRequest
+ _objc_msgSend$_removePoliciesFromGlobal:thatExistInRecord:
+ _objc_msgSend$_validPolicy:
+ _objc_msgSend$_validRecordInfo:
+ _objc_msgSend$allValues
+ _objc_msgSend$calculatePolicyExpirationInCategories:
+ _objc_msgSend$components:fromDate:toDate:options:
+ _objc_msgSend$copyCacheContents
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$day
+ _objc_msgSend$evaluatePoliciesAndCreateResponse
+ _objc_msgSend$evaluatePoliciesInCategories:
+ _objc_msgSend$evaluateWithObject:
+ _objc_msgSend$initWithType:data:
+ _objc_msgSend$invalidateCache
+ _objc_msgSend$invert
+ _objc_msgSend$logPredicate:andParameters:
+ _objc_msgSend$messageWithType:data:
+ _objc_msgSend$nextDateAfterDate:matchingUnit:value:options:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$pointerValue
+ _objc_msgSend$predicateFormat
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
+ _objc_msgSend$replyWithSuccess
+ _objc_msgSend$second
+ _objc_msgSend$setHour:
+ _objc_msgSend$setMinute:
+ _objc_msgSend$startOfDayForDate:
+ _objc_msgSend$valueWithPointer:
+ _referenceTimeAttribute.nonAlphaNumeric
+ _referenceTimeAttribute.once
+ _referenceTimeAttribute.referenceTimeAttrs
+ getSharedLogHandle.onceToken
+ getSharedLogHandle.sharedLogHandle
- +[APMessage messageWithReceivedXPCMessage:]
- +[APMessage messageWithType:data:receivedXPCMessage:]
- +[APMessage outgoingMessageWithType:andData:]
- -[APMessage initOutgoingMessageWithType:andData:]
- -[APMessage initWithReceivedXPCMessage:]
- -[APMessage initWithReceivedXPCMessage:].cold.1
- -[APMessage initWithType:data:receivedXPCMessage:]
- -[APMessage receivedXPCMessage]
- -[APMessage sendOnConnection:]
- -[APMessage sendToHelperAndReturnResponse]
- -[APMessage sendToHelperAndReturnResponse].cold.1
- -[APMessage sendWithReplyOnConnection:replyQueue:replyHandler:]
- -[APMessage sendWithReplyOnConnectionSync:error:]
- -[APMessage xpcMessage]
- -[APRequest evaluatePolicyAndReturnResponse].cold.1
- -[APRequest evaluatePolicyAndReturnResponse].cold.2
- -[APRequest logHandle]
- GCC_except_table17
- GCC_except_table26
- GCC_except_table29
- GCC_except_table38
- OBJC_IVAR_$_APMessage._receivedXPCMessage
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSPropertyListSerialization
- __42-[APMessage sendToHelperAndReturnResponse]_block_invoke.73
- __42-[APMessage sendToHelperAndReturnResponse]_block_invoke.cold.1
- __42-[APMessage sendToHelperAndReturnResponse]_block_invoke.cold.2
- __OBJC_$_INSTANCE_METHODS_APRequest
- ___22-[APRequest logHandle]_block_invoke
- ___42-[APMessage sendToHelperAndReturnResponse]_block_invoke
- ___63-[APMessage sendWithReplyOnConnection:replyQueue:replyHandler:]_block_invoke
- ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_40_e8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_48_e8_32s40r_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___copy_helper_block_e8_32s40r
- ___destroy_helper_block_e8_32s40r
- __xpc_error_connection_interrupted
- __xpc_error_connection_invalid
- __xpc_type_dictionary
- __xpc_type_error
- _dispatch_queue_create
- _kAPHelperName
- _objc_msgSend$bytes
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$dataWithPropertyList:format:options:error:
- _objc_msgSend$initOutgoingMessageWithType:andData:
- _objc_msgSend$initWithReceivedXPCMessage:
- _objc_msgSend$initWithType:data:receivedXPCMessage:
- _objc_msgSend$messageWithReceivedXPCMessage:
- _objc_msgSend$outgoingMessageWithType:andData:
- _objc_msgSend$propertyListWithData:options:format:error:
- _objc_msgSend$replyWithError:
- _objc_msgSend$replyWithErrorCode:andFormat:
- _objc_msgSend$sendToHelperAndReturnResponse
- _objc_msgSend$sendWithReplyOnConnectionSync:error:
- _objc_msgSend$xpcMessage
- _objc_retainAutoreleaseReturnValue
- _objc_unsafeClaimAutoreleasedReturnValue
- _xpc_connection_cancel
- _xpc_connection_create
- _xpc_connection_resume
- _xpc_connection_send_message
- _xpc_connection_send_message_with_reply
- _xpc_connection_send_message_with_reply_sync
- _xpc_connection_set_event_handler
- _xpc_dictionary_create
- _xpc_dictionary_create_reply
- _xpc_dictionary_get_data
- _xpc_dictionary_get_int64
- _xpc_dictionary_set_data
- _xpc_dictionary_set_int64
- _xpc_get_type
- logHandle.onceToken
- logHandle.sharedLogHandle
CStrings:
+ "%{pubic}@: Policy \"%@\" skipped: evaluation raised an exception"
+ "%{public}@: Calculating expiration for policy \"%@\" using attribute \"%@ = %@\""
+ "%{public}@: Evaluating %d %@ %s in category %@"
+ "%{public}@: Evaluating policy \"%@\""
+ "%{public}@: Expiration calculation result for policy %@: %@"
+ "%{public}@: Global policies in category %@ are not an array, not merging with record policies"
+ "%{public}@: Global policy \"%@\" is overridden by record policy with the same identifier"
+ "%{public}@: No %@ policies in category %@"
+ "%{public}@: No record policies in category %@, using global policies as is"
+ "%{public}@: No record policies, using global policies as is"
+ "%{public}@: Not updating policies in category %@: policies are not an array"
+ "%{public}@: Not updating policies: existing policies are nil"
+ "%{public}@: Policy \"%@\" %s (evaluated to %s, expected %s)"
+ "%{public}@: Policy \"%@\" skipped: evaluation raised an exception: %@"
+ "%{public}@: Policy '%@' is missing the key '%@'"
+ "%{public}@: Policy '%@' is not a dictionary"
+ "%{public}@: Policy is empty"
+ "%{public}@: Received invalid request %@"
+ "%{public}@: Record policies in category %@ are not an array, not merging with global policies"
+ "%{public}@: Skipping all %@ policies in category %@: policies are not an array"
+ "%{public}@: Skipping policy \"%@\": nil predicate returned for predicate string \"%@\""
+ "%{public}@: Skipping policy \"%@\": predicate creation failed for predicate string \"%@\""
+ "%{public}@: Skipping policy \"%@\": predicate creation failed for predicate string \"%@\": %@"
+ "%{public}@: completed request for record \"%@\", result: %@ (%d)%@"
+ "%{public}@: completed request for record \"%@\", result: %@%@"
+ "%{public}@: evaluating policies for record \"%@\", record type \"%@\""
+ "%{public}@: evaluating policy"
+ "%{public}@: evaluating policy after request for more information"
+ "%{public}@: parameters: %@"
+ "%{public}@: policy evaulation requested additional data: %@"
+ "%{public}@: predicate: \"%@\""
+ "%{public}@: record \"%@\", record type \"%@\""
+ "%{public}@: record is administratively disabled, setting result to \"failed authentication policy\""
+ "******"
+ ", %@"
+ ", expiration time from %@ policy \"%@\""
+ "@36@0:8@16@24B32"
+ "@44@0:8@16@24@32B40"
+ "Failed %@ policy \"%@\""
+ "Global policies are not a dictionary"
+ "Invalid request"
+ "Message data is malformed"
+ "Policy data is malformed"
+ "PolicyEvaluation"
+ "Record info data is malformed"
+ "Record policies are not a dictionary"
+ "_createPolicyWithPredicate:"
+ "_evaluateGlobalPolicies:recordPolicies:inCategories:calculateExpiration:"
+ "_evaluatePolicy:withInfo:expectedResult:"
+ "_expectedResultForCategory:"
+ "_gatherPoliciesForCategories:"
+ "_policiesFromCacheOrRequest"
+ "_removePoliciesFromGlobal:thatExistInRecord:"
+ "_updatePolicies:withNewPolicies:forCategories:"
+ "_validPolicy:"
+ "_validRecordInfo:"
+ "allValues"
+ "builtin"
+ "calculatePolicyExpirationInCategories:"
+ "com.apple.AccountPolicy.builtin-administratively-disabled"
+ "components:fromDate:toDate:options:"
+ "contains %d hash%s"
+ "contains %d history item%s"
+ "copyCacheContents"
+ "dateFromComponents:"
+ "day"
+ "es"
+ "evaluatePoliciesAndCreateResponse"
+ "evaluatePoliciesInCategories:"
+ "evaluateWithObject:"
+ "expires in %lld seconds (%@)"
+ "failed"
+ "false"
+ "global"
+ "has expired"
+ "initWithType:data:"
+ "invalidateCache"
+ "invert"
+ "kAPPolicyKeyPolicySet"
+ "kAPPolicyKeyPredicate"
+ "kAPPolicyKeySource"
+ "kAPResultKeyEvaluationDetails"
+ "kAPResultKeyParameters"
+ "kAPResultKeyPolicyIdentifier"
+ "kAPResultKeyPolicySource"
+ "kAPResultKeyResult"
+ "logPredicate:andParameters:"
+ "messageWithType:data:"
+ "never expires"
+ "nextDateAfterDate:matchingUnit:value:options:"
+ "numberWithBool:"
+ "passed"
+ "pointerValue"
+ "policies"
+ "predicateFormat"
+ "predicateWithFormat:"
+ "record"
+ "removeObjectsInRange:"
+ "replaceObjectAtIndex:withObject:"
+ "replaceOccurrencesOfString:withString:options:range:"
+ "s"
+ "second"
+ "setHour:"
+ "setMinute:"
+ "startOfDayForDate:"
+ "true"
+ "valueWithPointer:"
- "%{public}@: Failed to create XPC connection to Account Policy helper agent"
- "%{public}@: Sending back to helper for evaluation"
- "%{public}@: Sending to helper for evaluation"
- "%{public}@: Unhandled XPC event: %{public}@"
- "%{public}@: XPC connection error: %@"
- "%{public}@: helper requested additional data: %@"
- "@\"NSObject<OS_xpc_object>\""
- "@32@0:8@16^@24"
- "@36@0:8i16@20@28"
- "Connection error from Account Policy helper agent for request %@: %@"
- "Data in request %{public}@ is malformed, ignoring"
- "Nil connection parameter for request %@"
- "No reply from helper agent for request %@"
- "T@\"NSObject<OS_xpc_object>\",R,C,V_receivedXPCMessage"
- "Unable to create dispatch queue for xpc connection to Account Policy helper agent for request %@"
- "Unable to create xpc connection to Account Policy helper agent for request %@"
- "Unhandled event %@ from Account Policy helper agent for request %@"
- "XPC connection interrupted for request %@"
- "XPC connection was interrupted for request %{public}@"
- "XPC connection was invalidated for request %@"
- "XPC connection was invalidated for request %{public}@"
- "XPC reply didn't contain a valid response for request %@"
- "XPC reply didn't contain a valid response for request %{public}@"
- "_receivedXPCMessage"
- "bytes"
- "com.apple.AccountPolicy.helperConnectionQueue"
- "com.apple.AccountPolicyHelper"
- "connection interrupted"
- "connection invalid"
- "dataWithBytes:length:"
- "dataWithPropertyList:format:options:error:"
- "initOutgoingMessageWithType:andData:"
- "initWithReceivedXPCMessage:"
- "initWithType:data:receivedXPCMessage:"
- "kAPMessageKeyMessageData"
- "kAPMessageKeyMessageType"
- "messageWithReceivedXPCMessage:"
- "messageWithType:data:receivedXPCMessage:"
- "outgoingMessageWithType:andData:"
- "propertyListWithData:options:format:error:"
- "receivedXPCMessage"
- "sendOnConnection:"
- "sendToHelperAndReturnResponse"
- "sendWithReplyOnConnection:replyQueue:replyHandler:"
- "sendWithReplyOnConnectionSync:error:"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "v40@0:8@16@24@?32"
- "xpcMessage"

```
