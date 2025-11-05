## AMSFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/PlugIns/AMSFollowUpExtension.appex/Contents/MacOS/AMSFollowUpExtension`

```diff

-6.2.33.0.0
-  __TEXT.__text: 0x20fc
+6.4.22.1.4
+  __TEXT.__text: 0x1e50
   __TEXT.__auth_stubs: 0x190
-  __TEXT.__objc_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x1fc
-  __TEXT.__cstring: 0x14a
-  __TEXT.__objc_methname: 0x948
-  __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methtype: 0x1b3
+  __TEXT.__objc_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0x140
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__cstring: 0xcb
+  __TEXT.__objc_methname: 0x56f
   __TEXT.__oslogstring: 0x2ac
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__objc_classname: 0x1c
+  __TEXT.__objc_methtype: 0xb6
+  __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x180
-  __DATA_CONST.__cfstring: 0x1c0
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xbf8
-  __DATA.__objc_selrefs: 0x278
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x180
+  __DATA.__objc_const: 0x1c0
+  __DATA.__objc_selrefs: 0x1e0
+  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3764BA71-3944-3147-887A-BAF15A0E1E71
-  Functions: 59
-  Symbols:   55
-  CStrings:  212
+  UUID: 07C09E8F-8D3B-3173-94D5-405AE59EEDEB
+  Functions: 44
+  Symbols:   51
+  CStrings:  115
 
Symbols:
+ __NSConcreteGlobalBlock
- _OBJC_CLASS_$_AMSBagKeySet
- _OBJC_CLASS_$_AMSFollowUpBag
- _OBJC_CLASS_$_AMSMutableBagKeySet
- _OBJC_CLASS_$_NSObject
- _OBJC_METACLASS_$_AMSFollowUpBag
CStrings:
+ "performActionsWithBag:account:"
+ "postMetricsWithBag:"
- "#16@0:8"
- "@\"<AMSMescalBagContract>\"16@0:8"
- "@\"<AMSMetricsBagContract>\"16@0:8"
- "@\"AMSBag\""
- "@\"AMSBagValue\"16@0:8"
- "@\"NSString\"16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AMSFollowUpBag"
- "AMSMescalBagContract"
- "AMSMetricsBagContract"
- "AMSURLBagContract"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<AMSMescalBagContract>\",?,R"
- "T@\"<AMSMetricsBagContract>\",?,R"
- "T@\"AMSBag\",&,V_bag"
- "T@\"AMSBagValue\",?,R"
- "T@\"AMSBagValue\",R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TFOSamplingPercentage"
- "TFOSamplingSessionDuration"
- "TLSSamplingPercentage"
- "TLSSamplingSessionDuration"
- "TQ,R"
- "URLForKey:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_bagContract"
- "_keySet"
- "addBagKey:valueType:"
- "apsAllowedProductTypes"
- "apsEnabledPatterns"
- "apsSamplingPercent"
- "arrayForKey:"
- "autorelease"
- "bag"
- "class"
- "conformsToProtocol:"
- "debugDescription"
- "description"
- "dictionaryForKey:"
- "guidRegexes"
- "guidSchemes"
- "hash"
- "init"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "mescalCertificateURL"
- "mescalContract"
- "mescalPrimingURL"
- "mescalSetupURL"
- "mescalSignSapRequests"
- "mescalSignSapResponses"
- "mescalSignedActions"
- "metrics"
- "metrics/metricsUrl"
- "metricsContract"
- "metricsDictionary"
- "metricsURL"
- "metricsUrl"
- "performActionsWithContract:account:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postMetricsWithBagContract:"
- "registerBagKeySet:forProfile:profileVersion:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setBag:"
- "sign-sap-request"
- "sign-sap-response"
- "sign-sap-setup"
- "sign-sap-setup-cert"
- "signed-actions"
- "storefrontSuffix"
- "superclass"
- "trustedDomains"
- "zone"

```
