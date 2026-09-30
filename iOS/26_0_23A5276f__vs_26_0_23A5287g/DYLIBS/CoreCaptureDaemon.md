## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1301.70.0.0.0
-  __TEXT.__text: 0x402ec
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__const: 0x4f0
-  __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__oslogstring: 0x729e
-  __TEXT.__cstring: 0x86a5
-  __TEXT.__unwind_info: 0x618
+1301.74.0.0.0
+  __TEXT.__text: 0x4073c
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__const: 0x500
+  __TEXT.__gcc_except_tab: 0x268
+  __TEXT.__oslogstring: 0x73c2
+  __TEXT.__cstring: 0x87e8
+  __TEXT.__unwind_info: 0x600
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x107
   __TEXT.__objc_stubs: 0x180
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__const: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__auth_got: 0x8c0
   __AUTH_CONST.__const: 0x1088
   __AUTH_CONST.__cfstring: 0xa00
   __DATA.__data: 0x1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E1E87E24-D6C8-34FA-AEC4-487B10E07959
-  Functions: 499
-  Symbols:   1063
-  CStrings:  1334
+  UUID: 3D338067-68C0-3F73-8626-8184A752F096
+  Functions: 500
+  Symbols:   1077
+  CStrings:  1335
 
Symbols:
+ GCC_except_table265
+ GCC_except_table364
+ GCC_except_table365
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table370
+ GCC_except_table431
+ GCC_except_table495
+ __ZNSt3__115recursive_mutex4lockEv
+ __ZNSt3__115recursive_mutex6unlockEv
+ __ZNSt3__115recursive_mutexC1Ev
+ __ZNSt3__115recursive_mutexD1Ev
+ ____ZN16CCServiceMonitor6ccfreeEv_block_invoke
+ ___block_descriptor_tmp.1692
+ ___block_descriptor_tmp.1756
+ ___block_descriptor_tmp.1849
+ ___block_descriptor_tmp.2105
+ ___block_descriptor_tmp.2224
+ ___block_literal_global.1754
+ ___block_literal_global.2063
+ _os_variant_uses_ephemeral_storage
- GCC_except_table430
- GCC_except_table494
- ___block_descriptor_tmp.1754
- ___block_descriptor_tmp.1846
- ___block_descriptor_tmp.2102
- ___block_descriptor_tmp.2221
- ___block_literal_global.1752
- ___block_literal_global.2060
CStrings:
+ "CCLogTap::pipeEvent EXIT Event Count - Empty (%d) Reserved (%d) Written (%d) Padding (%d) Capture (%d) Skip (%d),prevread offset %u, new read offset %u, prev seq %u, expected seq %u entry %u, ring state readoff %u, write offset %u\n"
+ "Received Capture Event %u\n"
+ "Received Skip Event %u\n"
+ "com.apple.MobileSoftwareUpdate"
+ "previous and current sequence numbers are same %u prev read offset %u,new read ofsset %u, previous write offset %u, new write offset %u, entry %u\n"
+ "previous and current sequence numbers are same %u prev read offset %u,previous write offset %u, new write offset %u, entry %u\n"
- "CCLogTap::pipeEvent EXIT readOffset : %d entry:%u\n"
- "CCLogTap::pipeEvent Event Count - Empty (%d) Reserved (%d) Written (%d) Padding (%d) Capture (%d) Skip (%d)\n"
- "Received Capture Event\n"
- "Received Skip Event\n"
- "previous and current sequence numbers are same %u entry %u\n"

```
