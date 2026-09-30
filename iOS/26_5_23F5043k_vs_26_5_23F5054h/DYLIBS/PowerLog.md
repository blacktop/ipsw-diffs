## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`

```diff

-3031.120.21.0.0
-  __TEXT.__text: 0x205e4
+3031.120.25.0.0
+  __TEXT.__text: 0x20490
   __TEXT.__auth_stubs: 0x910
   __TEXT.__objc_methlist: 0x1474
   __TEXT.__const: 0xef0
-  __TEXT.__gcc_except_tab: 0x8e8
+  __TEXT.__gcc_except_tab: 0x8d4
   __TEXT.__cstring: 0x22b1
-  __TEXT.__oslogstring: 0x39c7
+  __TEXT.__oslogstring: 0x395f
   __TEXT.__unwind_info: 0x800
   __TEXT.__objc_classname: 0x22e
   __TEXT.__objc_methname: 0x3f69

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 50032074-7BAF-306C-84CA-347373C8B2E9
+  UUID: 28D02E12-A27F-3BA9-9C56-ED96517FEEBF
   Functions: 813
   Symbols:   2670
-  CStrings:  1842
+  CStrings:  1841
 
Symbols:
+ -[PLClientLogger xpcSendMessage:withClientID:withKey:withPayload:].cold.3
+ GCC_except_table157
- GCC_except_table156
- _PLShouldLogRegisteredEvent.cold.2
CStrings:
+ "Caching %d withKey:%@ withPayload:%@ ..."
+ "Log %@ withContent %@ cannot continue due to nils!"
+ "PLShouldLogRegisteredEvent: %d, ClientID: %d"
+ "Sending xpc message for client id: %d withKey:%@ withPayload:%@ dispatching..."
+ "Unknown Permission %d - for client id:%d withKey:%@ withPayload:%@"
+ "permissionForClientID: %hd withKey:%@ withType:%@ returnValue=%hd"
- "PLShouldLogRegisteredEvent: NO"
- "PLShouldLogRegisteredEvent: YES"
- "logForClientID: %d withKey:%@ withPayload:%@ caching..."
- "logForClientID: Unknown Permission %d - for client id:%d withKey:%@ withPayload:%@"
- "logForClientID: log %@ withContent %@ cannot continue due to nils!"
- "logForClientID: sending xpc message for client id: %d withKey:%@ withPayload:%@ dispatching..."
- "permissionForClientID: permissionForClientId: %hd withKey:%@ withType:%@ returnValue=%hd"

```
