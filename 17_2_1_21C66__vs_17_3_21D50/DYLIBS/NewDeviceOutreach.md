## NewDeviceOutreach

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach`

```diff

-407.8.0.0.0
-  __TEXT.__text: 0x136a0
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x11a0
+407.15.0.0.0
+  __TEXT.__text: 0x149b8
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_methlist: 0x1250
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x19ee
-  __TEXT.__oslogstring: 0x143e
-  __TEXT.__gcc_except_tab: 0x334
-  __TEXT.__unwind_info: 0x43c
-  __TEXT.__objc_classname: 0x10f
-  __TEXT.__objc_methname: 0x4bd1
-  __TEXT.__objc_methtype: 0x620
-  __TEXT.__objc_stubs: 0x3120
+  __TEXT.__cstring: 0x1b63
+  __TEXT.__oslogstring: 0x14de
+  __TEXT.__gcc_except_tab: 0x3ec
+  __TEXT.__unwind_info: 0x454
+  __TEXT.__objc_classname: 0x124
+  __TEXT.__objc_methname: 0x4cb1
+  __TEXT.__objc_methtype: 0x6c9
+  __TEXT.__objc_stubs: 0x3240
   __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1fd0
-  __DATA_CONST.__objc_selrefs: 0xfe0
+  __DATA_CONST.__objc_const: 0x2a18
+  __DATA_CONST.__objc_selrefs: 0xff8
   __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__cfstring: 0x1e20
   __AUTH_CONST.__objc_const: 0x500
-  __AUTH_CONST.__cfstring: 0x1d80
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH_CONST.__auth_got: 0x2c0
   __AUTH.__objc_data: 0x320
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x180
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x1b4
-  __DATA.__data: 0x1e0
+  __DATA.__objc_superrefs: 0x38
+  __DATA.__objc_ivar: 0x1cc
+  __DATA.__data: 0x240
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A52CC0DB-8F38-3F10-89A3-4B025CA7C884
-  Functions: 526
-  Symbols:   1909
-  CStrings:  1513
+  UUID: A69CF8BD-E09C-3D4E-AB17-AFB36B0BB2A5
+  Functions: 545
+  Symbols:   1984
+  CStrings:  1544
 
