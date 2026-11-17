## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

```diff

-5027.2.4.0.0
-  __TEXT.__text: 0x1cd944
+5027.2.9.0.0
+  __TEXT.__text: 0x1cdd0c
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x7b2c
   __TEXT.__const: 0x1a7d30
   __TEXT.__oslogstring: 0x59f1
-  __TEXT.__cstring: 0x14b3fe
-  __TEXT.__gcc_except_tab: 0x5e58
+  __TEXT.__cstring: 0x14b445
+  __TEXT.__gcc_except_tab: 0x5e5c
   __TEXT.__ustring: 0x48a
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x652
-  __TEXT.__unwind_info: 0x7dd8
+  __TEXT.__unwind_info: 0x7de0
   __TEXT.__eh_frame: 0x3f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3c89e8
+  __DATA_CONST.__const: 0x3c89f0
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_arraydata: 0x16f0
   __DATA_CONST.__got: 0x4b0
   __AUTH_CONST.__const: 0x4d48
-  __AUTH_CONST.__cfstring: 0x140da0
+  __AUTH_CONST.__cfstring: 0x140dc0
   __AUTH_CONST.__objc_const: 0x9c18
   __AUTH_CONST.__const_cfobj2: 0x40
   __AUTH_CONST.__objc_dictobj: 0x7f8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1908
+  __AUTH_CONST.__auth_got: 0x1910
   __AUTH.__objc_data: 0xa50
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x544

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8642
-  Symbols:   11486
-  CStrings:  44303
+  Functions: 8641
+  Symbols:   11489
+  CStrings:  44305
 
Symbols:
+ ___CFStackBufferHandleOutOfMemory
+ ___CFUserNotificationMachPortLock
+ _os_unfair_recursive_lock_lock
Functions:
~ _OUTLINED_FUNCTION_4 : 36 -> 16
- _OUTLINED_FUNCTION_4
~ __CFBundleCopyFindResources : 2620 -> 2664
~ __copyResourceURLsFromBundle : 1828 -> 1916
~ -[CFPDSource openActualPath] : 324 -> 424
~ -[CFPDSource acceptMessage:populatingReply:] : 3996 -> 4096
~ __CFBundleCreateMutableArrayOfFallbackLanguages : 564 -> 504
~ ___CFDateFormatterDeallocate : 784 -> 788
~ _findCFBurstTrieMappedPage : 632 -> 732
~ _findCFBurstTrieCompactMappedLevel : 472 -> 516
~ ___writeObject15 : 2668 -> 2884
~ _findCFBurstTrieMappedLevel : 368 -> 332
~ _CFPlugInInstanceCreate : 872 -> 868
- ___writeObject15.cold.9
~ ___CFUserNotificationDeallocate : 132 -> 156
~ __CFUserNotificationMachPortCallBack : 204 -> 316
~ ____InitializeDiskArbitrationKeys_block_invoke : 140 -> 148
~ _traverseCFBurstTrieMappedLevel : 408 -> 464
~ _traverseCFBurstTrieCompactMappedLevel : 444 -> 568
+ ___CFStackBufferHandleOutOfMemory
~ __copyResourceURLsFromBundle.cold.1 : 100 -> 60
+ __CFBundleCreateMutableArrayOfFallbackLanguages.cold.1
~ ___writeObject15.cold.5 : 76 -> 108
- ___writeObject15.cold.8
CStrings:
+ "/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration"
+ "/usr/libexec/secd"
+ "Attempt to temporarily allocate memory failed"
- "/System/Library/Frameworks/DiskArbitration.framework/DiskArbitration"
```
