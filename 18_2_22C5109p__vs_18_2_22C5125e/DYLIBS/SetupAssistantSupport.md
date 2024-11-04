## SetupAssistantSupport

> `/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport`

```diff

-507.0.0.0.0
-  __TEXT.__text: 0x121b0
+511.0.0.0.0
+  __TEXT.__text: 0x126fc
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x1490
+  __TEXT.__objc_methlist: 0x14f0
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0xd45
+  __TEXT.__cstring: 0xd8b
   __TEXT.__oslogstring: 0x9c2
   __TEXT.__gcc_except_tab: 0x2a4
   __TEXT.__dlopen_cstrs: 0x5ed
   __TEXT.__unwind_info: 0x438
   __TEXT.__objc_classname: 0x2d7
-  __TEXT.__objc_methname: 0x3d19
-  __TEXT.__objc_methtype: 0x6d6
-  __TEXT.__objc_stubs: 0x3100
-  __DATA_CONST.__got: 0x2d0
+  __TEXT.__objc_methname: 0x3f15
+  __TEXT.__objc_methtype: 0x722
+  __TEXT.__objc_stubs: 0x3180
+  __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__const: 0x820
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xef0
+  __DATA_CONST.__objc_selrefs: 0xf40
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x2e70
+  __AUTH_CONST.__cfstring: 0x1000
+  __AUTH_CONST.__objc_const: 0x2ef0
   __AUTH_CONST.__objc_intobj: 0x60
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0x730

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 538
-  Symbols:   885
-  CStrings:  1091
+  Functions: 546
+  Symbols:   896
+  CStrings:  1107
 
Symbols:
+ OBJC_IVAR_$_SASExpressSettings._stolenDeviceProtectionEnabled
+ OBJC_IVAR_$_SASExpressSettings._stolenDeviceProtectionStrictModeEnabled
+ _OBJC_CLASS_$_LARatchetManager
CStrings:
+ "TB,N,V_stolenDeviceProtectionEnabled"
+ "TB,N,V_stolenDeviceProtectionStrictModeEnabled"
+ "_stolenDeviceProtectionEnabled"
+ "_stolenDeviceProtectionStrictModeEnabled"
+ "hasStolenDeviceProtectionEnabled"
+ "hasStolenDeviceProtectionStrictModeEnabled"
+ "isFeatureEnabled"
+ "isFeatureStrictModeEnabled"
+ "setHasStolenDeviceProtectionEnabled:"
+ "setHasStolenDeviceProtectionStrictModeEnabled:"
+ "setStolenDeviceProtectionEnabled:"
+ "setStolenDeviceProtectionStrictModeEnabled:"
+ "stolenDeviceProtectionEnabled"
+ "stolenDeviceProtectionStrictModeEnabled"
+ "{?=\"appearanceMode\"b1\"displayZoomOption\"b1\"appAnalyticsOptIn\"b1\"deviceAnalyticsOptIn\"b1\"fileVaultEnabled\"b1\"findMyOptIn\"b1\"locationServicesOptIn\"b1\"screenTimeEnabled\"b1\"siriDataSharingOptIn\"b1\"siriOptIn\"b1\"siriVoiceTriggerEnabled\"b1\"softwareUpdateAutoDownloadEnabled\"b1\"softwareUpdateAutoUpdateEnabled\"b1\"stolenDeviceProtectionEnabled\"b1\"stolenDeviceProtectionStrictModeEnabled\"b1\"unlockWithWatchEnabled\"b1}"
- "{?=\"appearanceMode\"b1\"displayZoomOption\"b1\"appAnalyticsOptIn\"b1\"deviceAnalyticsOptIn\"b1\"fileVaultEnabled\"b1\"findMyOptIn\"b1\"locationServicesOptIn\"b1\"screenTimeEnabled\"b1\"siriDataSharingOptIn\"b1\"siriOptIn\"b1\"siriVoiceTriggerEnabled\"b1\"softwareUpdateAutoDownloadEnabled\"b1\"softwareUpdateAutoUpdateEnabled\"b1\"unlockWithWatchEnabled\"b1}"

```
