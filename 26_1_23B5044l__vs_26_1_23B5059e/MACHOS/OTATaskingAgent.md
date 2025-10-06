## OTATaskingAgent

> `/usr/libexec/OTATaskingAgent`

```diff

-927.0.2.0.0
-  __TEXT.__text: 0x1188
+927.40.3.0.0
+  __TEXT.__text: 0x1468
   __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_stubs: 0x360
-  __TEXT.__objc_methlist: 0x218
-  __TEXT.__oslogstring: 0x2f5
-  __TEXT.__cstring: 0x1aa
+  __TEXT.__objc_stubs: 0x460
+  __TEXT.__objc_methlist: 0x220
+  __TEXT.__oslogstring: 0x38d
+  __TEXT.__cstring: 0x229
   __TEXT.__const: 0x28
-  __TEXT.__objc_methname: 0x3fa
+  __TEXT.__objc_methname: 0x4b3
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methtype: 0x1e8
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x270
-  __DATA.__objc_selrefs: 0x1b8
+  __DATA.__objc_selrefs: 0x1f8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8489303-A202-39F8-B01D-0CBD71F28595
-  Functions: 20
-  Symbols:   74
-  CStrings:  138
+  UUID: 954B2662-64EC-38E6-A770-2F40DCE7D831
+  Functions: 25
+  Symbols:   77
+  CStrings:  155
 
Symbols:
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_OSASystemConfiguration
CStrings:
+ "/private/var/mnt"
+ "Attempting to fetch crk from mounted data volume for DRE"
+ "Failed to fetch %@ from %@: file does not exist"
+ "Failed to fetch %@ from %@: key does not exist"
+ "defaultManager"
+ "dictionaryWithContentsOfFile:"
+ "dreCrashreporterKey"
+ "dre_error_crash_reporter_key_unavailable"
+ "fileExistsAtPath:"
+ "isInDeviceRecoveryEnvironment"
+ "objectForKeyedSubscript:"
+ "root/Library/Preferences/com.apple.osanalytics.OTATaskingAgent.plist"
+ "sharedInstance"
+ "stringByAppendingPathComponent:"

```
