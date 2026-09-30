## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-9126.2.2.0.0
-  __TEXT.__text: 0xd6508
+9126.2.3.1.103
+  __TEXT.__text: 0xd7530
   __TEXT.__auth_stubs: 0x2bc0
-  __TEXT.__objc_methlist: 0xc234
+  __TEXT.__objc_methlist: 0xc28c
   __TEXT.__const: 0x2170
   __TEXT.__dlopen_cstrs: 0x1c4
-  __TEXT.__cstring: 0xa162
+  __TEXT.__cstring: 0xa1ac
   __TEXT.__swift5_typeref: 0xe7a
-  __TEXT.__oslogstring: 0x2b73
+  __TEXT.__oslogstring: 0x2cc0
   __TEXT.__swift5_capture: 0x2a8
   __TEXT.__constg_swiftt: 0xb44
   __TEXT.__swift5_reflstr: 0x468

   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x2dd0
+  __TEXT.__unwind_info: 0x2de8
   __TEXT.__eh_frame: 0xc6c
-  __TEXT.__objc_classname: 0x155a
-  __TEXT.__objc_methname: 0x23131
-  __TEXT.__objc_methtype: 0x4edc
-  __TEXT.__objc_stubs: 0x1b680
+  __TEXT.__objc_classname: 0x1586
+  __TEXT.__objc_methname: 0x2323c
+  __TEXT.__objc_methtype: 0x4f4e
+  __TEXT.__objc_stubs: 0x1b700
   __DATA_CONST.__got: 0x1178
-  __DATA_CONST.__const: 0x7200
+  __DATA_CONST.__const: 0x72a0
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x168
+  __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x84a8
+  __DATA_CONST.__objc_selrefs: 0x84d0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x568
   __AUTH_CONST.__auth_got: 0x15e8
   __AUTH_CONST.__const: 0x1608
   __AUTH_CONST.__cfstring: 0xb5e0
-  __AUTH_CONST.__objc_const: 0x13328
+  __AUTH_CONST.__objc_const: 0x133a8
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x170

   __AUTH_CONST.__objc_floatobj: 0xe0
   __AUTH.__objc_data: 0x2110
   __AUTH.__data: 0x5d0
-  __DATA.__objc_ivar: 0xe74
-  __DATA.__data: 0x18d0
+  __DATA.__objc_ivar: 0xe7c
+  __DATA.__data: 0x1930
   __DATA.__bss: 0x1638
   __DATA.__common: 0x168
   __DATA_DIRTY.__objc_data: 0x19f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3F1438F3-9C27-3454-BC56-A97B7973B386
-  Functions: 4811
-  Symbols:   16016
-  CStrings:  10025
+  UUID: 456CB13B-FDCE-30FE-8C23-D065E8188527
+  Functions: 4822
+  Symbols:   16053
+  CStrings:  10045
 
