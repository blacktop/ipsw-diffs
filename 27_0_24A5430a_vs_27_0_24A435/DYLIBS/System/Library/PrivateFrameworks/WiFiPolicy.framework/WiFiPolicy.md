## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

 1070.62.0.0.0
-  __TEXT.__text: 0xe2d8c
+  __TEXT.__text: 0xe2dbc
   __TEXT.__objc_methlist: 0x13d18
   __TEXT.__const: 0x868
-  __TEXT.__cstring: 0x25d0b
+  __TEXT.__cstring: 0x25d4b
   __TEXT.__oslogstring: 0x550e
   __TEXT.__gcc_except_tab: 0x190c
   __TEXT.__dlopen_cstrs: 0xa8

   __DATA_CONST.__objc_arraydata: 0x1510
   __DATA_CONST.__got: 0xbb8
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x20dc0
+  __AUTH_CONST.__cfstring: 0x20de0
   __AUTH_CONST.__objc_const: 0x25980
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x1aa0

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 7206
   Symbols:   15647
-  CStrings:  5322
+  CStrings:  5323
 
Functions:
~ _OUTLINED_FUNCTION_3 : 20 -> 12
~ sub_20316b3a4 -> sub_2037e839c : 256 -> 264
~ -[WFMeasure initWithType:andReason:prevTestedOptions:prevTestedTrafficClass:andInterfaceName:] : 1572 -> 1560
~ _OUTLINED_FUNCTION_2 : 12 -> 20
~ -[WiFiAirplaneLandingDetectorAnalytics buildAnalyticsEventDictionary:state:isAssociated:] : 1060 -> 1064
~ -[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:] : 932 -> 964
~ __ZNSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE6resizeEm : 300 -> 308
~ -[WiFiUsagePoorLinkSession roamCacheDidUpdate:] : 936 -> 940
~ -[WiFiUsageSession _generateState] : 984 -> 988
CStrings:
+ "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
```
