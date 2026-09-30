## libCommCenterKCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib`

```diff

-13080.2.0.0.0
-  __TEXT.__text: 0x14a784
+13085.1.0.0.0
+  __TEXT.__text: 0x14aa0c
   __TEXT.__auth_stubs: 0x7e70
   __TEXT.__const: 0x199f9
-  __TEXT.__gcc_except_tab: 0x16304
-  __TEXT.__oslogstring: 0x16014
+  __TEXT.__gcc_except_tab: 0x16310
+  __TEXT.__oslogstring: 0x160d4
   __TEXT.__cstring: 0x4946
   __TEXT.__unwind_info: 0x7838
   __DATA_CONST.__got: 0x468

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 8324AEC6-AFA6-30F5-B91D-5CD030447EA7
+  UUID: 58C69438-95E9-3CDF-9545-35FAA913CEB2
   Functions: 5898
   Symbols:   18905
-  CStrings:  2597
+  CStrings:  2601
 
Functions:
~ __ZN20IBIDataCommandDriverC1ENSt3__110shared_ptrIK8RegistryEEN8dispatch5queueERKNS1_IK15PersonalityInfoEENS1_I21DataInstanceICEClientEENS1_I31BBDataCommandDriverEventHandlerEE : 736 -> 740
~ __ZN20IBIDataCommandDriver21handleBasebandOn_syncEv : 936 -> 1108
~ __ZN20IBIDataCommandDriver37handleIBICallPsBandwidthEstimationIndERN6AriSdk39ARI_IBICallPsBandwidthEstimationInd_SDKE : 904 -> 1212
~ __ZNK20IBIDataCommandDriver26dumpDataCommandDriverStateEv : 2484 -> 2644
~ __ZN27IBIDataFactoryCommandDriver37handleIBICallPsBandwidthEstimationIndEPKhj : 520 -> 524
CStrings:
+ "#E IBICallPsBandwidthEstimationInd without TCP mitigation info"
+ "#I DATA:: \t fTcpMitigationBitmask = %hu"
+ "#I DATA:: \t fUlEmergencyBottleneck = %s"
+ "#I TCP mitigation bitmask change from %hu to %hu"
+ "/AppleInternal/Library/BuildRoots/4~B5YRugAD7WbH4Bzdf6BTzT9W6IrkbyNsjja7GYM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/AppleInternal/Library/BuildRoots/4~B4WhugC4w4xHpqF5sZpSh3QGSpr2Nyu3sHX8cLQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"

```
