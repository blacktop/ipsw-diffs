## HearingMLHelper

> `/System/Library/PrivateFrameworks/HearingMLHelper.framework/HearingMLHelper`

```diff

-496.22.0.0.0
-  __TEXT.__text: 0x2f28
-  __TEXT.__auth_stubs: 0x4f0
+527.0.0.0.0
+  __TEXT.__text: 0x2eac
   __TEXT.__objc_methlist: 0x1bc
-  __TEXT.__const: 0x62
-  __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__cstring: 0xfe
-  __TEXT.__oslogstring: 0x1ac
+  __TEXT.__const: 0x68
   __TEXT.__swift5_typeref: 0x15
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__cstring: 0xfc
+  __TEXT.__oslogstring: 0x1a5
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__unwind_info: 0x100
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methname: 0x401
-  __TEXT.__objc_methtype: 0x185
-  __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x148
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x288
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x48
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x328
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x170

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DCED79F1-0F29-3E10-A49A-36E10F4672CA
-  Functions: 45
-  Symbols:   232
-  CStrings:  97
+  UUID: 64DE1692-6C94-385B-AA1D-02DDD9AC19D7
+  Functions: 39
+  Symbols:   218
+  CStrings:  16
 
Symbols:
+ GCC_except_table5
+ GCC_except_table8
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x5
+ _objc_retain_x8
+ _swift_release_x19
- GCC_except_table4
- GCC_except_table7
- _HearingMLHelperServiceInterface.cold.1
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- ___39-[HearingMLHelperService _serviceProxy]_block_invoke.cold.1
- ___39-[HearingMLHelperService xpcConnection]_block_invoke.47.cold.1
- ___stack_chk_fail
- ___stack_chk_guard
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_HearingMLHelper
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- __swift_FORCE_LOAD_$_swiftVideoToolbox_$_HearingMLHelper
- _objc_release_x22
- _objc_retain_x22
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HearingMLHelperServiceDelegate>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24@32^@40"
- "AXSDKShotModelCreationManager"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "HearingMLHelper"
- "HearingMLHelperClientInterface"
- "HearingMLHelperService"
- "HearingMLHelperServiceInterfaceProtocol"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<HearingMLHelperServiceDelegate>\",W,N,V_delegate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_delegate"
- "_destroyXPCConnection"
- "_serviceProxy"
- "_xpcConnection"
- "_xpcConnectionQueue"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "hash"
- "hearingMLHelperService:eventOccurred:"
- "init"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "setWithObjects:"
- "setXpcConnection:"
- "superclass"
- "trainWithDetectorID:hallucinatorPath:pretrainedWeightsPath:error:"
- "trainWithDetectorID:hallucinatorPath:pretrainedWeightsPath:resultHandler:"
- "v16@0:8"
- "v24@0:8@16"
- "v48@0:8@\"NSString\"16@\"NSURL\"24@\"NSURL\"32@?<v@?@\"NSURL\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "xpcConnection"
- "zone"

```
