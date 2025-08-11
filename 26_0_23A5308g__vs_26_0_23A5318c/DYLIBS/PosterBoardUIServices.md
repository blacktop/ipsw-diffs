## PosterBoardUIServices

> `/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`

```diff

-289.103.0.0.0
-  __TEXT.__text: 0x8e8b8
+290.105.0.0.0
+  __TEXT.__text: 0x8e750
   __TEXT.__auth_stubs: 0x1f90
-  __TEXT.__objc_methlist: 0x67a8
+  __TEXT.__objc_methlist: 0x66f8
   __TEXT.__const: 0x2528
-  __TEXT.__cstring: 0x53af
-  __TEXT.__gcc_except_tab: 0xe2c
-  __TEXT.__oslogstring: 0x3e8f
+  __TEXT.__cstring: 0x538f
+  __TEXT.__gcc_except_tab: 0xe20
+  __TEXT.__oslogstring: 0x3e9f
   __TEXT.__swift5_typeref: 0x58ef
   __TEXT.__constg_swiftt: 0xbcc
   __TEXT.__swift5_reflstr: 0x903

   __TEXT.__unwind_info: 0x24b8
   __TEXT.__eh_frame: 0x1478
   __TEXT.__objc_classname: 0x1470
-  __TEXT.__objc_methname: 0x13517
-  __TEXT.__objc_methtype: 0x32d2
-  __TEXT.__objc_stubs: 0xb8c0
-  __DATA_CONST.__got: 0xcd8
+  __TEXT.__objc_methname: 0x133b0
+  __TEXT.__objc_methtype: 0x32a7
+  __TEXT.__objc_stubs: 0xb780
+  __DATA_CONST.__got: 0xcd0
   __DATA_CONST.__const: 0x1f38
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c80
+  __DATA_CONST.__objc_selrefs: 0x3c38
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x218
   __AUTH_CONST.__auth_got: 0xfd8
   __AUTH_CONST.__const: 0x16b0
-  __AUTH_CONST.__cfstring: 0x34a0
-  __AUTH_CONST.__objc_const: 0x141a8
+  __AUTH_CONST.__cfstring: 0x3440
+  __AUTH_CONST.__objc_const: 0x14088
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x15f8
   __AUTH.__data: 0x5d0
-  __DATA.__objc_ivar: 0x794
+  __DATA.__objc_ivar: 0x788
   __DATA.__data: 0x27d0
   __DATA.__bss: 0x23e0
   __DATA.__common: 0x98

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2698557F-D0EC-343C-8F09-FC643FC53A25
-  Functions: 3397
-  Symbols:   9316
-  CStrings:  4689
+  UUID: AD30B599-18A2-36E3-83FE-0EF0FACFB884
+  Functions: 3390
+  Symbols:   9289
+  CStrings:  4666
 
Symbols:
+ -[PRUISPosterChannelViewController loadView]
+ -[_PRUISPosterStagedSceneSettings pui_isAdaptiveTimeDisabled]
+ -[_PRUISPosterStagedSceneSettings pui_setAdaptiveTimeDisabled:]
+ GCC_except_table71
+ _OBJC_IVAR_$__PRUISPosterStagedSceneSettings._adaptiveTimeDisabled
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PUIPosterSnapshotDestinationProviding
+ __OBJC_$_PROTOCOL_REFS_PUIPosterSnapshotDestinationProviding
+ ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.128
+ ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.128.cold.1
+ ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.131
+ ___72-[_PRUISPosterSnapshotControllerImpl executeSnapshotRequest:completion:]_block_invoke.118
+ _objc_msgSend$pui_adaptiveTimeMode
+ _objc_msgSend$pui_isAdaptiveTimeDisabled
+ _objc_msgSend$pui_setAdaptiveTimeDisabled:
- -[PRUISPosterChannelViewController viewDidLoad]
- -[_PRUISPosterStagedSceneSettings pr_deviceMotionRotation]
- -[_PRUISPosterStagedSceneSettings pr_devicePitch]
- -[_PRUISPosterStagedSceneSettings pr_deviceRoll]
- -[_PRUISPosterStagedSceneSettings pr_deviceYaw]
- -[_PRUISPosterStagedSceneSettings pr_setDeviceMotionRotation:]
- -[_PRUISPosterStagedSceneSettings pr_setDevicePitch:]
- -[_PRUISPosterStagedSceneSettings pr_setDeviceRoll:]
- -[_PRUISPosterStagedSceneSettings pr_setDeviceYaw:]
- GCC_except_table73
- _OBJC_CLASS_$_PFDeviceMotionUtilities
- _OBJC_IVAR_$__PRUISPosterStagedSceneSettings._deviceMotionRotation
- _OBJC_IVAR_$__PRUISPosterStagedSceneSettings._devicePitch
- _OBJC_IVAR_$__PRUISPosterStagedSceneSettings._deviceRoll
- _OBJC_IVAR_$__PRUISPosterStagedSceneSettings._deviceYaw
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PUIPosterSnapshotDestinationProviding
- ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.129
- ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.129.cold.1
- ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.132
- ___66-[PRUISPosterChannelViewController _teardownPosterViewController:]_block_invoke.116
- ___72-[_PRUISPosterSnapshotControllerImpl executeSnapshotRequest:completion:]_block_invoke.119
- _objc_msgSend$_ui_encodeCGFloat:forKey:
- _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
- _objc_msgSend$mainRunLoop
- _objc_msgSend$pr_deviceMotionRotation
- _objc_msgSend$pr_devicePitch
- _objc_msgSend$pr_deviceRoll
- _objc_msgSend$pr_deviceYaw
- _objc_msgSend$pr_setDeviceMotionRotation:
- _objc_msgSend$pr_setDevicePitch:
- _objc_msgSend$pr_setDeviceRoll:
- _objc_msgSend$pr_setDeviceYaw:
- _objc_msgSend$rotationFromSerializedRepresentation:
- _objc_msgSend$serializedRepresentationFromRotation:
CStrings:
+ "%{public}@ loadView..."
+ "@\"PFTFuture\"32@0:8@\"PFPosterPath\"16@\"BSAuditToken\"24"
+ "TB,N,Gpui_isAdaptiveTimeDisabled,Spui_setAdaptiveTimeDisabled:"
+ "TB,N,Gpui_isAdaptiveTimeDisabled,Spui_setAdaptiveTimeDisabled:,V_adaptiveTimeDisabled"
+ "TB,R,N,Gpui_isAdaptiveTimeDisabled"
+ "_adaptiveTimeDisabled"
+ "loadView"
+ "pui_adaptiveTimeDisabled"
+ "pui_adaptiveTimeMode"
+ "pui_isAdaptiveTimeDisabled"
+ "pui_setAdaptiveTimeDisabled:"
+ "reachableCacheFuture"
+ "snapshotDestinationFutureForPath:clientAuditToken:"
- "(?={?=}{?=})16@0:8"
- "@\"PUIPosterSnapshotDestination\"40@0:8@\"PFPosterPath\"16@\"BSAuditToken\"24o^@32"
- "T(?={?=}{?=}),N,Spr_setDeviceMotionRotation:"
- "T(?={?=}{?=}),N,Spr_setDeviceMotionRotation:,V_deviceMotionRotation"
- "T(?={?=}{?=}),R,N"
- "Td,N,Spr_setDevicePitch:"
- "Td,N,Spr_setDevicePitch:,V_devicePitch"
- "Td,N,Spr_setDeviceRoll:"
- "Td,N,Spr_setDeviceRoll:,V_deviceRoll"
- "Td,N,Spr_setDeviceYaw:"
- "Td,N,Spr_setDeviceYaw:,V_deviceYaw"
- "_deviceMotionRotation"
- "_devicePitch"
- "_deviceRoll"
- "_deviceYaw"
- "_ui_encodeCGFloat:forKey:"
- "checkCacheIsReachableAsync"
- "decodeArrayOfObjectsOfClass:forKey:"
- "mainRunLoop"
- "pr_deviceMotionRotation"
- "pr_devicePitch"
- "pr_deviceRoll"
- "pr_deviceYaw"
- "pr_setDeviceMotionRotation:"
- "pr_setDevicePitch:"
- "pr_setDeviceRoll:"
- "pr_setDeviceYaw:"
- "rotationFromSerializedRepresentation:"
- "serializedRepresentationFromRotation:"
- "snapshotDestinationForPath:clientAuditToken:error:"

```
