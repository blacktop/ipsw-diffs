## AccountSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/AccountSubscriber`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-624.0.8.0.0
-  __TEXT.__text: 0x12350
+624.0.10.0.0
+  __TEXT.__text: 0x12784
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x1e20
+  __TEXT.__objc_stubs: 0x1f80
   __TEXT.__objc_methlist: 0x81c
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__cstring: 0xf3b
+  __TEXT.__cstring: 0x104b
   __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methname: 0x1b7b
+  __TEXT.__objc_methname: 0x1c97
   __TEXT.__objc_methtype: 0x2be
-  __TEXT.__oslogstring: 0xaa2
+  __TEXT.__oslogstring: 0xb0d
   __TEXT.__unwind_info: 0x3c8
-  __DATA_CONST.__const: 0x8a8
-  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__const: 0x8d8
+  __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__got: 0x3f8
   __DATA.__objc_const: 0xfd0
-  __DATA.__objc_selrefs: 0x8b8
+  __DATA.__objc_selrefs: 0x910
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 279
-  Symbols:   288
-  CStrings:  500
+  Functions: 280
+  Symbols:   300
+  CStrings:  519
 
Symbols:
+ _AccountPropertyExchangeAllowAppSheet
+ _AccountPropertyExchangeAllowMailRecentsSyncing
+ _AccountPropertyExchangeAllowMove
+ _AccountPropertyExchangeCommunicationServiceRules
+ _AccountPropertyExchangeEnableMailDrop
+ _AccountPropertyExchangeMailNumberOfPastDaysToSync
+ _MFMailAccountRestrictMessageTransfersToOtherAccounts
+ _MFMailAccountRestrictRecentsSyncing
+ _MFMailAccountRestrictSendingFromExternalProcesses
+ _MFMailAccountSupportsMailDrop
+ _OBJC_CLASS_$_MCCommunicationServiceRulesUtilities
+ _OBJC_CLASS_$_NSNull
CStrings:
+ "Invalid CommunicationServiceRules; not applying: %{public}@"
+ "VPNUUID specified (%{public}@) but not applied"
+ "_remotemanagement_exchangeAllowAppSheet"
+ "_remotemanagement_exchangeAllowMailRecentsSyncing"
+ "_remotemanagement_exchangeAllowMove"
+ "_remotemanagement_exchangeCommunicationServiceRules"
+ "_remotemanagement_exchangeEnableMailDrop"
+ "_remotemanagement_exchangeMailNumberOfPastDaysToSync"
+ "null"
+ "payloadAllowAppSheet"
+ "payloadAllowMailRecentsSyncing"
+ "payloadAllowMove"
+ "payloadCommunicationServiceRules"
+ "payloadEnableMailDrop"
+ "payloadMailNumberOfPastDaysToSync"
+ "payloadVPNUUID"
+ "setCommunicationServiceRules:"
+ "setMailNumberOfPastDaysToSync:"
+ "validatedCommunicationServiceRules:outError:"
```
