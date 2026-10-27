## AccountSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/Contents/MacOS/AccountSubscriber`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-624.1.3.0.0
-  __TEXT.__text: 0x12870
+624.40.16.0.0
+  __TEXT.__text: 0x12e18
   __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x1bc0
-  __TEXT.__objc_methlist: 0x81c
+  __TEXT.__objc_stubs: 0x1d60
+  __TEXT.__objc_methlist: 0x844
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x23c
-  __TEXT.__cstring: 0x10e1
+  __TEXT.__gcc_except_tab: 0x250
+  __TEXT.__cstring: 0x10fc
   __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methname: 0x1a31
+  __TEXT.__objc_methname: 0x1b3d
   __TEXT.__objc_methtype: 0x2f1
-  __TEXT.__oslogstring: 0x112b
-  __TEXT.__unwind_info: 0x530
-  __DATA_CONST.__const: 0xa10
-  __DATA_CONST.__cfstring: 0xd60
+  __TEXT.__oslogstring: 0x114e
+  __TEXT.__unwind_info: 0x540
+  __DATA_CONST.__const: 0x9c0
+  __DATA_CONST.__cfstring: 0xd40
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__got: 0x3a0
   __DATA.__objc_const: 0xfd0
-  __DATA.__objc_selrefs: 0x820
+  __DATA.__objc_selrefs: 0x880
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/Versions/A/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 323
-  Symbols:   251
-  CStrings:  520
+  Functions: 325
+  Symbols:   260
+  CStrings:  531
 
Symbols:
+ _AccountPropertyMailEnableMailDrop
+ _AccountPropertyRemoteManagementExchangeProtocolType
+ _OBJC_CLASS_$_NSNull
+ _RMModelAccountMailDeclaration_IncomingServer_AuthenticationMethod_CRAMMD5
+ _RMModelAccountMailDeclaration_IncomingServer_AuthenticationMethod_HTTPMD5
+ _RMModelAccountMailDeclaration_IncomingServer_AuthenticationMethod_NTLM
+ _RMModelStatusAccountListExchange_ProtocolType_EAS
+ _RMModelStatusAccountListExchange_ProtocolType_EWS
+ _RMModelStatusAccountListExchange_ProtocolType_graph
CStrings:
+ "Account cannot be saved: %{public}@ %{public}@"
+ "Configuration change to calendar URL or username requires account to be recreated"
+ "Only EWS or Graph are supported on this device"
+ "RemoteManagementExchangeProtocolType"
+ "_remotemanagement_mailEnableMailDrop"
+ "_transferProfileManagedAccountWithIdentifier:error:"
+ "canSaveAccount:withCompletionHandler:"
+ "componentsWithString:"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "denialErrorForSavingAccount:accountStore:"
+ "isValue:equalToValue:"
+ "null"
+ "path"
+ "port"
+ "query"
+ "setStatusProtocolType:"
+ "user"
- "Either EWS or Graph must be enabled for macOS"
- "EmailAuthCRAMMD5"
- "EmailAuthHTTPMD5"
- "EmailAuthNTLM"
- "Error saving incoming mail account: %{public}@"
- "Error saving outgoing mail account: %{public}@"
```
