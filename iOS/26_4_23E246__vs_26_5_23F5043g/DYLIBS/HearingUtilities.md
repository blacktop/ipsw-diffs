## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-496.17.0.0.0
-  __TEXT.__text: 0x9f278
+496.19.0.0.0
+  __TEXT.__text: 0x9f36c
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x7bec
+  __TEXT.__objc_methlist: 0x7c04
   __TEXT.__const: 0x402
   __TEXT.__gcc_except_tab: 0x2618
   __TEXT.__cstring: 0x4cda
-  __TEXT.__oslogstring: 0x9495
+  __TEXT.__oslogstring: 0x9582
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift5_reflstr: 0xb
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x29e0
+  __TEXT.__unwind_info: 0x29e8
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x883
-  __TEXT.__objc_methname: 0x14154
+  __TEXT.__objc_methname: 0x141a4
   __TEXT.__objc_methtype: 0x2275
-  __TEXT.__objc_stubs: 0xeb80
+  __TEXT.__objc_stubs: 0xeba0
   __DATA_CONST.__got: 0x620
   __DATA_CONST.__const: 0x33a0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4928
+  __DATA_CONST.__objc_selrefs: 0x4938
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x3d0
   __AUTH_CONST.__auth_got: 0x878

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0952C2BA-9273-3231-ACDA-1623B58F59CB
-  Functions: 3549
-  Symbols:   11474
-  CStrings:  5926
+  UUID: A41BCCDF-2F66-3E22-BBE5-D00F61A8C69C
+  Functions: 3551
+  Symbols:   11479
+  CStrings:  5930
 
Symbols:
+ -[HUAccessoryHearingSettings activeHearingProtectionIsAvailableForAddress:]
+ -[HUAccessoryHearingSettings activeHearingProtectionIsEnabledForAddress:]
+ _objc_msgSend$activeHearingProtectionIsAvailableForAddress:
+ _objc_msgSend$activeHearingProtectionIsEnabledForAddress:
- _objc_msgSend$activeHearingProtectionEnabledForAddress:
Functions:
~ ___63-[HUAccessoryManager getPairedDeviceSupportsHearingProtection:]_block_invoke : 380 -> 384
+ -[HUAccessoryHearingSettings activeHearingProtectionEnabledForAddress:]
+ -[HUAccessoryHearingSettings activeHearingProtectionAvailableForAddress:]
~ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke : 980 -> 1052
~ ___54-[HUAccessoryHearingSyncManager sendUpdateToAccessory]_block_invoke_2 : 440 -> 544
CStrings:
+ "AccessoryHearingSyncManager Adding entries to active hearing protection enabled dictionary from device %@: %@"
+ "AccessoryHearingSyncManager: skipping update to Active Hearing Protection because we do not have a stored value for address %@"
+ "activeHearingProtectionIsAvailableForAddress:"
+ "activeHearingProtectionIsEnabledForAddress:"

```
