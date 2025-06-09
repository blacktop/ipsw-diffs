## DADaemonSupport

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport`

```diff

-2673.6.1.0.0
-  __TEXT.__text: 0x37cb4
+2690.0.0.0.0
+  __TEXT.__text: 0x37f9c
   __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x256c
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x880
+  __TEXT.__objc_methlist: 0x2574
+  __TEXT.__const: 0x112
+  __TEXT.__gcc_except_tab: 0x844
   __TEXT.__oslogstring: 0x6463
-  __TEXT.__cstring: 0x13b9
-  __TEXT.__unwind_info: 0xb40
+  __TEXT.__cstring: 0x13bb
+  __TEXT.__unwind_info: 0xb38
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x6f3
-  __TEXT.__objc_methname: 0x7e79
-  __TEXT.__objc_methtype: 0x1205
+  __TEXT.__objc_classname: 0x6f5
+  __TEXT.__objc_methname: 0x7e2a
+  __TEXT.__objc_methtype: 0x1203
   __TEXT.__objc_stubs: 0x6be0
   __DATA_CONST.__got: 0xb40
-  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__const: 0x8c8
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8

   __AUTH_CONST.__auth_got: 0x6a8
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0xe60
-  __AUTH_CONST.__objc_const: 0x5aa0
+  __AUTH_CONST.__objc_const: 0x5b20
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x288
+  __DATA.__objc_ivar: 0x290
   __DATA.__data: 0x8a8
   __DATA.__bss: 0x74
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x80
-  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__common: 0x14
   - /AppleInternal/Library/Frameworks/CalDAVServerSimulator.framework/CalDAVServerSimulator
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 42F042BB-5EF5-3BA1-8938-3541F2953B69
-  Functions: 940
-  Symbols:   4015
-  CStrings:  2134
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: 297B16D5-B81E-376B-BBEE-B24114EC0CC4
+  Functions: 941
+  Symbols:   4041
+  CStrings:  2135
 
Symbols:
+ -[DADClientAccountTimers init]
+ _OBJC_IVAR_$_DADClient._accountTimersLock
+ _OBJC_IVAR_$_DADClientAccountTimers._lock
+ __OBJC_$_CLASS_PROP_LIST_DARefreshManager
+ __OBJC_$_PROP_LIST_DABabysittable
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_DADaemonSupport
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_DADaemonSupport
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_DADaemonSupport
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_DADaemonSupport
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_DADaemonSupport
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_DADaemonSupport
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_DADaemonSupport
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DADaemonSupport
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DADaemonSupport
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DADaemonSupport
- GCC_except_table120
CStrings:
+ "B32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
+ "C"
+ "MobileCalDAVDAAccount"
+ "T@\"DARefreshManager\",R"
+ "T@\"NSDate\",&,N"
+ "_accountTimersLock"
+ "{"
- "B32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16@24"
- "MobileCalDAVAccount"
- "T@\"NSDate\",&,N,V_lastAllFolderContentsRequestDate"
- "T@\"NSDate\",&,N,V_lastFolderListRequestDate"
- "T@\"NSDate\",&,N,V_lastFolderWipeRequestDate"
- "k"

```
