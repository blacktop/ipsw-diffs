## libAppleSSEExt.dylib

> `/usr/lib/libAppleSSEExt.dylib`

```diff

-297.0.0.0.0
-  __TEXT.__text: 0x2128
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x98
+302.100.2.0.0
+  __TEXT.__text: 0x253c
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__objc_methlist: 0xbc
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__cstring: 0xdc
-  __TEXT.__oslogstring: 0x22a
+  __TEXT.__cstring: 0x11d
+  __TEXT.__oslogstring: 0x4cf
   __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0x13
-  __TEXT.__objc_methname: 0x375
-  __TEXT.__objc_methtype: 0x74
-  __TEXT.__objc_stubs: 0x420
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__objc_methname: 0x397
+  __TEXT.__objc_methtype: 0x87
+  __TEXT.__objc_stubs: 0x480
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x148
+  __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1c0
-  __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x80
+  __DATA_CONST.__objc_arraydata: 0x30
+  __AUTH_CONST.__auth_got: 0x198
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x148
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x4
-  __DATA.__bss: 0x68
+  __DATA.__data: 0x20
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E571407-B595-3364-ADEE-1CAFF4646304
-  Functions: 42
-  Symbols:   211
-  CStrings:  76
+  UUID: DB4F4394-E2A6-3EB1-B621-9EBDC6640E18
+  Functions: 44
+  Symbols:   206
+  CStrings:  94
 
Symbols:
+ +[BAASupport prepareLazily:]
+ +[BAASupport prepareLazily]
+ -[Timer isActive]
+ GCC_except_table17
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSUserDefaults
+ __28+[BAASupport prepareLazily:]_block_invoke.14
+ __28+[BAASupport prepareLazily:]_block_invoke.cold.1
+ __28+[BAASupport prepareLazily:]_block_invoke.cold.2
+ ___28+[BAASupport prepareLazily:]_block_invoke
+ ___28+[BAASupport prepareLazily:]_block_invoke_2
+ __block_literal_global.20
+ __block_literal_global.22
+ __block_literal_global.76
+ __block_literal_global.78
+ __block_literal_global.84
+ __block_literal_global.87
+ __block_literal_global.89
+ __block_literal_global.92
+ __cfgBaaCertDeleteOnStart
+ __cfgBaaCertForcedFailures
+ __cfgBaaCertRenewPeriod
+ __cfgBaaCertRenewPeriodRatio
+ __cfgBaaCertRetryPeriods
+ __cfgBaaCertValidity
+ __scheduleBAACertificateIssuanceRetryTimer_block_invoke.85
+ __scheduleBAACertificateRenewalTimer_block_invoke.90
+ _ccdigest
+ _ccsha256_di
+ _objc_msgSend$boolValue
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$isActive
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$prepareLazily
+ _objc_msgSend$prepareLazily:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedLongValue
+ certificateRenewPeriod.computedForCertExpDate
+ certificateRenewPeriod.computedRenewPeriod
+ isDeviceReadyToIssueCertificate.cold.1
+ isDeviceReadyToIssueCertificate.cold.2
- GCC_except_table14
- _CFStringCreateWithCString
- _IOObjectRelease
- _IORegistryEntryCreateCFProperty
- _IORegistryEntryFromPath
- _MobileActivationErrorDomain
- _OBJC_CLASS_$_NSString
- ___21+[BAASupport prepare]_block_invoke
- ___21+[BAASupport prepare]_block_invoke_2
- ___21+[BAASupport prepare]_block_invoke_3
- ___getBootArgs_block_invoke
- __baaCertExpDate
- __baaCertIssueLock
- __baaCertIssueNetworkFailTime
- __baaCertPrepareLock
- __baaCertRetryPeriods
- __baaNetworkRetryTimer
- __baaRenewalTimer
- __block_literal_global.14
- __block_literal_global.19
- __block_literal_global.37
- __block_literal_global.39
- __block_literal_global.42
- __block_literal_global.55
- __block_literal_global.63
- __block_literal_global.66
- __block_literal_global.68
- __block_literal_global.71
- __delegate
- __networkReachabilityHandler_block_invoke.40
- __scheduleBAACertificateIssuanceRetryTimer_block_invoke.64
- __scheduleBAACertificateRenewalTimer_block_invoke.69
- _certificateValidity
- _getNumberFromBootArgs
- _kIOMasterPortDefault
- _mobileactivationErrorHasDomainAndErrorCode
- _objc_alloc
- _objc_autoreleaseReturnValue
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$date
- _objc_msgSend$dateByAddingTimeInterval:
- _objc_msgSend$initWithData:encoding:
- _objc_msgSend$integerValue
- _objc_msgSend$isEqualToString:
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$unsignedIntegerValue
- getBootArgs.bootArgs
- getBootArgs.onceToken
- prepare.onceToken
CStrings:
+ ","
+ "B16@0:8"
+ "DeviceIdentityIssueClientCertificateWithCompletion(attempt = %u) failed: %@"
+ "Forced delete of existing certificates"
+ "Forcing certificate issuance failure (attempt = %u)"
+ "boolValue"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertDeleteOnStart=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertForcedFailures=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertRenewPeriod=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertRenewPeriodRatio=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertRetryPeriods=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertValidity=%@"
+ "cacheConfiguration: validity=%llu, renewPeriod=%llu, renewPeriodRatio=%u, retryPeriods=(%@), forcedFailures=%u, deleteOnStart=%u"
+ "certificateRenewPeriod: renewPeriod=%llu, renewPeriodRatio=%u, x=%f, computedRenewPeriod=%llu"
+ "componentsJoinedByString:"
+ "i20@0:8B16"
+ "isActive"
+ "isEqualToDate:"
+ "numberWithUnsignedLongLong:"
+ "objectForKey:"
+ "prepareLazily"
+ "prepareLazily:"
+ "scheduleBAACertificateIssuanceRetryTimer(): attempt:%u, interval:%u, scheduled to %@"
+ "sseBAACertDeleteOnStart"
+ "sseBAACertForcedFailures"
+ "sseBAACertRenewPeriodRatio"
+ "sseBAACertRetryPeriods"
+ "standardUserDefaults"
+ "unsignedIntValue"
+ "unsignedLongValue"
- " "
- "="
- "DeviceIdentityIssueClientCertificateWithCompletion(attempt = %u, networkFailCount = %u) failed: %@"
- "IODeviceTree:/options"
- "boot-args"
- "componentsSeparatedByString:"
- "date"
- "dateByAddingTimeInterval:"
- "initWithData:encoding:"
- "integerValue"
- "isEqualToString:"
- "networkReachabilityHandler(): Re-check scheduled to %@ (networkFailCount = %u)"
- "numberWithInteger:"
- "scheduleBAACertificateIssuanceRetryTimer(): scheduled to %@"
- "unsignedIntegerValue"

```
