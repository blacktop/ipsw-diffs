## libCoreKE.dylib

> `/usr/lib/libCoreKE.dylib`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x1a9f57c
+  __TEXT.__text: 0x1a64718
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_stubs: 0x80
-  __TEXT.__const: 0xdd134
+  __TEXT.__const: 0xdd194
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x1f56
+  __TEXT.__cstring: 0x1f62
   __TEXT.__objc_methname: 0x5b
-  __TEXT.__unwind_info: 0xb80
-  __TEXT.__eh_frame: 0x80
+  __TEXT.__unwind_info: 0xb68
+  __TEXT.__eh_frame: 0x88
   __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x1ca60
+  __DATA_CONST.__const: 0x1cbf0
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0x5278
+  __DATA.__data: 0x5280
   __DATA.__bss: 0x71
-  __DATA.__common: 0xbb8
+  __DATA.__common: 0xbc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B35E20DD-CC41-3760-8812-83A672248B3F
-  Functions: 751
+  UUID: E0F25537-3999-3D81-A7EB-BED2FEAB542F
+  Functions: 750
   Symbols:   174
-  CStrings:  366
+  CStrings:  365
 
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unwrapped DER backup bag%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s overflow%s\n"
+ "aks_remote_reset_all_peers"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s Unwrapped DER backup bag%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s aks connection failed%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s bad 1%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s bad 2%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s fail%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n"
- "%s:%s%d{%s}:%s%s%s%s%s%u:%s overflow%s\n"
- "der_key_validate"

```
