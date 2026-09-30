## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/Versions/A/HearingUtilities`

```diff

 496.22.0.0.0
-  __TEXT.__text: 0x771f4
+  __TEXT.__text: 0x76e0c
   __TEXT.__auth_stubs: 0x9a0
   __TEXT.__objc_methlist: 0x5c2c
   __TEXT.__const: 0x2f2
   __TEXT.__gcc_except_tab: 0x1b48
-  __TEXT.__oslogstring: 0x71db
+  __TEXT.__oslogstring: 0x7146
   __TEXT.__cstring: 0x37f1
   __TEXT.__dlopen_cstrs: 0x2e6
   __TEXT.__unwind_info: 0x1e70
   __TEXT.__objc_classname: 0x5e9
   __TEXT.__objc_methname: 0xe692
   __TEXT.__objc_methtype: 0x1b35
-  __TEXT.__objc_stubs: 0xab40
+  __TEXT.__objc_stubs: 0xab20
   __DATA_CONST.__got: 0x408
   __DATA_CONST.__const: 0x8e8
   __DATA_CONST.__objc_classlist: 0x140

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2592
-  Symbols:   5425
-  CStrings:  3877
+  Symbols:   5424
+  CStrings:  3874
 
Symbols:
- _objc_msgSend$setIsSCIDSService:
Functions:
~ -[HUNearbyController nearbyDeviceWithSCIDSDevice:justCreated:] : 1008 -> 16
~ +[HUAccessoryCompatibilityUtilities deviceIsAirPodsWithAXSettings:] : 64 -> 60
~ +[HUAccessoryCompatibilityUtilities deviceIsAirpodsSupportingHeadphoneAccommodations:] : 132 -> 128
CStrings:
- "SC IDS Service already has nearby device %@ with IDS device %@"
- "SC IDS Service created nearby device %@ with IDS device %@"
- "SC IDS Service devices: %@"
```
