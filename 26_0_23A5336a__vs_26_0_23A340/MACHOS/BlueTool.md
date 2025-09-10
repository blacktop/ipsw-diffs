## BlueTool

> `/usr/sbin/BlueTool`

```diff

 1.41.1.1.0
-  __TEXT.__text: 0x4eaa0
-  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__text: 0x4fcac
+  __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__init_offsets: 0x590
-  __TEXT.__const: 0x47c478
-  __TEXT.__cstring: 0xea93
-  __TEXT.__oslogstring: 0x4673
+  __TEXT.__init_offsets: 0x594
+  __TEXT.__const: 0x47c560
+  __TEXT.__cstring: 0xeb44
+  __TEXT.__oslogstring: 0x4844
   __TEXT.__objc_methname: 0x1c0
-  __TEXT.__unwind_info: 0x1250
-  __DATA_CONST.__auth_got: 0x5c8
+  __TEXT.__unwind_info: 0x12b0
+  __DATA_CONST.__auth_got: 0x610
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x69a8
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x6ca8
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0xb8
   __DATA.__data: 0x990
-  __DATA.__bss: 0x1551
+  __DATA.__bss: 0x1559
   __DATA.__common: 0x4c2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/AirshipCentauriHelper.framework/AirshipCentauriHelper
+  - /System/Library/PrivateFrameworks/CentauriController.framework/CentauriController
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /usr/lib/libFDR.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 94080DAC-95E6-3962-8188-8A4B19D826BF
-  Functions: 2555
-  Symbols:   217
-  CStrings:  1960
+  UUID: FCC08C0B-E848-33DB-9A5A-766485CC06D2
+  Functions: 2603
+  Symbols:   226
+  CStrings:  1976
 
Symbols:
+ _CentauriControllerCreateWithParameters
+ _CentauriControllerFree
+ _CentauriControllerReset
+ _airship_ch_interface_close
+ _airship_ch_interface_create
+ _airship_ch_interface_destroy
+ _airship_ch_interface_open
+ _airship_ch_interface_read
+ _airship_ch_interface_write
CStrings:
+ "-D           - Open apple_pcie transport\n"
+ "0667328f8eee92ec1aac5f57a7da9d65822ac600"
+ "21:35:12"
+ "75530fa34f42fb82d43cb54a7b36bd645f5abc19"
+ "APPLE PCIE transport and ready to call apple_pcie_function_level_reset from %s"
+ "Apple PCIe failed to create controller handle 0x%08x\n"
+ "Apple PCIe failed to load controller framework\n"
+ "Apple PCIe failed to reset beta 0x%08x\n"
+ "Device is opened and ready to close it for transport APPLE PCIE from %s"
+ "HCI transport is APPLE PCIE and ready to open device from %s"
+ "PROXIMA"
+ "aci_proxima_init.hcd"
+ "airship failed to open hci: 0x%08x\n"
+ "bt-transport-override=9"
+ "failed to create airship\n"
+ "failed to load airship framework\n"
+ "using airship\n"
- "21:56:10"

```
