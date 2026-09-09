## AVKit

> `/System/Library/Frameworks/AVKit.framework/AVKit`

```diff

 1360.75.1.3.0
-  __TEXT.__text: 0x268b10
-  __TEXT.__objc_methlist: 0x1ed44
+  __TEXT.__text: 0x269ccc
+  __TEXT.__objc_methlist: 0x1ee14
   __TEXT.__const: 0x8438
   __TEXT.__constg_swiftt: 0x2cbc
   __TEXT.__swift5_typeref: 0x8312

   __TEXT.__swift5_fieldmd: 0x1e58
   __TEXT.__swift5_assocty: 0x858
   __TEXT.__swift5_capture: 0x18d8
-  __TEXT.__cstring: 0x1329a
+  __TEXT.__cstring: 0x13322
   __TEXT.__swift5_proto: 0x2cc
   __TEXT.__swift5_types: 0x24c
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift_as_entry: 0x2e8
   __TEXT.__swift_as_ret: 0x444
   __TEXT.__swift_as_cont: 0x86c
-  __TEXT.__oslogstring: 0xc11d
+  __TEXT.__oslogstring: 0xc15b
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__gcc_except_tab: 0x426c
   __TEXT.__dlopen_cstrs: 0x1ef
   __TEXT.__ustring: 0x10c
-  __TEXT.__unwind_info: 0xa368
+  __TEXT.__unwind_info: 0xa3a0
   __TEXT.__eh_frame: 0x7a5c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x33b0
-  __DATA_CONST.__objc_classlist: 0xae8
+  __DATA_CONST.__objc_classlist: 0xaf8
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd430
+  __DATA_CONST.__objc_selrefs: 0xd488
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x7f8
+  __DATA_CONST.__objc_superrefs: 0x808
   __DATA_CONST.__objc_arraydata: 0x6c0
-  __DATA_CONST.__got: 0x1848
+  __DATA_CONST.__got: 0x18a8
   __AUTH_CONST.__const: 0x88f8
-  __AUTH_CONST.__cfstring: 0x99a0
-  __AUTH_CONST.__objc_const: 0x382a0
+  __AUTH_CONST.__cfstring: 0x9a00
+  __AUTH_CONST.__objc_const: 0x38578
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_doubleobj: 0x280
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x1fa0
-  __AUTH.__objc_data: 0x6838
+  __AUTH_CONST.__auth_got: 0x1fa8
+  __AUTH.__objc_data: 0x68d8
   __AUTH.__data: 0x2148
-  __DATA.__objc_ivar: 0x3024
+  __DATA.__objc_ivar: 0x3054
   __DATA.__data: 0x5cb8
   __DATA.__common: 0x1c8
   __DATA_DIRTY.__objc_data: 0x12e0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14854
-  Symbols:   25650
-  CStrings:  2999
+  Functions: 14871
+  Symbols:   25715
+  CStrings:  3004
 
Symbols:
+ +[AVCaptureDeviceStates stateWithStateADeviceIDs:stateBDeviceIDs:]
+ -[AVCaptureDeviceStateCoordinator .cxx_destruct]
+ -[AVCaptureDeviceStateCoordinator _updateCurrentState:]
+ -[AVCaptureDeviceStateCoordinator dealloc]
+ -[AVCaptureDeviceStateCoordinator deviceState]
+ -[AVCaptureDeviceStateCoordinator initWithView:types:queue:handler:]
+ -[AVCaptureDeviceStateCoordinator observeValueForKeyPath:ofObject:change:context:]
+ -[AVCaptureDeviceStates .cxx_destruct]
+ -[AVCaptureDeviceStates _initWithStateADeviceIDs:stateBDeviceIDs:]
+ -[AVCaptureDeviceStates debugDescription]
+ -[AVCaptureDeviceStates description]
+ -[AVCaptureDeviceStates hash]
+ -[AVCaptureDeviceStates isEqual:]
+ -[AVCaptureDeviceStates stateADeviceIDs]
+ -[AVCaptureDeviceStates stateBDeviceIDs]
+ GCC_except_table10122
+ GCC_except_table10124
+ GCC_except_table10138
+ GCC_except_table10172
+ GCC_except_table10182
+ GCC_except_table10332
+ GCC_except_table10338
+ GCC_except_table10379
+ GCC_except_table10401
+ GCC_except_table10617
+ GCC_except_table10639
+ GCC_except_table8376
+ GCC_except_table8406
+ GCC_except_table8410
+ GCC_except_table8565
+ GCC_except_table8623
+ GCC_except_table8625
+ GCC_except_table8809
+ GCC_except_table8822
+ GCC_except_table8843
+ GCC_except_table8866
+ GCC_except_table8876
+ GCC_except_table8894
+ GCC_except_table8895
+ GCC_except_table8899
+ GCC_except_table8907
+ GCC_except_table8963
+ GCC_except_table9259
+ GCC_except_table9277
+ GCC_except_table9430
+ GCC_except_table9434
+ GCC_except_table9436
+ GCC_except_table9438
+ GCC_except_table9439
+ GCC_except_table9440
+ GCC_except_table9471
+ GCC_except_table9479
+ GCC_except_table9509
+ GCC_except_table9535
+ GCC_except_table9553
+ GCC_except_table9557
+ GCC_except_table9561
+ GCC_except_table9563
+ GCC_except_table9635
+ GCC_except_table9658
+ GCC_except_table9698
+ GCC_except_table9703
+ GCC_except_table9719
+ GCC_except_table9822
+ GCC_except_table9987
+ _AVCaptureDeviceStateCoordinatorChangedContext
+ _AVCaptureDeviceTypeBuiltInBostonUltraWideCamera
+ _AVCaptureDeviceTypeBuiltInDualCamera
+ _AVCaptureDeviceTypeBuiltInDualWideCamera
+ _AVCaptureDeviceTypeBuiltInLiDARDepthCamera
+ _AVCaptureDeviceTypeBuiltInRenoUltraWideCamera
+ _AVCaptureDeviceTypeBuiltInTelephotoCamera
+ _AVCaptureDeviceTypeBuiltInTripleCamera
+ _AVCaptureDeviceTypeBuiltInTrueDepthCamera
+ _AVCaptureDeviceTypeBuiltInUltraWideCamera
+ _AVCaptureDeviceTypeBuiltInWideAngleCamera
+ _OBJC_CLASS_$_AVCaptureDeviceDiscoverySession
+ _OBJC_CLASS_$_AVCaptureDeviceStateCoordinator
+ _OBJC_CLASS_$_AVCaptureDeviceStates
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._bostonDevices
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._currentState
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._handler
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._isRenoSuspended
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._lock
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._otherDevices
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._queue
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._renoCamera
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._renoDevices
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinator._types
+ _OBJC_IVAR_$_AVCaptureDeviceStates._stateADeviceIDs
+ _OBJC_IVAR_$_AVCaptureDeviceStates._stateBDeviceIDs
+ _OBJC_METACLASS_$_AVCaptureDeviceStateCoordinator
+ _OBJC_METACLASS_$_AVCaptureDeviceStates
+ __OBJC_$_CLASS_METHODS_AVCaptureDeviceStates
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDeviceStateCoordinator
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDeviceStates
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureDeviceStateCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureDeviceStates
+ __OBJC_$_PROP_LIST_AVCaptureDeviceStates
+ __OBJC_CLASS_RO_$_AVCaptureDeviceStateCoordinator
+ __OBJC_CLASS_RO_$_AVCaptureDeviceStates
+ __OBJC_METACLASS_RO_$_AVCaptureDeviceStateCoordinator
+ __OBJC_METACLASS_RO_$_AVCaptureDeviceStates
+ ___68-[AVCaptureDeviceStateCoordinator initWithView:types:queue:handler:]_block_invoke
+ ___82-[AVCaptureDeviceStateCoordinator observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ _dispatch_assert_queue$V2
+ _objc_msgSend$_initWithStateADeviceIDs:stateBDeviceIDs:
+ _objc_msgSend$_updateCurrentState:
+ _objc_msgSend$devices
+ _objc_msgSend$discoverySessionWithDeviceTypes:mediaType:position:
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$stateADeviceIDs
+ _objc_msgSend$stateBDeviceIDs
+ _objc_msgSend$stateWithStateADeviceIDs:stateBDeviceIDs:
+ _objc_msgSend$uniqueID
- GCC_except_table10105
- GCC_except_table10107
- GCC_except_table10121
- GCC_except_table10155
- GCC_except_table10165
- GCC_except_table10315
- GCC_except_table10321
- GCC_except_table10362
- GCC_except_table10384
- GCC_except_table10600
- GCC_except_table10622
- GCC_except_table8359
- GCC_except_table8389
- GCC_except_table8393
- GCC_except_table8548
- GCC_except_table8606
- GCC_except_table8608
- GCC_except_table8792
- GCC_except_table8805
- GCC_except_table8826
- GCC_except_table8849
- GCC_except_table8859
- GCC_except_table8877
- GCC_except_table8878
- GCC_except_table8882
- GCC_except_table8890
- GCC_except_table8946
- GCC_except_table9242
- GCC_except_table9260
- GCC_except_table9413
- GCC_except_table9417
- GCC_except_table9419
- GCC_except_table9421
- GCC_except_table9422
- GCC_except_table9423
- GCC_except_table9454
- GCC_except_table9462
- GCC_except_table9492
- GCC_except_table9518
- GCC_except_table9536
- GCC_except_table9540
- GCC_except_table9544
- GCC_except_table9546
- GCC_except_table9618
- GCC_except_table9641
- GCC_except_table9669
- GCC_except_table9681
- GCC_except_table9702
- GCC_except_table9805
- GCC_except_table9970
CStrings:
+ "%s Initialized AVCaptureDeviceStateCoordinator for UIView: %@"
+ "-[AVCaptureDeviceStateCoordinator initWithView:types:queue:handler:]"
+ "<%@: %p %@>"
+ "stateADeviceIDs: %@, stateBDeviceIDs: %@"
+ "suspended"
```
