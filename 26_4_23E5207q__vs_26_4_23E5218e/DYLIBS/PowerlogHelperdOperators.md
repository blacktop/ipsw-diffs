## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-3031.100.213.502.1
-  __TEXT.__text: 0x1d64e8
+3031.100.234.0.0
+  __TEXT.__text: 0x1d6bac
   __TEXT.__auth_stubs: 0x1b80
-  __TEXT.__objc_methlist: 0xf0f8
-  __TEXT.__const: 0x6b8
+  __TEXT.__objc_methlist: 0xf150
+  __TEXT.__const: 0x6c8
   __TEXT.__cstring: 0x241b9
-  __TEXT.__oslogstring: 0x12c42
+  __TEXT.__oslogstring: 0x12db4
   __TEXT.__gcc_except_tab: 0x24ec
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x38f8
+  __TEXT.__unwind_info: 0x3910
   __TEXT.__objc_classname: 0xc33
-  __TEXT.__objc_methname: 0x32b1e
-  __TEXT.__objc_methtype: 0x292c
-  __TEXT.__objc_stubs: 0x1f480
-  __DATA_CONST.__got: 0xec0
+  __TEXT.__objc_methname: 0x32c65
+  __TEXT.__objc_methtype: 0x29c8
+  __TEXT.__objc_stubs: 0x1f560
+  __DATA_CONST.__got: 0xec8
   __DATA_CONST.__const: 0x4420
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c30
+  __DATA_CONST.__objc_selrefs: 0x9c68
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x14bb0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F6D05ECA-4CE0-3045-9AFC-098D9EDA7007
-  Functions: 7988
-  Symbols:   27168
-  CStrings:  22650
+  UUID: 45436700-FEC3-3F0B-8367-1568ED57C262
+  Functions: 8003
+  Symbols:   27207
+  CStrings:  22672
 
