## AppleProxServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter`

```diff

-44.4.0.0.0
-  __TEXT.__text: 0x8c50
+44.5.0.0.0
+  __TEXT.__text: 0x9038
   __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_stubs: 0xc80
+  __TEXT.__objc_stubs: 0xcc0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x8bc
-  __TEXT.__gcc_except_tab: 0xad0
+  __TEXT.__objc_methlist: 0x8f4
+  __TEXT.__gcc_except_tab: 0xae8
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0xe07
-  __TEXT.__oslogstring: 0x9f5
-  __TEXT.__objc_methname: 0x14ad
-  __TEXT.__objc_classname: 0xad
-  __TEXT.__objc_methtype: 0x609
+  __TEXT.__cstring: 0xe27
+  __TEXT.__oslogstring: 0xa35
+  __TEXT.__objc_methname: 0x1595
+  __TEXT.__objc_classname: 0xae
+  __TEXT.__objc_methtype: 0x66f
   __TEXT.__swift5_typeref: 0xb2
   __TEXT.__constg_swiftt: 0x194
   __TEXT.__swift5_reflstr: 0x60

   __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__const: 0x198
-  __DATA_CONST.__cfstring: 0x1360
+  __DATA_CONST.__cfstring: 0x13a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xdd0
-  __DATA.__objc_selrefs: 0x618
-  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_const: 0xe30
+  __DATA.__objc_selrefs: 0x648
+  __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x200
   __DATA.__data: 0x310
   __DATA.__bss: 0x1d0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 238
+  Functions: 243
   Symbols:   181
-  CStrings:  619
+  CStrings:  636
 
Symbols:
+ _SBUserNotificationDontDismissOnUnlock
+ _objc_retain_x26
- _SBUserNotificationDismissOnLock
- _objc_retain_x22
CStrings:
+ "!\x12\x91"
+ "Active stats received: duration %u s, pearl60Hz %u msec"
+ "T@\"NSDate\",&,N,V_lastActiveStatsDate"
+ "T{?=CII},N,V_lastActiveStats"
+ "_lastActiveStats"
+ "_lastActiveStatsDate"
+ "handleActiveStatsReport:"
+ "lastActiveStats"
+ "lastActiveStatsDate"
+ "pearl_60hz"
+ "pearl_60hz_time_msec"
+ "setLastActiveStats:"
+ "setLastActiveStatsDate:"
+ "timeIntervalSinceDate:"
+ "v24@0:8r^{?=CII}16"
+ "v25@0:8{?=CII}16"
+ "{?=\"reportID\"C\"activeTimeSec\"I\"pearl60HzTimeMsec\"I}"
+ "{?=CII}16@0:8"
- "!\x12"

```
