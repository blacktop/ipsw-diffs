## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

 659.1.0.0.0
-  __TEXT.__text: 0x89820
+  __TEXT.__text: 0x8a3dc
   __TEXT.__auth_stubs: 0xdc0
-  __TEXT.__objc_methlist: 0x8d6c
+  __TEXT.__objc_methlist: 0x8dec
   __TEXT.__const: 0x858
   __TEXT.__dlopen_cstrs: 0x649
-  __TEXT.__cstring: 0x80d4
+  __TEXT.__cstring: 0x81e4
   __TEXT.__constg_swiftt: 0x2c8
   __TEXT.__swift5_typeref: 0x2ae
   __TEXT.__swift5_fieldmd: 0xe8

   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__oslogstring: 0x666c
+  __TEXT.__oslogstring: 0x6703
   __TEXT.__gcc_except_tab: 0x1a30
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x20c0
+  __TEXT.__unwind_info: 0x20e0
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_classname: 0x13f6
-  __TEXT.__objc_methname: 0x13bc9
+  __TEXT.__objc_methname: 0x13e8d
   __TEXT.__objc_methtype: 0x2973
-  __TEXT.__objc_stubs: 0xdae0
-  __DATA_CONST.__got: 0x968
-  __DATA_CONST.__const: 0x1120
+  __TEXT.__objc_stubs: 0xdca0
+  __DATA_CONST.__got: 0x978
+  __DATA_CONST.__const: 0x1148
   __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4bf8
+  __DATA_CONST.__objc_selrefs: 0x4c98
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x190
   __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__const: 0x628
-  __AUTH_CONST.__cfstring: 0x6bc0
-  __AUTH_CONST.__objc_const: 0xedf8
+  __AUTH_CONST.__cfstring: 0x6d00
+  __AUTH_CONST.__objc_const: 0xee58
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x1c30
   __AUTH.__data: 0x298
-  __DATA.__objc_ivar: 0x5d0
+  __DATA.__objc_ivar: 0x5d8
   __DATA.__data: 0xb38
   __DATA.__bss: 0x7f0
   __DATA_DIRTY.__objc_ivar: 0x508

   - /System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 25DC25D9-7EB0-3CE3-9837-E9EE3B382A81
-  Functions: 3115
-  Symbols:   10197
-  CStrings:  6383
+  UUID: AA4738A6-CB88-3455-864F-08944435D3E1
+  Functions: 3129
+  Symbols:   10244
+  CStrings:  6431
 
Symbols:
+ -[PSUICoreTelephonyRadioCache canSetTARandomization:]
+ -[PSUICoreTelephonyRadioCache getTARandomizationSetting:]
+ -[PSUICoreTelephonyRadioCache setTARandomization:enabled:]
+ -[PSUIDataModeSubgroup createTARandomizationSettingChangeAlertForDescriptor:enabled:]
+ -[PSUIDataModeSubgroup createTARandomizationSpecifiersIfNeeded]
+ -[PSUIDataModeSubgroup isTARandomizationEnabled]
+ -[PSUIDataModeSubgroup setTARandomizationEnabled:]
+ -[PSUIDataModeSubgroup setTaRandomizationGroupSpecifier:]
+ -[PSUIDataModeSubgroup setTaRandomizationSpecifier:]
+ -[PSUIDataModeSubgroup taRandomizationGroupSpecifier]
+ -[PSUIDataModeSubgroup taRandomizationSpecifier]
+ _OBJC_CLASS_$_FBSShutdownOptions
+ _OBJC_CLASS_$_FBSSystemService
+ _OBJC_IVAR_$_PSUIDataModeSubgroup._taRandomizationGroupSpecifier
+ _OBJC_IVAR_$_PSUIDataModeSubgroup._taRandomizationSpecifier
+ ___85-[PSUIDataModeSubgroup createTARandomizationSettingChangeAlertForDescriptor:enabled:]_block_invoke
+ ___85-[PSUIDataModeSubgroup createTARandomizationSettingChangeAlertForDescriptor:enabled:]_block_invoke_2
+ ___85-[PSUIDataModeSubgroup createTARandomizationSettingChangeAlertForDescriptor:enabled:]_block_invoke_3
+ ___block_descriptor_49_e8_32s40s_e23_v16?0"UIAlertAction"8ls32l8s40l8
+ _objc_msgSend$canSetTARandomization:
+ _objc_msgSend$createTARandomizationSettingChangeAlertForDescriptor:enabled:
+ _objc_msgSend$createTARandomizationSpecifiersIfNeeded
+ _objc_msgSend$getSupportsTARandomization:error:
+ _objc_msgSend$getTARandomizationSetting:
+ _objc_msgSend$getTARandomizationSetting:error:
+ _objc_msgSend$initWithReason:
+ _objc_msgSend$reloadSpecifierID:
+ _objc_msgSend$setRebootType:
+ _objc_msgSend$setSource:
+ _objc_msgSend$setTARandomization:enabled:
+ _objc_msgSend$setTARandomizationUserSetting:enabled:
+ _objc_msgSend$sharedService
+ _objc_msgSend$shutdownWithOptions:
CStrings:
+ "Error fetching TA Randomization setting: %@"
+ "Error fetching TA Randomization support status: %@"
+ "Error setting TA randomization setting to %@, error: %@"
+ "Limit Precise Location Setting Changed"
+ "S"
+ "T@\"PSSpecifier\",&,N,V_taRandomizationGroupSpecifier"
+ "T@\"PSSpecifier\",&,N,V_taRandomizationSpecifier"
+ "TAR"
+ "TARandomizationGroupSpecifier"
+ "TARandomizationWithoutReboot"
+ "TA_RANDOMIZATION"
+ "TA_RANDOMIZATION_ALERT_BODY"
+ "TA_RANDOMIZATION_ALERT_TITLE"
+ "TA_RANDOMIZATION_CANCEL"
+ "TA_RANDOMIZATION_FOOTER"
+ "TA_RANDOMIZATION_RESTART"
+ "TA_RANDOMIZATION_TITLE"
+ "_taRandomizationGroupSpecifier"
+ "_taRandomizationSpecifier"
+ "canSetTARandomization:"
+ "createTARandomizationSettingChangeAlertForDescriptor:enabled:"
+ "createTARandomizationSpecifiersIfNeeded"
+ "getSupportsTARandomization:error:"
+ "getTARandomizationSetting:"
+ "getTARandomizationSetting:error:"
+ "initWithReason:"
+ "isTARandomizationEnabled"
+ "reloadSpecifierID:"
+ "setRebootType:"
+ "setSource:"
+ "setTARandomization:enabled:"
+ "setTARandomizationEnabled:"
+ "setTARandomizationUserSetting:enabled:"
+ "setTaRandomizationGroupSpecifier:"
+ "setTaRandomizationSpecifier:"
+ "sharedService"
+ "shutdownWithOptions:"
+ "taRandomizationGroupSpecifier"
+ "taRandomizationSpecifier"

```
