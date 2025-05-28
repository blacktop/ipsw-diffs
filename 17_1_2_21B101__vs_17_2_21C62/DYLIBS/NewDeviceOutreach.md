## NewDeviceOutreach

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach`

```diff

-405.0.0.0.0
-  __TEXT.__text: 0x110dc
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x1000
+407.8.0.0.0
+  __TEXT.__text: 0x136a0
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_methlist: 0x11a0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x15e8
-  __TEXT.__oslogstring: 0x13ab
-  __TEXT.__gcc_except_tab: 0x314
-  __TEXT.__unwind_info: 0x3dc
-  __TEXT.__objc_classname: 0xfb
-  __TEXT.__objc_methname: 0x4901
-  __TEXT.__objc_methtype: 0x5b3
-  __TEXT.__objc_stubs: 0x2dc0
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x5b8
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__cstring: 0x19ee
+  __TEXT.__oslogstring: 0x143e
+  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__unwind_info: 0x43c
+  __TEXT.__objc_classname: 0x10f
+  __TEXT.__objc_methname: 0x4bd1
+  __TEXT.__objc_methtype: 0x620
+  __TEXT.__objc_stubs: 0x3120
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1da0
-  __DATA_CONST.__objc_selrefs: 0xf18
+  __DATA_CONST.__objc_const: 0x1fd0
+  __DATA_CONST.__objc_selrefs: 0xfe0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__objc_const: 0x470
-  __AUTH_CONST.__cfstring: 0x1940
+  __AUTH_CONST.__objc_const: 0x500
+  __AUTH_CONST.__cfstring: 0x1d80
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x290
-  __AUTH.__objc_data: 0x2d0
+  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH.__objc_data: 0x320
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x160
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x190
+  __DATA.__objc_classrefs: 0x180
+  __DATA.__objc_superrefs: 0x30
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 479
-  Symbols:   1759
-  CStrings:  1161
+  Functions: 526
+  Symbols:   1909
+  CStrings:  1277
 
