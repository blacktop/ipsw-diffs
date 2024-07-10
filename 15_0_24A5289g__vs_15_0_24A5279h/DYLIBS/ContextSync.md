## ContextSync

> `/System/Library/PrivateFrameworks/ContextSync.framework/Versions/A/ContextSync`

```diff

-153.0.7.0.0
-  __TEXT.__text: 0x122a8
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x938
-  __TEXT.__const: 0x90
+151.0.0.0.0
+  __TEXT.__text: 0x1207c
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_methlist: 0x8d8
+  __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x450
-  __TEXT.__cstring: 0xc63
-  __TEXT.__oslogstring: 0x104a
+  __TEXT.__cstring: 0xc27
+  __TEXT.__oslogstring: 0xfad
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x410
-  __TEXT.__objc_classname: 0x279
-  __TEXT.__objc_methname: 0x2e3d
-  __TEXT.__objc_methtype: 0x1052
-  __TEXT.__objc_stubs: 0x1d40
-  __DATA_CONST.__got: 0x178
+  __TEXT.__objc_classname: 0x22a
+  __TEXT.__objc_methname: 0x2d60
+  __TEXT.__objc_methtype: 0xfe3
+  __TEXT.__objc_stubs: 0x1d00
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x108
-  __DATA_CONST.__objc_classlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x940
+  __DATA_CONST.__objc_selrefs: 0x920
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__objc_superrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x1c70
+  __AUTH_CONST.__objc_const: 0x1b08
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0x240
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x9c
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 342
-  Symbols:   929
-  CStrings:  119
+  Functions: 333
+  Symbols:   903
+  CStrings:  118
 
Symbols:
+ -[BMDistributedContextService sendLocalSubscriptionToDevice:]
+ __48-[BMDistributedContextService loadSubscriptions]_block_invoke.42
+ __66-[BMDistributedContextService registerSinkWithIdentifier:withDSL:]_block_invoke.48
+ __66-[BMDistributedContextService registerSinkWithIdentifier:withDSL:]_block_invoke.48.cold.1
+ __66-[BMDistributedContextService registerSinkWithIdentifier:withDSL:]_block_invoke.49
+ _objc_msgSend$sendLocalSubscriptionToDevice:
- +[BMDistributedContextSubscriptionManager loadAndMigrateStorageFromLegacyToV1:withLocalDeviceID:].cold.1
- +[BMDistributedContextSubscriptionManager loadFromStorage:withLocalDeviceID:].cold.1
- -[BMDistributedContextService assertLocalSubscriptionsToDevice:shouldSendIfNoSubscriptions:]
- -[BMDistributedContextService setSubscriptionStorage:]
- -[BMDistributedContextService subscriptionStorage]
- -[BMDistributedContextUserDefaultStorage .cxx_destruct]
- -[BMDistributedContextUserDefaultStorage initWithUserDefault:]
- -[BMDistributedContextUserDefaultStorage objectForKey:]
- -[BMDistributedContextUserDefaultStorage removeObjectForKey:]
- -[BMDistributedContextUserDefaultStorage setObject:forKey:]
- OBJC_IVAR_$_BMDistributedContextService._subscriptionStorage
- OBJC_IVAR_$_BMDistributedContextUserDefaultStorage._storage
- _OBJC_CLASS_$_BMDistributedContextUserDefaultStorage
- _OBJC_CLASS_$_NSData
- _OBJC_METACLASS_$_BMDistributedContextUserDefaultStorage
- __48-[BMDistributedContextService loadSubscriptions]_block_invoke.44
- __66-[BMDistributedContextService registerSinkWithIdentifier:withDSL:]_block_invoke.50.cold.1
- __66-[BMDistributedContextService registerSinkWithIdentifier:withDSL:]_block_invoke.51
- __66-[BMDistributedContextService registerSinkWithIdentifier:withDSL:]_block_invoke.52
- __OBJC_$_INSTANCE_METHODS_BMDistributedContextUserDefaultStorage
- __OBJC_$_INSTANCE_VARIABLES_BMDistributedContextUserDefaultStorage
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMDistributedContextSubscriptionStorage
- __OBJC_$_PROTOCOL_METHOD_TYPES_BMDistributedContextSubscriptionStorage
- __OBJC_CLASS_PROTOCOLS_$_BMDistributedContextUserDefaultStorage
- __OBJC_CLASS_RO_$_BMDistributedContextUserDefaultStorage
- __OBJC_LABEL_PROTOCOL_$_BMDistributedContextSubscriptionStorage
- __OBJC_METACLASS_RO_$_BMDistributedContextUserDefaultStorage
- __OBJC_PROTOCOL_$_BMDistributedContextSubscriptionStorage
- _objc_msgSend$assertLocalSubscriptionsToDevice:shouldSendIfNoSubscriptions:
- _objc_msgSend$data
- _objc_msgSend$initWithUserDefault:
- _os_transaction_create
CStrings:
- "com.apple.biomesyncd.load-distributed-context-subscriptions"

```
