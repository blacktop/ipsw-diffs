## EnforcementService

> `/System/Library/Frameworks/AppTrackingTransparency.framework/XPCServices/EnforcementService.xpc/EnforcementService`

```diff

-104.0.0.0.0
-  __TEXT.__text: 0x142c
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_stubs: 0x680
-  __TEXT.__objc_methlist: 0x25c
-  __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__cstring: 0x21a
-  __TEXT.__oslogstring: 0x1ef
+106.1.1.0.0
+  __TEXT.__text: 0x168c
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_stubs: 0x640
+  __TEXT.__objc_methlist: 0x244
+  __TEXT.__const: 0x38
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__cstring: 0x23c
+  __TEXT.__oslogstring: 0x1de
   __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methtype: 0x183
-  __TEXT.__objc_methname: 0x62a
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0xa0
+  __TEXT.__objc_methtype: 0x17b
+  __TEXT.__objc_methname: 0x5cf
+  __TEXT.__unwind_info: 0xd8
+  __DATA_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA.__objc_const: 0x730
-  __DATA.__objc_selrefs: 0x258
+  __DATA.__objc_selrefs: 0x248
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
   __DATA.__bss: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 572A33F1-E6FE-3F9F-B9A3-4F6CFAA0E340
-  Functions: 25
-  Symbols:   93
-  CStrings:  165
+  UUID: 650E33CC-FEB4-334E-B4A0-13B549C23760
+  Functions: 26
+  Symbols:   104
+  CStrings:  164
 
Symbols:
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x27
CStrings:
+ "%@: Bag fetch complete. Updating keychain."
+ "%@: Error getting 'AppTrackingTransparencyEnforcementReason': %@"
+ "%@: Error getting 'IsAppTrackingTransparencyEnforced': %@"
+ "startOfDayForDate:"
+ "v28@?0@\"NSNumber\"8B16@\"NSError\"20"
+ "valueWithCompletion:"
- "%@: Unable to get the 'AppTrackingTransparencyEnforcementReason' value from the bag. Error: %@"
- "%@: Unable to get the 'IsAppTrackingTransparencyEnforced' value from the bag. Error: %@"
- "appTrackingTransparencyEnforcementReason"
- "isAppTrackingTransparencyEnforced"
- "q16@0:8"
- "rangeOfUnit:startDate:interval:forDate:"
- "valueWithError:"

```
