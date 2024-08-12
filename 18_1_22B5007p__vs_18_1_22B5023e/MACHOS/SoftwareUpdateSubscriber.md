## SoftwareUpdateSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber`

```diff

-2082.0.43.0.1
-  __TEXT.__text: 0x4ff4
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x1e4
-  __TEXT.__objc_classname: 0x131
+2082.40.21.0.0
+  __TEXT.__text: 0x4e84
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x224
+  __TEXT.__objc_classname: 0x155
   __TEXT.__const: 0x28
-  __TEXT.__cstring: 0xa4a
-  __TEXT.__objc_methname: 0xe7a
-  __TEXT.__oslogstring: 0x715
+  __TEXT.__cstring: 0x986
+  __TEXT.__objc_methname: 0xe52
+  __TEXT.__oslogstring: 0x745
   __TEXT.__objc_methtype: 0x531
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x150
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x140
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x700
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__cfstring: 0x660
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0xda0
-  __DATA.__objc_selrefs: 0x388
+  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__objc_arraydata: 0x38
+  __DATA_CONST.__objc_arrayobj: 0x90
+  __DATA.__objc_const: 0xe30
+  __DATA.__objc_selrefs: 0x390
   __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0x1e0
+  __DATA.__objc_data: 0x230
   __DATA.__data: 0x240
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 35
-  Symbols:   568
-  CStrings:  314
+  Functions: 39
+  Symbols:   600
+  CStrings:  311
 
Symbols:
+ +[RMModelStatusSoftwareUpdateDeviceID statusItemType]
+ +[RMModelStatusSoftwareUpdateDeviceID statusItemType]
+ +[RMModelStatusSoftwareUpdateDeviceID supportedOS]
+ +[RMModelStatusSoftwareUpdateDeviceID supportedOS]
+ +[SoftwareUpdateStatus supportedStatusClasses]
+ +[SoftwareUpdateStatus supportedStatusClasses]
+ -[RMModelStatusSoftwareUpdateDeviceID isArrayValue]
+ -[RMModelStatusSoftwareUpdateDeviceID isArrayValue]
+ /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/RMModelStatusSoftwareUpdateDeviceID.o
+ /Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate_SUCore/SoftwareUpdateSubscriber/Models/Status/
+ RMModelStatusSoftwareUpdateDeviceID.m
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_RMModelStatusBase
+ _OBJC_CLASS_$_RMModelStatusSoftwareUpdateDeviceID
+ _OBJC_CLASS_$_RMModelStatusSoftwareUpdateDeviceID
+ _OBJC_CLASS_$_RMModelStatusSoftwareUpdateFailureReason
+ _OBJC_CLASS_$_RMModelStatusSoftwareUpdateInstallReason
+ _OBJC_CLASS_$_RMModelStatusSoftwareUpdateInstallState
+ _OBJC_CLASS_$_RMModelStatusSoftwareUpdatePendingVersion
+ _OBJC_CLASS_$_SUUtility
+ _OBJC_METACLASS_$_RMModelStatusBase
+ _OBJC_METACLASS_$_RMModelStatusSoftwareUpdateDeviceID
+ _OBJC_METACLASS_$_RMModelStatusSoftwareUpdateDeviceID
+ _SUCorePolicyDDMStatusKeyDeviceID
+ __OBJC_$_CLASS_METHODS_RMModelStatusSoftwareUpdateDeviceID
+ __OBJC_$_INSTANCE_METHODS_RMModelStatusSoftwareUpdateDeviceID
+ __OBJC_CLASS_RO_$_RMModelStatusSoftwareUpdateDeviceID
+ __OBJC_CLASS_RO_$_RMModelStatusSoftwareUpdateDeviceID
+ __OBJC_METACLASS_RO_$_RMModelStatusSoftwareUpdateDeviceID
+ __OBJC_METACLASS_RO_$_RMModelStatusSoftwareUpdateDeviceID
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$currentProductType
+ _objc_msgSend$setObject:forKeyedSubscript:
- _OBJC_CLASS_$_NSNumber
- _SUCorePolicyDDMGlobalSettingAdminInstallRequiredKey
- _SUCorePolicyDDMGlobalSettingAutomaticallyInstallSystemAndSecurityUpdatesKey
- _SUCorePolicyDDMGlobalSettingMajorOSDeferralPeriodKey
- _SUCorePolicyDDMGlobalSettingMinorOSDeferralPeriodKey
- _SUCorePolicyDDMGlobalSettingSystemUpdatesDeferralPeriodKey
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- _objc_msgSend$numberWithInt:
- _objc_msgSend$payloadAllowStandardUserOSUpdates
- _objc_msgSend$payloadInstallSecurityUpdate
- _objc_msgSend$payloadMajorPeriodInDays
- _objc_msgSend$payloadMinorPeriodInDays
- _objc_msgSend$payloadSystemPeriodInDays
- _objc_retain_x1
- _objc_retain_x22
CStrings:
+ "%!s(MISSING): %!{(MISSING)public}@ is invalid, not adding key (%!{(MISSING)public}@)"
+ "%!s(MISSING): ANOMALY: No date found for declaration? %!{(MISSING)public}@, date: %!{(MISSING)public}@, formattedDateString: %!{(MISSING)public}@"
+ "%!s(MISSING): Error unenrolling device %!{(MISSING)public}@"
+ "RMModelStatusSoftwareUpdateDeviceID"
+ "addEntriesFromDictionary:"
+ "currentProductType"
+ "isArrayValue"
+ "q"
+ "setObject:forKeyedSubscript:"
+ "softwareupdate.device-id"
+ "statusItemType"
+ "supportedOS"
- "%!s(MISSING): %!@(MISSING) is invalid, not adding key (%!@(MISSING))"
- "%!s(MISSING): ANOMALY: No date found for declaration? %!@(MISSING), date: %!@(MISSING), formattedDateString: %!@(MISSING)"
- "%!s(MISSING): Error unenrolling device %!@(MISSING)"
- "SU_CONFIGURATION_ALLOW_STANDARD"
- "SU_CONFIGURATION_AUTOMATIC_ACTIONS_INSTALL_SECURITY_UPDATES"
- "SU_CONFIGURATION_DEFERRALS_MAJOR"
- "SU_CONFIGURATION_DEFERRALS_MINOR"
- "SU_CONFIGURATION_DEFERRALS_SYSTEM"
- "allow standard user OS updates"
- "numberWithInt:"
- "payloadAllowStandardUserOSUpdates"
- "payloadInstallSecurityUpdate"
- "payloadMajorPeriodInDays"
- "payloadMinorPeriodInDays"
- "payloadSystemPeriodInDays"

```
