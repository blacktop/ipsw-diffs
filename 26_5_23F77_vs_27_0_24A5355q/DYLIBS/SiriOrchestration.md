## SiriOrchestration

> `/System/Library/PrivateFrameworks/SiriOrchestration.framework/SiriOrchestration`

```diff

-3404.2.1.0.0
-  __TEXT.__text: 0xb2c
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_methlist: 0xb0
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x83
-  __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x25
-  __TEXT.__objc_methname: 0x287
-  __TEXT.__objc_methtype: 0x50
-  __TEXT.__objc_stubs: 0x300
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x50
-  __DATA_CONST.__objc_classlist: 0x10
+3600.13.1.0.0
+  __TEXT.__text: 0x0
+  __TEXT.__const: 0x4a
+  __DATA_CONST.__const: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc0
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x1a0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x8
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
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
