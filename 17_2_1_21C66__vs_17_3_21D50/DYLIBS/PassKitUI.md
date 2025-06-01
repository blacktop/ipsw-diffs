## PassKitUI

> `/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI`

```diff

-1552.3.6.4.0
-  __TEXT.__text: 0xbe6110
+1552.4.5.0.0
+  __TEXT.__text: 0xbe67e0
   __TEXT.__auth_stubs: 0xa2a0
-  __TEXT.__objc_methlist: 0x4a870
+  __TEXT.__objc_methlist: 0x4a878
   __TEXT.__const: 0x35940
-  __TEXT.__cstring: 0x5e20f
+  __TEXT.__cstring: 0x5e3e4
   __TEXT.__constg_swiftt: 0xdcec
   __TEXT.__swift5_typeref: 0x59a82
   __TEXT.__swift5_builtin: 0x730

   __TEXT.__swift5_capture: 0x68f8
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x70
-  __TEXT.__gcc_except_tab: 0xf0d8
-  __TEXT.__oslogstring: 0x190a0
-  __TEXT.__ustring: 0xd28
-  __TEXT.__unwind_info: 0x2663c
+  __TEXT.__gcc_except_tab: 0xf0ec
+  __TEXT.__oslogstring: 0x190e7
+  __TEXT.__ustring: 0xcae
+  __TEXT.__unwind_info: 0x26658
   __TEXT.__eh_frame: 0x53f4
   __TEXT.__objc_classname: 0x10583
-  __TEXT.__objc_methname: 0xb4bb0
+  __TEXT.__objc_methname: 0xb4b9c
   __TEXT.__objc_methtype: 0x1ff40
-  __TEXT.__objc_stubs: 0x76ba0
+  __TEXT.__objc_stubs: 0x76b80
   __DATA_CONST.__got: 0x4240
-  __DATA_CONST.__const: 0x170f8
+  __DATA_CONST.__const: 0x17128
   __DATA_CONST.__objc_classlist: 0x2dd8
   __DATA_CONST.__objc_catlist: 0x388
   __DATA_CONST.__objc_protolist: 0x13e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa0ee8
-  __DATA_CONST.__objc_selrefs: 0x23388
+  __DATA_CONST.__objc_selrefs: 0x23380
   __DATA_CONST.__objc_arraydata: 0x540
   __AUTH_CONST.__const: 0x35ea0
   __AUTH_CONST.__objc_const: 0x1c9c8
-  __AUTH_CONST.__cfstring: 0x32740
+  __AUTH_CONST.__cfstring: 0x32840
   __AUTH_CONST.__objc_doubleobj: 0x1c0
-  __AUTH_CONST.__objc_intobj: 0x1398
+  __AUTH_CONST.__objc_intobj: 0x13e0
   __AUTH_CONST.__objc_arrayobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__auth_got: 0x5160

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3586BC21-DB59-3666-B96C-401773D5C37F
-  Functions: 55924
-  Symbols:   108601
-  CStrings:  48914
+  UUID: 06F2E023-9C42-35BF-8D12-BC4031C38501
+  Functions: 55928
+  Symbols:   108609
+  CStrings:  48931
 
Symbols:
+ -[PKPaymentTransactionDetailViewController _businessChatContextForUnavailableDisputeStatus]
+ -[PKTransactionSupportTopicsViewController _openBusinessChatWithContext:]
+ ___66-[PKPasscodeUpgradeFlowController _showPasscodeUpgradeExplanation]_block_invoke.27
+ ___66-[PKPasscodeUpgradeFlowController _showPasscodeUpgradeExplanation]_block_invoke.41
+ ___66-[PKPasscodeUpgradeFlowController _showPasscodeUpgradeExplanation]_block_invoke.49
+ ___67-[PKBusinessChatController openBusinessChatWithContext:completion:]_block_invoke.615
+ ___73-[PKTransactionSupportTopicsViewController _openBusinessChatWithContext:]_block_invoke
+ ___73-[PKTransactionSupportTopicsViewController _openBusinessChatWithContext:]_block_invoke_2
+ ___74-[PKPaymentTransactionDetailViewController _loadAppPrivacyURLFromAppStore]_block_invoke.1106
+ ___76-[PKPaymentTransactionDetailViewController _cancelPeerPaymentPendingRequest]_block_invoke.746
+ ___block_descriptor_56_e8_32s40bs48w_e34_v24?0"NSDictionary"8"NSError"16ls32l8w48l8s40l8
+ ___block_literal_global.1577
+ ___block_literal_global.679
+ ___block_literal_global.684
+ ___block_literal_global.686
+ ___block_literal_global.745
+ _objc_msgSend$_businessChatContextForUnavailableDisputeStatus
- -[PKPaymentTransactionDetailViewController _businessChatContextForOtherIssue]
- ___67-[PKBusinessChatController openBusinessChatWithContext:completion:]_block_invoke.585
- ___70-[PKTransactionSupportTopicsViewController _openBusinessChatForTopic:]_block_invoke
- ___70-[PKTransactionSupportTopicsViewController _openBusinessChatForTopic:]_block_invoke_2
- ___74-[PKPaymentTransactionDetailViewController _loadAppPrivacyURLFromAppStore]_block_invoke.1107
- ___76-[PKPaymentTransactionDetailViewController _cancelPeerPaymentPendingRequest]_block_invoke.747
- ___block_descriptor_48_e8_32s40w_e62_v24?0"PKAccountWebServiceSupportTopicsResponse"8"NSError"16lw40l8s32l8
- ___block_literal_global.1578
- ___block_literal_global.649
- ___block_literal_global.654
- ___block_literal_global.656
- ___block_literal_global.715
- _objc_msgSend$_businessChatContextForOtherIssue
- _objc_msgSend$initWithNonCancellableBillPayment
CStrings:
+ "I need help with this Daily Cash Adjustment"
+ "I need help with this Monthly Installment"
+ "I need help with this balance adjustment"
+ "I need help with this payment"
+ "I need help with this transaction"
+ "PKPasscodeUpgradeFlowController requested local auth and returning %@."
+ "TRANSACTION_DETAILS_DISPUTE_TRANSACTION_APPLE_CARD_BALANCE_ADJUSTMENT"
+ "TRANSACTION_DETAILS_DISPUTE_TRANSACTION_APPLE_CARD_INSTALLMENT"
+ "TRANSACTION_DETAILS_DISPUTE_TRANSACTION_APPLE_CARD_REWARDS_ADJUSTMENT"
+ "TRANSACTION_DETAILS_DISPUTE_TRANSACTION_UNAVAILABLE_DISPUTE_STATUS"
+ "_businessChatContextForUnavailableDisputeStatus"
+ "wallet::transaction::generalcontact"
+ "wallet_transaction_generalcontact"
- "_businessChatContextForOtherIssue"
- "initWithNonCancellableBillPayment"
- "wallet::transaction::otherissue"
- "wallet_transaction_otherissue"

```
