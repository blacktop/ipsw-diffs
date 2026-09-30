## perfdiagsselfenabled

> `/usr/libexec/perfdiagsselfenabled`

```diff

-331.3.0.0.0
-  __TEXT.__text: 0xbe48
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0xe20
-  __TEXT.__objc_methlist: 0xa04
+352.0.0.0.0
+  __TEXT.__text: 0xc5ec
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_stubs: 0xe60
+  __TEXT.__objc_methlist: 0xa78
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x143d
-  __TEXT.__oslogstring: 0x1de1
-  __TEXT.__objc_classname: 0xc9
+  __TEXT.__cstring: 0x14f0
+  __TEXT.__oslogstring: 0x1eaf
+  __TEXT.__objc_classname: 0xda
   __TEXT.__objc_methtype: 0x55e
-  __TEXT.__objc_methname: 0x2fad
+  __TEXT.__objc_methname: 0x30eb
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x220
-  __DATA_CONST.__auth_got: 0x2e0
+  __TEXT.__unwind_info: 0x270
+  __DATA_CONST.__auth_got: 0x2e8
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x610
-  __DATA_CONST.__cfstring: 0x1580
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__const: 0x640
+  __DATA_CONST.__cfstring: 0x1640
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1930
-  __DATA.__objc_selrefs: 0x6f8
-  __DATA.__objc_ivar: 0x19c
-  __DATA.__objc_data: 0x320
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x1a50
+  __DATA.__objc_selrefs: 0x708
+  __DATA.__objc_ivar: 0x1a8
+  __DATA.__objc_data: 0x370
   __DATA.__data: 0x30
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 277
-  Symbols:   122
-  CStrings:  794
+  Functions: 307
+  Symbols:   123
+  CStrings:  812
 
Symbols:
+ __os_log_error_impl
CStrings:
+ "HangTracerConsecutiveHangWaitTimeoutDuration"
+ "PDSE: Enable WB client hang collection: Delete setting %@"
+ "PDSE: Enable WB client hang collection: set setting %@ to TRUE"
+ "PDSE: Enable WB client hang: set necessary settings with Self-Enablement prefix = %@"
+ "PDSEPrefWBClientHangKillSwitch"
+ "PDSEPrefWBClientHangPeriodDays"
+ "PDSEWBClientHang"
+ "PDSEWBClientHangTimeoutTimestampSec"
+ "TB,R,V_pdseWBClientHangKillSwitch"
+ "TB,R,V_shouldAugmentSentryTailspinWithSignposts"
+ "TQ,R,V_consecutiveHangWaitTimeoutDurationMSec"
+ "Ti,R,V_pdseWBClientHangPeriodDays"
+ "WBClientHangEnable"
+ "_consecutiveHangWaitTimeoutDurationMSec"
+ "_pdseWBClientHangKillSwitch"
+ "_pdseWBClientHangPeriodDays"
+ "_shouldAugmentSentryTailspinWithSignposts"
+ "consecutiveHangWaitTimeoutDurationMSec"
+ "pdseWBClientHangKillSwitch"
+ "pdseWBClientHangPeriodDays"
+ "shouldAugmentSentryTailspinWithSignposts"
+ "\xf0\xf0A!&!"
- "TB,R,V_shouldCollectOSSignpostsDeferred"
- "_shouldCollectOSSignpostsDeferred"
- "compare:"
- "shouldCollectOSSignpostsDeferred"
- "\xf0\xf0A\x11&!"

```
