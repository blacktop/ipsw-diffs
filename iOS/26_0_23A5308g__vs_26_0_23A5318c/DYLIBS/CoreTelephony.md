## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13090.3.0.0.0
-  __TEXT.__text: 0x18f068
+13091.1.6.0.0
+  __TEXT.__text: 0x192214
   __TEXT.__auth_stubs: 0x1990
-  __TEXT.__objc_methlist: 0x1b464
+  __TEXT.__objc_methlist: 0x1b76c
   __TEXT.__const: 0x1002
-  __TEXT.__gcc_except_tab: 0x1df98
-  __TEXT.__cstring: 0x1f851
-  __TEXT.__oslogstring: 0x43e5
+  __TEXT.__gcc_except_tab: 0x1e524
+  __TEXT.__cstring: 0x1fa3f
+  __TEXT.__oslogstring: 0x43ef
   __TEXT.__swift5_typeref: 0x17
-  __TEXT.__unwind_info: 0xd1f8
-  __TEXT.__objc_classname: 0x592f
-  __TEXT.__objc_methname: 0x22ca1
-  __TEXT.__objc_methtype: 0x72e4
-  __TEXT.__objc_stubs: 0x16d40
-  __DATA_CONST.__got: 0xb00
-  __DATA_CONST.__const: 0x7398
-  __DATA_CONST.__objc_classlist: 0x1530
+  __TEXT.__unwind_info: 0xd428
+  __TEXT.__objc_classname: 0x5a20
+  __TEXT.__objc_methname: 0x22fee
+  __TEXT.__objc_methtype: 0x7322
+  __TEXT.__objc_stubs: 0x16f60
+  __DATA_CONST.__got: 0xb08
+  __DATA_CONST.__const: 0x73c8
+  __DATA_CONST.__objc_classlist: 0x1568
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x77f8
+  __DATA_CONST.__objc_selrefs: 0x78b8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x17b0
+  __DATA_CONST.__objc_superrefs: 0x1810
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0xce0
-  __AUTH_CONST.__const: 0x2080
-  __AUTH_CONST.__cfstring: 0x1dbe0
-  __AUTH_CONST.__objc_const: 0x2f928
+  __AUTH_CONST.__const: 0x20c0
+  __AUTH_CONST.__cfstring: 0x1ddc0
+  __AUTH_CONST.__objc_const: 0x2fdc0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xaa50
-  __DATA.__objc_ivar: 0x1438
+  __AUTH.__objc_data: 0xac80
+  __DATA.__objc_ivar: 0x1440
   __DATA.__data: 0x1f88
   __DATA.__bss: 0x198
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 71DEA278-D71D-3B01-81FD-FA2F7072973F
-  Functions: 11284
-  Symbols:   38281
-  CStrings:  17133
+  UUID: E5175999-D6B6-35E0-8467-382532AF7EEF
+  Functions: 11358
+  Symbols:   38534
+  CStrings:  17203
 
