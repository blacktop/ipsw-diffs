## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/Versions/A/MultitouchSupport`

```diff

-8420.1.0.0.0
-  __TEXT.__text: 0x1c8fc
+8440.1.0.0.0
+  __TEXT.__text: 0x1cebc
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0xd4
-  __TEXT.__const: 0x2040
+  __TEXT.__objc_methlist: 0x23c
+  __TEXT.__const: 0x2010
   __TEXT.__cstring: 0x16c3
-  __TEXT.__oslogstring: 0xe24
+  __TEXT.__oslogstring: 0xe08
   __TEXT.__tpad_act_plist: 0x20c4c
-  __TEXT.__unwind_info: 0x690
-  __TEXT.__eh_frame: 0x50
+  __TEXT.__unwind_info: 0x6a0
   __TEXT.__objc_classname: 0x3a
   __TEXT.__objc_methname: 0x51d
   __TEXT.__objc_methtype: 0x56d
   __TEXT.__objc_stubs: 0x3c0
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x158
+  __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__const: 0x250
   __AUTH_CONST.__cfstring: 0x1160
-  __AUTH_CONST.__objc_const: 0x9c8
+  __AUTH_CONST.__objc_const: 0x738
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 68841138-333A-3FB8-8C94-DBD92C95253C
-  Functions: 634
-  Symbols:   971
-  CStrings:  584
+  UUID: 34BE12A5-0E61-3222-90DC-5293C61925C0
+  Functions: 637
+  Symbols:   985
+  CStrings:  583
 
Symbols:
+ -[MTBinaryFilterLegacy initFromURL:device:].cold.1
+ -[MTBinaryFilterLegacy initFromURL:device:].cold.2
+ -[MTBinaryFilterLegacy reset].cold.1
+ -[MTBinaryFilterLegacy reset].cold.2
+ MTLoggingFramework.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __MTDeviceCreateMultitouchDispatchSource_block_invoke.cold.1
+ mt_CreateBinaryFilters.cold.1
+ mt_CreateBinaryFilters.cold.2
+ mt_CreateBinaryFilters.cold.3
+ mt_CreateBinaryFilters.cold.4
+ mt_UpdateMaxPacketSize.cold.1
CStrings:
- "Invalid force sensor index\n"

```
