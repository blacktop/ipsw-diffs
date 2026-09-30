## DataAccessExpress

> `/System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress`

```diff

-2673.6.1.0.0
-  __TEXT.__text: 0x27efc
+2690.0.0.0.0
+  __TEXT.__text: 0x27dc0
   __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x200c
-  __TEXT.__gcc_except_tab: 0xf08
-  __TEXT.__cstring: 0x35d5
+  __TEXT.__objc_methlist: 0x1ffc
+  __TEXT.__gcc_except_tab: 0xee4
+  __TEXT.__cstring: 0x35c8
   __TEXT.__const: 0xc0
-  __TEXT.__oslogstring: 0x2d9f
+  __TEXT.__oslogstring: 0x2e3c
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x950
+  __TEXT.__unwind_info: 0x940
   __TEXT.__objc_classname: 0x3a2
-  __TEXT.__objc_methname: 0x5901
+  __TEXT.__objc_methname: 0x58e9
   __TEXT.__objc_methtype: 0x6b2
-  __TEXT.__objc_stubs: 0x4260
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0xf10
+  __TEXT.__objc_stubs: 0x4240
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0xf30
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1538
+  __DATA_CONST.__objc_selrefs: 0x1530
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x5d8
-  __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x3f80
+  __AUTH_CONST.__const: 0x4e0
+  __AUTH_CONST.__cfstring: 0x3f40
   __AUTH_CONST.__objc_const: 0x4058
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48

   __DATA.__bss: 0x264
   __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x148
+  __DATA_DIRTY.__bss: 0x160
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B966C015-814C-3044-A6A2-85C3486CA895
-  Functions: 911
-  Symbols:   3733
-  CStrings:  2436
+  UUID: 0758C7ED-BBE2-3DB4-B5A7-2147DF4CDB0D
+  Functions: 909
+  Symbols:   3731
+  CStrings:  2432
 
Symbols:
+ _ACAccountTypeIdentifierCloudKit
+ ___120-[DADConnection performCalendarDirectorySearchWithAccountID:terms:recordTypes:resultLimit:resultsBlock:completionBlock:]_block_invoke.265
+ ___160-[DACPLogShared _slurpToFileUUID:slurpeeFileDescriptor:prefix:suffix:startNewFile:sizeCheck:wantsCompressed:maxLogFileCount:outDidCreateNewFile:outNewFilePath:]_block_invoke.118
+ ___44-[DACPLogShared _getUUIDForFolder:baseName:]_block_invoke.116
+ ___82-[DADConnection performGroupExpansionWithAccountID:principalPath:completionBlock:]_block_invoke.268
+ ___block_descriptor_32_e49_v16?0"<DAESubscribedCalendarDownloadDelegate>"8l
+ ___block_literal_global.137
+ ___block_literal_global.140
+ ___block_literal_global.256
- -[DAESubscriptionCalendarDownloadContext asyncCallOutToDelegate:]
- ___120-[DADConnection performCalendarDirectorySearchWithAccountID:terms:recordTypes:resultLimit:resultsBlock:completionBlock:]_block_invoke.261
- ___160-[DACPLogShared _slurpToFileUUID:slurpeeFileDescriptor:prefix:suffix:startNewFile:sizeCheck:wantsCompressed:maxLogFileCount:outDidCreateNewFile:outNewFilePath:]_block_invoke.124
- ___44-[DACPLogShared _getUUIDForFolder:baseName:]_block_invoke.122
- ___65-[DAESubscriptionCalendarDownloadContext asyncCallOutToDelegate:]_block_invoke
- ___82-[DADConnection performGroupExpansionWithAccountID:principalPath:completionBlock:]_block_invoke.266
- ___block_literal_global.143
- ___block_literal_global.146
- _objc_msgSend$asyncCallOutToDelegate:
CStrings:
+ "nil delegate given to downloadSubscribedCalendarWithURL:queue:delegate:. Failing immediately"
+ "nil queue given to downloadSubscribedCalendarWithURL:queue:delegate:. Failing immediately."
+ "nil subscription URL given to downloadSubscribedCalendarWithURL:queue:delegate:. Failing immediately."
- "Library"
- "Log folder: “%@” must begin with /Library/Logs in the user’s home directory."
- "Logs"
- "Requested path into client home directory: %@"
- "asyncCallOutToDelegate:"

```
