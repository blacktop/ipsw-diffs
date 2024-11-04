## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1218.60.42.502.1
-  __TEXT.__text: 0x40974
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x2ed4
-  __TEXT.__cstring: 0x215b
+1218.60.60.502.1
+  __TEXT.__text: 0x41e00
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_methlist: 0x2f24
+  __TEXT.__cstring: 0x21e5
   __TEXT.__const: 0xaf6
   __TEXT.__gcc_except_tab: 0x508
-  __TEXT.__oslogstring: 0x1743
+  __TEXT.__oslogstring: 0x1845
   __TEXT.__swift5_typeref: 0x1eb
   __TEXT.__swift5_reflstr: 0xd1
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_fieldmd: 0x278
   __TEXT.__swift5_proto: 0x9c
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x1518
+  __TEXT.__unwind_info: 0x15a8
   __TEXT.__eh_frame: 0x2b0
   __TEXT.__objc_classname: 0x626
-  __TEXT.__objc_methname: 0x6611
-  __TEXT.__objc_methtype: 0x1ad0
-  __TEXT.__objc_stubs: 0x4e80
+  __TEXT.__objc_methname: 0x6751
+  __TEXT.__objc_methtype: 0x1b77
+  __TEXT.__objc_stubs: 0x4f80
   __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x1370
+  __DATA_CONST.__const: 0x1438
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1990
+  __DATA_CONST.__objc_selrefs: 0x19e0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x128
-  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__auth_got: 0x4c8
   __AUTH_CONST.__auth_ptr: 0x138
-  __AUTH_CONST.__const: 0x22a0
-  __AUTH_CONST.__cfstring: 0x3340
-  __AUTH_CONST.__objc_const: 0x7108
+  __AUTH_CONST.__const: 0x23c0
+  __AUTH_CONST.__cfstring: 0x33a0
+  __AUTH_CONST.__objc_const: 0x71e8
   __AUTH_CONST.__objc_intobj: 0x150
   __DATA.__objc_ivar: 0x2d4
   __DATA.__data: 0x750
-  __DATA.__bss: 0x1500
+  __DATA.__bss: 0x1510
   __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__data: 0x228
   __DATA_DIRTY.__bss: 0x198

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1808
-  Symbols:   1988
-  CStrings:  2015
+  Functions: 1839
+  Symbols:   2022
+  CStrings:  2041
 
Symbols:
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateFromSelf
+ _eligibilityKey
+ _eligibilityVersionKey
+ _ktEligibilityAnalyticsVersion
+ _os_eligibility_get_domain_answer
- _ktReliabilityAnalyticsVersion
- _reliabilityKey
- _reliabilityVersionKey
CStrings:
+ "@\"NSArray\"16@0:8"
+ "Sending clearEligibilityOverrides:"
+ "Sending clearTapToRadarNotification"
+ "Sending insertResultForElement:"
+ "Sending reportEligibility:complete:"
+ "Sending setOverrideTimeBetweenReports:complete:"
+ "Sending transparencyTriggerMaybeReportEligibility"
+ "clearEligibilityOverrides:"
+ "clearTapToRadarNotification:complete:"
+ "com.apple.networkserviceproxy"
+ "com.apple.transparency"
+ "gmEligibility"
+ "haveContact:complete:"
+ "insertResultForElement:samplesAgo:success:complete:"
+ "ktHasReachedEligibility"
+ "ktHasReachedEligibilityVersion"
+ "ktTTR: error handler %!{(MISSING)public}@"
+ "ktTTR: failed send %!{(MISSING)public}@"
+ "ktTTR: trigger ttr %!{(MISSING)public}@"
+ "reportEligibility:complete:"
+ "sasTTR:toHandle:pushToken:complete:"
+ "setOverrideTimeBetweenReports:completion:"
+ "testingSelfValidationFailing"
+ "transparencyHaveContact:complete:"
+ "transparencyTriggerMaybeReportEligibility:"
+ "transparencyTriggerTTR:handle:complete:"
+ "triggerMaybeReportEligibility:"
+ "ttr:fromHandle:complete:"
+ "v24@?0@\"<TransparencydIDSSupportProtocol>\"8@\"NSError\"16"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?>24"
+ "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "Sending clearReliabilityOverrides:"
- "Sending reportReliability:complete:"
- "clearReliabilityOverrides:"
- "insertResultForElement:daysAgo:success:complete:"
- "ktHasReachedReliability"
- "ktHasReachedReliabilityVersion"
- "reportReliability:complete:"
- "verifyProofs:for:counter:completion:"

```
