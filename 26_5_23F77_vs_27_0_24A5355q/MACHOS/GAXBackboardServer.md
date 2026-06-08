## GAXBackboardServer

> `/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer`

```diff

-1027.14.0.0.0
-  __TEXT.__text: 0x2d678
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_stubs: 0x66e0
-  __TEXT.__objc_methlist: 0x282c
-  __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x98c
-  __TEXT.__objc_methname: 0x899c
-  __TEXT.__cstring: 0x45fe
-  __TEXT.__oslogstring: 0x3cbe
-  __TEXT.__objc_classname: 0x363
-  __TEXT.__objc_methtype: 0x1836
-  __TEXT.__unwind_info: 0xc78
-  __DATA_CONST.__auth_got: 0x5e0
-  __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0x1668
+1054.0.0.0.0
+  __TEXT.__text: 0x2a0c8
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_stubs: 0x67a0
+  __TEXT.__objc_methlist: 0x284c
+  __TEXT.__const: 0x178
+  __TEXT.__gcc_except_tab: 0x7c0
+  __TEXT.__objc_methname: 0x8a42
+  __TEXT.__cstring: 0x462e
+  __TEXT.__oslogstring: 0x3dbe
+  __TEXT.__objc_classname: 0x33f
+  __TEXT.__objc_methtype: 0x1839
+  __TEXT.__unwind_info: 0xa48
+  __DATA_CONST.__const: 0x1620
   __DATA_CONST.__cfstring: 0x3620
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_intobj: 0x240
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__linkguard: 0x18
-  __DATA.__objc_const: 0x2a80
-  __DATA.__objc_selrefs: 0x1e38
-  __DATA.__objc_ivar: 0x19c
+  __DATA_CONST.__auth_got: 0x628
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x2ab0
+  __DATA.__objc_selrefs: 0x1e68
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x588
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5BC5EAE-96EB-340B-8292-638518C5F6D1
-  Functions: 1062
-  Symbols:   566
-  CStrings:  2656
+  UUID: 9BDFE87B-EE70-3D76-9569-38BDBCC66F61
+  Functions: 950
+  Symbols:   581
+  CStrings:  2669
 
Symbols:
+ _BKSHIDServicesLockOrientation
+ _BKSHIDServicesUnlockOrientation
+ _GAXBundleIdentifierGameOverlayUI
+ _GAXSafariViewServiceIdentifier
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSURL
+ _SBSDisplayLayoutElementFloatingDockIdentifier
+ __CFBundleCopyBundleURLForExecutableURL
+ ___chkstk_darwin
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _proc_pidpath
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[AXSpringBoardServer(GAXAdditions) gaxDidChangeMode:shouldAcquireLockScreenAssertion:gaxState:appInterfaceOrientation:]"
+ "Action button press blocked. Mode: %i"
+ "Failed to resolve bundle identifier for GAX client with pid %d"
+ "Failed to resolve bundle identifier for active app notification with pid %d"
+ "Guided Access locking orientation to %ld"
+ "Guided Access unlocking orientation"
+ "Ignoring mode change request: ASAM evaluation in progress"
+ "TB,N,V_isOrientationLocked"
+ "_isOrientationLocked"
+ "_updateOrientationLockForMode:"
+ "auditToken"
+ "com.apple.GameOverlayUI"
+ "fileURLWithPath:"
+ "gaxDidChangeMode:shouldAcquireLockScreenAssertion:gaxState:appInterfaceOrientation:"
+ "initWithBytes:length:encoding:"
+ "initWithPath:"
+ "isOrientationLocked"
+ "path"
+ "setIsOrientationLocked:"
+ "v60@0:8I16B20{?=IIIIIIb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24q52"
- "-[AXSpringBoardServer(GAXAdditions) gaxDidChangeMode:shouldAcquireLockScreenAssertion:gaxState:]"
- "com.apple.springboard.floating-dock"
- "decodePropertyListForKey:"
- "gaxDidChangeMode:shouldAcquireLockScreenAssertion:gaxState:"
- "performAsynchronousWritingBlock:"
- "setting ignored touch regions in screen coordinates:\n%@"
- "v52@0:8I16B20{?=IIIIIIb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24"

```
