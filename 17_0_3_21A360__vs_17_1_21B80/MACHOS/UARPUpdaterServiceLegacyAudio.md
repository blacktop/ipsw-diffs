## UARPUpdaterServiceLegacyAudio

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio`

```diff

-916.0.46.0.0
-  __TEXT.__text: 0x1f1f4
-  __TEXT.__auth_stubs: 0xa30
+916.40.22.0.2
+  __TEXT.__text: 0x1f4ac
+  __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_stubs: 0x4220
   __TEXT.__objc_methlist: 0x132c
-  __TEXT.__cstring: 0x7e66
+  __TEXT.__cstring: 0x7f7c
   __TEXT.__const: 0x2b8
   __TEXT.__objc_methname: 0x4d2c
   __TEXT.__objc_classname: 0x24e
   __TEXT.__objc_methtype: 0xc8b
-  __TEXT.__oslogstring: 0x60f
+  __TEXT.__oslogstring: 0x6ab
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x708
-  __DATA_CONST.__auth_got: 0x528
+  __TEXT.__unwind_info: 0x710
+  __DATA_CONST.__auth_got: 0x538
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1360
-  __DATA_CONST.__cfstring: 0x6360
+  __DATA_CONST.__const: 0x1398
+  __DATA_CONST.__cfstring: 0x6460
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78

   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 871
-  Symbols:   1017
-  CStrings:  2192
+  Functions: 877
+  Symbols:   1028
+  CStrings:  2205
 
Symbols:
+ _IOPMAssertionCreateWithName
+ _IOPMAssertionRelease
+ _createPowerAssertion
+ _kHWRevisionKey
+ _kSupplementalAssetLocationKey
+ _kSupplementalBasejumperBuildKey
+ _kSupplementalBasejumperTrainKey
+ _kUARPSupportedAccessoryCaseModelNameIdentifier
+ _kUARPSupportedAccessoryKeyPersonalities
+ _kUARPSupportedAccessoryKeyUpdateRequiresPowerAssertion
+ _releasePowerAssertion
CStrings:
+ "%s: Failed to create power assertion %@ with error %d"
+ "%s: Failed to release power assertion with error %d"
+ "%s: Invalid powerAssertionID received from caller"
+ "BOOL createPowerAssertion(NSString *__strong, IOPMAssertionID *)"
+ "BOOL releasePowerAssertion(IOPMAssertionID)"
+ "Case"
+ "DawnB"
+ "Personalities"
+ "PreventUserIdleSystemSleep"
+ "UpdateRequiresPowerAssertion"
+ "hwRevision"
+ "supplementalAssetLocation"
+ "supplementalBasejumperBuild"
+ "supplementalBasejumperTrain"
- "Dawn"

```
