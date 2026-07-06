## NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

```diff

-  __TEXT.__text: 0xf290
+  __TEXT.__text: 0xf5e8
   __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x1b0
   __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__cstring: 0x1235
+  __TEXT.__cstring: 0x1259
   __TEXT.__objc_methname: 0x15fe
-  __TEXT.__oslogstring: 0x2e6b
+  __TEXT.__oslogstring: 0x2f6f
   __TEXT.__objc_classname: 0xed
   __TEXT.__objc_methtype: 0x352
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__unwind_info: 0x310
   __DATA_CONST.__const: 0x690
-  __DATA_CONST.__cfstring: 0xa20
+  __DATA_CONST.__cfstring: 0xa60
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 251
+  Functions: 249
   Symbols:   199
-  CStrings:  827
+  CStrings:  837
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
CStrings:
+ "Failed to deregister inlineGC throughput: %@"
+ "Failed to register inlineGC throughput tracking: %@"
+ "IS High will skip lists."
+ "No new slowInlineGC this round."
+ "dLastInlineGCMiB"
+ "idlestack.inlineGC"
+ "idlestack_update_pre_round_stats - unexpected buf len %zu\n"
+ "nts_prst_log internal=%d, bootArgSet/Val=%d/%d"

```
