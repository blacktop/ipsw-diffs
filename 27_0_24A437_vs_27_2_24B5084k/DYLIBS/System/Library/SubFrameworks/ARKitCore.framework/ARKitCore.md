## ARKitCore

> `/System/Library/SubFrameworks/ARKitCore.framework/ARKitCore`

```diff

-781.0.7.0.0
-  __TEXT.__text: 0x195028
+781.40.3.0.0
+  __TEXT.__text: 0x195140
   __TEXT.__objc_methlist: 0x1143c
-  __TEXT.__const: 0x25d78
+  __TEXT.__const: 0x25d88
   __TEXT.__cstring: 0x1d99a
-  __TEXT.__gcc_except_tab: 0x13490
-  __TEXT.__oslogstring: 0x20dc6
+  __TEXT.__gcc_except_tab: 0x134bc
+  __TEXT.__oslogstring: 0x20dd9
   __TEXT.__ustring: 0xe6
-  __TEXT.__unwind_info: 0x7958
+  __TEXT.__unwind_info: 0x7960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__got: 0x15f8
   __AUTH_CONST.__const: 0x3e18
   __AUTH_CONST.__cfstring: 0xff40
-  __AUTH_CONST.__objc_const: 0x3d0e0
+  __AUTH_CONST.__objc_const: 0x3d100
   __AUTH_CONST.__weak_auth_got: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x5d0

   __AUTH_CONST.__auth_got: 0x1f10
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x2038
+  __DATA.__objc_ivar: 0x203c
   __DATA.__data: 0x1c90
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  Functions: 8016
-  Symbols:   18060
+  Functions: 8017
+  Symbols:   18061
   CStrings:  4554
 
Symbols:
+ _OBJC_IVAR_$_ARCubemapCompletion._espressoLock
Functions:
+ sub_2be3d87f0
~ ___34+[ARKitUserDefaults defaultValues]_block_invoke : 2264 -> 2280
~ -[ARCubemapCompletion init] : 4156 -> 4160
~ -[ARCubemapCompletion completeLatLongImage:] : 296 -> 376
~ __ZN5arkit10loadParamsE22ARNoiseModelIdentifierRNSt3__16vectorIfNS1_9allocatorIfEEEERNS2_IS5_NS3_IS5_EEEERNS2_IS8_NS3_IS8_EEEESC_S6_ : 24948 -> 25012
~ +[ARNoiseParameters modelIdentifierForDevicePosition:longEdgeImageResolution:] : 2368 -> 2416
~ -[ARViewRotationAngleProvider _deliverPreviewAngle:] : 472 -> 480
CStrings:
+ "%{public}@ <%p>: Delivering viewRotationAngle %f degrees (preview angle %.0f)"
- "%{public}@ <%p>: Delivering view rotation angle %f degrees"
```
