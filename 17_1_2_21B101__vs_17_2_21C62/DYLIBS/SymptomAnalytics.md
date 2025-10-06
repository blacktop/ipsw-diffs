## SymptomAnalytics

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics`

```diff

-1848.42.1.0.0
-  __TEXT.__text: 0x8848
+1848.60.8.0.0
+  __TEXT.__text: 0x8f40
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x8e8
+  __TEXT.__objc_methlist: 0x900
   __TEXT.__cstring: 0xec6
   __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__const: 0x10
-  __TEXT.__oslogstring: 0xd1c
-  __TEXT.__unwind_info: 0x284
+  __TEXT.__const: 0x18
+  __TEXT.__oslogstring: 0xe12
+  __TEXT.__unwind_info: 0x290
   __TEXT.__objc_classname: 0x21e
-  __TEXT.__objc_methname: 0x2c34
-  __TEXT.__objc_methtype: 0xa04
-  __TEXT.__objc_stubs: 0x1940
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__objc_methname: 0x2d48
+  __TEXT.__objc_methtype: 0xa06
+  __TEXT.__objc_stubs: 0x1a40
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x618
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x20f0
-  __DATA_CONST.__objc_selrefs: 0x878
+  __DATA_CONST.__objc_const: 0x2170
+  __DATA_CONST.__objc_selrefs: 0x8c8
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__cfstring: 0x1940
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x200
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x180
+  __DATA.__objc_classrefs: 0x188
   __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_ivar: 0x90
   __DATA.__data: 0x1f8
   __DATA_DIRTY.__const: 0x20
   __DATA_DIRTY.__objc_const: 0x8b8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96962418-CA66-34DE-93E7-972296F9609D
-  Functions: 189
-  Symbols:   1098
-  CStrings:  1150
+  UUID: 17DE8801-F80F-3DB5-9357-0172E75F85D4
+  Functions: 191
+  Symbols:   1115
+  CStrings:  1172
 
Symbols:
+ -[AnalyticsWorkspace currentDBSizeInBytes]
+ -[AnalyticsWorkspace fileSystemSizeInBytes]
+ _NSFileSystemSize
+ _OBJC_CLASS_$_NSDate
+ _OBJC_IVAR_$_AnalyticsWorkspace._currentDBSizeInBytes
+ _OBJC_IVAR_$_AnalyticsWorkspace._fileSystemSizeInBytes
+ _OBJC_IVAR_$_AnalyticsWorkspace._lastDBSizeUpdateTimestamp
+ _objc_msgSend$URL
+ _objc_msgSend$attributesOfFileSystemForPath:error:
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$fileSize
+ _objc_msgSend$isFileURL
+ _objc_msgSend$path
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$unsignedLongLongValue
CStrings:
+ "\x01\x12I"
+ "Analytics Workspace path = %@, file size = %llu"
+ "Error retrieving file path, storeURL: %@"
+ "Error retrieving file size: %@"
+ "Error retrieving file system size: %@"
+ "File System Size = %llu"
+ "Persistent store is nil."
+ "TQ,R,N"
+ "Total DB size = %llu, last update = %f"
+ "URL"
+ "_currentDBSizeInBytes"
+ "_fileSystemSizeInBytes"
+ "_lastDBSizeUpdateTimestamp"
+ "attributesOfFileSystemForPath:error:"
+ "attributesOfItemAtPath:error:"
+ "currentDBSizeInBytes"
+ "d"
+ "fileSize"
+ "fileSystemSizeInBytes"
+ "isFileURL"
+ "path"
+ "timeIntervalSinceReferenceDate"
+ "unsignedLongLongValue"
- "\x01\x12\x19"

```
