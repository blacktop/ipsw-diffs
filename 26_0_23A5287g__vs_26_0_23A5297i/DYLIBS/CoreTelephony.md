## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13080.2.0.0.0
-  __TEXT.__text: 0x18e930
+13085.1.0.0.0
+  __TEXT.__text: 0x18ed8c
   __TEXT.__auth_stubs: 0x1990
   __TEXT.__objc_methlist: 0x1b42c
   __TEXT.__const: 0x1002
-  __TEXT.__gcc_except_tab: 0x1def0
-  __TEXT.__cstring: 0x1f7e5
-  __TEXT.__oslogstring: 0x4368
+  __TEXT.__gcc_except_tab: 0x1df1c
+  __TEXT.__cstring: 0x1f84a
+  __TEXT.__oslogstring: 0x43e5
   __TEXT.__swift5_typeref: 0x17
   __TEXT.__unwind_info: 0xd1d0
   __TEXT.__objc_classname: 0x5928
   __TEXT.__objc_methname: 0x22c57
   __TEXT.__objc_methtype: 0x72e4
-  __TEXT.__objc_stubs: 0x16ce0
+  __TEXT.__objc_stubs: 0x16d00
   __DATA_CONST.__got: 0xb00
-  __DATA_CONST.__const: 0x7388
+  __DATA_CONST.__const: 0x7398
   __DATA_CONST.__objc_classlist: 0x1530
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x250

   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0xce0
   __AUTH_CONST.__const: 0x2080
-  __AUTH_CONST.__cfstring: 0x1da80
+  __AUTH_CONST.__cfstring: 0x1dbe0
   __AUTH_CONST.__objc_const: 0x2f928
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: E9A51677-1082-3A76-B5EF-E9C2542F5304
-  Functions: 11280
-  Symbols:   38265
-  CStrings:  17103
+  UUID: 1931F820-D819-3C7C-8DE3-812BD558DAAC
+  Functions: 11282
+  Symbols:   38269
+  CStrings:  17131
 
Symbols:
+ __ZL32_SendXpcMessageWithReplyAndRetryP20__CTServerConnectionN3xpc4dictEm
+ __ZL32_SendXpcMessageWithReplyAndRetryP20__CTServerConnectionN3xpc4dictEm.cold.1
+ _objc_msgSend$uniqueIdentifier
- _kCTCellularUsageAllSubscriberTags
Functions:
~ __Z16SendXpcMessageIfbP20__CTServerConnectionRKN3xpc4dictERS2_20CTFeatureRequirement : 656 -> 556
~ __ZL25_HandlePrepWorkBeforeSendP20__CTServerConnectionRN3xpc4dictEb : 200 -> 220
~ ____ZL25_HandlePrepWorkBeforeSendP20__CTServerConnectionRN3xpc4dictEb_block_invoke : 308 -> 280
~ -[CTMessage description] : 180 -> 452
~ -[CTMessageCenter incomingMessageWithId:] : 1232 -> 1376
+ __ZL32_SendXpcMessageWithReplyAndRetryP20__CTServerConnectionN3xpc4dictEm
+ __ZL32_SendXpcMessageWithReplyAndRetryP20__CTServerConnectionN3xpc4dictEm.cold.1
CStrings:
+ "#I Sending XPC message failed (%s) %zu attempt(s)"
+ ", CTMessageAddress=%@"
+ ", Content-Type params=%@"
+ ", Content-Type=%@"
+ ", Date=%@"
+ ", Items=%@"
+ ", Message ID=%u"
+ ", Message Type=%u"
+ ", Raw Headers=%@"
+ ", Recipients=%@"
+ ", Replace Message=%{bool}u"
+ ", Reply Enabled=%{bool}d"
+ ", Service Center=%@"
+ ", UUID=%@"
+ "13085.1"
+ "13085.1~24"
+ "CTPlanInstallRestrictionUnRegulated"
+ "CTPlanTransferCapabilityIneligibleForNow"
+ "CTPlanTransferCapabilityNotSupportedUnRegulatoryRestricted"
+ "Message ID %u UUID %{public}@"
+ "Sending XPC message failed (%s) all attempts"
- "13080.2"
- "13080.2~1"
- "<[CTMessageAddress: %@]\n\t[Recipients: %@]\n\t[Items: %@]\n\t[Raw Headers: %@]\n\t[Date: %@]\n\t[message ID: %d]\n\t[message Type: %d]\n\t[service center: %@]\n\t[Content-type: %@]\n\t[Content-type params: %@]\n\t[replace message: %d]\n [reply enabled: %d]"
- "kCTCellularUsageAllSubscriberTags"

```
