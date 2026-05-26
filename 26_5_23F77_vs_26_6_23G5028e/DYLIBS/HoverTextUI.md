## HoverTextUI

> `/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x66f90
-  __TEXT.__auth_stubs: 0x2450
+3191.39.0.0.0
+  __TEXT.__text: 0x69dec
+  __TEXT.__auth_stubs: 0x2470
   __TEXT.__objc_methlist: 0x404
-  __TEXT.__const: 0x3d38
+  __TEXT.__const: 0x3d88
   __TEXT.__cstring: 0xb39
-  __TEXT.__oslogstring: 0x1079
+  __TEXT.__oslogstring: 0x13c9
   __TEXT.__swift5_typeref: 0x42e6
   __TEXT.__constg_swiftt: 0x1d78
-  __TEXT.__swift5_reflstr: 0x1622
-  __TEXT.__swift5_fieldmd: 0x100c
+  __TEXT.__swift5_reflstr: 0x1642
+  __TEXT.__swift5_fieldmd: 0x1018
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x2e8
-  __TEXT.__swift5_capture: 0x7cc
+  __TEXT.__swift5_capture: 0x810
   __TEXT.__swift5_proto: 0x104
   __TEXT.__swift5_types: 0xe0
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift_as_entry: 0x78
-  __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x1660
-  __TEXT.__eh_frame: 0x1c18
+  __TEXT.__swift_as_entry: 0x8c
+  __TEXT.__swift_as_ret: 0x54
+  __TEXT.__unwind_info: 0x1748
+  __TEXT.__eh_frame: 0x1ff8
   __TEXT.__objc_classname: 0x22a
-  __TEXT.__objc_methname: 0x265b
+  __TEXT.__objc_methname: 0x26ae
   __TEXT.__objc_methtype: 0x5e5
-  __TEXT.__objc_stubs: 0x1b40
-  __DATA_CONST.__got: 0x760
+  __TEXT.__objc_stubs: 0x1b80
+  __DATA_CONST.__got: 0x770
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_selrefs: 0x848
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1230
-  __AUTH_CONST.__const: 0x2a60
+  __AUTH_CONST.__auth_got: 0x1240
+  __AUTH_CONST.__const: 0x2b00
   __AUTH_CONST.__cfstring: 0x4c0
-  __AUTH_CONST.__objc_const: 0x1930
+  __AUTH_CONST.__objc_const: 0x1950
   __AUTH.__objc_data: 0x2d0
-  __AUTH.__data: 0x15f8
+  __AUTH.__data: 0x15e8
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x13a0
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x2300
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x518
-  __DATA_DIRTY.__data: 0x190
+  __DATA_DIRTY.__data: 0x1a0
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 56FB29AC-C663-39B9-927B-7507FFBB9A95
-  Functions: 2084
-  Symbols:   1542
-  CStrings:  691
+  UUID: E3AE7430-B797-39F5-85AA-6F15EE6A1FDE
+  Functions: 2127
+  Symbols:   1555
+  CStrings:  706
 
Symbols:
+ _AXkMobileKeyBagLockStatusNotificationID
+ _CFNotificationCenterRemoveEveryObserver
+ _OBJC_CLASS_$_AXSpringBoardServer
+ _block_copy_helper.126
+ _block_copy_helper.163
+ _block_copy_helper.175
+ _block_descriptor.128
+ _block_descriptor.165
+ _block_descriptor.177
+ _block_destroy_helper.127
+ _block_destroy_helper.164
+ _block_destroy_helper.176
+ _kAXSContinuityDisplayStateChangedNotification
+ _objc_msgSend$isContinuitySessionActive
+ _objc_msgSend$windowScene
+ _objectdestroy.120Tm
- _block_copy_helper.141
- _block_copy_helper.153
- _block_descriptor.143
- _block_descriptor.155
- _block_destroy_helper.142
- _block_destroy_helper.154
CStrings:
+ "Continuity display state changed. isContinuitySessionActive=%{bool}d"
+ "Continuity session active. Removing Hover Typing from view hierarchy."
+ "Continuity session ended and device unlocked. Re-attaching Hover Typing to view hierarchy."
+ "Continuity session ended but device still locked. Will reattach on unlock."
+ "Device lock status changed. AXDeviceIsUnlocked=%{bool}d"
+ "Device locked. Removing Hover Typing from view hierarchy."
+ "Device unlocked. Re-attaching Hover Typing to view hierarchy."
+ "Failed to reattach Hover Typing after lock: %s"
+ "Initial state: isContinuitySessionActive=%{bool}d, isLocked=%{bool}d"
+ "Re-attaching Hover Typing VCs to display manager."
+ "Screen did lock. Turning off hover touch"
+ "Starting monitor for device lock status (Hover Typing)."
+ "Stopping monitor for device lock status (Hover Typing)."
+ "isContinuitySessionActive"
+ "isDetachedForLock"
+ "windowScene"
- "Screen did lock. Turning off live speech"

```
