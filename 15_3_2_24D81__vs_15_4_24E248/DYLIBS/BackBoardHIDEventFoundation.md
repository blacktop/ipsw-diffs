## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/Versions/A/BackBoardHIDEventFoundation`

```diff

-668.4.1.0.0
-  __TEXT.__text: 0x2548c
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x1424
+668.5.29.0.0
+  __TEXT.__text: 0x2597c
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_methlist: 0x1934
   __TEXT.__const: 0xf4
   __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__cstring: 0x2419
-  __TEXT.__oslogstring: 0x1b7c
+  __TEXT.__cstring: 0x24a4
+  __TEXT.__oslogstring: 0x1b8c
   __TEXT.__ustring: 0x5c
-  __TEXT.__unwind_info: 0x700
-  __TEXT.__objc_classname: 0x759
-  __TEXT.__objc_methname: 0x4288
-  __TEXT.__objc_methtype: 0x1548
-  __TEXT.__objc_stubs: 0x2e00
+  __TEXT.__unwind_info: 0x718
+  __TEXT.__objc_classname: 0x755
+  __TEXT.__objc_methname: 0x42e9
+  __TEXT.__objc_methtype: 0x15d2
+  __TEXT.__objc_stubs: 0x2e40
   __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0x3a8
+  __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_selrefs: 0xf98
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x290
-  __AUTH_CONST.__auth_got: 0x438
-  __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x2480
-  __AUTH_CONST.__objc_const: 0x51d0
+  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__const: 0x1130
+  __AUTH_CONST.__cfstring: 0x24a0
+  __AUTH_CONST.__objc_const: 0x4938
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xd20
-  __DATA.__objc_ivar: 0x378
+  __DATA.__objc_ivar: 0x374
   __DATA.__data: 0x900
   __DATA.__bss: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/Versions/A/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DE7E801D-ADF0-3E36-90DF-BADFFAB79BC2
-  Functions: 641
-  Symbols:   2100
-  CStrings:  1790
+  UUID: 9417E544-BDB3-35A5-B313-43A687EA5967
+  Functions: 652
+  Symbols:   2118
+  CStrings:  1798
 
Symbols:
+ -[BKHIDClientConnection copyConnection]
+ -[BKHIDClientConnection sendEvent:]
+ -[BKHIDClientConnectionManager _lock_clientForDestination:]
+ -[BKHIDClientConnectionManager sendEvent:toClientTaskPort:]
+ -[BKHIDClientConnectionManager sendEvent:toDestination:]
+ -[BKHIDEventDeliveryManagerServer _performDescriptionRetrieval:forAuditToken:]
+ -[BKHIDEventDeliveryManagerServer resolutionDescriptionForEventDescriptor:senderDescriptor:]
+ -[BKHIDEventDeliveryManagerServer resolutionDescriptionForKeyCommand:senderDescriptor:]
+ -[BKIOHIDServiceMatcher _lock_asyncNotifyServicesAdded:]
+ -[BKIOHIDServiceMatcher _lock_didAddIOHIDServiceRefs:]
+ -[BKIOHIDServiceMatcher _startObserving:queue:sync:]
+ -[BKIOHIDServiceMatcher startObservingSynchronously:]
+ GCC_except_table180
+ GCC_except_table278
+ GCC_except_table290
+ GCC_except_table295
+ GCC_except_table303
+ GCC_except_table308
+ GCC_except_table341
+ GCC_except_table543
+ GCC_except_table591
+ OBJC_IVAR_$_BKHIDClientConnection._lock_connection
+ OBJC_IVAR_$_BKIOHIDServiceMatcher._observeSynchronously
+ _CFAutorelease
+ _OBJC_CLASS_$_BSDescriptionStyle
+ __76-[BKHIDEventDeliveryManager _lock_notifyObserversForReason:chainsMayUpdate:]_block_invoke.252
+ ___56-[BKIOHIDServiceMatcher _lock_asyncNotifyServicesAdded:]_block_invoke
+ ___59-[BKHIDEventDeliveryManagerServer deliveryGraphDescription]_block_invoke
+ ___70-[BKHIDEventDeliveryManager _lock_setDeferringRules:forClientWithPID:]_block_invoke_2
+ ___81-[BKHIDEventDeliveryManagerServer connectionDescriptionForDeferringRuleIdentity:]_block_invoke
+ ___87-[BKHIDEventDeliveryManagerServer resolutionDescriptionForKeyCommand:senderDescriptor:]_block_invoke
+ ___92-[BKHIDEventDeliveryManagerServer resolutionDescriptionForEventDescriptor:senderDescriptor:]_block_invoke
+ ___block_descriptor_32_e35_v16?0"BSMutableDescriptionStyle"8l
+ ___block_descriptor_32_e45_"NSString"16?0"BKHIDEventDeliveryManager"8l
+ ___block_descriptor_40_e8_32s_e45_"NSString"16?0"BKHIDEventDeliveryManager"8l
+ ___block_descriptor_48_e8_32s40s_e45_"NSString"16?0"BKHIDEventDeliveryManager"8l
+ __block_literal_global.1360
+ __block_literal_global.1530
+ __block_literal_global.1780
+ __block_literal_global.1912
+ __block_literal_global.225
+ __block_literal_global.230
+ __block_literal_global.2707
+ __block_literal_global.2866
+ __block_literal_global.287
+ __block_literal_global.3002
+ __block_literal_global.512
+ _objc_msgSend$copyConnection
+ _objc_msgSend$descriptionForRootObject:withStyle:
+ _objc_msgSend$descriptionOfResolutionPathForEventDescriptor:senderDescriptor:
+ _objc_msgSend$descriptionOfResolutionPathForKeyCommand:senderDescriptor:
+ _objc_msgSend$sendEvent:toClientTaskPort:
+ _objc_msgSend$sendEvent:toDestination:
+ _objc_msgSend$setMaximumValueLengthBeforeTruncation:
+ _objc_msgSend$setValueTruncation:
+ sharedInstance.onceToken.2706
- -[BKHIDClientConnection addDisconnectionObserverBlock:]
- -[BKHIDClientConnection processDeathWatcher]
- -[BKHIDClientConnection setProcessDeathWatcher:]
- -[BKHIDClientConnectionManager addRemovalObserverForConnectionWithVersionedPID:observerBlock:]
- -[BKIOHIDServiceMatcher _lock_servicesAdded:]
- GCC_except_table178
- GCC_except_table276
- GCC_except_table288
- GCC_except_table293
- GCC_except_table299
- GCC_except_table304
- GCC_except_table337
- GCC_except_table532
- GCC_except_table580
- OBJC_IVAR_$_BKHIDClientConnection._connection
- OBJC_IVAR_$_BKHIDClientConnection._observerAssertion
- OBJC_IVAR_$_BKHIDClientConnection._processDeathWatcher
- _OBJC_CLASS_$_BSCompoundAssertion
- __76-[BKHIDEventDeliveryManager _lock_notifyObserversForReason:chainsMayUpdate:]_block_invoke.248
- __BKSendHIDEventToClientConnection
- ___45-[BKIOHIDServiceMatcher _lock_servicesAdded:]_block_invoke
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0l
- __block_literal_global.1368
- __block_literal_global.1779
- __block_literal_global.1908
- __block_literal_global.226
- __block_literal_global.2706
- __block_literal_global.2864
- __block_literal_global.290
- __block_literal_global.3000
- __block_literal_global.522
- _objc_msgSend$acquireForReason:withContext:
- _objc_msgSend$addDisconnectionObserverBlock:
- _objc_msgSend$assertionWithIdentifier:
- _objc_msgSend$context
- _objc_msgSend$copyClientForDestination:
- _objc_msgSend$copyClientForTaskPort:
- sharedInstance.onceToken.2705
CStrings:
+ "@\"NSString\"16@?0@\"BKHIDEventDeliveryManager\"8"
+ "@\"NSString\"32@0:8@\"BKSHIDEventDescriptor\"16@\"BKSHIDEventSenderDescriptor\"24"
+ "@\"NSString\"32@0:8@\"BKSHIDEventKeyCommand\"16@\"BKSHIDEventSenderDescriptor\"24"
+ "AB"
+ "_lock_asyncNotifyServicesAdded:"
+ "_lock_connection"
+ "_observeSynchronously"
+ "_startObserving:queue:sync:"
+ "copyConnection"
+ "descriptionForRootObject:withStyle:"
+ "missing queue for async case"
+ "new key command registrations for pid:%d %{public}@"
+ "no client connection for destination %{public}@"
+ "resolutionDescriptionForEventDescriptor:senderDescriptor:"
+ "resolutionDescriptionForKeyCommand:senderDescriptor:"
+ "sendEvent:toClientTaskPort:"
+ "sendEvent:toDestination:"
+ "setMaximumValueLengthBeforeTruncation:"
+ "setValueTruncation:"
+ "shouldn't be possible to be invalid here"
+ "startObservingSynchronously:"
+ "v16@?0@\"BSMutableDescriptionStyle\"8"
+ "v28@0:8^{__IOHIDEvent=}16I24"
+ "v32@0:8^{__IOHIDEvent=}16@24"
+ "wrong code path, pal"
- "%p disconnectionObservers"
- "<%@:%p>"
- "@\"BSCompoundAssertion\""
- "@\"BSProcessDeathWatcher\""
- "@24@0:8@?16"
- "@32@0:8q16@?24"
- "T@\"BSProcessDeathWatcher\",&,N,V_processDeathWatcher"
- "_connection"
- "_observerAssertion"
- "_processDeathWatcher"
- "acquireForReason:withContext:"
- "addDisconnectionObserverBlock:"
- "addRemovalObserverForConnectionWithVersionedPID:observerBlock:"
- "assertionWithIdentifier:"
- "context"
- "new key command registrations for pid:%d env:%{public}@ token:%{public}@ %{public}@"
- "processDeathWatcher"
- "setProcessDeathWatcher:"

```
