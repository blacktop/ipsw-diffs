## MobileGestalt

> `/System/ExclaveKit/System/Library/Frameworks/MobileGestalt.framework/MobileGestalt`

```diff

-1389.40.2.0.0
-  __TEXT.__text: 0x1510
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x1e0
-  __TEXT.__oslogstring: 0x12a
-  __TEXT.__cstring: 0xc2
+1393.60.16.0.0
+  __TEXT.__text: 0x1d34
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_methlist: 0x44
+  __TEXT.__const: 0x220
+  __TEXT.__oslogstring: 0x295
+  __TEXT.__cstring: 0x3f5
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__objc_methname: 0x1ca
+  __TEXT.__objc_methname: 0x260
   __TEXT.__objc_classname: 0x14
-  __TEXT.__objc_methtype: 0x78
-  __TEXT.__unwind_info: 0xd0
-  __DATA.__auth_got: 0x1a0
-  __DATA.__got: 0x50
-  __DATA.__const: 0x40
-  __DATA.__cfstring: 0x220
+  __TEXT.__objc_methtype: 0xe0
+  __TEXT.__unwind_info: 0xe0
+  __DATA.__auth_got: 0x1b0
+  __DATA.__got: 0x58
+  __DATA.__const: 0x70
+  __DATA.__cfstring: 0x380
   __DATA.__objc_classlist: 0x8
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x138
-  __DATA.__objc_selrefs: 0xb0
+  __DATA.__objc_const: 0x170
+  __DATA.__objc_selrefs: 0xe0
   __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x50
   __DATA.__DEVICETREE: 0x18
-  __DATA.__objc_arraydata: 0x50
-  __DATA.__objc_arrayobj: 0x90
-  __DATA.__bss: 0x10
+  __DATA.__objc_arraydata: 0x88
+  __DATA.__objc_arrayobj: 0x108
+  __DATA.__bss: 0x18
   - /System/ExclaveKit/System/Library/Frameworks/DeviceTreeKit.framework/DeviceTreeKit
   - /System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
-  Functions: 38
-  Symbols:   94
-  CStrings:  63
+  Functions: 44
+  Symbols:   98
+  CStrings:  106
 
Symbols:
+ _MobileGestalt_get_deviceSupportsAlwaysAPVoiceTrigger
+ __NSConcreteStackBlock
+ _objc_release
+ _printf
CStrings:
+ "!R"
+ "-[OS_MobileGestalt fetchCPUInfo]"
+ "@32@0:8@16@24"
+ "MGDeviceMapInit"
+ "MGDeviceTreeCopyProperty"
+ "MGDeviceTreeInit"
+ "T@\"NSDictionary\",R,N,V_deviceMap"
+ "[MobileGestalt] cpuinfo: fallback to empty info\n"
+ "[MobileGestalt] cpuinfo: missing cache size\n"
+ "[MobileGestalt] cpuinfo: missing core count node\n"
+ "[MobileGestalt] cpuinfo: missing cpu%!d(MISSING) node info\n\n"
+ "[MobileGestalt] cpuinfo: no device tree access\n"
+ "[MobileGestalt] cpuinfo: unknown cluster type for cpu%!d(MISSING): %!c(MISSING)\n\n"
+ "[MobileGestalt] cpuinfo: unsupported chip ID 0x%!x(MISSING)\n"
+ "[MobileGestalt] device map parsing error\n"
+ "[MobileGestalt] device tree init error\n"
+ "[MobileGestalt] device tree not available\n"
+ "[MobileGestalt] device tree property not found: %!s(MISSING)\n"
+ "[MobileGestalt] device_tree_root failed\n"
+ "[MobileGestalt] empty device map\n"
+ "[MobileGestalt] product not supported in device map\n"
+ "[MobileGestalt][%!s(MISSING):%!d(MISSING):%!s(MISSING)] Error: cpuinfo: missing cache size\n"
+ "[MobileGestalt][%!s(MISSING):%!d(MISSING):%!s(MISSING)] Error: cpuinfo: missing core count node\n"
+ "[MobileGestalt][%!s(MISSING):%!d(MISSING):%!s(MISSING)] Error: cpuinfo: no device tree access\n"
+ "[MobileGestalt][%!s(MISSING):%!d(MISSING):%!s(MISSING)] Error: cpuinfo: unsupported chip ID 0x%!x(MISSING)\n"
+ "[MobileGestalt][%!s(MISSING):%!d(MISSING):%!s(MISSING)] Error: device map parsing error\n"
+ "[MobileGestalt][%!s(MISSING):%!d(MISSING):%!s(MISSING)] Error: device tree init error\n"
+ "[MobileGestalt][%!s(MISSING):%!d(MISSING):%!s(MISSING)] Error: device tree not available\n"
+ "[MobileGestalt][%!s(MISSING):%!d(MISSING):%!s(MISSING)] Error: device_tree_root failed\n"
+ "[MobileGestalt][%!s(MISSING):%!d(MISSING):%!s(MISSING)] Error: product not supported in device map\n"
+ "_cpuInfo"
+ "arm-io"
+ "arrayWithObjects:count:"
+ "cluster-type"
+ "copyDeviceTreeProperty:forKey:"
+ "cpu%!d(MISSING)"
+ "cpus"
+ "dart-jpeg-h17a"
+ "deviceMap"
+ "device_map.m"
+ "device_tree.m"
+ "e-core-count"
+ "l2-cache-size"
+ "max_cpus"
+ "object.m"
+ "p-core-count"
+ "string"
+ "stringWithFormat:"
+ "subdataWithRange:"
+ "supports-always-apvoicetrigger"
+ "{OS_MobileGestalt_CPUInfo=\"family\"i\"subFamily\"i\"totalCount\"i\"count\"[2i]\"l2CacheSize\"[2i]}"
- "!\x12"
- "[MobileGestalt] device map parsing error"
- "[MobileGestalt] device tree init error"
- "[MobileGestalt] device tree not available"
- "[MobileGestalt] device tree property not found: %!s(MISSING)"
- "[MobileGestalt] device_tree_root failed"
- "[MobileGestalt] empty device map"
- "[MobileGestalt] product not supported in device map"

```
