## libAppleSSEExt.dylib

> `/usr/lib/libAppleSSEExt.dylib`

```diff

-297.0.0.0.0
-  __TEXT.__text: 0x28c0
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x98
-  __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0xf7
-  __TEXT.__oslogstring: 0x27a
-  __TEXT.__unwind_info: 0x108
+302.100.2.0.0
+  __TEXT.__text: 0x3fdc
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__objc_methlist: 0xbc
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0xd4
+  __TEXT.__cstring: 0x19b
+  __TEXT.__oslogstring: 0x536
+  __TEXT.__unwind_info: 0x138
   __TEXT.__objc_classname: 0x13
-  __TEXT.__objc_methname: 0x3ff
-  __TEXT.__objc_methtype: 0x74
-  __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x150
+  __TEXT.__objc_methname: 0x38d
+  __TEXT.__objc_methtype: 0x87
+  __TEXT.__objc_stubs: 0x480
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1f0
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x140
+  __DATA_CONST.__objc_arraydata: 0x30
+  __AUTH_CONST.__auth_got: 0x1a8
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x148
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x4
-  __DATA.__bss: 0x18
+  __DATA.__data: 0x18
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 45
-  Symbols:   155
-  CStrings:  86
+  Functions: 83
+  Symbols:   174
+  CStrings:  101
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSUserDefaults
+ _ccdigest
+ _ccsha256_di
- _CFStringCreateWithCString
- _IOObjectRelease
- _IORegistryEntryCreateCFProperty
- _IORegistryEntryFromPath
- _MobileActivationErrorDomain
- _OBJC_CLASS_$_NSKeyedUnarchiver
- _OBJC_CLASS_$_NSMutableData
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSString
- _SecCertificateCreateWithBytes
- _SecCertificateIsValid
- _SecItemCopyMatching
- _SecItemDelete
- _kIOMasterPortDefault
- _kSecAttrAccessGroup
- _kSecAttrLabel
- _kSecAttrService
- _kSecClass
- _kSecClassGenericPassword
- _kSecReturnData
- _mobileactivationErrorHasDomainAndErrorCode
- _objc_alloc
- _objc_autoreleaseReturnValue
CStrings:
+ "!error"
+ ","
+ "/Library/Caches/com.apple.xbs/Sources/AppleSSE/AppleSSElib/baaSupport.m"
+ "0"
+ "AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n"
+ "B16@0:8"
+ "DeviceIdentityIssueClientCertificateWithCompletion(attempt = %u) failed: %@"
+ "Forced delete of existing certificates"
+ "Forcing certificate issuance failure (attempt = %u)"
+ "[issuedCertificates count] > 0"
+ "_delegate"
+ "attestation"
+ "boolValue"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertDeleteOnStart=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertForcedFailures=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertRenewPeriod=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertRenewPeriodRatio=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertRetryPeriods=%@"
+ "cacheConfiguration: using NSUserDefaults value sseBAACertValidity=%@"
+ "cacheConfiguration: validity=%llu, renewPeriod=%llu, renewPeriodRatio=%u, retryPeriods=(%@), forcedFailures=%u, deleteOnStart=%u"
+ "certificateRenewPeriod: renewPeriod=%llu, renewPeriodRatio=%u, x=%f, computedRenewPeriod=%llu"
+ "certificates"
+ "componentsJoinedByString:"
+ "err == 0 "
+ "expirationDate"
+ "i20@0:8B16"
+ "isActive"
+ "isEqualToDate:"
+ "networkReachability"
+ "numberWithUnsignedLongLong:"
+ "objectForKey:"
+ "prepareLazily"
+ "prepareLazily:"
+ "pubKey"
+ "reachability"
+ "res"
+ "scheduleBAACertificateIssuanceRetryTimer(): attempt:%u, interval:%u, scheduled to %@"
+ "sseBAACertDeleteOnStart"
+ "sseBAACertForcedFailures"
+ "sseBAACertRenewPeriodRatio"
+ "sseBAACertRetryPeriods"
+ "standardUserDefaults"
+ "unsignedLongValue"
+ "v32@?0^{__SecKey=}8@\"NSArray\"16@\"NSError\"24"
- " "
- "="
- "BAACertificates"
- "BAAExpDate"
- "BAAKey"
- "BAASigKey"
- "BAAVersion"
- "DeviceIdentityIssueClientCertificateWithCompletion(attempt = %u, networkFailCount = %u) failed: %@"
- "IODeviceTree:/options"
- "_strictlyUnarchivedObjectOfClasses:fromData:error:"
- "boot-args"
- "bytes"
- "com.apple.applesse"
- "componentsSeparatedByString:"
- "date"
- "dateByAddingTimeInterval:"
- "dictionaryWithDictionary:"
- "initWithData:encoding:"
- "integerValue"
- "length"
- "networkReachabilityHandler(): Re-check scheduled to %@ (networkFailCount = %u)"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "scheduleBAACertificateIssuanceRetryTimer(): scheduled to %@"
- "setValue:forKey:"
- "setWithObjects:"
- "unarchivedObjectOfClasses() -> %@"
- "unsignedIntegerValue"
- "v32@?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8@\"NSArray\"16@\"NSError\"24"

```