Symbols:
+ +[NDOUtilities dateWithEpochNumber:]
+ +[NDOUtilities daysFromDate:]
+ -[NDODevice acOfferEligibleUntil]
+ -[NDODevice deviceDesc]
+ -[NDODevice parentId]
+ -[NDODevice pfcId]
+ -[NDODevice pgfId]
+ -[NDODevice setAcOfferEligibleUntil:]
+ -[NDODevice setDeviceDesc:]
+ -[NDODevice setParentId:]
+ -[NDODevice setPfcId:]
+ -[NDODevice setPgfId:]
+ -[NDODevice setSgId:]
+ -[NDODevice sgId]
+ -[NDOManager .cxx_destruct]
+ -[NDOManager _getDeviceListForLocalDevices:sessionID:params:completionBlock:]
+ -[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]
+ -[NDOManager init]
+ -[NDOManager payloadDictionaryForDeviceInfo:atIndex:]
+ -[NDOManager payloadFrom:atIndex:device:]
+ GCC_except_table12
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table46
+ GCC_except_table57
+ GCC_except_table9
+ _OBJC_IVAR_$_NDODevice._acOfferEligibleUntil
+ _OBJC_IVAR_$_NDODevice._deviceDesc
+ _OBJC_IVAR_$_NDODevice._parentId
+ _OBJC_IVAR_$_NDODevice._pfcId
+ _OBJC_IVAR_$_NDODevice._pgfId
+ _OBJC_IVAR_$_NDODevice._sgId
+ _OBJC_IVAR_$_NDOManager.workingQueue
+ __OBJC_$_INSTANCE_VARIABLES_NDOManager
+ __OBJC_$_PROP_LIST_SalesPayloadProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SalesPayloadProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SalesPayloadProvider
+ __OBJC_$_PROTOCOL_REFS_SalesPayloadProvider
+ __OBJC_LABEL_PROTOCOL_$_SalesPayloadProvider
+ __OBJC_PROTOCOL_$_SalesPayloadProvider
+ ___103-[NDOManager getDeviceInfoForSerialNumber:usingPolicy:sessionID:params:andForcePostFollowup:withReply:]_block_invoke.37
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.87
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.90
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.93
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.cold.1
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke_2
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke_2.cold.1
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke_3
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke_4
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke_5
+ ___27-[NDOManager defaultDevice]_block_invoke.29
+ ___27-[NDOManager pairedWatches]_block_invoke.31
+ ___29-[NDOManager pairedBTDevices]_block_invoke.33
+ ___29-[NDOManager webURLOverride:]_block_invoke.11
+ ___31-[NDOManager ulWebURLOverride:]_block_invoke.13
+ ___35-[NDOManager apsSupportedOverride:]_block_invoke.14
+ ___38-[NDOManager checkIsAvailableInStore:]_block_invoke.6
+ ___41-[NDOManager appleAccountAddedWithReply:]_block_invoke.2
+ ___44-[NDOManager appSupportDictionaryWithReply:]_block_invoke.10
+ ___46-[NDOManager scheduleOutreachAfter:withReply:]_block_invoke.4
+ ___48-[NDOManager getDecodedParamsForPath:withReply:]_block_invoke.28
+ ___56-[NDOManager dismissFollowUpForSerialNumber:completion:]_block_invoke.100
+ ___56-[NDOManager getDefaultDeviceInfoUsingForceCachedPolicy]_block_invoke.34
+ ___56-[NDOManager getDefaultDeviceInfoUsingPolicy:withReply:]_block_invoke.35
+ ___60-[NDOManager dismissNotificationForSerialNumber:completion:]_block_invoke.101
+ ___65-[NDOManager getDeviceInfoUsingForceCachedPolicyForSerialNumber:]_block_invoke.36
+ ___68-[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.98
+ ___75-[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.99
+ ___77-[NDOManager _getDeviceListForLocalDevices:sessionID:params:completionBlock:]_block_invoke
+ ___77-[NDOManager _getDeviceListForLocalDevices:sessionID:params:completionBlock:]_block_invoke.95
+ ___77-[NDOManager _getDeviceListForLocalDevices:sessionID:params:completionBlock:]_block_invoke.cold.1
+ ___80-[NDOManager getAllFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.97
+ ___84-[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.96
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_113_e8_32s40s48s56s64bs72bs80bs88r96r104r_e5_v8?0ls64l8r88l8s32l8s72l8r96l8r104l8s40l8s48l8s80l8s56l8
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSArray"8"NSString"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e26_v32?0"NDODevice"8Q16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e23_v16?0"NDODeviceInfo"8ls48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e40_v32?0"NDODevice"8"NDODeviceInfo"16Q24ls32l8r64l8s56l8r72l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e26_v32?0"NDODevice"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs_e23_v16?0"NDODeviceInfo"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_97_e8_32s40s48s56s64bs72bs80bs_e30_v24?0"NSArray"8"NSString"16ls32l8s40l8s64l8s72l8s48l8s56l8s80l8
+ _objc_msgSend$_getDeviceListForLocalDevices:sessionID:params:completionBlock:
+ _objc_msgSend$acOfferDisplayDate
+ _objc_msgSend$agsULURL
+ _objc_msgSend$dateWithEpochNumber:
+ _objc_msgSend$daysFromDate:
+ _objc_msgSend$deviceDesc
+ _objc_msgSend$getDeviceListForLocalDevices:sessionID:params:withReply:
+ _objc_msgSend$getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:
+ _objc_msgSend$parentId
+ _objc_msgSend$payloadDictionaryForDeviceInfo:atIndex:
+ _objc_msgSend$payloadFrom:atIndex:device:
+ _objc_msgSend$pfcId
+ _objc_msgSend$pgfId
+ _objc_msgSend$sgId
+ _objc_retain_x28
+ _objc_retain_x5
- +[NDOWarranty warrantyWithDictionary:serialNumber:]
- -[NDOWarranty _dateWithEpochNumber:]
- -[NDOWarranty initWithDictionary:serialNumber:]
- -[NDOWarranty serialNumber]
- -[NDOWarranty setSerialNumber:]
- GCC_except_table11
- GCC_except_table25
- GCC_except_table30
- GCC_except_table33
- GCC_except_table36
- GCC_except_table39
- GCC_except_table45
- GCC_except_table52
- GCC_except_table8
- _OBJC_IVAR_$_NDOWarranty._serialNumber
- ___103-[NDOManager getDeviceInfoForSerialNumber:usingPolicy:sessionID:params:andForcePostFollowup:withReply:]_block_invoke.36
- ___27-[NDOManager defaultDevice]_block_invoke.28
- ___27-[NDOManager pairedWatches]_block_invoke.30
- ___29-[NDOManager pairedBTDevices]_block_invoke.32
- ___29-[NDOManager webURLOverride:]_block_invoke.10
- ___31-[NDOManager ulWebURLOverride:]_block_invoke.12
- ___35-[NDOManager apsSupportedOverride:]_block_invoke.13
- ___38-[NDOManager checkIsAvailableInStore:]_block_invoke.5
- ___41-[NDOManager appleAccountAddedWithReply:]_block_invoke.1
- ___44-[NDOManager appSupportDictionaryWithReply:]_block_invoke.9
- ___46-[NDOManager scheduleOutreachAfter:withReply:]_block_invoke.3
- ___48-[NDOManager getDecodedParamsForPath:withReply:]_block_invoke.27
- ___56-[NDOManager dismissFollowUpForSerialNumber:completion:]_block_invoke.60
- ___56-[NDOManager getDefaultDeviceInfoUsingForceCachedPolicy]_block_invoke.33
- ___56-[NDOManager getDefaultDeviceInfoUsingPolicy:withReply:]_block_invoke.34
- ___60-[NDOManager dismissNotificationForSerialNumber:completion:]_block_invoke.61
- ___65-[NDOManager getDeviceInfoUsingForceCachedPolicyForSerialNumber:]_block_invoke.35
- ___68-[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.58
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke.54
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke.54.cold.1
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke.55
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke.55.cold.1
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_2
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_3
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_4
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_5
- ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_6
- ___75-[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.59
- ___80-[NDOManager getAllFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.57
- ___84-[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.56
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104s_e23_v16?0"NDODeviceInfo"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_56_e8_32bs40bs48r_e17_v16?0"NSArray"8ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e23_v16?0"NDODeviceInfo"8ls32l8s40l8s48l8
- ___block_descriptor_96_e8_32s40s48s56s64s72bs80r88r_e17_v16?0"NSArray"8lr80l8s32l8s40l8s48l8s56l8s64l8r88l8s72l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e26_v32?0"NDODevice"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- _objc_msgSend$_dateWithEpochNumber:
- _objc_msgSend$deviceForSN:
- _objc_msgSend$getDeviceListForLocalDevices:sessionID:withReply:
- _objc_msgSend$initWithDictionary:serialNumber:
- _objc_msgSend$warrantyWithDictionary:serialNumber:
- _objc_retain_x9
CStrings:
+ "\x13\x12\x19"
+ "%s Skipping APPLEID Device %@"
+ "%s:%d salesInfoReply salesURL:%@ agsULUrl:%@ %@"
+ "%{public}s: sn: %@ sn2: %@ %@"
+ "%{public}s:%d completionBlock"
+ "%{public}s:%d deviceInfoReply"
+ "%{public}s:%d salesInfoReply"
+ "+[NDOWarranty warrantyWithDictionary:]"
+ "-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke"
+ "-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke_2"
+ "-[NDOManager payloadFrom:atIndex:device:]"
+ "/\x0f\x02\x13\x1f\v("
+ "@\"NSDate\"16@0:8"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@32@0:8@16q24"
+ "@40@0:8@16q24@32"
+ "I24@0:8@16"
+ "PRIMARY"
+ "SalesPayloadProvider"
+ "T@\"NSDate\",R"
+ "_getDeviceListForLocalDevices:sessionID:params:completionBlock:"
+ "dateWithEpochNumber:"
+ "daysFromDate:"
+ "deviceSeq"
+ "eligibilityRemainingInDays"
+ "getDeviceListForLocalDevices:sessionID:params:withReply:"
+ "getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:"
+ "payloadDictionaryForDeviceInfo:atIndex:"
+ "payloadFrom:atIndex:device:"
+ "serialNum"
+ "v24@?0@\"NSArray\"8@\"NSString\"16"
+ "v32@?0@\"NDODevice\"8@\"NDODeviceInfo\"16Q24"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSString\">40"
+ "v48@0:8@16@24@32@?40"
+ "v76@0:8@16@24Q32@40B48@?52@?60@?68"
+ "workingQueue"
- "\x13\x12\x13"
- "%{public}s"
- "+[NDOWarranty warrantyWithDictionary:serialNumber:]"
- "-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_6"
- "/\x0f\x02\x13\x1f\v)"
- "Device list success (%lu)"
- "_dateWithEpochNumber:"
- "getDeviceListForLocalDevices:sessionID:withReply:"
- "initWithDictionary:serialNumber:"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
- "warrantyWithDictionary:serialNumber:"

```
