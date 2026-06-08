## SiriOrchestration

> `/System/Library/PrivateFrameworks/SiriOrchestration.framework/SiriOrchestration`

```diff

-3404.2.1.0.0
-  __TEXT.__text: 0xb2c sha256:471c27fb5a5fe726590fe003ef47e9e79d7aafb74c1f27cfd75905bda17eafe2
-  __TEXT.__auth_stubs: 0x170 sha256:deebf4d4bb7ade3291f561033d69d8da9dc8581775c0e23f5f6232b8d2887ca2
-  __TEXT.__objc_methlist: 0xb0 sha256:1070621eb30493671ed58f8d6e4ac82cbc09bcb9894db5bc2f4207154a384e48
-  __TEXT.__const: 0x50 sha256:4f39d04dc06e2f96105b40fd9ebd94a10541a69129f733beb4b2f6b91766be2a
-  __TEXT.__cstring: 0x83 sha256:3df3b45451dd96a9ef3ffe69bf51d192918c934ff70b88234007f2ffc54fd421
-  __TEXT.__unwind_info: 0xa8 sha256:75edc2266e1547cbcad4878a08f48b246f6bdae093d6fc2212f27d7dd1f10cdf
-  __TEXT.__objc_classname: 0x25 sha256:2cedd1985e68596caa6f46a98563e2790b5ebd131c4cc031f07b3944c556ca56
-  __TEXT.__objc_methname: 0x287 sha256:35d214c72c30c3c1a12fa4f0fcfb07973b0413ad23e788e0ac4d0a8842696986
-  __TEXT.__objc_methtype: 0x50 sha256:889fc6ef668fb1726d73ff8dce9850d63b688681db2a5d7c80be166057b268e2
-  __TEXT.__objc_stubs: 0x300 sha256:5863f6b398bda1bb5ac70e70df4927e2078656b190c1f3c4b5e384c4a3779def
-  __DATA_CONST.__got: 0x38 sha256:6819888f7c2dcc31ecb0c0ea06ea48ea82399f12fb83512cf21822109f4fa209
-  __DATA_CONST.__const: 0x50 sha256:e2c60b201273ae92896860b4077bd3780b505cbeae4eb896a317948aac3d7eb4
-  __DATA_CONST.__objc_classlist: 0x10 sha256:0c54791a93fa6e09f9c686e919d7efd2b2452e832f01a740e98a69951bc5e361
-  __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x100 sha256:4bf7ab39e845598e21b3c98a94561abffb8fe837dae74a652d6d35bbef8eb2a2
-  __DATA_CONST.__objc_superrefs: 0x10 sha256:69a4848a890c442451a2b3442ee9097079723dbdbebec6641fe48923d6c46112
-  __AUTH_CONST.__auth_got: 0xc0 sha256:5d89f056865052bcb89c910d2d62872e029fb273c3db03f8968a52a41593c1b5
-  __AUTH_CONST.__cfstring: 0x40 sha256:948ac6379e5190b838761d5e738ddd8d43c60faa0929a62da6b668ea4a754e64
-  __AUTH_CONST.__objc_const: 0x1a0 sha256:e787619592b825a9a05a175cde2f69b8249ad69531d7a99b27f4831d2f80b5b8
-  __AUTH.__objc_data: 0xa0 sha256:167f3f315f1ef6a0eaecf6e496dd8902741c28b2c0ccfb58057b11120ac27ca3
-  __DATA.__objc_ivar: 0x8 sha256:c0cdbb6e45249a718e7e605f801cf43f673a22fcf0347034da71f6be2e4f4d5e
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+3600.13.1.0.0
+  __TEXT.__text: 0x0
+  __TEXT.__const: 0x4a sha256:9eda718af5b20692d1c28e17f21bdcd65f44ab05d6314ea46764020b196f22b5
+  __DATA_CONST.__const: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
+  __DATA_CONST.__objc_imageinfo: 0x8 sha256:ce857dcadc2529f941104469975d60698ea3610a86c121e7b4aee224cd0c59ea
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6CDEFAF8-6ACE-361E-BFEF-BF9B6D4F46E3
-  Functions: 20
-  Symbols:   114
-  CStrings:  52
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  UUID: EC257CC7-5731-3412-9125-D6CC697F283D
+  Functions: 0
+  Symbols:   8
+  CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
- -[MulticastMessageForwarder .cxx_destruct]
- -[MulticastMessageForwarder addReceiver:]
- -[MulticastMessageForwarder cleanupNilReceivers]
- -[MulticastMessageForwarder forwardInvocation:]
- -[MulticastMessageForwarder init]
- -[MulticastMessageForwarder methodSignatureForSelector:]
- -[MulticastMessageForwarder receivers]
- -[MulticastMessageForwarder removeReceiver:]
- -[MulticastMessageForwarder respondsToSelector:]
- -[MulticastMessageForwarder setReceivers:]
- -[Receiver .cxx_destruct]
- -[Receiver initWithWrappedObject:]
- -[Receiver setWrappedObject:]
- -[Receiver wrappedObject]
- <redacted>
- _NSStringFromSelector
- _OBJC_CLASS_$_MulticastMessageForwarder
- _OBJC_CLASS_$_NSException
- _OBJC_CLASS_$_NSInvocation
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSMutableIndexSet
- _OBJC_CLASS_$_NSObject
- _OBJC_CLASS_$_Receiver
- _OBJC_IVAR_$_MulticastMessageForwarder._receivers
- _OBJC_IVAR_$_Receiver._wrappedObject
- _OBJC_METACLASS_$_MulticastMessageForwarder
- _OBJC_METACLASS_$_NSObject
- _OBJC_METACLASS_$_Receiver
- _OUTLINED_FUNCTION_0
- __NSConcreteStackBlock
- __OBJC_$_INSTANCE_METHODS_MulticastMessageForwarder
- __OBJC_$_INSTANCE_METHODS_Receiver
- __OBJC_$_INSTANCE_VARIABLES_MulticastMessageForwarder
- __OBJC_$_INSTANCE_VARIABLES_Receiver
- __OBJC_$_PROP_LIST_MulticastMessageForwarder
- __OBJC_$_PROP_LIST_Receiver
- __OBJC_CLASS_RO_$_MulticastMessageForwarder
- __OBJC_CLASS_RO_$_Receiver
- __OBJC_METACLASS_RO_$_MulticastMessageForwarder
- __OBJC_METACLASS_RO_$_Receiver
- ___41-[MulticastMessageForwarder addReceiver:]_block_invoke
- ___44-[MulticastMessageForwarder removeReceiver:]_block_invoke
- ___48-[MulticastMessageForwarder cleanupNilReceivers]_block_invoke
- ___CFConstantStringClassReference
- ___block_descriptor_40_e8_32s_e25_B32?0"Receiver"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e25_v32?0"Receiver"8Q16^B24ls32l8
- ___stack_chk_fail
- ___stack_chk_guard
- __objc_empty_cache
- _objc_alloc
- _objc_autoreleaseReturnValue
- _objc_destroyWeak
- _objc_enumerationMutation
- _objc_loadWeakRetained
- _objc_msgSend
- _objc_msgSend$addIndex:
- _objc_msgSend$addObject:
- _objc_msgSend$array
- _objc_msgSend$count
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$getArgument:atIndex:
- _objc_msgSend$getArgumentTypeAtIndex:
- _objc_msgSend$indexOfObjectPassingTest:
- _objc_msgSend$indexSet
- _objc_msgSend$initWithWrappedObject:
- _objc_msgSend$invocationWithMethodSignature:
- _objc_msgSend$invokeWithTarget:
- _objc_msgSend$methodSignature
- _objc_msgSend$methodSignatureForSelector:
- _objc_msgSend$numberOfArguments
- _objc_msgSend$raise:format:
- _objc_msgSend$receivers
- _objc_msgSend$removeObjectAtIndex:
- _objc_msgSend$removeObjectsAtIndexes:
- _objc_msgSend$selector
- _objc_msgSend$setArgument:atIndex:
- _objc_msgSend$setSelector:
- _objc_msgSend$wrappedObject
- _objc_msgSendSuper2
- _objc_opt_respondsToSelector
- _objc_release
- _objc_release_x19
- _objc_release_x20
- _objc_release_x21
- _objc_release_x22
- _objc_release_x23
- _objc_release_x27
- _objc_release_x28
- _objc_release_x8
- _objc_retainAutorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_storeStrong
- _objc_storeWeak
CStrings:
- ".cxx_destruct"
- "@"
- "@\"NSMutableArray\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "B24@0:8:16"
- "B32@?0@\"Receiver\"8Q16^B24"
- "MulticastMessageForwarder"
- "Receiver"
- "Selector %@ has unsupported argument typed %s at index %lu"
- "T@\"NSMutableArray\",&,N,V_receivers"
- "T@,W,N,V_wrappedObject"
- "UnsupportedArgument"
- "_receivers"
- "_wrappedObject"
- "addIndex:"
- "addObject:"
- "addReceiver:"
- "array"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "enumerateObjectsUsingBlock:"
- "forwardInvocation:"
- "getArgument:atIndex:"
- "getArgumentTypeAtIndex:"
- "indexOfObjectPassingTest:"
- "indexSet"
- "init"
- "initWithWrappedObject:"
- "invocationWithMethodSignature:"
- "invokeWithTarget:"
- "methodSignature"
- "methodSignatureForSelector:"
- "numberOfArguments"
- "raise:format:"
- "receivers"
- "removeObjectAtIndex:"
- "removeObjectsAtIndexes:"
- "removeReceiver:"
- "respondsToSelector:"
- "selector"
- "setArgument:atIndex:"
- "setReceivers:"
- "setSelector:"
- "setWrappedObject:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@?0@\"Receiver\"8Q16^B24"
- "wrappedObject"

```
