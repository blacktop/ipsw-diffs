## NewDeviceOutreach

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach`

```diff

-407.17.0.0.0
-  __TEXT.__text: 0x149cc
+407.25.0.0.0
+  __TEXT.__text: 0x14eac
   __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x1250
+  __TEXT.__objc_methlist: 0x12b0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x1b70
-  __TEXT.__oslogstring: 0x14de
-  __TEXT.__gcc_except_tab: 0x3ec
-  __TEXT.__unwind_info: 0x454
-  __TEXT.__objc_classname: 0x124
-  __TEXT.__objc_methname: 0x4cc5
-  __TEXT.__objc_methtype: 0x6c9
-  __TEXT.__objc_stubs: 0x3240
+  __TEXT.__cstring: 0x1be0
+  __TEXT.__oslogstring: 0x14f2
+  __TEXT.__gcc_except_tab: 0x410
+  __TEXT.__unwind_info: 0x468
+  __TEXT.__objc_classname: 0x157
+  __TEXT.__objc_methname: 0x4d69
+  __TEXT.__objc_methtype: 0x790
+  __TEXT.__objc_stubs: 0x32a0
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x738
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2a18
-  __DATA_CONST.__objc_selrefs: 0xff8
+  __DATA_CONST.__objc_const: 0x2f28
+  __DATA_CONST.__objc_selrefs: 0x1020
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x180
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x1e20
-  __AUTH_CONST.__objc_const: 0x500
+  __AUTH_CONST.__cfstring: 0x1e60
+  __AUTH_CONST.__objc_const: 0x548
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x2c0
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1cc
-  __DATA.__data: 0x240
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x1d4
+  __DATA.__data: 0x2a0
+  __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0CF43E2-E886-3C59-BA4C-CA7EF4B0B381
-  Functions: 545
-  Symbols:   1984
-  CStrings:  1546
+  UUID: F77B4DCE-AE56-3E7C-A70F-552CF3536F66
+  Functions: 556
+  Symbols:   2030
+  CStrings:  1567
 
