## TactSwitchHIDSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/TactSwitchHIDSessionFilter.plugin/TactSwitchHIDSessionFilter`

```diff

-9150.2.0.0.0
-  __TEXT.__text: 0x75c
-  __TEXT.__auth_stubs: 0x1c0
+9170.34.1.0.0
+  __TEXT.__text: 0x71c
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xb8
+  __TEXT.__cstring: 0xba
   __TEXT.__objc_methname: 0x310
   __TEXT.__oslogstring: 0xc0
-  __TEXT.__objc_classname: 0x37
+  __TEXT.__objc_classname: 0x35
   __TEXT.__objc_methtype: 0x237
   __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x18
   __DATA.__objc_const: 0x280
   __DATA.__objc_selrefs: 0x160
   __DATA.__objc_ivar: 0x8

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9DCC9FD3-1AA4-3647-8DB1-F079E2D160D8
+  UUID: 6020004E-05A2-3E69-A451-6A828FD8E3C3
   Functions: 13
-  Symbols:   94
+  Symbols:   95
   CStrings:  106
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x22
Functions:
~ -[TactSwitchHIDSessionFilter serviceNotification:added:] -> -[TactSwitchHIDSessionFilter filterEvent:forService:] : 856 -> 448
~ -[TactSwitchHIDSessionFilter filterEvent:forService:] -> -[TactSwitchHIDSessionFilter setProperty:forKey:] : 444 -> 8
~ -[TactSwitchHIDSessionFilter setProperty:forKey:] -> -[TactSwitchHIDSessionFilter propertyForKey:] : 8 -> 52
~ -[TactSwitchHIDSessionFilter propertyForKey:] -> -[TactSwitchHIDSessionFilter serviceNotification:added:] : 52 -> 852
~ _MTLoggingTactSwitchHIDSessionFilter : 84 -> 68
~ -[TactSwitchHIDSessionFilter initWithSession:] : 132 -> 128
~ -[TactSwitchHIDSessionFilter serviceNotification:added:].cold.1 : 120 -> 76

```
