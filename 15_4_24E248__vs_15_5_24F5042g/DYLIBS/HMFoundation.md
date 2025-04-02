## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation`

```diff

-856.5.4.0.0
-  __TEXT.__text: 0x8e330
+856.6.6.0.0
+  __TEXT.__text: 0x8e514
   __TEXT.__auth_stubs: 0x1b10
-  __TEXT.__objc_methlist: 0x72c4
-  __TEXT.__const: 0x1be0
+  __TEXT.__objc_methlist: 0x7374
+  __TEXT.__const: 0x1be8
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__cstring: 0x3010
   __TEXT.__swift5_typeref: 0xb35

   __TEXT.__oslogstring: 0x3c48
   __TEXT.__gcc_except_tab: 0x1a98
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2de0
+  __TEXT.__unwind_info: 0x2df8
   __TEXT.__eh_frame: 0x2fe8
-  __TEXT.__objc_classname: 0xfd3
-  __TEXT.__objc_methname: 0xb9ea
-  __TEXT.__objc_methtype: 0x24de
-  __TEXT.__objc_stubs: 0x8780
-  __DATA_CONST.__got: 0x730
+  __TEXT.__objc_classname: 0x1017
+  __TEXT.__objc_methname: 0xba8d
+  __TEXT.__objc_methtype: 0x250c
+  __TEXT.__objc_stubs: 0x87c0
+  __DATA_CONST.__got: 0x738
   __DATA_CONST.__const: 0x838
-  __DATA_CONST.__objc_classlist: 0x438
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x178
+  __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2df0
+  __DATA_CONST.__objc_selrefs: 0x2e10
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x378
   __AUTH_CONST.__auth_got: 0xd98
   __AUTH_CONST.__auth_ptr: 0x1e8
   __AUTH_CONST.__const: 0x2d80
   __AUTH_CONST.__cfstring: 0x4980
-  __AUTH_CONST.__objc_const: 0xd7a8
-  __AUTH.__objc_data: 0x19f0
+  __AUTH_CONST.__objc_const: 0xdb00
+  __AUTH.__objc_data: 0x1ae0
   __AUTH.__data: 0x248
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x184
-  __DATA.__data: 0x2618
+  __DATA.__data: 0x26d8
   __DATA.__bss: 0x928
   __DATA_DIRTY.__objc_ivar: 0x550
   __DATA_DIRTY.__objc_data: 0xff0

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/Versions/A/CollectionsInternal
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
+  - /System/Library/PrivateFrameworks/IDSFoundation.framework/Versions/A/IDSFoundation
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3438
-  Symbols:   6453
-  CStrings:  3808
+  Functions: 3445
+  Symbols:   6497
+  CStrings:  3820
 
Symbols:
+ -[HMFDate now]
+ -[HMFDate timeIntervalSince1970]
+ -[HMFIDSDate now]
+ -[HMFIDSDate timeIntervalSince1970]
+ -[HMFTimerFactory backoffTimerWithMinimumTimeInterval:maximumTimeInterval:exponentialFactor:options:]
+ -[HMFTimerFactory timerWithTimeInterval:options:]
+ _OBJC_CLASS_$_HMFDate
+ _OBJC_CLASS_$_HMFIDSDate
+ _OBJC_CLASS_$_HMFTimerFactory
+ _OBJC_CLASS_$_IDSCurrentServerTime
+ _OBJC_METACLASS_$_HMFDate
+ _OBJC_METACLASS_$_HMFIDSDate
+ _OBJC_METACLASS_$_HMFTimerFactory
+ __OBJC_$_INSTANCE_METHODS_HMFDate
+ __OBJC_$_INSTANCE_METHODS_HMFIDSDate
+ __OBJC_$_INSTANCE_METHODS_HMFTimerFactory
+ __OBJC_$_PROP_LIST_HMFDate
+ __OBJC_$_PROP_LIST_HMFDateProvider
+ __OBJC_$_PROP_LIST_HMFIDSDate
+ __OBJC_$_PROP_LIST_HMFTimerFactory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMFDateProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMFTimerProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMFTimerProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMFDateProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMFTimerProvider
+ __OBJC_$_PROTOCOL_REFS_HMFDateProvider
+ __OBJC_$_PROTOCOL_REFS_HMFTimerProvider
+ __OBJC_CLASS_PROTOCOLS_$_HMFDate
+ __OBJC_CLASS_PROTOCOLS_$_HMFIDSDate
+ __OBJC_CLASS_PROTOCOLS_$_HMFTimerFactory
+ __OBJC_CLASS_RO_$_HMFDate
+ __OBJC_CLASS_RO_$_HMFIDSDate
+ __OBJC_CLASS_RO_$_HMFTimerFactory
+ __OBJC_LABEL_PROTOCOL_$_HMFDateProvider
+ __OBJC_LABEL_PROTOCOL_$_HMFTimerProvider
+ __OBJC_METACLASS_RO_$_HMFDate
+ __OBJC_METACLASS_RO_$_HMFIDSDate
+ __OBJC_METACLASS_RO_$_HMFTimerFactory
+ __OBJC_PROTOCOL_$_HMFDateProvider
+ __OBJC_PROTOCOL_$_HMFTimerProvider
+ ___35-[HMFIDSDate timeIntervalSince1970]_block_invoke
+ _dispatch_block_perform
+ _objc_msgSend$currentServerTimeInterval
+ _objc_msgSend$sharedInstance
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
