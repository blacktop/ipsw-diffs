## cdpd

> `/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd`

```diff

-410.1.0.0.0
-  __TEXT.__text: 0x214
-  __TEXT.__auth_stubs: 0xd0
-  __TEXT.__objc_stubs: 0xe0
+412.0.0.0.0
+  __TEXT.__text: 0x320
+  __TEXT.__auth_stubs: 0x120
+  __TEXT.__objc_stubs: 0x140
   __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0xd
-  __TEXT.__objc_methname: 0x5e
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x70
-  __DATA_CONST.__got: 0x48
+  __TEXT.__oslogstring: 0xac
+  __TEXT.__cstring: 0x17
+  __TEXT.__objc_methname: 0xb1
+  __TEXT.__unwind_info: 0x68
+  __DATA_CONST.__auth_got: 0x98
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x38
+  __DATA.__objc_selrefs: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP
   - /System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D559679-0A88-3A98-9B88-00765585B624
-  Functions: 2
-  Symbols:   25
-  CStrings:  8
+  UUID: 17AE2159-8D1B-30C3-BCE6-2AB0CFA84AD0
+  Functions: 3
+  Symbols:   35
+  CStrings:  14
 
Symbols:
+ _OBJC_CLASS_$_CDPDBootSessionIDProvider
+ _OBJC_CLASS_$_CDPDFirstUnlockObserver
+ _OBJC_CLASS_$_CDPLocalDevice
+ _OBJC_CLASS_$_NSUserDefaults
+ ___CFConstantStringClassReference
+ __os_log_error_impl
+ _objc_alloc
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
- _objc_release
CStrings:
+ "Could not initialize AppleAccount UserDefaults suite. FirstUnlockObserver relies on this suite. Manatee may not be available for a while after initial boot..."
+ "bootSessionUUID"
+ "com.apple.appleaccount"
+ "initWithSuiteName:"
+ "initWithUserDefaults:localDevice:bootSessionID:"

```
