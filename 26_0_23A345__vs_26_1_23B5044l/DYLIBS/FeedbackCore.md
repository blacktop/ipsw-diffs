## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

```diff

-191.0.0.0.0
-  __TEXT.__text: 0x1415f0
-  __TEXT.__auth_stubs: 0x2c70
-  __TEXT.__objc_methlist: 0xb548
-  __TEXT.__const: 0x2df4
-  __TEXT.__cstring: 0xc101
-  __TEXT.__oslogstring: 0xa196
-  __TEXT.__gcc_except_tab: 0x1bec
+191.3.0.0.0
+  __TEXT.__text: 0x13f450
+  __TEXT.__auth_stubs: 0x2c50
+  __TEXT.__objc_methlist: 0xb560
+  __TEXT.__const: 0x2da4
+  __TEXT.__cstring: 0xc3c1
+  __TEXT.__oslogstring: 0xa0d6
+  __TEXT.__gcc_except_tab: 0x1cbc
   __TEXT.__ustring: 0xe6
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__constg_swiftt: 0x1d18
-  __TEXT.__swift5_typeref: 0x3d92
+  __TEXT.__constg_swiftt: 0x1cd4
+  __TEXT.__swift5_typeref: 0x3d90
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0xae2
-  __TEXT.__swift5_fieldmd: 0xcfc
-  __TEXT.__swift5_assocty: 0x2b8
-  __TEXT.__swift5_proto: 0x15c
-  __TEXT.__swift5_types: 0x13c
-  __TEXT.__swift5_capture: 0xcb8
+  __TEXT.__swift5_reflstr: 0xac2
+  __TEXT.__swift5_fieldmd: 0xcec
+  __TEXT.__swift5_assocty: 0x2a0
+  __TEXT.__swift5_proto: 0x158
+  __TEXT.__swift5_types: 0x138
+  __TEXT.__swift5_capture: 0xcdc
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4a90
-  __TEXT.__eh_frame: 0x1680
+  __TEXT.__unwind_info: 0x4aa8
+  __TEXT.__eh_frame: 0x1580
   __TEXT.__objc_classname: 0x11c9
-  __TEXT.__objc_methname: 0x1d004
-  __TEXT.__objc_methtype: 0x3dc2
-  __TEXT.__objc_stubs: 0x14c80
-  __DATA_CONST.__got: 0x11f8
-  __DATA_CONST.__const: 0x3f60
+  __TEXT.__objc_methname: 0x1d00a
+  __TEXT.__objc_methtype: 0x3dc8
+  __TEXT.__objc_stubs: 0x14c20
+  __DATA_CONST.__got: 0x11e8
+  __DATA_CONST.__const: 0x3fe0
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7538
+  __DATA_CONST.__objc_selrefs: 0x7530
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x4d0
-  __AUTH_CONST.__auth_got: 0x1648
-  __AUTH_CONST.__const: 0x4610
-  __AUTH_CONST.__cfstring: 0x8e00
-  __AUTH_CONST.__objc_const: 0x1d508
+  __AUTH_CONST.__auth_got: 0x1638
+  __AUTH_CONST.__const: 0x46f8
+  __AUTH_CONST.__cfstring: 0x8e80
+  __AUTH_CONST.__objc_const: 0x1d4c0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x498
   __AUTH.__objc_data: 0x4e08
   __AUTH.__data: 0xd50
-  __DATA.__objc_ivar: 0x704
-  __DATA.__data: 0x2cd0
+  __DATA.__objc_ivar: 0x700
+  __DATA.__data: 0x2cb0
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x3098
+  __DATA.__bss: 0x3028
   __DATA.__common: 0x158
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3CFBD108-7E5B-3CAD-936F-CB30DA3467C1
+  UUID: 294EF9E6-43CD-3763-B56B-4603721DF879
   Functions: 7285
-  Symbols:   15575
-  CStrings:  9343
+  Symbols:   15611
+  CStrings:  9353
 
Symbols:
+ +[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]
+ +[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:].cold.1
+ +[FBKDEDHelper _getSessionWithIdentifier:configuration:device:filerForm:getDetails:shouldGetSessionStatus:completion:]
+ +[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:filerForm:shouldGetDetails:shouldGetSessionStatus:completion:]
+ +[FBKDEDHelper fetchDETextDataWithFilerForm:fromSession:configuration:completion:]
+ +[FBKDEDHelper fetchDETextDataWithFilerForm:fromSession:configuration:completion:].cold.1
+ -[FBKBugFormTableViewController beginSubmission:]
+ -[FBKBugFormTableViewController checkAnnotatedContentConsent:hasShownPresubmissionConsent:andContinue:]
+ -[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]
+ -[FBKBugFormTableViewController checkMissingFiles:andContinue:]
+ -[FBKBugFormTableViewController checkPresubmissionLegalText:presentedDEConsent:andContinue:]
+ -[FBKBugFormTableViewController showMissingAnswersWithResult:sender:andContinue:]
+ -[FBKBugFormTableViewController validateAnswersAndPrepareForSubmission]
+ -[FBKFormResponse allFileMatchers]
+ -[FBKInstalledApp isIWorkApp].cold.1
+ GCC_except_table104
+ GCC_except_table111
+ GCC_except_table125
+ GCC_except_table143
+ GCC_except_table29
+ GCC_except_table343
+ GCC_except_table64
+ GCC_except_table99
+ ___103-[FBKBugFormTableViewController checkAnnotatedContentConsent:hasShownPresubmissionConsent:andContinue:]_block_invoke
+ ___103-[FBKBugFormTableViewController checkAnnotatedContentConsent:hasShownPresubmissionConsent:andContinue:]_block_invoke_2
+ ___118+[FBKDEDHelper _getSessionWithIdentifier:configuration:device:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke
+ ___118+[FBKDEDHelper _getSessionWithIdentifier:configuration:device:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.103
+ ___118+[FBKDEDHelper _getSessionWithIdentifier:configuration:device:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.103.cold.1
+ ___118+[FBKDEDHelper _getSessionWithIdentifier:configuration:device:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.cold.1
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.106
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.106.cold.1
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.110
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.111
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.111.cold.1
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.111.cold.2
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.115
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke.115.cold.1
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke_2
+ ___121+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:]_block_invoke_2.cold.1
+ ___141+[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:filerForm:shouldGetDetails:shouldGetSessionStatus:completion:]_block_invoke
+ ___141+[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:filerForm:shouldGetDetails:shouldGetSessionStatus:completion:]_block_invoke.100
+ ___141+[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:filerForm:shouldGetDetails:shouldGetSessionStatus:completion:]_block_invoke.cold.1
+ ___141+[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:filerForm:shouldGetDetails:shouldGetSessionStatus:completion:]_block_invoke_2
+ ___29-[FBKInstalledApp isIWorkApp]_block_invoke
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.265
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.265.cold.1
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.272
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.274
+ ___42-[FBKBugFormTableViewController legalText]_block_invoke.307
+ ___49-[FBKBugFormTableViewController beginSubmission:]_block_invoke
+ ___49-[FBKBugFormTableViewController beginSubmission:]_block_invoke_2
+ ___49-[FBKBugFormTableViewController beginSubmission:]_block_invoke_3
+ ___49-[FBKBugFormTableViewController beginSubmission:]_block_invoke_4
+ ___49-[FBKBugFormTableViewController beginSubmission:]_block_invoke_5
+ ___49-[FBKBugFormTableViewController beginSubmission:]_block_invoke_6
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke.239
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2.240
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2.240.cold.1
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2.240.cold.2
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_3
+ ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke
+ ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke.221
+ ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke.225
+ ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke.229
+ ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.324
+ ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.326
+ ___78+[FBKDEDHelper reconnectBugSessionWithIdentifier:deviceIdentifier:completion:]_block_invoke.117
+ ___81+[FBKDEDHelper completeEnhancedLoggingWithFollowup:devicesController:completion:]_block_invoke.125
+ ___81+[FBKDEDHelper completeEnhancedLoggingWithFollowup:devicesController:completion:]_block_invoke.128
+ ___82+[FBKDEDHelper fetchDETextDataWithFilerForm:fromSession:configuration:completion:]_block_invoke
+ ___82+[FBKDEDHelper fetchDETextDataWithFilerForm:fromSession:configuration:completion:]_block_invoke.121
+ ___82+[FBKDEDHelper fetchDETextDataWithFilerForm:fromSession:configuration:completion:]_block_invoke.121.cold.1
+ ___82+[FBKDEDHelper fetchDETextDataWithFilerForm:fromSession:configuration:completion:]_block_invoke_2
+ ___82+[FBKDEDHelper fetchDETextDataWithFilerForm:fromSession:configuration:completion:]_block_invoke_2.cold.1
+ ___82+[FBKDEDHelper fetchDETextDataWithFilerForm:fromSession:configuration:completion:]_block_invoke_2.cold.2
+ ___92-[FBKBugFormTableViewController checkPresubmissionLegalText:presentedDEConsent:andContinue:]_block_invoke
+ ___92-[FBKBugFormTableViewController checkPresubmissionLegalText:presentedDEConsent:andContinue:]_block_invoke_2
+ ___block_descriptor_121_e8_32s40s48s56s64s72bs80r88r96r104r112r_e5_v8?0ls32l8s72l8s40l8s48l8s56l8r80l8r88l8r96l8s64l8r104l8r112l8
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80bs88r96r104r112r120r128r_e17_v16?0"NSArray"8lr88l8s32l8s40l8r96l8r104l8s48l8s56l8s64l8s80l8s72l8r112l8r120l8r128l8
+ ___block_descriptor_154_e8_32s40s48s56s64s72bs80r88r96r104r112r120r128r136r_e35_v24?0"DEDBugSession"8"NSError"16lr80l8s32l8s40l8r88l8r96l8s48l8r104l8s72l8s56l8r112l8r120l8r128l8s64l8r136l8
+ ___block_descriptor_162_e8_32s40s48s56s64s72bs80r88r96r104r112r120r128r136r_e5_v8?0ls32l8s40l8s48l8r80l8s56l8r88l8r96l8r104l8s72l8r112l8r120l8r128l8s64l8r136l8
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_48_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e23_v16?0"UIAlertAction"8ls32l8w48l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e27_v24?0"NSSet"8"NSError"16ls32l8s40l8r56l8r64l8s48l8
+ ___block_descriptor_73_e8_32s40bs_e18_v16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_82_e8_32s40s48s56bs_e48_v24?0"DEDBugSessionConfiguration"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_82_e8_32s40s48s56s64bs_e24_v16?0"NSNotification"8ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_90_e8_32s40s48s56s64bs72w_e19_v16?0"DEDDevice"8lw72l8s32l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.124
+ ___block_literal_global.131
+ ___block_literal_global.168
+ ___block_literal_global.305
+ ___block_literal_global.328
+ ___block_literal_global.79
+ ___block_literal_global.82
+ _block_copy_helper.16
+ _block_copy_helper.23
+ _block_descriptor.18
+ _block_descriptor.25
+ _block_destroy_helper.17
+ _block_destroy_helper.24
+ _isIWorkApp._iWorkApps
+ _isIWorkApp.onceToken
+ _legalText.onceToken.306
+ _objc_msgSend$_getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:
+ _objc_msgSend$_getSessionWithIdentifier:configuration:device:filerForm:getDetails:shouldGetSessionStatus:completion:
+ _objc_msgSend$_startSessionByFirstPairingWithConfig:device:grouped:identifier:filerForm:shouldGetDetails:shouldGetSessionStatus:completion:
+ _objc_msgSend$allFileMatchers
+ _objc_msgSend$beginSubmission:
+ _objc_msgSend$checkAnnotatedContentConsent:hasShownPresubmissionConsent:andContinue:
+ _objc_msgSend$checkDEConsent:continueHandler:
+ _objc_msgSend$checkDeviceConnectivity:andContinue:
+ _objc_msgSend$checkMissingFiles:andContinue:
+ _objc_msgSend$checkPresubmissionLegalText:presentedDEConsent:andContinue:
+ _objc_msgSend$fetchDETextDataWithFilerForm:fromSession:configuration:completion:
+ _objc_msgSend$showMissingAnswersWithResult:sender:andContinue:
+ _objc_msgSend$validateAnswersAndPrepareForSubmission
+ _symbolic So29FBKBugFormTableViewControllerC
+ _symbolic So29FBKBugFormTableViewControllerCSgXw
+ _symbolic So29FBKBugFormTableViewControllerCSgXwz_Xx
- +[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]
- +[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:].cold.1
- +[FBKDEDHelper _getSessionWithIdentifier:configuration:device:getDetails:shouldGetSessionStatus:completion:]
- +[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:shouldGetDetails:shouldGetSessionStatus:completion:]
- +[FBKDEDHelper fetchTextDataOnMatcherPredicates:fromSession:completion:]
- +[FBKDEDHelper fetchTextDataOnMatcherPredicates:fromSession:completion:].cold.1
- -[FBKBugFormTableViewController beginPresubmissionCheck:]
- -[FBKBugFormTableViewController checkEnhancedLoggingAndSubmit]
- -[FBKBugFormTableViewController checkExplicitConfirmationAndSubmit]
- -[FBKBugFormTableViewController checkLegalAndSubmit]
- -[FBKBugFormTableViewController isSubmissionPendingOnEnhancedLogging]
- -[FBKBugFormTableViewController setIsSubmissionPendingOnEnhancedLogging:]
- -[FBKDECollector fetchTextDataOnMatcherPredicates:completion:]
- -[FBKDECollector fetchTextDataOnMatcherPredicates:completion:].cold.1
- GCC_except_table116
- GCC_except_table118
- GCC_except_table134
- GCC_except_table178
- GCC_except_table336
- GCC_except_table45
- _OBJC_IVAR_$_FBKBugFormTableViewController._isSubmissionPendingOnEnhancedLogging
- ___108+[FBKDEDHelper _getSessionWithIdentifier:configuration:device:getDetails:shouldGetSessionStatus:completion:]_block_invoke
- ___108+[FBKDEDHelper _getSessionWithIdentifier:configuration:device:getDetails:shouldGetSessionStatus:completion:]_block_invoke.103
- ___108+[FBKDEDHelper _getSessionWithIdentifier:configuration:device:getDetails:shouldGetSessionStatus:completion:]_block_invoke.103.cold.1
- ___108+[FBKDEDHelper _getSessionWithIdentifier:configuration:device:getDetails:shouldGetSessionStatus:completion:]_block_invoke.cold.1
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke.106
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke.106.cold.1
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke.110
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke.110.cold.1
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke.110.cold.2
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke.114
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke.114.cold.1
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke_2
- ___111+[FBKDEDHelper _getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:]_block_invoke_2.cold.1
- ___131+[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:shouldGetDetails:shouldGetSessionStatus:completion:]_block_invoke
- ___131+[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:shouldGetDetails:shouldGetSessionStatus:completion:]_block_invoke.100
- ___131+[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:shouldGetDetails:shouldGetSessionStatus:completion:]_block_invoke.cold.1
- ___131+[FBKDEDHelper _startSessionByFirstPairingWithConfig:device:grouped:identifier:shouldGetDetails:shouldGetSessionStatus:completion:]_block_invoke_2
- ___39-[FBKBugFormTableViewController submit]_block_invoke.269
- ___39-[FBKBugFormTableViewController submit]_block_invoke.269.cold.1
- ___39-[FBKBugFormTableViewController submit]_block_invoke.276
- ___39-[FBKBugFormTableViewController submit]_block_invoke.278
- ___42-[FBKBugFormTableViewController legalText]_block_invoke.311
- ___52-[FBKBugFormTableViewController checkLegalAndSubmit]_block_invoke
- ___52-[FBKBugFormTableViewController checkLegalAndSubmit]_block_invoke_2
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.221
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.225
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.229
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.236
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.240
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke_2
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke_2.241
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke_2.241.cold.1
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke_2.241.cold.2
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke_3
- ___67-[FBKBugFormTableViewController checkExplicitConfirmationAndSubmit]_block_invoke
- ___67-[FBKBugFormTableViewController checkExplicitConfirmationAndSubmit]_block_invoke_2
- ___72+[FBKDEDHelper fetchTextDataOnMatcherPredicates:fromSession:completion:]_block_invoke
- ___72+[FBKDEDHelper fetchTextDataOnMatcherPredicates:fromSession:completion:]_block_invoke_2
- ___72+[FBKDEDHelper fetchTextDataOnMatcherPredicates:fromSession:completion:]_block_invoke_3
- ___72+[FBKDEDHelper fetchTextDataOnMatcherPredicates:fromSession:completion:]_block_invoke_4
- ___72+[FBKDEDHelper fetchTextDataOnMatcherPredicates:fromSession:completion:]_block_invoke_4.cold.1
- ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.328
- ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.330
- ___78+[FBKDEDHelper reconnectBugSessionWithIdentifier:deviceIdentifier:completion:]_block_invoke.116
- ___81+[FBKDEDHelper completeEnhancedLoggingWithFollowup:devicesController:completion:]_block_invoke.124
- ___81+[FBKDEDHelper completeEnhancedLoggingWithFollowup:devicesController:completion:]_block_invoke.127
- ___block_descriptor_129_e8_32s40s48s56s64s72bs80r88r96r104r112r120r_e17_v16?0"NSArray"8lr80l8s32l8s40l8r88l8r96l8s72l8s48l8s56l8s64l8r104l8r112l8r120l8
- ___block_descriptor_138_e8_32s40s48s56s64bs72r80r88r96r104r112r120r128r_e35_v24?0"DEDBugSession"8"NSError"16lr72l8s32l8s40l8r80l8r88l8s48l8r96l8s64l8s56l8r104l8r112l8r120l8r128l8
- ___block_descriptor_146_e8_32s40s48s56s64bs72r80r88r96r104r112r120r128r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8r80l8r88l8r96l8s64l8r104l8r112l8r120l8r128l8
- ___block_descriptor_40_e8_32s_e22_B16?0"DEDExtension"8ls32l8
- ___block_descriptor_64_e8_32s40bs48r56r_e15_v16?0"NSSet"8lr48l8r56l8s32l8s40l8
- ___block_descriptor_72_e8_32s40bs_e18_v16?0"NSString"8ls32l8s40l8
- ___block_descriptor_74_e8_32s40s48bs_e48_v24?0"DEDBugSessionConfiguration"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_74_e8_32s40s48s56bs_e24_v16?0"NSNotification"8ls32l8s40l8s56l8s48l8
- ___block_descriptor_82_e8_32s40s48s56bs64w_e19_v16?0"DEDDevice"8lw64l8s32l8s40l8s56l8s48l8
- ___block_literal_global.123
- ___block_literal_global.130
- ___block_literal_global.313
- ___block_literal_global.332
- ___block_literal_global.76
- _associated conformance 12FeedbackCore14FBKLoadingViewV7SwiftUI0D0AA4BodyAdEP_AdE
- _block_copy_helper.17
- _block_descriptor.19
- _block_destroy_helper.18
- _get_witness_table 7SwiftUI15ModifiedContentVyAA12ProgressViewVyAA05EmptyF0VAGGAA12_ScaleEffectVGAA0F0HPAhaLHPyHC_AjA0F8ModifierHPyHCHC.13
- _legalText.onceToken.310
- _objc_msgSend$_getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:
- _objc_msgSend$_getSessionWithIdentifier:configuration:device:getDetails:shouldGetSessionStatus:completion:
- _objc_msgSend$_startSessionByFirstPairingWithConfig:device:grouped:identifier:shouldGetDetails:shouldGetSessionStatus:completion:
- _objc_msgSend$beginPresubmissionCheck:
- _objc_msgSend$checkEnhancedLoggingAndSubmit
- _objc_msgSend$checkExplicitConfirmationAndSubmit
- _objc_msgSend$checkLegalAndSubmit
- _objc_msgSend$fetchTextDataOnMatcherPredicates:fromSession:completion:
- _objc_msgSend$isSubmissionPendingOnEnhancedLogging
- _objc_msgSend$localizedDataCollectedExplanation
- _objc_msgSend$localizedDataCollectedSummary
- _objc_msgSend$sessionCapabilities
- _objc_msgSend$setIsSubmissionPendingOnEnhancedLogging:
- _objc_msgSend$setLocalizedDataCollectedExplanation:
- _objc_msgSend$setLocalizedDataCollectedSummary:
- _objc_msgSend$unansweredRequiredModalQuestions
- _symbolic So21FBKModalConfigurationC
- _symbolic _____ 12FeedbackCore14FBKLoadingViewV
- _symbolic _____y_____ABG 7SwiftUI12ProgressViewV AA05EmptyD0V
- _symbolic _____y_____G 7SwiftUI19UIHostingControllerC 12FeedbackCore14FBKLoadingViewV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12FeedbackCore29EnhancedLoggingViewControllerC19DiagnosticOperationV
- _symbolic _____y_____y_____ACG_____G 7SwiftUI15ModifiedContentV AA12ProgressViewV AA05EmptyF0V AA12_ScaleEffectV
CStrings:
+ "-[FBKBugFormTableViewController beginSubmission:]"
+ "-[FBKBugFormTableViewController checkAnnotatedContentConsent:hasShownPresubmissionConsent:andContinue:]"
+ "-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]"
+ "-[FBKBugFormTableViewController checkMissingFiles:andContinue:]"
+ "-[FBKBugFormTableViewController checkPresubmissionLegalText:presentedDEConsent:andContinue:]"
+ "-[FBKBugFormTableViewController showMissingAnswersWithResult:sender:andContinue:]"
+ "Alert View title shown prior to making a feedback submission"
+ "Cancel button in alert asking user to agree to consent text. If user choses to go back they will be brought back to the feedback editing UI"
+ "Failed to load text data for DEs with error: [%{public}@]"
+ "Fetch DiagnosticExtensions text data"
+ "FilerForm is nil for session [%{public}@]. Will not fetch text data"
+ "Session [%{public}@] does not have the required capability. Cannot fetch text data"
+ "Showing DE consent"
+ "Showing annotated/dynamic consent text."
+ "Showing missing files prompt"
+ "Showing missing/disconnected device prompt"
+ "Showing pre-submission consent text."
+ "Submit button in alert asking user to agree to consent text"
+ "_getSessionWithIdentifier:configuration:dedDevice:filerForm:getDetails:shouldGetSessionStatus:completion:"
+ "_getSessionWithIdentifier:configuration:device:filerForm:getDetails:shouldGetSessionStatus:completion:"
+ "_startSessionByFirstPairingWithConfig:device:grouped:identifier:filerForm:shouldGetDetails:shouldGetSessionStatus:completion:"
+ "beginSubmission:"
+ "checkAnnotatedContentConsent:hasShownPresubmissionConsent:andContinue:"
+ "checkDEConsent(sender:andContinue:)"
+ "checkDEConsent:continueHandler:"
+ "checkDeviceConnectivity:andContinue:"
+ "checkMissingFiles:andContinue:"
+ "checkPresubmissionLegalText:presentedDEConsent:andContinue:"
+ "com.apple.Keynote"
+ "com.apple.Numbers"
+ "com.apple.Pages"
+ "deConsentTextsForGatheringAttachments"
+ "ded-helper"
+ "fetchDETextDataWithFilerForm:fromSession:configuration:completion:"
+ "localizedCustomerConsentText"
+ "presentConsentTexts:presentedConsent:andContinue:"
+ "showMissingAnswersWithResult:sender:andContinue:"
+ "v72@0:8@16@24@32@40@48B56B60@?64"
+ "validateAnswersAndPrepareForSubmission"
- "-[FBKDECollector fetchTextDataOnMatcherPredicates:completion:]"
- "All given matchers already have cached data"
- "B16@?0@\"DEDExtension\"8"
- "Checking EL before submission on FR: %d"
- "Could not find collection for platform %{public}s"
- "EL FilePredicate contains mixed platforms. This is not yet supported"
- "Enhanced Logging session has no matcher predicates"
- "Found unanswered modal questions [%{public}@]. Showing [%{public}@]"
- "Launched EL UI for question without modal configuration"
- "No capabilities found. Cannot [%{public}s]"
- "No matchers given. Cannot fetch text data"
- "Session [%{public}@] does not have the required capability. Cannot [%{public}s]"
- "TB,N,V_isSubmissionPendingOnEnhancedLogging"
- "Will try loading text data from collection: %s"
- "_getSessionWithIdentifier:configuration:dedDevice:getDetails:shouldGetSessionStatus:completion:"
- "_getSessionWithIdentifier:configuration:device:getDetails:shouldGetSessionStatus:completion:"
- "_isSubmissionPendingOnEnhancedLogging"
- "_startSessionByFirstPairingWithConfig:device:grouped:identifier:shouldGetDetails:shouldGetSessionStatus:completion:"
- "beginPresubmissionCheck:"
- "checkEnhancedLoggingAndSubmit"
- "checkExplicitConfirmationAndSubmit"
- "checkLegalAndSubmit"
- "fetchTextDataOnMatcherPredicates:completion:"
- "fetchTextDataOnMatcherPredicates:fromSession:completion:"
- "hasCachedLocalizedDataFromExtension"
- "isSubmissionPendingOnEnhancedLogging"
- "localizedDataCollectedExplanation"
- "localizedDataCollectedSummary"
- "setIsSubmissionPendingOnEnhancedLogging:"
- "setLocalizedDataCollectedExplanation:"
- "setLocalizedDataCollectedSummary:"
- "v56@0:8@16@24@32B40B44@?48"

```
