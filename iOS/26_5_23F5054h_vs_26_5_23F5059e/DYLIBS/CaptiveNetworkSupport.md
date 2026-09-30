## CaptiveNetworkSupport

> `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport`

```diff

-514.100.16.0.0
-  __TEXT.__text: 0x30fac
+514.120.2.0.0
+  __TEXT.__text: 0x30fdc
   __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x210
   __TEXT.__oslogstring: 0x594d
   __TEXT.__gcc_except_tab: 0x210
-  __TEXT.__cstring: 0x209a
-  __TEXT.__unwind_info: 0x930
+  __TEXT.__cstring: 0x2099
+  __TEXT.__unwind_info: 0x938
   __TEXT.__objc_classname: 0x8e
   __TEXT.__objc_methname: 0xca9
   __TEXT.__objc_methtype: 0x5a9

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C5C6E031-C7E6-305D-93A6-CEA214A5E020
+  UUID: 22D5A917-6E21-3089-A0D0-00901C55410B
   Functions: 764
   Symbols:   2365
   CStrings:  1599
Symbols:
+ __handleBuiltinEvaluationFailureForCarPlayNetwork
- __handleIPv6OnlyEvaluationFailure
Functions:
~ _CNInfoEvaluating : 3372 -> 3408
~ _CNInfoFailure : 272 -> 276
~ __handleIPv6OnlyEvaluationFailure -> _postNonCaptiveAnalyticsEvent : 200 -> 100
~ _postNonCaptiveAnalyticsEvent -> _SendCleanupCommandToBuiltinPluginIfNecessary : 100 -> 152
~ _SendCleanupCommandToBuiltinPluginIfNecessary -> __handleBuiltinEvaluationFailureForCarPlayNetwork : 152 -> 200
~ _CNInfoInactive : 544 -> 548
~ _CNInfoNetworkActive : 1456 -> 1460
CStrings:
+ "CaptiveNetworkSupport-514.120.2"
- "CaptiveNetworkSupport-514.100.16"

```
