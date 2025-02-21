## PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

-640.0.0.0.0
-  __TEXT.__text: 0xcdc
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0xbc
-  __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x27a
-  __TEXT.__objc_methname: 0x2ba
-  __TEXT.__oslogstring: 0x13a
-  __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methtype: 0x80
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x118
-  __DATA_CONST.__cfstring: 0xe0
-  __DATA_CONST.__objc_classlist: 0x8
+651.0.0.0.0
+  __TEXT.__text: 0x73c
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__objc_stubs: 0x200
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x1f3
+  __TEXT.__oslogstring: 0x7c
+  __TEXT.__objc_methname: 0x142
+  __TEXT.__unwind_info: 0x70
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x160
-  __DATA.__objc_selrefs: 0xf0
-  __DATA.__objc_ivar: 0x10
-  __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x58
+  __DATA.__objc_selrefs: 0x80
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
-  - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 24
-  Symbols:   72
-  CStrings:  83
+  Functions: 6
+  Symbols:   57
+  CStrings:  38
 
Symbols:
+ _OBJC_CLASS_$_PowerUICECUtilities
+ _OBJC_CLASS_$_PowerUIDemoCECManager
- _OBJC_CLASS_$_BrightnessSystemClient
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_CLASS_$_NSObject
- _OBJC_METACLASS_$_NSObject
- ___kCFBooleanFalse
- ___kCFBooleanTrue
- __objc_empty_cache
- __os_log_error_impl
- _dispatch_once
- _dispatch_queue_attr_make_with_autorelease_frequency
- _dispatch_queue_create
- _dispatch_sync
- _objc_msgSendSuper2
- _objc_opt_new
- _objc_release_x1
- _objc_retainAutoreleaseReturnValue
- _objc_storeStrong
CStrings:
+ "isDemoDevice"
- "\x13"
- ".cxx_destruct"
- "@\"BrightnessSystemClient\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@16@0:8"
- "B"
- "B16@0:8"
- "Brightness"
- "Brightness string is null"
- "DisplayBrightness"
- "EcoMode"
- "EcoModeFactorUpdate"
- "Failed: Setting EcodMode to %@"
- "Failed: Setting brightness reduction factor to %@"
- "PowerUIBrightnessController"
- "Success: Setting EcodMode to %@"
- "Success: Setting brightness reduction factor to %@"
- "T@\"BrightnessSystemClient\",&,N,V_bClient"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_os_log>\",&,N,V_log"
- "TB,N,V_mitigationEngaged"
- "_bClient"
- "_log"
- "_mitigationEngaged"
- "_queue"
- "bClient"
- "brightnessController"
- "com.apple.powerui"
- "com.apple.powerui.brightnessController"
- "copyPropertyForKey:"
- "engageMitigation"
- "init"
- "log"
- "mitigationEngaged"
- "objectForKeyedSubscript:"
- "queue"
- "resetMitigation"
- "setBClient:"
- "setLog:"
- "setMitigationEngaged:"
- "setProperty:forKey:"
- "setQueue:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"

```
