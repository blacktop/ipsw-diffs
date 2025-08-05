## SOS

> `/System/Library/PrivateFrameworks/SOS.framework/SOS`

```diff

-655.100.3.0.0
-  __TEXT.__text: 0x373c0
+656.100.5.0.0
+  __TEXT.__text: 0x37448
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_methlist: 0x38a4
   __TEXT.__const: 0x266
   __TEXT.__cstring: 0x4ac2
-  __TEXT.__oslogstring: 0x6288
-  __TEXT.__gcc_except_tab: 0x90c
+  __TEXT.__oslogstring: 0x62e9
+  __TEXT.__gcc_except_tab: 0x918
   __TEXT.__dlopen_cstrs: 0x39f
   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_fieldmd: 0x20

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: DDC76E2F-6275-3086-973A-F28CB4ADD605
+  UUID: 8859EC9B-4817-30ED-AFB0-576E4694B3DE
   Functions: 1432
   Symbols:   5046
-  CStrings:  3552
+  CStrings:  3553
 
Symbols:
+ ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.375
+ ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.531
+ ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.401
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.394
+ ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.394.cold.1
+ ___block_literal_global.374
+ ___block_literal_global.380
+ ___block_literal_global.383
+ ___block_literal_global.391
+ ___block_literal_global.400
+ ___block_literal_global.494
+ ___block_literal_global.516
- ___38-[SOSEngine dismissSOSWithCompletion:]_block_invoke.373
- ___48-[SOSEngine listener:shouldAcceptNewConnection:]_block_invoke.529
- ___52+[SOSEngine shiftedLocationWithLocation:completion:]_block_invoke.399
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.392
- ___87+[SOSEngine _sendMessageToRecipients:withLocation:isFirstMessage:medicalIDName:Reason:]_block_invoke.392.cold.1
- ___block_literal_global.372
- ___block_literal_global.376
- ___block_literal_global.381
- ___block_literal_global.389
- ___block_literal_global.398
- ___block_literal_global.490
- ___block_literal_global.514
Functions:
~ -[SOSEngine updateCurrentSOSInteractiveState:] : 480 -> 624
~ -[SOSEngine listener:shouldAcceptNewConnection:] : 452 -> 444
CStrings:
+ "Could not send client a current interactive state due to client protocol error for connection %@"

```
