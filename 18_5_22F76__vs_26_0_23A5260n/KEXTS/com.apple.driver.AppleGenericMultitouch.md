## com.apple.driver.AppleGenericMultitouch

> `com.apple.driver.AppleGenericMultitouch`

```diff

-23.0.0.0.0
-  __TEXT.__cstring: 0x6115
+26.2.0.0.0
+  __TEXT.__cstring: 0x682c
   __TEXT.__const: 0x21e
-  __TEXT.__os_log: 0x6c4
-  __TEXT_EXEC.__text: 0x6e38
+  __TEXT.__os_log: 0x102f
+  __TEXT_EXEC.__text: 0x855c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd4
   __DATA.__common: 0x80
   __DATA.__bss: 0x1
   __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1658
   __DATA_CONST.__kalloc_type: 0x1c0
-  UUID: 32A6EAD4-84F6-3322-84BC-BAC3E2D07ECC
-  Functions: 183
+  UUID: 43532969-880E-3013-AA4A-B4ECCB4A89D6
+  Functions: 213
   Symbols:   0
-  CStrings:  144
+  CStrings:  201
 
CStrings:
+ "%s, %s file: %s, line: %d, value: 0x%08X\n%s line %d"
+ "/Library/Caches/com.apple.xbs/Sources/AppleGenericMultitouch/Kext/AppleGenericMultitouchDecider.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleGenericMultitouch/Kext/hiddevice/AppleGenericMultitouchHIDDeviceBase.cpp"
+ "121111121222121211112"
+ "1211111212221212112111222112"
+ "12111112122212121121112221121111"
+ "FirstInputReceived"
+ "Searching parent, name: %s\n%s line %d"
+ "Using config provider: %s\n%s line %d"
+ "_authCPMatch"
+ "_wl"
+ "action"
+ "auth-supported"
+ "auth-supported property found, matching AGM\n%s line %d"
+ "auth-supported property not found\n%s line %d"
+ "authReqStr"
+ "auto AppleGenericMultitouchDecider::modifyPersonalities()::(anonymous class)::operator()(IORegistryEntry *, void *) const"
+ "baseString"
+ "bool AppleGenericMultitouchDecider::performActionOnAuthConsumers(AuthConsumerAction *, void *, bool)"
+ "bool AppleGenericMultitouchDecider::setupMatchingCallback()"
+ "cached"
+ "classToLaunch"
+ "configProvider"
+ "configProviderName"
+ "descriptor"
+ "dict"
+ "downloaders"
+ "flagsNum"
+ "flagsObj"
+ "getConfigManager()"
+ "isAuthenticBool"
+ "isTrustedBool"
+ "md"
+ "newStringData"
+ "newStringSizeNullTerminated <= sizeof(newStringBuffer)"
+ "numberVal"
+ "personalityData"
+ "personalityProp"
+ "props"
+ "rd"
+ "report && (reportType == kIOHIDReportTypeFeature)"
+ "report->getLength() >= cached->getLength()"
+ "service"
+ "service->attach(provider)"
+ "service->init()"
+ "service->start(provider)"
+ "setupMatchingCallback()"
+ "stateBool"
+ "static OSSharedPtr<OSString> AppleGenericMultitouchHIDDeviceBase::copyPersonality(IOService *)"
+ "success"
+ "super::handleStart(provider)"
+ "super::init(dictionary)"
+ "super::start(provider)"
+ "virtual IOReturn AppleGenericMultitouchHIDDeviceBase::getReport(IOMemoryDescriptor *, IOHIDReportType, IOOptionBits)"
+ "virtual IOReturn AppleGenericMultitouchHIDDeviceBase::newReportDescriptor(IOMemoryDescriptor **) const"
+ "virtual IOService *AppleGenericMultitouchDecider::probe(IOService *, SInt32 *)"
+ "virtual bool AppleGenericMultitouchHIDDeviceBase::handleStart(IOService *)"
+ "virtual bool AppleGenericMultitouchHIDDeviceBase::init(OSDictionary *)"
+ "void AppleGenericMultitouchDecider::recordUltimateDecision(bool, bool)"
+ "void AppleGenericMultitouchHIDDeviceBase::setExtraProperties()"
- "12111112122212121112"
- "121111121222121211211122211"
- "1211111212221212112111222111111"

```