Symbols:
+ +[PLAggregateSummarizationService roundToSignificantDigits:sigDigs:]
+ +[PLBatteryUIResponderService shouldDisableQueryResponder]
+ -[PLBatteryUIResponseTypeIOSUISOCDrain drainForInterval:start:max:end:]
+ -[PLBatteryUIResponseTypeIOSUISOCDrain finalizeInterval:uiDrainTotal:dynamicDrainTotal:dynamicCutoff:includeDynamic:]
+ -[PLBatteryUIResponseTypeIOSUISOCDrain finalizeInterval:uiDrainTotal:dynamicDrainTotal:dynamicCutoff:includeDynamic:].cold.1
+ -[PLBatteryUIResponseTypeIOSUISOCDrain finalizeInterval:uiDrainTotal:dynamicDrainTotal:dynamicCutoff:includeDynamic:].cold.2
+ -[PLBatteryUIResponseTypeIOSUISOCDrain finalizeInterval:uiDrainTotal:dynamicDrainTotal:dynamicCutoff:includeDynamic:].cold.3
+ -[PLBatteryUIResponseTypeIOSUISOCDrain initializeInterval:isCharging:level:timestamp:]
+ -[PLBatteryUIResponseTypeIOSUISOCDrain initializeInterval:isCharging:level:timestamp:].cold.1
+ -[PLBatteryUIResponseTypeIOSUISOCDrain processBucketAtIndex:bucketStart:bucketEnd:levelIndex:uiDrain:dynamicDrain:]
+ -[PLBatteryUIResponseTypeIOSUISOCDrain processBucketAtIndex:bucketStart:bucketEnd:levelIndex:uiDrain:dynamicDrain:].cold.1
+ -[PLBatteryUIResponseTypeIOSUISOCDrain processBucketAtIndex:bucketStart:bucketEnd:levelIndex:uiDrain:dynamicDrain:].cold.2
+ -[PLBatteryUIResponseTypeIOSUISOCDrain processBucketAtIndex:bucketStart:bucketEnd:levelIndex:uiDrain:dynamicDrain:].cold.3
+ -[PLBatteryUIResponseTypeIOSUISOCDrain updateInterval:level:timestamp:]
+ -[PLBatteryUIResponseTypeIOSUISOCDrain updateInterval:level:timestamp:].cold.1
+ GCC_except_table18
+ GCC_except_table25
+ ___47-[PLBatteryUIResponderService linkDependencies]_block_invoke.69
+ ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.237
+ ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.281
+ ___block_literal_global.366
+ ___block_literal_global.625
+ ___block_literal_global.639
+ _objc_msgSend$drainForInterval:start:max:end:
+ _objc_msgSend$finalizeInterval:uiDrainTotal:dynamicDrainTotal:dynamicCutoff:includeDynamic:
+ _objc_msgSend$initializeInterval:isCharging:level:timestamp:
+ _objc_msgSend$processBucketAtIndex:bucketStart:bucketEnd:levelIndex:uiDrain:dynamicDrain:
+ _objc_msgSend$roundToSignificantDigits:sigDigs:
+ _objc_msgSend$shouldDisableQueryResponder
+ _objc_msgSend$updateInterval:level:timestamp:
- GCC_except_table17
- GCC_except_table24
- ___47-[PLBatteryUIResponderService linkDependencies]_block_invoke.68
- ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.236
- ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.280
- ___block_literal_global.365
- ___block_literal_global.624
- ___block_literal_global.638
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJI8ugAOavgk3v49SENRWlVI_uGQAVYuJccTSK8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLWifiAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLApplicationAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLFSEventAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSpringBoardAgent.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeBatteryBreakdown+Utilities.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeBatteryBreakdown.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeBatteryBreakdownInternal.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeDrainComparisonSummary.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeUtilities.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/PLAppTimeService.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/PLBLDService.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/PLBatteryBreakdownService.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/PLBatteryUIService.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetService.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetServiceDAS.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/PLEnergyIssuesService.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Utilities/PLMetricsFormatterJSON.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
+ "/Library/Caches/com.apple.xbs/3D0DBE5F-F63F-4599-93C9-4981F04101F2/TemporaryDirectory.z8FlEe/Sources/PerfPowerServices_Operators/Utilities/PLUtilities.m"
+ "@24@0:8^{net_port_info=SS{timeval32=ii}[16C]SS(in_addr_4_6={in_addr=I}{in6_addr=(?=[16C][8S][4I])})(in_addr_4_6={in_addr=I}{in6_addr=(?=[16C][8S][4I])})ii[17c][17c][16C][16C]S}16"
+ "Integer overflow detected in dynamicDrainTotal"
+ "Integer overflow detected in uiDrainTotal"
+ "Integer overflow in dynamic drain at cutoff"
+ "NULL pointer passed to processBucketAtIndex"
+ "Null interval pointer in initializeInterval"
+ "Null interval pointer in updateInterval"
+ "Null pointer in finalizeInterval"
+ "Q32@0:8Q16Q24"
+ "Unsupported platform, skipping query responder"
+ "drainForInterval:start:max:end:"
+ "finalizeInterval:uiDrainTotal:dynamicDrainTotal:dynamicCutoff:includeDynamic:"
+ "i32@0:8B16i20i24i28"
+ "initializeInterval:isCharging:level:timestamp:"
+ "levelIndex out of bounds: %d"
+ "processBucketAtIndex:bucketStart:bucketEnd:levelIndex:uiDrain:dynamicDrain:"
+ "roundToSignificantDigits:sigDigs:"
+ "shouldDisableQueryResponder"
+ "updateInterval:level:timestamp:"
+ "v36@0:8^{?=BiiidB}16i24d28"
+ "v40@0:8^{?=BiiidB}16B24i28d32"
+ "v52@0:8^{?=BiiidB}16^i24^i32d40B48"
+ "v60@0:8i16@20@28^i36^i44^i52"
- "/AppleInternal/Library/BuildRoots/4~CI0JugAXoICN1NwiahSdy4LC5PHcywQlTndJlu0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLWifiAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLApplicationAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLFSEventAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSpringBoardAgent.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeBatteryBreakdown+Utilities.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeBatteryBreakdown.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeBatteryBreakdownInternal.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeDrainComparisonSummary.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeUtilities.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/PLAppTimeService.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/PLBLDService.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/PLBatteryBreakdownService.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/PLBatteryUIService.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetService.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetServiceDAS.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/PLEnergyIssuesService.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Utilities/PLMetricsFormatterJSON.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
- "/Library/Caches/com.apple.xbs/3B0B5E59-D13B-40DA-A71F-9DC338232F79/TemporaryDirectory.eOSdWl/Sources/PerfPowerServices_Operators/Utilities/PLUtilities.m"
- "@24@0:8^{net_port_info=SS{timeval32=ii}[16C]SS(in_addr_4_6={in_addr=I}{in6_addr=(?=[16C][8S][4I])})(in_addr_4_6={in_addr=I}{in6_addr=(?=[16C][8S][4I])})ii[17c][17c][16C][16C]}16"

```
