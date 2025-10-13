## BacklightServices

> `/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`

```diff

-5.1.7.0.0
-  __TEXT.__text: 0x2872c
+5.1.8.0.0
+  __TEXT.__text: 0x28748
   __TEXT.__auth_stubs: 0x9a0
   __TEXT.__objc_methlist: 0x3344
   __TEXT.__const: 0x1b8

   __TEXT.__cstring: 0x19e1
   __TEXT.__ustring: 0xf4
   __TEXT.__gcc_except_tab: 0xe0c
-  __TEXT.__unwind_info: 0xfc8
+  __TEXT.__unwind_info: 0xfd0
   __TEXT.__objc_classname: 0x108e
-  __TEXT.__objc_methname: 0x5f93
+  __TEXT.__objc_methname: 0x5f94
   __TEXT.__objc_methtype: 0x1249
   __TEXT.__objc_stubs: 0x3de0
   __DATA_CONST.__got: 0x3e8

   __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0x2a8
   __DATA.__data: 0xba8
-  __DATA.__bss: 0xd9
+  __DATA.__bss: 0xf9
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 649043FB-4FE8-369C-A2E5-BFD6F85202B4
+  UUID: C3ACDC42-0FA1-3877-B97C-1F921EF2562E
   Functions: 1214
-  Symbols:   4461
+  Symbols:   4465
   CStrings:  2077
 
Symbols:
+ _bls_loggingString.distantFutureCache
+ _bls_loggingString.distantPastCache
+ _bls_shortLoggingString.distantFutureCache
+ _bls_shortLoggingString.distantPastCache
+ _objc_msgSend$stringFromTimeInterval:
- _objc_msgSend$stringFromDate:toDate:
Functions:
~ -[NSDate(BacklightServices) bls_loggingString] : 384 -> 328
~ -[NSDate(BacklightServices) bls_shortLoggingString] : 208 -> 156
~ ___46-[NSDate(BacklightServices) bls_loggingString]_block_invoke : 192 -> 260
~ ___51-[NSDate(BacklightServices) bls_shortLoggingString]_block_invoke : 140 -> 208
CStrings:
+ "stringFromTimeInterval:"
- "stringFromDate:toDate:"

```
