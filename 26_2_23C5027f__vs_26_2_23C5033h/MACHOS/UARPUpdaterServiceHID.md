## UARPUpdaterServiceHID

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID`

```diff

-1338.60.16.0.0
-  __TEXT.__text: 0x1d748
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x2800
-  __TEXT.__objc_methlist: 0x1180
+1338.60.22.0.0
+  __TEXT.__text: 0x1daf4
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x2820
+  __TEXT.__objc_methlist: 0x1190
   __TEXT.__gcc_except_tab: 0xe4
-  __TEXT.__objc_methname: 0x369a
+  __TEXT.__objc_methname: 0x36db
   __TEXT.__objc_classname: 0x1ac
-  __TEXT.__objc_methtype: 0xb8d
+  __TEXT.__objc_methtype: 0xbad
   __TEXT.__cstring: 0x1fb0
-  __TEXT.__oslogstring: 0x1037
+  __TEXT.__oslogstring: 0x112f
   __TEXT.__const: 0xb0
-  __TEXT.__unwind_info: 0x780
-  __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x890
+  __TEXT.__unwind_info: 0x788
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x8b8
   __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1be8
-  __DATA.__objc_selrefs: 0xd28
-  __DATA.__objc_ivar: 0xd4
+  __DATA.__objc_const: 0x1c08
+  __DATA.__objc_selrefs: 0xd30
+  __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x315
   __DATA.__bss: 0x1180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E355BBC9-EC82-3EF7-842E-7A1756E8B5ED
-  Functions: 758
-  Symbols:   559
-  CStrings:  1043
+  UUID: AC352D0B-36AA-38A0-947C-A09BA6A4ABCF
+  Functions: 766
+  Symbols:   569
+  CStrings:  1051
 
Symbols:
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
CStrings:
+ "@\"NSObject<OS_dispatch_source>\""
+ "Already released power assertion for timer"
+ "Created a power assertion, but the activity timer is already running"
+ "Failed to release power assertion for timer"
+ "Power assertion activity timeout fired"
+ "Power assertion activity timer fired, with nil timer"
+ "_powerAssertionActivityTimer"
+ "handlePowerAssertionActivityTimeout"

```
