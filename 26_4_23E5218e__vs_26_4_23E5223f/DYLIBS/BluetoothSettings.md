## BluetoothSettings

> `/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`

```diff

-454.3.0.0.0
-  __TEXT.__text: 0x23144
+454.4.0.0.0
+  __TEXT.__text: 0x2339c
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x18cc
-  __TEXT.__cstring: 0x1781
+  __TEXT.__objc_methlist: 0x18bc
+  __TEXT.__cstring: 0x1741
   __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0x320
-  __TEXT.__oslogstring: 0x2102
+  __TEXT.__oslogstring: 0x21c2
+  __TEXT.__ustring: 0x8c
   __TEXT.__swift5_typeref: 0x1b6
   __TEXT.__constg_swiftt: 0x118
   __TEXT.__swift5_reflstr: 0x41

   __TEXT.__unwind_info: 0x750
   __TEXT.__eh_frame: 0x258
   __TEXT.__objc_classname: 0x237
-  __TEXT.__objc_methname: 0x4ef4
+  __TEXT.__objc_methname: 0x4f05
   __TEXT.__objc_methtype: 0x1090
-  __TEXT.__objc_stubs: 0x4400
+  __TEXT.__objc_stubs: 0x4420
   __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__const: 0x580
+  __DATA_CONST.__const: 0x578
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x1ae0
+  __AUTH_CONST.__cfstring: 0x1aa0
   __AUTH_CONST.__objc_const: 0x2610
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E82BE94F-1302-34AD-AC99-A65787E2F49E
-  Functions: 590
-  Symbols:   2270
-  CStrings:  1700
+  UUID: E844E222-794F-3665-8364-016D8F1C525A
+  Functions: 593
+  Symbols:   2275
+  CStrings:  1696
 
Symbols:
+ +[DKMessage encodeDKMessageRangingProcedureResultsContinue:]
+ +[DKMessage encodeDKMessageRangingProcedureResultsStart:]
+ -[BTSDevicesController specifiers].cold.1
+ -[BTSDevicesController specifiers].cold.2
+ ___44-[BTSDevicesController _updateHealthDevices]_block_invoke.636
+ ___44-[BTSDevicesController _updateHealthDevices]_block_invoke.638
+ ___50-[BTSDevicesController startOutgoingCarPlaySetup:]_block_invoke.827
+ ___50-[BTSDevicesController startOutgoingCarPlaySetup:]_block_invoke_2.828
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.841
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.841.cold.1
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.845
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.845.cold.1
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.846
+ ___58-[BTSDevicesController tableView:didSelectRowAtIndexPath:]_block_invoke.732
+ ___block_literal_global.659
+ ___block_literal_global.734
+ ___block_literal_global.787
+ ___block_literal_global.801
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_BluetoothSettings
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$encodeDKMessageRangingProcedureResultsContinue:
+ _objc_msgSend$encodeDKMessageRangingProcedureResultsStart:
+ _processToneQualities
+ _reformatAntennaByte
- +[DKMessage encodeDKMessageMeasurementDataStart:]
- +[DKMessage encodeDKMessageMeasurementSubEventContinue:]
- +[DKMessage sumDataValues:]
- _BTSKDKMessageStatus
- _BTSKDKMessageType
- ___44-[BTSDevicesController _updateHealthDevices]_block_invoke.633
- ___44-[BTSDevicesController _updateHealthDevices]_block_invoke.635
- ___50-[BTSDevicesController startOutgoingCarPlaySetup:]_block_invoke.824
- ___50-[BTSDevicesController startOutgoingCarPlaySetup:]_block_invoke_2.825
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.838
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.838.cold.1
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.842
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.842.cold.1
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.843
- ___58-[BTSDevicesController tableView:didSelectRowAtIndexPath:]_block_invoke.729
- ___block_literal_global.656
- ___block_literal_global.731
- ___block_literal_global.784
- ___block_literal_global.798
- _objc_msgSend$encodeDKMessageMeasurementDataStart:
- _objc_msgSend$encodeDKMessageMeasurementSubEventContinue:
CStrings:
+ "MCProfileConnection localized restriction source description for feature “%@” is missing"
+ "MCProfileConnection localized restriction source description for feature “%@” should contain a “%@”"
+ "Missing ManagedConfiguration format string (%@)"
+ "This device is discoverable as “%@” while Bluetooth Settings is open."
+ "dataWithLength:"
+ "encodeDKMessageRangingProcedureResultsContinue:"
+ "encodeDKMessageRangingProcedureResultsStart:"
+ "kCSTotalStepsSubevent"
- "Q24@0:8@16"
- "bad format string for devices table view (A) (%@): %@"
- "encodeDKMessageMeasurementDataStart:"
- "encodeDKMessageMeasurementSubEventContinue:"
- "kBTSKDKMessageStatus"
- "kBTSKDKMessageType"
- "kCBCSCurrentStepIndex"
- "kCBCSNumAntennaPath"
- "sumDataValues:"

```
