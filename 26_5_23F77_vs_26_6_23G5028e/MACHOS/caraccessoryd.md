## caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

-515.29.0.0.0
-  __TEXT.__text: 0x416c8
+515.34.1.0.0
+  __TEXT.__text: 0x41b1c
   __TEXT.__auth_stubs: 0x1440
-  __TEXT.__objc_stubs: 0x31e0
-  __TEXT.__objc_methlist: 0x1d0c
+  __TEXT.__objc_stubs: 0x3240
+  __TEXT.__objc_methlist: 0x1d24
   __TEXT.__const: 0xb80
   __TEXT.__cstring: 0xe68
   __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__objc_methname: 0x4b75
-  __TEXT.__oslogstring: 0x4947
+  __TEXT.__objc_methname: 0x4bb5
+  __TEXT.__oslogstring: 0x49d7
   __TEXT.__objc_classname: 0x95d
-  __TEXT.__objc_methtype: 0x18eb
+  __TEXT.__objc_methtype: 0x18fb
   __TEXT.__swift5_typeref: 0x910
   __TEXT.__swift5_capture: 0x4a8
   __TEXT.__constg_swiftt: 0x948

   __TEXT.__swift5_types: 0x54
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0xcd8
+  __TEXT.__unwind_info: 0xcf0
   __TEXT.__eh_frame: 0x2e8
   __DATA_CONST.__auth_got: 0xa30
   __DATA_CONST.__got: 0x550

   __DATA_CONST.__objc_protorefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x5778
-  __DATA.__objc_selrefs: 0x1210
+  __DATA.__objc_const: 0x5780
+  __DATA.__objc_selrefs: 0x1228
   __DATA.__objc_ivar: 0xc8
   __DATA.__objc_data: 0x13d8
   __DATA.__data: 0x1a10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 94621F19-4955-334E-A403-480A34F838BD
-  Functions: 1296
-  Symbols:   3637
-  CStrings:  1426
+  UUID: A2E6B11E-4933-3699-8607-038D5518A4A5
+  Functions: 1301
+  Symbols:   3646
+  CStrings:  1433
 
Symbols:
+ -[_CAFdConnectionProxy didUpdateAttributes:]
+ -[_CAFdConnectionProxy rerequestRegistrations].cold.1
+ GCC_except_table100
+ GCC_except_table108
+ GCC_except_table40
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table93
+ _CAFDefaultsGetDouble
+ __46-[_CAFdConnectionProxy rerequestRegistrations]_block_invoke.150
+ __46-[_CAFdConnectionProxy rerequestRegistrations]_block_invoke.150.cold.1
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.284
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.284.cold.1
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.284.cold.2
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.284.cold.3
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.284.cold.4
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.284.cold.5
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.284.cold.6
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.284.cold.7
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.287
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.287.cold.1
+ __49-[_CAFdConnectionProxy didUpdatePluginID:values:]_block_invoke.146
+ __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.296
+ ___44-[_CAFdConnectionProxy didUpdateAttributes:]_block_invoke
+ _objc_msgSend$attributes
+ _objc_msgSend$didUpdateAttributes:
+ _objc_msgSend$updateCapabilitiesIfNeeded
- GCC_except_table106
- GCC_except_table38
- GCC_except_table62
- GCC_except_table63
- GCC_except_table91
- GCC_except_table98
- __46-[_CAFdConnectionProxy rerequestRegistrations]_block_invoke.148
- __46-[_CAFdConnectionProxy rerequestRegistrations]_block_invoke.148.cold.1
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.282
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.282.cold.1
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.282.cold.2
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.282.cold.3
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.282.cold.4
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.282.cold.5
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.283
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.285.cold.1
- __49-[_CAFdConnectionProxy didUpdatePluginID:values:]_block_invoke.144
- __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.294
CStrings:
+ "%{public}@: rerequestRegistrations"
+ "Configuration complete pre-channel did open UUID: %{public}@"
+ "Process pending registrations for %lu connections"
+ "attributes"
+ "current car is not configured %lu of %lu"
+ "didUpdateAttributes:"
+ "updateCapabilitiesIfNeeded"
+ "v24@0:8@\"CAFCarAttributes\"16"
- "Process pending registrations"

```
