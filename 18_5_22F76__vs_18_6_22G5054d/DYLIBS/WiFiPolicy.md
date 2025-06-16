## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-990.3.0.0.0
-  __TEXT.__text: 0xb92c8
+992.1.0.0.0
+  __TEXT.__text: 0xb95fc
   __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0x110e8
+  __TEXT.__objc_methlist: 0x11108
   __TEXT.__const: 0x638
-  __TEXT.__cstring: 0x1c060
-  __TEXT.__oslogstring: 0x3ac3
+  __TEXT.__cstring: 0x1c06c
+  __TEXT.__oslogstring: 0x3b16
   __TEXT.__gcc_except_tab: 0x18f0
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x20d0
+  __TEXT.__unwind_info: 0x20d8
   __TEXT.__objc_classname: 0x137b
-  __TEXT.__objc_methname: 0x31984
+  __TEXT.__objc_methname: 0x319e8
   __TEXT.__objc_methtype: 0x3a26
-  __TEXT.__objc_stubs: 0x180e0
+  __TEXT.__objc_stubs: 0x18120
   __DATA_CONST.__got: 0xa40
   __DATA_CONST.__const: 0x21d8
   __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9760
+  __DATA_CONST.__objc_selrefs: 0x9778
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0xa58
   __AUTH_CONST.__auth_got: 0xb10
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x187c0
-  __AUTH_CONST.__objc_const: 0x20b10
+  __AUTH_CONST.__cfstring: 0x187a0
+  __AUTH_CONST.__objc_const: 0x20b40
   __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x2098
+  __DATA.__objc_ivar: 0x209c
   __DATA.__data: 0x1bc0
   __DATA.__bss: 0x22
   __DATA_DIRTY.__objc_data: 0x2a80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FB50022-2DBD-3ADE-9896-3641E3F61FBC
-  Functions: 6014
-  Symbols:   19652
-  CStrings:  16306
+  UUID: 0C567C44-6AEE-307A-930B-88C3765AAE3A
+  Functions: 6017
+  Symbols:   19661
+  CStrings:  16313
 
Symbols:
+ -[WiFiUsageMonitor cachedFaults]
+ -[WiFiUsageMonitor processCachedFaults]
+ -[WiFiUsageMonitor setCachedFaults:]
+ GCC_except_table225
+ _OBJC_IVAR_$_WiFiUsageMonitor._cachedFaults
+ _objc_msgSend$cachedFaults
+ _objc_msgSend$processCachedFaults
- GCC_except_table224
CStrings:
+ "%s: Appended to in-memory cache (%lu %f.0sec)"
+ "%s: Processing in-memory cache (%lu)"
+ "-[WiFiUsageMonitor processCachedFaults]"
+ "-[WiFiUsageMonitor sendFaultToDB:]"
+ "T@\"NSMutableArray\",&,V_cachedFaults"
+ "_cachedFaults"
+ "cachedFaults"
+ "processCachedFaults"
+ "setCachedFaults:"
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"

```
