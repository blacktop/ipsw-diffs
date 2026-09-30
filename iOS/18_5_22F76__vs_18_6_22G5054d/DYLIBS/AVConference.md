## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2115.6.1.0.0
-  __TEXT.__text: 0x6cc0b8
+2125.1.0.0.0
+  __TEXT.__text: 0x6cc0dc
   __TEXT.__auth_stubs: 0x5050
   __TEXT.__objc_methlist: 0x312a8
   __TEXT.__const: 0x7a80
   __TEXT.__cstring: 0x80c55
-  __TEXT.__oslogstring: 0xee836
+  __TEXT.__oslogstring: 0xee83e
   __TEXT.__gcc_except_tab: 0x26d8
   __TEXT.__ustring: 0x144
   __TEXT.__unwind_info: 0xef00
   __TEXT.__objc_classname: 0x47d1
   __TEXT.__objc_methname: 0x72e48
   __TEXT.__objc_methtype: 0x2490a
-  __TEXT.__objc_stubs: 0x485c0
+  __TEXT.__objc_stubs: 0x48600
   __DATA_CONST.__got: 0x18e0
   __DATA_CONST.__const: 0x61c0
   __DATA_CONST.__objc_classlist: 0x1180

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2606158C-8195-3320-B5A2-6B0AE55C10ED
+  UUID: 3336DDE7-2B36-3AEA-BAA4-AB666BDB5A5A
   Functions: 28560
-  Symbols:   88907
+  Symbols:   88909
   CStrings:  52038
 
Symbols:
+ _objc_msgSend$setupLocalABTestSwitches
+ _objc_msgSend$setupLocalOnOffSwitches
Functions:
~ -[VCSwitchManager initializeLocalSwitches] : 472 -> 508
CStrings:
+ " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
- " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"

```
