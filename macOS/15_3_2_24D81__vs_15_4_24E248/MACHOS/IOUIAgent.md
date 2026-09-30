## IOUIAgent

> `/System/Library/CoreServices/IOUIAgent.app/Contents/MacOS/IOUIAgent`

```diff

-56.60.2.0.0
-  __TEXT.__text: 0x19998
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x1720
-  __TEXT.__objc_methlist: 0xa48
+64.0.0.0.0
+  __TEXT.__text: 0x19f48
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_stubs: 0x1920
+  __TEXT.__objc_methlist: 0xec0
   __TEXT.__const: 0xb9
-  __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__cstring: 0x2117
-  __TEXT.__objc_methname: 0x227f
-  __TEXT.__oslogstring: 0x1065
+  __TEXT.__gcc_except_tab: 0x27c
+  __TEXT.__cstring: 0x2130
+  __TEXT.__objc_methname: 0x2413
+  __TEXT.__oslogstring: 0x11c8
   __TEXT.__ustring: 0x18
-  __TEXT.__objc_classname: 0x126
-  __TEXT.__objc_methtype: 0x735
-  __TEXT.__unwind_info: 0x4c8
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x130
+  __TEXT.__objc_classname: 0x130
+  __TEXT.__objc_methtype: 0x741
+  __TEXT.__unwind_info: 0x510
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__cfstring: 0x7c0
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__cfstring: 0x7e0
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x26e8
-  __DATA.__objc_selrefs: 0x6e0
-  __DATA.__objc_ivar: 0x10c
-  __DATA.__objc_data: 0x320
+  __DATA.__objc_const: 0x2100
+  __DATA.__objc_selrefs: 0x958
+  __DATA.__objc_ivar: 0x114
+  __DATA.__objc_data: 0x370
   __DATA.__data: 0x1e2
-  __DATA.__bss: 0x4d
+  __DATA.__bss: 0x65
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F074BAF9-790D-3087-B0EC-BCEDA6CB13C4
-  Functions: 510
-  Symbols:   144
-  CStrings:  928
+  UUID: 05017C46-1FAC-357C-B13E-52BB0AEA496B
+  Functions: 649
+  Symbols:   154
+  CStrings:  965
 
Symbols:
+ _NSDefaultRunLoopMode
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSPort
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSThread
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCFUserNotificationAlertTopMostKey
+ _objc_sync_enter
+ _objc_sync_exit
- _CFRunLoopGetMain
- __dispatch_main_q
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "@\"IOThread\""
+ "CFUserNotificationCreate() failed! (error: %d)"
+ "Decremented class count! (sClassCount: %lu)"
+ "Flushed run loop!"
+ "IOThread"
+ "Incremented class count! (sClassCount: %lu)"
+ "Initializing thread..."
+ "Last instance deallocated! Setting timer for %lu seconds..."
+ "No instances of %@ allocated, releasing thread..."
+ "Starting run loop..."
+ "Starting thread..."
+ "Still an instance of %@ allocated, not releasing thread! (sClassCount: %lu)"
+ "T@\"IOThread\",&,N,V_thread"
+ "T@\"NSRunLoop\",R,N"
+ "TB,N,V_shouldDisplayOnTop"
+ "TQ,R,N"
+ "_shouldDisplayOnTop"
+ "_thread"
+ "addPort:forMode:"
+ "cancel"
+ "classCount"
+ "currentRunLoop"
+ "decrementClassCount"
+ "dictionaryWithObjects:forKeys:count:"
+ "dispatchAsync:"
+ "dispatchSync:"
+ "getCFRunLoop"
+ "incrementClassCount"
+ "initWithBlock:"
+ "initializeThread"
+ "numberWithBool:"
+ "performBlock:"
+ "runLoop"
+ "setShouldDisplayOnTop:"
+ "setThread:"
+ "shouldDisplayOnTop"
+ "thread"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "UserNotificationQueue"

```
