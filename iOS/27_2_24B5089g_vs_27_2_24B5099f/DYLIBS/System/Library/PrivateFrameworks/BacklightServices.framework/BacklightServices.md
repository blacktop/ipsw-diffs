## BacklightServices

> `/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`

```diff

-6.1.3.0.0
-  __TEXT.__text: 0x28c20
-  __TEXT.__objc_methlist: 0x38f4
+6.1.4.0.0
+  __TEXT.__text: 0x29364
+  __TEXT.__objc_methlist: 0x39cc
   __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x1b91
   __TEXT.__oslogstring: 0x295e
-  __TEXT.__cstring: 0x1bc7
   __TEXT.__ustring: 0xfe
   __TEXT.__gcc_except_tab: 0xcb4
-  __TEXT.__unwind_info: 0x14d0
+  __TEXT.__unwind_info: 0x1510
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xdd0
-  __DATA_CONST.__objc_classlist: 0x360
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16b8
+  __DATA_CONST.__objc_selrefs: 0x16f0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1c0
-  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__got: 0x410
   __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x2420
-  __AUTH_CONST.__objc_const: 0x8290
+  __AUTH_CONST.__cfstring: 0x2480
+  __AUTH_CONST.__objc_const: 0x8488
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1720
-  __DATA.__objc_ivar: 0x2e4
+  __AUTH.__objc_data: 0x17c0
+  __DATA.__objc_ivar: 0x2f4
   __DATA.__data: 0xc68
   __DATA_DIRTY.__objc_data: 0xaa0
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1352
-  Symbols:   2752
-  CStrings:  531
+  Functions: 1368
+  Symbols:   2789
+  CStrings:  533
 
Symbols:
+ +[BLSBacklightProxyObservation observationForObserver:backlight:]
+ +[BLSPendingBacklightProxy addObservation:toBacklightProxy:]
+ -[BLSBacklightProxyObservation .cxx_destruct]
+ -[BLSBacklightProxyObservation backlightForProxy:]
+ -[BLSBacklightProxyObservation backlight]
+ -[BLSBacklightProxyObservation description]
+ -[BLSBacklightProxyObservation initWithObserver:backlight:]
+ -[BLSBacklightProxyObservation observer]
+ -[BLSPendingBacklightProxy _addObserver:forBacklight:]
+ -[BLSPendingBacklightProxy addObserver:forBacklight:]
+ -[BLSPendingBacklightProxy initForDisplay:]
+ -[BLSXPCBacklightProxy _addObserver:forBacklight:]
+ -[BLSXPCBacklightProxy addObserver:forBacklight:]
+ -[BLSXPCBacklightProxy lock_allDidChangeAlwaysOnEnabledObservations]
+ -[BLSXPCBacklightProxy lock_allDidCompleteUpdateToStateObservations]
+ -[BLSXPCBacklightProxy lock_allObservationsPassingTest:]
+ -[BLSXPCBacklightProxy lock_enumerateObservationsWithBlock:]
+ -[BLSXPCBacklightProxyObservation .cxx_destruct]
+ -[BLSXPCBacklightProxyObservation description]
+ -[BLSXPCBacklightProxyObservation initWithObserver:backlight:]
+ -[BLSXPCBacklightProxyObservation mask]
+ _OBJC_CLASS_$_BLSBacklightProxyObservation
+ _OBJC_CLASS_$_BLSXPCBacklightProxyObservation
+ _OBJC_IVAR_$_BLSBacklightProxyObservation._backlight
+ _OBJC_IVAR_$_BLSBacklightProxyObservation._observer
+ _OBJC_IVAR_$_BLSPendingBacklightProxy._display
+ _OBJC_IVAR_$_BLSPendingBacklightProxy._observations
+ _OBJC_IVAR_$_BLSXPCBacklightProxyObservation._mask
+ _OBJC_METACLASS_$_BLSBacklightProxyObservation
+ _OBJC_METACLASS_$_BLSXPCBacklightProxyObservation
+ __OBJC_$_CLASS_METHODS_BLSBacklightProxyObservation
+ __OBJC_$_INSTANCE_METHODS_BLSBacklightProxyObservation
+ __OBJC_$_INSTANCE_METHODS_BLSXPCBacklightProxyObservation
+ __OBJC_$_INSTANCE_VARIABLES_BLSBacklightProxyObservation
+ __OBJC_$_INSTANCE_VARIABLES_BLSXPCBacklightProxyObservation
+ __OBJC_$_PROP_LIST_BLSBacklightProxyObservation
+ __OBJC_$_PROP_LIST_BLSXPCBacklightProxyObservation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSBacklightProxy
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSBacklightProxy
+ __OBJC_CLASS_RO_$_BLSBacklightProxyObservation
+ __OBJC_CLASS_RO_$_BLSXPCBacklightProxyObservation
+ __OBJC_METACLASS_RO_$_BLSBacklightProxyObservation
+ __OBJC_METACLASS_RO_$_BLSXPCBacklightProxyObservation
+ ___56-[BLSXPCBacklightProxy lock_allObservationsPassingTest:]_block_invoke
+ ___68-[BLSXPCBacklightProxy lock_allDidChangeAlwaysOnEnabledObservations]_block_invoke
+ ___68-[BLSXPCBacklightProxy lock_allDidCompleteUpdateToStateObservations]_block_invoke
+ ___block_descriptor_32_e41_B16?0"BLSXPCBacklightProxyObservation"8l
+ ___block_descriptor_48_e8_32s40bs_e41_v16?0"BLSXPCBacklightProxyObservation"8ls40l8s32l8
+ ___block_descriptor_58_e8_32s40s48s_e41_v16?0"BLSXPCBacklightProxyObservation"8ls32l8s40l8s48l8
- -[BLSPendingBacklightProxy init]
- -[BLSXPCBacklightProxy lock_allDidChangeAlwaysOnEnabledObservers]
- -[BLSXPCBacklightProxy lock_allDidCompleteUpdateToStateObservers]
- -[BLSXPCBacklightProxy lock_allObserversPassingTest:]
- -[BLSXPCBacklightProxy lock_enumerateObserversWithBlock:]
- _OBJC_IVAR_$_BLSPendingBacklightProxy._observers
- ___53-[BLSXPCBacklightProxy lock_allObserversPassingTest:]_block_invoke
- ___65-[BLSXPCBacklightProxy lock_allDidChangeAlwaysOnEnabledObservers]_block_invoke
- ___65-[BLSXPCBacklightProxy lock_allDidCompleteUpdateToStateObservers]_block_invoke
- ___block_descriptor_32_e75_B24?0"<BLSBacklightStateObserving>"8"BLSXPCBacklightProxyObserverMask"16l
- ___block_descriptor_48_e8_32s40bs_e75_v24?0"<BLSBacklightStateObserving>"8"BLSXPCBacklightProxyObserverMask"16ls40l8s32l8
- ___block_descriptor_58_e8_32s40s48s_e75_v24?0"<BLSBacklightStateObserving>"8"BLSXPCBacklightProxyObserverMask"16ls32l8s40l8s48l8
CStrings:
+ "B16@?0@\"BLSXPCBacklightProxyObservation\"8"
+ "mask"
+ "observer"
+ "v16@?0@\"BLSXPCBacklightProxyObservation\"8"
- "B24@?0@\"<BLSBacklightStateObserving>\"8@\"BLSXPCBacklightProxyObserverMask\"16"
- "v24@?0@\"<BLSBacklightStateObserving>\"8@\"BLSXPCBacklightProxyObserverMask\"16"
```
