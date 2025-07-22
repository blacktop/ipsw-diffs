## DeviceCheck

> `/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck`

```diff

-123.0.0.0.0
-  __TEXT.__text: 0xa028
-  __TEXT.__auth_stubs: 0x4d0
+125.0.0.0.0
+  __TEXT.__text: 0xa1b0
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_methlist: 0x67c
   __TEXT.__const: 0xa8
   __TEXT.__cstring: 0x7f0
-  __TEXT.__gcc_except_tab: 0x43c
+  __TEXT.__gcc_except_tab: 0x548
   __TEXT.__oslogstring: 0xc8e
-  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__unwind_info: 0x2b8
   __TEXT.__objc_classname: 0xf8
   __TEXT.__objc_methname: 0x105b
   __TEXT.__objc_methtype: 0x5b9

   __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x640
   __AUTH_CONST.__objc_const: 0xa60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98E7C75A-8E43-318A-BACD-0146A48058F9
+  UUID: 698979C8-B03D-3384-945C-C23D0BE443E7
   Functions: 174
-  Symbols:   832
+  Symbols:   835
   CStrings:  416
 
Symbols:
+ GCC_except_table9
+ _objc_sync_enter
+ _objc_sync_exit
Functions:
~ -[DCAnalytics sendPerformanceForCategory:eventType:] : 2472 -> 2864

```
