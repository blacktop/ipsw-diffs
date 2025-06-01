## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-466.7.12.0.0
-  __TEXT.__text: 0x121754
+466.7.15.0.0
+  __TEXT.__text: 0x122328
   __TEXT.__auth_stubs: 0x1730
-  __TEXT.__objc_stubs: 0x14740
-  __TEXT.__objc_methlist: 0x7684
+  __TEXT.__objc_stubs: 0x148e0
+  __TEXT.__objc_methlist: 0x76a4
   __TEXT.__const: 0x1b50
-  __TEXT.__cstring: 0xafb8
+  __TEXT.__cstring: 0xb068
   __TEXT.__objc_classname: 0x15bc
-  __TEXT.__objc_methname: 0x1c80c
+  __TEXT.__objc_methname: 0x1c9b4
   __TEXT.__objc_methtype: 0x4fee
   __TEXT.__gcc_except_tab: 0x1a30
-  __TEXT.__oslogstring: 0x16b4e
+  __TEXT.__oslogstring: 0x16d3d
   __TEXT.__swift5_typeref: 0xca4
   __TEXT.__swift5_fieldmd: 0x4b4
   __TEXT.__constg_swiftt: 0x814

   __TEXT.__swift5_proto: 0x78
   __TEXT.__swift5_types: 0x7c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x3804
+  __TEXT.__unwind_info: 0x3818
   __TEXT.__eh_frame: 0x2ff0
   __DATA_CONST.__auth_got: 0xba8
-  __DATA_CONST.__got: 0xc78
+  __DATA_CONST.__got: 0xc90
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0xa4e8
-  __DATA_CONST.__cfstring: 0x5d20
+  __DATA_CONST.__const: 0xa558
+  __DATA_CONST.__cfstring: 0x5dc0
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x210
   __DATA.__objc_const: 0x1b700
-  __DATA.__objc_selrefs: 0x5f38
+  __DATA.__objc_selrefs: 0x5fa0
   __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0xa60
+  __DATA.__objc_classrefs: 0xa78
   __DATA.__objc_superrefs: 0x360
   __DATA.__objc_ivar: 0x8d4
   __DATA.__objc_data: 0x4260

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 16EA5569-E9A3-3804-BA9E-8F77B2C9DB98
-  Functions: 5443
-  Symbols:   1050
-  CStrings:  8687
+  UUID: DFC07B8F-3A06-3EE4-BD79-07335849A4CD
+  Functions: 5458
+  Symbols:   1056
+  CStrings:  8720
 
Symbols:
+ _AKBiometricRatchetStateDidChangeNotification
+ _AKFalseValue
+ _AKURLBagKeyDeviceInfo
+ _OBJC_CLASS_$_AKBiometricRatchetController
+ _OBJC_CLASS_$_AKDeviceSafetyRestrictionState
+ _OBJC_CLASS_$_LAStorage
CStrings:
+ "-1"
+ "9"
+ "Error parsing `AKDeviceSafetyRestrictionState`: %{public}@"
+ "Failed to fetch device info with error: %@"
+ "Failed to parse device info JSON for altDSID: %{mask.hash}@"
+ "Fetched device info for %{mask.hash}@"
+ "Fetching Device Info to get device restriction state"
+ "Liveness performed for DTO status change notification"
+ "Ratchet state unexpectly found nil during liveness"
+ "Received DTO status change notification, triggering liveness..."
+ "_fetchDeviceSafetyRestrictionStateForAltDSID:completion:"
+ "_isBiometricRatchetStatusChangeDarwinNotification:"
+ "_updateDeviceListResponseWithDeviceInfo:completion:"
+ "biometricLivenessInLast24Hours"
+ "biometricRatchetEnablementState"
+ "boolForKey:"
+ "com.apple.LocalAuthentication.ratchet.StateDidChange"
+ "currentRachetState"
+ "deviceSafetyRestrictionReasonOverride"
+ "fetchDeviceSafetyState"
+ "fetchDeviceSafetyState set but AuthKit/DTO feature flag is not turned on"
+ "initWithDeviceMID:serialNumber:restrictionReason:"
+ "initWithDomain:authenticationContext:"
+ "initWithResponse:error:"
+ "isDTOEnabled"
+ "rawState"
+ "updateWithDeviceRestrictionState:"
+ "v24@?0@\"AKDeviceSafetyRestrictionState\"8@\"NSError\"16"

```
