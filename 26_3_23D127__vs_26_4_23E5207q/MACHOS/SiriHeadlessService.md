## SiriHeadlessService

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService`

```diff

-3500.16.1.0.0
-  __TEXT.__text: 0x1e0
+3520.28.1.0.0
+  __TEXT.__text: 0x1e4
   __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x1c
+  __TEXT.__cstring: 0x1a
   __TEXT.__oslogstring: 0x81
   __TEXT.__objc_methname: 0x34
   __TEXT.__unwind_info: 0x68

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration
+  - /System/Library/PrivateFrameworks/SiriDeviceSelection.framework/SiriDeviceSelection
   - /System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 384B4387-6DEA-34A4-A334-92D5F8E1BA32
+  UUID: 148BA098-33AC-3E9D-B7F0-AB4E6907FE78
   Functions: 3
   Symbols:   21
   CStrings:  9
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
Functions:
~ sub_1000009a0 -> sub_100000a10 : 344 -> 348
CStrings:
+ "19"
+ "SiriVOX-3520.28.1"
- "4190"
- "SiriVOX-3500.16.1"

```
