## WebKit

> `/System/Library/Frameworks/WebKit.framework/WebKit`

```diff

-622.2.11.10.4
-  __TEXT.__text: 0x119c700
+622.2.11.10.8
+  __TEXT.__text: 0x119ca30
   __TEXT.__auth_stubs: 0x19430
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x1a384
+  __TEXT.__objc_methlist: 0x1a39c
   __TEXT.__const: 0x5bc8
   __TEXT.__dlsym_cstr: 0x757
   __TEXT.__getClass_cstr: 0xa41

   __TEXT.__swift_as_ret: 0x11c
   __TEXT.__swift5_assocty: 0x1b0
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x72260
+  __TEXT.__gcc_except_tab: 0x7229c
   __TEXT.__oslogstring: 0x4896c
   __TEXT.__ustring: 0xd40
-  __TEXT.__unwind_info: 0x2dd98
+  __TEXT.__unwind_info: 0x2ddb8
   __TEXT.__eh_frame: 0x22c0
   __TEXT.__objc_classname: 0x33a1
-  __TEXT.__objc_methname: 0x4a73a
+  __TEXT.__objc_methname: 0x4a772
   __TEXT.__objc_methtype: 0x3b21d
-  __TEXT.__objc_stubs: 0x2bf00
+  __TEXT.__objc_stubs: 0x2bf40
   __DATA_CONST.__got: 0x2198
   __DATA_CONST.__const: 0x1f9f0
   __DATA_CONST.__objc_classlist: 0xc60
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x450
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10a78
+  __DATA_CONST.__objc_selrefs: 0x10a88
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x9b8
   __DATA_CONST.__objc_arraydata: 0x638
   __AUTH_CONST.__auth_got: 0xca30
-  __AUTH_CONST.__const: 0x63a18
+  __AUTH_CONST.__const: 0x63a40
   __AUTH_CONST.__cfstring: 0x142a0
-  __AUTH_CONST.__objc_const: 0x28a98
+  __AUTH_CONST.__objc_const: 0x28ab8
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x5c50
   __AUTH.__data: 0x6e8
-  __DATA.__objc_ivar: 0xffc
+  __DATA.__objc_ivar: 0x1000
   __DATA.__data: 0x3b3c
   __DATA.__bss: 0x2970
   __DATA.__common: 0xf88

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F8CFE682-15C9-3DDE-944A-29E8B0A8656B
-  Functions: 71710
-  Symbols:   194552
-  CStrings:  33004
+  UUID: F2321104-8C05-34EF-BB9E-5F9FCEAB779B
+  Functions: 71715
+  Symbols:   194568
+  CStrings:  33007
 
Symbols:
+ -[WKFullScreenWindowController _cancelWatchdogTimer]
+ -[WKFullScreenWindowController _startWatchdogTimer]
+ _OBJC_IVAR_$_WKFullScreenWindowController._watchdogTimer
+ __ZN3WTF6Detail15CallableWrapperIZ51-[WKFullScreenWindowController _startWatchdogTimer]E3$_5vJEE4callEv
+ __ZN3WTF6Detail15CallableWrapperIZ51-[WKFullScreenWindowController _startWatchdogTimer]E3$_5vJEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZ51-[WKFullScreenWindowController _startWatchdogTimer]E3$_5vJEED1Ev
+ __ZN3WTF6Detail15CallableWrapperIZ55-[WKFullScreenWindowController didExitPictureInPicture]E4$_10vJbEE4callEb
+ __ZN3WTF6Detail15CallableWrapperIZ55-[WKFullScreenWindowController didExitPictureInPicture]E4$_10vJbEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZ55-[WKFullScreenWindowController didExitPictureInPicture]E4$_10vJbEED1Ev
+ __ZN3WTF6Detail15CallableWrapperIZ57-[WKFullScreenWindowController _completedExitFullScreen:]E3$_8vJEE4callEv
+ __ZN3WTF6Detail15CallableWrapperIZ57-[WKFullScreenWindowController _completedExitFullScreen:]E3$_8vJEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZ57-[WKFullScreenWindowController _completedExitFullScreen:]E3$_8vJEED1Ev
+ __ZN3WTF6Detail15CallableWrapperIZ63-[WKFullScreenWindowController placeholderWillMoveToSuperview:]E3$_9vJEE4callEv
+ __ZN3WTF6Detail15CallableWrapperIZ63-[WKFullScreenWindowController placeholderWillMoveToSuperview:]E3$_9vJEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZ63-[WKFullScreenWindowController placeholderWillMoveToSuperview:]E3$_9vJEED1Ev
+ __ZN3WTF6Detail15CallableWrapperIZ65-[WKFullScreenWindowController _startToDismissFullscreenChanged:]E4$_11vJEE4callEv
+ __ZN3WTF6Detail15CallableWrapperIZ65-[WKFullScreenWindowController _startToDismissFullscreenChanged:]E4$_11vJEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZ65-[WKFullScreenWindowController _startToDismissFullscreenChanged:]E4$_11vJEED1Ev
+ __ZN3WTF6Detail15CallableWrapperIZ66-[WKFullScreenWindowController enterFullScreen:completionHandler:]E3$_7vJP16UIViewControllerP7NSErrorEE4callES4_S6_
+ __ZN3WTF6Detail15CallableWrapperIZ66-[WKFullScreenWindowController enterFullScreen:completionHandler:]E3$_7vJP16UIViewControllerP7NSErrorEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZ66-[WKFullScreenWindowController enterFullScreen:completionHandler:]E3$_7vJP16UIViewControllerP7NSErrorEED1Ev
+ __ZN3WTF6Detail15CallableWrapperIZZ57-[WKFullScreenWindowController _completedExitFullScreen:]ENK3$_8clEvEUlbE_vJbEE4callEb
+ __ZN3WTF6Detail15CallableWrapperIZZ57-[WKFullScreenWindowController _completedExitFullScreen:]ENK3$_8clEvEUlbE_vJbEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZZ57-[WKFullScreenWindowController _completedExitFullScreen:]ENK3$_8clEvEUlbE_vJbEED1Ev
+ __ZTVN3WTF6Detail15CallableWrapperIZ51-[WKFullScreenWindowController _startWatchdogTimer]E3$_5vJEEE
+ __ZTVN3WTF6Detail15CallableWrapperIZ55-[WKFullScreenWindowController didExitPictureInPicture]E4$_10vJbEEE
+ __ZTVN3WTF6Detail15CallableWrapperIZ57-[WKFullScreenWindowController _completedExitFullScreen:]E3$_8vJEEE
+ __ZTVN3WTF6Detail15CallableWrapperIZ63-[WKFullScreenWindowController placeholderWillMoveToSuperview:]E3$_9vJEEE
+ __ZTVN3WTF6Detail15CallableWrapperIZ65-[WKFullScreenWindowController _startToDismissFullscreenChanged:]E4$_11vJEEE
+ __ZTVN3WTF6Detail15CallableWrapperIZ66-[WKFullScreenWindowController enterFullScreen:completionHandler:]E3$_7vJP16UIViewControllerP7NSErrorEEE
+ __ZTVN3WTF6Detail15CallableWrapperIZZ57-[WKFullScreenWindowController _completedExitFullScreen:]ENK3$_8clEvEUlbE_vJbEEE
+ __ZZN3WTF8BlockPtrIFvvEE12fromCallableIZ65-[WKFullScreenWindowController _dismissFullscreenViewController:]E3$_6EES2_T_E10descriptor
+ __ZZN3WTF8BlockPtrIFvvEE12fromCallableIZ65-[WKFullScreenWindowController _dismissFullscreenViewController:]E3$_6EES2_T_ENUlPKvE_8__invokeES7_
+ __ZZN3WTF8BlockPtrIFvvEE12fromCallableIZ65-[WKFullScreenWindowController _dismissFullscreenViewController:]E3$_6EES2_T_ENUlPvE_8__invokeES6_
+ _objc_msgSend$_cancelWatchdogTimer
+ _objc_msgSend$_startWatchdogTimer
- __ZN3WTF6Detail15CallableWrapperIZ55-[WKFullScreenWindowController didExitPictureInPicture]E3$_9vJbEE4callEb
- __ZN3WTF6Detail15CallableWrapperIZ55-[WKFullScreenWindowController didExitPictureInPicture]E3$_9vJbEED0Ev
- __ZN3WTF6Detail15CallableWrapperIZ55-[WKFullScreenWindowController didExitPictureInPicture]E3$_9vJbEED1Ev
- __ZN3WTF6Detail15CallableWrapperIZ57-[WKFullScreenWindowController _completedExitFullScreen:]E3$_7vJEE4callEv
- __ZN3WTF6Detail15CallableWrapperIZ57-[WKFullScreenWindowController _completedExitFullScreen:]E3$_7vJEED0Ev
- __ZN3WTF6Detail15CallableWrapperIZ57-[WKFullScreenWindowController _completedExitFullScreen:]E3$_7vJEED1Ev
- __ZN3WTF6Detail15CallableWrapperIZ63-[WKFullScreenWindowController placeholderWillMoveToSuperview:]E3$_8vJEE4callEv
- __ZN3WTF6Detail15CallableWrapperIZ63-[WKFullScreenWindowController placeholderWillMoveToSuperview:]E3$_8vJEED0Ev
- __ZN3WTF6Detail15CallableWrapperIZ63-[WKFullScreenWindowController placeholderWillMoveToSuperview:]E3$_8vJEED1Ev
- __ZN3WTF6Detail15CallableWrapperIZ65-[WKFullScreenWindowController _startToDismissFullscreenChanged:]E4$_10vJEE4callEv
- __ZN3WTF6Detail15CallableWrapperIZ65-[WKFullScreenWindowController _startToDismissFullscreenChanged:]E4$_10vJEED0Ev
- __ZN3WTF6Detail15CallableWrapperIZ65-[WKFullScreenWindowController _startToDismissFullscreenChanged:]E4$_10vJEED1Ev
- __ZN3WTF6Detail15CallableWrapperIZ66-[WKFullScreenWindowController enterFullScreen:completionHandler:]E3$_6vJP16UIViewControllerP7NSErrorEE4callES4_S6_
- __ZN3WTF6Detail15CallableWrapperIZ66-[WKFullScreenWindowController enterFullScreen:completionHandler:]E3$_6vJP16UIViewControllerP7NSErrorEED0Ev
- __ZN3WTF6Detail15CallableWrapperIZ66-[WKFullScreenWindowController enterFullScreen:completionHandler:]E3$_6vJP16UIViewControllerP7NSErrorEED1Ev
- __ZN3WTF6Detail15CallableWrapperIZZ57-[WKFullScreenWindowController _completedExitFullScreen:]ENK3$_7clEvEUlbE_vJbEE4callEb
- __ZN3WTF6Detail15CallableWrapperIZZ57-[WKFullScreenWindowController _completedExitFullScreen:]ENK3$_7clEvEUlbE_vJbEED0Ev
- __ZN3WTF6Detail15CallableWrapperIZZ57-[WKFullScreenWindowController _completedExitFullScreen:]ENK3$_7clEvEUlbE_vJbEED1Ev
- __ZTVN3WTF6Detail15CallableWrapperIZ55-[WKFullScreenWindowController didExitPictureInPicture]E3$_9vJbEEE
- __ZTVN3WTF6Detail15CallableWrapperIZ57-[WKFullScreenWindowController _completedExitFullScreen:]E3$_7vJEEE
- __ZTVN3WTF6Detail15CallableWrapperIZ63-[WKFullScreenWindowController placeholderWillMoveToSuperview:]E3$_8vJEEE
- __ZTVN3WTF6Detail15CallableWrapperIZ65-[WKFullScreenWindowController _startToDismissFullscreenChanged:]E4$_10vJEEE
- __ZTVN3WTF6Detail15CallableWrapperIZ66-[WKFullScreenWindowController enterFullScreen:completionHandler:]E3$_6vJP16UIViewControllerP7NSErrorEEE
- __ZTVN3WTF6Detail15CallableWrapperIZZ57-[WKFullScreenWindowController _completedExitFullScreen:]ENK3$_7clEvEUlbE_vJbEEE
- __ZZN3WTF8BlockPtrIFvvEE12fromCallableIZ65-[WKFullScreenWindowController _dismissFullscreenViewController:]E3$_5EES2_T_E10descriptor
- __ZZN3WTF8BlockPtrIFvvEE12fromCallableIZ65-[WKFullScreenWindowController _dismissFullscreenViewController:]E3$_5EES2_T_ENUlPKvE_8__invokeES7_
- __ZZN3WTF8BlockPtrIFvvEE12fromCallableIZ65-[WKFullScreenWindowController _dismissFullscreenViewController:]E3$_5EES2_T_ENUlPvE_8__invokeES6_
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedArithmetic.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CompactVariantOperations.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/RefPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/RetainPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/WeakRef.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/4~CAtBugAdX2ypK3woS13W0YBGfMX4uuy1xhucdh4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "_cancelWatchdogTimer"
+ "_startWatchdogTimer"
+ "_watchdogTimer"
+ "\xf0\xf0\xf0\xf0A"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedArithmetic.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CompactVariantOperations.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/RefPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/RetainPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/WeakRef.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/4~CAMZugAJYsfAnKialVrvuIa2tUbnzeG_qOU32dc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "\xf0\xf0\xf0\xf01"

```
