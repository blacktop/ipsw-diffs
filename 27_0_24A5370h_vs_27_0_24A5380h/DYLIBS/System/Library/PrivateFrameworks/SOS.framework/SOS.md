## SOS

> `/System/Library/PrivateFrameworks/SOS.framework/SOS`

```diff

-  __TEXT.__text: 0x355fc
-  __TEXT.__objc_methlist: 0x394c
+  __TEXT.__text: 0x3609c
+  __TEXT.__objc_methlist: 0x39d4
   __TEXT.__const: 0x256
-  __TEXT.__cstring: 0x4b02
-  __TEXT.__oslogstring: 0x63b8
+  __TEXT.__cstring: 0x4bb8
+  __TEXT.__oslogstring: 0x6670
   __TEXT.__gcc_except_tab: 0x85c
   __TEXT.__dlopen_cstrs: 0x3e9
   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xff8
+  __TEXT.__unwind_info: 0x1008
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1150
+  __DATA_CONST.__const: 0x1178
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2778
+  __DATA_CONST.__objc_selrefs: 0x27e0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__got: 0x380
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x4180
-  __AUTH_CONST.__objc_const: 0x4d58
+  __AUTH_CONST.__cfstring: 0x4240
+  __AUTH_CONST.__objc_const: 0x4db8
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x640
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x2fc
+  __DATA.__objc_ivar: 0x304
   __DATA.__data: 0x9f0
   __DATA.__bss: 0x268
   __DATA_DIRTY.__objc_data: 0x500

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1455
-  Symbols:   5143
-  CStrings:  1681
+  Functions: 1468
+  Symbols:   5188
+  CStrings:  1704
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[SOSContactsManager isMessagesHandlingSMS]
+ -[SOSCoordinator _sendUrgentMessageToPairedDevice:retries:identifier:]
+ -[SOSCoordinator handleSOSMessageTypeMessagesHandlingSMS:]
+ -[SOSCoordinator handleSOSMessageTypeMessagesHandlingSMSReq:]
+ -[SOSCoordinator messagesHandlingSMSRequestTimers]
+ -[SOSCoordinator pendingMessagesHandlingSMSRequests]
+ -[SOSCoordinator requestMessagesHandlingSMSFromCompanionWithCompletion:]
+ -[SOSCoordinator sendUrgentMessageToPairedDevice:identifier:]
+ -[SOSCoordinator setMessagesHandlingSMSRequestTimers:]
+ -[SOSCoordinator setPendingMessagesHandlingSMSRequests:]
+ -[SOSCoordinator startMessagesHandlingSMSRequestTimerWithIdentifier:]
+ -[SOSEngine refreshMessagesHandlingSMS]
+ GCC_except_table105
+ GCC_except_table35
+ GCC_except_table41
+ GCC_except_table50
+ GCC_except_table90
+ GCC_except_table96
+ _OBJC_CLASS_$_NSError
+ _OBJC_IVAR_$_SOSCoordinator._messagesHandlingSMSRequestTimers
+ _OBJC_IVAR_$_SOSCoordinator._pendingMessagesHandlingSMSRequests
+ ___58-[SOSCoordinator handleSOSMessageTypeMessagesHandlingSMS:]_block_invoke
+ ___69-[SOSCoordinator startMessagesHandlingSMSRequestTimerWithIdentifier:]_block_invoke
+ ___70-[SOSCoordinator _sendUrgentMessageToPairedDevice:retries:identifier:]_block_invoke
+ ___block_descriptor_41_e8_32s_e42_v32?0"NSString"8?<v?B"NSError">16^B24ls32l8
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _objc_msgSend$_sendUrgentMessageToPairedDevice:retries:identifier:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$handleSOSMessageTypeMessagesHandlingSMS:
+ _objc_msgSend$handleSOSMessageTypeMessagesHandlingSMSReq:
+ _objc_msgSend$messagesHandlingSMSRequestTimers
+ _objc_msgSend$pendingMessagesHandlingSMSRequests
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$sendUrgentMessageToPairedDevice:identifier:
+ _objc_msgSend$startMessagesHandlingSMSRequestTimerWithIdentifier:
- -[SOSCoordinator _sendUrgentMessageToPairedDevice:retries:]
- GCC_except_table102
- GCC_except_table34
- GCC_except_table89
- GCC_except_table95
- ___59-[SOSCoordinator _sendUrgentMessageToPairedDevice:retries:]_block_invoke
- _objc_msgSend$_sendUrgentMessageToPairedDevice:retries:
CStrings:
+ "NO"
+ "SOSContactsManager, refreshIsMessagesHandlingSMS no-op"
+ "SOSCoordinationMessagesHandlingSMS"
+ "SOSCoordinator, IDS didSendWithSuccess identifier=%@ Success!"
+ "SOSCoordinator, IDS didSendWithSuccess identifier=%@ error=%@"
+ "SOSCoordinator, cancelling timeout timer for messagesHandlingSMS"
+ "SOSCoordinator, handleSOSMessageTypeMessagesHandlingSMS"
+ "SOSCoordinator, handleSOSMessageTypeMessagesHandlingSMSReq"
+ "SOSCoordinator, messagesHandlingSMS: %@, clearing out pending messages handling SMS requests, count: %lu"
+ "SOSCoordinator, no paired device nearby, not asking companion for messages handling SMS"
+ "SOSCoordinator, requestMessagesHandlingSMSFromCompanionWithCompletion"
+ "SOSCoordinator, sendUrgentMessageToPairedDevice"
+ "SOSCoordinator, waiting for response from phone for messages handling SMS"
+ "SOSCoordinatorErrorDomain"
+ "SOSMessageTypeMessagesHandlingSMS"
+ "SOSMessageTypeMessagesHandlingSMSReq"
+ "Timed out waiting for reply to message (%@)"
+ "YES"
+ "v32@?0@\"NSString\"8@?<v@?B@\"NSError\">16^B24"
- "IDS didSendWithSuccess identifier=%@ Success!"
- "IDS didSendWithSuccess identifier=%@ error=%@"

```
