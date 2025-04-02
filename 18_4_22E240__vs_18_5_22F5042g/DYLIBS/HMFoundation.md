## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-856.5.4.0.0
-  __TEXT.__text: 0x81440
+856.6.6.0.0
+  __TEXT.__text: 0x81628
   __TEXT.__auth_stubs: 0x1ea0
-  __TEXT.__objc_methlist: 0x74f4
-  __TEXT.__const: 0x20e0
+  __TEXT.__objc_methlist: 0x75a4
+  __TEXT.__const: 0x20e8
   __TEXT.__dlopen_cstrs: 0xf8
   __TEXT.__cstring: 0x3129
   __TEXT.__swift5_typeref: 0xb35

   __TEXT.__oslogstring: 0x3fca
   __TEXT.__gcc_except_tab: 0x1b6c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2e10
+  __TEXT.__unwind_info: 0x2da8
   __TEXT.__eh_frame: 0x2fc0
-  __TEXT.__objc_classname: 0x1089
-  __TEXT.__objc_methname: 0xbedd
-  __TEXT.__objc_methtype: 0x2654
-  __TEXT.__objc_stubs: 0x89c0
-  __DATA_CONST.__got: 0x750
+  __TEXT.__objc_classname: 0x10cd
+  __TEXT.__objc_methname: 0xbf80
+  __TEXT.__objc_methtype: 0x2682
+  __TEXT.__objc_stubs: 0x8a00
+  __DATA_CONST.__got: 0x758
   __DATA_CONST.__const: 0x1578
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x198
+  __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e90
+  __DATA_CONST.__objc_selrefs: 0x2eb0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x380
   __AUTH_CONST.__auth_got: 0xf60
   __AUTH_CONST.__auth_ptr: 0x1e8
   __AUTH_CONST.__const: 0x1ee8
   __AUTH_CONST.__cfstring: 0x4cc0
-  __AUTH_CONST.__objc_const: 0xde30
-  __AUTH.__objc_data: 0x1040
+  __AUTH_CONST.__objc_const: 0xe188
+  __AUTH.__objc_data: 0x1130
   __AUTH.__data: 0x248
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x27a8
+  __DATA.__data: 0x2868
   __DATA.__bss: 0x6c0
   __DATA_DIRTY.__objc_ivar: 0x59c
   __DATA_DIRTY.__objc_data: 0x19f0

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3350
-  Symbols:   3500
-  CStrings:  3917
+  Functions: 3357
+  Symbols:   3515
+  CStrings:  3929
 
Symbols:
+ _OBJC_CLASS_$_HMFDate
+ _OBJC_CLASS_$_HMFIDSDate
+ _OBJC_CLASS_$_HMFTimerFactory
+ _OBJC_CLASS_$_IDSCurrentServerTime
+ _OBJC_METACLASS_$_HMFDate
+ _OBJC_METACLASS_$_HMFIDSDate
+ _OBJC_METACLASS_$_HMFTimerFactory
+ _dispatch_block_perform
CStrings:
+ "@\"HMFTimer\"48@0:8d16d24q32Q40"
+ "@\"NSDate\"16@0:8"
+ "HMFDate"
+ "HMFDateProvider"
+ "HMFIDSDate"
+ "HMFTimerFactory"
+ "HMFTimerProvider"
+ "T@\"NSDate\",R,C,N"
+ "backoffTimerWithMinimumTimeInterval:maximumTimeInterval:exponentialFactor:options:"
+ "currentServerTimeInterval"
+ "sharedInstance"
+ "timeIntervalSince1970"

```
