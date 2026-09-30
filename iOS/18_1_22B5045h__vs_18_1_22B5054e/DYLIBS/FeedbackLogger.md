## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger`

```diff

-3401.11.1.0.0
-  __TEXT.__text: 0x1f33c
-  __TEXT.__auth_stubs: 0xf20
+3401.17.1.0.0
+  __TEXT.__text: 0x1f328
+  __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_methlist: 0xfa8
   __TEXT.__cstring: 0x22cf
   __TEXT.__swift5_typeref: 0x3f7

   __TEXT.__swift5_reflstr: 0x23f
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__gcc_except_tab: 0x26c
-  __TEXT.__unwind_info: 0xa40
+  __TEXT.__unwind_info: 0xa38
   __TEXT.__eh_frame: 0x5a8
   __TEXT.__objc_classname: 0x135
   __TEXT.__objc_methname: 0x2fa4

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x7a0
+  __AUTH_CONST.__auth_got: 0x798
   __AUTH_CONST.__auth_ptr: 0x1c0
   __AUTH_CONST.__const: 0x5c0
   __AUTH_CONST.__cfstring: 0x8a0

   __DATA.__objc_ivar: 0x130
   __DATA.__data: 0x4f8
   __DATA.__common: 0x110
-  __DATA.__bss: 0x2088
+  __DATA.__bss: 0x2080
   __DATA_DIRTY.__objc_data: 0x470
   __DATA_DIRTY.__data: 0x468
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x60
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 930
-  Symbols:   686
+  Symbols:   685
   CStrings:  979
 
Symbols:
- _MKBDeviceUnlockedSinceBoot
CStrings:
+ "SELECT batchId FROM batchStatus WHERE status=? ORDER BY rowid ASC LIMIT 4096;"
- "SELECT batchId FROM batchStatus WHERE status=? ORDER BY rowid ASC LIMIT 1024;"

```
