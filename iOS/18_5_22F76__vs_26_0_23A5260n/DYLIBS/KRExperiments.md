## KRExperiments

> `/System/Library/PrivateFrameworks/KRExperiments.framework/KRExperiments`

```diff

-158.100.15.0.0
-  __TEXT.__text: 0x11bc
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__const: 0x78
+199.0.0.0.0
+  __TEXT.__text: 0x14c0
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__const: 0x80
   __TEXT.__cstring: 0x159
-  __TEXT.__oslogstring: 0x26e
+  __TEXT.__oslogstring: 0x390
   __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_methname: 0x2a0
-  __TEXT.__objc_stubs: 0x440
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_methname: 0x294
+  __TEXT.__objc_stubs: 0x420
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x110
-  __AUTH_CONST.__auth_got: 0x128
+  __DATA_CONST.__objc_selrefs: 0x108
+  __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__cfstring: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 26A0CCCA-EBC2-32B9-A53A-7943EC3AFD4D
-  Functions: 9
-  Symbols:   101
-  CStrings:  86
+  UUID: 6BEAD1C9-EAC8-31FC-97DA-1BCB37C1B529
+  Functions: 12
+  Symbols:   110
+  CStrings:  89
 
Symbols:
+ _CFPreferencesAppSynchronize
+ _UpdatePrewarmingDefault
+ _UpdatePrewarmingDefault.cold.1
+ _UpdatePrewarmingDefault.cold.2
+ __os_log_fault_impl
+ _kCFPreferencesCurrentApplication
+ _objc_retain_x20
- _objc_msgSend$synchronize
CStrings:
+ "UpdatePrewarmingDefault: All %d attempts at removing the default failed"
+ "UpdatePrewarmingDefault: All %d attempts of setting default failed"
+ "UpdatePrewarmingDefault: Attempt %d/%d at removing default failed, retrying"
+ "UpdatePrewarmingDefault: Attempt %d/%d at setting default failed, retrying"
- "synchronize"

```
