## FamilyCircle

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle`

```diff

-250.0.0.0.0
-  __TEXT.__text: 0xa8ae4
+251.1.0.0.0
+  __TEXT.__text: 0xa933c
   __TEXT.__auth_stubs: 0x24d0
-  __TEXT.__objc_methlist: 0x39bc
+  __TEXT.__objc_methlist: 0x39dc
   __TEXT.__const: 0x6ea8
-  __TEXT.__gcc_except_tab: 0x4b4
-  __TEXT.__cstring: 0x5e96
-  __TEXT.__oslogstring: 0x422f
+  __TEXT.__gcc_except_tab: 0x514
+  __TEXT.__cstring: 0x5ef6
+  __TEXT.__oslogstring: 0x431f
   __TEXT.__dlopen_cstrs: 0x1a6
   __TEXT.__swift5_typeref: 0x2168
   __TEXT.__constg_swiftt: 0x21b8

   __TEXT.__swift_as_entry: 0x184
   __TEXT.__swift_as_ret: 0x1c8
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__unwind_info: 0x3508
+  __TEXT.__unwind_info: 0x3518
   __TEXT.__eh_frame: 0x4df0
-  __TEXT.__objc_classname: 0x965
-  __TEXT.__objc_methname: 0xa484
-  __TEXT.__objc_methtype: 0x1728
-  __TEXT.__objc_stubs: 0x4f00
+  __TEXT.__objc_classname: 0x968
+  __TEXT.__objc_methname: 0xa550
+  __TEXT.__objc_methtype: 0x17a8
+  __TEXT.__objc_stubs: 0x4f40
   __DATA_CONST.__got: 0x9e0
-  __DATA_CONST.__const: 0x1720
+  __DATA_CONST.__const: 0x1770
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2620
+  __DATA_CONST.__objc_selrefs: 0x2630
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x170
   __AUTH_CONST.__auth_got: 0x1278
   __AUTH_CONST.__const: 0x5608
-  __AUTH_CONST.__cfstring: 0x3da0
-  __AUTH_CONST.__objc_const: 0xbd80
+  __AUTH_CONST.__cfstring: 0x3dc0
+  __AUTH_CONST.__objc_const: 0xbdb8
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x1018
   __AUTH.__data: 0x10b8
-  __DATA.__objc_ivar: 0x420
+  __DATA.__objc_ivar: 0x424
   __DATA.__data: 0x2280
   __DATA.__bss: 0x9e60
   __DATA.__common: 0x70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DD90D1D0-DDD3-35DC-9974-CFF8265164A9
-  Functions: 4701
-  Symbols:   6427
-  CStrings:  3796
+  UUID: EBFACD2B-D248-374B-AEEA-50A4F86FF149
+  Functions: 4708
+  Symbols:   6449
+  CStrings:  3808
 
Symbols:
+ -[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]
+ -[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:].cold.1
+ -[FAAgeRangeResponse initWithLowerbound:upperbound:validationLevel:response:parentalControlsInformation:isSharingNewInformation:]
+ -[FAAgeRangeResponse isSharingNewInformation]
+ GCC_except_table54
+ _OBJC_IVAR_$_FAAgeRangeResponse._isSharingNewInformation
+ ___121-[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]_block_invoke
+ ___121-[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]_block_invoke.49
+ ___121-[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]_block_invoke.49.cold.1
+ ___121-[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]_block_invoke.50
+ ___121-[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]_block_invoke.50.cold.1
+ ___block_descriptor_40_e8_32bs_e40_v24?0"FAAgeRangeResponse"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32bs40r_e40_v24?0"FAAgeRangeResponse"8"NSError"16lr40l8s32l8
+ _objc_msgSend$isSharingNewInformation
+ _objc_msgSend$requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:
- -[FAAgeRangeResponse initWithLowerbound:upperbound:validationLevel:response:parentalControlsInformation:]
CStrings:
+ "@60@0:8@16@24q32q40@48B56"
+ "Age Range response with lowerbound: %@, upperbound: %@, validationLevel: %@ , response: %@, parentalControlsInformation: %@, isSharingNewInformation: %@"
+ "Error requesting age range from daemon: %@."
+ "FamilyCircle daemon connection for requestAgeRange returned an error: %@."
+ "Requesting age range from daemon with parameters: ages=%@, bundleID=%@, appName=%@"
+ "TB,R,N,V_isSharingNewInformation"
+ "_isSharingNewInformation"
+ "initWithLowerbound:upperbound:validationLevel:response:parentalControlsInformation:isSharingNewInformation:"
+ "isSharingNewInformation"
+ "requestAgeRange with response: %@."
+ "requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:"
+ "v24@?0@\"FAAgeRangeResponse\"8@\"NSError\"16"
+ "v72@0:8@\"NSArray\"16@\"NSNumber\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSNumber\"56@?<v@?@\"FAAgeRangeResponse\"@\"NSError\">64"
- "@56@0:8@16@24q32q40@48"
- "Age Range response with lowerbound: %@, upperbound: %@, validationLevel: %@ , response: %@, parentalControlsInformation: %@"
- "initWithLowerbound:upperbound:validationLevel:response:parentalControlsInformation:"

```
