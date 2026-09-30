## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-426.0.0.0.0
-  __TEXT.__text: 0x17a28
+430.0.0.0.0
+  __TEXT.__text: 0x17ab0
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0xb6c
-  __TEXT.__const: 0x288
+  __TEXT.__objc_methlist: 0xb74
+  __TEXT.__const: 0x258
   __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__cstring: 0x469d
+  __TEXT.__cstring: 0x4697
   __TEXT.__oslogstring: 0x2d1c
   __TEXT.__ustring: 0xe0
   __TEXT.__unwind_info: 0x858

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1890
+  __DATA_CONST.__const: 0x1898
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb48
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__got: 0x1f8
-  __AUTH_CONST.__const: 0x5c0
+  __AUTH_CONST.__const: 0x5a0
   __AUTH_CONST.__cfstring: 0x5d20
   __AUTH_CONST.__objc_const: 0x1cb8
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__auth_got: 0x628
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x1f4
   __DATA.__data: 0x30c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 606
-  Symbols:   1570
+  Functions: 607
+  Symbols:   1572
   CStrings:  1012
 
Symbols:
+ -[HTPrefs allTaskingPrefNames]
+ GCC_except_table40
+ _CFPreferencesCopyMultiple
+ ___NSDictionary0__struct
+ __isBlockedWidgetRendererBundleID
+ _defaultsTextForDomain
+ _kHTExtendedAttributeEventEnd
+ _kHTExtendedAttributeEventStart
+ _kHTExtendedAttributeEventType
+ _objc_opt_new
- GCC_except_table39
- _HTCPURoleMonitoringDenylist.denylist
- _HTCPURoleMonitoringDenylist.onceToken
- _OBJC_CLASS_$_NSSet
- ___HTCPURoleMonitoringDenylist_block_invoke
- _kHTExtendedAttributeHangEnd
- _kHTExtendedAttributeHangStart
- _objc_msgSend$setWithObjects:
CStrings:
+ "com.apple.chrono.WidgetRenderer-"
+ "hangtracer.event_end"
+ "hangtracer.event_start"
+ "hangtracer.event_type"
- "WidgetRenderer-Default"
- "com.apple.chrono.WidgetRenderer-Default"
- "hangtracer.hang_end"
- "hangtracer.hang_start"
```
