## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation`

```diff

-835.4.1.0.0
-  __TEXT.__text: 0x8bd54
-  __TEXT.__auth_stubs: 0x19d0
-  __TEXT.__objc_methlist: 0x682c
-  __TEXT.__cstring: 0x324f
-  __TEXT.__swift5_typeref: 0x980
-  __TEXT.__swift5_capture: 0x4e4
-  __TEXT.__swift5_reflstr: 0x433
-  __TEXT.__swift5_assocty: 0x80
-  __TEXT.__const: 0x19b0
-  __TEXT.__constg_swiftt: 0xcc4
-  __TEXT.__swift5_fieldmd: 0x628
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x90
-  __TEXT.__swift5_protos: 0x1c
-  __TEXT.__oslogstring: 0x3cda
-  __TEXT.__gcc_except_tab: 0x1ab8
+856.5.4.0.0
+  __TEXT.__text: 0x8e330
+  __TEXT.__auth_stubs: 0x1b10
+  __TEXT.__objc_methlist: 0x72c4
+  __TEXT.__const: 0x1be0
   __TEXT.__dlopen_cstrs: 0x10a
+  __TEXT.__cstring: 0x3010
+  __TEXT.__swift5_typeref: 0xb35
+  __TEXT.__swift5_capture: 0x59c
+  __TEXT.__swift_as_entry: 0x184
+  __TEXT.__swift_as_ret: 0x1ac
+  __TEXT.__swift5_reflstr: 0x463
+  __TEXT.__swift5_assocty: 0x98
+  __TEXT.__constg_swiftt: 0xef8
+  __TEXT.__swift5_fieldmd: 0x6b0
+  __TEXT.__swift5_proto: 0x48
+  __TEXT.__swift5_types: 0xa0
+  __TEXT.__swift5_protos: 0x28
+  __TEXT.__oslogstring: 0x3c48
+  __TEXT.__gcc_except_tab: 0x1a98
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2ca8
-  __TEXT.__eh_frame: 0x2b20
-  __TEXT.__objc_classname: 0xfae
-  __TEXT.__objc_methname: 0xb8cf
-  __TEXT.__objc_methtype: 0x2478
-  __TEXT.__objc_stubs: 0x86c0
-  __DATA_CONST.__got: 0x700
-  __DATA_CONST.__const: 0x7f8
+  __TEXT.__unwind_info: 0x2de0
+  __TEXT.__eh_frame: 0x2fe8
+  __TEXT.__objc_classname: 0xfd3
+  __TEXT.__objc_methname: 0xb9ea
+  __TEXT.__objc_methtype: 0x24de
+  __TEXT.__objc_stubs: 0x8780
+  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__const: 0x838
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ca0
+  __DATA_CONST.__objc_selrefs: 0x2df0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x378
-  __AUTH_CONST.__auth_got: 0xcf8
-  __AUTH_CONST.__const: 0x29e8
-  __AUTH_CONST.__cfstring: 0x49a0
-  __AUTH_CONST.__objc_const: 0xe7a8
+  __AUTH_CONST.__auth_got: 0xd98
+  __AUTH_CONST.__const: 0x2d80
+  __AUTH_CONST.__cfstring: 0x4980
+  __AUTH_CONST.__objc_const: 0xd7a8
   __AUTH.__objc_data: 0x19f0
-  __AUTH.__data: 0x220
+  __AUTH.__data: 0x248
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x184
-  __DATA.__data: 0x2438
-  __DATA.__bss: 0x918
+  __DATA.__data: 0x2618
+  __DATA.__bss: 0x928
   __DATA_DIRTY.__objc_ivar: 0x550
   __DATA_DIRTY.__objc_data: 0xff0
   __DATA_DIRTY.__bss: 0x2a0

   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/Versions/A/CollectionsInternal
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
-  - /System/Library/PrivateFrameworks/RTCReporting.framework/Versions/A/RTCReporting
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: BC14EC7E-6332-3D88-A4D2-74BDF310E71E
-  Functions: 3348
-  Symbols:   6351
+  UUID: C2B53974-A3D5-3508-823F-AA1B5B012223
+  Functions: 3438
+  Symbols:   6453
   CStrings:  4367
 
Symbols:
+ +[HMFVersion versionFromOperatingSystemVersion:]
+ +[HMFVersion versionRegex]
+ -[HMFMessage(SendableFixup) sendableResponseHandlerInternal]
+ -[HMFMessage(SendableFixup) setSendableResponseHandlerInternal:]
+ -[HMFMessageDispatcher __registerHandler:]
+ -[HMFMessageDispatcher messageRegistrationForReceiver:name:policies:selector:]
+ -[HMFSoftwareVersion initWithString:]
+ -[HMFVersion initWithOperatingSystemVersion:]
+ -[HMFVersion initWithString:]
+ -[HMFVersion operatingSystemVersion]
+ -[__HMFMessageHandler shouldDeregisterIfMatchingReceiver:]
+ _CFDataGetLength
+ _CFDateGetTypeID
+ _CFNumberGetByteSize
+ _CFStringGetBytes
+ _CFStringGetLength
+ _HMFApproximateSizeOfPlistValue
+ _HMFProductInfoConstellationDOSVersion
+ _HMFProductInfoConstellationEOSVersion
+ _HMFProductInfoCrystalDOSVersion
+ _HMFProductInfoCrystalEOSVersion
+ _HMFProductInfoGlowDOSVersion
+ _HMFProductInfoGlowEOSVersion
+ _HMFProductInfoMoonstoneDOSVersion
+ _HMFProductInfoMoonstoneEOSVersion
+ _HMFProductInfoSapphireDOSVersion
+ _HMFProductInfoSapphireEOSVersion
+ __103-[HMFMessageDispatcher(Deprecated) sendMessage:target:responseQueue:responseHandler:completionHandler:]_block_invoke.180
+ __103-[HMFMessageDispatcher(Deprecated) sendMessage:target:responseQueue:responseHandler:completionHandler:]_block_invoke_2.181
+ __Block_copy
+ __Block_release
+ __IVARS__TtCO12HMFoundation3HMF14SleepTaskTimer
+ __OBJC_$_CLASS_METHODS_HMFMessage(HMFFuture|Deprecated|MessagePayload|SendableFixup)
+ __OBJC_$_INSTANCE_METHODS_HMFMessage(HMFFuture|Deprecated|MessagePayload|SendableFixup)
+ __OBJC_$_PROP_LIST_HMFMessageRegistration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMFMessageRegistration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMFMessageRegistration
+ __OBJC_$_PROTOCOL_REFS_HMFMessageRegistration
+ __OBJC_LABEL_PROTOCOL_$_HMFMessageRegistration
+ __OBJC_PROTOCOL_$_HMFMessageRegistration
+ ___26+[HMFVersion versionRegex]_block_invoke
+ ___block_descriptor_40_e8_32s_e41_B32?0"<HMFMessageRegistration>"8Q16^B24l
+ ___block_descriptor_48_e8_32s40s_e41_B32?0"<HMFMessageRegistration>"8Q16^B24l
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_instantiateGenericMetadata
+ ___swift_project_boxed_opaque_existential_0
+ __block_literal_global.138
+ __block_literal_global.27
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_HMFoundation
+ __validatePayloadObject_block_invoke.300
+ __validatePayloadObject_block_invoke.314
+ _associated conformance 12HMFoundation3HMFO22SleepTaskTimerProviderVAC0eF0AA0E4TypeAcFP_AC0E0
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _generic environment 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_s23CustomStringConvertible0B9LabelTypeRpzr1_l
+ _malloc
+ _objc_msgSend$__registerHandler:
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithOperatingSystemVersion:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$messageRegistrationForReceiver:name:policies:selector:
+ _objc_msgSend$shouldDeregisterIfMatchingReceiver:
+ _swift_deallocClassInstance
+ _swift_dynamicCast
+ _swift_getAtKeyPath
+ _swift_getKeyPath
+ _swift_getMetatypeMetadata
+ _symbolic $s12HMFoundation3HMFO13TimerProviderP
+ _symbolic $s12HMFoundation3HMFO17MockableSleepTaskP
+ _symbolic $s12HMFoundation3HMFO5TimerP
+ _symbolic 9TimerType_____Qz 12HMFoundation3HMFO13TimerProviderP
+ _symbolic SDySSypG
+ _symbolic SaySDySSypGG
+ _symbolic ScTyyt_____G s5NeverO
+ _symbolic So7NSErrorCSgSo12NSDictionaryCSgIeyBhyy_
+ _symbolic _____ 12HMFoundation17UncheckedSendableV
+ _symbolic _____ 12HMFoundation3HMFO14SleepTaskTimerC
+ _symbolic _____ 12HMFoundation3HMFO16DefaultSleepTaskV
+ _symbolic _____ 12HMFoundation3HMFO22SleepTaskTimerProviderV
+ _symbolic _____ s8DurationV
+ _symbolic ______pSgSDySSypGSgIeghgg_ s5ErrorP
+ _symbolic ______pSgSDySSypGSgytIeghnnr_ s5ErrorP
+ _symbolic _____y______G 12HMFoundation3HMFO14SleepTaskTimerC AC07DefaultcD0V
+ _symbolic qd0__
+ _symbolic qd__IeghHg_
+ _symbolic yp
+ _symbolic ytIeAgHr_
+ block_copy_helper.1
+ block_copy_helper.14
+ block_copy_helper.4
+ block_descriptor.16
+ block_descriptor.3
+ block_descriptor.6
+ block_destroy_helper.15
+ block_destroy_helper.2
+ block_destroy_helper.5
+ get_witness_table 12HMFoundation3HMFO13TimerProviderRzScARd__r__lxAcDHD1_0C4TypeQzAC0C0HA0_.2
+ get_witness_table 12HMFoundation3HMFO13TimerProviderRzlxAcDHD1_0C4TypeQzAC0C0HA0_.1
- +[HMFSoftwareVersion versionFromOperatingSystemVersion:]
- +[HMFSoftwareVersion versionRegex]
- -[HMFSoftwareVersion initWithVersionString:]
- -[HMFSoftwareVersion operatingSystemVersion]
- _NSOperatingSystemVersionToString
- __103-[HMFMessageDispatcher(Deprecated) sendMessage:target:responseQueue:responseHandler:completionHandler:]_block_invoke.178
- __103-[HMFMessageDispatcher(Deprecated) sendMessage:target:responseQueue:responseHandler:completionHandler:]_block_invoke_2.179
- __OBJC_$_CLASS_METHODS_HMFMessage(HMFFuture|Deprecated|MessagePayload)
- __OBJC_$_INSTANCE_METHODS_HMFMessage(HMFFuture|Deprecated|MessagePayload)
- ___block_descriptor_40_e8_32s_e36_B32?0"__HMFMessageHandler"8Q16^B24l
- ___block_descriptor_48_e8_32s40s_e36_B32?0"__HMFMessageHandler"8Q16^B24l
- __block_literal_global.130
- __validatePayloadObject_block_invoke.297
- __validatePayloadObject_block_invoke.311
- _objc_msgSend$versionFromOperatingSystemVersion:
- _swift_arrayDestroy
CStrings:
+ "@\"<HMFMessageReceiver>\"16@0:8"
+ "@\"NSUUID\"16@0:8"
+ "B24@0:8@\"<HMFMessageReceiver>\"16"
+ "B24@0:8@\"HMFMessage\"16"
+ "B32@?0@\"<HMFMessageRegistration>\"8Q16^B24"
+ "Failed to compile HMFSoftwareVersion regex pattern '%@': %@"
+ "HMFMessageRegistration"
+ "SendableFixup"
+ "T@\"<HMFMessageReceiver>\",R,W"
+ "T{?=qqq},R"
+ "^(\\d+)(\\.(\\d+))?(\\.(\\d+))?((;(.*))|(\\s*\\((.*)\\))|(\\.(.*)))?"
+ "__registerHandler:"
+ "arrayWithObject:"
+ "initWithOperatingSystemVersion:"
+ "initWithString:"
+ "messageRegistrationForReceiver:name:policies:selector:"
+ "sendableResponseHandlerInternal"
+ "setSendableResponseHandlerInternal:"
+ "shouldDeregisterIfMatchingReceiver:"
+ "sleepTask"
- "%ld.%ld.%ld"
- "%{public}@Failed to create version string regex with error: %@"
- "%{public}@HMFSoftwareVersion: Failed to create version string regex with error: %@"
- "B32@?0@\"__HMFMessageHandler\"8Q16^B24"
- "HMFoundation/HierarchicalStateMachine.swift"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "^(\\d+)(\\.(\\d+))?(\\.(\\d+))?((;(.*))|(\\s*\\((.*)\\))|(\\.(.*)))?.*$"
- "^(\\d+)(\\.(\\d+))?(\\.(\\d+))?.*$"
- "invalid Collection: less than 'count' elements in collection"

```
