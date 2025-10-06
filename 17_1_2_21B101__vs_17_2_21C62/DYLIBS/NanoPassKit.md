## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1160.0.0.0.0
-  __TEXT.__text: 0x2119e4
-  __TEXT.__auth_stubs: 0x17f0
-  __TEXT.__objc_methlist: 0x20404
+1161.3.0.0.0
+  __TEXT.__text: 0x21185c
+  __TEXT.__auth_stubs: 0x17e0
+  __TEXT.__objc_methlist: 0x2040c
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x1665c
-  __TEXT.__oslogstring: 0x28570
+  __TEXT.__cstring: 0x165e9
+  __TEXT.__oslogstring: 0x284e2
   __TEXT.__gcc_except_tab: 0x3c80
   __TEXT.__dlopen_cstrs: 0x2eb
   __TEXT.__ustring: 0x160
-  __TEXT.__unwind_info: 0x7eac
-  __TEXT.__objc_classname: 0x646d
-  __TEXT.__objc_methname: 0x3b834
-  __TEXT.__objc_methtype: 0x95e6
-  __TEXT.__objc_stubs: 0x20120
-  __DATA_CONST.__got: 0x7c8
-  __DATA_CONST.__const: 0x63f0
-  __DATA_CONST.__objc_classlist: 0x10a0
+  __TEXT.__unwind_info: 0x7ea8
+  __TEXT.__objc_classname: 0x6450
+  __TEXT.__objc_methname: 0x3b804
+  __TEXT.__objc_methtype: 0x96d6
+  __TEXT.__objc_stubs: 0x20060
+  __DATA_CONST.__got: 0x7b0
+  __DATA_CONST.__const: 0x6418
+  __DATA_CONST.__objc_classlist: 0x1098
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x39330
-  __DATA_CONST.__objc_selrefs: 0xb5c8
+  __DATA_CONST.__objc_const: 0x39488
+  __DATA_CONST.__objc_selrefs: 0xb5a8
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__cfstring: 0xe1e0
-  __AUTH_CONST.__objc_const: 0xc320
+  __AUTH_CONST.__cfstring: 0xe160
+  __AUTH_CONST.__objc_const: 0xc2d8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__const: 0xcc0
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0xc08
-  __AUTH.__objc_data: 0xa5f0
+  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH.__objc_data: 0xa5a0
   __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0x1460
-  __DATA.__objc_superrefs: 0xfe0
-  __DATA.__objc_ivar: 0x1a70
+  __DATA.__objc_classrefs: 0x1438
+  __DATA.__objc_superrefs: 0xfd8
+  __DATA.__objc_ivar: 0x1a6c
   __DATA.__data: 0x1bd0
   __DATA.__bss: 0x360
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
-  - /System/Library/PrivateFrameworks/ChatKit.framework/ChatKit
   - /System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
-  - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 6402E488-9DC5-3E1F-BAA2-4619ECE20E29
-  Functions: 13012
-  Symbols:   39019
-  CStrings:  16092
+  UUID: 2B808CF3-2ADD-37E2-9B56-1903DB1DBE87
+  Functions: 13014
+  Symbols:   39003
+  CStrings:  16080
 
