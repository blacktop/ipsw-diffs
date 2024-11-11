## AppDeletionUIHost

> `/Applications/AppDeletionUIHost.app/AppDeletionUIHost`

```diff

-631.60.47.0.0
-  __TEXT.__text: 0x38fc
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x1460
-  __TEXT.__objc_methlist: 0x2d4
-  __TEXT.__const: 0x9c
-  __TEXT.__cstring: 0xcff
-  __TEXT.__objc_methname: 0x200f
-  __TEXT.__oslogstring: 0x4d1
+631.60.50.0.0
+  __TEXT.__text: 0x3fd0
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_stubs: 0x15c0
+  __TEXT.__objc_methlist: 0x354
+  __TEXT.__const: 0xb4
+  __TEXT.__objc_methname: 0x2188
+  __TEXT.__cstring: 0xeab
+  __TEXT.__objc_classname: 0x122
+  __TEXT.__oslogstring: 0x598
+  __TEXT.__objc_methtype: 0xf02
   __TEXT.__ustring: 0x27e
-  __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methtype: 0xeb1
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x1c0
-  __DATA_CONST.__got: 0x148
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__cfstring: 0x860
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__cfstring: 0x920
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x2000
-  __DATA.__objc_selrefs: 0x598
-  __DATA.__objc_ivar: 0x34
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x250
-  __DATA.__bss: 0x8
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA.__objc_const: 0x24d0
+  __DATA.__objc_selrefs: 0x5f8
+  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x2b0
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 89
-  Symbols:   107
-  CStrings:  530
+  Functions: 101
+  Symbols:   115
+  CStrings:  568
 
Symbols:
+ _OBJC_CLASS_$_CTStewieStateMonitor
+ _OBJC_CLASS_$_NSObject
+ __xpc_error_connection_invalid
+ __xpc_type_error
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _free
+ _xpc_copy_description
CStrings:
+ "\x02"
+ "\x14\x11"
+ "%!s(MISSING): CTStewieStateMonitor returned %!c(MISSING) for SOS state"
+ "%!s(MISSING): Got XPC error on listenerConnection handler: %!@(MISSING)"
+ "%!s(MISSING): Got unknown XPC event on listenerConnection handler: %!s(MISSING)"
+ "%!s(MISSING): PresenterConnection invalidated"
+ "-[AppDeletionUISOSState sosIsAvailable]"
+ "@\"CTStewieStateMonitor\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "AppDeletionUISOSState"
+ "CTStewieStateMonitorDelegate"
+ "Cellular charges may still apply."
+ "DELETION_SHEET_MESSAGES_BODY_FOURTH_SOS_NOT_AVAILABLE"
+ "DELETION_SHEET_MESSAGES_TITLE_BODY_WATCH_NOT_PAIRED"
+ "Deleting this app will limit iPhone and Apple Watch functionality."
+ "Emergency SOS via satellite, government text alerts, and other emergency text services will not be available."
+ "Government text alerts and other emergency text services will not be available."
+ "ShowArchiveOption"
+ "T@\"CTStewieStateMonitor\",R,N,V_monitor"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_internalQueue"
+ "TB,R,N,V_isSOSAvailable"
+ "TB,R,N,V_isWatchPaired"
+ "TB,R,N,V_showArchiveOption"
+ "TestSOSAvailable"
+ "WatchIsPaired"
+ "_internalQueue"
+ "_isSOSAvailable"
+ "_isWatchPaired"
+ "_monitor"
+ "_showArchiveOption"
+ "com.apple.AppDeletionUIHost.AppDeletionUICTStewieStateMonitorDelegate.internal"
+ "getState"
+ "initWithDelegate:queue:"
+ "internalQueue"
+ "isPermittedAtCurrentLocation:"
+ "isSOSAvailable"
+ "isWatchPaired"
+ "localizedStringWithFormat:"
+ "monitor"
+ "sharedInstance"
+ "showArchiveOption"
+ "sosIsAvailable"
+ "start"
+ "stateChanged:"
+ "v24@0:8@\"CTStewieState\"16"
- "\x14\x12"
- "Data charges may still apply."
- "Emergency messaging services, such as Emergency SOS via satellite, will not be available."
- "NumAppsInstalled"
- "T@\"NSNumber\",R,N,V_numAppsInstalled"
- "_numAppsInstalled"
- "numAppsInstalled"

```
