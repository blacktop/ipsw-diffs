## AccessoryFirmwareUpdate

> `/System/Library/PrivateFrameworks/AccessoryFirmwareUpdate.framework/AccessoryFirmwareUpdate`

```diff

-17.0.0.0.0
-  __TEXT.__text: 0x1a2a4
+19.0.0.0.0
+  __TEXT.__text: 0x1a328
   __TEXT.__auth_stubs: 0x9e0
   __TEXT.__objc_methlist: 0x1d4
   __TEXT.__const: 0xc60

   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x38
   __TEXT.__cstring: 0xd7d
-  __TEXT.__oslogstring: 0x1313
+  __TEXT.__oslogstring: 0x13a3
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_capture: 0x368
   __TEXT.__unwind_info: 0x418

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 564F11AE-2A88-375B-98E7-6E8FD89C87D7
+  UUID: 48A12BB4-36F4-3FFA-AF0C-BE1F68D0CF3A
   Functions: 477
   Symbols:   378
-  CStrings:  207
+  CStrings:  208
 
Functions:
~ sub_2506c30e0 -> sub_22af9d0e0 : 1000 -> 1132
CStrings:
+ "#AccessoryInteraction: %s - firmware version has not been updated, still informing Find My in case the last updates was not propagated"
+ "#AccessoryInteraction: %s - firmware version has updated, informing Find My"
- "#AccessoryInteraction: %s - firmware version has not been updated"

```
