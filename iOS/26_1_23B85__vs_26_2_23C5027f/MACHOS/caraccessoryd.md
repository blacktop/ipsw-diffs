## caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

-488.18.3.2.0
-  __TEXT.__text: 0x3b4f4
+488.25.0.0.0
+  __TEXT.__text: 0x3bd30
   __TEXT.__auth_stubs: 0x1450
-  __TEXT.__objc_stubs: 0x2040
-  __TEXT.__objc_methlist: 0x1bd4
+  __TEXT.__objc_stubs: 0x2140
+  __TEXT.__objc_methlist: 0x1bf4
   __TEXT.__const: 0xb60
-  __TEXT.__cstring: 0x16b6
-  __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__objc_methname: 0x4144
-  __TEXT.__oslogstring: 0x4557
+  __TEXT.__cstring: 0x1736
+  __TEXT.__gcc_except_tab: 0x1d4
+  __TEXT.__objc_methname: 0x426d
+  __TEXT.__oslogstring: 0x45d7
   __TEXT.__objc_classname: 0x482
-  __TEXT.__objc_methtype: 0x13d5
+  __TEXT.__objc_methtype: 0x13e5
   __TEXT.__swift5_typeref: 0x93a
   __TEXT.__swift5_capture: 0x4b8
   __TEXT.__constg_swiftt: 0x8e4

   __TEXT.__swift5_types: 0x50
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0xba0
+  __TEXT.__unwind_info: 0xbd8
   __TEXT.__eh_frame: 0x358
   __DATA_CONST.__auth_got: 0xa38
-  __DATA_CONST.__got: 0x560
+  __DATA_CONST.__got: 0x568
   __DATA_CONST.__auth_ptr: 0x260
-  __DATA_CONST.__const: 0x1b50
+  __DATA_CONST.__const: 0x1ba0
   __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x4f70
-  __DATA.__objc_selrefs: 0x1130
-  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_const: 0x4fa0
+  __DATA.__objc_selrefs: 0x1170
+  __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x12f0
   __DATA.__data: 0x1990
   __DATA.__bss: 0x900

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C73D704B-24EC-3728-BB32-D8D7EE82ADAF
-  Functions: 1231
-  Symbols:   3399
-  CStrings:  1382
+  UUID: 5D2CCCD2-3230-3BD0-8811-9F2D970B2212
+  Functions: 1242
+  Symbols:   3425
+  CStrings:  1400
 
Symbols:
+ -[CAFDCarDataServiceAgent _featureListDidUpdateFeature:]
+ -[CAFDCarDataServiceAgent _featureListDidUpdateFeature:].cold.1
+ -[CAFDCarDataServiceAgent _mainQueue_initVehicleDataSession:].cold.13
+ -[CAFDCarDataServiceAgent featureDenyLists]
+ -[CAFDCarDataServiceAgent session:didUpdateConfiguration:]
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table78
+ GCC_except_table85
+ GCC_except_table93
+ OBJC_IVAR_$_CAFDCarDataServiceAgent._featureDenyLists
+ _OBJC_CLASS_$_CRCarPlayFeatureDenyList
+ _OUTLINED_FUNCTION_13
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244.cold.1
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244.cold.2
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244.cold.3
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.244.cold.4
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.245
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.247
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.247.cold.1
+ __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.257
+ ___56-[CAFDCarDataServiceAgent initWithSessionStatus:config:]_block_invoke
+ ___56-[CAFDCarDataServiceAgent initWithSessionStatus:config:]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e51_v32?0"NSNumber"8"CRCarPlayFeatureDenyList"16^B24lw32l8
+ ___block_descriptor_48_e8_32s40w_e23_v28?0Q8B16"NSError"20lw40l8s32l8
+ _objc_msgSend$_featureListDidUpdateFeature:
+ _objc_msgSend$configureDisabledASCFromSessionConfig:featureDenyList:
+ _objc_msgSend$featureDenyLists
+ _objc_msgSend$featureDisabledWithUpdateHandler:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithOptions:
+ _objc_msgSend$updatePluginConfigs:
+ _objc_msgSend$vehicleDataPluginConfigs
- GCC_except_table74
- GCC_except_table80
- GCC_except_table88
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.241
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.241.cold.1
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.242
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.242.cold.1
- __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.252
CStrings:
+ "%s feature=%lu currentSession=%@ currentCar=%@"
+ "-[CAFDCarDataServiceAgent _featureListDidUpdateFeature:]"
+ "@\"NSDictionary\""
+ "Plugin configs provided"
+ "Processed plugin configs"
+ "Processing plugin configs"
+ "T@\"NSDictionary\",R,N,V_featureDenyLists"
+ "_featureDenyLists"
+ "_featureListDidUpdateFeature:"
+ "configureDisabledASCFromSessionConfig:featureDenyList:"
+ "featureDenyLists"
+ "featureDisabledWithUpdateHandler:"
+ "initWithIdentifier:"
+ "initWithOptions:"
+ "initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:playbackState:mediaItemIdentifier:"
+ "updatePluginConfigs:"
+ "v28@?0Q8B16@\"NSError\"20"
+ "v32@?0@\"NSNumber\"8@\"CRCarPlayFeatureDenyList\"16^B24"
+ "vehicleDataPluginConfigs"
- "initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:playbackState:"

```
