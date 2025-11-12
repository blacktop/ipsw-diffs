## UARPUpdaterServiceUSBPD

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD`

```diff

-1338.60.16.0.0
-  __TEXT.__text: 0x27534
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_stubs: 0x3580
-  __TEXT.__objc_methlist: 0x1ab0
+1338.60.22.0.0
+  __TEXT.__text: 0x27b20
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_stubs: 0x35a0
+  __TEXT.__objc_methlist: 0x1ac0
   __TEXT.__const: 0xd0
-  __TEXT.__oslogstring: 0x2983
-  __TEXT.__cstring: 0x30ae
-  __TEXT.__objc_classname: 0x20b
-  __TEXT.__objc_methtype: 0x38d9
+  __TEXT.__oslogstring: 0x2a7b
+  __TEXT.__cstring: 0x30fb
+  __TEXT.__objc_classname: 0x20c
+  __TEXT.__objc_methtype: 0x38f9
   __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__objc_methname: 0x47da
-  __TEXT.__unwind_info: 0x828
-  __DATA_CONST.__auth_got: 0x448
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x718
+  __TEXT.__objc_methname: 0x4838
+  __TEXT.__unwind_info: 0x838
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x740
   __DATA_CONST.__cfstring: 0x640
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x3708
-  __DATA.__objc_selrefs: 0x10b8
-  __DATA.__objc_ivar: 0x240
+  __DATA.__objc_const: 0x3748
+  __DATA.__objc_selrefs: 0x10c0
+  __DATA.__objc_ivar: 0x248
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x375
   __DATA.__bss: 0x1178

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 07743A06-BBA9-3C40-9986-F6D7BF3EDA3D
-  Functions: 1114
-  Symbols:   590
-  CStrings:  1645
+  UUID: D9A321E0-ADDF-37E4-B6BE-8219E8B36EE8
+  Functions: 1123
+  Symbols:   596
+  CStrings:  1655
 
Symbols:
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
CStrings:
+ "-[UARPUSBPDUpdater holdPowerAssertionForAccessory]_block_invoke"
+ "-[UARPUSBPDUpdater releasePowerAssertionForAccessory]_block_invoke"
+ "@\"NSObject<OS_dispatch_source>\""
+ "Already released power assertion for timer"
+ "Created a power assertion, but the activity timer is already running"
+ "Failed to release power assertion for timer"
+ "Power assertion activity timeout fired"
+ "Power assertion activity timer fired, with nil timer"
+ "_powerAssertionActivityTimer"
+ "_powerAssertionDispatchQueue"
+ "com.apple.accessoryupdater.usbpd.powerassert.queue"
+ "handlePowerAssertionActivityTimeout"
- "-[UARPUSBPDUpdater holdPowerAssertionForAccessory]"
- "-[UARPUSBPDUpdater releasePowerAssertionForAccessory]"

```
