## HomeControlCenterModule

> `/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule`

```diff

-989.4.12.0.0
-  __TEXT.__text: 0x17514
+1025.0.0.1.1
+  __TEXT.__text: 0x1808c
   __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x1064
-  __TEXT.__const: 0x204
-  __TEXT.__cstring: 0xe67
-  __TEXT.__oslogstring: 0xbe8
+  __TEXT.__objc_methlist: 0x19fc
+  __TEXT.__const: 0x1f4
+  __TEXT.__cstring: 0xbc7
+  __TEXT.__oslogstring: 0xc48
   __TEXT.__gcc_except_tab: 0x1ec
-  __TEXT.__swift5_typeref: 0x2a0
+  __TEXT.__swift5_typeref: 0x2f8
   __TEXT.__swift5_fieldmd: 0x3c
   __TEXT.__constg_swiftt: 0xc8
   __TEXT.__swift5_reflstr: 0xd
-  __TEXT.__swift5_capture: 0x1ec
+  __TEXT.__swift5_capture: 0x244
   __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x770
-  __TEXT.__eh_frame: 0x770
+  __TEXT.__unwind_info: 0x7e0
+  __TEXT.__eh_frame: 0x938
   __TEXT.__objc_classname: 0x452
-  __TEXT.__objc_methname: 0x5c82
-  __TEXT.__objc_methtype: 0x1121
-  __TEXT.__objc_stubs: 0x3b80
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x5d0
+  __TEXT.__objc_methname: 0x5d1d
+  __TEXT.__objc_methtype: 0x1166
+  __TEXT.__objc_stubs: 0x3c00
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x5b8
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1220
+  __DATA_CONST.__objc_selrefs: 0x1550
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x670
-  __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__auth_ptr: 0x78
+  __AUTH_CONST.__const: 0x628
   __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x3488
+  __AUTH_CONST.__objc_const: 0x2418
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1a8
+  __AUTH.__objc_data: 0x188
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x110
-  __DATA.__data: 0xcf8
+  __DATA.__objc_ivar: 0x114
+  __DATA.__data: 0xd18
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x280

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 588
+  Functions: 614
   Symbols:   313
-  CStrings:  1230
+  CStrings:  1225
 
Symbols:
+ _OBJC_CLASS_$_NSUUID
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_arrayDestroy
CStrings:
+ "\a"
+ "%@:controlCenterModuleViewController %@ didStartDisplayingHome %@ allowsCharacteristicNotifications:%{BOOL}d"
+ "@\"NSUUID\""
+ "T@\"<NACancelable>\",&,N,V_registrationScheduledCancelation"
+ "T@\"NSUUID\",R,N,V_moduleUniqueIdentifier"
+ "UUID"
+ "_moduleUniqueIdentifier"
+ "_registrationScheduledCancelation"
+ "addStateSubscriptionReasonToDataModel"
+ "controlCenterModuleViewController:didStartDisplayingHome:"
+ "moduleUniqueIdentifier"
+ "registerForItems:inHome:currentRegistration:completionBlock:"
+ "registrationScheduledCancelation"
+ "removeStateSubscriptionReasonFromDataModel"
+ "setModuleWithIdentifier:subscribedToHome:"
+ "setRegistrationScheduledCancelation:"
+ "v32@0:8@\"HUControlCenterModuleViewController\"16@\"HMHome\"24"
+ "v48@0:8@\"NSSet\"16@\"HMHome\"24@32@?<v@?@>40"
- "\x06"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"<NACancelable>\",&,N,V_characteristicRegistrationScheduledCancelation"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_characteristicRegistrationScheduledCancelation"
- "characteristicRegistrationScheduledCancelation"
- "characteristicsToEnableNotificationsForItems:"
- "invalid Collection: less than 'count' elements in collection"
- "registerForCharacteristics:items:inHome:currentRegistration:completionBlock:"
- "setCharacteristicRegistrationScheduledCancelation:"
- "v56@0:8@\"NSSet\"16@\"NSSet\"24@\"HMHome\"32@40@?<v@?@>48"

```
