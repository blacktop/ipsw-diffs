## com.apple.driver.IOPAudioLPMicDevice

> `com.apple.driver.IOPAudioLPMicDevice`

```diff

-340.3.0.0.0
+400.34.0.0.0
   __TEXT.__const: 0x8 sha256:3e990d45c83fa01d9bf0c64b79ed7678df3c723614f0f7eccdc3d196fa3073e9
-  __TEXT.__cstring: 0x180e sha256:b3437e30a3e19e510743cb0047add7f820301cc524690e74352fe3dadf8082b9
-  __TEXT.__os_log: 0xd9e sha256:ed4a99eca032637e73d0277be8c91291a902951f870554e5b64c18e96d355b30
-  __TEXT_EXEC.__text: 0x4690 sha256:bed1d1d5e7cf7fa80195c3f792bdef67e74d2144e76cd9673f5dd48e7cfe0c22
+  __TEXT.__cstring: 0x18a0 sha256:7c24f65f1a1c8b048edc2a3eb872e50afdd9ae56a8c9cef6987add58f71c3830
+  __TEXT.__os_log: 0xbf1 sha256:ac0b59ef20398bcbef4b4b760b4da012e6effe3c2efe0fbcded10513aa81e287
+  __TEXT_EXEC.__text: 0x4730 sha256:a7d7e868c9c734a8f6bb3d94d1afc0d3cd6d33049a698b55efb7e9938a6406a7
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:0fc6ecc68009152420acab276ca3c7ff30e977ee1fd814f8bdd035f422cfe9c2
+  __DATA.__data: 0xc8 sha256:5264da86cc52bfe7be7d4f13760247216b66fbac91e0225f5669de4edd97b24e
   __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_CONST.__auth_got: 0xa0 sha256:be136e6741187f347d86eec7fd4e20790e8159fd88aee3ce946f29e4ebdc81ba
-  __DATA_CONST.__got: 0x60 sha256:9af216c27d95539a483787c0f77b27f22c17407dbed509d074adbc521dea01bc
-  __DATA_CONST.__mod_init_func: 0x10 sha256:6f2ab500c85a00dc77a25ab56f2978f2bff371f5f4ad45e32a501d1a2ea4f7be
-  __DATA_CONST.__mod_term_func: 0x10 sha256:ad94dd39593aec8aae6c450cd6ff8ed1da4189cc4125d16dff89cb68d8db8f1c
-  __DATA_CONST.__const: 0xe68 sha256:ed7929d9e978118fbd7a63369e66183c07a882777d344c8b5acc2df83bf2f7b4
-  __DATA_CONST.__kalloc_type: 0x80 sha256:0f59b2ed15bf1862802d5ecea66c2ccd0d21b38c1f57c0e5436a38dbcd7a5aea
-  UUID: E67E2EB8-E937-3462-9541-7F17623D01FF
-  Functions: 138
+  __DATA_CONST.__mod_init_func: 0x10 sha256:aaa52341ffd9574726f6419803dd5ddace97bc8106718af8115fb7cb4693ffb5
+  __DATA_CONST.__mod_term_func: 0x10 sha256:97269cfc5bfb288151d72b63d92d8a90c263e144572e2192f1663e5a8ce345bf
+  __DATA_CONST.__const: 0xe70 sha256:a4a27a25a8b5c5465b2e87723a2a57af1882c01f879c8a8e7a8d4ea3196905c7
+  __DATA_CONST.__kalloc_type: 0x80 sha256:df869125c6b520517f4834ff2b465fa75689428f2872fe43f3ce7952fb6f752d
+  __DATA_CONST.__auth_got: 0xa0 sha256:69b0519e3b616c9ff662a562d24541cf3c9b52cda5327effadc16eb33e30413a
+  __DATA_CONST.__got: 0x60 sha256:200ec5ad54cae89a2b43b9dd56b01099edba6f8386149012db427f019660b3d8
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