Symbols:
+ -[TUIKeyboardTrackingCoordinator resizingDelegate]
+ -[TUIKeyboardTrackingCoordinator setResizingDelegate:]
+ -[TUIKeyboardTrackingProvider trackingWindowDidResizeForScene:requestingUpdatedFrame:]
+ -[TUIKeyplaneView dismissingPopover]
+ -[TUIKeyplaneView setDismissingPopover:]
+ _OBJC_IVAR_$_TUIKeyboardTrackingCoordinator._resizingDelegate
+ _OBJC_IVAR_$_TUIKeyplaneView._dismissingPopover
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUIKeyboardTrackingWindowResizingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUIKeyboardTrackingWindowResizingDelegate
+ __OBJC_CLASS_PROTOCOLS_$_TUIKeyboardTrackingProvider
+ __OBJC_LABEL_PROTOCOL_$_TUIKeyboardTrackingWindowResizingDelegate
+ __OBJC_PROTOCOL_$_TUIKeyboardTrackingWindowResizingDelegate
+ __TUIKeyboardTrackingLogger.8543
+ __TUIKeyboardTrackingLogger.log.8549
+ __TUIKeyboardTrackingLogger.onceToken.8547
+ ___52-[TUIKeyboardTrackingCoordinator addTrackingWindow:]_block_invoke.11
+ ___52-[TUIKeyboardTrackingCoordinator addTrackingWindow:]_block_invoke_2
+ ___68-[TUIKeyboardTrackingCoordinator sendUpdateCompleteWithExistingInfo]_block_invoke
+ ___68-[TUIKeyboardTrackingCoordinator sendUpdateCompleteWithExistingInfo]_block_invoke.35
+ ___68-[TUIKeyboardTrackingCoordinator sendUpdateCompleteWithExistingInfo]_block_invoke_2
+ ___68-[TUIKeyboardTrackingCoordinator sendUpdateCompleteWithExistingInfo]_block_invoke_3
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke.20
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke.26
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke.29
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke.31
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke.32
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke_2.24
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke_2.30
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke_2.33
+ ___Block_byref_object_copy_.12776
+ ___Block_byref_object_copy_.5497
+ ___Block_byref_object_copy_.5867
+ ___Block_byref_object_copy_.8285
+ ___Block_byref_object_copy_.9878
+ ___Block_byref_object_dispose_.12777
+ ___Block_byref_object_dispose_.5498
+ ___Block_byref_object_dispose_.5868
+ ___Block_byref_object_dispose_.8286
+ ___Block_byref_object_dispose_.9879
+ ____TUIKeyboardTrackingLogger_block_invoke.8552
+ ___block_descriptor_112_8_32s40s_e18_v16?0"UIWindow"8ls32l8s40l8
+ ___block_descriptor_112_8_32s40s_e30_v16?0"<TUIKeyboardTracker>"8ls32l8s40l8
+ ___block_descriptor_40_8_32s_e39_v40?0{CGRect={CGPoint=dd}{CGSize=dd}}8ls32l8
+ ___block_descriptor_48_8_32s40s_e36_v44?0{CGSize=dd}8{UIOffset=dd}24B40ls32l8s40l8
+ ___block_descriptor_48_8_32s40s_e39_v40?0{CGRect={CGPoint=dd}{CGSize=dd}}8ls32l8s40l8
+ ___block_descriptor_72_8_32s_e36_v44?0{CGSize=dd}8{UIOffset=dd}24B40ls32l8
+ ___block_literal_global.10.10830
+ ___block_literal_global.10515
+ ___block_literal_global.10835
+ ___block_literal_global.11020
+ ___block_literal_global.11354
+ ___block_literal_global.11509
+ ___block_literal_global.11782
+ ___block_literal_global.12786
+ ___block_literal_global.13027
+ ___block_literal_global.13486
+ ___block_literal_global.18.8340
+ ___block_literal_global.20.9439
+ ___block_literal_global.20.9977
+ ___block_literal_global.22.9441
+ ___block_literal_global.240
+ ___block_literal_global.4.13050
+ ___block_literal_global.5322
+ ___block_literal_global.5530
+ ___block_literal_global.5986
+ ___block_literal_global.6.11022
+ ___block_literal_global.61.13025
+ ___block_literal_global.6676
+ ___block_literal_global.6797
+ ___block_literal_global.7061
+ ___block_literal_global.7329
+ ___block_literal_global.748
+ ___block_literal_global.752
+ ___block_literal_global.7726
+ ___block_literal_global.7896
+ ___block_literal_global.8344
+ ___block_literal_global.8548
+ ___block_literal_global.8751
+ ___block_literal_global.9170
+ ___block_literal_global.9352
+ ___block_literal_global.9432
+ ___block_literal_global.9514
+ ___block_literal_global.9887
+ ___block_literal_global.9980
+ _objc_msgSend$dismissingPopover
+ _objc_msgSend$resizingDelegate
+ _objc_msgSend$setDismissingPopover:
+ _objc_msgSend$setResizingDelegate:
+ _objc_msgSend$trackingWindowDidResizeForScene:requestingUpdatedFrame:
+ _sharedInstance.__instance.10831
+ _sharedInstance.onceToken.10829
+ _sharedInstance.onceToken.6796
+ _sharedInstance.onceToken.9976
+ _shouldGenerateCandidateForContext:.onceToken.9893
- __TUIKeyboardTrackingLogger.8534
- __TUIKeyboardTrackingLogger.log.8539
- __TUIKeyboardTrackingLogger.onceToken.8537
- ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke.22
- ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke.25
- ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke.27
- ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke.28
- ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke_2.26
- ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke_2.29
- ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke_3
- ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke_4
- ___Block_byref_object_copy_.12764
- ___Block_byref_object_copy_.5499
- ___Block_byref_object_copy_.5869
- ___Block_byref_object_copy_.8280
- ___Block_byref_object_copy_.9867
- ___Block_byref_object_dispose_.12765
- ___Block_byref_object_dispose_.5500
- ___Block_byref_object_dispose_.5870
- ___Block_byref_object_dispose_.8281
- ___Block_byref_object_dispose_.9868
- ____TUIKeyboardTrackingLogger_block_invoke.8542
- ___block_descriptor_40_8_32s_e33_v40?0{CGSize=dd}8{UIOffset=dd}24ls32l8
- ___block_descriptor_48_8_32s40s_e33_v40?0{CGSize=dd}8{UIOffset=dd}24ls32l8s40l8
- ___block_literal_global.10.10817
- ___block_literal_global.10504
- ___block_literal_global.10822
- ___block_literal_global.11008
- ___block_literal_global.11342
- ___block_literal_global.11497
- ___block_literal_global.11770
- ___block_literal_global.12774
- ___block_literal_global.13015
- ___block_literal_global.13468
- ___block_literal_global.18.8335
- ___block_literal_global.20.9428
- ___block_literal_global.20.9966
- ___block_literal_global.22.9430
- ___block_literal_global.227
- ___block_literal_global.4.13038
- ___block_literal_global.5337
- ___block_literal_global.5532
- ___block_literal_global.5988
- ___block_literal_global.6.11010
- ___block_literal_global.61.13013
- ___block_literal_global.6677
- ___block_literal_global.6798
- ___block_literal_global.7058
- ___block_literal_global.7325
- ___block_literal_global.743
- ___block_literal_global.747
- ___block_literal_global.7721
- ___block_literal_global.7891
- ___block_literal_global.8339
- ___block_literal_global.8538
- ___block_literal_global.8740
- ___block_literal_global.9159
- ___block_literal_global.9341
- ___block_literal_global.9421
- ___block_literal_global.9503
- ___block_literal_global.9876
- ___block_literal_global.9969
- _objc_msgSend$postNotificationsWithInfo:type:start:
- _sharedInstance.__instance.10818
- _sharedInstance.onceToken.10816
- _sharedInstance.onceToken.6797
- _sharedInstance.onceToken.9965
- _shouldGenerateCandidateForContext:.onceToken.9882
CStrings:
+ "@\"<TUIKeyboardTrackingWindowResizingDelegate>\""
+ "T@\"<TUIKeyboardTrackingWindowResizingDelegate>\",W,N,V_resizingDelegate"
+ "TB,N,V_dismissingPopover"
+ "TUIKeyboardTracker: [Resizing] Converted frame to %@ for <%@: %p>"
+ "TUIKeyboardTracker: [Resizing] Intersection is %@ and offset is %@ for <%@: %p>"
+ "TUIKeyboardTrackingWindowResizingDelegate"
+ "Tracking provider update to offscreen down for %@"
+ "Tracking window bounds did change <%@: %p> scene frame %@"
+ "Update size to %@; offset to %@; from %@; for %@"
+ "Updated tracking window via resizing delegate <%@: %p> with existing info %@"
+ "_dismissingPopover"
+ "_resizingDelegate"
+ "dismissingPopover"
+ "resizingDelegate"
+ "setDismissingPopover:"
+ "setResizingDelegate:"
+ "trackingWindowDidResizeForScene:requestingUpdatedFrame:"
+ "v16@?0@\"<TUIKeyboardTracker>\"8"
+ "v32@0:8@\"UIWindowScene\"16@?<v@?{CGRect={CGPoint=dd}{CGSize=dd}}>24"
+ "v40@?0{CGRect={CGPoint=dd}{CGSize=dd}}8"
+ "v44@?0{CGSize=dd}8{UIOffset=dd}24B40"
+ "\x81"
- "Update size to %@; offset to %@ from %@ for %@"
- "v40@?0{CGSize=dd}8{UIOffset=dd}24"

```
