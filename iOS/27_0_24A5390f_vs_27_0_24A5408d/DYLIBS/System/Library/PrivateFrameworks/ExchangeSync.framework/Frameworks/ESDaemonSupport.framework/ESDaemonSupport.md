## ESDaemonSupport

> `/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/ESDaemonSupport.framework/ESDaemonSupport`

```diff

-2078.0.0.0.0
-  __TEXT.__text: 0x20f5c
-  __TEXT.__objc_methlist: 0x14e4
+2079.0.1.0.0
+  __TEXT.__text: 0x212c4
+  __TEXT.__objc_methlist: 0x14ec
   __TEXT.__const: 0xc0
-  __TEXT.__oslogstring: 0x339b
-  __TEXT.__cstring: 0x10fe
+  __TEXT.__oslogstring: 0x34c8
+  __TEXT.__cstring: 0x10ff
   __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__unwind_info: 0x698
+  __TEXT.__unwind_info: 0x6a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1270
+  __DATA_CONST.__objc_selrefs: 0x1278
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__got: 0x750
+  __DATA_CONST.__got: 0x758
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0xaa0
-  __AUTH_CONST.__objc_const: 0x2a70
+  __AUTH_CONST.__objc_const: 0x2a90
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x160
+  __DATA.__objc_ivar: 0x164
   __DATA.__data: 0x370
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 582
-  Symbols:   1789
-  CStrings:  335
+  Functions: 583
+  Symbols:   1793
+  CStrings:  338
 
Symbols:
+ +[ESDAgentManager wirelessPolicy:isMorePermissiveThanPolicy:]
+ GCC_except_table46
+ GCC_except_table69
+ _OBJC_IVAR_$_ESDAgentManager._wirelessPolicies
+ _kCTCellularDataUsagePolicyDeny
+ _objc_msgSend$activeAccountBundleIDs
+ _objc_msgSend$wirelessPolicy:isMorePermissiveThanPolicy:
- GCC_except_table45
- GCC_except_table68
- _CFDictionaryGetValue
CStrings:
+ "Received cellular data usage changed notification. Checking if a refresh is required."
+ "Refreshing account %@ because wireless data use is now allowed for %{public}@ and might not have been before."
+ "User allowed cellular or wifi data for BundleID %{public}@"
+ "Wireless data usage policy changes do not affect any existing agents; no refreshes will be done."
- "User allowed cellular-data for BundleID %{public}@"
```
