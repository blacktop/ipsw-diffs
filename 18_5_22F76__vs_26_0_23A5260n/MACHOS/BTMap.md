## BTMap

> `/usr/sbin/BTMap`

```diff

-345.1.0.0.0
-  __TEXT.__text: 0x3b68
+350.33.1.1.0
+  __TEXT.__text: 0x3b70
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_stubs: 0xd20
   __TEXT.__objc_methlist: 0x494

   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F33FA688-66E8-3618-9CC1-902382BA3E56
+  UUID: CD4C8054-43E0-3C7E-90D9-66F9C14C0CA1
   Functions: 103
   Symbols:   141
   CStrings:  330
Symbols:
+ _IMSPIQueryMessageWithGUIDAndQOS
+ _IMSPIQueryMessagesWithQOS
- _IMSPIQueryMessageWithGUID
- _IMSPIQueryMessages
Functions:
~ sub_100002eb4 : 264 -> 268
~ sub_100003470 -> sub_100003474 : 156 -> 160
CStrings:
+ "body"
- "text"

```
