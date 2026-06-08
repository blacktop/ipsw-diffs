## storagekitd

> `/usr/libexec/storagekitd`

```diff

-1037.120.10.0.0
-  __TEXT.__text: 0x30104
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_stubs: 0x62e0
-  __TEXT.__objc_methlist: 0x294c
-  __TEXT.__objc_classname: 0x523
-  __TEXT.__objc_methname: 0x652a
+1075.0.0.0.0
+  __TEXT.__text: 0x2ce94
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_stubs: 0x63e0
+  __TEXT.__objc_methlist: 0x29a4
+  __TEXT.__objc_classname: 0x4f1
+  __TEXT.__objc_methname: 0x6637
   __TEXT.__objc_methtype: 0xfe6
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0xc48
-  __TEXT.__cstring: 0x2dd8
-  __TEXT.__oslogstring: 0x26ac
-  __TEXT.__unwind_info: 0xba8
-  __DATA_CONST.__auth_got: 0x600
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__auth_ptr: 0x8
+  __TEXT.__gcc_except_tab: 0xb1c
+  __TEXT.__cstring: 0x2ea6
+  __TEXT.__oslogstring: 0x275f
+  __TEXT.__unwind_info: 0xaa8
   __DATA_CONST.__const: 0xf60
   __DATA_CONST.__cfstring: 0x1ec0
   __DATA_CONST.__objc_classlist: 0x190

   __DATA_CONST.__objc_dictobj: 0x1b8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x5f60
-  __DATA.__objc_selrefs: 0x1c80
-  __DATA.__objc_ivar: 0x2c4
+  __DATA_CONST.__auth_got: 0x630
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x5fc0
+  __DATA.__objc_selrefs: 0x1cc0
+  __DATA.__objc_ivar: 0x2cc
   __DATA.__objc_data: 0xfa0
   __DATA.__data: 0x700
   __DATA.__bss: 0x98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: E290ECF6-EBFB-392A-8443-752F97A839F1
-  Functions: 912
-  Symbols:   367
-  CStrings:  2397
+  UUID: DE9E8901-059B-3A98-8C7D-B58A40F4B4D0
+  Functions: 922
+  Symbols:   375
+  CStrings:  2417
 
Symbols:
+ __dispatch_source_type_timer
+ _dispatch_source_cancel
+ _dispatch_source_set_timer
+ _kDADiskDescriptionRepairRunningKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
- _objc_release_x10
CStrings:
+ "%s: DA notification timer fired"
+ "%s: Starting notification processing timer (5 second timeout)"
+ "%s: Timeout waiting for DA idle notification, proceeding manually"
+ "%s: timer canceled"
+ "-[SKDaemonManager _timerFired]"
+ "-[SKDaemonManager cancelTimer]"
+ "-[SKDaemonManager startTimer]"
+ "-[SKDaemonManager syncAllDisksWithCompletionBlock:]_block_invoke"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_notificationProcessingTimer"
+ "TB,N,V_enableTimer"
+ "_enableTimer"
+ "_notificationProcessingTimer"
+ "_timerFired"
+ "cancelTimer"
+ "enableTimer"
+ "notificationProcessingTimer"
+ "setEnableTimer:"
+ "setNotificationProcessingTimer:"
+ "setRepairRunning:"
+ "startTimer"

```
