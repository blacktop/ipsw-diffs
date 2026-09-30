## HealthLEHeartRate

> `/System/Library/PrivateFrameworks/HealthLEHeartRate.framework/HealthLEHeartRate`

```diff

-6074.1.2.4.0
-  __TEXT.__text: 0x311c
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x55c
+6087.1.2.1.0
+  __TEXT.__text: 0x33f8
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0x574
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__cstring: 0x206
-  __TEXT.__oslogstring: 0x556
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__gcc_except_tab: 0x11c
+  __TEXT.__cstring: 0x20f
+  __TEXT.__oslogstring: 0x643
+  __TEXT.__unwind_info: 0x1a0
   __TEXT.__objc_classname: 0x16b
-  __TEXT.__objc_methname: 0xe82
-  __TEXT.__objc_methtype: 0x3c7
-  __TEXT.__objc_stubs: 0xa40
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x1a8
+  __TEXT.__objc_methname: 0xec5
+  __TEXT.__objc_methtype: 0x3c9
+  __TEXT.__objc_stubs: 0xa60
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e0
+  __DATA_CONST.__objc_selrefs: 0x3f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0xc40
+  __AUTH_CONST.__objc_const: 0xc60
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2A63615C-9B33-3513-969A-BEFC361F7040
-  Functions: 94
-  Symbols:   488
-  CStrings:  307
+  UUID: 6144D6A5-1B50-36D2-ABDE-0E9DBDF607A6
+  Functions: 96
+  Symbols:   499
+  CStrings:  315
 
Symbols:
+ -[HLEHeartRateCollectionObserver _setupNotificationListener]
+ -[HLEHeartRateCollectionObserver dealloc]
+ GCC_except_table15
+ GCC_except_table7
+ _OBJC_IVAR_$_HLEHeartRateCollectionObserver._heartRateCollectionNotifyToken
+ ___60-[HLEHeartRateCollectionObserver _setupNotificationListener]_block_invoke
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ __dispatch_main_q
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_msgSend$_setupNotificationListener
- -[HLEHeartRateCollectionObserver connectionInvalidated].cold.1
- GCC_except_table12
- GCC_except_table2
CStrings:
+ "%{public}@: Connection Interrupted, but collection is off. Invalidating connection"
+ "%{public}@: Setting up XPC Connection"
+ "HLEHeartRateCollectionObserver: Notification received for collection state change while connection was invalidated."
+ "_heartRateCollectionNotifyToken"
+ "_setupNotificationListener"
+ "dealloc"
+ "v12@?0i8"

```
