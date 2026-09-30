## SiriRequestDispatcher

> `/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher`

```diff

-3403.3.1.0.0
-  __TEXT.__text: 0x24bac
-  __TEXT.__auth_stubs: 0x1250
-  __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0x10a0
-  __TEXT.__cstring: 0x1098
-  __TEXT.__swift5_typeref: 0x8bd
-  __TEXT.__swift5_fieldmd: 0x598
-  __TEXT.__constg_swiftt: 0xc98
+3404.62.2.0.0
+  __TEXT.__text: 0x2752c
+  __TEXT.__auth_stubs: 0x12d0
+  __TEXT.__objc_methlist: 0x540
+  __TEXT.__const: 0x1500
+  __TEXT.__cstring: 0xdc8
+  __TEXT.__swift5_typeref: 0xbfb
+  __TEXT.__swift5_fieldmd: 0x684
+  __TEXT.__constg_swiftt: 0xf18
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x698
+  __TEXT.__swift5_reflstr: 0x6d8
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x68
-  __TEXT.__swift5_types: 0x84
-  __TEXT.__oslogstring: 0x1c17
-  __TEXT.__swift5_capture: 0x29c
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_proto: 0x80
+  __TEXT.__swift5_types: 0x94
+  __TEXT.__oslogstring: 0x1f97
+  __TEXT.__swift5_capture: 0x380
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x830
-  __TEXT.__eh_frame: 0x380
+  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__eh_frame: 0x960
   __TEXT.__objc_classname: 0xb1
-  __TEXT.__objc_methname: 0x1321
-  __TEXT.__objc_methtype: 0x752
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x258
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__objc_methname: 0x1336
+  __TEXT.__objc_methtype: 0x778
+  __DATA_CONST.__got: 0x2f0
+  __DATA_CONST.__const: 0x288
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x308
+  __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_protorefs: 0x58
-  __AUTH_CONST.__auth_got: 0x928
-  __AUTH_CONST.__auth_ptr: 0x2a8
-  __AUTH_CONST.__const: 0x1138
-  __AUTH_CONST.__objc_const: 0x3a50
+  __AUTH_CONST.__auth_got: 0x968
+  __AUTH_CONST.__auth_ptr: 0x2d8
+  __AUTH_CONST.__const: 0x14b0
+  __AUTH_CONST.__objc_const: 0x3c38
   __AUTH.__objc_data: 0xb0
-  __AUTH.__data: 0x50
-  __DATA.__data: 0x6f8
-  __DATA.__bss: 0x900
-  __DATA.__common: 0x10
+  __AUTH.__data: 0x28
+  __DATA.__data: 0x6c8
+  __DATA.__bss: 0xb00
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xd38
-  __DATA_DIRTY.__common: 0x98
-  __DATA_DIRTY.__bss: 0x280
+  __DATA_DIRTY.__data: 0xd98
+  __DATA_DIRTY.__common: 0xb8
+  __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1072
-  Symbols:   480
-  CStrings:  472
+  Functions: 1153
+  Symbols:   534
+  CStrings:  469
 
Symbols:
+ _swift_allocBox
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_deallocPartialClassInstance
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_getDynamicType
+ _swift_initStructMetadataWithLayoutString
+ _swift_isClassType
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _swift_willThrowTypedImpl
- _AFDeviceSupportsSAE
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
+ "%s was not able to handle: %{public}s: Command is not registered with bridge."
+ "%{public}s was not able to handle: %{public}s: Command group is not registered with bridge"
+ "Bridge \"%{public}s\" received message: %{public}@"
+ "Bridge %{public}s took more than 60 seconds to process %{public}s."
+ "Cannot get command encoded name %{public}s"
+ "Cannot get command group identifier %{public}s"
+ "Command %{public}s does not have encodedClassName"
+ "Command %{public}s does not have group identifier"
+ "Could not find a refId on this command: %{public}s"
+ "Dispatching command %{public}s to the handle method"
+ "Ending active request with message: %{public}s"
+ "Ending candidate request with message: %{public}s"
+ "Found an existing candidate RequestProcessor for requestId: %{public}s"
+ "Input command type: %{public}s but expected type: %{public}s"
+ "Input message type: %{public}s but expected type: %{public}s"
+ "Lifecycle of %{public}s has ended before message dispatch could start."
+ "Lifecycle of %{public}s has ended before receiving next %{public}s."
+ "Message %{public}s is not registered properly"
+ "Message handler invoking object is of type: %{public}s but expected type: %{public}s"
+ "Message handler invoking object is of unexpected type. Actual: %{public}s, Expected: %{public}s"
+ "Message type: %{public}s is already registered with bridge"
+ "MessageHandlerType for %{public}@ is: %{public}s"
+ "MessageProcessingTime"
+ "Not creating a CandidateRequestProcessor for message: %s because there is already a candidate request started with requestId: %s"
+ "Not handling message: %{public}s with requestId: %{public}s since no handlers were found"
+ "Processing of %{public}s by %{public}s was canceled."
+ "Received %{public}s, but %{public}s did not subscribe to it."
+ "Received finisher message: %{public}s while there is no CandidateRequestProcessor for requestId: %s"
+ "Replacing already registered method to handle command: %{public}s:%{public}s, replacing"
+ "RequestProcessor cannot handle message: %{public}s"
+ "RequestProcessor threw error: %s while handling message: %{public}s"
+ "Starting active request with message: %{public}s"
+ "Starting candidate request with message: %{public}s"
+ "Unknown error happened while %{public}s was processing %{public}s: %{public}s."
+ "_TtC21SiriRequestDispatcher27SimpleSubscriptionRegistrar"
+ "container"
+ "handleMessage got message type %{public}s which is not registered with the bridge"
+ "messageHandlers"
+ "messageTypes"
+ "publisher"
+ "registerInternalGestureTestingHandler:"
+ "stream"
+ "v24@0:8@?<v@?qB@?<v@?B@\"NSString\">>16"
+ "wrappedBridge"
- "%s was not able to handle: %s, command is not register. Falling back to super.handle()"
- "%s was not able to handle: %s, group is not register. Falling back to super.handle()"
- "Cannot get command encode name %s"
- "Cannot get command group identifier %s"
- "Commnad %s don't have encodedClassName, failed command"
- "Commnad %s don't have group identifier, failed command"
- "Could not find a RequestProcessor for message: %s with requestId: %s"
- "Ending active request with message: %s"
- "Ending candidate request with message: %s"
- "Fatal error"
- "Found an existing candidate RequestProcessor for requestId: %s"
- "Handler invoking object is of type %s and not of type %s"
- "Input command %s of type %s is not of type %s"
- "Input message %s of type %s is not of type %s"
- "Insufficient space allocated to copy string contents"
- "Message %@ is not registered properly"
- "Message type: %s is already registered so ignore this request"
- "MessageHandlerType for %@ is: %s"
- "Not creating a CandidateRequestProcessor for message: %@ because there is already a candidate request started with requestId: %s"
- "Received finisher message: %@ while there is no CandidateRequestProcessor for requestId: %s"
- "RequestProcessor cannot handle message: %@"
- "RequestProcessor threw error: %s while handling message: %s"
- "Siri"
- "Starting active request with message: %s"
- "Starting candidate request with message: %s"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "There is already a method register to handle command: %s:%s, replacing"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "dispatch command %s to the handle method"
- "handleMessage got message type %s with message id: %s which is not registered with the bridge"
- "invalid Collection: less than 'count' elements in collection"
- "isIFFlowEnabled"
- "isReuseEagerChildRequestForIFEnabled"
- "personaIdentifier"
- "reuseEagerChildRequestForIF"
- "siri_ifflow"

```
