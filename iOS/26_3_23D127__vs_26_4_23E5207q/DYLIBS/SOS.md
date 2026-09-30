## SOS

> `/System/Library/PrivateFrameworks/SOS.framework/SOS`

```diff

-656.300.1.0.0
-  __TEXT.__text: 0x3738c
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x38cc
+656.500.61.0.0
+  __TEXT.__text: 0x396c8
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_methlist: 0x38fc
   __TEXT.__const: 0x266
-  __TEXT.__cstring: 0x4a22
-  __TEXT.__oslogstring: 0x62e9
-  __TEXT.__gcc_except_tab: 0x918
+  __TEXT.__cstring: 0x4a44
+  __TEXT.__oslogstring: 0x6374
+  __TEXT.__gcc_except_tab: 0x980
   __TEXT.__dlopen_cstrs: 0x39f
   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xfa8
-  __TEXT.__objc_classname: 0x586
-  __TEXT.__objc_methname: 0xab06
-  __TEXT.__objc_methtype: 0x1b7a
-  __TEXT.__objc_stubs: 0x7660
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x1100
-  __DATA_CONST.__objc_classlist: 0x118
+  __TEXT.__unwind_info: 0x1110
+  __TEXT.__objc_classname: 0x5f2
+  __TEXT.__objc_methname: 0xabd3
+  __TEXT.__objc_methtype: 0x1bc5
+  __TEXT.__objc_stubs: 0x7700
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__const: 0x1128
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2720
+  __DATA_CONST.__objc_selrefs: 0x2748
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x458
+  __AUTH_CONST.__auth_got: 0x438
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x40e0
-  __AUTH_CONST.__objc_const: 0x4b90
+  __AUTH_CONST.__cfstring: 0x4100
+  __AUTH_CONST.__objc_const: 0x4c68
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x5f0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x2f0
+  __DATA.__objc_ivar: 0x2f8
   __DATA.__data: 0x9f0
   __DATA.__bss: 0x250
-  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/FriendKit.framework/FriendKit
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: CEAA6768-D2B7-3512-8398-BEE7A8D0FEFA
-  Functions: 1432
-  Symbols:   5047
-  CStrings:  3551
+  UUID: F20C1432-174A-3563-BD14-5EEC720D4B89
+  Functions: 1449
+  Symbols:   5133
+  CStrings:  3566
 
Symbols:
+ -[SOSMessagesConnectionManager .cxx_destruct]
+ -[SOSMessagesConnectionManager connectToMessageDaemonWithCompletion:]
+ -[SOSMessagesConnectionManager disconnectFromMessagesDaemon]
+ GCC_except_table44
+ GCC_except_table89
+ GCC_except_table95
+ _IMSPIResetChatRegistry
+ _OBJC_CLASS_$_IMDaemonController
+ _OBJC_CLASS_$_SOSMessagesConnectionManager
+ _OBJC_IVAR_$_SOSEngine._messagesConnectionManager
+ _OBJC_IVAR_$_SOSMessagesConnectionManager._daemonConnection
+ _OBJC_METACLASS_$_SOSMessagesConnectionManager
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_INSTANCE_METHODS_SOSMessagesConnectionManager
+ __OBJC_$_INSTANCE_VARIABLES_SOSMessagesConnectionManager
+ __OBJC_CLASS_RO_$_SOSMessagesConnectionManager
+ __OBJC_METACLASS_RO_$_SOSMessagesConnectionManager
+ ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.379
+ ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.535
+ ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.405
+ ___60-[SOSMessagesConnectionManager disconnectFromMessagesDaemon]_block_invoke
+ ___66-[SOSEngine sosPersistentTimerLocationManagerTimerFired:location:]_block_invoke
+ ___69-[SOSMessagesConnectionManager connectToMessageDaemonWithCompletion:]_block_invoke
+ ___69-[SOSMessagesConnectionManager connectToMessageDaemonWithCompletion:]_block_invoke_2
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.398
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.398.cold.1
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.370
+ ___block_literal_global.372
+ ___block_literal_global.374
+ ___block_literal_global.378
+ ___block_literal_global.382
+ ___block_literal_global.384
+ ___block_literal_global.387
+ ___block_literal_global.395
+ ___block_literal_global.404
+ ___block_literal_global.496
+ ___block_literal_global.498
+ ___block_literal_global.520
+ _objc_autorelease
+ _objc_msgSend$connectToMessageDaemonWithCompletion:
+ _objc_msgSend$connectWithCompletion:
+ _objc_msgSend$disconnectFromMessagesDaemon
+ _objc_msgSend$multiplexedConnectionWithLabel:capabilities:context:
+ _objc_msgSend$sharedController
- GCC_except_table101
- GCC_except_table88
- GCC_except_table94
- ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.378
- ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.534
- ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.404
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.397
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.397.cold.1
- ___block_literal_global.369
- ___block_literal_global.371
- ___block_literal_global.373
- ___block_literal_global.377
- ___block_literal_global.381
- ___block_literal_global.383
- ___block_literal_global.386
- ___block_literal_global.394
- ___block_literal_global.403
- ___block_literal_global.495
- ___block_literal_global.497
- ___block_literal_global.519
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "%s, Creating connection"
+ "%s, Disconnected from daemon"
+ "%s, Resetting registry"
+ "%s, _daemonConnection is already created"
+ "%s, _daemonConnection is already nil"
+ "-[SOSMessagesConnectionManager connectToMessageDaemonWithCompletion:]"
+ "-[SOSMessagesConnectionManager disconnectFromMessagesDaemon]_block_invoke"
+ "@\"<IMDaemonMultiplexedConnectionManaging>\""
+ "@\"SOSMessagesConnectionManager\""
+ "SOSEmergencyContactNotifications"
+ "SOSMessagesConnectionManager"
+ "_daemonConnection"
+ "_messagesConnectionManager"
+ "connectToMessageDaemonWithCompletion:"
+ "connectWithCompletion:"
+ "disconnectFromMessagesDaemon"
+ "multiplexedConnectionWithLabel:capabilities:context:"
+ "sharedController"
+ "\xd1"
- "%s - FF is off"
- "MessagingAPI"
- "\xc1"

```
