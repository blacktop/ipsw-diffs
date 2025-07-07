## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-855.0.0.0.0
-  __TEXT.__text: 0xa9664
+858.2.0.0.0
+  __TEXT.__text: 0xaa7e0
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x9704
+  __TEXT.__objc_methlist: 0x97cc
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x1b98
-  __TEXT.__cstring: 0xee66
-  __TEXT.__oslogstring: 0x619c
+  __TEXT.__gcc_except_tab: 0x1bdc
+  __TEXT.__cstring: 0xf07f
+  __TEXT.__oslogstring: 0x61f4
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x23e0
-  __TEXT.__objc_classname: 0x14c1
-  __TEXT.__objc_methname: 0x14fdd
-  __TEXT.__objc_methtype: 0x3324
-  __TEXT.__objc_stubs: 0xd880
+  __TEXT.__unwind_info: 0x2410
+  __TEXT.__objc_classname: 0x14d1
+  __TEXT.__objc_methname: 0x150ed
+  __TEXT.__objc_methtype: 0x334a
+  __TEXT.__objc_stubs: 0xd940
   __DATA_CONST.__got: 0xa28
-  __DATA_CONST.__const: 0x1ca8
-  __DATA_CONST.__objc_classlist: 0x450
+  __DATA_CONST.__const: 0x1d00
+  __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d10
+  __DATA_CONST.__objc_selrefs: 0x4d48
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0x6d40
-  __AUTH_CONST.__objc_const: 0x3ac60
+  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__cfstring: 0x6ee0
+  __AUTH_CONST.__objc_const: 0x3ade8
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x2ad0
-  __DATA.__objc_ivar: 0xdc8
+  __AUTH.__objc_data: 0x2b20
+  __DATA.__objc_ivar: 0xdd8
   __DATA.__data: 0xb50
-  __DATA.__bss: 0x160
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4DBA40ED-7E88-358D-991D-B8959BF134FA
-  Functions: 3661
-  Symbols:   13356
-  CStrings:  6988
+  UUID: EF183810-9B65-382C-823D-9FE376B4240A
+  Functions: 3681
+  Symbols:   13419
+  CStrings:  7032
 
