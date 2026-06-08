## com.apple.driver.IOPAudioLPMicDevice

> `com.apple.driver.IOPAudioLPMicDevice`

```diff

-340.3.0.0.0
+400.34.0.0.0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x180e
-  __TEXT.__os_log: 0xd9e
-  __TEXT_EXEC.__text: 0x4690
+  __TEXT.__cstring: 0x18a0
+  __TEXT.__os_log: 0xbf1
+  __TEXT_EXEC.__text: 0x4730
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xe68
+  __DATA_CONST.__const: 0xe70
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: E67E2EB8-E937-3462-9541-7F17623D01FF
-  Functions: 138
+  __DATA_CONST.__auth_got: 0xa0
+  __DATA_CONST.__got: 0x60
+  UUID: C6D3EBCC-B695-3823-8510-DF35C4BD592C
+  Functions: 178
   Symbols:   0
-  CStrings:  128
+  CStrings:  112
 
CStrings:
+ "!((inKey) == nullptr)"
+ "!((inPath) == nullptr)"
+ "!((kRemoteIOStatus) == nullptr)"
+ "!((localIOStatus) == nullptr)"
+ "!((registryEntry) == nullptr)"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/IOPAudioDrivers/src/kext/LPMicDevice/LPMicDeviceHelpers.cpp"
+ "ret = getPropertyDataFromIORegistryPath( gIODTPlane, kPath, IORegistry::kEnabledChannelsKey, outChannelControl.enabledChannels) == 0 "
+ "ret = getPropertyDataFromIORegistryPath( gIODTPlane, kPath, IORegistry::kHistoryChannelsKey, outChannelControl.historyChannels) == 0 "
+ "ret = getPropertyDataFromIORegistryPath( gIODTPlane, kPath, IORegistry::kSupportedChannelsKey, outChannelControl.supportedChannels) == 0 "
+ "ret = inMessage.iopTimeToAbsolute(kRemoteIOStatus->mInputHostTime, convertedHostTime) == 0 "
+ "ret = inNodeInterface->getNodeProperty(latencyProperty) == 0 "
+ "ret = inNodeInterface->getNodeProperty(propertyDescriptor) == 0 "
+ "ret = inNodeInterface->getNodeProperty(safetyOffsetProperty) == 0 "
+ "ret = inNodeInterface->getNodeProperty(streamInfoProperty) == 0 "
+ "ret = inNodeInterface->setNodeProperty(propertyDescriptor) == 0 "
+ "ret = processStreamDescription(currentConfig, outStreamDescriptor.formatFlags) == 0 "
+ "ret = setBooleanValue( inRegistryEntry, IORegistryKey::kHistoricDataSupported, inDeviceInfo.supportsHistorical) == 0 "
+ "ret = setIntegerValue( inRegistryEntry, IORegistryKey::kIOFrameBufferSize, inDeviceInfo.frameBufferSize) == 0 "
+ "ret = setIntegerValue( inRegistryEntry, IORegistryKey::kIOFrameBufferWrapSize, inDeviceInfo.frameBufferWrapSize) == 0 "
+ "ret = setIntegerValue(inRegistryEntry, IORegistryKey::kClockDomain, inDeviceInfo.clockDomain) == 0 "
+ "ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kBitsPerChannel, inStreamDescriptor.bitsPerChannel) == 0 "
+ "ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kBytesPerFrame, inStreamDescriptor.bytesPerFrame) == 0 "
+ "ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kChannelsPerFrame, inStreamDescriptor.channelsPerFrame) == 0 "
+ "ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kFormatFlags, inStreamDescriptor.formatFlags) == 0 "
+ "ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kLatency, inStreamDescriptor.latency) == 0 "
+ "ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kSafetyOffset, inStreamDescriptor.safetyOffset) == 0 "
+ "ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kSampleRate, inStreamDescriptor.sampleRate) == 0 "
- "clearIOAudio2Status"
- "cond \"%s\" fail, %s() ln %d, stat %#x"
- "exp \"%s\" fail, %s(), ln %d, stat %#x"
- "getPropertyDataFromIORegistryPath( gIODTPlane, kPath, IORegistry::kEnabledChannelsKey, outChannelControl.enabledChannels)"
- "getPropertyDataFromIORegistryPath( gIODTPlane, kPath, IORegistry::kHistoryChannelsKey, outChannelControl.historyChannels)"
- "getPropertyDataFromIORegistryPath( gIODTPlane, kPath, IORegistry::kSupportedChannelsKey, outChannelControl.supportedChannels)"
- "getPropertyFromIORegistryPath"
- "handleIOAudio2StatusPacket"
- "inKey"
- "inMessage.iopTimeToAbsolute(kRemoteIOStatus->mInputHostTime, convertedHostTime)"
- "inNodeInterface->getNodeProperty(latencyProperty)"
- "inNodeInterface->getNodeProperty(propertyDescriptor)"
- "inNodeInterface->getNodeProperty(safetyOffsetProperty)"
- "inNodeInterface->getNodeProperty(streamInfoProperty)"
- "inNodeInterface->setNodeProperty(propertyDescriptor)"
- "inPath"
- "inRegistryEntry"
- "kIOReturnUnsupported"
- "kRemoteIOStatus"
- "localIOStatus"
- "processStreamDescription"
- "processStreamDescription(currentConfig, outStreamDescriptor.formatFlags)"
- "ptr \"%s\" is null, cant cont, %s(), ln %d, stat %#x"
- "registryEntry"
- "retrieveChannelControlInfoFromDT"
- "retrieveDeviceInfoFromIOP"
- "retrieveInputStreamDescriptorFromIOP"
- "retrievePropertyChangeEventPacket"
- "sendChannelControlInfoToIOP"
- "setBooleanValue"
- "setBooleanValue( inRegistryEntry, IORegistryKey::kHistoricDataSupported, inDeviceInfo.supportsHistorical)"
- "setIORegistryProperty"
- "setIntegerValue( inRegistryEntry, IORegistryKey::kIOFrameBufferSize, inDeviceInfo.frameBufferSize)"
- "setIntegerValue( inRegistryEntry, IORegistryKey::kIOFrameBufferWrapSize, inDeviceInfo.frameBufferWrapSize)"
- "setIntegerValue(inRegistryEntry, IORegistryKey::kClockDomain, inDeviceInfo.clockDomain)"
- "setIntegerValue(streamDescription, IORegistryKey::Stream::kBitsPerChannel, inStreamDescriptor.bitsPerChannel)"
- "setIntegerValue(streamDescription, IORegistryKey::Stream::kBytesPerFrame, inStreamDescriptor.bytesPerFrame)"
- "setIntegerValue(streamDescription, IORegistryKey::Stream::kChannelsPerFrame, inStreamDescriptor.channelsPerFrame)"
- "setIntegerValue(streamDescription, IORegistryKey::Stream::kFormatFlags, inStreamDescriptor.formatFlags)"
- "setIntegerValue(streamDescription, IORegistryKey::Stream::kLatency, inStreamDescriptor.latency)"
- "setIntegerValue(streamDescription, IORegistryKey::Stream::kSafetyOffset, inStreamDescriptor.safetyOffset)"
- "setIntegerValue(streamDescription, IORegistryKey::Stream::kSampleRate, inStreamDescriptor.sampleRate)"
- "valueObject"

```