Symbols:
+ +[CTXPCLoadCarrierStoreVisitStatusRequest allowedClassesForArguments]
+ +[CTXPCLoadCarrierStoreVisitStatusResponse allowedClassesForArguments]
+ +[CTXPCLoadSimSetupInfoRequest allowedClassesForArguments]
+ +[CTXPCLoadSimSetupInfoResponse allowedClassesForArguments]
+ +[CTXPCSaveCarrierStoreVisitStatusRequest allowedClassesForArguments]
+ +[CTXPCSaveSimSetupInfoRequest allowedClassesForArguments]
+ -[CTRemotePlan needHideForCloudFlow]
+ -[CTRemotePlan needVisitStoreForTransfer]
+ -[CTRemotePlan setNeedHideForCloudFlow:]
+ -[CTRemotePlan setNeedVisitStoreForTransfer:]
+ -[CTXPCLoadCarrierStoreVisitStatusRequest carrier]
+ -[CTXPCLoadCarrierStoreVisitStatusRequest ct_shortName]
+ -[CTXPCLoadCarrierStoreVisitStatusRequest initWithCarrier:]
+ -[CTXPCLoadCarrierStoreVisitStatusRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCLoadCarrierStoreVisitStatusRequest requiredEntitlement]
+ -[CTXPCLoadCarrierStoreVisitStatusResponse ct_shortName]
+ -[CTXPCLoadCarrierStoreVisitStatusResponse initWithVisited:]
+ -[CTXPCLoadCarrierStoreVisitStatusResponse visited]
+ -[CTXPCLoadSimSetupInfoRequest ct_shortName]
+ -[CTXPCLoadSimSetupInfoRequest infoKey]
+ -[CTXPCLoadSimSetupInfoRequest initWithInfo:]
+ -[CTXPCLoadSimSetupInfoRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCLoadSimSetupInfoRequest requiredEntitlement]
+ -[CTXPCLoadSimSetupInfoResponse ct_shortName]
+ -[CTXPCLoadSimSetupInfoResponse info]
+ -[CTXPCLoadSimSetupInfoResponse initWithInfo:]
+ -[CTXPCSaveCarrierStoreVisitStatusRequest carrier]
+ -[CTXPCSaveCarrierStoreVisitStatusRequest ct_shortName]
+ -[CTXPCSaveCarrierStoreVisitStatusRequest initWithCarrier:visited:]
+ -[CTXPCSaveCarrierStoreVisitStatusRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCSaveCarrierStoreVisitStatusRequest requiredEntitlement]
+ -[CTXPCSaveCarrierStoreVisitStatusRequest visited]
+ -[CTXPCSaveSimSetupInfoRequest ct_shortName]
+ -[CTXPCSaveSimSetupInfoRequest infoKey]
+ -[CTXPCSaveSimSetupInfoRequest info]
+ -[CTXPCSaveSimSetupInfoRequest initWithInfo:info:]
+ -[CTXPCSaveSimSetupInfoRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCSaveSimSetupInfoRequest requiredEntitlement]
+ -[CTXPCShowTravelEducationRequest ct_shortName]
+ -[CTXPCShowTravelEducationRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCShowTravelEducationRequest requiredEntitlement]
+ -[CoreTelephonyClient(CellularPlanManager) shouldShowTravelEducation:]
+ -[CoreTelephonyClient(PlanTransfer) loadCarrierStoreVisitStatusForCarrier:error:]
+ -[CoreTelephonyClient(PlanTransfer) loadSimSetupInfo:error:]
+ -[CoreTelephonyClient(PlanTransfer) saveCarrierStoreVisitStatus:visited:completion:]
+ -[CoreTelephonyClient(PlanTransfer) saveSimSetupInfo:info:completion:]
+ -[CoreTelephonyClient(Radio) getSupportsTARandomization:error:]
+ -[CoreTelephonyClient(Radio) getTARandomizationSetting:error:]
+ -[CoreTelephonyClient(Radio) setTARandomizationUserSetting:enabled:]
+ GCC_except_table401
+ GCC_except_table426
+ GCC_except_table430
+ GCC_except_table443
+ GCC_except_table464
+ GCC_except_table475
+ GCC_except_table476
+ GCC_except_table487
+ GCC_except_table522
+ GCC_except_table525
+ GCC_except_table526
+ GCC_except_table537
+ GCC_except_table541
+ GCC_except_table544
+ GCC_except_table548
+ GCC_except_table559
+ GCC_except_table570
+ GCC_except_table571
+ GCC_except_table574
+ GCC_except_table575
+ GCC_except_table579
+ GCC_except_table621
+ GCC_except_table628
+ GCC_except_table638
+ GCC_except_table639
+ GCC_except_table650
+ GCC_except_table661
+ GCC_except_table676
+ GCC_except_table677
+ GCC_except_table687
+ GCC_except_table688
+ GCC_except_table691
+ GCC_except_table692
+ GCC_except_table694
+ GCC_except_table695
+ GCC_except_table698
+ GCC_except_table699
+ GCC_except_table701
+ GCC_except_table702
+ GCC_except_table703
+ GCC_except_table705
+ GCC_except_table708
+ GCC_except_table709
+ GCC_except_table712
+ GCC_except_table713
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table717
+ GCC_except_table718
+ _OBJC_CLASS_$_CTXPCLoadCarrierStoreVisitStatusRequest
+ _OBJC_CLASS_$_CTXPCLoadCarrierStoreVisitStatusResponse
+ _OBJC_CLASS_$_CTXPCLoadSimSetupInfoRequest
+ _OBJC_CLASS_$_CTXPCLoadSimSetupInfoResponse
+ _OBJC_CLASS_$_CTXPCSaveCarrierStoreVisitStatusRequest
+ _OBJC_CLASS_$_CTXPCSaveSimSetupInfoRequest
+ _OBJC_CLASS_$_CTXPCShowTravelEducationRequest
+ _OBJC_IVAR_$_CTRemotePlan._needHideForCloudFlow
+ _OBJC_IVAR_$_CTRemotePlan._needVisitStoreForTransfer
+ _OBJC_METACLASS_$_CTXPCLoadCarrierStoreVisitStatusRequest
+ _OBJC_METACLASS_$_CTXPCLoadCarrierStoreVisitStatusResponse
+ _OBJC_METACLASS_$_CTXPCLoadSimSetupInfoRequest
+ _OBJC_METACLASS_$_CTXPCLoadSimSetupInfoResponse
+ _OBJC_METACLASS_$_CTXPCSaveCarrierStoreVisitStatusRequest
+ _OBJC_METACLASS_$_CTXPCSaveSimSetupInfoRequest
+ _OBJC_METACLASS_$_CTXPCShowTravelEducationRequest
+ __OBJC_$_CLASS_METHODS_CTXPCLoadCarrierStoreVisitStatusRequest
+ __OBJC_$_CLASS_METHODS_CTXPCLoadCarrierStoreVisitStatusResponse
+ __OBJC_$_CLASS_METHODS_CTXPCLoadSimSetupInfoRequest
+ __OBJC_$_CLASS_METHODS_CTXPCLoadSimSetupInfoResponse
+ __OBJC_$_CLASS_METHODS_CTXPCSaveCarrierStoreVisitStatusRequest
+ __OBJC_$_CLASS_METHODS_CTXPCSaveSimSetupInfoRequest
+ __OBJC_$_INSTANCE_METHODS_CTXPCLoadCarrierStoreVisitStatusRequest
+ __OBJC_$_INSTANCE_METHODS_CTXPCLoadCarrierStoreVisitStatusResponse
+ __OBJC_$_INSTANCE_METHODS_CTXPCLoadSimSetupInfoRequest
+ __OBJC_$_INSTANCE_METHODS_CTXPCLoadSimSetupInfoResponse
+ __OBJC_$_INSTANCE_METHODS_CTXPCSaveCarrierStoreVisitStatusRequest
+ __OBJC_$_INSTANCE_METHODS_CTXPCSaveSimSetupInfoRequest
+ __OBJC_$_INSTANCE_METHODS_CTXPCShowTravelEducationRequest
+ __OBJC_$_PROP_LIST_CTXPCLoadCarrierStoreVisitStatusResponse
+ __OBJC_$_PROP_LIST_CTXPCLoadSimSetupInfoResponse
+ __OBJC_CLASS_RO_$_CTXPCLoadCarrierStoreVisitStatusRequest
+ __OBJC_CLASS_RO_$_CTXPCLoadCarrierStoreVisitStatusResponse
+ __OBJC_CLASS_RO_$_CTXPCLoadSimSetupInfoRequest
+ __OBJC_CLASS_RO_$_CTXPCLoadSimSetupInfoResponse
+ __OBJC_CLASS_RO_$_CTXPCSaveCarrierStoreVisitStatusRequest
+ __OBJC_CLASS_RO_$_CTXPCSaveSimSetupInfoRequest
+ __OBJC_CLASS_RO_$_CTXPCShowTravelEducationRequest
+ __OBJC_METACLASS_RO_$_CTXPCLoadCarrierStoreVisitStatusRequest
+ __OBJC_METACLASS_RO_$_CTXPCLoadCarrierStoreVisitStatusResponse
+ __OBJC_METACLASS_RO_$_CTXPCLoadSimSetupInfoRequest
+ __OBJC_METACLASS_RO_$_CTXPCLoadSimSetupInfoResponse
+ __OBJC_METACLASS_RO_$_CTXPCSaveCarrierStoreVisitStatusRequest
+ __OBJC_METACLASS_RO_$_CTXPCSaveSimSetupInfoRequest
+ __OBJC_METACLASS_RO_$_CTXPCShowTravelEducationRequest
+ __Z21CTThrowingCastIfClassI8NSObjectEPT_P11objc_object
+ ___60-[CoreTelephonyClient(PlanTransfer) loadSimSetupInfo:error:]_block_invoke
+ ___60-[CoreTelephonyClient(PlanTransfer) loadSimSetupInfo:error:]_block_invoke_2
+ ___60-[CoreTelephonyClient(PlanTransfer) loadSimSetupInfo:error:]_block_invoke_2.cold.1
+ ___62-[CoreTelephonyClient(Radio) getTARandomizationSetting:error:]_block_invoke
+ ___62-[CoreTelephonyClient(Radio) getTARandomizationSetting:error:]_block_invoke_2
+ ___63-[CoreTelephonyClient(Radio) getSupportsTARandomization:error:]_block_invoke
+ ___63-[CoreTelephonyClient(Radio) getSupportsTARandomization:error:]_block_invoke_2
+ ___68-[CoreTelephonyClient(Radio) setTARandomizationUserSetting:enabled:]_block_invoke
+ ___68-[CoreTelephonyClient(Radio) setTARandomizationUserSetting:enabled:]_block_invoke_2
+ ___70-[CoreTelephonyClient(CellularPlanManager) shouldShowTravelEducation:]_block_invoke
+ ___70-[CoreTelephonyClient(CellularPlanManager) shouldShowTravelEducation:]_block_invoke_2
+ ___70-[CoreTelephonyClient(PlanTransfer) saveSimSetupInfo:info:completion:]_block_invoke
+ ___70-[CoreTelephonyClient(PlanTransfer) saveSimSetupInfo:info:completion:]_block_invoke_2
+ ___70-[CoreTelephonyClient(PlanTransfer) saveSimSetupInfo:info:completion:]_block_invoke_3
+ ___76-[CTXPCLoadSimSetupInfoRequest performRequestWithHandler:completionHandler:]_block_invoke
+ ___76-[CTXPCSaveSimSetupInfoRequest performRequestWithHandler:completionHandler:]_block_invoke
+ ___79-[CTXPCShowTravelEducationRequest performRequestWithHandler:completionHandler:]_block_invoke
+ ___81-[CoreTelephonyClient(PlanTransfer) loadCarrierStoreVisitStatusForCarrier:error:]_block_invoke
+ ___81-[CoreTelephonyClient(PlanTransfer) loadCarrierStoreVisitStatusForCarrier:error:]_block_invoke_2
+ ___84-[CoreTelephonyClient(PlanTransfer) saveCarrierStoreVisitStatus:visited:completion:]_block_invoke
+ ___84-[CoreTelephonyClient(PlanTransfer) saveCarrierStoreVisitStatus:visited:completion:]_block_invoke_2
+ ___84-[CoreTelephonyClient(PlanTransfer) saveCarrierStoreVisitStatus:visited:completion:]_block_invoke_3
+ ___87-[CTXPCLoadCarrierStoreVisitStatusRequest performRequestWithHandler:completionHandler:]_block_invoke
+ ___87-[CTXPCSaveCarrierStoreVisitStatusRequest performRequestWithHandler:completionHandler:]_block_invoke
+ ___block_descriptor_40_ea8_32bs_e18_v16?0"NSObject"8ls32l8
+ ___block_literal_global.1020
+ ___block_literal_global.1029
+ _objc_msgSend$carrier
+ _objc_msgSend$getSupportsTARandomization:completion:
+ _objc_msgSend$getTARandomizationSetting:completion:
+ _objc_msgSend$infoKey
+ _objc_msgSend$initWithCarrier:
+ _objc_msgSend$initWithCarrier:visited:
+ _objc_msgSend$initWithInfo:info:
+ _objc_msgSend$initWithVisited:
+ _objc_msgSend$loadCarrierStoreVisitStatusForCarrier:completion:
+ _objc_msgSend$loadSimSetupInfo:completion:
+ _objc_msgSend$needHideForCloudFlow
+ _objc_msgSend$needVisitStoreForTransfer
+ _objc_msgSend$saveCarrierStoreVisitStatus:visited:completion:
+ _objc_msgSend$saveSimSetupInfo:info:completion:
+ _objc_msgSend$setTARandomizationUserSetting:enabled:completion:
+ _objc_msgSend$shouldShowTravelEducation:
+ _objc_msgSend$visited
- GCC_except_table385
- GCC_except_table425
- GCC_except_table427
- GCC_except_table428
- GCC_except_table429
- GCC_except_table432
- GCC_except_table433
- GCC_except_table445
- GCC_except_table465
- GCC_except_table473
- GCC_except_table477
- GCC_except_table486
- GCC_except_table490
- GCC_except_table510
- GCC_except_table518
- GCC_except_table523
- GCC_except_table527
- GCC_except_table538
- GCC_except_table543
- GCC_except_table558
- GCC_except_table573
- GCC_except_table577
- GCC_except_table584
- GCC_except_table590
- GCC_except_table605
- GCC_except_table606
- GCC_except_table618
- GCC_except_table622
- GCC_except_table624
- GCC_except_table626
- GCC_except_table630
- GCC_except_table652
- GCC_except_table660
- GCC_except_table674
- GCC_except_table675
- ___block_literal_global.1016
- ___block_literal_global.1021
CStrings:
+ " needHideForCloudFlow=%d"
+ " needHideForCloudFlow=(null)"
+ " needVisitStoreForTransfer=%d"
+ " needVisitStoreForTransfer=(null)"
+ "13091.1.6"
+ "13091.1.6~11"
+ "CCCallSourceMode::kCCCallSourceModeScreeningNoHO"
+ "CTXPCLoadCarrierStoreVisitStatusRequest"
+ "CTXPCLoadCarrierStoreVisitStatusResponse"
+ "CTXPCLoadSimSetupInfoRequest"
+ "CTXPCLoadSimSetupInfoResponse"
+ "CTXPCSaveCarrierStoreVisitStatusRequest"
+ "CTXPCSaveSimSetupInfoRequest"
+ "CTXPCShowTravelEducationRequest"
+ "T@\"NSNumber\",&,N,V_needHideForCloudFlow"
+ "T@\"NSNumber\",&,N,V_needVisitStoreForTransfer"
+ "T@\"NSObject\",R,N"
+ "_needHideForCloudFlow"
+ "_needVisitStoreForTransfer"
+ "error: %@"
+ "getSupportsTARandomization:completion:"
+ "getSupportsTARandomization:error:"
+ "getTARandomizationSetting:completion:"
+ "getTARandomizationSetting:error:"
+ "infoKey"
+ "initWithCarrier:"
+ "initWithCarrier:visited:"
+ "initWithInfo:info:"
+ "initWithVisited:"
+ "loadCarrierStoreVisitStatusForCarrier:completion:"
+ "loadCarrierStoreVisitStatusForCarrier:error:"
+ "loadSimSetupInfo:completion:"
+ "loadSimSetupInfo:error:"
+ "needHideForCloudFlow"
+ "needVisitStoreForTransfer"
+ "saveCarrierStoreVisitStatus:visited:completion:"
+ "saveSimSetupInfo:info:completion:"
+ "setNeedHideForCloudFlow:"
+ "setNeedVisitStoreForTransfer:"
+ "setTARandomizationUserSetting:enabled:"
+ "setTARandomizationUserSetting:enabled:completion:"
+ "shouldShowTravelEducation:"
+ "v16@?0@\"NSObject\"8"
+ "v32@0:8@\"CTServiceDescriptor\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "visited"
- "13090.3"
- "13090.3~67"

```
