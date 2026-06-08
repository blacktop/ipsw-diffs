## com.apple.driver.AppleHIDTransport

> `com.apple.driver.AppleHIDTransport`

```diff

-9140.6.0.0.0
-  __TEXT.__const: 0x2d4
-  __TEXT.__cstring: 0xc73b
+10100.34.0.0.0
+  __TEXT.__const: 0x2e3
+  __TEXT.__cstring: 0xc8e9
   __TEXT.__os_log: 0x2d8
-  __TEXT_EXEC.__text: 0x7a138
+  __TEXT_EXEC.__text: 0x7bef4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3e8
   __DATA.__common: 0x4c0
   __DATA.__bss: 0x130
-  __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0x140
   __DATA_CONST.__mod_init_func: 0xc8
   __DATA_CONST.__mod_term_func: 0xc8
-  __DATA_CONST.__const: 0x90a8
+  __DATA_CONST.__const: 0x91f8
   __DATA_CONST.__kalloc_type: 0xac0
-  UUID: 9471948E-6848-34C7-8E34-C2D6ECA37D01
-  Functions: 2189
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x140
+  UUID: 87E52601-CFF7-3AF6-B1EE-1C543F65DEC7
+  Functions: 2222
   Symbols:   0
-  CStrings:  1499
+  CStrings:  1522
 
CStrings:
+ "(ioRet == kIOReturnSuccess) || (ioRet == kIOReturnNotReady)"
+ "(ret == kIOReturnSuccess) || (ret == kIOReturnUnsupported)"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/AppleHIDTransportDeviceDummy.cpp"
+ "1211111"
+ "1211111212221212111111111111111112"
+ "1211111212221212111111111111111212"
+ "121111121222121211111111111111121212"
+ "12111112122212121111112111111111122112111121"
+ "1211111212221212111112111221121111"
+ "12111112122212121111121112211211111"
+ "AHTOverrideWorkLoopAtInit"
+ "AsyncDescriptorDone"
+ "EncodedPayload"
+ "False"
+ "MemoryDumpOnBootFailure"
+ "OSDynamicCast(OSData, image->getObject(kPropertyPayloadKey))"
+ "OSDynamicCast(OSDictionary, image->getObject(kPropertyMatchingDictionaryKey))"
+ "OSDynamicCast(OSNumber, calibrationDict->getObject(kPropertyLengthKey))"
+ "OSDynamicCast(OSNumber, descriptor->getObject(kPropertyLengthKey))"
+ "OSDynamicCast(OSNumber, descriptor->getObject(kPropertyOffsetKey))"
+ "OSDynamicCast(OSNumber, image->getObject(kPropertyBranchOffsetKey))"
+ "OSDynamicCast(OSNumber, image->getObject(kPropertyDelayKey))"
+ "OSDynamicCast(OSNumber, image->getObject(kPropertyOffsetLengthKey))"
+ "OSDynamicCast(OSNumber, image->getObject(kPropertyPropertyIDKey))"
+ "OSDynamicCast(OSNumber, image->getObject(kPropertyReportIDKey))"
+ "OSDynamicCast(OSString, calibrationDict->getObject(kPropertyCalibrationPropertyNameKey))"
+ "OSDynamicCast(OSString, descriptor->getObject(kPropertyVariableNameKey))"
+ "OSDynamicCast(OSString, image->getObject(kPropertyVariableNameKey))"
+ "Off Without Reset"
+ "[0x%llx][%llx][%s::%s]: Drain was active during stop, cleaning up"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Failed to remove property"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Failed to send mach notification with type %u (err=0x%X)"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Hasn't finished processing the descriptors. Waiting for descriptors."
+ "[0x%llx][%llx][%s::%s]: Loading EEPROM content from key: %s"
+ "[0x%llx][%llx][%s::%s]: Mach notification queue is full, current notification is dropped"
+ "[0x%llx][%llx][%s::%s]: Property %s reference did not define an offset or size. Using entire payload"
+ "[0x%llx][%llx][%s::%s]: Run In RestoreOS = %u, In %s, skipping image loading for interface %s"
+ "[0x%llx][%llx][%s::%s]: Triggering memory dump due to boot failure"
+ "_eepromContentKey"
+ "beginDrainFifo"
+ "eeprom-read-property"
+ "endDrainFifo"
+ "mergeFromHeader || validReferenceLocation"
+ "performMemoryDumpSequence"
+ "pollData"
+ "ret == kIOReturnSuccess || ret == kIOReturnUnsupported"
+ "retVal == kIOReturnSuccess"
+ "setProperty(kAHTPropertyHeaderKey, propertyHeaderDict)"
+ "sharedMemoryBlock->getBuffer()->getCapacity() < UINT32_MAX"
+ "shouldSkipPayloadVerification || OSDynamicCast(OSData, image->getObject(kPropertyPayloadKey))"
+ "unknown"
- "((OSData *) OSMetaClassBase::safeMetaCast((image->getObject(kPropertyPayloadKey)), (OSData::metaClass)))"
- "((OSDictionary *) OSMetaClassBase::safeMetaCast((image->getObject(kPropertyMatchingDictionaryKey)), (OSDictionary::metaClass)))"
- "((OSNumber *) OSMetaClassBase::safeMetaCast((calibrationDict->getObject(kPropertyLengthKey)), (OSNumber::metaClass)))"
- "((OSNumber *) OSMetaClassBase::safeMetaCast((descriptor->getObject(kPropertyLengthKey)), (OSNumber::metaClass)))"
- "((OSNumber *) OSMetaClassBase::safeMetaCast((descriptor->getObject(kPropertyOffsetKey)), (OSNumber::metaClass)))"
- "((OSNumber *) OSMetaClassBase::safeMetaCast((image->getObject(kPropertyBranchOffsetKey)), (OSNumber::metaClass)))"
- "((OSNumber *) OSMetaClassBase::safeMetaCast((image->getObject(kPropertyDelayKey)), (OSNumber::metaClass)))"
- "((OSNumber *) OSMetaClassBase::safeMetaCast((image->getObject(kPropertyOffsetLengthKey)), (OSNumber::metaClass)))"
- "((OSNumber *) OSMetaClassBase::safeMetaCast((image->getObject(kPropertyPropertyIDKey)), (OSNumber::metaClass)))"
- "((OSNumber *) OSMetaClassBase::safeMetaCast((image->getObject(kPropertyReportIDKey)), (OSNumber::metaClass)))"
- "((OSString *) OSMetaClassBase::safeMetaCast((calibrationDict->getObject(kPropertyCalibrationPropertyNameKey)), (OSString::metaClass)))"
- "((OSString *) OSMetaClassBase::safeMetaCast((descriptor->getObject(kPropertyVariableNameKey)), (OSString::metaClass)))"
- "((OSString *) OSMetaClassBase::safeMetaCast((image->getObject(kPropertyVariableNameKey)), (OSString::metaClass)))"
- "(ioRet == 0) || (ioRet == (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2d8))"
- "(ret == 0) || (ret == (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c7))"
- "121111121222121211111111111111111"
- "121111121222121211111111111111112"
- "1211111212221212111111211111111112211211111"
- "121111121222121211111211122112111"
- "mergeFromHeader || referenceOffset"
- "mergeFromHeader || referenceSize"
- "referenceOffset"
- "referenceSize"
- "ret == 0 || ret == (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c7)"
- "retVal == 0"
- "setProperty(\"Property Header\", propertyHeaderDict)"
- "sharedMemoryBlock->getBuffer()->getCapacity() < 4294967295U"
- "shouldSkipPayloadVerification || ((OSData *) OSMetaClassBase::safeMetaCast((image->getObject(kPropertyPayloadKey)), (OSData::metaClass)))"

```
