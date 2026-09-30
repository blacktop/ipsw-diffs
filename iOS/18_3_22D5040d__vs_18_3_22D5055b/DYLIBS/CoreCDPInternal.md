## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-386.233.0.0.0
-  __TEXT.__text: 0x8ec8c
-  __TEXT.__auth_stubs: 0x11d0
-  __TEXT.__objc_methlist: 0x44cc
-  __TEXT.__const: 0x730
-  __TEXT.__oslogstring: 0x13788
-  __TEXT.__cstring: 0x7705
+386.234.0.0.0
+  __TEXT.__text: 0x8db54
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_methlist: 0x4474
+  __TEXT.__const: 0x720
+  __TEXT.__oslogstring: 0x13568
+  __TEXT.__cstring: 0x7675
   __TEXT.__gcc_except_tab: 0xbac
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x301

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_capture: 0x1b8
-  __TEXT.__unwind_info: 0x1cb8
+  __TEXT.__unwind_info: 0x1c90
   __TEXT.__eh_frame: 0x8e0
-  __TEXT.__objc_classname: 0xc8c
-  __TEXT.__objc_methname: 0xeb7e
+  __TEXT.__objc_classname: 0xc79
+  __TEXT.__objc_methname: 0xeb56
   __TEXT.__objc_methtype: 0x28e1
   __TEXT.__objc_stubs: 0xbea0
-  __DATA_CONST.__got: 0x1008
+  __DATA_CONST.__got: 0x1000
   __DATA_CONST.__const: 0x2588
-  __DATA_CONST.__objc_classlist: 0x288
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x178
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3530
-  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_selrefs: 0x3520
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x8f8
+  __AUTH_CONST.__auth_got: 0x8a8
   __AUTH_CONST.__auth_ptr: 0x1d8
   __AUTH_CONST.__const: 0x9e8
   __AUTH_CONST.__cfstring: 0x4e60
-  __AUTH_CONST.__objc_const: 0x11af8
+  __AUTH_CONST.__objc_const: 0x116c8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1110
-  __AUTH.__data: 0x78
+  __AUTH.__objc_data: 0x10a0
+  __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x3a0
-  __DATA.__data: 0x1308
+  __DATA.__data: 0x1288
   __DATA.__bss: 0x840
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x920

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3028
-  Symbols:   3839
-  CStrings:  4739
+  Functions: 3016
+  Symbols:   3832
+  CStrings:  4721
 
Symbols:
- _MKBGetDeviceLockState
- _OBJC_CLASS_$_CDPDUnlockObserver
- _OBJC_METACLASS_$_CDPDUnlockObserver
- _swift_endAccess
- _swift_unknownObjectRelease_n
- _swift_unknownObjectRetain_n
CStrings:
- "%{public}s device is not unlocked. Found lock state %{public}d."
- "%{public}s ignoring event %{public}s because device is not unlocked"
- "%{public}s ignoring notification event %{public}s"
- "%{public}s received a nil eventName"
- "%{public}s recognizes event name %{public}s as unlocked. Notifying %{public}ld listeners."
- "CDPDUnlockListener"
- "CDPDUnlockObserver"
- "Fetched manatee status after device unlock with altDSID=%@, isPrimaryAccount=%{BOOL}d"
- "Fetching manatee status after device unlock with altDSID=%@, isPrimaryAccount=%{BOOL}d"
- "Notifying listener %{public}s"
- "com.apple.mobile.keybagd.lock_status"
- "currentDeviceIsUnlocked"
- "deviceDidUnlock"

```
