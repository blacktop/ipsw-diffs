## CoreRecents

> `/System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1233.100.1.0.0
-  __TEXT.__text: 0xc5fc
-  __TEXT.__objc_methlist: 0x11dc
-  __TEXT.__const: 0xe8
+1234.100.1.0.0
+  __TEXT.__text: 0xc63c
+  __TEXT.__objc_methlist: 0x11f4
+  __TEXT.__const: 0xf0
   __TEXT.__cstring: 0x9e9
-  __TEXT.__oslogstring: 0x7e8
-  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__oslogstring: 0x827
+  __TEXT.__gcc_except_tab: 0x15c
   __TEXT.__unwind_info: 0x4c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb88
+  __DATA_CONST.__objc_selrefs: 0xb98
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__got: 0x1a0
   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__cfstring: 0xd40
-  __AUTH_CONST.__objc_const: 0x1800
+  __AUTH_CONST.__objc_const: 0x1830
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_ivar: 0xa8
   __DATA.__data: 0x258
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 405
-  Symbols:   1099
-  CStrings:  184
+  Functions: 407
+  Symbols:   1109
+  CStrings:  185
 
Symbols:
+ -[CRRecentContactsLibraryRemoteAccess initWithConnection:searchTimeout:]
+ -[CRRecentContactsLibraryRemoteAccess searchTimeout]
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table2
+ GCC_except_table7
+ _OBJC_IVAR_$_CRRecentContactsLibraryRemoteAccess._searchTimeout
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_msgSend$initWithConnection:searchTimeout:
+ _objc_msgSend$searchTimeout
- GCC_except_table1
- GCC_except_table12
- GCC_except_table6
- GCC_except_table9
Functions:
- ___59-[CRRecentContactsLibraryRemoteAccess executeSearch:error:]_block_invoke.6
~ -[CRRecentContactsLibraryRemoteAccess executeSearch:error:] : 580 -> 648
~ ___59-[CRRecentContactsLibraryRemoteAccess executeSearch:error:]_block_invoke : 124 -> 156
~ -[CRRecentContactsLibraryRemoteAccess initWithConnection:] : 124 -> 8
+ -[CRRecentContactsLibraryRemoteAccess initWithConnection:searchTimeout:]
+ -[CRRecentContactsLibraryRemoteAccess searchTimeout]
+ -[CRRecentContactsLibraryRemoteAccess executeSearch:error:].cold.1
CStrings:
+ "Timed out after %.1fs waiting for recentsd to service a search"
```
