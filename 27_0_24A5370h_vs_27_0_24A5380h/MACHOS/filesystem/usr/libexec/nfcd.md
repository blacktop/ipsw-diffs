## nfcd

> `/usr/libexec/nfcd`

```diff

-  __TEXT.__text: 0x1e5bf4
-  __TEXT.__auth_stubs: 0x1820
+  __TEXT.__text: 0x1e677c
+  __TEXT.__auth_stubs: 0x1860
   __TEXT.__delay_stubs: 0x500
   __TEXT.__delay_helper: 0x16f4
-  __TEXT.__objc_stubs: 0xdde0
-  __TEXT.__objc_methlist: 0x9cd4
-  __TEXT.__const: 0x13bc
-  __TEXT.__cstring: 0x2287e
-  __TEXT.__oslogstring: 0x2016b
-  __TEXT.__objc_classname: 0x1d22
-  __TEXT.__objc_methname: 0x157d0
-  __TEXT.__objc_methtype: 0x4de2
-  __TEXT.__unwind_info: 0x2c30
-  __DATA_CONST.__const: 0x9a18
-  __DATA_CONST.__cfstring: 0x11760
-  __DATA_CONST.__objc_classlist: 0x640
+  __TEXT.__objc_stubs: 0xdf20
+  __TEXT.__objc_methlist: 0x9d6c
+  __TEXT.__const: 0x144c
+  __TEXT.__cstring: 0x226d3
+  __TEXT.__oslogstring: 0x2038d
+  __TEXT.__objc_classname: 0x1d44
+  __TEXT.__objc_methname: 0x1585d
+  __TEXT.__objc_methtype: 0x4dfe
+  __TEXT.__unwind_info: 0x2c50
+  __DATA_CONST.__const: 0x9a00
+  __DATA_CONST.__cfstring: 0x112a0
+  __DATA_CONST.__objc_classlist: 0x650
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x388
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1d8
-  __DATA_CONST.__objc_superrefs: 0x470
-  __DATA_CONST.__objc_intobj: 0x7bc0
+  __DATA_CONST.__objc_superrefs: 0x480
+  __DATA_CONST.__objc_intobj: 0x7bf0
   __DATA_CONST.__objc_arraydata: 0x1e38
   __DATA_CONST.__objc_dictobj: 0x1018
   __DATA_CONST.__objc_arrayobj: 0x318
-  __DATA_CONST.__auth_got: 0xcb8
-  __DATA_CONST.__got: 0x838
+  __DATA_CONST.__auth_got: 0xcd8
+  __DATA_CONST.__got: 0x9f8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x14bd8
-  __DATA.__objc_selrefs: 0x4b78
-  __DATA.__objc_ivar: 0x1104
-  __DATA.__objc_data: 0x3e80
+  __DATA.__objc_const: 0x14e48
+  __DATA.__objc_selrefs: 0x4b60
+  __DATA.__objc_ivar: 0x112c
+  __DATA.__objc_data: 0x3f20
   __DATA.__data: 0x2b34
-  __DATA.__bss: 0x2a0
+  __DATA.__bss: 0x2c0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
+  - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4257
-  Symbols:   666
-  CStrings:  13853
+  Functions: 4269
+  Symbols:   669
+  CStrings:  13801
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _NSSystemClockDidChangeNotification
+ _TMGetReferenceTime
+ _TMIsAutomaticTimeEnabled
+ _mach_timebase_info
- _OBJC_CLASS_$_LSApplicationRecord
- _OBJC_CLASS_$_NSAssertionHandler
CStrings:
+ "%{public}s:%i Cannot add receipt for %{public}@/%{public}@"
+ "%{public}s:%i Could not get reference time"
+ "%{public}s:%i Failed to start wired mode to validate key %{public}@ on applet %{public}@"
+ "%{public}s:%i Fetched reference time interval: %.3f, user delta: %.3f, uncertainty: %.3f"
+ "%{public}s:%i Invalid key identifier format: %{public}@"
+ "%{public}s:%i Key %{public}@ not provisioned on applet %{public}@ - rejecting early (err=%{public}@)"
+ "%{public}s:%i Untrusted time source, need to query server"
+ "%{public}s:%i pause=%{public}d, suspendFD=%{public}d, fdSuspended=%{public}d"
+ "-[NFPaymentTagReaderDeveloperPresentmentLogger checkAvailabilityForBundleID:teamID:completion:]"
+ "-[NFPaymentTagReaderDeveloperPresentmentReporter _getFirstReportForBundleID:teamID:olderThanTimestampDay:]"
+ "-[NFPaymentTagReaderDeveloperPresentmentReporter checkLocalAvailabilityForBundleID:teamID:]"
+ "-[NFTrustedTimeSource getTime]"
+ "-[NFTrustedTimeSource handleSystemTimeChanged:]"
+ "-[_NFUnifiedAccessSession setActiveApplets:keyIdentifiers:activationConfig:]"
+ "-[_NFUnifiedAccessSession setActiveKeys:onApplet:activationConfig:]"
+ "@40@0:8@16d24Q32"
+ "Customer Factory Page"
+ "NFCD built from (B&I) Stockholm_Base-370.38.2"
+ "NFTrustedTime"
+ "NFTrustedTimeSource"
+ "Unexpected state : unknown"
+ "_cachedReferenceAbsTimeSec"
+ "_cachedReferenceMachTimeSec"
+ "_fieldDetectSuspended"
+ "_getFirstReportForBundleID:teamID:olderThanTimestampDay:"
+ "_monotonicCounterSeconds"
+ "_observerRegistered"
+ "_refreshTimeSyncSetting:"
+ "_timeSyncSettingCacheTime"
+ "_timeSyncedWithAutoTimeEnabled"
+ "_updateCachedAbsTime:machTime:"
+ "addObserver:selector:name:object:"
+ "convertMachContinuousTicksToSeconds:"
+ "d24@0:8Q16"
+ "fetchDeveloperPaymentReportsForBundleID:teamID:outError:"
+ "handleSystemTimeChanged:"
+ "initWithDate:monotonicCounterSeconds:source:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "machContinuousTimeSeconds"
+ "removeObserver:"
+ "timeIntervalSinceReferenceDate"
+ "timestampDay"
+ "v32@0:8d16d24"
- "%{public}s:%i pause=%{public}d, suspendFD=%{public}d"
- "-[NFPaymentTagReaderDeveloperPresentmentReporter _checkLocalAvailabilityForBundleID:teamID:]"
- "Empty dictionary"
- "Expects card type to *not* be NFCardTypeNone"
- "Failed to initialize nonce"
- "I32@0:8@16@24"
- "Invalid"
- "Invalid argument"
- "Invalid parameter not satisfying: %@"
- "Missing task ref"
- "NFApplet.m"
- "NFCD built from (B&I) Stockholm_Base-370.37"
- "NFDriverWrapper+Fury.m"
- "NFDriverWrapper+RFConfig.m"
- "NFDriverWrapper+SE.m"
- "NFDriverWrapper.m"
- "NFFieldNotification.m"
- "NFLoyaltyAgent.m"
- "NFReaderRestrictor.m"
- "NFRoutingConfig.m"
- "NFSecureElementHandle.m"
- "NFSecureElementWrapper+ContactlessRegistry.m"
- "NFWalletPresentationEntitlement.m"
- "Not implemented"
- "Polling mask invalid"
- "Session over released"
- "Tag Discovery cannot be empty"
- "Tag not handle!"
- "Unexpected class"
- "Unexpected config: %@"
- "Unexpected state %u"
- "_NFContactlessSession.m"
- "_NFReaderSession+Entitlement.m"
- "_NFSecureTransactionServicesHandoverHybridSession.m"
- "_NFSecureTransactionServicesHandoverSession.m"
- "_appletCollection!=nil"
- "_checkLocalAvailabilityForBundleID:teamID:"
- "_driver != nil"
- "_handleOseSelect:"
- "clearMultiTagPollingState"
- "closeSession:"
- "configureMultiTagPolling"
- "crs_authorizeForECommerce:cryptogram:encryptedPIN:request:response:"
- "currentHandler"
- "driver not open"
- "driver session not held"
- "embeddedCardEmulationWithHCE:emulationType:"
- "embeddedExpressCardEmulation:"
- "entitlementFromXPC:"
- "getControllerInfo:"
- "getRFSettings:"
- "getSecureElementInfo:info:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "setPollingMask:tagConfig:"
- "setSecureElement:alwaysOn:"
- "theResponse != nil"

```
