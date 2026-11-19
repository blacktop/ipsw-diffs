## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/Versions/A/CoreRepairCore`

```diff

-1307.1.2.0.0
-  __TEXT.__text: 0x7ec48
-  __TEXT.__objc_methlist: 0x440c
-  __TEXT.__const: 0x866
-  __TEXT.__cstring: 0x6152
-  __TEXT.__oslogstring: 0x9495
-  __TEXT.__gcc_except_tab: 0x15e0
-  __TEXT.__unwind_info: 0x1330
+1307.40.66.0.0
+  __TEXT.__text: 0x7fcc0
+  __TEXT.__objc_methlist: 0x44c4
+  __TEXT.__const: 0x886
+  __TEXT.__cstring: 0x61c1
+  __TEXT.__oslogstring: 0x9652
+  __TEXT.__gcc_except_tab: 0x1610
+  __TEXT.__unwind_info: 0x1378
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2848
+  __DATA_CONST.__objc_selrefs: 0x2898
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x630
-  __DATA_CONST.__got: 0x518
-  __AUTH_CONST.__const: 0x11a0
-  __AUTH_CONST.__cfstring: 0x7300
-  __AUTH_CONST.__objc_const: 0x6428
+  __DATA_CONST.__got: 0x530
+  __AUTH_CONST.__const: 0x11e0
+  __AUTH_CONST.__cfstring: 0x7380
+  __AUTH_CONST.__objc_const: 0x64a8
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x450
-  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH_CONST.__auth_got: 0xa68
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_ivar: 0x3ac
+  __DATA.__objc_ivar: 0x3b4
   __DATA.__data: 0x658
-  __DATA.__bss: 0x160
+  __DATA.__bss: 0x180
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x180

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2463
-  Symbols:   587
-  CStrings:  2207
+  Functions: 2490
+  Symbols:   594
+  CStrings:  2218
 
Symbols:
+ _NSCalendarIdentifierGregorian
+ _NSClassFromString
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NSCalendar
+ _kCRNetworkRetryDelaySeconds
+ _kCRNetworkRetryMaxAttempts
+ _kCRNetworkRetryWindowSeconds
CStrings:
+ "%s exit: challenge: %@, outSignature: %@, outDeviceNonce: %@, typeInfo: %@, outError: %@"
+ "(null)"
+ "(nullptr)"
+ "+[CRUtils shouldRetryNetworkError:attempt:startedAtClock:]"
+ "CRShipModeBatteryClient: ignoring proxyProvider seam outside a test process"
+ "CRShipModeServerNotifier: ignoring proxyProvider seam outside a test process; opening a real XPC connection"
+ "Set sensor power failed: %d"
+ "Set sensor power to %d successfully"
+ "XCTestCase"
+ "[%s] retry window closed after %{public}.0fs (attempt %{public}lu/%{public}lu); failing instead of retrying"
+ "kCFErrorDomainCFNetwork"
```
