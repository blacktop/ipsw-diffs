## deviceinterfaced

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Support/deviceinterfaced`

```diff

-  __TEXT.__text: 0x9188
+  __TEXT.__text: 0x9390
   __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_stubs: 0x440
   __TEXT.__objc_methlist: 0x374
-  __TEXT.__cstring: 0x4655
+  __TEXT.__cstring: 0x4720
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0x18b5
   __TEXT.__objc_methtype: 0x737
   __TEXT.__unwind_info: 0x90
   __TEXT.__eh_frame: 0x7c
-  __DATA_CONST.__const: 0x230
-  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x288

   __DATA.__objc_classrefs: 0x10
   __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0xd
-  __DATA.__bss: 0xb8
+  __DATA.__data: 0xe
+  __DATA.__bss: 0xc0
   - /Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 137
+  Functions: 139
   Symbols:   99
-  CStrings:  518
+  CStrings:  524
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
Functions:
~ sub_100003e60 : 1736 -> 1768
+ sub_100004548
+ sub_100009064
CStrings:
+ "%s DockChannel serial RX queue log size: %u (%u)"
+ "%s preferences override: %d (%d)"
+ "DockChannelSerialRxQueueLogSize"
+ "dock_channel_serial_rx_queue_log_size"
+ "dock_channel_serial_rx_queue_log_size_block_invoke"

```
