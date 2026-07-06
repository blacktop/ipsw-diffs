## nfcd

> `/usr/libexec/nfcd`

```diff

-  __TEXT.__text: 0x170f7c
-  __TEXT.__auth_stubs: 0x13b0
+  __TEXT.__text: 0x170f08
+  __TEXT.__auth_stubs: 0x13f0
   __TEXT.__delay_helper: 0x1f4
-  __TEXT.__objc_stubs: 0x9e00
-  __TEXT.__objc_methlist: 0x7518
-  __TEXT.__const: 0x10ac
-  __TEXT.__cstring: 0x1895e
-  __TEXT.__oslogstring: 0x184b0
-  __TEXT.__objc_classname: 0x14d3
-  __TEXT.__objc_methname: 0x1098e
-  __TEXT.__objc_methtype: 0x3d6c
-  __TEXT.__unwind_info: 0x1e48
-  __DATA_CONST.__const: 0x6d60
-  __DATA_CONST.__cfstring: 0xec60
-  __DATA_CONST.__objc_classlist: 0x4c0
+  __TEXT.__objc_stubs: 0x9ee0
+  __TEXT.__objc_methlist: 0x7598
+  __TEXT.__const: 0x10cc
+  __TEXT.__cstring: 0x18769
+  __TEXT.__oslogstring: 0x18567
+  __TEXT.__objc_classname: 0x14f5
+  __TEXT.__objc_methname: 0x10a14
+  __TEXT.__objc_methtype: 0x3d9e
+  __TEXT.__unwind_info: 0x1e58
+  __DATA_CONST.__const: 0x6d70
+  __DATA_CONST.__cfstring: 0xe920
+  __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x328
+  __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_intobj: 0x5ef8
   __DATA_CONST.__objc_arraydata: 0x1a20
   __DATA_CONST.__objc_dictobj: 0xbe0
   __DATA_CONST.__objc_arrayobj: 0x138
-  __DATA_CONST.__auth_got: 0x9e0
-  __DATA_CONST.__got: 0x598
-  __DATA.__objc_const: 0xfe70
-  __DATA.__objc_selrefs: 0x3a78
-  __DATA.__objc_ivar: 0xcd0
-  __DATA.__objc_data: 0x2f80
+  __DATA_CONST.__auth_got: 0xa00
+  __DATA_CONST.__got: 0x708
+  __DATA.__objc_const: 0x100e0
+  __DATA.__objc_selrefs: 0x3a68
+  __DATA.__objc_ivar: 0xcf8
+  __DATA.__objc_data: 0x3020
   __DATA.__data: 0x1df4
-  __DATA.__bss: 0x1e0
+  __DATA.__bss: 0x200
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AppletTranslationFramework.framework/Versions/A/AppletTranslationFramework
+  - /System/Library/PrivateFrameworks/CoreTime.framework/Versions/A/CoreTime
   - /System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/Versions/A/NearFieldPrivateServices
   - /System/Library/PrivateFrameworks/STSXPCHelperClient.framework/Versions/A/STSXPCHelperClient
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3103
-  Symbols:   505
-  CStrings:  10902
+  Functions: 3115
+  Symbols:   509
+  CStrings:  10868
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _NSSystemClockDidChangeNotification
+ _TMGetReferenceTime
+ _TMIsAutomaticTimeEnabled
+ _mach_timebase_info
- _OBJC_CLASS_$_NSAssertionHandler
CStrings:
+ "%{public}s:%i Could not get reference time"
+ "%{public}s:%i Fetched reference time interval: %.3f, user delta: %.3f, uncertainty: %.3f"
+ "%{public}s:%i pause=%{public}d, suspendFD=%{public}d, fdSuspended=%{public}d"
+ "-[NFTrustedTimeSource getTime]"
+ "-[NFTrustedTimeSource handleSystemTimeChanged:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "@40@0:8@16d24Q32"
+ "NFCD built from (B&I) Stockholm_Base-370.38.2"
+ "NFTrustedTime"
+ "NFTrustedTimeSource"
+ "Unexpected state : unknown"
+ "_cachedReferenceAbsTimeSec"
+ "_cachedReferenceMachTimeSec"
+ "_date"
+ "_fieldDetectSuspended"
+ "_monotonicCounterSeconds"
+ "_observerRegistered"
+ "_refreshTimeSyncSetting:"
+ "_timeSyncSettingCacheTime"
+ "_timeSyncedWithAutoTimeEnabled"
+ "_updateCachedAbsTime:machTime:"
+ "addObserver:selector:name:object:"
+ "convertMachContinuousTicksToSeconds:"
+ "d16@0:8"
+ "d24@0:8Q16"
+ "handleSystemTimeChanged:"
+ "initWithDate:monotonicCounterSeconds:source:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "machContinuousTimeSeconds"
+ "removeObserver:"
+ "timeIntervalSinceReferenceDate"
+ "v32@0:8d16d24"
- "%{public}s:%i pause=%{public}d, suspendFD=%{public}d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "Empty dictionary"
- "Expects card type to *not* be NFCardTypeNone"
- "Failed to initialize nonce"
- "Invalid argument"
- "Invalid parameter not satisfying: %@"
- "NFApplet.m"
- "NFCD built from (B&I) Stockholm_Base-370.37"
- "NFDriverWrapper+RFConfig.m"
- "NFDriverWrapper+SE.m"
- "NFDriverWrapper.m"
- "NFFieldNotification.m"
- "NFLoyaltyAgent.m"
- "NFRoutingConfig.m"
- "NFSecureElementHandle.m"
- "NFSecureElementWrapper+ContactlessRegistry.m"
- "Polling mask invalid"
- "Session over released"
- "Tag Discovery cannot be empty"
- "Unexpected config: %@"
- "Unexpected state %u"
- "_NFContactlessSession.m"
- "_appletCollection!=nil"
- "_driver != nil"
- "_handleOseSelect:"
- "closeSession:"
- "crs_authorizeForECommerce:cryptogram:encryptedPIN:request:response:"
- "currentHandler"
- "driver not open"
- "driver session not held"
- "embeddedCardEmulationWithHCE:emulationType:"
- "embeddedExpressCardEmulation:"
- "getControllerInfo:"
- "getRFSettings:"
- "getSecureElementInfo:info:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "setPollingMask:tagConfig:"
- "setSecureElement:alwaysOn:"
- "theResponse != nil"

```