Symbols:
+ +[NDODevice deviceWithCBDevice:]
+ +[NDODevice deviceWithCBDevice:isVisibleInCC:]
+ +[NDODevice deviceWithDeviceListDevice:]
+ +[NDODeviceSection supportsSecureCoding]
+ -[NDODevice acLocalizedOfferStatusLabel]
+ -[NDODevice acOfferEligible]
+ -[NDODevice cachingPolicy]
+ -[NDODevice colorCode]
+ -[NDODevice coverageLocalizedLabel]
+ -[NDODevice covered]
+ -[NDODevice deviceImageUrl]
+ -[NDODevice initWithName:serialNumber:activationDate:deviceType:productID:productName:isVisibleInCC:cachingPolicy:]
+ -[NDODevice setAcLocalizedOfferStatusLabel:]
+ -[NDODevice setAcOfferEligible:]
+ -[NDODevice setCachingPolicy:]
+ -[NDODevice setColorCode:]
+ -[NDODevice setCoverageLocalizedLabel:]
+ -[NDODevice setCovered:]
+ -[NDODevice setDeviceImageUrl:]
+ -[NDODevice sourceFromDeviceType]
+ -[NDODevice updateWithWarranty:]
+ -[NDODeviceSection .cxx_destruct]
+ -[NDODeviceSection addDevice:]
+ -[NDODeviceSection description]
+ -[NDODeviceSection deviceForSN:]
+ -[NDODeviceSection deviceList]
+ -[NDODeviceSection encodeWithCoder:]
+ -[NDODeviceSection identifier]
+ -[NDODeviceSection initWithCoder:]
+ -[NDODeviceSection initWithLabel:identifier:]
+ -[NDODeviceSection label]
+ -[NDODeviceSection privateDeviceList]
+ -[NDODeviceSection setIdentifier:]
+ -[NDODeviceSection setLabel:]
+ -[NDODeviceSection setPrivateDeviceList:]
+ -[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]
+ -[NSMutableURLRequest(AccountHeaders) ndo_setDeviceListRequestBodyWithSerialNumber:localDevices:primaryAccount:]
+ -[NSMutableURLRequest(AccountHeaders) storeLocaleForAccount:]
+ -[NSMutableURLRequest(AccountHeaders) storeLocaleForAccount:].cold.1
+ GCC_except_table10
+ GCC_except_table52
+ _CBDeviceTypeToNSLocalizedString
+ _OBJC_CLASS_$_CBProductInfo
+ _OBJC_CLASS_$_NDODeviceSection
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_IVAR_$_NDODevice._acLocalizedOfferStatusLabel
+ _OBJC_IVAR_$_NDODevice._acOfferEligible
+ _OBJC_IVAR_$_NDODevice._cachingPolicy
+ _OBJC_IVAR_$_NDODevice._colorCode
+ _OBJC_IVAR_$_NDODevice._coverageLocalizedLabel
+ _OBJC_IVAR_$_NDODevice._covered
+ _OBJC_IVAR_$_NDODevice._deviceImageUrl
+ _OBJC_IVAR_$_NDODeviceSection._identifier
+ _OBJC_IVAR_$_NDODeviceSection._label
+ _OBJC_IVAR_$_NDODeviceSection._privateDeviceList
+ _OBJC_METACLASS_$_NDODeviceSection
+ __OBJC_$_CLASS_METHODS_NDODeviceSection
+ __OBJC_$_CLASS_PROP_LIST_NDODeviceSection
+ __OBJC_$_INSTANCE_METHODS_NDODeviceSection
+ __OBJC_$_INSTANCE_VARIABLES_NDODeviceSection
+ __OBJC_$_PROP_LIST_NDODeviceSection
+ __OBJC_CLASS_PROTOCOLS_$_NDODeviceSection
+ __OBJC_CLASS_RO_$_NDODeviceSection
+ __OBJC_METACLASS_RO_$_NDODeviceSection
+ ___112-[NSMutableURLRequest(AccountHeaders) ndo_setDeviceListRequestBodyWithSerialNumber:localDevices:primaryAccount:]_block_invoke
+ ___56-[NDOManager dismissFollowUpForSerialNumber:completion:]_block_invoke.60
+ ___60-[NDOManager dismissNotificationForSerialNumber:completion:]_block_invoke.61
+ ___68-[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.58
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke.54
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke.54.cold.1
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke.55
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke.55.cold.1
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_2
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_3
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_4
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_5
+ ___69-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_6
+ ___75-[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.59
+ ___80-[NDOManager getAllFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.57
+ ___84-[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.56
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104s_e23_v16?0"NDODeviceInfo"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_56_e8_32bs40bs48r_e17_v16?0"NSArray"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e23_v16?0"NDODeviceInfo"8ls32l8s40l8s48l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs80r88r_e17_v16?0"NSArray"8lr80l8s32l8s40l8s48l8s56l8s64l8r88l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e26_v32?0"NDODevice"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ _dispatch_async
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _objc_msgSend$acLocalizedOfferStatusLabel
+ _objc_msgSend$acOfferEligible
+ _objc_msgSend$addDevice:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$colorCode
+ _objc_msgSend$colorCodeBest
+ _objc_msgSend$coverageLocalizedLabel
+ _objc_msgSend$covered
+ _objc_msgSend$defaultDevice
+ _objc_msgSend$deviceForSN:
+ _objc_msgSend$deviceImageUrl
+ _objc_msgSend$deviceList
+ _objc_msgSend$deviceWithCBDevice:isVisibleInCC:
+ _objc_msgSend$deviceWithName:serialNumber:activationDate:deviceType:productID:productName:isVisibleInCC:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$getDeviceListForLocalDevices:sessionID:withReply:
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithLabel:identifier:
+ _objc_msgSend$initWithName:serialNumber:activationDate:deviceType:productID:productName:isVisibleInCC:cachingPolicy:
+ _objc_msgSend$label
+ _objc_msgSend$privateDeviceList
+ _objc_msgSend$productInfoWithProductID:
+ _objc_msgSend$setCachingPolicy:
+ _objc_msgSend$setColorCode:
+ _objc_msgSend$setPrivateDeviceList:
+ _objc_msgSend$storeLocaleForAccount:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$unarchivedArrayOfObjectsOfClass:fromData:error:
+ _objc_msgSend$updateWithWarranty:
+ _objc_retain_x9
- +[NDODevice deviceWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:]
- -[NDODevice initWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:isVisibleInCC:]
- -[NDODevice isICloudDevice]
- -[NDODevice setIsICloudDevice:]
- -[NSMutableURLRequest(AccountHeaders) addBAAAuthenticationHeadersWithSerialNumber:]
- -[NSMutableURLRequest(AccountHeaders) addStoreLocaleHeaderIfNeededForAccount:].cold.1
- GCC_except_table7
- _OBJC_IVAR_$_NDODevice._isICloudDevice
- ___56-[NDOManager dismissFollowUpForSerialNumber:completion:]_block_invoke.41
- ___60-[NDOManager dismissNotificationForSerialNumber:completion:]_block_invoke.42
- ___68-[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.39
- ___75-[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.40
- ___80-[NDOManager getAllFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.38
- ___84-[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.37
- _objc_msgSend$addBAAAuthenticationHeadersWithBody:
- _objc_msgSend$initWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:isVisibleInCC:
- _objc_msgSend$isICloudDevice
- _objc_msgSend$setIsICloudDevice:
CStrings:
+ "\x03"
+ "\x13\x12\x13"
+ "%@\n"
+ "%@ (%@):\n"
+ "%@ :: (%@) :: (%@) :: %@ - %@ :: (%@) :: %d"
+ "%lu"
+ "%{public}s"
+ "-[NDOManager getDeviceListForLocalDevices:sessionID:completionBlock:]_block_invoke_6"
+ "/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework"
+ "?"
+ "@\"NSMutableArray\""
+ "APPLE_ID"
+ "ATVRemote1,1"
+ "ATVRemote1,2"
+ "AirPods1,1"
+ "AirPods1,3"
+ "AirPodsPro1,1"
+ "ApGn"
+ "AppleID"
+ "AppleTV11,2"
+ "AppleTV5,3"
+ "AppleTV6,2"
+ "AudioAccessory1,1"
+ "AudioAccessory1,2"
+ "AudioAccessory5,1"
+ "BeatsSolo3,1"
+ "BeatsSoloPro1,1"
+ "BeatsStudio3,2"
+ "BeatsStudioBuds1,1"
+ "BeatsStudioBuds1,2"
+ "BeatsStudioPro1,1"
+ "BeatsX1,1"
+ "CBLocalizable"
+ "DEFAULT"
+ "Device list came back empty, falling to summarily call"
+ "Device list failed with %@, falling to summarily call "
+ "Device list success (%lu)"
+ "Device1,21760"
+ "Device1,8202"
+ "Device1,8208"
+ "Device1,8210"
+ "Device1,8211"
+ "Device1,8212"
+ "Device1,8213"
+ "Device1,8216"
+ "Device1,8228"
+ "HeGn"
+ "ICLOUD"
+ "Invalid"
+ "MORE_DEVICES"
+ "NDODeviceSection"
+ "NO_CACHE"
+ "OTHER"
+ "PowerBeats3,1"
+ "Powerbeats4,1"
+ "PowerbeatsPro1,1"
+ "T@\"NSArray\",R"
+ "T@\"NSMutableArray\",&,V_privateDeviceList"
+ "T@\"NSString\",&,V_identifier"
+ "T@\"NSString\",&,V_label"
+ "TB,V_cachingPolicy"
+ "THIS_DEVICE"
+ "Tq,V_colorCode"
+ "WATCH"
+ "_cachingPolicy"
+ "_colorCode"
+ "_identifier"
+ "_label"
+ "_privateDeviceList"
+ "addDevice:"
+ "apple_airpods_case"
+ "apple_magic_keyboard"
+ "apple_magic_mouse"
+ "apple_magic_trackpad"
+ "apple_mighty_mouse"
+ "apple_wireless_keyboard"
+ "apple_wireless_mouse"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "bundleWithIdentifier:"
+ "bundleWithPath:"
+ "cachePolicy"
+ "cachingPolicy"
+ "color"
+ "colorCode"
+ "colorCodeBest"
+ "com.apple.CoreBluetooth"
+ "com.apple.newdeviceoutreach.ndoagent.devicelist"
+ "coverageInfo"
+ "deviceForSN:"
+ "deviceList"
+ "deviceName"
+ "deviceWithCBDevice:"
+ "deviceWithCBDevice:isVisibleInCC:"
+ "deviceWithDeviceListDevice:"
+ "devicesInfo"
+ "dictionaryWithDictionary:"
+ "getDeviceListForLocalDevices:sessionID:completionBlock:"
+ "getDeviceListForLocalDevices:sessionID:withReply:"
+ "identifier"
+ "initWithLabel:identifier:"
+ "initWithName:serialNumber:activationDate:deviceType:productID:productName:isVisibleInCC:cachingPolicy:"
+ "label"
+ "localDevices"
+ "modelInfo"
+ "ndo_setDeviceListRequestBodyWithSerialNumber:localDevices:primaryAccount:"
+ "nickName"
+ "primarySN"
+ "privateDeviceList"
+ "productInfoWithProductID:"
+ "q"
+ "q16@0:8"
+ "setCachingPolicy:"
+ "setColorCode:"
+ "setPrivateDeviceList:"
+ "sourceFromDeviceType"
+ "storeLocaleForAccount:"
+ "stringWithUTF8String:"
+ "unarchivedArrayOfObjectsOfClass:fromData:error:"
+ "updateWithWarranty:"
+ "v24@0:8q16"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@16@24@?32"
- "\x13\x12"
- "%@ :: (%@) :: (%@) :: %@ - %@ :: (%@) :: %d :: %d"
- "TB,V_isICloudDevice"
- "_isICloudDevice"
- "addBAAAuthenticationHeadersWithSerialNumber:"
- "deviceWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:"
- "initWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:isVisibleInCC:"
- "isICloudDevice"
- "setIsICloudDevice:"

```