Symbols:
+ +[DCTCodeManager shared]
+ +[DCTCodeManager shared].cold.1
+ -[CrossPlatformShowManualDetailsViewController codeDidChange]
+ -[CrossPlatformShowManualDetailsViewController dealloc]
+ -[CrossPlatformShowManualDetailsViewController init]
+ -[CrossPlatformShowManualDetailsViewController updateText]
+ -[CrossPlatformTransferAuthQRCodeViewController codeDidChange]
+ -[CrossPlatformTransferAuthQRCodeViewController dealloc]
+ -[CrossPlatformTransferAuthQRCodeViewController imgView]
+ -[CrossPlatformTransferAuthQRCodeViewController init]
+ -[CrossPlatformTransferAuthQRCodeViewController setImgView:]
+ -[CrossPlatformTransferAuthQRCodeViewController updateImage]
+ -[DCTCodeManager .cxx_destruct]
+ -[DCTCodeManager addObserver:selector:]
+ -[DCTCodeManager code]
+ -[DCTCodeManager removeObserver:]
+ -[DCTCodeManager setCode:]
+ -[TSCellularSetupActivatingViewController setTransferStarted]
+ -[TSEnableTableViewController secondaryButtonDetail]
+ -[TSEnableTableViewController setSecondaryButtonDetail:]
+ -[TSEnableTableViewController(UIScrollViewDelegate) scrollViewDidEndDecelerating:]
+ -[TSEnableTableViewController(UITableViewDataSource) _titleForItem:]
+ -[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:]
+ GCC_except_table67
+ _DCTCodeDidChangeNotification
+ _OBJC_CLASS_$_DCTCodeManager
+ _OBJC_IVAR_$_CrossPlatformTransferAuthQRCodeViewController._imgView
+ _OBJC_IVAR_$_DCTCodeManager._code
+ _OBJC_IVAR_$_TSEnableTableViewController._secondaryButtonDetail
+ _OBJC_IVAR_$_TSTravelBuddyViewController._isDualSIMConfig
+ _OBJC_IVAR_$_TSTravelBuddyViewController._secondHomeIccidPhoneNumber
+ _OBJC_METACLASS_$_DCTCodeManager
+ __OBJC_$_CLASS_METHODS_DCTCodeManager
+ __OBJC_$_INSTANCE_METHODS_DCTCodeManager
+ __OBJC_$_INSTANCE_METHODS_TSEnableTableViewController(UITableViewDelegate|UITableViewDataSource|UIScrollViewDelegate)
+ __OBJC_$_INSTANCE_VARIABLES_DCTCodeManager
+ __OBJC_$_PROP_LIST_DCTCodeManager
+ __OBJC_CLASS_PROTOCOLS_$_TSEnableTableViewController(UITableViewDelegate|UITableViewDataSource|UIScrollViewDelegate)
+ __OBJC_CLASS_RO_$_DCTCodeManager
+ __OBJC_METACLASS_RO_$_DCTCodeManager
+ ___108-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:]_block_invoke
+ ___24+[DCTCodeManager shared]_block_invoke
+ ___45-[TSLowDataModeConfigViewController prepare:]_block_invoke.43
+ ___45-[TSLowDataModeConfigViewController prepare:]_block_invoke.43.cold.1
+ ___45-[TSLowDataModeConfigViewController prepare:]_block_invoke.43.cold.2
+ ___82-[TSEnableTableViewController(UIScrollViewDelegate) scrollViewDidEndDecelerating:]_block_invoke
+ ___block_descriptor_49_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_49_e8_32bs40w_e61_v32?0"NSArray"8"CTDisplayPlanList"16"CTDisplayPlanList"24lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e41_v24?0"CTPlanTravelDetails"8"NSError"16lw56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e50_v24?0"CTXPCServiceSubscriptionInfo"8"NSError"16lw56l8s48l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48r56w_e61_v32?0"NSArray"8"CTDisplayPlanList"16"CTDisplayPlanList"24lr48l8w56l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e8_v12?0B8lr64l8s32l8s40l8s48l8s56l8
+ _objc_msgSend$_titleForItem:
+ _objc_msgSend$addObserver:selector:
+ _objc_msgSend$didEnablePlanItemsForTravel:
+ _objc_msgSend$imgView
+ _objc_msgSend$setCode:
+ _objc_msgSend$setImgView:
+ _objc_msgSend$setTransferStarted
+ _objc_msgSend$shared
+ _objc_msgSend$shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:
+ _objc_msgSend$updateImage
+ _objc_msgSend$updateText
+ _objc_msgSend$uppercaseString
+ _sIsAnyPlanTransferable
+ _shared.instance
+ _shared.onceToken
- -[CrossPlatformShowManualDetailsViewController initWithAuthCode:]
- -[CrossPlatformTransferAuthQRCodeViewController dctCode]
- -[CrossPlatformTransferAuthQRCodeViewController initWithAuthCode:]
- -[CrossPlatformTransferAuthQRCodeViewController setDctCode:]
- -[TSEnableTableViewController(UITableViewDataSource) scrollViewDidEndDecelerating:]
- -[TSTransferFlow _hasTransferablePlan:]
- -[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:]
- GCC_except_table66
- _OBJC_CLASS_$_UIButton
- _OBJC_IVAR_$_CrossPlatformTransferAuthQRCodeViewController._dctCode
- __OBJC_$_INSTANCE_METHODS_TSEnableTableViewController(UITableViewDelegate|UITableViewDataSource)
- __OBJC_CLASS_PROTOCOLS_$_TSEnableTableViewController(UITableViewDelegate|UITableViewDataSource)
- ___45-[TSLowDataModeConfigViewController prepare:]_block_invoke.cold.1
- ___83-[TSEnableTableViewController(UITableViewDataSource) scrollViewDidEndDecelerating:]_block_invoke
- ___94-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:]_block_invoke
- ___block_descriptor_40_e8_32r_e61_v32?0"NSArray"8"CTDisplayPlanList"16"CTDisplayPlanList"24lr32l8
- ___block_descriptor_57_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
- ___block_descriptor_57_e8_32s40bs48w_e61_v32?0"NSArray"8"CTDisplayPlanList"16"CTDisplayPlanList"24lw48l8s40l8s32l8
- ___block_descriptor_66_e8_32s40s48bs56w_e8_v12?0B8lw56l8s48l8s32l8s40l8
- _objc_msgSend$_hasTransferablePlan:
- _objc_msgSend$initWithAuthCode:
- _objc_msgSend$safeAreaLayoutGuide
- _objc_msgSend$setEdgesForExtendedLayout:
- _objc_msgSend$setTitleColor:forState:
- _objc_msgSend$shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:
CStrings:
+ "-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:]"
+ "CELLULAR_PLAN_ENABLEMENT_TURN_OFF_%@"
+ "CROSSPLATFORM_TRANSFER_COMPLETE_TITLE_SOURCE"
+ "CROSSPLATFORM_TRANSFER_DETAIL_TARGET_POST_BUDDY"
+ "CROSSTRANSFER_SESSION_ERROR_CARRIER_LOCK"
+ "CROSSTRANSFER_SESSION_ERROR_CARRIER_LOCK_MSG"
+ "CROSSTRANSFER_USERCANCEL_DETAIL"
+ "CROSSTRANSFER_USERCANCEL_TITLE"
+ "DCTCodeDidChangeNotification"
+ "DCTCodeManager"
+ "Setting _defaultDataContext to be %@ @%s"
+ "Subscription context UUID is not ready! @%s"
+ "T@\"NSString\",&,N,V_code"
+ "T@\"NSString\",&,V_secondaryButtonDetail"
+ "T@\"SSOBLinkTrayButton\",&,V_enterDetailsManuallyButton"
+ "T@\"UIImageView\",&,N,V_imgView"
+ "TRANSFERING"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_DATAONLY_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_DATAONLY_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DATAONLY_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DATAONLY_DUALSIM_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_%@_%@"
+ "User is in dual SIM config @%s"
+ "[E]Failed to find subscription context for travel SIM %@ @%s"
+ "_code"
+ "_imgView"
+ "_isDualSIMConfig"
+ "_secondHomeIccidPhoneNumber"
+ "_secondaryButtonDetail"
+ "_titleForItem:"
+ "addObserver:selector:"
+ "codeDidChange"
+ "didEnablePlanItemsForTravel:"
+ "imgView"
+ "secondaryButtonDetail"
+ "setCode:"
+ "setImgView:"
+ "setSecondaryButtonDetail:"
+ "setTransferStarted"
+ "shared"
+ "shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:"
+ "updateImage"
+ "updateText"
+ "uppercaseString"
+ "v32@0:8@16:24"
+ "v52@0:8@16@24B32@36@?44"
- "-[CrossPlatformTransferAuthQRCodeViewController viewDidLoad]"
- "-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:]"
- "Cancel"
- "T@\"NSString\",&,N,V_dctCode"
- "T@\"UIButton\",&,V_enterDetailsManuallyButton"
- "[E]Fail to fetch CurrentDataSubscription: %@ @%s"
- "_hasTransferablePlan:"
- "generate CIImage with auth code: %@ @%s"
- "initWithAuthCode:"
- "safeAreaLayoutGuide"
- "setDctCode:"
- "setEdgesForExtendedLayout:"
- "setTitleColor:forState:"
- "shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:"
- "\xf1"

```
