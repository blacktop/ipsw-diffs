## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

-35.11.0.0.0
-  __TEXT.__text: 0x1362c
+35.12.0.0.0
+  __TEXT.__text: 0x13644
   __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0xc6c
   __TEXT.__const: 0x86

   __TEXT.__cstring: 0x51e9
   __TEXT.__unwind_info: 0x620
   __TEXT.__objc_classname: 0x14d
-  __TEXT.__objc_methname: 0x36e2
+  __TEXT.__objc_methname: 0x36e4
   __TEXT.__objc_methtype: 0x8ef
   __TEXT.__objc_stubs: 0x3280
   __DATA_CONST.__got: 0x200

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 872B8B53-DCD0-34B2-8812-394904A87405
+  UUID: 5E0B4275-2CAD-3821-9FBF-81BE5AB3A791
   Functions: 462
   Symbols:   1713
   CStrings:  1145
Symbols:
+ _objc_msgSend$activeHearingProtectionIsEnabledForAddress:
- _objc_msgSend$activeHearingProtectionEnabledForAddress:
Functions:
~ -[HMDeviceManager _retrieveHearingProtectionSettingsForDevice:] : 300 -> 324
CStrings:
+ "activeHearingProtectionIsEnabledForAddress:"
- "activeHearingProtectionEnabledForAddress:"

```
