## CoreRecents

> `/System/Library/PrivateFrameworks/CoreRecents.framework/Versions/A/CoreRecents`

```diff

-1233.100.1.0.0
-  __TEXT.__text: 0xd4f4
-  __TEXT.__objc_methlist: 0x11dc
-  __TEXT.__const: 0xf0
+1234.100.1.0.0
+  __TEXT.__text: 0xd5dc
+  __TEXT.__objc_methlist: 0x11f4
+  __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x9df
-  __TEXT.__oslogstring: 0x7e8
-  __TEXT.__gcc_except_tab: 0x150
-  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__oslogstring: 0x827
+  __TEXT.__gcc_except_tab: 0x15c
+  __TEXT.__unwind_info: 0x4a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb88
+  __DATA_CONST.__objc_selrefs: 0xb98
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__got: 0x1a0
-  __AUTH_CONST.__const: 0x700
+  __AUTH_CONST.__const: 0x730
   __AUTH_CONST.__cfstring: 0xd40
-  __AUTH_CONST.__objc_const: 0x1800
+  __AUTH_CONST.__objc_const: 0x1830
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_ivar: 0xa8
   __DATA.__data: 0x258
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 425
-  Symbols:   1102
-  CStrings:  184
+  Functions: 429
+  Symbols:   1113
+  CStrings:  185
 
Symbols:
+ -[CRRecentContactsLibraryRemoteAccess initWithConnection:searchTimeout:]
+ -[CRRecentContactsLibraryRemoteAccess searchTimeout]
+ GCC_except_table14
+ GCC_except_table17
+ GCC_except_table2
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table38
+ GCC_except_table9
+ OBJC_IVAR_$_CRRecentContactsLibraryRemoteAccess._searchTimeout
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16l
+ ___copy_helper_block_e8_32s40r48r
+ ___destroy_helper_block_e8_32s40r48r
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_msgSend$initWithConnection:searchTimeout:
+ _objc_msgSend$searchTimeout
- GCC_except_table1
- GCC_except_table13
- GCC_except_table16
- GCC_except_table24
- GCC_except_table27
- GCC_except_table36
- GCC_except_table8
- __59-[CRRecentContactsLibraryRemoteAccess executeSearch:error:]_block_invoke
CStrings:
+ "Timed out after %.1fs waiting for recentsd to service a search"
```
