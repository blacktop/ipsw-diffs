## com.apple.driver.AppleHIDTransport

> `com.apple.driver.AppleHIDTransport`

```diff

-8150.1.0.0.0
+9100.28.0.0.0
   __TEXT.__const: 0x2d4
-  __TEXT.__cstring: 0xab70
-  __TEXT.__os_log: 0x283
-  __TEXT_EXEC.__text: 0x70fa8
+  __TEXT.__cstring: 0xbf56
+  __TEXT.__os_log: 0x2d8
+  __TEXT_EXEC.__text: 0x884e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x420
-  __DATA.__bss: 0x98
-  __DATA_CONST.__auth_got: 0x438
+  __DATA.__common: 0x4c0
+  __DATA.__bss: 0x130
+  __DATA_CONST.__auth_got: 0x460
   __DATA_CONST.__got: 0x140
-  __DATA_CONST.__mod_init_func: 0xb8
-  __DATA_CONST.__mod_term_func: 0xb8
-  __DATA_CONST.__const: 0x8a88
-  __DATA_CONST.__kalloc_type: 0x9c0
-  UUID: 5C6F0875-6B54-3A5D-A454-5A740C425AEF
-  Functions: 1983
+  __DATA_CONST.__mod_init_func: 0xc8
+  __DATA_CONST.__mod_term_func: 0xc8
+  __DATA_CONST.__const: 0x8fd0
+  __DATA_CONST.__kalloc_type: 0xac0
+  UUID: 612C5B9A-1E41-34FC-913E-9F541FDA5445
+  Functions: 2164
   Symbols:   0
-  CStrings:  1316
+  CStrings:  1451
 
CStrings:
+ "%u"
+ "*dest"
+ "/Library/Caches/com.apple.xbs/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/AHTFunctionExecutor.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/AppleHIDTransportStats.cpp"
+ "12111111"
+ "12111112122212121111111111112111121212121211111222221111221111111121111121"
+ "121111121222121211111121111111111221121111"
+ "1211111212221212111111211111111112211211111"
+ "1211111212221212111111211111111112211211111111"
+ "121111121222121211111121111111111221121111112222111122222222222222222222222222222222222222222222222222212"
+ "1211122"
+ "121121"
+ "121121211"
+ "AHTFunctionDisplayMessage"
+ "AHTFunctionExecutor"
+ "ARMFunctionConfigurations"
+ "AppleHIDTransportDRAMUsageStats"
+ "AppleHIDTransportStats"
+ "DRAM_Size"
+ "DelayUs"
+ "FDR - interface"
+ "FIFOid"
+ "Integer"
+ "MTP.SharedDRAMUsage"
+ "MaxDRAMUsageInLastDay"
+ "Multitouch"
+ "Notify"
+ "NotifyParameter"
+ "Overwrites"
+ "ParameterConfigs"
+ "PropertyLength"
+ "ReadOffset"
+ "Sequence"
+ "SerialEnabled"
+ "TimeoutUs"
+ "WriteOffset"
+ "ZeroedData"
+ "[0x%llx][%llx][%s::%s]: %s's AIDImageDownloader hasn't finished loading calibration data, will handle calibration request later"
+ "[0x%llx][%llx][%s::%s]: AHTFunction Notify for interfaceId %u, functionId %s, reason %u, timestamp %llu Returned data size:%u, arg0Size:%u, arg1Size:%u, arg2Size:%u"
+ "[0x%llx][%llx][%s::%s]: AHTFunction request for interfaceId %u, functionId %s, reason %u, timestamp %llu"
+ "[0x%llx][%llx][%s::%s]: Caching function executor for interfaceId:%u"
+ "[0x%llx][%llx][%s::%s]: ERROR!! %s got a memory dump version mistach, got %u, expected %u"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Cannot acquire report gate"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Fail to notify after ARM function call with error 0x%08X for interface %u, functionID %s reason %u, timestamp %llu"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Failed to construct function with name: %s"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Failing validation due to failed ARM function call %s"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Function %s specified the TimeoutUs key in a customer build. This timeout will be ignored"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Parameter configs contains unsupported type:%s"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Parameter of type %s cannot have overwrites"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Validation failed: 0x%08X"
+ "[0x%llx][%llx][%s::%s]: ERROR!! bad data retrieved"
+ "[0x%llx][%llx][%s::%s]: ERROR!! data retrieval failed, result = 0x%08x"
+ "[0x%llx][%llx][%s::%s]: ERROR!! dictData is nullptr"
+ "[0x%llx][%llx][%s::%s]: ERROR!! entry in array is empty"
+ "[0x%llx][%llx][%s::%s]: ERROR!! eventPayload is nullptr"
+ "[0x%llx][%llx][%s::%s]: ERROR!! logEvent failed, result = 0x%08x"
+ "[0x%llx][%llx][%s::%s]: FDR load completed for interface %s, will fetch calibration data now"
+ "[0x%llx][%llx][%s::%s]: InterfaceId:%u not configured with any functions"
+ "[0x%llx][%llx][%s::%s]: Request for AHTFunction with ID:%s"
+ "[0x%llx][%llx][%s::%s]: Scheduled ARM function request on separate thread"
+ "[0x%llx][%llx][%s::%s]: Skipping memory dump capture for interface %u (%s) due to level being 0"
+ "[0x%llx][%llx][%s::%s]: logDRAMUsage, idx = %d, id = %u, maxDRAMUsageInLastDay = %llu, totalDRAMCapacity = %llu, isSerialLogEnabled = %x"
+ "[0x%llx][%llx][%s::%s]: logDRAMUsage, memoryFifoCount = %d"
+ "[0x%llx][%llx][%s::%s]: statCollection"
+ "[AHTPF::%s]: ERROR!! Param 1 should contain a message ID"
+ "_allFunctionConfigs"
+ "_allFunctionConfigs->getCount() > 0"
+ "_functionExecutors"
+ "_functionProvider"
+ "_notifyCallbackOwner"
+ "_pendingCalibrationDescriptors"
+ "_provider && _provider->getWorkLoop()"
+ "_statCollectionTimer"
+ "allAgumentData->getCount() <= kMaxFunctionArgCount && allAgumentData->getCount() == allParameterConfigs->getCount()"
+ "allAgumentData->setObject(argumentData)"
+ "allFunctionConfigs->getCount() > 0"
+ "allParameterConfigs"
+ "allParameterConfigs && allAgumentData"
+ "allParameterConfigs->getCount() <= kMaxFunctionArgCount"
+ "argData"
+ "argOutput"
+ "argumentData"
+ "argumentData->getCapacity() > 0"
+ "cacheAHTFunctions"
+ "cacheFunctionExecutor"
+ "cacheResult == 0 "
+ "callARMFunction"
+ "callARMFunctionSequence"
+ "callFunctionFromThread_block_invoke"
+ "configuredData"
+ "defaultProperties"
+ "dictDataDRAMFIFOid"
+ "dictDataIsSerialEnabled && dictKeyMaxDRAMUsageInLastDay && dictKeyIsSerialEnabled && dictKeyDRAMTotalSize && dictKeyDRAMFIFOid"
+ "dstBytes"
+ "eventPayload"
+ "functionCache->getCount() > 0"
+ "functionExecutor"
+ "functionID"
+ "getDataArgument"
+ "getIntegerArgument"
+ "getPropertyLengthArgument"
+ "getPropertyValueArgument"
+ "getZeroedDataArgument"
+ "handleAHTFunctionNotify"
+ "handleAHTFunctionRequest"
+ "handleCalibrationDescriptor"
+ "handlePendingCalibrationDescriptor_block_invoke"
+ "hid-restore-personality"
+ "logDRAMUsage"
+ "maxDRAMUsageInLastDayArray && totalDRAMCapacityArray"
+ "maxDRAMUsageInLastDayObj && totalDRAMCapacityObj"
+ "memoryFifoCount && fifoIds && maxDRAMUsageInLastDayArray->getCount() == memoryFifoCount && totalDRAMCapacityArray->getCount() == memoryFifoCount"
+ "notifyCallbackOwner"
+ "notifyReportData"
+ "notifyReportData->appendBytes(&notifyReport, sizeof(notifyReport))"
+ "notifyReportData->appendBytes(returnData->returnBytes)"
+ "notifyReportData->getLength() == sizeof(notifyReport) + notifyReport.argSizes[0] + notifyReport.argSizes[1] + notifyReport.argSizes[2]"
+ "notifyWithResult"
+ "number"
+ "osNumber"
+ "owner && action"
+ "owner && callback"
+ "parameterConfig"
+ "propertyName"
+ "propertyValue"
+ "provider && functionRegistry && allFunctionConfigs"
+ "readOffset + size <= runtimeData->getLength()"
+ "readOffsetObject && writeOffsetObject && sizeObject"
+ "registerDRAMUsageDataCollection"
+ "reportBuffer->getLength() == reportSize"
+ "reportBuffer->getLength() >= sizeof(ConfiguredFunctionCallRequest)"
+ "reportDescriptor"
+ "request"
+ "returnBytes->appendBytes(argOutput.get())"
+ "setDownloadCompletedAction"
+ "setObjectSucceed"
+ "shouldAbort"
+ "site.AHTFunctionCallThreadParam"
+ "site.AHTFunctionDisplayMessage"
+ "site.AHTFunctionExecutor"
+ "site.AppleHIDTransportDRAMUsageStats"
+ "site.AppleHIDTransportStats"
+ "sizeObject"
+ "srcBytes"
+ "statCollection"
+ "validationConfig"
+ "writeOffset + size <= argumentData->getLength()"
- "121111121222121211111111111121111212121212111112222211112211111111211112"
- "121111121222121211111121111111111221121"
- "1211111212221212111111211111111112211211"
- "12111112122212121111112111111111122112111111"
- "121111121222121211111121111111111221121111222211112222222222222222222222222222222222222222222222222221"
- "121112"
- "[0x%llx][%llx][%s::%s]: %s received firmware update complete message with ID=%u, status=0x%08X (%s)"
- "config->setObject(\"DefaultDumpLevelCustomer\", levelNum)"
- "config->setObject(\"DefaultDumpLevelInternal\", levelNum)"
- "firmwareUpdateCompleteFromThread"
- "firmwareUpdateCompleteFromThread_block_invoke"
- "site.FirmwareUpdateCompleteThreadParam"

```
