## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-774.19.0.0.0
-  __TEXT.__text: 0xc1d4
+774.23.0.0.0
+  __TEXT.__text: 0xc208
   __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0x984
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x2e0
-  __TEXT.__cstring: 0x10ea
+  __TEXT.__gcc_except_tab: 0x2ec
+  __TEXT.__cstring: 0x112d
   __TEXT.__oslogstring: 0x4b2
   __TEXT.__unwind_info: 0x2f8
   __TEXT.__objc_classname: 0x1ae

   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__cfstring: 0x1820
   __AUTH_CONST.__objc_const: 0x12a8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4277EBFF-CFB1-3645-8212-1CC4D4A0C8C1
+  UUID: 9BEDC2B7-CFE0-3C3E-9FC3-68D60C981F7A
   Functions: 219
   Symbols:   1031
-  CStrings:  906
+  CStrings:  910
 
Functions:
~ -[CARSetupOnboardingViewController initWithFeatures:doneHandler:] : 3112 -> 3164
CStrings:
+ "WELCOME_TO_CARPLAY"
+ "WELCOME_TO_CARPLAY_ULTRA"
+ "WHAT_IS_NEW_CARPLAY"
+ "WHAT_IS_NEW_CARPLAY_ULTRA"
- "WELCOME_TO"
- "WHAT_IS_NEW"

```
