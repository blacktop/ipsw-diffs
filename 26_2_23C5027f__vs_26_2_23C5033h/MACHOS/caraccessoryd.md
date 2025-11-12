## caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

-488.25.0.0.0
-  __TEXT.__text: 0x3bd30
+488.28.0.0.0
+  __TEXT.__text: 0x3c578
   __TEXT.__auth_stubs: 0x1450
-  __TEXT.__objc_stubs: 0x2140
-  __TEXT.__objc_methlist: 0x1bf4
+  __TEXT.__objc_stubs: 0x2200
+  __TEXT.__objc_methlist: 0x1c34
   __TEXT.__const: 0xb60
-  __TEXT.__cstring: 0x1736
+  __TEXT.__cstring: 0x1738
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__objc_methname: 0x426d
-  __TEXT.__oslogstring: 0x45d7
-  __TEXT.__objc_classname: 0x482
-  __TEXT.__objc_methtype: 0x13e5
+  __TEXT.__objc_methname: 0x431b
+  __TEXT.__oslogstring: 0x4687
+  __TEXT.__objc_classname: 0x483
+  __TEXT.__objc_methtype: 0x1425
   __TEXT.__swift5_typeref: 0x93a
   __TEXT.__swift5_capture: 0x4b8
   __TEXT.__constg_swiftt: 0x8e4

   __TEXT.__swift5_types: 0x50
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__unwind_info: 0xbf0
   __TEXT.__eh_frame: 0x358
   __DATA_CONST.__auth_got: 0xa38
   __DATA_CONST.__got: 0x568
   __DATA_CONST.__auth_ptr: 0x260
-  __DATA_CONST.__const: 0x1ba0
+  __DATA_CONST.__const: 0x1bf0
   __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x4fa0
-  __DATA.__objc_selrefs: 0x1170
-  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_const: 0x5018
+  __DATA.__objc_selrefs: 0x11a0
+  __DATA.__objc_ivar: 0xc4
   __DATA.__objc_data: 0x12f0
   __DATA.__data: 0x1990
   __DATA.__bss: 0x900

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5D2CCCD2-3230-3BD0-8811-9F2D970B2212
-  Functions: 1242
-  Symbols:   3425
-  CStrings:  1400
+  UUID: A52AEEAA-8020-3229-A23F-6779782F8106
+  Functions: 1251
+  Symbols:   3447
+  CStrings:  1412
 
Symbols:
+ -[CAFBatchUpdate(CAFD) writeToDataService:]
+ -[_CAFdConnectionProxy invalidatedUpdate]
+ -[_CAFdConnectionProxy setInvalidatedUpdate:]
+ -[_CAFdConnectionProxy setInvalidatedUpdate:withResponse:]
+ -[_CAFdConnectionProxy setInvalidatedUpdate:withResponse:].cold.1
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table96
+ OBJC_IVAR_$__CAFdConnectionProxy._invalidatedUpdate
+ _OBJC_CLASS_$_CAFBatchUpdate
+ _OUTLINED_FUNCTION_14
+ __43-[CAFBatchUpdate(CAFD) writeToDataService:]_block_invoke_3.cold.1
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.253
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.253.cold.1
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.253.cold.2
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.253.cold.3
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.253.cold.4
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.254
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.256
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.256.cold.1
+ __49-[_CAFdConnectionProxy initWithConnection:agent:]_block_invoke.35
+ __49-[_CAFdConnectionProxy initWithConnection:agent:]_block_invoke.35.cold.1
+ __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.266
+ __OBJC_$_CATEGORY_CAFBatchUpdate_$_CAFD
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CAFBatchUpdate_$_CAFD
+ ___43-[CAFBatchUpdate(CAFD) writeToDataService:]_block_invoke
+ ___43-[CAFBatchUpdate(CAFD) writeToDataService:]_block_invoke_2
+ ___43-[CAFBatchUpdate(CAFD) writeToDataService:]_block_invoke_3
+ ___block_descriptor_48_e8_32s40s_e39_v32?0"NSNumber"8"NSDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e21_v16?0"CAFResponse"8ls32l8s40l8s48l8
+ _objc_msgSend$instanceID
+ _objc_msgSend$invalidatedUpdate
+ _objc_msgSend$items
+ _objc_msgSend$setInvalidatedUpdate:
+ _objc_msgSend$writeToDataService:
+ _objc_msgSend$writeToPluginID:values:priority:withResponse:
- GCC_except_table50
- GCC_except_table51
- GCC_except_table78
- GCC_except_table85
- GCC_except_table93
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244.cold.1
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244.cold.2
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244.cold.3
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244.cold.4
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.245
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.247
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.247.cold.1
- __49-[_CAFdConnectionProxy initWithConnection:agent:]_block_invoke.29
- __49-[_CAFdConnectionProxy initWithConnection:agent:]_block_invoke.29.cold.1
- __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.257
CStrings:
+ "%{public}@: self.invalidatedUpdate=%{public}@ invalidatedUpdate=%{public}@"
+ "@\"CAFBatchUpdate\""
+ "BatchUpdate.%{public}@.%{public}@ write done count=%ld"
+ "Connection interrupted: %{public}@ invalidateUpdate=%{public}@"
+ "Connection invalidated: %{public}@ invalidateUpdate=%{public}@"
+ "T@\"CAFBatchUpdate\",C,N,V_invalidatedUpdate"
+ "_invalidatedUpdate"
+ "instanceID"
+ "invalidatedUpdate"
+ "items"
+ "setInvalidatedUpdate:"
+ "setInvalidatedUpdate:withResponse:"
+ "v32@0:8@\"CAFBatchUpdate\"16@?<v@?@\"NSError\">24"
+ "writeToDataService:"
- "Connection interrupted: %{public}@"
- "Connection invalidated: %{public}@"

```
