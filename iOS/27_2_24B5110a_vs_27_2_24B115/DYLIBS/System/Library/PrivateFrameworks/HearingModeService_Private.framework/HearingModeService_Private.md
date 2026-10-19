## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

 41.7.0.0.0
-  __TEXT.__text: 0x12604
-  __TEXT.__objc_methlist: 0xc84
+  __TEXT.__text: 0x128c4
+  __TEXT.__objc_methlist: 0xc8c
   __TEXT.__const: 0x86
   __TEXT.__gcc_except_tab: 0x514
-  __TEXT.__cstring: 0x51fa
-  __TEXT.__unwind_info: 0x758
+  __TEXT.__cstring: 0x5351
+  __TEXT.__unwind_info: 0x770
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x858
+  __DATA_CONST.__const: 0x878
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xed0
+  __DATA_CONST.__objc_selrefs: 0xee8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__got: 0x208
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0x14a8

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 461
-  Symbols:   664
-  CStrings:  458
+  Functions: 466
+  Symbols:   666
+  CStrings:  463
 
Symbols:
+ -[HMDeviceManager _hearingAssistEligibleViaTINDomain]
+ GCC_except_table108
+ _OBJC_CLASS_$_OSEligibilityQuery
- GCC_except_table107
CStrings:
+ "### OSEligibility TIN domain query failed: %@"
+ "-[HMDeviceManager _hearingAssistEligibleViaTINDomain]"
+ "HearingAidV2 region status upgraded to Supported via OSEligibility TIN domain (HealthKit reported %s)"
+ "HearingAssist region status upgraded to Supported via OSEligibility TIN domain (HealthKit reported %s)"
+ "OSEligibility TIN domain eligible: %d"
```
