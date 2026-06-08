## IMDMessageServices

> `/System/Library/PrivateFrameworks/IMDMessageServices.framework/IMDMessageServices`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0x1d64
-  __TEXT.__auth_stubs: 0x1a0
+1481.100.29.2.9
+  __TEXT.__text: 0x1b44
   __TEXT.__objc_methlist: 0xec
-  __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x378
-  __TEXT.__cstring: 0x2bf
-  __TEXT.__oslogstring: 0x540
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0x31c
+  __TEXT.__cstring: 0x2f7
+  __TEXT.__oslogstring: 0x56c
   __TEXT.__unwind_info: 0x160
-  __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x28f
-  __TEXT.__objc_methtype: 0x66
-  __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x38
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0xb8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 884647D1-0FBE-32FE-865A-D9EC13C732E1
+  UUID: 6423FC0E-682D-39EB-811E-672A1D123553
   Functions: 25
   Symbols:   54
-  CStrings:  93
+  CStrings:  67
 
Symbols:
+ _IMDMessageServicesRoutingShouldRetrySendKey
+ _IMDMessageServicesWatchdogActionKey
+ _xpc_dictionary_set_bool
- _IMDMessageServicesWatchdogShouldFailSendKey
- ___stack_chk_fail
- ___stack_chk_guard
CStrings:
+ "MessageServices received request for watchdog (networkAvailable=%d)"
+ "MessageServices received request for watchdog for guid: %@ (networkAvailable=%d)"
+ "__kIMDMessageServicesRoutingShouldRetrySendKey"
+ "__kIMDMessageServicesWatchdogActionKey"
+ "networkAvailable"
- "@\"NSObject<OS_xpc_object>\""
- "@16@0:8"
- "B16@0:8"
- "IMDMessageServicesCenter"
- "MessageServices received request for watchdog"
- "MessageServices received request for watchdog for guid: %@"
- "UTF8String"
- "__kIMDMessageServicesWatchdogShouldFailSendKey"
- "_connect"
- "_connection"
- "_disconnect"
- "_disconnected"
- "_requestExpireStateWithGUID:handler:"
- "_requestRoutingWithGUID:chatGUID:downgradableServices:error:handler:"
- "_requestScheduleMessagesWithGUID:handler:"
- "_requestWatchdogWithGUID:handler:"
- "count"
- "dealloc"
- "init"
- "requestExpireStateForMessageGuid:completionBlock:"
- "requestExpireStateWithCompletion:"
- "requestRoutingForMessageGuid:inChat:downgradableServices:error:completionBlock:"
- "requestRoutingWithDowngradableServices:completion:"
- "requestScheduledMessageForGuid:completionBlock:"
- "requestScheduledMessagesWithCompletion:"
- "requestWatchdogForMessageGuid:completionBlock:"
- "requestWatchdogWithCompletion:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@?16"
- "v32@0:8@16@?24"
- "v52@0:8@16@24@32I40@?44"

```