Symbols:
+ -[NPKCommutePlanField availableFrom]
+ -[NPKCommutePlanField availableUntil]
+ -[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]
+ -[NPKExpressPassesManager states]
+ -[NPKPassesManager group:didInsertPass:withState:atIndex:]
+ -[NPKPassesManager group:didUpdatePass:withState:atIndex:]
+ -[NPKPassesManager group:didUpdatePassState:forPass:atIndex:]
+ -[NPKPassesManager states]
+ -[NPKValueAddedServiceAutomaticSelectionCoordinator passesDataSource:didUpdatePasses:withStates:]
+ -[PKPaymentPass(NanoPassKit) npkHasTransitNetworkIdentifiers]
+ GCC_except_table35
+ __OBJC_$_PROP_LIST_NPKCommutePlanField.197
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PKGroupDelegate
+ ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.528
+ ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.535
+ ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.355
+ ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.373
+ ___49-[NPKPassesManager _handleObjectSettingsChanged:]_block_invoke.75
+ ___58-[NPKPassesManager group:didInsertPass:withState:atIndex:]_block_invoke
+ ___58-[NPKPassesManager group:didUpdatePass:withState:atIndex:]_block_invoke
+ ___61-[NPKPassesManager group:didUpdatePassState:forPass:atIndex:]_block_invoke
+ ___63-[NPKPassesManager _loadContentAndImageSetsForPass:completion:]_block_invoke.70
+ ___63-[NPKPassesManager _loadContentAndImageSetsForPass:completion:]_block_invoke.74
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.510
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.512
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.513
+ ___block_descriptor_56_e8_32s40s48s_e39_v16?0"<NPKPassesDataSourceObserver>"8ls32l8s40l8s48l8
+ ___block_literal_global.509
+ _objc_msgSend$availableFrom
+ _objc_msgSend$availableFromRelative
+ _objc_msgSend$availableUntil
+ _objc_msgSend$availableUntilRelative
+ _objc_msgSend$isPlanDisplayable
+ _objc_msgSend$passesDataSource:didUpdatePasses:withStates:
+ _objc_msgSend$passesDataSource:didUpdateStates:forPasses:
+ _objc_msgSend$supportedTransitNetworkIdentifiers
- -[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:]
- -[NPKMessageCompositionManager .cxx_destruct]
- -[NPKMessageCompositionManager _sendComposition:toRecipient:completion:]
- -[NPKMessageCompositionManager dealloc]
- -[NPKMessageCompositionManager init]
- -[NPKMessageCompositionManager sendMessage:withAppExtensionIdentifier:toRecipient:completion:]
- -[NPKPassesManager group:didInsertPass:atIndex:]
- -[NPKPassesManager group:didUpdatePass:atIndex:]
- -[NPKValueAddedServiceAutomaticSelectionCoordinator passesDataSource:didUpdatePasses:]
- _CKMakeHandlesFromRecipients
- _OBJC_CLASS_$_CKComposition
- _OBJC_CLASS_$_CKConversation
- _OBJC_CLASS_$_IMChatRegistry
- _OBJC_CLASS_$_IMDaemonController
- _OBJC_CLASS_$_IMService
- _OBJC_CLASS_$_NPKMessageCompositionManager
- _OBJC_IVAR_$_NPKMessageCompositionManager._listenerID
- _OBJC_METACLASS_$_NPKMessageCompositionManager
- __OBJC_$_INSTANCE_METHODS_NPKMessageCompositionManager
- __OBJC_$_INSTANCE_VARIABLES_NPKMessageCompositionManager
- __OBJC_$_PROP_LIST_NPKCommutePlanField.190
- __OBJC_CLASS_RO_$_NPKMessageCompositionManager
- __OBJC_METACLASS_RO_$_NPKMessageCompositionManager
- ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.522
- ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.529
- ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.349
- ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.367
- ___48-[NPKPassesManager group:didInsertPass:atIndex:]_block_invoke
- ___48-[NPKPassesManager group:didUpdatePass:atIndex:]_block_invoke
- ___49-[NPKPassesManager _handleObjectSettingsChanged:]_block_invoke.72
- ___63-[NPKPassesManager _loadContentAndImageSetsForPass:completion:]_block_invoke.67
- ___63-[NPKPassesManager _loadContentAndImageSetsForPass:completion:]_block_invoke.68
- ___72-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:]_block_invoke
- ___72-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:]_block_invoke.504
- ___72-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:]_block_invoke.506
- ___72-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:]_block_invoke.507
- ___block_literal_global.498
- ___block_literal_global.503
- _kFZListenerCapChats
- _kFZListenerCapFileTransfers
- _kFZListenerCapMessageHistory
- _objc_msgSend$_sendComposition:toRecipient:completion:
- _objc_msgSend$addListenerID:capabilities:
- _objc_msgSend$chatWithHandle:
- _objc_msgSend$compositionWithMSMessage:appExtensionIdentifier:
- _objc_msgSend$hasListenerForID:
- _objc_msgSend$initWithChat:
- _objc_msgSend$join
- _objc_msgSend$messagesFromComposition:
- _objc_msgSend$passesDataSource:didUpdatePasses:
- _objc_msgSend$refreshServiceForSending
- _objc_msgSend$removeListenerID:
- _objc_msgSend$sendMessage:onService:newComposition:
- _objc_msgSend$serviceWithName:
- _objc_msgSend$sharedRegistry
CStrings:
+ "Notice: Group %@ inserted pass %@ (%@) with state (%@) at index %lu"
+ "Notice: Group %@ updated pass %@ (%@) with state (%@) at index %lu"
+ "Notice: Group %@ updated state (%@) for pass %@ (%@) at index %lu"
+ "availableFrom"
+ "availableFromRelative"
+ "availableUntil"
+ "availableUntilRelative"
+ "group:didInsertPass:withState:atIndex:"
+ "group:didUpdatePass:withState:atIndex:"
+ "group:didUpdatePassState:forPass:atIndex:"
+ "isPlanDisplayable"
+ "npkHasTransitNetworkIdentifiers"
+ "passesDataSource:didUpdatePasses:withStates:"
+ "passesDataSource:didUpdateStates:forPasses:"
+ "states"
+ "supportedTransitNetworkIdentifiers"
+ "v40@0:8@\"<NPKPassesDataSource>\"16@\"NSArray\"24@\"NSDictionary\"32"
+ "v40@0:8@\"<NPKPassesDataSource>\"16@\"NSDictionary\"24@\"NSArray\"32"
+ "v48@0:8@\"PKGroup\"16@\"PKPass\"24@\"PKPassDynamicState\"32Q40"
+ "v48@0:8@\"PKGroup\"16@\"PKPassDynamicState\"24@\"PKPass\"32Q40"
- "%@:%ld:NPKMessageCompositionManager:%@"
- "Error: Could not create IMMessages with composition: %@ conversation %@"
- "Error: Could not resolve IMHandle for recipient %@"
- "NPKMessageCompositionManager"
- "Notice: Group %@ inserted pass %@ (%@) at index %lu"
- "Notice: Group %@ updated pass %@ (%@) at index %lu"
- "Notice: Resolved recipient IMHandle: %@"
- "Notice: Sending IMMessage: %@"
- "Notice: Sending composition %@ to recipient %@"
- "Unable to compose message"
- "Unable to resolve IMHandle for recipient"
- "_listenerID"
- "_sendComposition:toRecipient:completion:"
- "addListenerID:capabilities:"
- "chatWithHandle:"
- "compositionWithMSMessage:appExtensionIdentifier:"
- "hasListenerForID:"
- "iMessage"
- "initWithChat:"
- "join"
- "messagesFromComposition:"
- "passesDataSource:didUpdatePasses:"
- "refreshServiceForSending"
- "removeListenerID:"
- "sendMessage:onService:newComposition:"
- "sendMessage:withAppExtensionIdentifier:toRecipient:completion:"
- "serviceWithName:"
- "sharedRegistry"

```
