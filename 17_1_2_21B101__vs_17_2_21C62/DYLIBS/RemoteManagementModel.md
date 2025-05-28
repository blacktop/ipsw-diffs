## RemoteManagementModel

> `/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel`

```diff

-500.25.2.2.0
-  __TEXT.__text: 0x4052c
+500.25.3.7.0
+  __TEXT.__text: 0x4068c
   __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x63c4
+  __TEXT.__objc_methlist: 0x63dc
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x3476
-  __TEXT.__unwind_info: 0xfb0
-  __TEXT.__objc_classname: 0x13d8
-  __TEXT.__objc_methname: 0xa657
-  __TEXT.__objc_methtype: 0xad3
+  __TEXT.__cstring: 0x347b
+  __TEXT.__unwind_info: 0xfc0
+  __TEXT.__objc_classname: 0x13e0
+  __TEXT.__objc_methname: 0xa633
+  __TEXT.__objc_methtype: 0xadb
   __TEXT.__objc_stubs: 0x4dc0
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x678
+  __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7d10
+  __DATA_CONST.__objc_const: 0x7d40
   __DATA_CONST.__objc_selrefs: 0x18c8
-  __DATA_CONST.__objc_arraydata: 0x22d8
-  __AUTH_CONST.__cfstring: 0x55e0
+  __DATA_CONST.__objc_arraydata: 0x22c8
+  __AUTH_CONST.__cfstring: 0x5660
   __AUTH_CONST.__objc_arrayobj: 0x3df8
   __AUTH_CONST.__objc_intobj: 0x1f38
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__objc_const: 0x120
+  __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__auth_got: 0x1a0
-  __AUTH.__objc_data: 0x50
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_classrefs: 0x478
   __DATA.__objc_superrefs: 0x320
-  __DATA.__objc_ivar: 0x698
+  __DATA.__objc_ivar: 0x69c
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x88
-  __DATA_DIRTY.__const: 0x640
-  __DATA_DIRTY.__objc_const: 0x4178
-  __DATA_DIRTY.__objc_data: 0x28a0
+  __DATA_DIRTY.__const: 0x620
+  __DATA_DIRTY.__objc_const: 0x40e8
+  __DATA_DIRTY.__objc_data: 0x2850
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2048
-  Symbols:   7274
-  CStrings:  2286
+  Functions: 2051
+  Symbols:   7277
+  CStrings:  2291
 
Symbols:
+ +[RMModelAppManagedDeclaration buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:includeInBackup:attributes:]
+ +[RMModelAppManagedDeclaration_InstallBehavior buildWithInstall:license:]
+ +[RMModelAppManagedDeclaration_InstallBehaviorLicense allowedPayloadKeys]
+ +[RMModelAppManagedDeclaration_InstallBehaviorLicense buildRequiredOnly]
+ +[RMModelAppManagedDeclaration_InstallBehaviorLicense buildWithVPPType:]
+ +[RMModelStatusAppManagedList buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:updateState:reasons:]
+ -[RMModelAppManagedDeclaration_InstallBehavior payloadLicense]
+ -[RMModelAppManagedDeclaration_InstallBehavior setPayloadLicense:]
+ -[RMModelAppManagedDeclaration_InstallBehaviorLicense .cxx_destruct]
+ -[RMModelAppManagedDeclaration_InstallBehaviorLicense copyWithZone:]
+ -[RMModelAppManagedDeclaration_InstallBehaviorLicense loadFromDictionary:serializationType:error:]
+ -[RMModelAppManagedDeclaration_InstallBehaviorLicense payloadVPPType]
+ -[RMModelAppManagedDeclaration_InstallBehaviorLicense serializeWithType:]
+ -[RMModelAppManagedDeclaration_InstallBehaviorLicense setPayloadVPPType:]
+ -[RMModelStatusAppManagedList setStatusReasons:]
+ -[RMModelStatusAppManagedList setStatusUpdateState:]
+ -[RMModelStatusAppManagedList statusReasons]
+ -[RMModelStatusAppManagedList statusUpdateState]
+ _OBJC_CLASS_$_RMModelAppManagedDeclaration_InstallBehaviorLicense
+ _OBJC_IVAR_$_RMModelAppManagedDeclaration_InstallBehavior._payloadLicense
+ _OBJC_IVAR_$_RMModelAppManagedDeclaration_InstallBehaviorLicense._payloadVPPType
+ _OBJC_IVAR_$_RMModelStatusAppManagedList._statusReasons
+ _OBJC_IVAR_$_RMModelStatusAppManagedList._statusUpdateState
+ _OBJC_METACLASS_$_RMModelAppManagedDeclaration_InstallBehaviorLicense
+ _RMModelAppManagedDeclaration_InstallBehaviorLicense_VPPType_device
+ _RMModelAppManagedDeclaration_InstallBehaviorLicense_VPPType_user
+ _RMModelAppManagedDeclaration_InstallBehavior_Install_optional
+ _RMModelAppManagedDeclaration_InstallBehavior_Install_required
+ _RMModelStatusAppManagedList_State_downloading
+ _RMModelStatusAppManagedList_State_promptingForConsent
+ _RMModelStatusAppManagedList_UpdateState_available
+ _RMModelStatusAppManagedList_UpdateState_failed
+ _RMModelStatusAppManagedList_UpdateState_promptingForUpdate
+ _RMModelStatusAppManagedList_UpdateState_promptingForUpdateLogin
+ _RMModelStatusAppManagedList_UpdateState_updating
+ __OBJC_$_CLASS_METHODS_RMModelAppManagedDeclaration_InstallBehaviorLicense
+ __OBJC_$_CLASS_PROP_LIST_RMModelAppManagedDeclaration_InstallBehaviorLicense
+ __OBJC_$_INSTANCE_METHODS_RMModelAppManagedDeclaration_InstallBehaviorLicense
+ __OBJC_$_INSTANCE_VARIABLES_RMModelAppManagedDeclaration_InstallBehaviorLicense
+ __OBJC_$_PROP_LIST_RMModelAppManagedDeclaration_InstallBehaviorLicense
+ __OBJC_CLASS_RO_$_RMModelAppManagedDeclaration_InstallBehaviorLicense
+ __OBJC_METACLASS_RO_$_RMModelAppManagedDeclaration_InstallBehaviorLicense
+ ___56-[RMModelStatusAppManagedList serializePayloadWithType:]_block_invoke
+ ___66-[RMModelAppManagedDeclaration_InstallBehavior serializeWithType:]_block_invoke
+ ___block_literal_global.284
+ __unnamed_array_storage.82
+ __unnamed_array_storage.85
+ __unnamed_array_storage.90
+ _objc_msgSend$payloadLicense
+ _objc_msgSend$payloadVPPType
+ _objc_msgSend$setPayloadLicense:
+ _objc_msgSend$setPayloadVPPType:
+ _objc_msgSend$setStatusUpdateState:
+ _objc_msgSend$statusUpdateState
- +[RMModelAppManagedDeclaration buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:removeBehavior:includeInBackup:attributes:]
- +[RMModelAppManagedDeclaration_InstallBehavior buildWithInstall:accountPromptAllowed:]
- +[RMModelAppManagedDeclaration_RemoveBehavior allowedPayloadKeys]
- +[RMModelAppManagedDeclaration_RemoveBehavior buildRequiredOnly]
- +[RMModelAppManagedDeclaration_RemoveBehavior buildWithRemovable:]
- +[RMModelStatusAppManagedList buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:]
- -[RMModelAppManagedDeclaration payloadRemoveBehavior]
- -[RMModelAppManagedDeclaration setPayloadRemoveBehavior:]
- -[RMModelAppManagedDeclaration_InstallBehavior payloadAccountPromptAllowed]
- -[RMModelAppManagedDeclaration_InstallBehavior setPayloadAccountPromptAllowed:]
- -[RMModelAppManagedDeclaration_RemoveBehavior .cxx_destruct]
- -[RMModelAppManagedDeclaration_RemoveBehavior copyWithZone:]
- -[RMModelAppManagedDeclaration_RemoveBehavior loadFromDictionary:serializationType:error:]
- -[RMModelAppManagedDeclaration_RemoveBehavior payloadRemovable]
- -[RMModelAppManagedDeclaration_RemoveBehavior serializeWithType:]
- -[RMModelAppManagedDeclaration_RemoveBehavior setPayloadRemovable:]
- _OBJC_CLASS_$_RMModelAppManagedDeclaration_RemoveBehavior
- _OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadRemoveBehavior
- _OBJC_IVAR_$_RMModelAppManagedDeclaration_InstallBehavior._payloadAccountPromptAllowed
- _OBJC_IVAR_$_RMModelAppManagedDeclaration_RemoveBehavior._payloadRemovable
- _OBJC_METACLASS_$_RMModelAppManagedDeclaration_RemoveBehavior
- _RMModelAppManagedDeclaration_InstallBehavior_Install_immediately
- _RMModelAppManagedDeclaration_InstallBehavior_Install_onDemand
- _RMModelStatusAppManagedList_State_managementRejected
- _RMModelStatusAppManagedList_State_needsRedemption
- _RMModelStatusAppManagedList_State_prompting
- _RMModelStatusAppManagedList_State_promptingForUpdate
- _RMModelStatusAppManagedList_State_promptingForUpdateLogin
- _RMModelStatusAppManagedList_State_redeeming
- _RMModelStatusAppManagedList_State_unknown
- _RMModelStatusAppManagedList_State_updateRejected
- _RMModelStatusAppManagedList_State_updating
- _RMModelStatusAppManagedList_State_userInstalledApp
- _RMModelStatusAppManagedList_State_userRejected
- _RMModelStatusAppManagedList_State_validatingPurchase
- _RMModelStatusAppManagedList_State_validatingUpdate
- __OBJC_$_CLASS_METHODS_RMModelAppManagedDeclaration_RemoveBehavior
- __OBJC_$_CLASS_PROP_LIST_RMModelAppManagedDeclaration_RemoveBehavior
- __OBJC_$_INSTANCE_METHODS_RMModelAppManagedDeclaration_RemoveBehavior
- __OBJC_$_INSTANCE_VARIABLES_RMModelAppManagedDeclaration_RemoveBehavior
- __OBJC_$_PROP_LIST_RMModelAppManagedDeclaration_RemoveBehavior
- __OBJC_CLASS_RO_$_RMModelAppManagedDeclaration_RemoveBehavior
- __OBJC_METACLASS_RO_$_RMModelAppManagedDeclaration_RemoveBehavior
- ___57-[RMModelAppManagedDeclaration serializePayloadWithType:]_block_invoke_3
- ___block_literal_global.289
- __unnamed_array_storage.100
- __unnamed_array_storage.108
- __unnamed_array_storage.94
- __unnamed_array_storage.97
- _objc_msgSend$payloadAccountPromptAllowed
- _objc_msgSend$payloadRemovable
- _objc_msgSend$payloadRemoveBehavior
- _objc_msgSend$setPayloadAccountPromptAllowed:
- _objc_msgSend$setPayloadRemovable:
- _objc_msgSend$setPayloadRemoveBehavior:
CStrings:
+ "@\"RMModelAppManagedDeclaration_InstallBehaviorLicense\""
+ "Device"
+ "License"
+ "Optional"
+ "RMModelAppManagedDeclaration_InstallBehaviorLicense"
+ "Required"
+ "T@\"NSNumber\",C,N,V_statusExternalVersionId"
+ "T@\"NSString\",C,N,V_payloadVPPType"
+ "T@\"NSString\",C,N,V_statusUpdateState"
+ "T@\"RMModelAppManagedDeclaration_InstallBehaviorLicense\",C,N,V_payloadLicense"
+ "User"
+ "VPPType"
+ "_payloadLicense"
+ "_payloadVPPType"
+ "_statusUpdateState"
+ "available"
+ "buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:includeInBackup:attributes:"
+ "buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:updateState:reasons:"
+ "buildWithInstall:license:"
+ "buildWithVPPType:"
+ "payloadLicense"
+ "payloadVPPType"
+ "prompting-for-consent"
+ "setPayloadLicense:"
+ "setPayloadVPPType:"
+ "setStatusUpdateState:"
+ "statusUpdateState"
+ "update-state"
- "@\"RMModelAppManagedDeclaration_RemoveBehavior\""
- "AccountPromptAllowed"
- "Immediately"
- "OnDemand"
- "RMModelAppManagedDeclaration_RemoveBehavior"
- "Removable"
- "RemoveBehavior"
- "T@\"NSNumber\",C,N,V_payloadAccountPromptAllowed"
- "T@\"NSNumber\",C,N,V_payloadRemovable"
- "T@\"RMModelAppManagedDeclaration_RemoveBehavior\",C,N,V_payloadRemoveBehavior"
- "_payloadAccountPromptAllowed"
- "_payloadRemovable"
- "_payloadRemoveBehavior"
- "buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:removeBehavior:includeInBackup:attributes:"
- "buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:"
- "buildWithInstall:accountPromptAllowed:"
- "buildWithRemovable:"
- "payloadAccountPromptAllowed"
- "payloadRemovable"
- "payloadRemoveBehavior"
- "setPayloadAccountPromptAllowed:"
- "setPayloadRemovable:"
- "setPayloadRemoveBehavior:"

```