Symbols:
+ +[NDOServerVersionUtilities clientConfig]
+ -[NDOClientConfiguration generalAboutPolicy]
+ -[NDOClientConfiguration initWithConfigDictionary:]
+ -[NDOClientConfiguration setGeneralAboutPolicy:]
+ -[NDODevice acLocalizedUnlinkedPlanStatusLabel]
+ -[NDODevice setAcLocalizedUnlinkedPlanStatusLabel:]
+ -[NDOManager clientConfiguration]
+ GCC_except_table43
+ GCC_except_table49
+ GCC_except_table60
+ _OBJC_CLASS_$_NDOClientConfiguration
+ _OBJC_IVAR_$_NDOClientConfiguration._generalAboutPolicy
+ _OBJC_IVAR_$_NDODevice._acLocalizedUnlinkedPlanStatusLabel
+ _OBJC_METACLASS_$_NDOClientConfiguration
+ __OBJC_$_INSTANCE_METHODS_NDOClientConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_NDOClientConfiguration
+ __OBJC_$_PROP_LIST_NDOClientConfiguration
+ __OBJC_$_PROP_LIST_NDOManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NDOCoverageCentralVCManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NDOCoverageCentralVCManager
+ __OBJC_$_PROTOCOL_REFS_NDOCoverageCentralVCManager
+ __OBJC_CLASS_PROTOCOLS_$_NDOManager
+ __OBJC_CLASS_RO_$_NDOClientConfiguration
+ __OBJC_LABEL_PROTOCOL_$_NDOCoverageCentralVCManager
+ __OBJC_METACLASS_RO_$_NDOClientConfiguration
+ __OBJC_PROTOCOL_$_NDOCoverageCentralVCManager
+ ___103-[NDOManager getDeviceInfoForSerialNumber:usingPolicy:sessionID:params:andForcePostFollowup:withReply:]_block_invoke.39
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.89
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.92
+ ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.95
+ ___27-[NDOManager defaultDevice]_block_invoke.31
+ ___27-[NDOManager pairedWatches]_block_invoke.33
+ ___29-[NDOManager pairedBTDevices]_block_invoke.35
+ ___33-[NDOManager clientConfiguration]_block_invoke
+ ___33-[NDOManager clientConfiguration]_block_invoke.29
+ ___33-[NDOManager clientConfiguration]_block_invoke.cold.1
+ ___56-[NDOManager dismissFollowUpForSerialNumber:completion:]_block_invoke.102
+ ___56-[NDOManager getDefaultDeviceInfoUsingForceCachedPolicy]_block_invoke.36
+ ___56-[NDOManager getDefaultDeviceInfoUsingPolicy:withReply:]_block_invoke.37
+ ___60-[NDOManager dismissNotificationForSerialNumber:completion:]_block_invoke.103
+ ___65-[NDOManager getDeviceInfoUsingForceCachedPolicyForSerialNumber:]_block_invoke.38
+ ___68-[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.100
+ ___75-[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.101
+ ___77-[NDOManager _getDeviceListForLocalDevices:sessionID:params:completionBlock:]_block_invoke.97
+ ___80-[NDOManager getAllFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.99
+ ___84-[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.98
+ _objc_msgSend$acLocalizedUnlinkedPlanStatusLabel
+ _objc_msgSend$getClientConfigurationWithReply:
+ _objc_msgSend$initWithConfigDictionary:
+ _objc_msgSend$setGeneralAboutPolicy:
- GCC_except_table46
- GCC_except_table57
- ___103-[NDOManager getDeviceInfoForSerialNumber:usingPolicy:sessionID:params:andForcePostFollowup:withReply:]_block_invoke.37
- ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.87
- ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.90
- ___129-[NDOManager getDeviceListForLocalDevices:sessionID:policy:params:salesReplyOnly:salesInfoReply:deviceInfoReply:completionBlock:]_block_invoke.93
- ___27-[NDOManager defaultDevice]_block_invoke.29
- ___27-[NDOManager pairedWatches]_block_invoke.31
- ___29-[NDOManager pairedBTDevices]_block_invoke.33
- ___56-[NDOManager dismissFollowUpForSerialNumber:completion:]_block_invoke.100
- ___56-[NDOManager getDefaultDeviceInfoUsingForceCachedPolicy]_block_invoke.34
- ___56-[NDOManager getDefaultDeviceInfoUsingPolicy:withReply:]_block_invoke.35
- ___60-[NDOManager dismissNotificationForSerialNumber:completion:]_block_invoke.101
- ___65-[NDOManager getDeviceInfoUsingForceCachedPolicyForSerialNumber:]_block_invoke.36
- ___68-[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.98
- ___75-[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.99
- ___77-[NDOManager _getDeviceListForLocalDevices:sessionID:params:completionBlock:]_block_invoke.95
- ___80-[NDOManager getAllFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.97
- ___84-[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.96
- _objc_msgSend$displayStyle
CStrings:
+ "\x13\x12\x1a"
+ "%{public}s error:%@"
+ "-[NDOManager clientConfiguration]_block_invoke"
+ "@\"NDODevice\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "Device1,8218"
+ "Device1,8230"
+ "NDOClientConfiguration"
+ "NDOCoverageCentralVCManager"
+ "TQ,V_generalAboutPolicy"
+ "_generalAboutPolicy"
+ "alwaysRefreshGeneralAbout"
+ "clientConfig"
+ "clientConfiguration"
+ "generalAboutPolicy"
+ "getClientConfigurationWithReply:"
+ "initWithConfigDictionary:"
+ "setGeneralAboutPolicy:"
+ "v24@0:8@?<v@?@\"NSDictionary\">16"
+ "v76@0:8@\"NSArray\"16@\"NSString\"24Q32@\"NSString\"40B48@?<v@?@\"NSString\"@\"NSArray\"@\"NSString\">52@?<v@?@\"NSArray\">60@?<v@?@\"NSArray\">68"
- "\x13\x12\x19"
- "displayStyle"

```
