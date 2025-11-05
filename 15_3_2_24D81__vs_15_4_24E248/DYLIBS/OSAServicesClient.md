## OSAServicesClient

> `/System/Library/PrivateFrameworks/OSAServicesClient.framework/Versions/A/OSAServicesClient`

```diff

-727.80.2.0.0
-  __TEXT.__text: 0x46f4
+758.100.43.0.0
+  __TEXT.__text: 0x4748
   __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0x46c
+  __TEXT.__objc_methlist: 0x680
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x54
   __TEXT.__cstring: 0x457
   __TEXT.__oslogstring: 0x495
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x228
   __TEXT.__objc_classname: 0x150
   __TEXT.__objc_methname: 0xc9e
   __TEXT.__objc_methtype: 0x47c

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x318
+  __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x168
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x15b0
+  __AUTH_CONST.__objc_const: 0x1208
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x300

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C12892A-8561-345C-964A-164E40476E7D
-  Functions: 140
-  Symbols:   483
+  UUID: 2DE3D82E-5C18-322A-B563-C6F4DE3603AF
+  Functions: 147
+  Symbols:   490
   CStrings:  309
 
Symbols:
+ +[OSADiagnosticMonitor sharedMonitor].cold.1
+ +[OSADiagnosticMonitorClient sharedClient].cold.1
+ +[OSAServicesClient sharedClient].cold.1
+ -[OSAServicesClient awdKey].cold.1
+ -[OSAServicesClient crashreporterKey].cold.1
+ -[OSAServicesClient queryKey:].cold.2
+ DiagnosticMonitorLog.cold.1

```
