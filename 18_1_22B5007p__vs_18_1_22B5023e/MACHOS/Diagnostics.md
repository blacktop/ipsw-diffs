## Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

-795.0.0.0.0
-  __TEXT.__text: 0xc259c
+818.0.0.0.0
+  __TEXT.__text: 0xc2de0
   __TEXT.__auth_stubs: 0x1ea0
-  __TEXT.__objc_stubs: 0x68c0
-  __TEXT.__objc_methlist: 0x4378
+  __TEXT.__objc_stubs: 0x6b40
+  __TEXT.__objc_methlist: 0x4420
   __TEXT.__gcc_except_tab: 0xa98
-  __TEXT.__objc_methname: 0xca4f
+  __TEXT.__objc_methname: 0xcc82
   __TEXT.__objc_classname: 0xa83
   __TEXT.__objc_methtype: 0x3459
   __TEXT.__const: 0x2cf4
-  __TEXT.__cstring: 0x8f5b
-  __TEXT.__oslogstring: 0x2763
+  __TEXT.__cstring: 0x8fab
+  __TEXT.__oslogstring: 0x2963
   __TEXT.__dlopen_cstrs: 0xfc
   __TEXT.__ustring: 0x64
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x3718
+  __TEXT.__constg_swiftt: 0x3720
   __TEXT.__swift5_typeref: 0x14a0
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_reflstr: 0x2967

   __TEXT.__swift5_assocty: 0x270
   __TEXT.__swift5_proto: 0x1d0
   __TEXT.__swift5_types: 0x19c
-  __TEXT.__swift5_capture: 0x11e0
+  __TEXT.__swift5_capture: 0x11f0
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2658
+  __TEXT.__unwind_info: 0x2680
   __TEXT.__eh_frame: 0x318
   __DATA_CONST.__auth_got: 0xf60
-  __DATA_CONST.__got: 0xa90
+  __DATA_CONST.__got: 0xaa8
   __DATA_CONST.__auth_ptr: 0xce0
-  __DATA_CONST.__const: 0x6e18
-  __DATA_CONST.__cfstring: 0x1ca0
+  __DATA_CONST.__const: 0x6e90
+  __DATA_CONST.__cfstring: 0x1ce0
   __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x130
-  __DATA_CONST.__objc_intobj: 0x990
-  __DATA_CONST.__objc_arraydata: 0x278
+  __DATA_CONST.__objc_intobj: 0x9c0
+  __DATA_CONST.__objc_arraydata: 0x288
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA.__objc_const: 0x1aa38
-  __DATA.__objc_selrefs: 0x2eb8
-  __DATA.__objc_ivar: 0x360
-  __DATA.__objc_data: 0x68e8
-  __DATA.__data: 0x3f28
+  __DATA.__objc_const: 0x1aaf8
+  __DATA.__objc_selrefs: 0x2f58
+  __DATA.__objc_ivar: 0x370
+  __DATA.__objc_data: 0x68f0
+  __DATA.__data: 0x3f38
   __DATA.__bss: 0x2dd0
   __DATA.__common: 0x108
   - /System/Library/Frameworks/Combine.framework/Combine
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

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
-  Functions: 4003
-  Symbols:   987
-  CStrings:  3926
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4022
+  Symbols:   998
+  CStrings:  3960
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CBDiscovery
+ _OBJC_CLASS_$_ELSEnvironment
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\x19"
+ "Accessory is in a disconnected state upon resuming handling. Ending the session immediately."
+ "DAOverrideSessionMode"
+ "DK requested to allow accessory disconnect for %!@(MISSING)"
+ "DK requested to clear allowing accessory disconnects"
+ "Disconnect is temporairly ignored"
+ "Ignoring accessory disconnects for %!@(MISSING) seconds"
+ "Resuming handling for accessory disconnects"
+ "T@\"NSTimer\",&,N,V_ignoreDisconnectTimer"
+ "T@\"NSUUID\",&,N,V_airpodsUUID"
+ "TB,N,V_hasIgnoredDisconnect"
+ "TB,N,V_isIgnoringDisconnect"
+ "UUIDString"
+ "Unable to find CoreBluetooth identifier for session accessory"
+ "_airpodsUUID"
+ "_hasIgnoredDisconnect"
+ "_ignoreDisconnectTimer"
+ "_isIgnoringDisconnect"
+ "airpodsUUID"
+ "allowSessionAccessoryDisconnectForDuration called with an invalid duration of %!@(MISSING). Ignoring request. If the accessory disconnects, the session will end. This is a bug in the calling DK."
+ "cloudKitContainerIdentifier"
+ "containerIdentifier"
+ "devicesWithDiscoveryFlags:error:"
+ "endIgnoringDisconnects"
+ "environment"
+ "hasIgnoredDisconnect"
+ "ignoreDisconnectTimer"
+ "initWithDomain:code:userInfo:"
+ "initWithUUIDString:"
+ "isIgnoringDisconnect"
+ "serialNumberLeft"
+ "serialNumberRight"
+ "sessionMode"
+ "setAirpodsUUID:"
+ "setHasIgnoredDisconnect:"
+ "setIgnoreDisconnectTimer:"
+ "setIsIgnoringDisconnect:"
- "\x18"
- "Server"
- "setHyphenationFactor:"

```
