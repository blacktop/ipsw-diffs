## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-515.29.0.0.0
-  __TEXT.__text: 0x69568
+515.34.1.0.0
+  __TEXT.__text: 0x6945c
   __TEXT.__auth_stubs: 0xc60
   __TEXT.__objc_methlist: 0x8a88
   __TEXT.__const: 0x562

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x1f60
+  __TEXT.__unwind_info: 0x1f50
   __TEXT.__objc_classname: 0x128b
-  __TEXT.__objc_methname: 0x1232b
-  __TEXT.__objc_methtype: 0x2d7b
+  __TEXT.__objc_methname: 0x1234b
+  __TEXT.__objc_methtype: 0x2d8b
   __TEXT.__objc_stubs: 0xb240
   __DATA_CONST.__got: 0x7f8
-  __DATA_CONST.__const: 0x1dd8
+  __DATA_CONST.__const: 0x1db8
   __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cc8
+  __DATA_CONST.__objc_selrefs: 0x3cb8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x2f0
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0xac8
   __AUTH_CONST.__cfstring: 0x4be0
-  __AUTH_CONST.__objc_const: 0x1ee00
+  __AUTH_CONST.__objc_const: 0x1ee58
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x1d30

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0F633FDE-4AFF-3C9B-823B-6068DDCC784F
-  Functions: 3050
-  Symbols:   11346
-  CStrings:  5087
+  UUID: 5ECA58C4-5E4A-3F32-B899-D03A44305850
+  Functions: 3048
+  Symbols:   11342
+  CStrings:  5086
 
Symbols:
+ -[CPNavXPCProxy activeNavigationIdentifiersChangedTo:]
+ -[CPNavXPCProxy didUpdateActiveComponents:]
+ -[CPNavXPCProxy navigationOwnershipChangedTo:]
+ __OBJC_CLASS_PROTOCOLS_$_CPNavXPCProxy
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.471.cold.1
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.472
+ ___62-[CPInterfaceController clientPushNowPlayingTemplateAnimated:]_block_invoke.487
+ ___block_descriptor_58_e8_32s40s48s_e40_v16?0"<CPNavigationSessionProviding>"8ls32l8s40l8s48l8
+ ___block_literal_global.478
+ ___block_literal_global.489
+ ___block_literal_global.494
+ ___block_literal_global.50
+ ___block_literal_global.502
+ ___block_literal_global.507
+ ___block_literal_global.632
+ ___block_literal_global.635
+ ___block_literal_global.637
+ ___block_literal_global.639
+ ___block_literal_global.641
+ ___block_literal_global.643
+ ___block_literal_global.645
+ ___block_literal_global.647
+ ___block_literal_global.649
+ ___block_literal_global.651
+ ___block_literal_global.653
+ ___block_literal_global.655
+ ___block_literal_global.657
+ ___block_literal_global.659
+ _objc_msgSend$didUpdateActiveComponents:
+ _objc_msgSend$hostStartNavigationSessionForTrip:sendsNavigationMetadata:supportsRouteSharing:reply:
+ _objc_msgSend$updateNavigationOwnerWithIdentifier:accNavRole:
- -[CPNavXPCProxy forwardInvocation:]
- -[CPNavXPCProxy methodSignatureForSelector:]
- -[CPNavXPCProxy respondsToSelector:]
- ___47-[CPNavigationSession setSupportsRouteSharing:]_block_invoke
- ___50-[CPNavigationSession setSendsNavigationMetadata:]_block_invoke
- ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.470
- ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.470.cold.1
- ___62-[CPInterfaceController clientPushNowPlayingTemplateAnimated:]_block_invoke.486
- ___block_descriptor_33_e39_v16?0"<CPNavigationSessionManaging>"8l
- ___block_descriptor_56_e8_32s40s48s_e40_v16?0"<CPNavigationSessionProviding>"8ls32l8s40l8s48l8
- ___block_literal_global.477
- ___block_literal_global.488
- ___block_literal_global.493
- ___block_literal_global.501
- ___block_literal_global.506
- ___block_literal_global.631
- ___block_literal_global.634
- ___block_literal_global.636
- ___block_literal_global.638
- ___block_literal_global.640
- ___block_literal_global.642
- ___block_literal_global.644
- ___block_literal_global.646
- ___block_literal_global.648
- ___block_literal_global.650
- ___block_literal_global.652
- ___block_literal_global.654
- ___block_literal_global.656
- ___block_literal_global.658
- _objc_msgSend$hostStartNavigationSessionForTrip:reply:
- _objc_msgSend$invokeWithTarget:
- _objc_msgSend$methodSignatureForSelector:
CStrings:
+ "hostStartNavigationSessionForTrip:sendsNavigationMetadata:supportsRouteSharing:reply:"
+ "updateNavigationOwnerWithIdentifier:accNavRole:"
+ "v40@0:8@\"CPTrip\"16B24B28@?<v@?@\"<CPNavigationSessionManaging>\">32"
+ "v40@0:8@16B24B28@?32"
- "forwardInvocation:"
- "hostStartNavigationSessionForTrip:reply:"
- "invokeWithTarget:"
- "methodSignatureForSelector:"
- "v32@0:8@\"CPTrip\"16@?<v@?@\"<CPNavigationSessionManaging>\">24"

```
