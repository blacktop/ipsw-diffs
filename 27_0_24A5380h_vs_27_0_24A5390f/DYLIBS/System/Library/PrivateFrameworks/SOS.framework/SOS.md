## SOS

> `/System/Library/PrivateFrameworks/SOS.framework/SOS`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__DATA.__data`

```diff

-669.100.1.0.0
-  __TEXT.__text: 0x3609c
+670.100.1.0.0
+  __TEXT.__text: 0x360d0
   __TEXT.__objc_methlist: 0x39d4
   __TEXT.__const: 0x256
   __TEXT.__cstring: 0x4bb8
-  __TEXT.__oslogstring: 0x6670
+  __TEXT.__oslogstring: 0x6676
   __TEXT.__gcc_except_tab: 0x85c
   __TEXT.__dlopen_cstrs: 0x3e9
   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1008
+  __TEXT.__unwind_info: 0x1000
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1178
+  __DATA_CONST.__const: 0x1180
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__got: 0x398
   __AUTH_CONST.__const: 0x640
   __AUTH_CONST.__cfstring: 0x4240
   __AUTH_CONST.__objc_const: 0x4db8

   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x640
-  __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x304
   __DATA.__data: 0x9f0
-  __DATA.__bss: 0x268
-  __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__data: 0x1
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA.__bss: 0x218
+  __DATA_DIRTY.__objc_data: 0xb40
+  __DATA_DIRTY.__data: 0x99
+  __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 1468
-  Symbols:   3404
+  Symbols:   3405
   CStrings:  1174
 
Symbols:
+ -[SOSCoordinator effectivePairedDeviceInDevices:]
+ _SOSCoordinatorErrorDomain
+ _objc_msgSend$effectivePairedDeviceInDevices:
- -[SOSCoordinator _handleServiceUpdate:]
- _objc_msgSend$_handleServiceUpdate:
Functions:
~ -[SOSCoordinator SOSCoordinationMessageTypeForString:] -> -[SOSCoordinator effectivePairedDevice] : 208 -> 92
~ -[SOSCoordinator isPairedDeviceNearby] -> -[SOSCoordinator SOSCoordinationMessageTypeForString:] : 72 -> 208
~ -[SOSCoordinator service:nearbyDevicesChanged:] -> -[SOSCoordinator isPairedDeviceNearby] : 140 -> 72
~ -[SOSCoordinator _handleServiceUpdate:] -> -[SOSCoordinator service:nearbyDevicesChanged:] : 84 -> 184
CStrings:
+ "SOSCoordinator nearbyDevicesChanged (%tu)"
- "SOSCoordinator nearbyDevicesChanged"
```
