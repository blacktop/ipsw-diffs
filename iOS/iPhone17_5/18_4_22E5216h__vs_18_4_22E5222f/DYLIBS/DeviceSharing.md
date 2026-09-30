## DeviceSharing

> `/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing`

```diff

-27.100.10.0.2
-  __TEXT.__text: 0x6040c
-  __TEXT.__auth_stubs: 0x1b40
+27.100.12.0.0
+  __TEXT.__text: 0x6324c
+  __TEXT.__auth_stubs: 0x1c30
   __TEXT.__objc_methlist: 0x2f8
-  __TEXT.__const: 0x1728
-  __TEXT.__cstring: 0x19eb
-  __TEXT.__swift5_typeref: 0xf4b
-  __TEXT.__swift5_fieldmd: 0x710
-  __TEXT.__constg_swiftt: 0x1124
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x622
+  __TEXT.__const: 0x17d8
+  __TEXT.__cstring: 0x19bb
+  __TEXT.__swift5_typeref: 0xf87
+  __TEXT.__swift5_fieldmd: 0x728
+  __TEXT.__constg_swiftt: 0x1144
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_reflstr: 0x642
   __TEXT.__swift5_assocty: 0x108
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__swift5_proto: 0x104
+  __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x90
-  __TEXT.__oslogstring: 0x1f79
+  __TEXT.__oslogstring: 0x20f9
   __TEXT.__swift_as_entry: 0x324
-  __TEXT.__swift_as_ret: 0x2dc
-  __TEXT.__swift5_capture: 0x590
-  __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x1880
-  __TEXT.__eh_frame: 0x49f8
+  __TEXT.__swift_as_ret: 0x2e0
+  __TEXT.__swift5_capture: 0x5a8
+  __TEXT.__swift5_mpenum: 0x2c
+  __TEXT.__unwind_info: 0x1910
+  __TEXT.__eh_frame: 0x4c88
   __TEXT.__objc_classname: 0x93
   __TEXT.__objc_methname: 0x76c
   __TEXT.__objc_methtype: 0x25d
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__got: 0x5d0
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xda8
-  __AUTH_CONST.__auth_ptr: 0x540
-  __AUTH_CONST.__const: 0x17d8
+  __AUTH_CONST.__auth_got: 0xe20
+  __AUTH_CONST.__auth_ptr: 0x548
+  __AUTH_CONST.__const: 0x17f0
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0xfa8
+  __AUTH_CONST.__objc_const: 0xfc8
   __AUTH.__objc_data: 0x410
   __AUTH.__data: 0xa20
-  __DATA.__data: 0x1800
-  __DATA.__bss: 0x1800
+  __DATA.__data: 0x1858
+  __DATA.__bss: 0x1900
   __DATA.__common: 0xe8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1511
-  Symbols:   291
-  CStrings:  413
+  Functions: 1526
+  Symbols:   290
+  CStrings:  418
 
CStrings:
+ "%{public}s attempting to reconnect due to %{public}@"
+ "%{public}s cannot reconnect because maximum retry count exceeded; throwing error: %{public}@"
+ "%{public}s cannot reconnect if %s"
+ "%{public}s cannot reconnect if inactive"
+ "%{public}s will attempt to reconnect after retry delay %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/DeviceSharing/DeviceSharing/Daemon/Peer/PeerConnection.swift"
+ "[%{public}s] Connection waiting with error: %{public}@"
+ "[%{public}s] Created peer connection service %{public}s with peer connection %{public}s"
+ "[%{public}s] Invalidate for state: %{public}s)"
+ "[%{public}s] Peer connection activation timeout hit"
+ "[%{public}s] Peer connection activation timeout started"
+ "[%{public}s] Peer connection initiated: %{public}s"
+ "[%{public}s] Peer connection initiation failed: %{public}@"
+ "timeoutTask"
- "%{public}s max reconnect retry count; not reconnecting"
- "%{public}s not initiator; not reconnecting"
- "%{public}s will attempt to reconnect; retry delay %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/DeviceSharing/DeviceSharing/Daemon/Peer/PeerConnectionServiceCoordinator.swift"
- "[%{public}s] Invalidate"
- "[%{public}s] Peer connection %{public}s is waiting with error: %{public}@"
- "[%{public}s] Peer connection %{public}s was active; resetting"
- "[%{public}s] Peer connection is waiting with error: %{public}@"
- "reconnectIfNeeded(error:)"

```
