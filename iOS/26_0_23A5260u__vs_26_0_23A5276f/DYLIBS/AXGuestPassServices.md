## AXGuestPassServices

> `/System/Library/PrivateFrameworks/AXGuestPassServices.framework/AXGuestPassServices`

```diff

-3180.6.1.0.0
-  __TEXT.__text: 0xefc4
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x394
-  __TEXT.__const: 0x428
-  __TEXT.__cstring: 0x66f
+3183.1.0.0.0
+  __TEXT.__text: 0xfa58
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_methlist: 0x364
+  __TEXT.__const: 0x438
+  __TEXT.__cstring: 0x62f
   __TEXT.__swift5_typeref: 0x255
-  __TEXT.__swift5_capture: 0x33c
-  __TEXT.__oslogstring: 0x8cb
+  __TEXT.__swift5_capture: 0x358
+  __TEXT.__oslogstring: 0xa2b
   __TEXT.__constg_swiftt: 0x1e8
   __TEXT.__swift5_reflstr: 0x10f
   __TEXT.__swift5_fieldmd: 0x12c
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x18
-  __TEXT.__swift_as_entry: 0x50
-  __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x4b8
-  __TEXT.__eh_frame: 0x7a8
-  __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0x859
-  __TEXT.__objc_methtype: 0x2be
-  __TEXT.__objc_stubs: 0x40
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x54
+  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__eh_frame: 0x850
+  __TEXT.__objc_classname: 0x47
+  __TEXT.__objc_methname: 0x84f
+  __TEXT.__objc_methtype: 0x285
+  __TEXT.__objc_stubs: 0x20
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x5b8
-  __AUTH_CONST.__const: 0x918
-  __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x638
-  __AUTH.__objc_data: 0x470
+  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__const: 0x968
+  __AUTH_CONST.__objc_const: 0x580
+  __AUTH.__objc_data: 0x420
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x2f0
   __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0x98

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 489464B0-92EF-364F-8713-0112BB08C3E5
-  Functions: 360
-  Symbols:   417
-  CStrings:  214
+  UUID: 4A481F7F-D072-3A5B-8F3E-4A147F6CC965
+  Functions: 366
+  Symbols:   394
+  CStrings:  213
 
Symbols:
+ _objectdestroy.5Tm
+ _swift_dynamicCastClass
- -[AXGuestPassNetworkListenerWrapper .cxx_destruct]
- -[AXGuestPassNetworkListenerWrapper init]
- -[AXGuestPassNetworkListenerWrapper listen]
- _AXGuestPassSceneConnectionOptionsID
- _OBJC_CLASS_$_AXGuestPassNetworkListenerWrapper
- _OBJC_IVAR_$_AXGuestPassNetworkListenerWrapper._listener
- _OBJC_METACLASS_$_AXGuestPassNetworkListenerWrapper
- __OBJC_$_INSTANCE_METHODS_AXGuestPassNetworkListenerWrapper
- __OBJC_$_INSTANCE_VARIABLES_AXGuestPassNetworkListenerWrapper
- __OBJC_CLASS_RO_$_AXGuestPassNetworkListenerWrapper
- __OBJC_METACLASS_RO_$_AXGuestPassNetworkListenerWrapper
- ___CFConstantStringClassReference
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AXGuestPassServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AXGuestPassServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AXGuestPassServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AXGuestPassServices
- _objc_alloc_init
- _objc_msgSend$listen
- _objc_storeStrong
CStrings:
+ "AXGuestPassNetworkListener: Ending guest pass session due to severed connection. Physical device range likely too far."
+ "AXGuestPassNetworkListener: Failed to end guest pass session."
+ "AXGuestPassNetworkListener: Failed to retrieve metadata from connection."
+ "AXGuestPassNetworkListener: Setting connection keep alive timer to 15 seconds."
- "@\"_TtC19AXGuestPassServices26AXGuestPassNetworkListener\""
- "AXGuestPassNetworkListenerWrapper"
- "_listener"
- "com.apple.AccessibilityUIServer.AXGuestPassServer"

```
