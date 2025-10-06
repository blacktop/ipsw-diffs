## OSAServicesClient

> `/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient`

```diff

-927.0.2.0.0
-  __TEXT.__text: 0x40e4
-  __TEXT.__auth_stubs: 0x3e0
+927.40.3.0.0
+  __TEXT.__text: 0x4134
+  __TEXT.__auth_stubs: 0x3f0
   __TEXT.__objc_methlist: 0x680
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x54

   __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x200
+  __AUTH_CONST.__auth_got: 0x208
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x1208
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x300
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A091D215-A731-351B-825C-896226E8BE71
+  UUID: 14D8321A-262B-3CB7-B0FB-B2DEE804AF7B
   Functions: 135
-  Symbols:   630
+  Symbols:   632
   CStrings:  309
 
Symbols:
+ _DREIsRunningInDeviceRecoveryEnvironment
+ _queryKey:.forceIPC
Functions:
~ ___30-[OSAServicesClient queryKey:]_block_invoke : 116 -> 160
~ ___30-[OSAServicesClient queryKey:]_block_invoke_2 : 308 -> 328
~ ___30-[OSAServicesClient queryKey:]_block_invoke_3 : 108 -> 124

```
