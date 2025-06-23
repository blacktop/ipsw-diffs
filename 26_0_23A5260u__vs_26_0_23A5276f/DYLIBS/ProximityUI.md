## ProximityUI

> `/System/Library/PrivateFrameworks/ProximityUI.framework/ProximityUI`

```diff

-502.0.0.0.0
-  __TEXT.__text: 0x33124
+505.0.3.0.0
+  __TEXT.__text: 0x33530
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x1fd0
+  __TEXT.__objc_methlist: 0x2010
   __TEXT.__const: 0x6a0
-  __TEXT.__gcc_except_tab: 0x4f14
-  __TEXT.__cstring: 0x181e
-  __TEXT.__oslogstring: 0x33e4
-  __TEXT.__unwind_info: 0x1190
+  __TEXT.__gcc_except_tab: 0x4fc4
+  __TEXT.__cstring: 0x1826
+  __TEXT.__oslogstring: 0x3447
+  __TEXT.__unwind_info: 0x1198
   __TEXT.__objc_classname: 0x25b
-  __TEXT.__objc_methname: 0x4ac6
-  __TEXT.__objc_methtype: 0x10a7
-  __TEXT.__objc_stubs: 0x3de0
+  __TEXT.__objc_methname: 0x4bda
+  __TEXT.__objc_methtype: 0x10b1
+  __TEXT.__objc_stubs: 0x3ee0
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11c0
+  __DATA_CONST.__objc_selrefs: 0x1200
   __DATA_CONST.__objc_superrefs: 0xa0
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x5f8
-  __AUTH_CONST.__cfstring: 0x1160
-  __AUTH_CONST.__objc_const: 0x3ff8
+  __AUTH_CONST.__cfstring: 0x1180
+  __AUTH_CONST.__objc_const: 0x4058
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x33c
+  __DATA.__objc_ivar: 0x344
   __DATA.__data: 0x318
   __DATA.__bss: 0x48
   - /System/Library/Frameworks/ARKit.framework/ARKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 287DD10A-DEBE-3377-B256-8A00DA06E70A
-  Functions: 1071
-  Symbols:   3732
-  CStrings:  1671
+  UUID: 58A8C2AD-EFD3-3B92-A85C-DDE621E7CAEB
+  Functions: 1076
+  Symbols:   3753
+  CStrings:  1688
 
Symbols:
+ -[PRItemLocalizer recordUsage]
+ -[PRItemLocalizer setUsageFirstRange:]
+ -[PRItemLocalizer setUsageStartTimestamp:]
+ -[PRItemLocalizer usageFirstRange]
+ -[PRItemLocalizer usageStartTimestamp]
+ GCC_except_table124
+ GCC_except_table52
+ GCC_except_table60
+ _OBJC_IVAR_$_PRItemLocalizer._usageFirstRange
+ _OBJC_IVAR_$_PRItemLocalizer._usageStartTimestamp
+ ___42-[PRItemLocalizer didReceiveNewSolutions:]_block_invoke.86
+ ___block_literal_global.59
+ ___block_literal_global.83
+ _objc_msgSend$now
+ _objc_msgSend$recordUsage
+ _objc_msgSend$recordUsageOfCompanionRanging:usageParameters:
+ _objc_msgSend$setUsageFirstRange:
+ _objc_msgSend$setUsageStartTimestamp:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$usageFirstRange
+ _objc_msgSend$usageStartTimestamp
- GCC_except_table119
- GCC_except_table53
- ___42-[PRItemLocalizer didReceiveNewSolutions:]_block_invoke.73
- ___block_literal_global.46
- ___block_literal_global.70
CStrings:
+ "@\"NSDate\""
+ "Record usage: first range %0.1f m, session duration %0.1f s"
+ "Record usage: skipping, no first range"
+ "T@\"NSDate\",&,N,V_usageStartTimestamp"
+ "T@\"NSNumber\",&,N,V_usageFirstRange"
+ "UNKNOWN"
+ "_usageFirstRange"
+ "_usageStartTimestamp"
+ "now"
+ "recordUsage"
+ "recordUsageOfCompanionRanging:usageParameters:"
+ "setUsageFirstRange:"
+ "setUsageStartTimestamp:"
+ "timeIntervalSinceDate:"
+ "usageFirstRange"
+ "usageStartTimestamp"

```
