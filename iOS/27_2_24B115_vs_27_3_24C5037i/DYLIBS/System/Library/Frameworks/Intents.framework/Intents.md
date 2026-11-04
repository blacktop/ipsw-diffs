## Intents

> `/System/Library/Frameworks/Intents.framework/Intents`

```diff

-4016.1.16.0.0
-  __TEXT.__text: 0x4452f8
-  __TEXT.__objc_methlist: 0x78cb4
+4016.2.7.0.0
+  __TEXT.__text: 0x447548
+  __TEXT.__objc_methlist: 0x78e94
   __TEXT.__const: 0x1d80
   __TEXT.__dlopen_cstrs: 0xce9
-  __TEXT.__gcc_except_tab: 0x21c4
-  __TEXT.__cstring: 0x47cf6
-  __TEXT.__oslogstring: 0x657d
+  __TEXT.__gcc_except_tab: 0x221c
+  __TEXT.__cstring: 0x480db
+  __TEXT.__oslogstring: 0x6975
   __TEXT.__ustring: 0x512
-  __TEXT.__unwind_info: 0x14c70
+  __TEXT.__unwind_info: 0x14d20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb870
-  __DATA_CONST.__objc_classlist: 0x2930
+  __DATA_CONST.__const: 0xb920
+  __DATA_CONST.__objc_classlist: 0x2948
   __DATA_CONST.__objc_catlist: 0x100
-  __DATA_CONST.__objc_protolist: 0x1938
+  __DATA_CONST.__objc_protolist: 0x1948
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x154f8
-  __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x1398
+  __DATA_CONST.__objc_selrefs: 0x15608
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x13a8
   __DATA_CONST.__objc_arraydata: 0xc820
-  __DATA_CONST.__got: 0x28d8
-  __AUTH_CONST.__const: 0x17e0
-  __AUTH_CONST.__cfstring: 0x42ac0
-  __AUTH_CONST.__objc_const: 0xb4578
+  __DATA_CONST.__got: 0x2928
+  __AUTH_CONST.__const: 0x1800
+  __AUTH_CONST.__cfstring: 0x42c20
+  __AUTH_CONST.__objc_const: 0xb49b8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x4dd0
   __AUTH_CONST.__objc_dictobj: 0x3b60
-  __AUTH_CONST.__auth_got: 0x868
-  __AUTH.__objc_data: 0x15388
-  __DATA.__objc_ivar: 0x3d5c
-  __DATA.__data: 0x12f38
+  __AUTH_CONST.__auth_got: 0x870
+  __AUTH.__objc_data: 0x15478
+  __DATA.__objc_ivar: 0x3d70
+  __DATA.__data: 0x12ff8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x4858
   __DATA_DIRTY.__bss: 0x1a0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 30724
-  Symbols:   51870
-  CStrings:  9726
+  Functions: 30775
+  Symbols:   51980
+  CStrings:  9763
 
Symbols:
+ +[INIntentDeliveryEnvelope supportsBSXPCSecureCoding]
+ +[INIntentDeliveryListener sharedListener]
+ +[INIntentDeliveryRequest supportsBSXPCSecureCoding]
+ -[INAppIntentDeliverer _completeWithArchivedResponse:error:]
+ -[INAppIntentDeliverer _handleLaunchActionResponse:archivedForwardingAction:]
+ -[INAppIntentDeliverer _handshakeLaunchAction]
+ -[INAppIntentDeliverer _launchAction]
+ -[INAppIntentDeliverer deliveryConnection]
+ -[INAppIntentDeliverer setDeliveryConnection:]
+ -[INAppIntentDispatcher _dispatchIntentForwardingAction:auditToken:completionHandler:]
+ -[INAppIntentDispatcher dispatchIntentForwardingAction:verifiedPeerAuditToken:completionHandler:]
+ -[INAppResolver _resolvedAppMatchingDescriptor:options:]
+ -[INAppResolver cachedStrictMatchingResults]
+ -[INAppResolver resolvedAppMatchingDescriptor:options:]
+ -[INAppResolverOptions requireStrictMatching]
+ -[INIntentDeliveryEnvelope .cxx_destruct]
+ -[INIntentDeliveryEnvelope encodeWithBSXPCCoder:]
+ -[INIntentDeliveryEnvelope initWithBSXPCCoder:]
+ -[INIntentDeliveryEnvelope initWithListenerEndpoint:]
+ -[INIntentDeliveryEnvelope listenerEndpoint]
+ -[INIntentDeliveryListener .cxx_destruct]
+ -[INIntentDeliveryListener _init]
+ -[INIntentDeliveryListener deliverArchivedForwardingAction:endpoint:reply:]
+ -[INIntentDeliveryListener envelope]
+ -[INIntentDeliveryListener executionHandler]
+ -[INIntentDeliveryListener listener:shouldAcceptNewConnection:]
+ -[INIntentDeliveryListener listener]
+ -[INIntentDeliveryListener setExecutionHandler:]
+ -[INIntentDeliveryRequest encodeWithBSXPCCoder:]
+ -[INIntentDeliveryRequest initWithBSXPCCoder:]
+ -[INStartSendingUpdatesForwardingAction _updateObserverEndpoint:]
+ -[INStartSendingUpdatesForwardingAction setEndpoint:]
+ GCC_except_table10005
+ GCC_except_table10193
+ GCC_except_table10203
+ GCC_except_table10205
+ GCC_except_table10210
+ GCC_except_table10275
+ GCC_except_table10282
+ GCC_except_table10835
+ GCC_except_table10960
+ GCC_except_table10964
+ GCC_except_table11077
+ GCC_except_table11190
+ GCC_except_table11217
+ GCC_except_table11218
+ GCC_except_table11441
+ GCC_except_table11883
+ GCC_except_table12173
+ GCC_except_table12616
+ GCC_except_table12623
+ GCC_except_table12626
+ GCC_except_table12634
+ GCC_except_table12655
+ GCC_except_table13260
+ GCC_except_table13799
+ GCC_except_table13839
+ GCC_except_table13843
+ GCC_except_table14088
+ GCC_except_table14615
+ GCC_except_table15295
+ GCC_except_table15299
+ GCC_except_table16439
+ GCC_except_table16542
+ GCC_except_table16550
+ GCC_except_table16551
+ GCC_except_table16854
+ GCC_except_table18500
+ GCC_except_table19155
+ GCC_except_table19325
+ GCC_except_table19352
+ GCC_except_table19917
+ GCC_except_table19919
+ GCC_except_table19922
+ GCC_except_table20001
+ GCC_except_table21002
+ GCC_except_table21097
+ GCC_except_table21319
+ GCC_except_table22389
+ GCC_except_table22392
+ GCC_except_table22395
+ GCC_except_table23010
+ GCC_except_table23027
+ GCC_except_table23744
+ GCC_except_table25220
+ GCC_except_table25232
+ GCC_except_table27103
+ GCC_except_table27106
+ GCC_except_table27107
+ GCC_except_table27108
+ GCC_except_table27109
+ GCC_except_table28801
+ GCC_except_table28803
+ GCC_except_table28805
+ GCC_except_table28813
+ GCC_except_table28815
+ GCC_except_table28824
+ GCC_except_table29872
+ GCC_except_table29880
+ GCC_except_table29881
+ GCC_except_table29885
+ GCC_except_table29886
+ GCC_except_table29887
+ GCC_except_table29888
+ GCC_except_table29890
+ GCC_except_table29894
+ GCC_except_table29896
+ GCC_except_table29897
+ GCC_except_table29898
+ GCC_except_table29899
+ GCC_except_table29901
+ GCC_except_table30090
+ GCC_except_table5403
+ GCC_except_table5404
+ GCC_except_table5461
+ GCC_except_table5621
+ GCC_except_table5624
+ GCC_except_table5630
+ GCC_except_table5867
+ GCC_except_table5876
+ GCC_except_table6426
+ GCC_except_table6460
+ GCC_except_table6461
+ GCC_except_table6495
+ GCC_except_table7056
+ GCC_except_table7141
+ GCC_except_table7142
+ GCC_except_table7863
+ GCC_except_table8129
+ GCC_except_table8480
+ GCC_except_table8735
+ GCC_except_table8742
+ GCC_except_table9416
+ GCC_except_table9617
+ GCC_except_table9628
+ GCC_except_table9629
+ _BSActionErrorDomain
+ _INAppResolverOptionsRequireStrictMatchingKey
+ _INBundleIdentifiersAreLikelyVariants
+ _INIntentDeliveryEntitlement
+ _INIntentDeliveryEnvelopeInActionInfo
+ _INIntentDeliveryGetMode
+ _INIntentDeliveryModeForFlags
+ _INIntentDeliveryModeOverrideForTesting
+ _INIntentDeliveryObjectOfClassInActionInfo
+ _INIntentDeliveryPeerEntitlementOverrideForTesting
+ _INIntentDeliveryPeerIsEntitled
+ _INIntentDeliveryProcessDescription
+ _INIntentDeliveryReceivingXPCInterface
+ _INIntentDeliveryRequestInActionInfo
+ _INNamesAreEquivalent
+ _OBJC_CLASS_$_BSActionResponder
+ _OBJC_CLASS_$_BSMutableSettings
+ _OBJC_CLASS_$_BSSettings
+ _OBJC_CLASS_$_INIntentDeliveryEnvelope
+ _OBJC_CLASS_$_INIntentDeliveryListener
+ _OBJC_CLASS_$_INIntentDeliveryRequest
+ _OBJC_CLASS_$_NSXPCListener
+ _OBJC_IVAR_$_INAppIntentDeliverer._deliveryConnection
+ _OBJC_IVAR_$_INAppResolver._cachedStrictMatchingResults
+ _OBJC_IVAR_$_INIntentDeliveryEnvelope._listenerEndpoint
+ _OBJC_IVAR_$_INIntentDeliveryListener._executionHandler
+ _OBJC_IVAR_$_INIntentDeliveryListener._listener
+ _OBJC_METACLASS_$_INIntentDeliveryEnvelope
+ _OBJC_METACLASS_$_INIntentDeliveryListener
+ _OBJC_METACLASS_$_INIntentDeliveryRequest
+ _SecTaskCopySigningIdentifier
+ __INIntentDeliverySetModeOverrideForTesting
+ __INIntentDeliverySetPeerEntitlementOverrideForTesting
+ __OBJC_$_CLASS_METHODS_INIntentDeliveryEnvelope
+ __OBJC_$_CLASS_METHODS_INIntentDeliveryListener
+ __OBJC_$_CLASS_METHODS_INIntentDeliveryRequest
+ __OBJC_$_CLASS_PROP_LIST_INIntentDeliveryListener
+ __OBJC_$_INSTANCE_METHODS_INIntentDeliveryEnvelope
+ __OBJC_$_INSTANCE_METHODS_INIntentDeliveryListener
+ __OBJC_$_INSTANCE_METHODS_INIntentDeliveryRequest
+ __OBJC_$_INSTANCE_VARIABLES_INIntentDeliveryEnvelope
+ __OBJC_$_INSTANCE_VARIABLES_INIntentDeliveryListener
+ __OBJC_$_PROP_LIST_INIntentDeliveryEnvelope
+ __OBJC_$_PROP_LIST_INIntentDeliveryListener
+ __OBJC_$_PROP_LIST_INIntentDeliveryRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_INIntentDeliveryReceiving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_INIntentDeliveryReceiving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_INIntentDeliveryReceiving
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_INIntentDeliveryEnvelope
+ __OBJC_CLASS_PROTOCOLS_$_INIntentDeliveryListener
+ __OBJC_CLASS_PROTOCOLS_$_INIntentDeliveryRequest
+ __OBJC_CLASS_RO_$_INIntentDeliveryEnvelope
+ __OBJC_CLASS_RO_$_INIntentDeliveryListener
+ __OBJC_CLASS_RO_$_INIntentDeliveryRequest
+ __OBJC_LABEL_PROTOCOL_$_INIntentDeliveryReceiving
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_METACLASS_RO_$_INIntentDeliveryEnvelope
+ __OBJC_METACLASS_RO_$_INIntentDeliveryListener
+ __OBJC_METACLASS_RO_$_INIntentDeliveryRequest
+ __OBJC_PROTOCOL_$_INIntentDeliveryReceiving
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_INIntentDeliveryReceiving
+ ___37-[INAppIntentDeliverer _launchAction]_block_invoke
+ ___37-[INAppIntentDeliverer _launchAction]_block_invoke_2
+ ___42+[INIntentDeliveryListener sharedListener]_block_invoke
+ ___46-[INAppIntentDeliverer _handshakeLaunchAction]_block_invoke
+ ___56-[INAppResolver _resolvedAppMatchingDescriptor:options:]_block_invoke
+ ___75-[INIntentDeliveryListener deliverArchivedForwardingAction:endpoint:reply:]_block_invoke
+ ___77-[INAppIntentDeliverer _handleLaunchActionResponse:archivedForwardingAction:]_block_invoke
+ ___86-[INAppIntentDispatcher _dispatchIntentForwardingAction:auditToken:completionHandler:]_block_invoke
+ ___INIntentDeliveryObjectOfClassInActionInfo_block_invoke
+ ___block_descriptor_40_e8_32bs_e42_v16?0"INIntentForwardingActionResponse"8ls32l8
+ ___block_descriptor_40_e8_32s_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e26_v16?0"BSActionResponse"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e12_v24?0q8^B16ls32l8u48l8r40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e42_v16?0"INIntentForwardingActionResponse"8ls32l8r56l8s40l8s48l8
+ _sharedListener.onceToken
+ _sharedListener.sharedListener
- -[INAppResolver _resolvedAppMatchingDescriptor:]
- GCC_except_table10147
- GCC_except_table10157
- GCC_except_table10159
- GCC_except_table10164
- GCC_except_table10229
- GCC_except_table10236
- GCC_except_table10789
- GCC_except_table10914
- GCC_except_table10918
- GCC_except_table11031
- GCC_except_table11144
- GCC_except_table11171
- GCC_except_table11172
- GCC_except_table11395
- GCC_except_table11837
- GCC_except_table12127
- GCC_except_table12570
- GCC_except_table12577
- GCC_except_table12580
- GCC_except_table12588
- GCC_except_table12609
- GCC_except_table13214
- GCC_except_table13753
- GCC_except_table13793
- GCC_except_table13797
- GCC_except_table14042
- GCC_except_table14569
- GCC_except_table15249
- GCC_except_table15253
- GCC_except_table16393
- GCC_except_table16496
- GCC_except_table16504
- GCC_except_table16505
- GCC_except_table16807
- GCC_except_table18453
- GCC_except_table19108
- GCC_except_table19278
- GCC_except_table19305
- GCC_except_table19870
- GCC_except_table19872
- GCC_except_table19875
- GCC_except_table19953
- GCC_except_table20953
- GCC_except_table21048
- GCC_except_table21270
- GCC_except_table22338
- GCC_except_table22341
- GCC_except_table22344
- GCC_except_table22959
- GCC_except_table22976
- GCC_except_table23693
- GCC_except_table25169
- GCC_except_table25181
- GCC_except_table27052
- GCC_except_table27055
- GCC_except_table27056
- GCC_except_table27057
- GCC_except_table27058
- GCC_except_table28750
- GCC_except_table28752
- GCC_except_table28754
- GCC_except_table28762
- GCC_except_table28764
- GCC_except_table28773
- GCC_except_table29821
- GCC_except_table29829
- GCC_except_table29830
- GCC_except_table29834
- GCC_except_table29835
- GCC_except_table29836
- GCC_except_table29837
- GCC_except_table29839
- GCC_except_table29843
- GCC_except_table29845
- GCC_except_table29846
- GCC_except_table29847
- GCC_except_table29848
- GCC_except_table29850
- GCC_except_table30039
- GCC_except_table5401
- GCC_except_table5402
- GCC_except_table5459
- GCC_except_table5619
- GCC_except_table5622
- GCC_except_table5626
- GCC_except_table5865
- GCC_except_table5874
- GCC_except_table6422
- GCC_except_table6456
- GCC_except_table6457
- GCC_except_table6493
- GCC_except_table7054
- GCC_except_table7139
- GCC_except_table7140
- GCC_except_table7861
- GCC_except_table8127
- GCC_except_table8472
- GCC_except_table8724
- GCC_except_table8726
- GCC_except_table9403
- GCC_except_table9959
- ___48-[INAppResolver _resolvedAppMatchingDescriptor:]_block_invoke
- ___74-[INAppIntentDeliverer _deliverIntentForwardingActionWithResponseHandler:]_block_invoke_3
- ___74-[INAppIntentDeliverer _deliverIntentForwardingActionWithResponseHandler:]_block_invoke_4
- ___74-[INAppIntentDispatcher dispatchIntentForwardingAction:completionHandler:]_block_invoke
- ___block_descriptor_40_e8_32bs_e48_v16?0"INHandleIntentForwardingActionResponse"8ls32l8
CStrings:
+ "%@ (pid %d)"
+ "%s Failed to archive intent forwarding action response: %{public}@"
+ "%s Failed to unarchive intent delivery from pid %d: %{public}@"
+ "%s Failed to unarchive intent forwarding action response from %{public}@: %{public}@"
+ "%s Falling back to unverified intent delivery: UISIntentForwardingAction has no -initWithInfo:responder:"
+ "%s Falling back to unverified intent delivery: failed to archive the action: %{public}@"
+ "%s Ignoring a late handshake answer from %{public}@"
+ "%s Ignoring a second completion for intent delivery from pid %d"
+ "%s Intent delivery connection to %{public}@ failed: %{public}@"
+ "%s Intent delivery for %{public}@ got no handshake envelope back: %{public}@"
+ "%s Refusing intent delivery from pid %d: no execution handler is installed"
+ "%s Rejecting intent delivery connection: verified delivery is off"
+ "%s Rejecting intent delivery from %{public}@: missing %{public}@"
+ "%s Replacing unexpected %{public}@ from %{public}@ with an error"
+ "%s Would reject intent delivery from %{public}@: missing %{public}@ (audit mode)"
+ "-[INAppIntentDeliverer _completeWithArchivedResponse:error:]"
+ "-[INAppIntentDeliverer _handleLaunchActionResponse:archivedForwardingAction:]"
+ "-[INAppIntentDeliverer _handleLaunchActionResponse:archivedForwardingAction:]_block_invoke"
+ "-[INAppIntentDeliverer _handshakeLaunchAction]"
+ "-[INAppIntentDeliverer completeWithIntentForwardingActionResponse:]"
+ "-[INIntentDeliveryListener deliverArchivedForwardingAction:endpoint:reply:]"
+ "-[INIntentDeliveryListener deliverArchivedForwardingAction:endpoint:reply:]_block_invoke"
+ "-[INIntentDeliveryListener listener:shouldAcceptNewConnection:]"
+ "0@`"
+ "<unknown>"
+ "Application answered with an unexpected response"
+ "Application answered with an unreadable response"
+ "Application did not answer the delivery handshake"
+ "Application did not answer the delivery handshake in time"
+ "No intent delivery handler is installed"
+ "RequireStrictMatching"
+ "Unreadable intent forwarding action"
+ "com.apple.private.intents.delivery"
+ "intent_delivery_enforce"
+ "intent_delivery_handshake"
+ "listenerEndpoint"
+ "v16@?0@\"BSActionResponse\"8"
+ "v24@?0q8^B16"
- "v16@?0@\"INHandleIntentForwardingActionResponse\"8"
```
