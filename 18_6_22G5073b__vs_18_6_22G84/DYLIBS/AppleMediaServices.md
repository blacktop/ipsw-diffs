## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-8.6.7.0.0
-  __TEXT.__text: 0x694b8c
+8.6.8.0.0
+  __TEXT.__text: 0x695164
   __TEXT.__auth_stubs: 0x40c0
-  __TEXT.__objc_methlist: 0x20b44
+  __TEXT.__objc_methlist: 0x20b9c
   __TEXT.__const: 0x540e0
   __TEXT.__dlopen_cstrs: 0x8d3
-  __TEXT.__cstring: 0x25186
+  __TEXT.__cstring: 0x25366
   __TEXT.__swift5_typeref: 0x3eb1
   __TEXT.__swift5_reflstr: 0x1f18
   __TEXT.__swift5_assocty: 0x9d8

   __TEXT.__swift5_capture: 0x1e10
   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__swift5_protos: 0x80
-  __TEXT.__oslogstring: 0x2e72b
-  __TEXT.__gcc_except_tab: 0x7b34
+  __TEXT.__oslogstring: 0x2e7b7
+  __TEXT.__gcc_except_tab: 0x7b2c
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0xd468
+  __TEXT.__unwind_info: 0xd490
   __TEXT.__eh_frame: 0xd314
   __TEXT.__objc_classname: 0x3bf6
-  __TEXT.__objc_methname: 0x410a3
+  __TEXT.__objc_methname: 0x4119d
   __TEXT.__objc_methtype: 0x7374
-  __TEXT.__objc_stubs: 0x2d1a0
+  __TEXT.__objc_stubs: 0x2d280
   __DATA_CONST.__got: 0x17d0
   __DATA_CONST.__const: 0xba78
   __DATA_CONST.__objc_classlist: 0x12c0
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe6c8
+  __DATA_CONST.__objc_selrefs: 0xe700
   __DATA_CONST.__objc_protorefs: 0x1b8
   __DATA_CONST.__objc_superrefs: 0xc58
-  __DATA_CONST.__objc_arraydata: 0x4f8
+  __DATA_CONST.__objc_arraydata: 0x568
   __AUTH_CONST.__auth_got: 0x2078
-  __AUTH_CONST.__const: 0x24e10
-  __AUTH_CONST.__cfstring: 0x211c0
+  __AUTH_CONST.__const: 0x24e30
+  __AUTH_CONST.__cfstring: 0x213a0
   __AUTH_CONST.__objc_const: 0x38400
   __AUTH_CONST.__objc_intobj: 0xcd8
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0x7f40
   __AUTH.__data: 0x12b0

   __DATA_DIRTY.__objc_ivar: 0x65c
   __DATA_DIRTY.__objc_data: 0x5478
   __DATA_DIRTY.__data: 0x1ae0
-  __DATA_DIRTY.__bss: 0x3320
+  __DATA_DIRTY.__bss: 0x3330
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8B9FF647-A559-3621-8716-E1E1FE896ADE
-  Functions: 19890
-  Symbols:   46165
-  CStrings:  23990
+  UUID: 8BDBA751-8134-3D06-A45E-D299BC3BB355
+  Functions: 19899
+  Symbols:   46191
+  CStrings:  24029
 
Symbols:
+ +[AMSMetrics _defaultAccountClearingTopics]
+ -[AMSMetrics _cachedAccountClearingTopicsFromBag]
+ -[AMSMetrics _clearAccountForEventIfNeeded:]
+ -[AMSMetrics _topicsRequiringAccountClearing]
+ -[AMSMetrics enqueueEventWithoutAccountClearing:]
+ -[AMSMetrics enqueueEventsWithoutAccountClearing:]
+ -[AMSMetrics promiseForEnqueueingEvents:skipAccountClearing:]
+ GCC_except_table77
+ GCC_except_table78
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke.132
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke.137
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke_2.133
+ ___43+[AMSMetrics _defaultAccountClearingTopics]_block_invoke
+ ___44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.144
+ ___49-[AMSMetrics _cachedAccountClearingTopicsFromBag]_block_invoke
+ ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.140
+ ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.142
+ ___block_literal_global.106
+ ___block_literal_global.113
+ ___block_literal_global.122
+ ___block_literal_global.125
+ _objc_msgSend$_clearAccountForEventIfNeeded:
+ _objc_msgSend$_defaultAccountClearingTopics
+ _objc_msgSend$_topicsRequiringAccountClearing
+ _objc_msgSend$cachedValuesForKeys:observationToken:updateHandler:
+ _objc_msgSend$enqueueEventsWithoutAccountClearing:
+ _objc_msgSend$promiseForEnqueueingEvents:skipAccountClearing:
+ _objc_msgSend$removeObserverWithToken:
- GCC_except_table68
- GCC_except_table69
- ___36-[AMSMetrics _processOperationQueue]_block_invoke.82
- ___36-[AMSMetrics _processOperationQueue]_block_invoke.87
- ___36-[AMSMetrics _processOperationQueue]_block_invoke_2.83
- ___44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.94
- ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.90
- ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.92
CStrings:
+ "%{public}@: Bag values updated for account clearing topics to %@"
+ "%{public}@: [%{public}@] Clearing account for event with topic: %{public}@"
+ "<private>"
+ "_cachedAccountClearingTopicsFromBag"
+ "_clearAccountForEventIfNeeded:"
+ "_defaultAccountClearingTopics"
+ "_topicsRequiringAccountClearing"
+ "accountClearingTopics"
+ "enqueueEventWithoutAccountClearing:"
+ "enqueueEventsWithoutAccountClearing:"
+ "promiseForEnqueueingEvents:skipAccountClearing:"
+ "xp_ase_appstore/arcade_substate"
+ "xp_ase_appstore/billing_refunds"
+ "xp_ase_appstore/preorders"
+ "xp_ase_appstore/subscription_movement"
+ "xp_ase_messaging/appstore_experimentation"
+ "xp_ase_messaging/appstore_notifications"
+ "xp_ase_payments/appstore_payments_ue"
+ "xp_ase_payments/appstore_redeem_ue"
+ "xp_ase_payments/transient"
+ "xp_ase_personalization/appstore"
+ "xp_ase_subscriptions/commerce"
+ "xp_ase_subscriptions/movement"
+ "xp_ase_subscriptions/ue"
+ "xp_ase_transient/appstore_ue"
- "seed"

```
