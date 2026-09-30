## PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

-623.0.0.0.0
-  __TEXT.__text: 0x6d8
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x1e2
-  __TEXT.__oslogstring: 0x7c
-  __TEXT.__objc_methname: 0x12f
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__cfstring: 0x60
+631.0.0.0.0
+  __TEXT.__text: 0xcd8
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__objc_methlist: 0xbc
+  __TEXT.__const: 0x38
+  __TEXT.__cstring: 0x275
+  __TEXT.__objc_methname: 0x2d8
+  __TEXT.__oslogstring: 0xd8
+  __TEXT.__objc_classname: 0x1e
+  __TEXT.__objc_methtype: 0x80
+  __TEXT.__unwind_info: 0xa0
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x70
-  __DATA.__bss: 0x48
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x160
+  __DATA.__objc_selrefs: 0x100
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0x50
+  __DATA.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
+  - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6
-  Symbols:   52
-  CStrings:  34
+  Functions: 24
+  Symbols:   71
+  CStrings:  83
 
Symbols:
+ _OBJC_CLASS_$_BrightnessSystemClient
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_PowerUIDrainMonitor
+ _OBJC_METACLASS_$_NSObject
+ __objc_empty_cache
+ __os_feature_enabled_impl
+ __os_log_error_impl
+ _dispatch_once
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _dispatch_sync
+ _objc_msgSendSuper2
+ _objc_opt_new
+ _objc_release_x1
+ _objc_release_x20
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x20
+ _objc_storeStrong
- _objc_retain_x21
CStrings:
+ "\x13"
+ ".cxx_destruct"
+ "@\"BrightnessSystemClient\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSObject<OS_os_log>\""
+ "@16@0:8"
+ "B"
+ "B16@0:8"
+ "Brightness"
+ "Brightness string is null"
+ "Capping max brightness to %!l(MISSING)f"
+ "DisplayBrightness"
+ "DisplayBrightnessMax"
+ "PowerUI"
+ "PowerUIBrightnessController"
+ "Reducing brightness from %!l(MISSING)f to %!l(MISSING)f"
+ "T@\"BrightnessSystemClient\",&,N,V_bClient"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSObject<OS_os_log>\",&,N,V_log"
+ "TB,N,V_mitigationEngaged"
+ "_bClient"
+ "_log"
+ "_mitigationEngaged"
+ "_queue"
+ "ambrosia"
+ "bClient"
+ "brightnessController"
+ "com.apple.powerui"
+ "com.apple.powerui.brightnessController"
+ "copyPropertyForKey:"
+ "doubleValue"
+ "engageMitigation"
+ "i"
+ "init"
+ "log"
+ "mitigationEngaged"
+ "numberWithDouble:"
+ "objectForKeyedSubscript:"
+ "queue"
+ "resetMitigation"
+ "setBClient:"
+ "setLog:"
+ "setMitigationEngaged:"
+ "setProperty:forKey:"
+ "setQueue:"
+ "start"
+ "v16@0:8"
+ "v20@0:8B16"
+ "v24@0:8@16"

```
