## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-760.19.3.1.0
-  __TEXT.__text: 0xad570
+765.6.0.0.0
+  __TEXT.__text: 0xad804
   __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_methlist: 0xf224
+  __TEXT.__objc_methlist: 0xf24c
   __TEXT.__const: 0x510
-  __TEXT.__cstring: 0x1a7a8
+  __TEXT.__cstring: 0x1a7c8
   __TEXT.__gcc_except_tab: 0x1344
   __TEXT.__oslogstring: 0x36b2
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1f74
+  __TEXT.__unwind_info: 0x200c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x1250
-  __TEXT.__objc_methname: 0x2d53c
-  __TEXT.__objc_methtype: 0x3025
-  __TEXT.__objc_stubs: 0x16680
+  __TEXT.__objc_methname: 0x2d5a2
+  __TEXT.__objc_methtype: 0x3045
+  __TEXT.__objc_stubs: 0x166c0
   __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x2008
+  __DATA_CONST.__const: 0x1fe0
   __DATA_CONST.__objc_classlist: 0x4e8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1b398
-  __DATA_CONST.__objc_selrefs: 0x8938
+  __DATA_CONST.__objc_selrefs: 0x8948
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_classrefs: 0x6f8
   __DATA_CONST.__objc_superrefs: 0x408

   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0xaf0
-  __AUTH.__objc_data: 0x780
+  __AUTH.__objc_data: 0x730
   __DATA.__objc_ivar: 0x1ddc
   __DATA.__data: 0x1a40
-  __DATA.__bss: 0x2a
-  __DATA_DIRTY.__objc_data: 0x2990
-  __DATA_DIRTY.__bss: 0x260
+  __DATA.__bss: 0x1a
+  __DATA_DIRTY.__objc_data: 0x29e0
+  __DATA_DIRTY.__bss: 0x270
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1543C4FB-448A-367F-94D9-C66FDEC264AE
-  Functions: 5515
-  Symbols:   18135
-  CStrings:  15138
+  UUID: 6A61F385-F4A4-3349-B39F-69B0CBF087FE
+  Functions: 5518
+  Symbols:   18142
+  CStrings:  15142
 
Symbols:
+ -[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:]
+ -[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:completionHandler:]
+ -[WiFiUsageLinkSession joinStateDidChange:withReason:lastDisconnectReason:lastJoinFailure:andNetworkDetails:]
+ GCC_except_table39
+ GCC_except_table42
+ ___58-[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:]_block_invoke
+ ___58-[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:]_block_invoke.cold.1
+ ___76-[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:completionHandler:]_block_invoke
+ ___76-[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:completionHandler:]_block_invoke.cold.1
+ _objc_msgSend$askToLaunchTapToRadarWithMessage:timeout:
+ _objc_msgSend$askToLaunchTapToRadarWithMessage:timeout:completionHandler:
- GCC_except_table40
- ___50-[WiFiSoftError askToLaunchTapToRadarWithMessage:]_block_invoke
- ___50-[WiFiSoftError askToLaunchTapToRadarWithMessage:]_block_invoke.cold.1
- ___68-[WiFiSoftError askToLaunchTapToRadarWithMessage:completionHandler:]_block_invoke
- ___68-[WiFiSoftError askToLaunchTapToRadarWithMessage:completionHandler:]_block_invoke.cold.1
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
CStrings:
+ "%s: reached end of buffer while parsing IE %u before parsing IE content (length:%hhu IE content:(%p + %u = %p) > %p)"
+ "%s: reached end of buffer while parsing IE %u before parsing length ((%p + %lu = %p) > %p)"
+ "-[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:]_block_invoke"
+ "-[WiFiSoftError askToLaunchTapToRadarWithMessage:timeout:completionHandler:]_block_invoke"
+ "2024-01-30"
+ "2024-12-30"
+ "B32@0:8@16d24"
+ "B40@0:8@16d24@?32"
+ "askToLaunchTapToRadarWithMessage:timeout:"
+ "askToLaunchTapToRadarWithMessage:timeout:completionHandler:"
- "%s: reached end of buffer before parsing IE content (length:%lu IE content:(%p + %u = %p) > %p)"
- "%s: reached end of buffer before parsing IE length (length:%lu IE content:(%p + %lu = %p) > %p)"
- "-[WiFiSoftError askToLaunchTapToRadarWithMessage:]_block_invoke"
- "-[WiFiSoftError askToLaunchTapToRadarWithMessage:completionHandler:]_block_invoke"
- "2023-01-30"
- "2023-12-30"

```
