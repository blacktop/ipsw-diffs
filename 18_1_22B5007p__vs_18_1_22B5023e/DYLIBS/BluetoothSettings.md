## BluetoothSettings

> `/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`

```diff

-440.46.0.0.0
-  __TEXT.__text: 0x1a554
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x101c
-  __TEXT.__const: 0x37a
+441.1.0.0.0
+  __TEXT.__text: 0x1bc30
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x107c
+  __TEXT.__const: 0x51e
   __TEXT.__gcc_except_tab: 0x350
-  __TEXT.__cstring: 0x1361
-  __TEXT.__oslogstring: 0x1658
-  __TEXT.__swift5_typeref: 0xb7
-  __TEXT.__constg_swiftt: 0x70
-  __TEXT.__swift5_fieldmd: 0x2c
-  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__cstring: 0x1431
+  __TEXT.__oslogstring: 0x198b
+  __TEXT.__swift5_typeref: 0x12f
+  __TEXT.__constg_swiftt: 0x9c
+  __TEXT.__swift5_fieldmd: 0x48
+  __TEXT.__swift5_capture: 0x24
+  __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x23
-  __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x18
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x5a0
-  __TEXT.__objc_classname: 0x182
-  __TEXT.__objc_methname: 0x435c
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__objc_classname: 0x183
+  __TEXT.__objc_methname: 0x4540
   __TEXT.__objc_methtype: 0xd0d
-  __TEXT.__objc_stubs: 0x3b40
-  __DATA_CONST.__got: 0x530
-  __DATA_CONST.__const: 0x4e8
+  __TEXT.__objc_stubs: 0x3c00
+  __DATA_CONST.__got: 0x558
+  __DATA_CONST.__const: 0x528
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11a0
+  __DATA_CONST.__objc_selrefs: 0x1210
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x3f0
-  __AUTH_CONST.__auth_ptr: 0xe8
-  __AUTH_CONST.__const: 0xe8
-  __AUTH_CONST.__cfstring: 0x1680
-  __AUTH_CONST.__objc_const: 0x24d8
+  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_ptr: 0xf8
+  __AUTH_CONST.__const: 0x188
+  __AUTH_CONST.__cfstring: 0x1740
+  __AUTH_CONST.__objc_const: 0x2558
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x420
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x174
-  __DATA.__data: 0x3c0
+  __DATA.__objc_ivar: 0x180
+  __DATA.__data: 0x430
   __DATA.__common: 0x18
-  __DATA.__bss: 0x310
+  __DATA.__bss: 0x610
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 473
-  Symbols:   767
-  CStrings:  1244
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 506
+  Symbols:   795
+  CStrings:  1282
 
Symbols:
+ _OBJC_CLASS_$_OS_dispatch_queue
+ __Block_copy
+ __Block_release
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x25
+ _swift_allocObject
+ _swift_deallocObject
+ _swift_dynamicCastObjCClass
+ _swift_getObjCClassMetadata
+ _swift_initStackObject
+ _swift_unknownObjectRelease
CStrings:
+ "\x0f\x02(\x1a\x12"
+ "%!s(MISSING) %!@(MISSING)"
+ "-[BTSDevicesController forcePushDetailViewForDevice:]"
+ "ASK_LINKED_RADIO_ADDRESS"
+ "ASK_RELATED_RADIO_ADDRESS"
+ "DADeviceLost"
+ "Device linked radio address: %!@(MISSING)"
+ "EnableBLE"
+ "Merging dual radio devices from AccessorySetupKit"
+ "Not showing peripheral because it's CTKD and will be shown with the classic device instead: %!@(MISSING)"
+ "Not showing peripheral because it's linked to another classic radio and will be shown with the classic device instead: %!@(MISSING)"
+ "Peripheral does not have linked address: %!@(MISSING)"
+ "Peripheral has linked classic radio but we don't see the classic device with this address. Showing LE device %!@(MISSING)"
+ "Peripheral is waiting to link to a classic radio that is yet to be paired, showing LE first: %!@(MISSING)"
+ "Stop Force Push to Detail View because we're already in this page for device %!@(MISSING)"
+ "T@\"NSString\",&,N,GlinkedRadioAddress,V_linkedRadioAddress"
+ "T@\"NSString\",&,N,GrelatedFutureRadioAddress,V_relatedFutureRadioAddress"
+ "This device needs to be coalesced with a DADevice before being displayed: %!@(MISSING)"
+ "UICTFontTextStyleShortEmphasizedBody"
+ "We cannot link to the new classic device because it's already linked to another LE device due to CTKD %!@(MISSING)"
+ "_dualRadioCounterpartDevicesDict"
+ "_linkedRadioAddress"
+ "_pendingOtherRadioDevicesDict"
+ "_relatedFutureRadioAddress"
+ "childViewControllers"
+ "colorWithAlphaComponent:"
+ "com.apple.carplay"
+ "initWithString:attributes:"
+ "isLECarPlayEnabled"
+ "labelColor"
+ "linked-le-device"
+ "linkedRadioAddress"
+ "mergeDualRadioDevices:"
+ "relatedFutureRadioAddress"
+ "setFont:"
+ "setLinkedRadioAddress:"
+ "setRelatedFutureRadioAddress:"
+ "setTitleView:"
+ "target"
+ "topViewController"
- "\x0f(\x1a\x12"
- "_awaitingIncomingConnection"

```
