## AddDevicesToAutomatedDeviceEnrollmentExtension

> `/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-42.0.0.0.0
-  __TEXT.__text: 0x90e34
+42.60.2.0.0
+  __TEXT.__text: 0x90ffc
   __TEXT.__auth_stubs: 0x25e0
   __TEXT.__objc_stubs: 0x1100
   __TEXT.__objc_methlist: 0x55c

   __TEXT.__objc_methname: 0x24a5
   __TEXT.__objc_methtype: 0x873
   __TEXT.__oslogstring: 0x21a0
-  __TEXT.__cstring: 0x4175
+  __TEXT.__cstring: 0x4275
   __TEXT.__swift5_capture: 0xb24
   __TEXT.__swift_as_entry: 0x178
   __TEXT.__swift_as_ret: 0x184

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3054
   Symbols:   284
-  CStrings:  962
+  CStrings:  964
 
Functions:
~ sub_10000b6ac : 112 -> 124
~ sub_10000b974 -> sub_10000b980 : 272 -> 308
~ sub_10000ba84 -> sub_10000bab4 : 432 -> 476
~ sub_10000bc34 -> sub_10000bc90 : 256 -> 280
~ sub_100016544 -> sub_1000165b8 : 2876 -> 2884
~ sub_100017bf4 -> sub_100017c70 : 1804 -> 1824
~ sub_100039c50 -> sub_100039ce0 : 1340 -> 1376
~ sub_10003a9e8 -> sub_10003aa9c : 436 -> 480
~ sub_10003ab9c -> sub_10003ac7c : 260 -> 284
~ sub_100075a84 -> sub_100075b7c : 260 -> 404
~ sub_10007ec04 -> sub_10007ed8c : 508 -> 520
~ sub_1000820b4 -> sub_100082248 : 1248 -> 1300
CStrings:
+ "Message for the alert shown when the device cannot be enrolled because no WLAN or network configuration is available to share."
+ "There is no WLAN or network configuration to share with the device. Please check your network selection and try again."
```
