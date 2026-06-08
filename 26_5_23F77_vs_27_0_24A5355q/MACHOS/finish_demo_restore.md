## finish_demo_restore

> `/usr/libexec/finish_demo_restore`

```diff

-220.100.2.0.0
-  __TEXT.__text: 0x3ca0
+225.0.0.0.0
+  __TEXT.__text: 0x3d68
   __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x1f4
+  __TEXT.__objc_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x1fc
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__cstring: 0xe29
-  __TEXT.__objc_methname: 0x837
+  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__cstring: 0xf99
+  __TEXT.__objc_methname: 0x8c1
   __TEXT.__oslogstring: 0x16
-  __TEXT.__objc_classname: 0x4c
+  __TEXT.__objc_classname: 0x49
   __TEXT.__objc_methtype: 0x100
   __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0xb80
+  __DATA_CONST.__cfstring: 0xce0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__got: 0xd0
   __DATA.__objc_const: 0x318
-  __DATA.__objc_selrefs: 0x2c0
+  __DATA.__objc_selrefs: 0x2f0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x140
   __DATA.__bss: 0x40

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE601483-2DBD-3324-8B01-C32136DCD876
-  Functions: 62
-  Symbols:   108
-  CStrings:  313
+  UUID: 1932167A-C818-3068-988D-58E49DD12CEA
+  Functions: 66
+  Symbols:   110
+  CStrings:  342
 
Symbols:
+ _OBJC_CLASS_$_NSMutableDictionary
+ ___kCFBooleanFalse
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x28
CStrings:
+ "-[FDRContentInstaller revokeStoreDemoMode]"
+ "/private/var/mobile/Library/Preferences/com.apple.demo-settings.plist"
+ "Can't load demo config from %@"
+ "Can't overwrite demo config to %@"
+ "Demo plist %@ doesn't exist"
+ "Failed to finish install demo contents"
+ "NO"
+ "Read %@ = %@"
+ "StoreDemoMode"
+ "StoreDemoMode has been revoked due to install failure"
+ "Try to revoke StoreDemoMode ..."
+ "YES"
+ "boolValue"
+ "dictionaryWithContentsOfFile:"
+ "objectForKeyedSubscript:"
+ "revokeStoreDemoMode"
+ "setObject:forKeyedSubscript:"
+ "writeToFile:atomically:"

```
