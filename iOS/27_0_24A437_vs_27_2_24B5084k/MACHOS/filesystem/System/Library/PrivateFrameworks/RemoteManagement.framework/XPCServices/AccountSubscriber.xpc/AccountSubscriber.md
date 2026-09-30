## AccountSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/AccountSubscriber`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-624.2.3.0.0
-  __TEXT.__text: 0x13630
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x2100
-  __TEXT.__objc_methlist: 0x86c
+624.40.12.0.0
+  __TEXT.__text: 0x14184
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_stubs: 0x2280
+  __TEXT.__objc_methlist: 0x88c
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__cstring: 0x10e9
+  __TEXT.__gcc_except_tab: 0x290
+  __TEXT.__cstring: 0x11e9
   __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methname: 0x1e36
+  __TEXT.__objc_methname: 0x1f31
   __TEXT.__objc_methtype: 0x2f1
-  __TEXT.__oslogstring: 0xfd0
-  __TEXT.__unwind_info: 0x4f8
-  __DATA_CONST.__const: 0x8d8
-  __DATA_CONST.__cfstring: 0xd20
+  __TEXT.__oslogstring: 0x10a8
+  __TEXT.__unwind_info: 0x518
+  __DATA_CONST.__const: 0x940
+  __DATA_CONST.__cfstring: 0xdc0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0x440
   __DATA.__objc_const: 0xfd0
-  __DATA.__objc_selrefs: 0x978
+  __DATA.__objc_selrefs: 0x9d0
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 299
-  Symbols:   300
-  CStrings:  555
+  Functions: 310
+  Symbols:   318
+  CStrings:  574
 
Symbols:
+ _AccountPropertyCommunicationServiceRules
+ _AccountPropertyMailAllowAppSheet
+ _AccountPropertyMailAllowMailRecentsSyncing
+ _AccountPropertyMailAllowMove
+ _AccountPropertyMailEnableMailDrop
+ _AccountPropertyRemoteManagementProfileTransferDate
+ _AccountPropertyRemoteManagementTransferredFromProfileIdentifier
+ _MCRemoteManagementTransferProfileAccount
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_RMFeatureFlags
+ _RMModelAccountMailDeclaration_IncomingServer_AuthenticationMethod_CRAMMD5
+ _RMModelAccountMailDeclaration_IncomingServer_AuthenticationMethod_HTTPMD5
+ _RMModelAccountMailDeclaration_IncomingServer_AuthenticationMethod_NTLM
+ _RMModelStatusAccountListExchange_ProtocolType_EAS
+ _RemoteManagementManagingOwnerIdentifier
+ _kDAAccountEmailAddress
+ _kMCAccountProfileUUIDKey
+ _kMCCommunicationServiceRulesAccountProperty
CStrings:
+ "Account cannot be saved: %{public}@ %{public}@"
+ "AudioCall"
+ "DefaultServiceHandlers"
+ "Failed to record failure for %{public}@: %{public}@"
+ "No existing DDM-managed account for key %{public}@, checking for profile transfer candidate"
+ "No supported protocol in EnabledProtocolTypes: %{public}@"
+ "Only EAS is supported on this device"
+ "RemoteManagementProfileTransferDate"
+ "RemoteManagementTransferredFromProfileIdentifier"
+ "Skipping configuration %{public}@ after failed profile transfer: %{public}@"
+ "_remotemanagement_communicationServiceRules"
+ "_remotemanagement_mailAllowAppSheet"
+ "_remotemanagement_mailAllowMailRecentsSyncing"
+ "_remotemanagement_mailAllowMove"
+ "_remotemanagement_mailEnableMailDrop"
+ "_transferProfileManagedAccountWithIdentifier:error:"
+ "canSaveAccount:withCompletionHandler:"
+ "copy"
+ "date"
+ "denialErrorForSavingAccount:accountStore:"
+ "isAccountTakeoverEnabled"
+ "payloadAudioCall"
+ "payloadDefaultServiceHandlers"
+ "removeSearchSettings:"
+ "searchSettings"
+ "setStatusProtocolType:"
- "EmailAuthCRAMMD5"
- "EmailAuthHTTPMD5"
- "EmailAuthNTLM"
- "Only EAS is supported on iOS"
- "Profile account transfer to DDM"
- "createNotImplementedErrorForFeature:"
- "transferProfileAccount: not implemented on this platform for account %{public}@"
```
