## ptpd

> `/usr/libexec/ptpd`

```diff

-2013.0.0.0.0
-  __TEXT.__text: 0x2d5d4
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_stubs: 0x45a0
-  __TEXT.__objc_methlist: 0x2960
+2016.0.0.0.0
+  __TEXT.__text: 0x2dce8
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_stubs: 0x4680
+  __TEXT.__objc_methlist: 0x29b8
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x5b88
+  __TEXT.__cstring: 0x5c2b
   __TEXT.__oslogstring: 0x3f
-  __TEXT.__objc_classname: 0x1f2
-  __TEXT.__objc_methname: 0x6121
-  __TEXT.__objc_methtype: 0xb14
+  __TEXT.__objc_classname: 0x1f0
+  __TEXT.__objc_methname: 0x62cd
+  __TEXT.__objc_methtype: 0xb33
   __TEXT.__ustring: 0xc32
-  __TEXT.__gcc_except_tab: 0x5a0
-  __TEXT.__unwind_info: 0x768
-  __DATA_CONST.__auth_got: 0x540
+  __TEXT.__gcc_except_tab: 0x5c0
+  __TEXT.__unwind_info: 0x780
+  __DATA_CONST.__auth_got: 0x548
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x6700
+  __DATA_CONST.__cfstring: 0x6780
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_const: 0x3b48
-  __DATA.__objc_selrefs: 0x1a58
-  __DATA.__objc_ivar: 0x3fc
+  __DATA.__objc_const: 0x3bd8
+  __DATA.__objc_selrefs: 0x1a90
+  __DATA.__objc_ivar: 0x408
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x1b4
   __DATA.__common: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C583820-717D-3B3B-9A51-43E596526DAD
-  Functions: 957
-  Symbols:   233
-  CStrings:  3122
+  UUID: 018C9ED8-CCB6-3BC4-8E11-233EF6CA83BE
+  Functions: 966
+  Symbols:   234
+  CStrings:  3145
 
Symbols:
+ _os_transaction_create
CStrings:
+ "%x-GroupNotificationQueue"
+ "@\"NSObject<OS_os_transaction>\""
+ "New uncollected groups present (%u/%lu) -- notifying"
+ "PTPGroup"
+ "Stopping groups available notifier, all groups collected."
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_groupNotificationTimerQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_groupNotificationTimer"
+ "T@\"NSObject<OS_os_transaction>\",&,V_activeTransaction"
+ "_activeTransaction"
+ "_groupNotificationTimer"
+ "_groupNotificationTimerQueue"
+ "activeTransaction"
+ "groupNotificationTimer"
+ "groupNotificationTimerQueue"
+ "ptp_open_session"
+ "setActiveTransaction:"
+ "setGroupNotificationTimer:"
+ "setGroupNotificationTimerQueue:"
+ "startGroupNotifications"

```
