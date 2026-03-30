## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2418.4.13.104.0
-  __TEXT.__text: 0xbb7c8
-  __TEXT.__auth_stubs: 0x1fc0
+2418.5.3.100.0
+  __TEXT.__text: 0xbb824
+  __TEXT.__auth_stubs: 0x1fd0
   __TEXT.__objc_methlist: 0x46d4
   __TEXT.__const: 0x368
-  __TEXT.__cstring: 0x8b42
+  __TEXT.__cstring: 0x8b37
   __TEXT.__gcc_except_tab: 0x454c
   __TEXT.__oslogstring: 0xb117
   __TEXT.__dlopen_cstrs: 0x4a

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __AUTH_CONST.__auth_got: 0xff8
+  __AUTH_CONST.__auth_got: 0x1000
   __AUTH_CONST.__const: 0x1168
   __AUTH_CONST.__cfstring: 0x7660
   __AUTH_CONST.__objc_const: 0x5ae8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 42506EFF-951C-37F2-997F-BCB10A6FA964
+  UUID: 8CDD96B2-6015-36B0-8653-E80AFD048FC8
   Functions: 3092
-  Symbols:   10469
+  Symbols:   10470
   CStrings:  6140
 
Symbols:
+ _SIFetchCSRegisteredClients
Functions:
~ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:] : 7868 -> 7916
~ ___45-[SPConcreteCoreSpotlightIndexer addClients:]_block_invoke_2 : 416 -> 460
CStrings:
+ "analytics:"
- "analytics:findreports"

```
